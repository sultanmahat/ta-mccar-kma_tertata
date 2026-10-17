"""Perhitungan Marginal Conditional Cost at Risk (MCCaR) dan Dispersi Risiko J.

Mengimplementasikan ukuran risiko marjinal dan dispersi:
- Persamaan 2.14: Cost_s^{(+i)}(w; delta) = Cost_s(w) + delta * C_{s,i}
- Persamaan 2.16: MC_i(w) = Cost_bar^{(+i)}(w; delta) - Cost_bar(w) = delta * mean(C_{s,i})
- Persamaan 2.17: MCCaR_{alpha,i}(w) = CCaR_alpha^{(+i)}(w; delta) - CCaR_alpha(w)
- Persamaan 2.18: theta_i(w) = MCCaR_{alpha,i}(w) / MC_i(w),  MC_i != 0
- Persamaan 2.19: theta_bar(w) = (1 / n) * sum_{i=1}^n theta_i(w)
- Persamaan 2.20: J_MCCaR(w) = sqrt( (1 / n) * sum_{i=1}^n (theta_i(w) - theta_bar(w))^2 )
                  (pembagi n, bukan n - 1)

Keputusan D5:
Jika |MC_i| <= zero_tol (default 1e-12), theta_i di-set ke 0.0.
"""

from typing import Optional, Tuple, Union
import numpy as np

from mccar_kma.risk.ccar import compute_ccar, compute_tail_count


def compute_marginal_cost(cost_matrix: np.ndarray, delta: float = 0.01) -> np.ndarray:
    """Menghitung biaya marjinal MC_i (Persamaan 2.16).

    Persamaan 2.16:
        MC_i(w) = Cost_bar^{(+i)}(w; delta) - Cost_bar(w)
        Secara aljabar, MC_i = delta * mean_s(C_{s,i}), yang konstan terhadap w!

    Parameters
    ----------
    cost_matrix : np.ndarray
        Matriks biaya instrumen utang per skenario C berukuran (N, n).
    delta : float
        Tambahan penerbitan proporsi utang (default: 0.01 = 1%).

    Returns
    -------
    np.ndarray
        Vektor 1-dimensi berukuran (n,) berisi MC_i untuk setiap instrumen.
    """
    cost_matrix = np.asarray(cost_matrix, dtype=float)
    if cost_matrix.ndim != 2:
        raise ValueError(f"cost_matrix harus 2-dimensi (N, n), didapat: {cost_matrix.ndim}")

    return delta * np.mean(cost_matrix, axis=0)


def compute_mccar(
    cost_s: np.ndarray,
    delta_c_matrix: np.ndarray,
    ccar_base: float,
    alpha: float = 0.95,
) -> np.ndarray:
    """Menghitung nilai MCCaR_{alpha, i} untuk setiap instrumen i (Persamaan 2.17).

    Persamaan 2.14 & 2.17:
        Cost_s^{(+i)} = Cost_s + delta * C_{s,i}
        MCCaR_{alpha, i} = CCaR_alpha(Cost_s^{(+i)}) - ccar_base

    Aturan:
        Himpunan ekor S_alpha dipilih ULANG pada biaya yang sudah ditambah
        delta * C_{s,i} untuk setiap instrumen i.

    Parameters
    ----------
    cost_s : np.ndarray
        Array 1-dimensi biaya portofolio saat ini (Cost_s) berukuran (N,).
    delta_c_matrix : np.ndarray
        Matriks (delta * C) berukuran (N, n). Prekomputasi dari delta * C.
    ccar_base : float
        Nilai CCaR_alpha(w) portofolio dasar saat ini.
    alpha : float
        Tingkat kepercayaan (default: 0.95).

    Returns
    -------
    np.ndarray
        Vektor berukuran (n,) berisi MCCaR_i untuk setiap instrumen i.
    """
    n_scen, n_inst = delta_c_matrix.shape
    m = compute_tail_count(n_scen, alpha)

    mccar = np.empty(n_inst, dtype=float)

    for i in range(n_inst):
        # Biaya terganggu: Cost_s + delta * C_{s,i} (Persamaan 2.14)
        cost_pert = cost_s + delta_c_matrix[:, i]
        # Pilih ulang ekor m terbesar
        tail_vals = np.partition(cost_pert, n_scen - m)[-m:]
        ccar_pert = float(np.mean(tail_vals))
        # Persamaan 2.17
        mccar[i] = ccar_pert - ccar_base

    return mccar


def compute_theta(
    mccar: np.ndarray,
    mc: np.ndarray,
    zero_tol: float = 1e-12,
) -> Tuple[np.ndarray, float]:
    """Menghitung rasio theta_i dan rata-rata theta_bar (Persamaan 2.18 & 2.19).

    Persamaan 2.18:
        theta_i(w) = MCCaR_{alpha, i}(w) / MC_i(w),  MC_i != 0
        Keputusan D5: jika |MC_i| <= zero_tol, set theta_i = 0.0.

    Persamaan 2.19:
        theta_bar(w) = (1 / n) * sum_{i=1}^n theta_i(w)

    Parameters
    ----------
    mccar : np.ndarray
        Array (n,) berisi MCCaR tiap instrumen.
    mc : np.ndarray
        Array (n,) berisi MC tiap instrumen.
    zero_tol : float
        Ambang batas toleransi pembagian nol D5 (default: 1e-12).

    Returns
    -------
    Tuple[np.ndarray, float]
        (theta, theta_bar): array theta (n,) dan skalar rata-rata theta_bar.
    """
    mccar = np.asarray(mccar, dtype=float)
    mc = np.asarray(mc, dtype=float)

    # D5 guard: perlindungan terhadap MC_i mendekati nol
    safe_mc = np.where(np.abs(mc) <= zero_tol, np.nan, mc)
    theta = np.where(np.isnan(safe_mc), 0.0, mccar / safe_mc)

    theta_bar = float(np.mean(theta))
    return theta, theta_bar


def compute_j_mccar(theta: np.ndarray, theta_bar: Optional[float] = None) -> float:
    """Menghitung dispersi rasio risiko-biaya marjinal J_MCCaR (Persamaan 2.20).

    Persamaan 2.20:
        J_MCCaR(w) = sqrt( (1 / n) * sum_{i=1}^n (theta_i(w) - theta_bar(w))^2 )

    Catatan Penting:
        Pembagi di dalam akar adalah n (jumlah instrumen, n=7), BUKAN n - 1!
        (Lihat spesifikasi model §5: "pembagi n, bukan n-1").

    Parameters
    ----------
    theta : np.ndarray
        Array (n,) berisi rasio theta_i.
    theta_bar : Optional[float]
        Nilai rata-rata theta. Jika None, dihitung otomatis.

    Returns
    -------
    float
        Nilai simpangan baku populasi dari theta (J_MCCaR).
    """
    theta = np.asarray(theta, dtype=float)
    if theta_bar is None:
        theta_bar = float(np.mean(theta))

    # np.std dengan ddof=0 menggunakan pembagi n (populasi)
    return float(np.std(theta, ddof=0))
