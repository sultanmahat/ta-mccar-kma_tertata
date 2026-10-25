"""Pelari eksperimen portofolio utang negara: orkestrasi single run dan batch paralel.

Mendukung:
1. Resumability: otomatis melewati run yang file JSON-nya sudah lengkap dan valid.
2. Pengujian adil: inisialisasi, batasan, batas risiko, dan evaluator seragam.
3. Eksekusi paralel multi-core / multi-worker.
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import concurrent.futures
import json
import logging
import multiprocessing as mp
import time
import numpy as np

from mccar_kma.experiments.seeds import ExperimentSpec, compute_spec_hash
from mccar_kma.experiments.io import (
    get_run_result_path,
    is_run_completed,
    load_run_result,
    save_run_result,
)
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, LB_FREE, UB_FREE
from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.utils.config import load_config

logger = logging.getLogger(__name__)

ALGORITHM_REGISTRY = {
    "kma": KomodoMlipirOptimizer,
    "ga": GeneticAlgorithmOptimizer,
    "pso": ParticleSwarmOptimizer,
}


def get_bounds_for_constraint(constraint_type: str) -> Tuple[np.ndarray, np.ndarray]:
    """Mengembalikan batas proporsi (lb, ub) berdasarkan jenis kendala."""
    if constraint_type.lower() == "djppr":
        return LB_DJPPR.copy(), UB_DJPPR.copy()
    elif constraint_type.lower() == "free":
        return LB_FREE.copy(), UB_FREE.copy()
    else:
        raise ValueError(f"Jenis kendala tidak dikenal: {constraint_type}. Harus 'djppr' atau 'free'.")


def build_optimizer(algo_name: str, cfg: Dict[str, Any]) -> BaseOptimizer:
    """Membangun instance optimizer dari blok `algorithms.<algo_name>` di params.yaml.

    Mengalirkan konfigurasi ke konstruktor (temuan S1, audit_ulang_2026-10-25.md):
    mengubah params.yaml sekarang benar-benar mengubah hyperparameter eksperimen,
    bukan hanya dokumentasi yang tidak dipakai kode.
    """
    if algo_name not in ALGORITHM_REGISTRY:
        raise ValueError(f"Algoritma {algo_name} tidak terdaftar di ALGORITHM_REGISTRY.")

    eps_tol = float(cfg["optimization"]["eps_tol"])
    algo_cfg = cfg["algorithms"][algo_name]

    if algo_name == "kma":
        return KomodoMlipirOptimizer(
            phase_1_n_pop=int(algo_cfg["phase_1"]["n_pop"]),
            phase_1_budget=int(algo_cfg["phase_1"]["budget"]),
            phase_2_n_pop_init=int(algo_cfg["phase_2"]["n_pop_init"]),
            phase_2_n_pop_min=int(algo_cfg["phase_2"]["n_pop_min"]),
            phase_2_n_pop_max=int(algo_cfg["phase_2"]["n_pop_max"]),
            phase_2_budget=int(algo_cfg["phase_2"]["budget"]),
            p_bm=float(algo_cfg["p_bm"]),
            gamma=float(algo_cfg["gamma"]),
            q_interactions=algo_cfg["q_interactions"],
            p_mating=float(algo_cfg["p_mating"]),
            stagnation_patience=int(algo_cfg["stagnation_patience"]),
            stagnation_tol=float(algo_cfg["stagnation_tol"]),
            delta_n=int(algo_cfg["delta_n"]),
            phase_2_mlipir_rate=float(algo_cfg["phase_2"]["mlipir_rate"]),
            population_adapt_floor=float(algo_cfg["phase_2"]["population_adapt_floor"]),
            eps_tol=eps_tol,
        )
    if algo_name == "ga":
        return GeneticAlgorithmOptimizer(
            n_pop=int(algo_cfg["n_pop"]),
            tournament_size=int(algo_cfg["tournament_size"]),
            p_crossover=float(algo_cfg["p_crossover"]),
            p_mutation=float(algo_cfg["p_mutation"]) if algo_cfg.get("p_mutation") is not None else None,
            sigma_m_factor=float(algo_cfg["sigma_m_factor"]),
            elitism_count=int(algo_cfg["elitism_count"]),
            eps_tol=eps_tol,
        )
    # algo_name == "pso"
    return ParticleSwarmOptimizer(
        n_pop=int(algo_cfg["n_pop"]),
        w_start=float(algo_cfg["w_start"]),
        w_end=float(algo_cfg["w_end"]),
        c1=float(algo_cfg["c1"]),
        c2=float(algo_cfg["c2"]),
        v_max_factor=float(algo_cfg["v_max_factor"]),
        velocity_clamp_strategy=str(algo_cfg["velocity_clamp_strategy"]),
        eps_tol=eps_tol,
    )


def execute_single_run(
    spec: ExperimentSpec,
    bank_path: Path,
    limits_path: Path,
    output_dir: Path,
    resume: bool = True,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Mengeksekusi satu replikasi eksperimen optimasi secara modular.

    Parameters
    ----------
    spec : ExperimentSpec
        Spesifikasi replikasi eksperimen.
    bank_path : Path
        Lokasi file NPZ bank skenario.
    limits_path : Path
        Lokasi file JSON batas risiko (tau dan eta).
    output_dir : Path
        Direktori target penyimpanan hasil.
    resume : bool
        Jika True, lewati run jika file hasil yang valid sudah ada.
    config : Optional[Dict[str, Any]]
        Konfigurasi params.yaml terparse. Jika None, dimuat via `load_config()`
        (temuan S1, audit_ulang_2026-10-25.md).

    Returns
    -------
    Dict[str, Any]
        Hasil replikasi.
    """
    cfg = config if config is not None else load_config()
    result_path = get_run_result_path(
        base_dir=output_dir,
        config_id=spec.config_id,
        algo=spec.algo_name,
        rep=spec.rep,
        seed=spec.seed,
    )

    if resume and is_run_completed(result_path):
        logger.info("[RESUME SKIP] Run %s sudah selesai di %s", spec.run_id, result_path)
        existing = load_run_result(result_path)
        existing["status"] = "skipped"
        return existing

    # 1. Muat bank skenario dan batas risiko
    bank_npz = np.load(bank_path)
    cost_key = f"cost_{spec.cost_definition}"
    if cost_key not in bank_npz:
        raise KeyError(f"Kunci matriks biaya {cost_key} tidak ditemukan di {bank_path}")
    cost_matrix = bank_npz[cost_key]

    with open(limits_path, "r", encoding="utf-8") as f:
        limits_data = json.load(f)

    if spec.cost_definition not in limits_data:
        raise KeyError(f"Definisi biaya {spec.cost_definition} tidak ada di {limits_path}")

    tau = float(limits_data[spec.cost_definition]["tau"])
    eta = float(limits_data[spec.cost_definition]["eta"])

    # 2. Inisialisasi Evaluator dengan batas risiko dan parameter dari config
    risk_cfg = cfg["risk"]
    opt_cfg = cfg["optimization"]
    evaluator = PortfolioEvaluator(
        cost_matrix=cost_matrix,
        alpha=float(risk_cfg["alpha"]),
        delta=float(risk_cfg["delta"]),
        tau=tau,
        eta=eta,
        rho_J=float(opt_cfg["penalty_rho_J"]),
        rho_R=float(opt_cfg["penalty_rho_R"]),
        eps_tol=float(opt_cfg["eps_tol"]),
        zero_tol_mc=float(risk_cfg["zero_tolerance_mc"]),
    )

    # 3. Ambil batas proporsi & inisialisasi optimizer dari config
    lb, ub = get_bounds_for_constraint(spec.constraint_type)
    optimizer: BaseOptimizer = build_optimizer(spec.algo_name, cfg)

    # 4. Jalankan optimasi
    t_start = time.perf_counter()
    opt_result: OptimizationResult = optimizer.run(
        evaluator=evaluator,
        lb=lb,
        ub=ub,
        budget=spec.budget,
        rng=spec.seed,
    )
    t_elapsed = time.perf_counter() - t_start

    # 5. Evaluasi metrik akhir presisi tinggi untuk solusi terbaik
    final_eval = evaluator.evaluate(opt_result.best_w)
    is_feasible = bool(opt_result.is_feasible and final_eval["is_feasible"])

    # 6. Bentuk payload hasil
    timestamp_iso = datetime.now(timezone.utc).isoformat()
    spec_hash = compute_spec_hash(spec)

    payload = {
        "run_id": spec.run_id,
        "config_id": spec.config_id,
        "cost_definition": spec.cost_definition,
        "constraint_type": spec.constraint_type,
        "algo": spec.algo_name,
        "rep": spec.rep,
        "seed": spec.seed,
        "budget": spec.budget,
        "evaluations": opt_result.evaluations_used,
        "is_feasible": is_feasible,
        "best_cost": float(final_eval["mean_cost"]),
        "best_fitness": float(opt_result.best_fitness),
        "ccar": float(final_eval["ccar"]),
        "j_mccar": float(final_eval["j_mccar"]),
        "tau_limit": tau,
        "eta_limit": eta,
        "v_J": float(final_eval["v_J"]),
        "v_R": float(final_eval["v_R"]),
        "theta_i": [float(x) for x in final_eval["theta"]],
        "mc_i": [float(x) for x in final_eval["mc"]],
        "mccar_i": [float(x) for x in final_eval["mccar"]],
        "best_w": [float(w) for w in opt_result.best_w],
        "time_seconds": round(t_elapsed, 4),
        "convergence_history": [
            {
                "evaluation": int(pt["evaluation"]),
                "best_cost": float(pt["best_cost"]) if pt["best_cost"] is not None else None,
                "best_fitness": float(pt["best_fitness"]) if pt.get("best_fitness") is not None else None,
                "is_feasible": bool(pt["is_feasible"]),
            }
            for pt in opt_result.convergence_history
        ],
        "config_hash": spec_hash,
        "timestamp": timestamp_iso,
        "status": "completed",
    }

    # 7. Simpan secara atomic
    save_run_result(result_path, payload)
    logger.info(
        "[DONE] Run %s: Cost=%.8f Feasible=%s Time=%.2fs",
        spec.run_id,
        payload["best_cost"],
        payload["is_feasible"],
        t_elapsed,
    )
    return payload


