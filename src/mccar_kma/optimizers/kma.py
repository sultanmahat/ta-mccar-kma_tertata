"""Implementasi Komodo Mlipir Algorithm (KMA) Dua Fase.

Berdasarkan:
1. Suyanto, Ariyanto, & Ariyanto (2022), "Komodo Mlipir Algorithm",
   Applied Soft Computing, Vol. 114, 108043.
2. Proposal Tesis Sultan Bakri Baihaqi Mahat (Subbab 2.8, Algoritma 1, Persamaan 2.25–2.32).
3. Keputusan D4 (docs/decisions/0006-kma-parameters-d4.md).

Struktur KMA:
- Tiga kelompok individu:
  * Big Males: HILE (High-Exploitation Low-Exploration, Persamaan 2.26–2.27)
  * Female: MIME (Medium-Exploitation Medium-Exploration, Persamaan 2.28–2.30)
  * Small Males: LIHE (Low-Exploitation High-Exploration via Mlipir, Persamaan 2.31–2.32)
- Dua Fase:
  * Fase 1: n_pop = 5, d = (D-1)/D, anggaran 5.000 evaluasi
  * Serah-terima: solusi terbaik Fase 1 diwariskan ke populasi awal Fase 2
  * Fase 2: n_pop awal 200, batas [20, 200], d = 0.5, langkah adaptasi delta_n = 5,
    sisa anggaran 20.000 evaluasi
"""

import time
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np

from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.model.constraints import project_weights


def compute_group_sizes(n_pop: int, p_bm: float = 0.5) -> Tuple[int, int, int]:
    """Menghitung ukuran kelompok Big Males, Female, dan Small Males (Persamaan 2.25).

    Persamaan 2.25:
        n* = floor(p_bm * (n_pop - 1))
        n_bm = min(max(n*, 2), n_pop - 3)
        n_female = 1
        n_sm = n_pop - n_bm - 1

    Parameters
    ----------
    n_pop : int
        Ukuran total populasi.
    p_bm : float
        Proporsi Big Males (default: 0.5).

    Returns
    -------
    Tuple[int, int, int]
        (n_bm, n_female, n_sm)
    """
    if n_pop < 5:
        n_bm = max(1, n_pop - 2)
        n_female = 1
        n_sm = max(0, n_pop - n_bm - n_female)
        return n_bm, n_female, n_sm

    n_star = int(np.floor(p_bm * (n_pop - 1)))
    n_bm = min(max(n_star, 2), n_pop - 3)
    n_female = 1
    n_sm = n_pop - n_bm - n_female
    return n_bm, n_female, n_sm


