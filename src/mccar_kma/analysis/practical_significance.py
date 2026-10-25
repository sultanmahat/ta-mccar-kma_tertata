"""Analisis signifikansi praktis komparasi KMA/GA/PSO (Tahap 19-20).

Melengkapi uji inferensial Tahap 13 (Kruskal-Wallis, Dunn; lihat
`mccar_kma.analysis.stats_tests`) dengan ukuran beda praktis: estimator lokasi
Hodges-Lehmann, interval kepercayaan bootstrap, uji ekivalensi (TOST dan
CI-vs-margin), status kendala aktif (J, CCaR) dan vertex kotak-simpleks
("optimum LP"), serta uji eksak Fisher/Barnard untuk tabel kelayakan validasi
2x2. Modul ini hanya membaca ulang hasil yang sudah ada (`results/runs`,
`results/tables`) — tidak menjalankan optimasi baru.
"""

from __future__ import annotations

from typing import Any, Dict, Sequence, Tuple

import numpy as np
from scipy import stats


# ==============================================================================
# 1. Estimator Hodges-Lehmann dan interval bootstrap
# ==============================================================================

def hodges_lehmann_estimator(x: Sequence[float], y: Sequence[float]) -> float:
    """Estimator lokasi Hodges-Lehmann untuk dua sampel independen.

    Median dari seluruh selisih berpasangan x_i - y_j (n*m pasangan), estimator
    lokasi standar yang berasosiasi dengan uji Mann-Whitney U (dipakai oleh
    Kruskal-Wallis/Dunn di Tahap 13 untuk x, y yang dianggap independen, bukan
    berpasangan per-seed).
    """
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    diffs = xa[:, None] - ya[None, :]
    return float(np.median(diffs))


def bootstrap_hl_ci(
    x: Sequence[float],
    y: Sequence[float],
    resamples: int,
    seed: int,
    level: float,
) -> Tuple[float, float]:
    """CI bootstrap persentil untuk estimator Hodges-Lehmann (Generator ber-seed)."""
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    rng = np.random.default_rng(int(seed))
    idx_x = rng.integers(0, xa.size, size=(int(resamples), xa.size))
    idx_y = rng.integers(0, ya.size, size=(int(resamples), ya.size))
    hl_vals = np.empty(int(resamples), dtype=float)
    for b in range(int(resamples)):
        diffs = xa[idx_x[b]][:, None] - ya[idx_y[b]][None, :]
        hl_vals[b] = np.median(diffs)
    lo = (1.0 - level) / 2.0
    return (float(np.quantile(hl_vals, lo)), float(np.quantile(hl_vals, 1.0 - lo)))


def median_diff_pct(x: Sequence[float], y: Sequence[float]) -> Dict[str, float]:
    """Selisih median x - y dalam satuan asli dan persen relatif terhadap median y."""
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    med_x, med_y = float(np.median(xa)), float(np.median(ya))
    diff_abs = med_x - med_y
    diff_pct = 100.0 * diff_abs / med_y if med_y != 0 else float("nan")
    return {"median_x": med_x, "median_y": med_y, "diff_abs": diff_abs, "diff_pct": diff_pct}


# ==============================================================================
# 2. Uji ekivalensi: TOST non-parametrik dan CI-vs-margin
# ==============================================================================

def equivalence_test_tost(
    x: Sequence[float],
    y: Sequence[float],
    margin: float,
    alpha: float = 0.05,
) -> Dict[str, Any]:
    """Uji ekivalensi dua sisi (TOST) non-parametrik via Mann-Whitney bergeser.

    H0_low: median(x) - median(y) <= -margin  (diuji via x+margin vs y, alternative='greater')
    H0_high: median(x) - median(y) >= +margin (diuji via x-margin vs y, alternative='less')
    Ekivalen (pada level alpha) bila KEDUA p-value satu-sisi <= alpha;
    p_tost = max(p_low, p_high) sesuai konvensi TOST standar.
    """
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    p_low = float(stats.mannwhitneyu(xa + margin, ya, alternative="greater").pvalue)
    p_high = float(stats.mannwhitneyu(xa - margin, ya, alternative="less").pvalue)
    p_tost = max(p_low, p_high)
    return {
        "margin": float(margin),
        "p_low": p_low,
        "p_high": p_high,
        "p_tost": p_tost,
        "is_equivalent": bool(p_tost <= alpha),
    }