def _worker_wrapper(
    args: Tuple[ExperimentSpec, Path, Path, Path, bool, Dict[str, Any]]
) -> Dict[str, Any]:
    """Helper worker untuk eksekusi paralel multiprocessing."""
    spec, bank_path, limits_path, output_dir, resume, config = args
    return execute_single_run(
        spec=spec,
        bank_path=bank_path,
        limits_path=limits_path,
        output_dir=output_dir,
        resume=resume,
        config=config,
    )


def run_experiment_batch(
    specs: List[ExperimentSpec],
    bank_path: Path,
    limits_path: Path,
    output_dir: Path,
    max_workers: int = 1,
    resume: bool = True,
    config: Optional[Dict[str, Any]] = None,
) -> List[Dict[str, Any]]:
    """Menjalankan kumpulan replikasi eksperimen secara sequential atau paralel.

    `config` dimuat sekali di proses induk (jika tidak diberikan) lalu dikirim
    identik ke setiap worker, supaya seluruh batch memakai satu snapshot
    params.yaml yang konsisten (temuan S1).
    """
    cfg = config if config is not None else load_config()
    total_runs = len(specs)
    logger.info("Memulai batch eksperimen (%d run) dengan max_workers=%d", total_runs, max_workers)

    tasks_args = [
        (spec, bank_path, limits_path, output_dir, resume, cfg)
        for spec in specs
    ]

    results: List[Dict[str, Any]] = []

    if max_workers <= 1:
        for idx, arg in enumerate(tasks_args, start=1):
            logger.info("Eksekusi run [%d/%d]: %s", idx, total_runs, arg[0].run_id)
            res = _worker_wrapper(arg)
            results.append(res)
    else:
        ctx = mp.get_context("spawn")
        with ctx.Pool(processes=max_workers) as pool:
            for idx, res in enumerate(pool.imap_unordered(_worker_wrapper, tasks_args), start=1):
                logger.info("Selesai run [%d/%d]: %s", idx, total_runs, res.get("run_id"))
                results.append(res)

    return results
