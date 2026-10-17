"""Perhitungan Conditional Cost at Risk (CCaR).

Mengimplementasikan ukuran risiko ekor biaya portofolio:
- Persamaan 2.13:
    m = ceil((1 - alpha) * N)
    CCaR_alpha(w) = (1 / m) * sum_{s in S_alpha(w)} Cost_s(w)
    di mana S_alpha adalah himpunan indeks m biaya portofolio tertinggi.

Optimasi:
Menggunakan np.partition (kompleksitas O(N)) alih-alih pengurutan penuh np.sort (O(N log N)).
"""

import math
from typing import Union
import numpy as np


def compute_tail_count(n_scenarios: int, alpha: float = 0.95) -> int:
    """Menghitung jumlah skenario ekor m = ceil((1 - alpha) * N).

    Parameters
    ----------
    n_scenarios : int
        Jumlah total skenario N (misal 5.000).
    alpha : float
        Tingkat kepercayaan risiko (default: 0.95).

    Returns
    -------
    int
        Jumlah skenario pada ekor distribusi m.
    """
    if not (0.0 < alpha < 1.0):
        raise ValueError(f"alpha harus berada di dalam rentang (0, 1), didapat: {alpha}")
    if n_scenarios < 1:
        raise ValueError(f"n_scenarios harus bernilai minimal 1, didapat: {n_scenarios}")

    m = int(math.ceil((1.0 - alpha) * n_scenarios))
    return max(1, min(m, n_scenarios))


def compute_ccar(costs: np.ndarray, alpha: float = 0.95) -> float:
    """Menghitung nilai CCaR_alpha untuk satu vektor biaya skenario (Persamaan 2.13).

    Persamaan 2.13:
        m = ceil((1 - alpha) * N)
        CCaR_alpha(w) = (1 / m) * sum_{s in S_alpha} Cost_s

    Parameters
    ----------
    costs : np.ndarray
        Array 1-dimensi biaya portofolio untuk N skenario (Cost_s).
    alpha : float
        Tingkat kepercayaan (default: 0.95).

    Returns
    -------
    float
        Nilai rata-rata m biaya terbesar (CCaR).
    """
    costs = np.asarray(costs, dtype=float)
    if costs.ndim != 1:
        raise ValueError(f"Array costs harus 1-dimensi, didapat dimensi: {costs.ndim}")

    n = len(costs)
    m = compute_tail_count(n, alpha)

    # np.partition memindahkan m elemen terbesar ke m posisi paling kanan dalam O(N)
    tail_vals = np.partition(costs, n - m)[-m:]
    return float(np.mean(tail_vals))


def compute_ccar_batch(costs_batch: np.ndarray, alpha: float = 0.95) -> np.ndarray:
    """Menghitung nilai CCaR_alpha secara tervektorisasi untuk batch portofolio.

    Parameters
    ----------
    costs_batch : np.ndarray
        Array 2-dimensi berukuran (P, N), di mana P adalah ukuran populasi/batch
        dan N adalah jumlah skenario.
    alpha : float
        Tingkat kepercayaan (default: 0.95).

    Returns
    -------
    np.ndarray
        Array 1-dimensi berukuran (P,) berisi nilai CCaR tiap portofolio.
    """
    costs_batch = np.asarray(costs_batch, dtype=float)
    if costs_batch.ndim != 2:
        raise ValueError(f"costs_batch harus 2-dimensi (P, N), didapat: {costs_batch.ndim}")

    p, n = costs_batch.shape
    m = compute_tail_count(n, alpha)

    # Partisi sepanjang axis skenario (axis=1)
    tail_vals = np.partition(costs_batch, n - m, axis=1)[:, -m:]
    return np.mean(tail_vals, axis=1)
