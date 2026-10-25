"""Tahap 18: Diagnosis KMA v2 (fidelitas benchmark, ablation, kendala aktif, konvergensi).

Modul ini TIDAK mengubah perilaku optimizer. Isinya:
1. Fungsi benchmark standar (Sphere, Rastrigin, Rosenbrock) dan versi tergeser.
2. `KMAVariant`: salinan KMA (Suyanto dkk., 2022; Proposal Pers. 2.25-2.32) dengan flag
   diagnostik. Semua flag mati = perilaku `KomodoMlipirOptimizer` bit-identik (diuji).
3. `EvalRecorder`: pembungkus evaluator yang mencatat jarak kandidat mentah ke hasil
   proyeksi, pelanggaran kendala, dan kelayakan tiap evaluasi.
4. Eksekusi tugas (benchmark, portofolio, timing, profil) yang dipanggil skrip 18.
5. Analisis read-only atas 360 run utama di `results/runs/`.
"""

from __future__ import annotations

import contextlib
import cProfile
import hashlib
import json
import os
import pstats
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple
from unittest import mock

import numpy as np
import pandas as pd
import yaml

import mccar_kma.optimizers.base as base_mod
import mccar_kma.optimizers.pso as pso_mod
from mccar_kma.model.constraints import (
    LB_DJPPR,
    LB_FREE,
    UB_DJPPR,
    UB_FREE,
    project_weights as _REAL_PROJECT,
    project_weights_batch as _REAL_PROJECT_BATCH,
)
from mccar_kma.optimizers.base import BaseOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer, compute_group_sizes
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator

FORBIDDEN_OUTPUT_DIRS = ("results/runs", "results/tables", "results/figures", "results/sensitivity/limits")
FUNCTION_ORDER = ("sphere", "rastrigin", "rosenbrock")


# ==============================================================================
# 0. Utilitas konfigurasi & metadata
# ==============================================================================

