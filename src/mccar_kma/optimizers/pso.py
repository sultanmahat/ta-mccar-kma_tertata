"""Implementasi Particle Swarm Optimization (PSO) untuk Portofolio Utang Multivaluta.

Berdasarkan:
1. Proposal Tesis Sultan Bakri Baihaqi Mahat (Subbab 2.9.2, Persamaan 2.35–2.36, Tabel 3.1).
2. Spesifikasi Model §7.3.
3. Keputusan Terbuka D6 (docs/decisions/0007-ga-pso-parameters-d6.md).

Operator & Mekanisme PSO:
- Ukuran kawanan: n_pop = 50.
- Bobot inersia dinamis: Turun linear dari omega_start = 0.9 ke omega_end = 0.4
  berdasarkan jumlah evaluasi fungsi terpakai (D6 Opsi A).
- Koefisien akselerasi kognitif dan sosial: c1 = c2 = 1.49618.
- Batas kecepatan maksimum: v_max_i = 0.2 * (ub_i - lb_i).
- Pembaruan kecepatan dan posisi (Persamaan 2.35–2.36):
  v_i^(t+1) = omega * v_i^(t) + c1 * r1 * (p_i - x_i^(t)) + c2 * r2 * (g - x_i^(t))
  x_i^(t+1) = x_i^(t) + v_i^(t+1)
- Proyeksi kendala: project_weights ke sum(w)=1 dan lb <= w <= ub.
- Konsistensi kecepatan pasca-proyeksi (D6 Opsi A):
  v_i^(t+1) disesuaikan dengan perpindahan efektif (x_proj - x_old).
- Anggaran: 25.000 evaluasi fungsi, dilacak ketat via BudgetCounter & FeasibleArchive.
"""

import time
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np

from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.model.constraints import project_weights


