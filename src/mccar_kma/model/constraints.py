"""Penanganan kendala optimasi portofolio utang multivaluta.

Mengimplementasikan:
1. Proyeksi bobot iteratif ke himpunan layak sum(w) = 1 dan lb <= w <= ub:
   - Kliping ke [lb_i, ub_i]
   - Normalisasi ke jumlah 1
   - Diulang hingga kedua syarat terpenuhi dalam toleransi eps_tol = 1e-8
2. Evaluasi pelanggaran kendala relatif v_J(w) dan v_R(w) (Persamaan 2.23):
   - v_J(w) = max(0, (J_MCCaR(w) - eta) / max(|eta|, eps_tol))
   - v_R(w) = max(0, (CCaR_alpha(w) - tau) / max(|tau|, eps_tol))
"""

from typing import Tuple, Union
import numpy as np

# Batas proporsi DJPPR (Tabel 2.1 & 2.2 spesifikasi)
LB_DJPPR = np.array([0.425, 0.100, 0.130, 0.130, 0.015, 0.050, 0.030], dtype=float)
UB_DJPPR = np.array([0.490, 0.125, 0.165, 0.155, 0.030, 0.085, 0.055], dtype=float)

# Batas proporsi Free (0 <= w_i <= 1)
LB_FREE = np.zeros(7, dtype=float)
UB_FREE = np.ones(7, dtype=float)

# Bobot eksisting 2024 (w0) presisi penuh (Tabel 2.1 & 2.2)
W0 = np.array([
    0.459485835,
    0.113620854,
    0.147798763,
    0.143927407,
    0.024401992,
    0.066688212,
    0.044076937,
], dtype=float)


def project_weights(
    w: np.ndarray,
    lb: np.ndarray,
    ub: np.ndarray,
    max_iter: int = 1000,
    eps_tol: float = 1e-8,
) -> np.ndarray:
    """Memproyeksikan vektor bobot w ke ruang layak sum(w) = 1 dan lb <= w <= ub.

    Prosedur iteratif (§6 spesifikasi):
        1. Clip tiap bobot ke [lb_i, ub_i]
        2. Normalisasi w = w / sum(w)
        3. Ulangi sampai max(|w - clip(w)|) <= eps_tol dan |sum(w) - 1| <= eps_tol.

    Parameters
    ----------
    w : np.ndarray
        Vektor bobot kandidat berukuran (D,).
    lb : np.ndarray
        Batas bawah proporsi (D,).
    ub : np.ndarray
        Batas atas proporsi (D,).
    max_iter : int
        Jumlah iterasi maksimum (default: 1.000).
    eps_tol : float
        Toleransi numerik (default: 1e-8).

    Returns
    -------
    np.ndarray
        Vektor bobot terproyeksi yang memenuhi sum(w)=1 dan lb <= w <= ub.
    """
    w = np.asarray(w, dtype=float).copy()
    lb = np.asarray(lb, dtype=float)
    ub = np.asarray(ub, dtype=float)

    for _ in range(max_iter):
        clipped = np.clip(w, lb, ub)
        s = float(np.sum(clipped))

        # Guard: jika semua komponen nol atau negatif (s <= 0)
        if s <= 0.0:
            mid = (lb + ub) / 2.0
            w = mid / np.sum(mid)
            continue

        w_new = clipped / s
        max_clip_diff = float(np.max(np.abs(w_new - np.clip(w_new, lb, ub))))
        sum_diff = abs(float(np.sum(w_new)) - 1.0)

        if max_clip_diff <= eps_tol and sum_diff <= eps_tol:
            return w_new

        w = w_new

    # Kembalikan hasil terbaik yang terklip dan ternormalisasi
    clipped = np.clip(w, lb, ub)
    return clipped / np.sum(clipped)


