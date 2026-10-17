"""Modul pemuatan dan audit data mentah utang valas DJPPR.

Menyediakan fungsi-fungsi pembacaan dataset secara read-only dari file Excel,
deteksi blok data hilang, validasi kendala data awal, deteksi lonjakan ekstrem,
serta perbandingan kesamaan terhadap file acuan legacy.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd

# Penanda data hilang standar pada dataset DJPPR
DEFAULT_NA_VALUES = ["#N/A N/A", "#N/A", "NaN", "nan"]


def load_raw_sheet(
    filepath: Union[str, Path],
    sheet_name: str,
    na_values: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Membaca satu sheet dari file Excel dataset utama secara read-only.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path menuju file Excel mentah.
    sheet_name : str
        Nama sheet yang akan dibaca.
    na_values : Optional[List[str]]
        Daftar string yang dianggap sebagai NaN.

    Returns
    -------
    pd.DataFrame
        DataFrame hasil pembacaan sheet.
    """
    if na_values is None:
        na_values = DEFAULT_NA_VALUES

    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File dataset tidak ditemukan: {path}")

    df = pd.read_excel(path, sheet_name=sheet_name, na_values=na_values)
    if "Tanggal" in df.columns:
        df["Tanggal"] = pd.to_datetime(df["Tanggal"])
    return df