class KomodoMlipirOptimizer(BaseOptimizer):
    """Pengoptimal Komodo Mlipir Algorithm (KMA) Dua Fase.

    Parameters
    ----------
    phase_1_n_pop : int
        Ukuran populasi pada Fase 1 (default: 5).
    phase_1_budget : int
        Anggaran evaluasi fungsi Fase 1 (default: 5.000).
    phase_2_n_pop_init : int
        Ukuran populasi awal pada Fase 2 (default: 200).
    phase_2_n_pop_min : int
        Batas minimum ukuran populasi Fase 2 (default: 20).
    phase_2_n_pop_max : int
        Batas maksimum ukuran populasi Fase 2 (default: 200).
    phase_2_budget : int
        Anggaran evaluasi fungsi Fase 2 (default: 20.000).
    p_bm : float
        Proporsi Big Males dalam populasi (default: 0.5, D4).
    gamma : float
        Radius partenogenesis sebagai fraksi rentang [lb, ub] (default: 0.1, D4).
    q_interactions : Optional[int]
        Banyaknya Big Males yang berinteraksi. Jika None, gunakan seluruh n_bm (D4).
    p_mating : float
        Peluang memilih kawin vs partenogenesis pada female (default: 0.5, D4).
    stagnation_patience : int
        Jumlah generasi beruntun untuk memicu adaptasi populasi (default: 2, D4).
    stagnation_tol : float
        Toleransi perubahan fitness relatif untuk mendeteksi stagnasi (default: 1e-7, D4).
    delta_n : int
        Besar perubahan ukuran populasi saat adaptasi (default: 5, D4).
    phase_2_mlipir_rate : float
        Laju mlipir (d) pada Fase 2 (default: 0,5, D13 -- usulan agen, menunggu
        konfirmasi Sultan: docs/decisions/0013-kma-phase2-mlipir-rate-d13.md).
    population_adapt_floor : float
        Lantai pembagi relatif saat menghitung delta_f1/delta_f2 pada adaptasi
        ukuran populasi Fase 2, mencegah pembagian oleh nol (default: 1e-12, R11).
    check_interval : int
        Interval evaluasi untuk pencatatan konvergensi (default: 250).
    eps_tol : float
        Toleransi numerik kendala bobot (default: 1e-8).
    """

    def __init__(
        self,
        phase_1_n_pop: int = 5,
        phase_1_budget: int = 5000,
        phase_2_n_pop_init: int = 200,
        phase_2_n_pop_min: int = 20,
        phase_2_n_pop_max: int = 200,
        phase_2_budget: int = 20000,
        p_bm: float = 0.5,
        gamma: float = 0.1,
        q_interactions: Optional[int] = None,
        p_mating: float = 0.5,
        stagnation_patience: int = 2,
        stagnation_tol: float = 1e-7,
        delta_n: int = 5,
        phase_2_mlipir_rate: float = 0.5,
        population_adapt_floor: float = 1e-12,
        check_interval: int = 250,
        eps_tol: float = 1e-8,
    ) -> None:
        super().__init__(check_interval=check_interval, eps_tol=eps_tol)
        self.phase_1_n_pop = int(phase_1_n_pop)
        self.phase_1_budget = int(phase_1_budget)
        self.phase_2_n_pop_init = int(phase_2_n_pop_init)
        self.phase_2_n_pop_min = int(phase_2_n_pop_min)
        self.phase_2_n_pop_max = int(phase_2_n_pop_max)
        self.phase_2_budget = int(phase_2_budget)
        self.p_bm = float(p_bm)
        self.gamma = float(gamma)
        self.q_interactions = q_interactions
        self.p_mating = float(p_mating)
        self.stagnation_patience = int(stagnation_patience)
        self.stagnation_tol = float(stagnation_tol)
        self.delta_n = int(delta_n)
        self.phase_2_mlipir_rate = float(phase_2_mlipir_rate)
        self.population_adapt_floor = float(population_adapt_floor)

    def run(
        self,
        evaluator: Any,
        lb: np.ndarray,
        ub: np.ndarray,
        budget: int = 25000,
        rng: Optional[Union[int, np.random.Generator]] = None,
    ) -> OptimizationResult:
        """Menjalankan KMA dua fase hingga batas anggaran terpenuhi."""
        start_time = time.perf_counter()
        gen_rng = self._init_run(budget=budget, lb=lb, ub=ub, rng=rng)
        dim = len(self._lb)
        bound_range = np.abs(self._ub - self._lb)

        # Alokasi anggaran Fase 1 vs Fase 2
        total_nominal = self.phase_1_budget + self.phase_2_budget
        frac_phase_1 = self.phase_1_budget / total_nominal if total_nominal > 0 else 0.2
        target_phase_1_budget = min(self.phase_1_budget, int(np.round(frac_phase_1 * budget)))

        # =====================================================================
        # FASE 1: Deteksi Cepat & Eksplorasi Luas
        # n_pop = 5, d = (dim - 1) / dim
        # =====================================================================
        mlipir_rate_1 = (dim - 1.0) / float(dim)
        n_pop_1 = self.phase_1_n_pop

        # Inisialisasi populasi Fase 1
        raw_init_1 = gen_rng.uniform(self._lb, self._ub, size=(n_pop_1, dim))
        results_1 = self.evaluate_population(raw_init_1, evaluator)
        pop_1 = [r["w"] for r in results_1]
        pop_1, results_1 = self._sort_population(pop_1, results_1)

        # Loop generasi Fase 1
        while (
            self.budget.evaluations < target_phase_1_budget
            and not self.budget.is_exhausted
        ):
            pop_1, results_1 = self._evolve_generation(
                pop=pop_1,
                results=results_1,
                mlipir_rate=mlipir_rate_1,
                bound_range=bound_range,
                evaluator=evaluator,
                rng=gen_rng,
            )

        # Catat solusi terbaik Fase 1 untuk serah-terima ke Fase 2 (D4 Opsi A)
        best_phase_1_w = pop_1[0].copy()

        # =====================================================================
        # FASE 2: Eksploitasi & Adaptasi Ukuran Populasi
        # n_pop awal 200, rentang [20, 200], d = 0.5
        # =====================================================================
        if not self.budget.is_exhausted:
            mlipir_rate_2 = self.phase_2_mlipir_rate
            rem_budget = self.budget.remaining
            init_n_pop_2 = min(self.phase_2_n_pop_init, max(self.phase_2_n_pop_min, rem_budget))

            # Populasi awal Fase 2:
            # Individu ke-0 mewarisi solusi terbaik Fase 1 (tanpa evaluasi ulang)
            # Sisa (init_n_pop_2 - 1) dibangkitkan secara acak seragam
            pop_2: List[np.ndarray] = [best_phase_1_w]
            results_2: List[Dict[str, Any]] = [results_1[0]]
            num_new = max(0, init_n_pop_2 - 1)
            if num_new > 0 and self.budget.remaining > 0:
                raw_init_2 = gen_rng.uniform(self._lb, self._ub, size=(num_new, dim))
                results_new = self.evaluate_population(raw_init_2, evaluator)
                pop_2.extend([r["w"] for r in results_new])
                results_2.extend(results_new)

            pop_2, results_2 = self._sort_population(pop_2, results_2)

            # Riwayat fitness terbaik generasi Fase 2 untuk adaptasi ukuran populasi
            fitness_history: List[float] = [results_2[0]["f_val"]] if results_2 else []

            # Loop generasi Fase 2
            while not self.budget.is_exhausted:
                pop_2, results_2 = self._evolve_generation(
                    pop=pop_2,
                    results=results_2,
                    mlipir_rate=mlipir_rate_2,
                    bound_range=bound_range,
                    evaluator=evaluator,
                    rng=gen_rng,
                )

                if not results_2:
                    break

                current_best_f = results_2[0]["f_val"]
                fitness_history.append(current_best_f)

                # Adaptasi Ukuran Populasi Fase 2 (Persamaan 2.18–2.19 Suyanto / D4)
                if len(fitness_history) >= 3 and not self.budget.is_exhausted:
                    pop_2, results_2 = self._adapt_population_size(
                        pop=pop_2,
                        results=results_2,
                        fitness_history=fitness_history,
                        bound_range=bound_range,
                        evaluator=evaluator,
                        rng=gen_rng,
                    )

        elapsed = time.perf_counter() - start_time
        meta = {
            "algorithm": "Komodo Mlipir Algorithm (KMA)",
            "dim": dim,
            "budget": budget,
            "p_bm": self.p_bm,
            "gamma": self.gamma,
            "p_mating": self.p_mating,
            "delta_n": self.delta_n,
            "stagnation_tol": self.stagnation_tol,
        }
        return self._build_result(elapsed_seconds=elapsed, metadata=meta)

    def _sort_population(
        self,
        pop: List[np.ndarray],
        results: List[Dict[str, Any]],
    ) -> Tuple[List[np.ndarray], List[Dict[str, Any]]]:
        """Mengurutkan populasi berdasarkan nilai f_val ascending (minimasi)."""
        if not results:
            return pop, results
        n = min(len(pop), len(results))
        pop = pop[:n]
        results = results[:n]

        order = np.argsort([r["f_val"] for r in results])
        sorted_pop = [pop[idx] for idx in order]
        sorted_results = [results[idx] for idx in order]
        return sorted_pop, sorted_results

    def _evolve_generation(
        self,
        pop: List[np.ndarray],
        results: List[Dict[str, Any]],
        mlipir_rate: float,
        bound_range: np.ndarray,
        evaluator: Any,
        rng: np.random.Generator,
    ) -> Tuple[List[np.ndarray], List[Dict[str, Any]]]:
        """Mengeksekusi satu generasi KMA (Big Males, Female, Small Males)."""
        n_pop = len(pop)
        if n_pop < 3 or self.budget.is_exhausted:
            return pop, results

        dim = len(self._lb)
        n_bm, n_female, n_sm = compute_group_sizes(n_pop, self.p_bm)

        # ---------------------------------------------------------------------
        # 1. Pergerakan Big Males (HILE, Persamaan 2.26–2.27)
        # ---------------------------------------------------------------------
        q = n_bm if self.q_interactions is None else min(self.q_interactions, n_bm)
        for i in range(n_bm):
            if self.budget.is_exhausted:
                break
            k_i = pop[i]
            w_ij_sum = np.zeros(dim, dtype=float)

            for j in range(q):
                if j == i:
                    continue
                k_j = pop[j]
                r1 = rng.uniform(0.0, 1.0)
                r2 = rng.uniform(0.0, 1.0)

                # Persamaan 2.26:
                # u_ij = r1 * (k_j - k_i) jika f(k_j) < f(k_i) atau r2 < 0.5
                #        r1 * (k_i - k_j) lainnya
                if results[j]["f_val"] < results[i]["f_val"] or r2 < 0.5:
                    u_ij = r1 * (k_j - k_i)
                else:
                    u_ij = r1 * (k_i - k_j)
                w_ij_sum += u_ij

            # Persamaan 2.27:
            k_i_new = k_i + w_ij_sum
            new_res = self.evaluate_candidate(k_i_new, evaluator)

            # Seleksi penyintas Big Males: pertahankan posisi terbaik
            if new_res is not None and new_res["f_val"] < results[i]["f_val"]:
                pop[i] = new_res["w"]
                results[i] = new_res

        # ---------------------------------------------------------------------
        # 2. Reproduksi Female (MIME, Persamaan 2.28–2.30)
        # ---------------------------------------------------------------------
        female_idx = n_bm
        if female_idx < n_pop and not self.budget.is_exhausted:
            k_female = pop[female_idx]
            k_winner = pop[0]  # Winner big male

            p_choice = rng.uniform(0.0, 1.0)
            if p_choice < self.p_mating:
                # Mating (Persamaan 2.28–2.29):
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_offspring1 = r_l * k_female + (1.0 - r_l) * k_winner
                k_offspring2 = r_l * k_winner + (1.0 - r_l) * k_female

                res1 = self.evaluate_candidate(k_offspring1, evaluator)
                res2 = self.evaluate_candidate(k_offspring2, evaluator)

                best_res = None
                if res1 is not None and res2 is not None:
                    best_res = res1 if res1["f_val"] < res2["f_val"] else res2
                elif res1 is not None:
                    best_res = res1
                elif res2 is not None:
                    best_res = res2

                if best_res is not None and best_res["f_val"] < results[female_idx]["f_val"]:
                    pop[female_idx] = best_res["w"]
                    results[female_idx] = best_res
            else:
                # Partenogenesis (Persamaan 2.30):
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_partheno = k_female + (2.0 * r_l - 1.0) * self.gamma * bound_range
                res_partheno = self.evaluate_candidate(k_partheno, evaluator)

                if res_partheno is not None and res_partheno["f_val"] < results[female_idx]["f_val"]:
                    pop[female_idx] = res_partheno["w"]
                    results[female_idx] = res_partheno

        # ---------------------------------------------------------------------
        # 3. Pergerakan Small Males (LIHE / Mlipir, Persamaan 2.31–2.32)
        # ---------------------------------------------------------------------
        start_sm = n_bm + n_female
        for i in range(start_sm, n_pop):
            if self.budget.is_exhausted:
                break
            k_i = pop[i]
            k_i_new = k_i.copy()

            for j in range(n_bm):
                k_j = pop[j]
                for l in range(dim):
                    r2 = rng.uniform(0.0, 1.0)
                    if r2 < mlipir_rate:
                        r1 = rng.uniform(0.0, 1.0)
                        u_ijl = r1 * (k_j[l] - k_i[l])
                        k_i_new[l] += u_ijl

            new_sm_res = self.evaluate_candidate(k_i_new, evaluator)
            if new_sm_res is not None:
                # Small males diperbarui langsung tanpa survivor selection
                pop[i] = new_sm_res["w"]
                results[i] = new_sm_res

        # Urutkan kembali seluruh populasi
        return self._sort_population(pop, results)

    def _adapt_population_size(
        self,
        pop: List[np.ndarray],
        results: List[Dict[str, Any]],
        fitness_history: List[float],
        bound_range: np.ndarray,
        evaluator: Any,
        rng: np.random.Generator,
    ) -> Tuple[List[np.ndarray], List[Dict[str, Any]]]:
        """Mengadaptasi ukuran populasi n pada Fase 2 (Persamaan 10 Suyanto 2022)."""
        f_t = fitness_history[-1]
        f_t1 = fitness_history[-2]
        f_t2 = fitness_history[-3]

        denom1 = max(abs(f_t1), self.population_adapt_floor)
        denom2 = max(abs(f_t2), self.population_adapt_floor)
        delta_f1 = abs(f_t1 - f_t) / denom1
        delta_f2 = abs(f_t2 - f_t1) / denom2

        current_n = len(pop)

        # Kasus A: Kualitas membaik 2 generasi berturut-turut -> kurangi populasi
        if (
            f_t < f_t1 - self.stagnation_tol * denom1
            and f_t1 < f_t2 - self.stagnation_tol * denom2
        ):
            target_n = max(self.phase_2_n_pop_min, current_n - self.delta_n)
            if target_n < current_n:
                pop = pop[:target_n]
                results = results[:target_n]

        # Kasus B: Mengalami stagnasi 2 generasi berturut-turut -> tambah populasi
        elif delta_f1 <= self.stagnation_tol and delta_f2 <= self.stagnation_tol:
            target_n = min(self.phase_2_n_pop_max, current_n + self.delta_n)
            num_to_add = target_n - current_n
            dim = len(self._lb)

            if num_to_add > 0 and not self.budget.is_exhausted:
                best_k = pop[0]
                for _ in range(num_to_add):
                    if self.budget.is_exhausted:
                        break
                    # Pembangkitan individu baru dari best-so-far dengan gangguan acak
                    r_l = rng.uniform(0.0, 1.0, size=dim)
                    cand = best_k + (2.0 * r_l - 1.0) * self.gamma * bound_range
                    res = self.evaluate_candidate(cand, evaluator)
                    if res is not None:
                        pop.append(res["w"])
                        results.append(res)

                pop, results = self._sort_population(pop, results)

        return pop, results
