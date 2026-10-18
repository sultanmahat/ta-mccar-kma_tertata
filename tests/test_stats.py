"""Pengujian unit untuk modul analisis statistik dan uji hipotesis non-parametrik (Tahap 13)."""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest
from scipy import stats

from mccar_kma.analysis.stats_tests import (
    kruskal_wallis_test,
    epsilon_squared,
    interpret_epsilon_squared,
    dunn_posthoc_test,
    rank_biserial_correlation,
    holm_bonferroni_correction,
)
from mccar_kma.analysis.summary import (
    compute_algorithm_summary,
    check_parametric_assumptions,
)


def test_kruskal_wallis_synthetic_manual():
    """Uji Kruskal-Wallis pada data sintetis yang nilai analitisnya dihitung manual."""
    # 3 kelompok berukuran n1=n2=n3=3, total N=9, tanpa ties
    g1 = np.array([1.0, 2.0, 3.0])
    g2 = np.array([4.0, 5.0, 6.0])
    g3 = np.array([7.0, 8.0, 9.0])

    # Perhitungan manual:
    # R1 = 1+2+3 = 6
    # R2 = 4+5+6 = 15
    # R3 = 7+8+9 = 24
    # H = (12 / 90) * (36/3 + 225/3 + 576/3) - 3(10)
    #   = (2/15) * (12 + 75 + 192) - 30 = (2/15) * 279 - 30 = 37.2 - 30 = 7.2
    # eps^2 = 7.2 / (9 - 1) = 7.2 / 8 = 0.90
    res = kruskal_wallis_test([g1, g2, g3], group_names=["A", "B", "C"])

    assert abs(res["H_raw"] - 7.2) < 1e-10
    assert abs(res["H_corrected"] - 7.2) < 1e-10
    assert abs(res["epsilon_squared"] - 0.9) < 1e-10
    assert res["epsilon_squared_interpretation"] == "Large (>= 0.26)"
    assert res["scipy_match"] is True

    # Cek derajat bebas dan p-value
    assert res["df"] == 2
    scipy_h, scipy_p = stats.kruskal(g1, g2, g3)
    assert abs(res["H_stat"] - scipy_h) < 1e-10
    assert abs(res["p_value"] - scipy_p) < 1e-10


def test_dunn_synthetic_manual():
    """Uji post-hoc Dunn pada data sintetis yang nilainya dihitung manual."""
    g1 = np.array([1.0, 2.0, 3.0])
    g2 = np.array([4.0, 5.0, 6.0])
    g3 = np.array([7.0, 8.0, 9.0])

    # Manual:
    # R_bar_1 = 2.0, R_bar_2 = 5.0, R_bar_3 = 8.0
    # var_base = 9 * 10 / 12 = 7.5
    # se = sqrt(7.5 * (1/3 + 1/3)) = sqrt(5.0) = 2.236067977...
    # z(A vs C) = (2.0 - 8.0) / sqrt(5.0) = -6.0 / 2.236067977 = -2.68328157...
    df_dunn = dunn_posthoc_test([g1, g2, g3], group_names=["A", "B", "C"])

    assert len(df_dunn) == 3  # A vs B, A vs C, B vs C

    row_ac = df_dunn[df_dunn["comparison"] == "A vs C"].iloc[0]
    expected_z = -6.0 / np.sqrt(5.0)
    assert abs(row_ac["z_stat"] - expected_z) < 1e-6
    assert abs(row_ac["rank_diff"] - (-6.0)) < 1e-10

    # Pastikan Holm p-value monotonik dan valid [0, 1]
    for _, r in df_dunn.iterrows():
        assert 0.0 <= r["p_unadjusted"] <= 1.0
        assert 0.0 <= r["p_holm"] <= 1.0
        assert r["p_holm"] >= r["p_unadjusted"]


def test_rank_biserial_properties():
    """Uji sifat matematis korelasi Rank-Biserial."""
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([4.0, 5.0, 6.0])

    # Seluruh x < y -> Mann-Whitney U_x = 0 -> r_rb = 1 - 0 = +1.0
    r_xy = rank_biserial_correlation(x, y)
    assert abs(r_xy - 1.0) < 1e-10

    # Seluruh y > x -> r_rb(y, x) = -1.0
    r_yx = rank_biserial_correlation(y, x)
    assert abs(r_yx - (-1.0)) < 1e-10

    # Antisimetri
    assert abs(r_xy + r_yx) < 1e-10

    # Sampel identik
    r_xx = rank_biserial_correlation(x, x)
    assert abs(r_xx - 0.0) < 1e-10


