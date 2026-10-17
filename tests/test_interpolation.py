"""Unit test untuk Natural Cubic Spline (Persamaan 2.4–2.6) dan pipeline cleaning.

Menguji sifat matematis kritis:
1. Presisi terhadap scipy (selisih < 1e-8)
2. Interpolasi tepat di titik simpul (g(x_i) = y_i)
3. Syarat batas natural (c_0 = c_{n-1} = 0)
4. Gap 163 hari diisi 163 nilai positif dan halus
5. Varian intersection identik 100% dengan legacy CSV
"""

from pathlib import Path
import pytest
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

from mccar_kma.data.interpolation import NaturalCubicSpline, interpolate_series_spline
from mccar_kma.data.cleaning import (
    extract_window,
    create_intersection_dataset,
    create_spline_dataset,
    compute_log_returns,
    verify_intersection_vs_legacy,
    ALL_MARKET_COLS,
)
from mccar_kma.data.loader import load_raw_sheet

RAW_EXCEL_PATH = Path("data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx")
LEGACY_DIR = Path("legacy/data_v0")

# =============================================================================
# Fixture data sederhana untuk pengujian unit spline
# =============================================================================
@pytest.fixture
def simple_knots():
    x = np.array([0.0, 1.0, 2.0, 4.0, 7.0])
    y = np.array([1.5, 3.2, 2.1, 5.0, 4.3])
    return x, y


@pytest.fixture
def fitted_spline(simple_knots):
    x, y = simple_knots
    sp = NaturalCubicSpline()
    sp.fit(x, y)
    return sp, x, y


# =============================================================================
# 1. Uji Presisi terhadap Scipy (selisih < 1e-8)
# =============================================================================
def test_spline_vs_scipy(simple_knots, fitted_spline):
    """Persamaan 2.4–2.6: selisih maksimum terhadap scipy harus < 1e-8."""
    x, y = simple_knots
    sp, _, _ = fitted_spline

    cs_scipy = CubicSpline(x, y, bc_type="natural")
    x_eval = np.linspace(x[0], x[-1], 200)
    y_scipy = cs_scipy(x_eval)
    y_manual = sp.predict(x_eval)

    max_err = float(np.max(np.abs(y_scipy - y_manual)))
    assert max_err < 1e-8, f"Selisih maksimum terhadap scipy = {max_err:.2e} (harus < 1e-8)"


# =============================================================================
# 2. Uji Interpolasi Sempurna di Titik Simpul
# =============================================================================
def test_spline_exact_at_knots(fitted_spline):
    """g(x_i) = y_i untuk semua titik simpul."""
    sp, x, y = fitted_spline
    y_pred = sp.predict(x)
    max_err = float(np.max(np.abs(y_pred - y)))
    assert max_err < 1e-12, f"Tidak tepat di simpul: max error = {max_err:.2e}"


# =============================================================================
# 3. Uji Syarat Batas Natural (c_0 = c_{n-1} = 0)
# =============================================================================
def test_natural_boundary_conditions(fitted_spline):
    """Syarat batas natural: turunan kedua di ujung = 0 (Persamaan 2.4)."""
    sp, _, _ = fitted_spline
    c_left, c_right = sp.c_boundary
    assert abs(c_left) < 1e-14, f"c_batas_kiri = {c_left} (harus = 0)"
    assert abs(c_right) < 1e-14, f"c_batas_kanan = {c_right} (harus = 0)"


# =============================================================================
# 4. Uji Monotonisitas pada Dataset Non-Monoton (tidak crash)
# =============================================================================
def test_spline_non_monotone_y():
    """Spline harus berfungsi normal pada data tidak monoton."""
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([0.5, 2.1, 1.8, 3.5, 2.9, 4.0])
    sp = NaturalCubicSpline()
    sp.fit(x, y)
    y_pred = sp.predict(x)
    assert np.allclose(y_pred, y, atol=1e-10)


