"""Fungsi penalti kendala, pelacak anggaran evaluasi, dan arsip solusi layak.

Mengimplementasikan:
1. Fungsi kualitas (fitness function) f(w) dengan penalti kuadratik (Persamaan 2.24):
   f(w) = Cost_bar(w) + rho_J * v_J(w)^2 + rho_R * v_R(w)^2
   dengan rho_J = rho_R = 1e6.
2. BudgetCounter:
   Melacak penggunaan anggaran evaluasi fungsi (maksimum 25.000 per replikasi).
3. FeasibleArchive:
   Menyimpan solusi layak terbaik (v_J <= 1e-8 dan v_R <= 1e-8) berdasarkan Cost_bar terendah
   (bukan sekadar nilai f terendah, sesuai spesifikasi §6 langkah 3).
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np


def compute_penalized_fitness(
    mean_cost: float,
    v_J: float,
    v_R: float,
    rho_J: float = 1e6,
    rho_R: float = 1e6,
) -> float:
    """Menghitung nilai fungsi kualitas f(w) dengan penalti kuadratik (Persamaan 2.24).

    Persamaan 2.24:
        f(w) = Cost_bar(w) + rho_J * v_J(w)^2 + rho_R * v_R(w)^2

    Parameters
    ----------
    mean_cost : float
        Rata-rata biaya portofolio Cost_bar(w).
    v_J : float
        Pelanggaran relatif kendala dispersi risiko v_J(w).
    v_R : float
        Pelanggaran relatif kendala risiko ekor v_R(w).
    rho_J : float
        Koefisien penalti kendala dispersi J (default: 1e6).
    rho_R : float
        Koefisien penalti kendala risiko CCaR (default: 1e6).

    Returns
    -------
    float
        Nilai fungsi objektif yang dipenalti f(w).
    """
    penalty = rho_J * (v_J ** 2) + rho_R * (v_R ** 2)
    return float(mean_cost + penalty)


def compute_penalized_fitness_batch(
    mean_cost_arr: np.ndarray,
    v_J_arr: np.ndarray,
    v_R_arr: np.ndarray,
    rho_J: float = 1e6,
    rho_R: float = 1e6,
) -> np.ndarray:
    """Versi batch untuk perhitungan fungsi penalti populasi (Persamaan 2.24)."""
    penalty = rho_J * (v_J_arr ** 2) + rho_R * (v_R_arr ** 2)
    return mean_cost_arr + penalty


class BudgetCounter:
    """Pelacak anggaran evaluasi fungsi untuk memastikan kepatuhan batas 25.000."""

    def __init__(self, max_evaluations: int = 25000) -> None:
        if max_evaluations < 1:
            raise ValueError(f"max_evaluations harus >= 1, didapat: {max_evaluations}")
        self._max = int(max_evaluations)
        self._count = 0

    @property
    def max_evaluations(self) -> int:
        return self._max

    @property
    def evaluations(self) -> int:
        return self._count

    @property
    def remaining(self) -> int:
        return max(0, self._max - self._count)

    @property
    def is_exhausted(self) -> bool:
        return self._count >= self._max

    def consume(self, n: int = 1) -> int:
        """Mencatat konsumsi n evaluasi fungsi.

        Returns
        -------
        int
            Jumlah evaluasi yang berhasil dicatat sebelum menyentuh batas.
        """
        if n < 0:
            raise ValueError(f"n tidak boleh negatif, didapat: {n}")
        allowed = min(n, self.remaining)
        self._count += allowed
        return allowed

    def reset(self) -> None:
        """Mereset penghitung evaluasi ke 0."""
        self._count = 0


@dataclass
class FeasibleSolution:
    """Representasi solusi layak portofolio."""
    w: np.ndarray
    mean_cost: float
    ccar: float
    j_mccar: float
    v_J: float
    v_R: float
    evaluation_index: int


class FeasibleArchive:
    """Arsip terpisah yang menyimpan solusi layak terbaik sepanjang pencarian.

    Aturan (§6 spesifikasi):
        Solusi akhir algoritma adalah solusi layak terbaik di arsip (v_J <= eps_tol
        dan v_R <= eps_tol) berdasarkan Cost_bar terendah, BUKAN sekadar nilai f terendah.
    """

    def __init__(self, eps_tol: float = 1e-8) -> None:
        self.eps_tol = float(eps_tol)
        self.best_solution: Optional[FeasibleSolution] = None
        self.total_feasible_count: int = 0
        self.history: List[FeasibleSolution] = []

    @property
    def is_empty(self) -> bool:
        return self.best_solution is None

    def is_feasible(self, v_J: float, v_R: float) -> bool:
        """Memeriksa apakah pelanggaran berada dalam batas toleransi numerik."""
        return bool(v_J <= self.eps_tol and v_R <= self.eps_tol)

    def update(
        self,
        w: np.ndarray,
        mean_cost: float,
        ccar: float,
        j_mccar: float,
        v_J: float,
        v_R: float,
        evaluation_index: int = 0,
    ) -> bool:
        """Memperbarui arsip jika kandidat layak dan memiliki mean_cost lebih rendah.

        Returns
        -------
        bool
            True jika kandidat menjadi solusi terbaik baru di arsip.
        """
        if not self.is_feasible(v_J, v_R):
            return False

        self.total_feasible_count += 1
        candidate = FeasibleSolution(
            w=np.asarray(w, dtype=float).copy(),
            mean_cost=float(mean_cost),
            ccar=float(ccar),
            j_mccar=float(j_mccar),
            v_J=float(v_J),
            v_R=float(v_R),
            evaluation_index=int(evaluation_index),
        )

        if self.best_solution is None or candidate.mean_cost < self.best_solution.mean_cost:
            self.best_solution = candidate
            self.history.append(candidate)
            return True

        return False