def test_ties_correction_d7():
    """Uji pengaruh faktor koreksi ties (D7) pada Kruskal-Wallis dan Dunn."""
    # Data dengan nilai kembar:
    # 2 muncul 3 kali (t1=3), 4 muncul 3 kali (t2=3)
    g1 = np.array([1.0, 2.0, 2.0])
    g2 = np.array([2.0, 3.0, 4.0])
    g3 = np.array([4.0, 4.0, 5.0])

    res_with_ties = kruskal_wallis_test([g1, g2, g3], ties_correction=True)
    res_no_ties = kruskal_wallis_test([g1, g2, g3], ties_correction=False)

    assert res_with_ties["has_ties"] is True
    # H terkoreksi ties harus lebih besar dari H mentah: H_c = H_raw / C_ties (karena C_ties < 1)
    assert res_with_ties["H_stat"] > res_no_ties["H_stat"]
    assert res_with_ties["c_ties"] < 1.0
    # Harus cocok persis dengan scipy.stats.kruskal
    scipy_h, _ = stats.kruskal(g1, g2, g3)
    assert abs(res_with_ties["H_stat"] - scipy_h) < 1e-10

    # Uji Dunn dengan dan tanpa koreksi ties
    df_dunn_ties = dunn_posthoc_test([g1, g2, g3], ties_correction=True)
    df_dunn_noties = dunn_posthoc_test([g1, g2, g3], ties_correction=False)

    # Variansi dengan koreksi ties lebih kecil, sehingga z-stat absolut sedikit lebih besar
    z_ties = abs(df_dunn_ties.iloc[0]["z_stat"])
    z_noties = abs(df_dunn_noties.iloc[0]["z_stat"])
    assert z_ties > z_noties


def test_holm_bonferroni_correction():
    """Uji algoritma koreksi Holm-Bonferroni."""
    p_vals = [0.01, 0.04, 0.03]
    # Urutkan: 0.01, 0.03, 0.04
    # m = 3
    # p1_adj = 0.01 * 3 = 0.03
    # p2_adj = max(0.03, 0.03 * 2) = 0.06
    # p3_adj = max(0.06, 0.04 * 1) = 0.06
    # Hasil urutan asli [0.01, 0.04, 0.03]: [0.03, 0.06, 0.06]
    adj = holm_bonferroni_correction(p_vals)
    expected = np.array([0.03, 0.06, 0.06])
    assert np.allclose(adj, expected, atol=1e-10)


def test_real_experiment_stats_pipeline():
    """Uji integrasi pemrosesan statistik pada data eksperimen riil runs_summary.csv."""
    runs_csv = Path("results/tables/runs_summary.csv")
    if not runs_csv.exists():
        pytest.skip("runs_summary.csv belum tersedia.")

    df = pd.read_csv(runs_csv)
    sub = df[df["config_id"] == "gross_djppr"]

    # 1. Ringkasan deskriptif
    desc = compute_algorithm_summary(sub, runs_dir=Path("results/runs"))
    assert len(desc) == 3
    assert set(desc["algo"]) == {"KMA", "GA", "PSO"}
    assert "iqr_cost" in desc.columns
    assert "mean_conv_eval" in desc.columns

    # 2. Uji asumsi parametrik
    assumptions = check_parametric_assumptions(sub)
    assert "shapiro_wilk" in assumptions
    assert "levene" in assumptions
    assert assumptions["parametric_valid"] is False  # Data eksperimen non-normal / heterogen

    # 3. Uji Kruskal-Wallis
    groups = [sub[sub["algo"] == a]["best_cost"].values for a in ["kma", "ga", "pso"]]
    kw = kruskal_wallis_test(groups, group_names=["KMA", "GA", "PSO"])
    assert kw["scipy_match"] is True
    assert kw["p_value"] < 0.001
    assert 0.0 <= kw["epsilon_squared"] <= 1.0

    # 4. Uji Dunn post-hoc
    dunn = dunn_posthoc_test(groups, group_names=["KMA", "GA", "PSO"])
    assert len(dunn) == 3
    assert "p_holm" in dunn.columns
    assert "rank_biserial" in dunn.columns
