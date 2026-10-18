"""Modul pengujian hipotesis non-parametrik (Tahap 13).

Mengimplementasikan:
1. Uji Kruskal-Wallis (Persamaan 2.37) mandiri dengan faktor koreksi ties.
2. Ukuran efek Epsilon-squared (Persamaan 2.39).
3. Uji lanjut post-hoc Dunn (Persamaan 2.38) dengan koreksi ties D7.
4. Koreksi multi-komparasi Holm-Bonferroni step-down.
5. Korelasi Rank-Biserial berbasis Mann-Whitney U.
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import itertools
import numpy as np
import pandas as pd
from scipy import stats


def kruskal_wallis_test(
    groups: List[np.ndarray],
    group_names: Optional[List[str]] = None,
    ties_correction: bool = True,
) -> Dict[str, Any]:
    """Menjalankan uji non-parametrik Kruskal-Wallis (Persamaan 2.37).

    Persamaan 2.37:
        H = 12 / (N(N+1)) * sum_g (R_g^2 / n_g) - 3(N+1)

    Koreksi Nilai Kembar (Ties):
        C_ties = 1 - sum(t_j^3 - t_j) / (N^3 - N)
        H_c = H / C_ties

    Parameters
    ----------
    groups : List[np.ndarray]
        Daftar array 1D berisi sampel data per kelompok.
    group_names : Optional[List[str]]
        Nama kelompok (misal ['KMA', 'GA', 'PSO']).
    ties_correction : bool
        Jika True, gunakan faktor koreksi ties C_ties (default: True).

    Returns
    -------
    Dict[str, Any]
        Dictionary berisi statistik H, H_c, df, p_value, mean_ranks, dll.
    """
    k = len(groups)
    if k < 2:
        raise ValueError("Kruskal-Wallis membutuhkan minimal 2 kelompok.")

    n_g = [len(g) for g in groups]
    N = int(sum(n_g))
    if N <= k:
        raise ValueError("Jumlah total observasi N harus lebih besar dari jumlah kelompok k.")

    if group_names is None:
        group_names = [f"Group_{i+1}" for i in range(k)]

    # 1. Gabungkan seluruh observasi dan hitung peringkat rata-rata (mid-ranks)
    all_data = np.concatenate(groups)
    ranks = stats.rankdata(all_data, method="average")

    # 2. Hitung jumlah peringkat R_g dan rata-rata peringkat R_bar_g per kelompok
    R_g = np.empty(k, dtype=float)
    R_bar_g = np.empty(k, dtype=float)
    idx_start = 0
    for i in range(k):
        idx_end = idx_start + n_g[i]
        group_ranks = ranks[idx_start:idx_end]
        R_g[i] = np.sum(group_ranks)
        R_bar_g[i] = R_g[i] / n_g[i]
        idx_start = idx_end

    # 3. Hitung statistik H mentah (Persamaan 2.37)
    sum_term = np.sum((R_g ** 2) / n_g)
    H_raw = (12.0 / (N * (N + 1.0))) * sum_term - 3.0 * (N + 1.0)

    # 4. Hitung faktor koreksi ties C_ties
    _, counts = np.unique(all_data, return_counts=True)
    tie_counts = counts[counts > 1]
    sum_t3_minus_t = np.sum(tie_counts ** 3 - tie_counts) if len(tie_counts) > 0 else 0.0

    if sum_t3_minus_t > 0.0:
        c_ties = 1.0 - (sum_t3_minus_t / (N ** 3 - N))
        H_corrected = H_raw / c_ties if c_ties > 0.0 else H_raw
    else:
        c_ties = 1.0
        H_corrected = H_raw

    # Pilih H yang digunakan
    H_stat = H_corrected if ties_correction else H_raw

    # Derajat bebas df = k - 1
    df = k - 1
    # p-value dari distribusi Chi-Square
    p_value = float(stats.chi2.sf(H_stat, df))

    # Ukuran efek Epsilon-squared (Persamaan 2.39)
    eps_sq = epsilon_squared(H_stat, N)

    # Cross-check dengan scipy.stats.kruskal
    scipy_res = stats.kruskal(*groups)
    scipy_h = float(scipy_res.statistic)
    scipy_p = float(scipy_res.pvalue)

    return {
        "H_raw": float(H_raw),
        "H_corrected": float(H_corrected),
        "H_stat": float(H_stat),
        "c_ties": float(c_ties),
        "has_ties": bool(sum_t3_minus_t > 0),
        "ties_sum": float(sum_t3_minus_t),
        "df": df,
        "p_value": p_value,
        "epsilon_squared": eps_sq,
        "epsilon_squared_interpretation": interpret_epsilon_squared(eps_sq),
        "group_names": group_names,
        "n_g": n_g,
        "R_g": R_g.tolist(),
        "R_bar_g": {group_names[i]: float(R_bar_g[i]) for i in range(k)},
        "scipy_h": scipy_h,
        "scipy_p": scipy_p,
        "scipy_match": bool(np.isclose(H_corrected, scipy_h, atol=1e-8)),
    }


def epsilon_squared(h_stat: float, n_total: int) -> float:
    """Menghitung ukuran efek Epsilon-squared (Persamaan 2.39).

    Persamaan 2.39:
        epsilon^2 = H / (N - 1)

    Parameters
    ----------
    h_stat : float
        Statistik Kruskal-Wallis H.
    n_total : int
        Jumlah total observasi N.

    Returns
    -------
    float
        Nilai ukuran efek dalam interval [0, 1].
    """
    if n_total <= 1:
        return 0.0
    val = float(h_stat / (n_total - 1.0))
    return float(np.clip(val, 0.0, 1.0))


def interpret_epsilon_squared(eps_sq: float) -> str:
    """Menginterpretasikan nilai ukuran efek Epsilon-squared (Tomczak & Tomczak, 2014).

    Kriteria:
        - < 0.01        : Negligible (Dapat diabaikan)
        - 0.01 - < 0.08 : Small (Kecil)
        - 0.08 - < 0.26 : Medium (Sedang)
        - >= 0.26       : Large (Besar)
    """
    if eps_sq < 0.01:
        return "Negligible (< 0.01)"
    elif eps_sq < 0.08:
        return "Small (0.01 - 0.08)"
    elif eps_sq < 0.26:
        return "Medium (0.08 - 0.26)"
    else:
        return "Large (>= 0.26)"


def rank_biserial_correlation(x: np.ndarray, y: np.ndarray) -> float:
    """Menghitung korelasi Rank-Biserial berbasis Mann-Whitney U.

    Formula:
        r_rb = 1 - 2 * U_x / (n_x * n_y)

    Interpretasi arah:
        - r_rb > 0: Kelompok x cenderung memiliki nilai lebih rendah (unggul dalam minimasi biaya).
        - r_rb < 0: Kelompok y cenderung memiliki nilai lebih rendah.
        - r_rb = 0: Distribusi seimbang.

    Parameters
    ----------
    x : np.ndarray
        Sampel kelompok x.
    y : np.ndarray
        Sampel kelompok y.

    Returns
    -------
    float
        Koefisien korelasi rank-biserial dalam interval [-1, 1].
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    nx = len(x)
    ny = len(y)
    if nx == 0 or ny == 0:
        return 0.0

    res = stats.mannwhitneyu(x, y, alternative="two-sided")
    u_x = float(res.statistic)

    r_rb = 1.0 - (2.0 * u_x) / (nx * ny)
    return float(np.clip(r_rb, -1.0, 1.0))


