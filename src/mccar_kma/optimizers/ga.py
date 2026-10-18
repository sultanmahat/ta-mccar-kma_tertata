"""Implementasi Genetic Algorithm (GA) dengan Representasi Bilangan Riil.

Berdasarkan:
1. Proposal Tesis Sultan Bakri Baihaqi Mahat (Subbab 2.9.1, Persamaan 2.33–2.34, Tabel 3.1).
2. Spesifikasi Model §7.2.
3. Keputusan Terbuka D6 (docs/decisions/0007-ga-pso-parameters-d6.md).

Operator GA:
- Ukuran populasi: n_pop = 50.
- Seleksi orang tua: Seleksi turnamen ukuran 2 (Tournament Selection, size 2).
- Persilangan: Aritmetika (Persamaan 2.33–2.34) dengan peluang p_c = 0.9.
- Mutasi: Gaussian per dimensi dengan peluang p_m = 1/D dan simpangan baku
  sigma_m = 0.1 * (ub - lb).
- Elitisme: n_elite = 2 individu terbaik dipertahankan secara utuh ke generasi berikutnya.
- Proyeksi kendala: project_weights ke sum(w)=1 dan lb <= w <= ub.
- Anggaran: 25.000 evaluasi fungsi, dilacak ketat via BudgetCounter & FeasibleArchive.
"""

import time
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np

from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.model.constraints import project_weights