def equivalence_via_ci(hl_estimate: float, ci: Tuple[float, float], margin: float) -> bool:
    """Ekivalen bila CI estimator (mis. Hodges-Lehmann) seluruhnya di dalam [-margin, margin]."""
    lo, hi = ci
    return bool(lo >= -margin and hi <= margin)


# ==============================================================================
# 3. Kendala aktif (J, CCaR) dan vertex kotak-simpleks ("optimum LP")
# ==============================================================================

def constraint_activity_flags(
    j_mccar: float, eta: float, ccar: float, tau: float, rel_tol: float
) -> Dict[str, bool]:
    """Status kedekatan praktis solusi ke batas J<=eta dan CCaR<=tau.

    "Aktif" berarti slack relatif terhadap batas <= rel_tol (default longgar,
    1e-3, soal kedekatan praktis -- bukan toleransi kelayakan numerik solver
    optimization.eps_tol yang jauh lebih ketat, 1e-8).
    """
    j_active = bool(abs(eta - j_mccar) <= rel_tol * abs(eta)) if eta != 0 else False
    r_active = bool(abs(tau - ccar) <= rel_tol * abs(tau)) if tau != 0 else False
    return {"j_active": j_active, "r_active": r_active}


def box_vertex_flags(
    w: Sequence[float], lb: Sequence[float], ub: Sequence[float], bound_tol: float
) -> Dict[str, Any]:
    """Jumlah bobot w_i yang menempel di lb_i atau ub_i, dan status vertex kotak-simpleks.

    is_lp_vertex: True bila jumlah bobot di batas >= n-1 (kendala sum(w)=1 menyerap
    1 derajat bebas sisanya) -- yaitu kotak [lb,ub] bersama simpleks sum(w)=1 sudah
    cukup menentukan solusi tanpa perlu kendala risiko (J, CCaR) aktif.
    """
    wa = np.asarray(w, dtype=float)
    lba = np.asarray(lb, dtype=float)
    uba = np.asarray(ub, dtype=float)
    at_lb = np.abs(wa - lba) <= bound_tol
    at_ub = np.abs(wa - uba) <= bound_tol
    n_active = int(np.sum(at_lb | at_ub))
    n = wa.size
    return {"n_bound_active": n_active, "n_instruments": n, "is_lp_vertex": bool(n_active >= n - 1)}


def lp_vertex_feasible(
    w: Sequence[float],
    lb: Sequence[float],
    ub: Sequence[float],
    bound_tol: float,
    j_mccar: float,
    eta: float,
    ccar: float,
    tau: float,
    rel_tol: float,
) -> Dict[str, Any]:
    """Gabungan: vertex kotak-simpleks yang kebetulan sudah di dalam kendala risiko.

    lp_feasible = vertex kotak-simpleks DAN kendala J, CCaR TIDAK aktif (ada slack) --
    artinya minimisasi biaya linear atas kotak x simpleks saja (mengabaikan J, CCaR)
    sudah menghasilkan titik yang memenuhi J dan CCaR tanpa kendala itu menahan.
    """
    bv = box_vertex_flags(w, lb, ub, bound_tol)
    ca = constraint_activity_flags(j_mccar, eta, ccar, tau, rel_tol)
    lp_feasible_flag = bool(bv["is_lp_vertex"] and not ca["j_active"] and not ca["r_active"])
    return {**bv, **ca, "lp_feasible": lp_feasible_flag}


# ==============================================================================
# 4. Uji eksak tabel 2x2: Fisher dan Barnard
# ==============================================================================

def contingency_exact_test(table_2x2: Sequence[Sequence[int]]) -> Dict[str, float]:
    """Uji eksak Fisher dan Barnard untuk tabel kontingensi 2x2.

    table_2x2 = [[a, b], [c, d]] dengan baris = kelompok (mis. algoritma A, B),
    kolom = status (layak, tidak layak).
    """
    tbl = np.asarray(table_2x2, dtype=int)
    _, p_fisher = stats.fisher_exact(tbl)
    barnard_res = stats.barnard_exact(tbl)
    return {"p_fisher": float(p_fisher), "p_barnard": float(barnard_res.pvalue)}