def holm_bonferroni_correction(p_values: Union[List[float], np.ndarray]) -> np.ndarray:
    """Menerapkan penyesuaian p-value Holm-Bonferroni (step-down).

    Parameters
    ----------
    p_values : Union[List[float], np.ndarray]
        Daftar atau array p-value tak terkoreksi.

    Returns
    -------
    np.ndarray
        Array p-value terkoreksi Holm dengan urutan yang sama seperti input.
    """
    p_vals = np.asarray(p_values, dtype=float)
    m = len(p_vals)
    if m <= 1:
        return np.clip(p_vals, 0.0, 1.0)

    # Urutkan indeks berdasarkan p-value dari terkecil ke terbesar
    sort_idx = np.argsort(p_vals)
    sorted_p = p_vals[sort_idx]

    # Hitung p terkoreksi step-down: min(1, (m - i) * p_i)
    adj_sorted = np.empty(m, dtype=float)
    for i in range(m):
        multiplier = m - i
        adj_sorted[i] = min(1.0, multiplier * sorted_p[i])

    # Pastikan monotonik tidak menurun: adj[i] = max(adj[i], adj[i-1])
    for i in range(1, m):
        if adj_sorted[i] < adj_sorted[i - 1]:
            adj_sorted[i] = adj_sorted[i - 1]

    # Kembalikan ke urutan semula
    adj_p = np.empty(m, dtype=float)
    adj_p[sort_idx] = adj_sorted
    return np.clip(adj_p, 0.0, 1.0)