# =============================================================================
# 5. Uji interpolate_series_spline: tidak ada NaN di output
# =============================================================================
def test_interpolate_series_no_nan():
    """Setelah spline, tidak ada NaN tersisa di Series."""
    s = pd.Series([1.0, np.nan, np.nan, 2.0, 3.5, np.nan, 4.0])
    result = interpolate_series_spline(s)
    assert result.isna().sum() == 0, "Masih ada NaN setelah interpolasi spline."
    assert result[0] == pytest.approx(1.0)
    assert result[3] == pytest.approx(2.0)


# =============================================================================
# 6. Uji dengan Dataset Riil: Gap 163 Hari EUR_10Y
# =============================================================================
@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_spline_fills_163_gap():
    """Varian spline menghasilkan tepat 2.191 baris dengan 0 NaN pada semua kolom."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_EXCEL_PATH, "Data FX")
    df_window = extract_window(df_ir, df_fx)

    df_spline = create_spline_dataset(df_window)

    assert len(df_spline) == 2191, f"Panjang spline = {len(df_spline)} (harus 2191)"
    assert df_spline[ALL_MARKET_COLS].isna().sum().sum() == 0, "Masih ada NaN di dataset spline"
    assert (df_spline["IR_EUR_10Y"] > 0).all(), "Ada nilai non-positif di IR_EUR_10Y setelah spline"


# =============================================================================
# 7. Uji Varian Intersection: 2.028 Baris, 0 NaN
# =============================================================================
@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_intersection_shape_no_nan():
    """Varian intersection menghasilkan tepat 2.028 baris dengan 0 NaN."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_EXCEL_PATH, "Data FX")
    df_window = extract_window(df_ir, df_fx)

    df_inter = create_intersection_dataset(df_window)

    assert len(df_inter) == 2028, f"Panjang intersection = {len(df_inter)} (harus 2028)"
    assert df_inter[ALL_MARKET_COLS].isna().sum().sum() == 0, "Masih ada NaN di dataset intersection"


# =============================================================================
# 8. Uji Log-Return: Celah 163 Hari Dikeluarkan pada Intersection
# =============================================================================
@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_log_returns_gap_excluded():
    """Pada intersection, log-return yang melintasi celah 163 hari harus dikeluarkan."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_EXCEL_PATH, "Data FX")
    df_window = extract_window(df_ir, df_fx)
    df_inter = create_intersection_dataset(df_window)

    lr_with_gap = compute_log_returns(df_inter, exclude_gap=False)
    lr_without_gap = compute_log_returns(df_inter, exclude_gap=True)

    # Dengan exclude_gap: harus 1 baris lebih sedikit
    assert len(lr_without_gap) == len(lr_with_gap) - 1, (
        "Satu baris transisi gap harus dikeluarkan."
    )
    # Total log-return yang valid = 2028 - 2 = 2026 (bukan 2027)
    assert len(lr_without_gap) == 2026, f"Panjang lr_without_gap = {len(lr_without_gap)} (harus 2026)"


# =============================================================================
# 9. Uji Kesamaan Intersection vs Legacy CSV
# =============================================================================
@pytest.mark.skipif(
    not RAW_EXCEL_PATH.exists() or not LEGACY_DIR.exists(),
    reason="Dataset atau legacy tidak tersedia",
)
def test_intersection_identical_to_legacy():
    """Varian intersection harus 100% identik dengan legacy/data_v0/."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_EXCEL_PATH, "Data FX")
    df_window = extract_window(df_ir, df_fx)
    df_inter = create_intersection_dataset(df_window)

    result = verify_intersection_vs_legacy(df_inter, legacy_dir=LEGACY_DIR)

    assert result["is_identical"] is True, f"Intersection tidak identik dengan legacy: {result}"
    assert result["max_diff_ir"] == 0.0
    assert result["max_diff_fx"] == 0.0