def load_config(path: Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def config_hash(cfg: Dict[str, Any]) -> str:
    """Hash SHA-256 blok konfigurasi yang memengaruhi hasil diagnosis."""
    sub = {k: cfg.get(k) for k in ("kma_diagnosis", "algorithms", "risk", "optimization", "scenarios")}
    return hashlib.sha256(json.dumps(sub, sort_keys=True, default=str).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_safe_output_dir(out_dir: Path, base_dir: Path) -> Path:
    """Menolak folder keluaran yang beririsan dengan hasil utama atau Tahap 17."""
    resolved = out_dir.resolve()
    for forbidden in FORBIDDEN_OUTPUT_DIRS:
        f = (base_dir / forbidden).resolve()
        if resolved == f or f in resolved.parents or resolved in f.parents:
            raise ValueError(f"Folder keluaran tidak aman: {out_dir} (beririsan dengan {forbidden})")
    return resolved


def atomic_write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=1, default=_json_default)
    os.replace(tmp, path)


def _json_default(o: Any) -> Any:
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    raise TypeError(f"Tidak bisa serialisasi {type(o)}")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ==============================================================================
# 1. Fungsi benchmark (Suyanto dkk., 2022, Tabel 6: F1, F5, F9)
# ==============================================================================

def sphere(z: np.ndarray) -> float:
    """F1 Sphere: f(z) = sum z_i^2, optimum f(0) = 0."""
    return float(np.sum(z * z))


def rastrigin(z: np.ndarray) -> float:
    """F9 Rastrigin: f(z) = sum (z_i^2 - 10 cos(2 pi z_i) + 10), optimum f(0) = 0."""
    return float(np.sum(z * z - 10.0 * np.cos(2.0 * np.pi * z) + 10.0))


def rosenbrock(z: np.ndarray) -> float:
    """F5 Rosenbrock: f(z) = sum 100 (z_{i+1} - z_i^2)^2 + (z_i - 1)^2, optimum f(1) = 0."""
    return float(np.sum(100.0 * (z[1:] - z[:-1] ** 2) ** 2 + (z[:-1] - 1.0) ** 2))


BENCHMARK_FUNCS = {"sphere": sphere, "rastrigin": rastrigin, "rosenbrock": rosenbrock}


def make_shift(function: str, dim: int, lb: float, ub: float, cfg_bench: Dict[str, Any]) -> np.ndarray:
    """Vektor optimum tergeser o ~ U(frac*lb, frac*ub)^D dengan Generator ber-seed."""
    idx = FUNCTION_ORDER.index(function)
    seed = int(cfg_bench["shift_seed_base"]) + 100 * idx + int(dim)
    frac = float(cfg_bench["shift_domain_fraction"])
    return np.random.default_rng(seed).uniform(frac * lb, frac * ub, size=dim)


class BenchmarkProblem:
    """Fungsi benchmark, opsional tergeser sehingga optimum berada di vektor `shift`."""

    def __init__(self, function: str, dim: int, shift: Optional[np.ndarray] = None) -> None:
        self.function = function
        self.dim = int(dim)
        self.func = BENCHMARK_FUNCS[function]
        self.shift = None if shift is None else np.asarray(shift, dtype=float)

    def optimum(self) -> np.ndarray:
        if self.shift is not None:
            return self.shift.copy()
        return np.ones(self.dim) if self.function == "rosenbrock" else np.zeros(self.dim)

    def __call__(self, x: np.ndarray) -> float:
        x = np.asarray(x, dtype=float)
        if self.shift is None:
            return self.func(x)
        z = x - self.shift
        if self.function == "rosenbrock":
            z = z + 1.0
        return self.func(z)


class BenchmarkEvaluator:
    """Evaluator benchmark tanpa kendala (selalu layak); kompatibel dgn BaseOptimizer."""

    def __init__(self, problem: BenchmarkProblem) -> None:
        self.problem = problem

    def evaluate(self, x: np.ndarray, apply_penalty: bool = True) -> Dict[str, Any]:
        val = self.problem(x)
        return {"mean_cost": val, "f_val": val, "ccar": 0.0, "j_mccar": 0.0,
                "v_J": 0.0, "v_R": 0.0, "is_feasible": True}


def _box_clip(w: np.ndarray, lb: np.ndarray, ub: np.ndarray, **_: Any) -> np.ndarray:
    return np.clip(np.asarray(w, dtype=float), lb, ub)


@contextlib.contextmanager
def box_only_projection() -> Iterator[None]:
    """Mengganti proyeksi simpleks+kotak dengan clipping kotak saja, terlingkup.

    Hanya untuk benchmark tanpa kendala Σw=1. Patch dipulihkan saat keluar konteks.
    """
    with mock.patch.object(base_mod, "project_weights", _box_clip), \
            mock.patch.object(base_mod, "project_weights_batch", _box_clip), \
            mock.patch.object(pso_mod, "project_weights", _box_clip):
        yield


# ==============================================================================
# 2. KMAVariant (Suyanto dkk., 2022, Algoritma 1, Pers. 1-10; Proposal Pers. 2.25-2.32)
# ==============================================================================

MLIPIR_RATE_2_MODES = ("half", "low", "high")

VARIANT_FLAGS: Dict[str, Dict[str, Any]] = {
    "default": {},
    "paper_pool": {"pool_selection": True},
    "sync": {"synchronous": True},
    "paper_mlipir": {"paper_mlipir": True},
    "paper_q": {"paper_q": True},
    "paper_all": {"pool_selection": True, "synchronous": True, "paper_mlipir": True, "paper_q": True},
    "one_phase_n5": {"one_phase": "phase1"},
    "one_phase_n200": {"one_phase": "phase2"},
    "d2_low": {"mlipir_rate_2_mode": "low"},
    "d2_high": {"mlipir_rate_2_mode": "high"},
    "deb_rules": {"deb_rules": True},
    "norm_q": {"normalize_q": True},
}


class KMAVariant(KomodoMlipirOptimizer):
    """KMA dua fase dengan flag diagnostik (semua mati = identik dgn kma.py).

    Flag:
    - pool_selection (K1): Big Male lama ∪ baru diurutkan, q terbaik bertahan (Algoritma 1).
    - synchronous (K2): langkah Big Male dihitung dari posisi awal generasi (snapshot).
    - paper_mlipir (K3): tiap Big Male yang diikuti memilih 1..(m-1) dimensi (Pers. 8).
    - paper_q (K4): q = floor(p * n) (Pers. 1, salah cetak "(p-1)n" dikoreksi).
    - deb_rules: perbandingan layak-dulu (Deb, 2000) menggantikan urutan fitness penalti.
    - normalize_q: langkah Big Male dibagi banyak interaksi (diagnostik, bukan usulan).
    - one_phase: None | "phase1" (n=5, d1 sepanjang anggaran) | "phase2" (n=200 adaptif saja).
    - mlipir_rate_2_mode: "half" (0,5) | "low" (1/D) | "high" ((D-1)/D).
    - instrument: catat statistik per generasi ke `self.gen_log`.
    """

    def __init__(
        self,
        pool_selection: bool = False,
        synchronous: bool = False,
        paper_mlipir: bool = False,
        paper_q: bool = False,
        deb_rules: bool = False,
        normalize_q: bool = False,
        one_phase: Optional[str] = None,
        mlipir_rate_2_mode: str = "half",
        instrument: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if one_phase not in (None, "phase1", "phase2"):
            raise ValueError(f"one_phase tidak dikenal: {one_phase}")
        if mlipir_rate_2_mode not in MLIPIR_RATE_2_MODES:
            raise ValueError(f"mlipir_rate_2_mode tidak dikenal: {mlipir_rate_2_mode}")
        self.pool_selection = bool(pool_selection)
        self.synchronous = bool(synchronous)
        self.paper_mlipir = bool(paper_mlipir)
        self.paper_q = bool(paper_q)
        self.deb_rules = bool(deb_rules)
        self.normalize_q = bool(normalize_q)
        self.one_phase = one_phase
        self.mlipir_rate_2_mode = mlipir_rate_2_mode
        self.instrument = bool(instrument)
        self.gen_log: List[Dict[str, Any]] = []
        self.phase_1_end_eval: Optional[int] = None
        self._phase = 1
        self._gen = 0

    # ------------------------------------------------------------------
    def _mlipir_rate_2(self, dim: int) -> float:
        if self.mlipir_rate_2_mode == "low":
            return 1.0 / float(dim)
        if self.mlipir_rate_2_mode == "high":
            return (dim - 1.0) / float(dim)
        return 0.5

    def _group_sizes(self, n_pop: int) -> Tuple[int, int, int]:
        """Pers. 1-2 (Suyanto) / Pers. 2.25 (proposal)."""
        if not self.paper_q or n_pop < 5:
            return compute_group_sizes(n_pop, self.p_bm)
        q = int(np.floor(self.p_bm * n_pop))
        n_bm = min(max(q, 2), n_pop - 3)
        return n_bm, 1, n_pop - n_bm - 1

    def _key(self, res: Dict[str, Any]) -> Tuple[float, float]:
        if self.deb_rules:
            if res["is_feasible"]:
                return (0.0, float(res["mean_cost"]))
            return (1.0, float(res["v_J"]) + float(res["v_R"]))
        return (float(res["f_val"]), 0.0)

    def _better(self, a: Dict[str, Any], b: Dict[str, Any]) -> bool:
        if self.deb_rules:
            return self._key(a) < self._key(b)
        return a["f_val"] < b["f_val"]

    def _sort_population(self, pop, results):
        if not self.deb_rules:
            return super()._sort_population(pop, results)
        if not results:
            return pop, results
        n = min(len(pop), len(results))
        order = sorted(range(n), key=lambda i: self._key(results[i]))
        return [pop[i] for i in order], [results[i] for i in order]

    # ------------------------------------------------------------------
    def run(self, evaluator, lb, ub, budget=25000, rng=None):
        """Salinan `KomodoMlipirOptimizer.run` + opsi satu fase dan d2."""
        start_time = time.perf_counter()
        gen_rng = self._init_run(budget=budget, lb=lb, ub=ub, rng=rng)
        dim = len(self._lb)
        bound_range = np.abs(self._ub - self._lb)
        self.gen_log = []
        self._gen = 0
        self.phase_1_end_eval = None

        total_nominal = self.phase_1_budget + self.phase_2_budget
        frac_phase_1 = self.phase_1_budget / total_nominal if total_nominal > 0 else 0.2
        target_phase_1_budget = min(self.phase_1_budget, int(np.round(frac_phase_1 * budget)))
        if self.one_phase == "phase1":
            target_phase_1_budget = budget
        run_phase_1 = self.one_phase != "phase2"

        results_1: List[Dict[str, Any]] = []
        best_phase_1_w = None
        if run_phase_1:
            self._phase = 1
            mlipir_rate_1 = (dim - 1.0) / float(dim)
            raw_init_1 = gen_rng.uniform(self._lb, self._ub, size=(self.phase_1_n_pop, dim))
            results_1 = self.evaluate_population(raw_init_1, evaluator)
            pop_1 = [r["w"] for r in results_1]
            pop_1, results_1 = self._sort_population(pop_1, results_1)
            while self.budget.evaluations < target_phase_1_budget and not self.budget.is_exhausted:
                pop_1, results_1 = self._evolve_generation(
                    pop=pop_1, results=results_1, mlipir_rate=mlipir_rate_1,
                    bound_range=bound_range, evaluator=evaluator, rng=gen_rng,
                )
            best_phase_1_w = pop_1[0].copy()
        self.phase_1_end_eval = int(self.budget.evaluations)

        if not self.budget.is_exhausted:
            self._phase = 2
            mlipir_rate_2 = self._mlipir_rate_2(dim)
            rem_budget = self.budget.remaining
            init_n_pop_2 = min(self.phase_2_n_pop_init, max(self.phase_2_n_pop_min, rem_budget))
            if run_phase_1:
                pop_2: List[np.ndarray] = [best_phase_1_w]
                results_2: List[Dict[str, Any]] = [results_1[0]]
                num_new = max(0, init_n_pop_2 - 1)
            else:
                pop_2, results_2 = [], []
                num_new = init_n_pop_2
            if num_new > 0 and self.budget.remaining > 0:
                raw_init_2 = gen_rng.uniform(self._lb, self._ub, size=(num_new, dim))
                results_new = self.evaluate_population(raw_init_2, evaluator)
                pop_2.extend([r["w"] for r in results_new])
                results_2.extend(results_new)
            pop_2, results_2 = self._sort_population(pop_2, results_2)
            fitness_history: List[float] = [results_2[0]["f_val"]] if results_2 else []

            while not self.budget.is_exhausted:
                pop_2, results_2 = self._evolve_generation(
                    pop=pop_2, results=results_2, mlipir_rate=mlipir_rate_2,
                    bound_range=bound_range, evaluator=evaluator, rng=gen_rng,
                )
                if not results_2:
                    break
                fitness_history.append(results_2[0]["f_val"])
                if len(fitness_history) >= 3 and not self.budget.is_exhausted:
                    pop_2, results_2 = self._adapt_population_size(
                        pop=pop_2, results=results_2, fitness_history=fitness_history,
                        bound_range=bound_range, evaluator=evaluator, rng=gen_rng,
                    )

        elapsed = time.perf_counter() - start_time
        meta = {
            "algorithm": "KMAVariant",
            "dim": dim, "budget": budget,
            "flags": {
                "pool_selection": self.pool_selection, "synchronous": self.synchronous,
                "paper_mlipir": self.paper_mlipir, "paper_q": self.paper_q,
                "deb_rules": self.deb_rules, "normalize_q": self.normalize_q,
                "one_phase": self.one_phase, "mlipir_rate_2_mode": self.mlipir_rate_2_mode,
            },
            "phase_1_end_eval": self.phase_1_end_eval,
        }
        return self._build_result(elapsed_seconds=elapsed, metadata=meta)

    # ------------------------------------------------------------------
    def _paper_mlipir_mask(self, rng: np.random.Generator, dim: int, rate: float) -> np.ndarray:
        """Pers. 8: pilih dimensi dgn peluang d, dibatasi 1..(m-1) dimensi (rejection)."""
        while True:
            mask = rng.uniform(0.0, 1.0, size=dim) < rate
            k = int(mask.sum())
            if dim == 1 or 1 <= k <= dim - 1:
                return mask

    def _evolve_generation(self, pop, results, mlipir_rate, bound_range, evaluator, rng):
        """Satu generasi KMA (Pers. 2.26-2.32) dengan flag diagnostik."""
        n_pop = len(pop)
        if n_pop < 3 or self.budget.is_exhausted:
            return pop, results

        dim = len(self._lb)
        n_bm, n_female, n_sm = self._group_sizes(n_pop)
        range_norm = float(np.linalg.norm(bound_range)) or 1.0
        step_norms: List[float] = []
        bm_attempts = 0
        bm_accepted = 0

        # 1. Big Males (HILE, Pers. 2.26-2.27)
        q = n_bm if self.q_interactions is None else min(self.q_interactions, n_bm)
        if self.synchronous:
            ref_pop = [p.copy() for p in pop[:n_bm]]
            ref_res = list(results[:n_bm])
        new_bm: List[Dict[str, Any]] = []
        for i in range(n_bm):
            if self.budget.is_exhausted:
                break
            k_i = ref_pop[i] if self.synchronous else pop[i]
            res_i = ref_res[i] if self.synchronous else results[i]
            w_ij_sum = np.zeros(dim, dtype=float)
            n_inter = 0
            for j in range(q):
                if j == i:
                    continue
                k_j = ref_pop[j] if self.synchronous else pop[j]
                res_j = ref_res[j] if self.synchronous else results[j]
                r1 = rng.uniform(0.0, 1.0)
                r2 = rng.uniform(0.0, 1.0)
                if self._better(res_j, res_i) or r2 < 0.5:
                    u_ij = r1 * (k_j - k_i)
                else:
                    u_ij = r1 * (k_i - k_j)
                w_ij_sum += u_ij
                n_inter += 1
            if self.normalize_q and n_inter > 1:
                w_ij_sum = w_ij_sum / float(n_inter)
            if self.instrument:
                step_norms.append(float(np.linalg.norm(w_ij_sum)) / range_norm)

            k_i_new = k_i + w_ij_sum
            new_res = self.evaluate_candidate(k_i_new, evaluator)
            bm_attempts += 1
            if new_res is None:
                continue
            if self.pool_selection:
                new_bm.append(new_res)
            elif self._better(new_res, results[i]):
                pop[i] = new_res["w"]
                results[i] = new_res
                bm_accepted += 1

        if self.pool_selection and new_bm:
            pool = [(results[i], False) for i in range(n_bm)] + [(r, True) for r in new_bm]
            order = sorted(range(len(pool)), key=lambda t: self._key(pool[t][0]))[:n_bm]
            survivors = [pool[t] for t in order]
            bm_accepted = sum(1 for _, is_new in survivors if is_new)
            for slot, (res, _) in enumerate(survivors):
                pop[slot] = res["w"]
                results[slot] = res

        # 2. Female (MIME, Pers. 2.28-2.30)
        female_mode = None
        female_accepted = False
        female_idx = n_bm
        if female_idx < n_pop and not self.budget.is_exhausted:
            k_female = pop[female_idx]
            k_winner = pop[0]
            p_choice = rng.uniform(0.0, 1.0)
            if p_choice < self.p_mating:
                female_mode = "mating"
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_off1 = r_l * k_female + (1.0 - r_l) * k_winner
                k_off2 = r_l * k_winner + (1.0 - r_l) * k_female
                res1 = self.evaluate_candidate(k_off1, evaluator)
                res2 = self.evaluate_candidate(k_off2, evaluator)
                best_res = None
                if res1 is not None and res2 is not None:
                    best_res = res1 if self._better(res1, res2) else res2
                elif res1 is not None:
                    best_res = res1
                elif res2 is not None:
                    best_res = res2
                if best_res is not None and self._better(best_res, results[female_idx]):
                    pop[female_idx] = best_res["w"]
                    results[female_idx] = best_res
                    female_accepted = True
            else:
                female_mode = "parthenogenesis"
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_par = k_female + (2.0 * r_l - 1.0) * self.gamma * bound_range
                res_par = self.evaluate_candidate(k_par, evaluator)
                if res_par is not None and self._better(res_par, results[female_idx]):
                    pop[female_idx] = res_par["w"]
                    results[female_idx] = res_par
                    female_accepted = True

        # 3. Small Males (LIHE / mlipir, Pers. 2.31-2.32)
        start_sm = n_bm + n_female
        sm_moved = 0
        for i in range(start_sm, n_pop):
            if self.budget.is_exhausted:
                break
            k_i = pop[i]
            k_i_new = k_i.copy()
            for j in range(n_bm):
                k_j = pop[j]
                if self.paper_mlipir:
                    mask = self._paper_mlipir_mask(rng, dim, mlipir_rate)
                    r1v = rng.uniform(0.0, 1.0, size=dim)
                    k_i_new += np.where(mask, r1v * (k_j - k_i), 0.0)
                else:
                    for l in range(dim):
                        r2 = rng.uniform(0.0, 1.0)
                        if r2 < mlipir_rate:
                            r1 = rng.uniform(0.0, 1.0)
                            k_i_new[l] += r1 * (k_j[l] - k_i[l])
            new_sm_res = self.evaluate_candidate(k_i_new, evaluator)
            if new_sm_res is not None:
                pop[i] = new_sm_res["w"]
                results[i] = new_sm_res
                sm_moved += 1

        pop, results = self._sort_population(pop, results)

        if self.instrument:
            self._gen += 1
            sn = np.asarray(step_norms) if step_norms else np.array([np.nan])
            self.gen_log.append({
                "phase": self._phase, "generation": self._gen, "n_pop": n_pop, "n_bm": n_bm,
                "bm_attempts": bm_attempts, "bm_accepted": bm_accepted,
                "bm_step_norm_mean": float(np.nanmean(sn)), "bm_step_norm_median": float(np.nanmedian(sn)),
                "bm_step_norm_max": float(np.nanmax(sn)),
                "female_mode": female_mode, "female_accepted": female_accepted,
                "sm_moved": sm_moved, "eval_end": int(self.budget.evaluations),
                "best_f": float(results[0]["f_val"]) if results else float("nan"),
            })
        return pop, results


def make_optimizer(name: str, instrument: bool = False) -> BaseOptimizer:
    """`kma`/`ga`/`pso` = kelas asli (default = Tabel 3.1); `kma_<varian>` = KMAVariant."""
    if name == "kma" and not instrument:
        return KomodoMlipirOptimizer()
    if name == "kma":
        return KMAVariant(instrument=True)
    if name == "ga":
        return GeneticAlgorithmOptimizer()
    if name == "pso":
        return ParticleSwarmOptimizer()
    if name.startswith("kma_"):
        variant = name[len("kma_"):]
        if variant not in VARIANT_FLAGS:
            raise ValueError(f"Varian KMA tidak dikenal: {variant}")
        return KMAVariant(instrument=instrument, **VARIANT_FLAGS[variant])
    raise ValueError(f"Algoritma tidak dikenal: {name}")


# ==============================================================================
# 3. Perekam evaluasi (H5): jarak proyeksi, pelanggaran, kelayakan
# ==============================================================================

class EvalRecorder:
    """Pembungkus evaluator portofolio yang mencatat statistik per evaluasi.

    Dipakai bersama konteks `recording_projection(recorder)` agar kandidat mentah (sebelum
    proyeksi clip+normalisasi, `constraints.project_weights`) ikut tercatat. PSO
    memproyeksikan sendiri (pso.py) sebelum `evaluate_population` memproyeksikan ulang
    (idempoten); statistik PSO diambil dari proyeksi pertama.
    """

    def __init__(self, evaluator: PortfolioEvaluator, bound_tol: float) -> None:
        self.inner = evaluator
        self.bound_tol = float(bound_tol)
        self.queue: deque = deque()
        self.pending: deque = deque()
        self.rows: List[Tuple[float, ...]] = []

    def _stats(self, raw: np.ndarray, proj: np.ndarray, lb: np.ndarray, ub: np.ndarray) -> Tuple[float, int, int, int]:
        raw = np.asarray(raw, dtype=float)
        dist = float(np.linalg.norm(raw - proj))
        n_bound = int(np.sum((np.abs(proj - lb) <= self.bound_tol) | (np.abs(proj - ub) <= self.bound_tol)))
        fallback = int(float(np.sum(np.clip(raw, lb, ub))) <= 0.0)
        out_box = int(bool(np.any(raw < lb - self.bound_tol) or np.any(raw > ub + self.bound_tol)))
        return dist, n_bound, fallback, out_box

    def project_single(self, w, lb, ub, **kw):
        wp = _REAL_PROJECT(w, lb, ub, **kw)
        self.queue.append(self._stats(w, wp, lb, ub))
        return wp

    def project_batch(self, W, lb, ub, **kw):
        Wp = _REAL_PROJECT_BATCH(W, lb, ub, **kw)
        n = len(Wp)
        if len(self.pending) >= n:
            for _ in range(n):
                self.queue.append(self.pending.popleft())
        else:
            self.pending.clear()
            for i in range(n):
                self.queue.append(self._stats(W[i], Wp[i], lb, ub))
        return Wp

    def project_pso(self, w, lb, ub, **kw):
        wp = _REAL_PROJECT(w, lb, ub, **kw)
        self.pending.append(self._stats(w, wp, lb, ub))
        return wp

    def _record(self, mean_cost, j_mccar, ccar, v_J, v_R, feasible, f_val) -> None:
        stats = self.queue.popleft() if self.queue else (np.nan, -1, -1, -1)
        self.rows.append((*stats, mean_cost, j_mccar, ccar, v_J, v_R, float(feasible), f_val))

    def evaluate(self, w, apply_penalty: bool = True):
        res = self.inner.evaluate(w, apply_penalty=apply_penalty)
        if apply_penalty:
            self._record(res["mean_cost"], res["j_mccar"], res["ccar"], res["v_J"], res["v_R"],
                         res["is_feasible"], res["f_val"])
        return res

    def evaluate_batch(self, W, apply_penalty: bool = True):
        res = self.inner.evaluate_batch(W, apply_penalty=apply_penalty)
        if apply_penalty:
            for i in range(len(W)):
                self._record(float(res["mean_cost"][i]), float(res["j_mccar"][i]), float(res["ccar"][i]),
                             float(res["v_J"][i]), float(res["v_R"][i]), bool(res["is_feasible"][i]),
                             float(res["f_val"][i]))
        return res

    def to_frame(self) -> pd.DataFrame:
        cols = ["proj_dist", "n_at_bound", "fallback_mid", "raw_out_box", "mean_cost", "j_mccar",
                "ccar", "v_J", "v_R", "feasible", "f_val"]
        df = pd.DataFrame(self.rows, columns=cols)
        df.insert(0, "evaluation", np.arange(1, len(df) + 1))
        return df


@contextlib.contextmanager
def recording_projection(recorder: EvalRecorder) -> Iterator[None]:
    with mock.patch.object(base_mod, "project_weights", recorder.project_single), \
            mock.patch.object(base_mod, "project_weights_batch", recorder.project_batch), \
            mock.patch.object(pso_mod, "project_weights", recorder.project_pso):
        yield


def summarize_eval_blocks(df: pd.DataFrame, eta: float, eps_tol: float, block_size: int,
                          dist_tol: float, near_rel: float) -> pd.DataFrame:
    """Ringkasan per blok evaluasi (default 250) untuk uji H5."""
    if df.empty:
        return pd.DataFrame()
    feas = df["feasible"].to_numpy() > 0.5
    cost = df["mean_cost"].to_numpy()
    j = df["j_mccar"].to_numpy()
    rel_slack = (eta - j) / eta
    cost_feas = np.where(feas, cost, np.inf)
    run_min = np.minimum.accumulate(cost_feas)
    prev = np.concatenate(([np.inf], run_min[:-1]))
    new_best = cost_feas < prev
    best_idx = np.maximum.accumulate(np.where(new_best, np.arange(len(df)), -1))

    block = (df["evaluation"].to_numpy() - 1) // block_size
    out = []
    for b in np.unique(block):
        m = block == b
        end = int(np.max(np.where(m)[0]))
        bi = int(best_idx[end])
        out.append({
            "block": int(b), "eval_end": int(df["evaluation"].iloc[end]), "n": int(m.sum()),
            "frac_projected": float(np.mean(df["proj_dist"].to_numpy()[m] > dist_tol)),
            "mean_proj_dist": float(np.nanmean(df["proj_dist"].to_numpy()[m])),
            "median_proj_dist": float(np.nanmedian(df["proj_dist"].to_numpy()[m])),
            "mean_n_at_bound": float(np.mean(df["n_at_bound"].to_numpy()[m])),
            "frac_fallback_mid": float(np.mean(df["fallback_mid"].to_numpy()[m] > 0)),
            "frac_raw_out_box": float(np.mean(df["raw_out_box"].to_numpy()[m] > 0)),
            "frac_vJ_pos": float(np.mean(df["v_J"].to_numpy()[m] > eps_tol)),
            "frac_vR_pos": float(np.mean(df["v_R"].to_numpy()[m] > eps_tol)),
            "frac_feasible": float(np.mean(feas[m])),
            "frac_near_boundary": float(np.mean(feas[m] & (rel_slack[m] <= near_rel))),
            "best_feasible_cost": float(run_min[end]) if np.isfinite(run_min[end]) else np.nan,
            "best_rel_slack_J": float(rel_slack[bi]) if bi >= 0 else np.nan,
        })
    return pd.DataFrame(out)


# ==============================================================================
# 4. Tugas portofolio (ablation, instrumentasi, timing, profil)
# ==============================================================================

_BANK_CACHE: Dict[str, Any] = {}


def split_config_id(config_id: str) -> Tuple[str, str]:
    cost_def, ctype = config_id.split("_", 1)
    return cost_def, ctype


def bounds_for(constraint_type: str) -> Tuple[np.ndarray, np.ndarray]:
    if constraint_type == "djppr":
        return LB_DJPPR.copy(), UB_DJPPR.copy()
    if constraint_type == "free":
        return LB_FREE.copy(), UB_FREE.copy()
    raise ValueError(constraint_type)


def bank_paths(base_dir: Path, cfg: Dict[str, Any]) -> Tuple[Path, Path]:
    seed = int(cfg["scenarios"]["train_seed"])
    n = int(cfg["scenarios"]["n_scenarios"])
    proc = base_dir / "data" / "processed"
    return proc / f"bank_train_seed{seed}_N{n}.npz", proc / f"risk_limits_bank_train_seed{seed}_N{n}.json"


def make_portfolio_evaluator(bank_path: str, limits_path: str, cost_def: str) -> Tuple[PortfolioEvaluator, float, float]:
    """Evaluator identik dgn `experiments.runner.execute_single_run` (bank & batas sama)."""
    key = f"{bank_path}|{cost_def}"
    if key not in _BANK_CACHE:
        cost = np.load(bank_path)[f"cost_{cost_def}"]
        with open(limits_path, "r", encoding="utf-8") as f:
            lim = json.load(f)[cost_def]
        _BANK_CACHE[key] = (cost, float(lim["tau"]), float(lim["eta"]))
    cost, tau, eta = _BANK_CACHE[key]
    return PortfolioEvaluator(cost_matrix=cost, tau=tau, eta=eta), tau, eta


class TimingEvaluator:
    """Pencatat waktu dinding tiap kelipatan `block` evaluasi (overhead diabaikan)."""

    def __init__(self, inner: PortfolioEvaluator, block: int) -> None:
        self.inner = inner
        self.block = int(block)
        self.count = 0
        self.t0 = time.perf_counter()
        self.marks: List[Tuple[int, float]] = []

    def _tick(self, n: int) -> None:
        before = self.count
        self.count += n
        k = before // self.block + 1
        while k * self.block <= self.count:
            self.marks.append((k * self.block, time.perf_counter() - self.t0))
            k += 1

    def evaluate(self, w, apply_penalty: bool = True):
        res = self.inner.evaluate(w, apply_penalty=apply_penalty)
        if apply_penalty:
            self._tick(1)
        return res

    def evaluate_batch(self, W, apply_penalty: bool = True):
        res = self.inner.evaluate_batch(W, apply_penalty=apply_penalty)
        if apply_penalty:
            self._tick(len(W))
        return res


def _checkpoint_costs(history: Sequence[Dict[str, Any]], checkpoints: Sequence[int]) -> Dict[str, Optional[float]]:
    by_eval = {int(h["evaluation"]): h.get("best_cost") for h in history}
    return {f"cost_{c}": (None if by_eval.get(int(c)) is None else float(by_eval[int(c)])) for c in checkpoints}


def run_portfolio_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Satu run portofolio. kind ∈ {ablation, instrument, timing}. Hasil ditulis JSON atomik."""
    out_path = Path(task["out_path"])
    if task.get("resume", True) and out_path.exists():
        with open(out_path, "r", encoding="utf-8") as f:
            return json.load(f)

    cost_def, ctype = split_config_id(task["config_id"])
    evaluator, tau, eta = make_portfolio_evaluator(task["bank_path"], task["limits_path"], cost_def)
    lb, ub = bounds_for(ctype)
    kind = task["kind"]
    opt = make_optimizer(task["algo"], instrument=(kind == "instrument"))

    recorder = None
    timer = None
    t0 = time.perf_counter()
    if kind == "instrument":
        recorder = EvalRecorder(evaluator, bound_tol=task["bound_tol"])
        with recording_projection(recorder):
            res = opt.run(evaluator=recorder, lb=lb, ub=ub, budget=task["budget"], rng=task["seed"])
    elif kind == "timing":
        timer = TimingEvaluator(evaluator, block=task["block_size"])
        res = opt.run(evaluator=timer, lb=lb, ub=ub, budget=task["budget"], rng=task["seed"])
    else:
        res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=task["budget"], rng=task["seed"])
    elapsed = time.perf_counter() - t0

    final = evaluator.evaluate(res.best_w)
    payload: Dict[str, Any] = {
        "kind": kind, "config_id": task["config_id"], "algo": task["algo"], "rep": task["rep"],
        "seed": task["seed"], "budget": task["budget"], "evaluations": res.evaluations_used,
        "is_feasible": bool(res.is_feasible and final["is_feasible"]),
        "best_cost": float(final["mean_cost"]), "best_fitness": float(res.best_fitness),
        "ccar": float(final["ccar"]), "j_mccar": float(final["j_mccar"]),
        "eta": eta, "tau": tau,
        "slack_J_abs": eta - float(final["j_mccar"]), "slack_J_rel": (eta - float(final["j_mccar"])) / eta,
        "slack_R_abs": tau - float(final["ccar"]), "slack_R_rel": (tau - float(final["ccar"])) / tau,
        "best_w": [float(x) for x in res.best_w],
        "time_seconds": round(elapsed, 4),
        "phase_1_end_eval": getattr(opt, "phase_1_end_eval", None),
        "checkpoints": _checkpoint_costs(res.convergence_history, task["checkpoints"]),
        "convergence": [[int(h["evaluation"]), h["best_cost"]] for h in res.convergence_history],
        "meta": {"date": now_iso(), "config_hash": task["config_hash"], "data_version": task["data_version"]},
    }
    if kind == "instrument":
        blocks = summarize_eval_blocks(recorder.to_frame(), eta=eta, eps_tol=task["eps_tol"],
                                       block_size=task["block_size"], dist_tol=task["dist_tol"],
                                       near_rel=task["near_rel"])
        payload["blocks"] = blocks.to_dict(orient="list")
        if isinstance(opt, KMAVariant):
            payload["gen_log"] = opt.gen_log
    if kind == "timing":
        payload["timing_marks"] = timer.marks
    atomic_write_json(out_path, payload)
    return payload


def run_profile_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Profil cProfile 1 run (1 worker) → pembagian waktu evaluator / proyeksi / RNG / sisa (H6)."""
    cost_def, ctype = split_config_id(task["config_id"])
    evaluator, _, _ = make_portfolio_evaluator(task["bank_path"], task["limits_path"], cost_def)
    lb, ub = bounds_for(ctype)
    opt = make_optimizer(task["algo"])
    prof = cProfile.Profile()
    t0 = time.perf_counter()
    prof.enable()
    opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=task["budget"], rng=task["seed"])
    prof.disable()
    wall = time.perf_counter() - t0
    st = pstats.Stats(prof)
    total = float(st.total_tt)
    t_eval = t_proj = t_rng = 0.0
    for (fname, _, func), (_, _, tt, ct, _) in st.stats.items():  # type: ignore[attr-defined]
        norm = fname.replace("\\", "/")
        if norm.endswith("risk/evaluator.py") and func in ("evaluate", "evaluate_batch"):
            t_eval += ct
        elif norm.endswith("model/constraints.py") and func in ("project_weights", "project_weights_batch"):
            t_proj += ct
        elif "numpy.random._generator.Generator" in func:
            t_rng += tt
    return {
        "config_id": task["config_id"], "algo": task["algo"], "seed": task["seed"],
        "wall_seconds_profiled": wall, "profiled_total_seconds": total,
        "evaluator_seconds": t_eval, "projection_seconds": t_proj, "rng_seconds": t_rng,
        "other_seconds": max(0.0, total - t_eval - t_proj - t_rng),
    }


# ==============================================================================
# 5. Tugas benchmark
# ==============================================================================

def run_benchmark_task(task: Dict[str, Any]) -> Dict[str, Any]:
    out_path = Path(task["out_path"])
    if task.get("resume", True) and out_path.exists():
        with open(out_path, "r", encoding="utf-8") as f:
            return json.load(f)
    fn, dim = task["function"], int(task["dim"])
    lo, hi = task["domain"]
    lb, ub = np.full(dim, float(lo)), np.full(dim, float(hi))
    shift = None if task["shift"] is None else np.asarray(task["shift"], dtype=float)
    problem = BenchmarkProblem(fn, dim, shift)
    opt = make_optimizer(task["algo"])
    t0 = time.perf_counter()
    with box_only_projection():
        res = opt.run(evaluator=BenchmarkEvaluator(problem), lb=lb, ub=ub, budget=task["budget"], rng=task["seed"])
    elapsed = time.perf_counter() - t0
    payload = {
        "set": task["set"], "function": fn, "dim": dim, "shifted": shift is not None, "algo": task["algo"],
        "rep": task["rep"], "seed": task["seed"], "budget": task["budget"],
        "evaluations": res.evaluations_used, "best_fitness": float(res.best_fitness),
        "dist_to_optimum": float(np.linalg.norm(np.asarray(res.best_w) - problem.optimum())),
        "time_seconds": round(elapsed, 4),
        "phase_1_end_eval": getattr(opt, "phase_1_end_eval", None),
        "checkpoints": _checkpoint_costs(res.convergence_history, task["checkpoints"]),
        "meta": {"date": now_iso(), "config_hash": task["config_hash"]},
    }
    atomic_write_json(out_path, payload)
    return payload


# ==============================================================================
# 6. Analisis read-only 360 run utama
# ==============================================================================

def load_main_runs(base_dir: Path) -> Tuple[pd.DataFrame, Dict[Tuple[str, str], np.ndarray]]:
    """Membaca semua `results/runs/**/*.json` (read-only) → tabel run + kurva biaya per 250 eval."""
    rows = []
    curves: Dict[Tuple[str, str], List[np.ndarray]] = {}
    for p in sorted((base_dir / "results" / "runs").rglob("*.json")):
        with open(p, "r", encoding="utf-8") as f:
            d = json.load(f)
        hist = d.get("convergence_history", [])
        ev = np.array([h["evaluation"] for h in hist], dtype=float)
        cs = np.array([np.nan if h["best_cost"] is None else h["best_cost"] for h in hist], dtype=float)
        rows.append({
            "config_id": d["config_id"], "algo": d["algo"], "rep": d["rep"], "seed": d["seed"],
            "best_cost": d["best_cost"], "is_feasible": d["is_feasible"], "time_seconds": d["time_seconds"],
            "eta": d["eta_limit"], "tau": d["tau_limit"], "j_mccar": d["j_mccar"], "ccar": d["ccar"],
            "cost_5000": _at(ev, cs, 5000), "cost_10000": _at(ev, cs, 10000), "cost_25000": _at(ev, cs, 25000),
        })
        curves.setdefault((d["config_id"], d["algo"]), []).append(cs)
    df = pd.DataFrame(rows)
    df["slack_J_abs"] = df["eta"] - df["j_mccar"]
    df["slack_J_rel"] = df["slack_J_abs"] / df["eta"]
    df["slack_R_abs"] = df["tau"] - df["ccar"]
    df["slack_R_rel"] = df["slack_R_abs"] / df["tau"]
    ref = df[df["is_feasible"]].groupby("config_id")["best_cost"].min()
    df["ref_best_cost"] = df["config_id"].map(ref)
    df["gap_pct_25000"] = (df["best_cost"] - df["ref_best_cost"]) / df["ref_best_cost"] * 100.0
    df["improve_pct_5k_25k"] = (df["cost_5000"] - df["cost_25000"]) / df["cost_5000"] * 100.0
    df["improve_pct_5k_10k"] = (df["cost_5000"] - df["cost_10000"]) / df["cost_5000"] * 100.0
    out_curves = {k: np.vstack(v) for k, v in curves.items()}
    return df, out_curves


def _at(ev: np.ndarray, cs: np.ndarray, e: int) -> float:
    idx = np.where(ev == e)[0]
    return float(cs[idx[0]]) if len(idx) else np.nan


def summarize_main_runs(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    def iqr(x):
        return float(np.nanpercentile(x, 75) - np.nanpercentile(x, 25))

    slack = df.groupby(["config_id", "algo"]).agg(
        n=("rep", "count"),
        slack_J_abs_mean=("slack_J_abs", "mean"), slack_J_abs_median=("slack_J_abs", "median"),
        slack_J_rel_mean=("slack_J_rel", "mean"), slack_J_rel_median=("slack_J_rel", "median"),
        slack_J_rel_max=("slack_J_rel", "max"),
        slack_R_rel_mean=("slack_R_rel", "mean"), slack_R_rel_median=("slack_R_rel", "median"),
    ).reset_index()

    rows = []
    for (cid, algo), g in df.groupby(["config_id", "algo"]):
        for e in (5000, 10000, 25000):
            x = g[f"cost_{e}"].to_numpy()
            ref = g["ref_best_cost"].iloc[0]
            rows.append({"config_id": cid, "algo": algo, "evaluation": e,
                         "median": float(np.nanmedian(x)), "mean": float(np.nanmean(x)), "iqr": iqr(x),
                         "q25": float(np.nanpercentile(x, 25)), "q75": float(np.nanpercentile(x, 75)),
                         "median_gap_pct": float((np.nanmedian(x) - ref) / ref * 100.0)})
    checkpoints = pd.DataFrame(rows)

    phase = df.groupby(["config_id", "algo"]).agg(
        improve_5k_25k_median=("improve_pct_5k_25k", "median"),
        improve_5k_25k_mean=("improve_pct_5k_25k", "mean"),
        improve_5k_25k_max=("improve_pct_5k_25k", "max"),
        improve_5k_10k_median=("improve_pct_5k_10k", "median"),
        frac_runs_improved=("improve_pct_5k_25k", lambda x: float(np.mean(np.asarray(x) > 1e-9))),
    ).reset_index()
    return {"slack": slack, "checkpoints": checkpoints, "phase": phase}


# ==============================================================================
# 7. Ringkasan hasil diagnosis
# ==============================================================================

def load_json_dir(folder: Path) -> List[Dict[str, Any]]:
    out = []
    if not folder.exists():
        return out
    for p in sorted(folder.rglob("*.json")):
        with open(p, "r", encoding="utf-8") as f:
            out.append(json.load(f))
    return out


def summarize_benchmark(records: List[Dict[str, Any]]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    if not records:
        return pd.DataFrame(), pd.DataFrame()
    df = pd.DataFrame([{k: v for k, v in r.items() if k not in ("checkpoints", "meta")} |
                       {f"best_{k.split('_')[1]}": v for k, v in r["checkpoints"].items()} for r in records])
    summ = df.groupby(["set", "function", "dim", "shifted", "algo"]).agg(
        n=("rep", "count"),
        median=("best_fitness", "median"), mean=("best_fitness", "mean"), std=("best_fitness", "std"),
        min=("best_fitness", "min"), max=("best_fitness", "max"),
        median_at_5000=("best_5000", "median"), median_at_10000=("best_10000", "median"),
        median_dist_to_opt=("dist_to_optimum", "median"),
        time_median=("time_seconds", "median"),
    ).reset_index()
    return df, summ


def compare_with_suyanto(summ: pd.DataFrame, ref_cfg: Dict[str, Any]) -> pd.DataFrame:
    rows = []
    for algo in ("kma", "ga"):
        for fn, ref in ref_cfg[algo].items():
            sub = summ[(summ["algo"] == algo) & (summ["function"] == fn) & (~summ["shifted"])]
            for _, r in sub.iterrows():
                rows.append({
                    "algo": algo, "function": fn, "dim": int(r["dim"]), "our_mean": r["mean"], "our_std": r["std"],
                    "our_median": r["median"], "paper_dim": int(ref_cfg["dim"]),
                    "paper_avg": float(ref["avg"]), "paper_std": float(ref["std"]),
                    "same_dim_as_paper": int(r["dim"]) == int(ref_cfg["dim"]),
                    "note": "GA paper: n=100, turnamen 10, pc=0,8, creep pm=0,05 (beda dgn GA kita)" if algo == "ga" else "",
                })
    return pd.DataFrame(rows)


def summarize_portfolio(records: List[Dict[str, Any]], ref_best: Dict[str, float]) -> pd.DataFrame:
    if not records:
        return pd.DataFrame()
    df = pd.DataFrame([{k: r[k] for k in ("config_id", "algo", "rep", "seed", "best_cost", "is_feasible",
                                          "slack_J_abs", "slack_J_rel", "slack_R_rel", "time_seconds",
                                          "phase_1_end_eval")} | r["checkpoints"] for r in records])
    df["gap_pct"] = [(c - ref_best[cid]) / ref_best[cid] * 100.0 for c, cid in zip(df["best_cost"], df["config_id"])]
    return df


def ablation_tests(df: pd.DataFrame, baseline: str = "kma_default") -> pd.DataFrame:
    """Mann-Whitney dua sisi tiap varian vs baseline per konfigurasi + koreksi Holm."""
    from scipy.stats import mannwhitneyu
    from mccar_kma.analysis.stats_tests import holm_bonferroni_correction, rank_biserial_correlation

    rows = []
    for cid, g in df.groupby("config_id"):
        base = g[g["algo"] == baseline]["best_cost"].to_numpy()
        if len(base) == 0:
            continue
        tmp = []
        for algo, h in g.groupby("algo"):
            if algo == baseline:
                continue
            x = h["best_cost"].to_numpy()
            p = float(mannwhitneyu(x, base, alternative="two-sided").pvalue)
            tmp.append({"config_id": cid, "variant": algo, "n": len(x), "n_baseline": len(base),
                        "median_variant": float(np.median(x)), "median_baseline": float(np.median(base)),
                        "median_gap_pct_variant": float(h["gap_pct"].median()),
                        "median_gap_pct_baseline": float(g[g["algo"] == baseline]["gap_pct"].median()),
                        "median_slack_J_rel_variant": float(h["slack_J_rel"].median()),
                        "p_value": p, "rank_biserial": float(rank_biserial_correlation(x, base))})
        if tmp:
            adj = holm_bonferroni_correction([t["p_value"] for t in tmp])
            for t, a in zip(tmp, adj):
                t["p_holm"] = float(a)
            rows.extend(tmp)
    return pd.DataFrame(rows)