def dunn_posthoc_test(
    groups: List[np.ndarray],
    group_names: Optional[List[str]] = None,
    ties_correction: bool = True,
    alpha: float = 0.05,
) -> pd.DataFrame:
    """Menjalankan uji lanjut post-hoc Dunn dengan koreksi Holm (Persamaan 2.38, D7).

    Persamaan 2.38:
        z_gh = (R_bar_g - R_bar_h) / sigma_gh

    Variansi tanpa koreksi ties:
        sigma_gh = sqrt( N(N+1) / 12 * (1/n_g + 1/n_h) )

    Variansi dengan koreksi ties (D7):
        sigma_gh_ties = sqrt( (N(N+1)/12 - sum(t_j^3 - t_j)/(12(N-1))) * (1/n_g + 1/n_h) )

    Parameters
    ----------
    groups : List[np.ndarray]
        Daftar array data kelompok.
    group_names : Optional[List[str]]
        Nama kelompok (misal ['KMA', 'GA', 'PSO']).
    ties_correction : bool
        Keputusan D7: gunakan koreksi ties jika True (default: True).
    alpha : float
        Taraf signifikansi uji (default: 0.05).

    Returns
    -------
    pd.DataFrame
        Tabel hasil uji Dunn per pasangan algoritma.
    """
    k = len(groups)
    if k < 2:
        raise ValueError("Dunn post-hoc test membutuhkan minimal 2 kelompok.")

    if group_names is None:
        group_names = [f"Group_{i+1}" for i in range(k)]

    n_g = [len(g) for g in groups]
    N = int(sum(n_g))

    all_data = np.concatenate(groups)
    ranks = stats.rankdata(all_data, method="average")

    # Hitung rata-rata peringkat R_bar_g
    R_bar_g = []
    idx_start = 0
    for i in range(k):
        idx_end = idx_start + n_g[i]
        R_bar_g.append(float(np.mean(ranks[idx_start:idx_end])))
        idx_start = idx_end

    # Hitung faktor koreksi ties
    _, counts = np.unique(all_data, return_counts=True)
    tie_counts = counts[counts > 1]
    sum_t3_minus_t = np.sum(tie_counts ** 3 - tie_counts) if len(tie_counts) > 0 else 0.0

    var_base = (N * (N + 1.0)) / 12.0
    if ties_correction and sum_t3_minus_t > 0:
        var_base -= sum_t3_minus_t / (12.0 * (N - 1.0))

    # Bangkitkan seluruh pasangan perbandingan berpasangan (g, h)
    pairs = list(itertools.combinations(range(k), 2))
    rows = []
    unadj_p_list = []

    for g_idx, h_idx in pairs:
        g_name = group_names[g_idx]
        h_name = group_names[h_idx]

        r_diff = R_bar_g[g_idx] - R_bar_g[h_idx]
        se = np.sqrt(var_base * (1.0 / n_g[g_idx] + 1.0 / n_g[h_idx]))

        if se > 0.0:
            z_stat = r_diff / se
        else:
            z_stat = 0.0

        p_unadj = float(2.0 * stats.norm.sf(abs(z_stat)))
        unadj_p_list.append(p_unadj)

        # Rank-biserial correlation
        r_rb = rank_biserial_correlation(groups[g_idx], groups[h_idx])

        rows.append({
            "comparison": f"{g_name} vs {h_name}",
            "group_1": g_name,
            "group_2": h_name,
            "mean_rank_1": R_bar_g[g_idx],
            "mean_rank_2": R_bar_g[h_idx],
            "rank_diff": r_diff,
            "se": float(se),
            "z_stat": float(z_stat),
            "p_unadjusted": p_unadj,
            "rank_biserial": r_rb,
        })

    # Terapkan koreksi Holm-Bonferroni
    holm_p_list = holm_bonferroni_correction(unadj_p_list)

    for i, p_h in enumerate(holm_p_list):
        rows[i]["p_holm"] = float(p_h)
        rows[i]["is_significant"] = bool(p_h < alpha)
        rows[i]["conclusion"] = (
            f"Signifikan (p_holm < {alpha})"
            if p_h < alpha
            else f"Tidak Signifikan (p_holm >= {alpha})"
        )

    return pd.DataFrame(rows)