def project_weights_batch(
    W: np.ndarray,
    lb: np.ndarray,
    ub: np.ndarray,
    max_iter: int = 1000,
    eps_tol: float = 1e-8,
) -> np.ndarray:
    """Memproyeksikan batch populasi bobot W (P x D) secara tervektorisasi.

    Parameters
    ----------
    W : np.ndarray
        Matriks populasi bobot berukuran (P, D).
    lb : np.ndarray
        Batas bawah proporsi (D,).
    ub : np.ndarray
        Batas atas proporsi (D,).
    max_iter : int
        Jumlah iterasi maksimum.
    eps_tol : float
        Toleransi numerik (default: 1e-8).

    Returns
    -------
    np.ndarray
        Matriks populasi bobot terproyeksi (P, D).
    """
    W = np.asarray(W, dtype=float).copy()
    lb = np.asarray(lb, dtype=float)
    ub = np.asarray(ub, dtype=float)

    mid = (lb + ub) / 2.0
    mid_norm = mid / np.sum(mid)

    for _ in range(max_iter):
        clipped = np.clip(W, lb, ub)
        s = np.sum(clipped, axis=1, keepdims=True)

        zero_mask = (s <= 0.0).squeeze()
        if np.any(zero_mask):
            clipped[zero_mask] = mid_norm
            s[zero_mask] = 1.0

        W_new = clipped / s
        max_clip_diff = np.max(np.abs(W_new - np.clip(W_new, lb, ub)), axis=1)
        sum_diff = np.abs(np.sum(W_new, axis=1) - 1.0)

        converged = (max_clip_diff <= eps_tol) & (sum_diff <= eps_tol)
        if np.all(converged):
            return W_new

        W = W_new

    clipped = np.clip(W, lb, ub)
    return clipped / np.sum(clipped, axis=1, keepdims=True)


def check_weight_feasibility(
    w: np.ndarray,
    lb: np.ndarray,
    ub: np.ndarray,
    eps_tol: float = 1e-8,
) -> bool:
    """Memeriksa apakah vektor bobot memenuhi batas proporsi dan jumlah 1.

    Parameters
    ----------
    w : np.ndarray
        Vektor bobot (D,).
    lb : np.ndarray
        Batas bawah (D,).
    ub : np.ndarray
        Batas atas (D,).
    eps_tol : float
        Toleransi numerik.

    Returns
    -------
    bool
        True jika lb - eps <= w <= ub + eps dan |sum(w) - 1| <= eps.
    """
    w = np.asarray(w, dtype=float)
    lb = np.asarray(lb, dtype=float)
    ub = np.asarray(ub, dtype=float)

    sum_ok = abs(float(np.sum(w)) - 1.0) <= eps_tol
    bounds_ok = bool(np.all(w >= lb - eps_tol) and np.all(w <= ub + eps_tol))
    return sum_ok and bounds_ok


def compute_relative_violations(
    j_mccar: float,
    ccar: float,
    eta: float,
    tau: float,
    eps_tol: float = 1e-8,
) -> Tuple[float, float]:
    """Menghitung pelanggaran kendala relatif v_J(w) dan v_R(w) (Persamaan 2.23).

    Persamaan 2.23:
        v_J(w) = max(0, (J_MCCaR(w) - eta) / max(|eta|, eps_tol))
        v_R(w) = max(0, (CCaR_alpha(w) - tau) / max(|tau|, eps_tol))

    Parameters
    ----------
    j_mccar : float
        Nilai dispersi risiko portofolio J_MCCaR(w).
    ccar : float
        Nilai risiko ekor portofolio CCaR_alpha(w).
    eta : float
        Threshold dispersi acuan baseline J_MCCaR(w0).
    tau : float
        Threshold risiko ekor acuan baseline CCaR_alpha(w0).
    eps_tol : float
        Toleransi numerik pembagi (default: 1e-8).

    Returns
    -------
    Tuple[float, float]
        (v_J, v_R): Nilai pelanggaran relatif non-negatif.
    """
    denom_eta = max(abs(eta), eps_tol)
    denom_tau = max(abs(tau), eps_tol)

    v_J = max(0.0, (j_mccar - eta) / denom_eta)
    v_R = max(0.0, (ccar - tau) / denom_tau)

    return float(v_J), float(v_R)


def compute_relative_violations_batch(
    j_mccar_arr: np.ndarray,
    ccar_arr: np.ndarray,
    eta: float,
    tau: float,
    eps_tol: float = 1e-8,
) -> Tuple[np.ndarray, np.ndarray]:
    """Versi batch untuk perhitungan pelanggaran kendala relatif populasi."""
    denom_eta = max(abs(eta), eps_tol)
    denom_tau = max(abs(tau), eps_tol)

    v_J = np.maximum(0.0, (j_mccar_arr - eta) / denom_eta)
    v_R = np.maximum(0.0, (ccar_arr - tau) / denom_tau)

    return v_J, v_R