class GeneticAlgorithmOptimizer(BaseOptimizer):
    """Pengoptimal Genetic Algorithm (GA) untuk Portofolio Utang Multivaluta.

    Parameters
    ----------
    n_pop : int
        Ukuran populasi (default: 50, Tabel 3.1).
    tournament_size : int
        Ukuran turnamen untuk seleksi orang tua (default: 2, Tabel 3.1).
    p_crossover : float
        Peluang persilangan aritmetika (default: 0.9, Tabel 3.1).
    p_mutation : Optional[float]
        Peluang mutasi per dimensi. Jika None, bernilai 1/D (default: None).
    sigma_m_factor : float
        Faktor pengali rentang batas untuk simpangan baku mutasi Gaussian
        sigma_m = sigma_m_factor * (ub - lb) (default: 0.1, Tabel 3.1).
    elitism_count : int
        Jumlah individu elit yang dipertahankan utuh ke generasi berikutnya
        (default: 2, D6).
    check_interval : int
        Interval evaluasi untuk pencatatan konvergensi (default: 250).
    eps_tol : float
        Toleransi numerik kendala (default: 1e-8).
    """

    def __init__(
        self,
        n_pop: int = 50,
        tournament_size: int = 2,
        p_crossover: float = 0.9,
        p_mutation: Optional[float] = None,
        sigma_m_factor: float = 0.1,
        elitism_count: int = 2,
        check_interval: int = 250,
        eps_tol: float = 1e-8,
    ) -> None:
        super().__init__(check_interval=check_interval, eps_tol=eps_tol)
        self.n_pop = int(n_pop)
        self.tournament_size = int(tournament_size)
        self.p_crossover = float(p_crossover)
        self.p_mutation = float(p_mutation) if p_mutation is not None else None
        self.sigma_m_factor = float(sigma_m_factor)
        self.elitism_count = int(elitism_count)

    def run(
        self,
        evaluator: Any,
        lb: np.ndarray,
        ub: np.ndarray,
        budget: int = 25000,
        rng: Optional[Union[int, np.random.Generator]] = None,
    ) -> OptimizationResult:
        """Menjalankan algoritma GA hingga anggaran evaluasi terpenuhi."""
        start_time = time.perf_counter()
        gen_rng = self._init_run(budget=budget, lb=lb, ub=ub, rng=rng)
        dim = len(self._lb)
        bound_range = np.abs(self._ub - self._lb)

        # Parameter mutasi per dimensi: p_m = 1/D, sigma_m = 0.1 * rentang
        p_mut = self.p_mutation if self.p_mutation is not None else (1.0 / float(dim))
        sigma_m = self.sigma_m_factor * bound_range

        # Ukuran populasi awal tidak boleh melebihi total anggaran
        init_pop_size = min(self.n_pop, budget)

        # ---------------------------------------------------------------------
        # Inisialisasi Populasi Awal Bersama (D6 Opsi A)
        # Acak seragam di [lb, ub] + proyeksi
        # ---------------------------------------------------------------------
        raw_init = gen_rng.uniform(self._lb, self._ub, size=(init_pop_size, dim))
        results = self.evaluate_population(raw_init, evaluator)
        pop = [r["w"] for r in results]
        pop, results = self._sort_population(pop, results)

        # ---------------------------------------------------------------------
        # Loop Generasi GA
        # ---------------------------------------------------------------------
        while not self.budget.is_exhausted:
            current_pop_size = len(pop)
            if current_pop_size < self.tournament_size:
                break

            # 1. Elitisme: Ambil n_elite individu terbaik yang sudah dievaluasi
            n_elite = min(self.elitism_count, current_pop_size)
            elite_pop = pop[:n_elite]
            elite_results = results[:n_elite]

            # Jumlah keturunan baru yang dibutuhkan
            n_offspring_needed = current_pop_size - n_elite
            rem_budget = self.budget.remaining
            if rem_budget <= 0:
                break
            if n_offspring_needed > rem_budget:
                n_offspring_needed = rem_budget

            offspring_list: List[np.ndarray] = []

            # 2. Pembentukan Keturunan (Seleksi Turnamen, Crossover, Mutasi)
            while len(offspring_list) < n_offspring_needed:
                # Seleksi Turnamen Ukuran 2 untuk Parent 1
                idx1 = gen_rng.choice(current_pop_size, size=self.tournament_size, replace=False)
                best_idx1 = min(idx1, key=lambda k: results[k]["f_val"])
                p1 = pop[best_idx1]

                # Seleksi Turnamen Ukuran 2 untuk Parent 2
                idx2 = gen_rng.choice(current_pop_size, size=self.tournament_size, replace=False)
                best_idx2 = min(idx2, key=lambda k: results[k]["f_val"])
                p2 = pop[best_idx2]

                # Persilangan Aritmetika (Persamaan 2.33–2.34)
                if gen_rng.uniform(0.0, 1.0) < self.p_crossover:
                    lam = gen_rng.uniform(0.0, 1.0, size=dim)
                    c1 = lam * p1 + (1.0 - lam) * p2
                    c2 = lam * p2 + (1.0 - lam) * p1
                else:
                    c1 = p1.copy()
                    c2 = p2.copy()

                # Mutasi Gaussian
                for child in (c1, c2):
                    for l in range(dim):
                        if gen_rng.uniform(0.0, 1.0) < p_mut:
                            eps = gen_rng.normal(0.0, sigma_m[l])
                            child[l] += eps

                    offspring_list.append(child)
                    if len(offspring_list) >= n_offspring_needed:
                        break

            # 3. Evaluasi Populasi Keturunan
            if not offspring_list:
                break

            W_offspring = np.array(offspring_list)
            new_results = self.evaluate_population(W_offspring, evaluator)
            new_pop = [r["w"] for r in new_results]

            # 4. Gabungkan Elit + Keturunan Baru
            pop = elite_pop + new_pop
            results = elite_results + new_results

            # 5. Urutkan berdasarkan f_val
            pop, results = self._sort_population(pop, results)

        elapsed = time.perf_counter() - start_time
        meta = {
            "algorithm": "Genetic Algorithm (GA)",
            "dim": dim,
            "budget": budget,
            "n_pop": self.n_pop,
            "tournament_size": self.tournament_size,
            "p_crossover": self.p_crossover,
            "p_mutation": p_mut,
            "sigma_m_factor": self.sigma_m_factor,
            "elitism_count": self.elitism_count,
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
