"""Unit test untuk modul audit data mccar_kma.data.loader."""

from pathlib import Path
import pytest
import pandas as pd
import numpy as np

from mccar_kma.data.loader import (
    load_raw_sheet,
    load_data_awal,
    validate_data_awal,
    detect_missing_blocks,
    detect_extreme_jumps,
    compare_data_ir_sheets,
    compare_with_legacy,
)

RAW_EXCEL_PATH = Path("data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx")
LEGACY_DIR = Path("legacy/data_v0")


@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_load_raw_sheet():
    """Uji pemuatan sheet Excel dan penanganan NaN."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    assert isinstance(df_ir, pd.DataFrame)
    assert len(df_ir) == 3104
    assert "Tanggal" in df_ir.columns
    assert pd.api.types.is_datetime64_any_dtype(df_ir["Tanggal"])
    # Cek bahwa #N/A dibaca sebagai NaN
    assert df_ir["IR_JPY_5Y"].iloc[0] is np.nan or np.isnan(df_ir["IR_JPY_5Y"].iloc[0])


@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_load_and_validate_data_awal():
    """Uji pemuatan dan validasi matematis sheet Data Awal."""
    df_awal = load_data_awal(RAW_EXCEL_PATH)
    assert len(df_awal) == 7
    val = validate_data_awal(df_awal)
    assert val["sum_w0_is_one"] is True
    assert val["w0_within_bounds"] is True
    assert val["feasible_space_exists"] is True
    assert np.isclose(val["sum_lb"], 0.88)
    assert np.isclose(val["sum_ub"], 1.105)


@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_detect_missing_blocks():
    """Uji pendeteksian blok data hilang EUR_10Y dalam jendela."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    gaps = detect_missing_blocks(df_ir, sheet_name="Data IR")
    # Pastikan gap 163 baris EUR_10Y terdeteksi
    eur_gaps = [g for g in gaps if g["column"] == "IR_EUR_10Y" and g["length"] == 163]
    assert len(eur_gaps) == 1
    assert eur_gaps[0]["start_date"] == "2021-02-01"
    assert eur_gaps[0]["end_date"] == "2021-09-15"


@pytest.mark.skipif(not RAW_EXCEL_PATH.exists(), reason="Dataset mentah tidak tersedia")
def test_compare_data_ir_sheets():
    """Uji identitas Data IR vs Data IR_formula."""
    res = compare_data_ir_sheets(RAW_EXCEL_PATH)
    assert res["cols_match"] is True
    assert res["shape_match"] is True
    assert res["mismatches_count"] == 0
    assert res["is_identical"] is True


@pytest.mark.skipif(not RAW_EXCEL_PATH.exists() or not LEGACY_DIR.exists(), reason="Data atau legacy tidak tersedia")
def test_compare_with_legacy():
    """Uji kesamaan irisan lengkap 2.028 baris dengan file legacy."""
    df_ir = load_raw_sheet(RAW_EXCEL_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_EXCEL_PATH, "Data FX")
    sub_ir = df_ir[(df_ir["Tanggal"] >= "2017-07-03") & (df_ir["Tanggal"] <= "2025-11-24")].copy()
    sub_fx = df_fx[(df_fx["Tanggal"] >= "2017-07-03") & (df_fx["Tanggal"] <= "2025-11-24")].copy()
    complete_ir = sub_ir.dropna(subset=["IR_EUR_10Y"])
    complete_fx = sub_fx.loc[complete_ir.index]

    res = compare_with_legacy(complete_ir, complete_fx, LEGACY_DIR)
    assert res["rows_match"] is True
    assert res["dates_match"] is True
    assert res["categories_match"] is True
    assert res["max_diff_ir"] == 0.0
    assert res["max_diff_fx"] == 0.0
    assert res["is_identical"] is True