def load_data_awal(filepath: Union[str, Path]) -> pd.DataFrame:
    """Membaca sheet 'Data Awal' yang memuat komposisi eksisting dan batas proporsi.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path menuju file Excel mentah.

    Returns
    -------
    pd.DataFrame
        DataFrame informasi 7 instrumen utang valas.
    """
    df = load_raw_sheet(filepath, sheet_name="Data Awal")
    expected_cols = ["Instrument", "Curr", "Tenor (yr)", "Existing (2024)", "Min", "Max"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Kolom wajib '{col}' tidak ditemukan di sheet Data Awal")
    return df


def validate_data_awal(df_awal: pd.DataFrame) -> Dict[str, Any]:
    """Memvalidasi integritas komposisi eksisting w0 dan batas proporsi [lb, ub].

    Sesuai Spesifikasi §2 dan Persamaan 2.21:
    - sum(w0) == 1
    - lb_i <= w0_i <= ub_i untuk setiap instrumen
    - sum(lb) <= 1 <= sum(ub) sehingga ruang solusi layak tidak kosong.

    Parameters
    ----------
    df_awal : pd.DataFrame
        DataFrame sheet 'Data Awal'.

    Returns
    -------
    Dict[str, Any]
        Ringkasan hasil validasi matematis.
    """
    w0 = df_awal["Existing (2024)"]
    lb = df_awal["Min"]
    ub = df_awal["Max"]

    sum_w0 = float(w0.sum())
    sum_lb = float(lb.sum())
    sum_ub = float(ub.sum())

    w0_within_bounds = bool(((w0 >= lb) & (w0 <= ub)).all())
    feasible_space_exists = bool(sum_lb <= 1.0 <= sum_ub)
    sum_w0_is_one = bool(np.isclose(sum_w0, 1.0, atol=1e-8))

    return {
        "sum_w0": sum_w0,
        "sum_lb": sum_lb,
        "sum_ub": sum_ub,
        "sum_w0_is_one": sum_w0_is_one,
        "w0_within_bounds": w0_within_bounds,
        "feasible_space_exists": feasible_space_exists,
        "instruments_count": len(df_awal),
    }


def detect_missing_blocks(
    df: pd.DataFrame,
    date_col: str = "Tanggal",
    exclude_cols: Optional[List[str]] = None,
    sheet_name: str = "",
) -> List[Dict[str, Any]]:
    """Mendeteksi seluruh blok contiguous data hilang per kolom numerik.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame yang diuji.
    date_col : str
        Nama kolom tanggal.
    exclude_cols : Optional[List[str]]
        Daftar kolom yang dikecualikan dari pengecekan.
    sheet_name : str
        Nama sheet sumber untuk pelaporan.

    Returns
    -------
    List[Dict[str, Any]]
        Daftar blok gap (sheet, column, start_date, end_date, length).
    """
    if exclude_cols is None:
        exclude_cols = [date_col, "Kategori", "Unnamed: 9"]

    check_cols = [c for c in df.columns if c not in exclude_cols]
    gaps: List[Dict[str, Any]] = []

    for col in check_cols:
        is_null = df[col].isnull()
        in_block = False
        start_idx = 0

        for i, val in enumerate(is_null):
            if val and not in_block:
                in_block = True
                start_idx = i
            elif not val and in_block:
                in_block = False
                end_idx = i - 1
                gaps.append(
                    {
                        "sheet": sheet_name,
                        "column": col,
                        "start_date": str(df.loc[start_idx, date_col])[:10],
                        "end_date": str(df.loc[end_idx, date_col])[:10],
                        "length": end_idx - start_idx + 1,
                    }
                )

        if in_block:
            end_idx = len(df) - 1
            gaps.append(
                {
                    "sheet": sheet_name,
                    "column": col,
                    "start_date": str(df.loc[start_idx, date_col])[:10],
                    "end_date": str(df.loc[end_idx, date_col])[:10],
                    "length": end_idx - start_idx + 1,
                }
            )

    return gaps


def detect_extreme_jumps(
    df: pd.DataFrame,
    date_col: str = "Tanggal",
    target_cols: Optional[List[str]] = None,
    n_std: float = 5.0,
) -> pd.DataFrame:
    """Mendeteksi lonjakan harian ekstrem |dln| > n_std * std pada deret log-change.

    Sesuai spesifikasi dan prinsip pemodelan: lonjakan ini diidentifikasi
    dan dilaporkan, bukan dihapus (Preserve raw facts).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame deret waktu.
    date_col : str
        Nama kolom tanggal.
    target_cols : Optional[List[str]]
        Daftar kolom target.
    n_std : float
        Batas kelipatan simpangan baku (default 5.0).

    Returns
    -------
    pd.DataFrame
        Tabel berisi daftar observasi lonjakan ekstrem.
    """
    if target_cols is None:
        target_cols = [c for c in df.columns if c not in [date_col, "Kategori", "Unnamed: 9"]]

    records = []
    for col in target_cols:
        s = df[[date_col, col]].dropna().copy()
        if len(s) < 2:
            continue

        vals = s[col].to_numpy(dtype=float)
        dates = s[date_col].to_numpy()

        # Log change r_t = ln(S_t / S_{t-1})
        dln = np.log(vals[1:] / vals[:-1])
        mean = float(np.mean(dln))
        std = float(np.std(dln, ddof=1))

        if std == 0 or np.isnan(std):
            continue

        threshold = n_std * std
        outliers_idx = np.where(np.abs(dln) > threshold)[0]

        for idx in outliers_idx:
            records.append(
                {
                    "series": col,
                    "date": str(dates[idx + 1])[:10],
                    "prev_val": float(vals[idx]),
                    "curr_val": float(vals[idx + 1]),
                    "dln": float(dln[idx]),
                    "std": std,
                    "z_score": float(dln[idx] / std),
                }
            )

    return pd.DataFrame(records)


def compare_data_ir_sheets(filepath: Union[str, Path]) -> Dict[str, Any]:
    """Membandingkan sheet 'Data IR' dan 'Data IR_formula' pada file Excel asli.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path menuju file Excel.

    Returns
    -------
    Dict[str, Any]
        Hasil perbandingan (kesesuaian kolom, baris, dan isi sel).
    """
    df_ir = load_raw_sheet(filepath, "Data IR")
    df_formula = load_raw_sheet(filepath, "Data IR_formula")

    # Kolom ekstra 'Unnamed: 9' hanya ada di sheet Data IR
    has_unnamed = "Unnamed: 9" in df_ir.columns
    df_ir_clean = df_ir.drop(columns=["Unnamed: 9"]) if has_unnamed else df_ir

    cols_match = df_ir_clean.columns.tolist() == df_formula.columns.tolist()
    shape_match = df_ir_clean.shape == df_formula.shape

    mismatches = 0
    if cols_match and shape_match:
        for col in df_formula.columns:
            s1 = df_ir_clean[col]
            s2 = df_formula[col]
            match = (s1 == s2) | (s1.isnull() & s2.isnull())
            mismatches += int((~match).sum())

    return {
        "has_unnamed_in_ir": has_unnamed,
        "cols_match": cols_match,
        "shape_match": shape_match,
        "mismatches_count": mismatches,
        "is_identical": (cols_match and shape_match and mismatches == 0),
    }


def compare_with_legacy(
    df_complete_ir: pd.DataFrame,
    df_complete_fx: pd.DataFrame,
    legacy_dir: Union[str, Path],
) -> Dict[str, Any]:
    """Membandingkan irisan lengkap 9 seri (2.028 baris) dengan legacy CSV.

    Parameters
    ----------
    df_complete_ir : pd.DataFrame
        Irisan lengkap yield 7 instrumen dari Excel asli.
    df_complete_fx : pd.DataFrame
        Irisan lengkap kurs 2 valas dari Excel asli.
    legacy_dir : Union[str, Path]
        Direktori folder legacy (berisi ir_data_clean.csv dan fx_data_clean.csv).

    Returns
    -------
    Dict[str, Any]
        Perbandingan jumlah baris, rentang tanggal, dan selisih absolut maksimum.
    """
    leg_path = Path(legacy_dir)
    legacy_ir_file = leg_path / "ir_data_clean.csv"
    legacy_fx_file = leg_path / "fx_data_clean.csv"

    if not legacy_ir_file.exists() or not legacy_fx_file.exists():
        raise FileNotFoundError(f"File legacy tidak ditemukan di {leg_path}")

    legacy_ir = pd.read_csv(legacy_ir_file)
    legacy_fx = pd.read_csv(legacy_fx_file)

    legacy_ir["Tanggal"] = pd.to_datetime(legacy_ir["Tanggal"]).dt.strftime("%Y-%m-%d")
    legacy_fx["Tanggal"] = pd.to_datetime(legacy_fx["Tanggal"]).dt.strftime("%Y-%m-%d")

    comp_ir = df_complete_ir.copy()
    comp_fx = df_complete_fx.copy()
    comp_ir["Tanggal"] = pd.to_datetime(comp_ir["Tanggal"]).dt.strftime("%Y-%m-%d")
    comp_fx["Tanggal"] = pd.to_datetime(comp_fx["Tanggal"]).dt.strftime("%Y-%m-%d")

    # Pastikan urutan tanggal dan indeks seragam
    comp_ir = comp_ir.reset_index(drop=True)
    comp_fx = comp_fx.reset_index(drop=True)

    ir_cols = [c for c in comp_ir.columns if c not in ["Tanggal", "Kategori", "Unnamed: 9"]]
    fx_cols = [c for c in comp_fx.columns if c != "Tanggal"]

    rows_match = bool((len(comp_ir) == len(legacy_ir)) and (len(comp_fx) == len(legacy_fx)))
    dates_match = bool(
        (comp_ir["Tanggal"].values == legacy_ir["Tanggal"].values).all()
        and (comp_fx["Tanggal"].values == legacy_fx["Tanggal"].values).all()
    )

    max_diff_ir = float(
        np.max([np.nanmax(np.abs(comp_ir[c].values - legacy_ir[c].values)) for c in ir_cols])
    )
    max_diff_fx = float(
        np.max([np.nanmax(np.abs(comp_fx[c].values - legacy_fx[c].values)) for c in fx_cols])
    )
    categories_match = bool((comp_ir["Kategori"].values == legacy_ir["Kategori"].values).all())

    is_identical = bool(
        rows_match
        and dates_match
        and categories_match
        and max_diff_ir == 0.0
        and max_diff_fx == 0.0
    )

    return {
        "rows_count": len(comp_ir),
        "legacy_rows_count": len(legacy_ir),
        "rows_match": rows_match,
        "dates_match": dates_match,
        "categories_match": categories_match,
        "max_diff_ir": max_diff_ir,
        "max_diff_fx": max_diff_fx,
        "is_identical": is_identical,
    }