class ParticleSwarmOptimizer(BaseOptimizer):
    """Pengoptimal Particle Swarm Optimization (PSO).

    Parameters
    ----------
    n_pop : int
        Ukuran kawanan partikel (default: 50, Tabel 3.1).
    w_start : float
        Bobot inersia awal (default: 0.9, Tabel 3.1).
    w_end : float
        Bobot inersia akhir (default: 0.4, Tabel 3.1).
    c1 : float
        Koefisien akselerasi kognitif (default: 1.49618, Tabel 3.1).
    c2 : float
        Koefisien akselerasi sosial (default: 1.49618, Tabel 3.1).
    v_max_factor : float
        Faktor penentu batas kecepatan v_max = v_max_factor * (ub - lb)
        (default: 0.2, Tabel 3.1).
    velocity_clamp_strategy : str
        Strategi penyesuaian kecepatan pasca-proyeksi (default: "effective_displacement", D6).
    check_interval : int
        Interval evaluasi untuk pencatatan konvergensi (default: 250).
    eps_tol : float
        Toleransi numerik kendala (default: 1e-8).
    """

    def __init__(
        self,
        n_pop: int = 50,
        w_start: float = 0.9,
        w_end: float = 0.4,
        c1: float = 1.49618,
        c2: float = 1.49618,
        v_max_factor: float = 0.2,
        velocity_clamp_strategy: str = "effective_displacement",
        check_interval: int = 250,
        eps_tol: float = 1e-8,
    ) -> None:
        super().__init__(check_interval=check_interval, eps_tol=eps_tol)
        self.n_pop = int(n_pop)
        self.w_start = float(w_start)
        self.w_end = float(w_end)
        self.c1 = float(c1)
        self.c2 = float(c2)
        self.v_max_factor = float(v_max_factor)
        self.velocity_clamp_strategy = str(velocity_clamp_strategy)

    def run(
        self,
        evaluator: Any,
        lb: np.ndarray,
        ub: np.ndarray,
        budget: int = 25000,
        rng: Optional[Union[int, np.random.Generator]] = None,
    ) -> OptimizationResult:
        """Menjalankan algoritma PSO hingga anggaran evaluasi terpenuhi."""
        start_time = time.perf_counter()
        gen_rng = self._init_run(budget=budget, lb=lb, ub=ub, rng=rng)
        dim = len(self._lb)
        bound_range = np.abs(self._ub - self._lb)

        # Batas kecepatan maksimum per dimensi: v_max_i = 0.2 * (ub_i - lb_i)
        v_max = self.v_max_factor * bound_range

        # Ukuran kawanan awal tidak boleh melebihi anggaran
        pop_size = min(self.n_pop, budget)

        # ---------------------------------------------------------------------
        # Inisialisasi Posisi dan Kecepatan Kawanan Partikel (D6 Opsi A)
        # ---------------------------------------------------------------------
        raw_x = gen_rng.uniform(self._lb, self._ub, size=(pop_size, dim))
        results = self.evaluate_population(raw_x, evaluator)
        actual_size = len(results)

        # Posisi partikel saat ini
        X = np.array([r["w"] for r in results])

        # Kecepatan awal partikel di [-v_max, v_max]
        V = gen_rng.uniform(-v_max, v_max, size=(actual_size, dim))

        # Personal best (p_best) tiap partikel
        P_best = X.copy()
        P_best_fitness = np.array([r["f_val"] for r in results])

        # Global best (g_best) kawanan
        best_idx = int(np.argmin(P_best_fitness))
        g_best = P_best[best_idx].copy()
        g_best_fitness = float(P_best_fitness[best_idx])

        # ---------------------------------------------------------------------
        # Loop Iterasi Kawanan PSO
        # ---------------------------------------------------------------------
        while not self.budget.is_exhausted:
            rem_budget = self.budget.remaining
            if rem_budget <= 0:
                break

            current_size = len(X)
            if rem_budget < current_size:
                # Pangkas kawanan untuk generasi terakhir jika sisa anggaran < pop_size
                current_size = rem_budget
                X = X[:current_size]
                V = V[:current_size]
                P_best = P_best[:current_size]
                P_best_fitness = P_best_fitness[:current_size]

            # 1. Hitung bobot inersia dinamis omega(eval) sesuai D6 Opsi A
            eval_ratio = min(1.0, float(self.budget.evaluations) / float(self.budget.max_evaluations))
            omega = self.w_start - (self.w_start - self.w_end) * eval_ratio

            # 2. Pembangkitan bilangan acak r1, r2 ~ U(0, 1) berukuran (current_size, dim)
            r1 = gen_rng.uniform(0.0, 1.0, size=(current_size, dim))
            r2 = gen_rng.uniform(0.0, 1.0, size=(current_size, dim))

            # 3. Pembaruan Kecepatan (Persamaan 2.35):
            # v_i^(t+1) = omega * v_i^(t) + c1 * r1 * (p_i - x_i) + c2 * r2 * (g - x_i)
            cognitive = self.c1 * r1 * (P_best - X)
            social = self.c2 * r2 * (g_best - X)
            V_new = omega * V + cognitive + social

            # Clamping kecepatan ke [-v_max, v_max]
            V_clamped = np.clip(V_new, -v_max, v_max)

            # 4. Pembaruan Posisi (Persamaan 2.36) & Proyeksi Kendala
            X_raw = X + V_clamped
            X_new = np.empty_like(X_raw)

            for i in range(current_size):
                # Proyeksikan ke ruang layak sum(w)=1 dan lb <= w <= ub
                x_proj = project_weights(X_raw[i], self._lb, self._ub, eps_tol=self.eps_tol)
                X_new[i] = x_proj

                # Re-estimasi kecepatan efektif pasca-proyeksi (D6 Opsi A)
                if self.velocity_clamp_strategy == "effective_displacement":
                    eff_disp = x_proj - X[i]
                    V_clamped[i] = np.clip(eff_disp, -v_max, v_max)

            # 5. Evaluasi Posisi Baru
            new_results = self.evaluate_population(X_new, evaluator)
            if not new_results:
                break

            actual_evaluated = len(new_results)
            X = X_new[:actual_evaluated]
            V = V_clamped[:actual_evaluated]

            # 6. Pembaruan Personal Best & Global Best
            for i in range(actual_evaluated):
                f_cur = new_results[i]["f_val"]
                if f_cur < P_best_fitness[i]:
                    P_best[i] = X[i].copy()
                    P_best_fitness[i] = f_cur

                    if f_cur < g_best_fitness:
                        g_best = X[i].copy()
                        g_best_fitness = f_cur

        elapsed = time.perf_counter() - start_time
        meta = {
            "algorithm": "Particle Swarm Optimization (PSO)",
            "dim": dim,
            "budget": budget,
            "n_pop": self.n_pop,
            "w_start": self.w_start,
            "w_end": self.w_end,
            "c1": self.c1,
            "c2": self.c2,
            "v_max_factor": self.v_max_factor,
            "velocity_clamp_strategy": self.velocity_clamp_strategy,
        }
        return self._build_result(elapsed_seconds=elapsed, metadata=meta)
