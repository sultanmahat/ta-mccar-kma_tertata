"""Fungsi pembersihan dan pembentukan dataset pra-pemrosesan.

Menyediakan fungsi untuk memotong jendela analisis, membentuk dua varian dataset
(intersection dan spline), serta menghitung log-return dengan penanganan celah
163 hari pada varian intersection.
"""

from pathlib import Path
from typing import Optional, Tuple, Union

import numpy as np
import pandas as pd

from mccar_kma.data.loader import load_raw_sheet, compare_with_legacy
from mccar_kma.data.interpolation import interpolate_series_spline

# Nama-nama kolom 9 variabel pasar
IR_COLS = [
    "IR_USD_5Y",
    "IR_USD_10Y",
    "IR_USD_30Y",
    "IR_EUR_7Y",
    "IR_EUR_10Y",
    "IR_JPY_5Y",
    "IR_JPY_10Y",
]
FX_COLS = ["FX_USD/EUR", "FX_USD/JPY"]
ALL_MARKET_COLS = IR_COLS + FX_COLS
KATEGORI_COL = "Kategori"

WINDOW_START = "2017-07-03"
WINDOW_END = "2025-11-24"


def extract_window(
    df_ir: pd.DataFrame,
    df_fx: pd.DataFrame,
    start_date: str = WINDOW_START,
    end_date: str = WINDOW_END,
) -> pd.DataFrame:
    """Menggabungkan 7 kolom yield dan 2 kolom kurs ke satu DataFrame jendela.

    Parameters
    ----------
    df_ir : pd.DataFrame
        Sheet 'Data IR' dari file Excel (hasil load_raw_sheet).
    df_fx : pd.DataFrame
        Sheet 'Data FX' dari file Excel (hasil load_raw_sheet).
    start_date : str
        Tanggal awal jendela analisis (termasuk).
    end_date : str
        Tanggal akhir jendela analisis (termasuk).

    Returns
    -------
    pd.DataFrame
        DataFrame berisi kolom Tanggal, Kategori, 7 IR, 2 FX.
        Baris yang berada di luar jendela dibuang; indeks di-reset.
    """
    # Potong ke jendela
    mask_ir = (df_ir["Tanggal"] >= start_date) & (df_ir["Tanggal"] <= end_date)
    mask_fx = (df_fx["Tanggal"] >= start_date) & (df_fx["Tanggal"] <= end_date)

    sub_ir = df_ir.loc[mask_ir, ["Tanggal", KATEGORI_COL] + IR_COLS].copy()
    sub_fx = df_fx.loc[mask_fx, ["Tanggal"] + FX_COLS].copy()

    # Gabung berdasarkan tanggal
    merged = pd.merge(sub_ir, sub_fx, on="Tanggal", how="inner")
    merged = merged.sort_values("Tanggal").reset_index(drop=True)

    return merged


def create_intersection_dataset(df_window: pd.DataFrame) -> pd.DataFrame:
    """Varian dataset 'intersection': hanya baris dengan 9 seri lengkap.

    Membuang baris yang mengandung NaN pada kolom manapun dari 9 seri pasar.
    Sesuai spesifikasi: 2.191 − 163 = 2.028 baris.

    Parameters
    ----------
    df_window : pd.DataFrame
        DataFrame jendela analisis hasil extract_window().

    Returns
    -------
    pd.DataFrame
        DataFrame tanpa NaN, diharapkan 2.028 baris, indeks di-reset.
    """
    complete = df_window.dropna(subset=ALL_MARKET_COLS).copy()
    complete = complete.reset_index(drop=True)
    return complete


def create_spline_dataset(df_window: pd.DataFrame) -> pd.DataFrame:
    """Varian dataset 'spline': gap IR_EUR_10Y diisi interpolasi spline mandiri.

    Mengisi 163 nilai NaN pada kolom IR_EUR_10Y menggunakan NaturalCubicSpline
    (Persamaan 2.4–2.6). Kolom lain tidak diubah.

    Parameters
    ----------
    df_window : pd.DataFrame
        DataFrame jendela analisis hasil extract_window().

    Returns
    -------
    pd.DataFrame
        DataFrame 2.191 baris dengan 0 NaN pada semua 9 kolom pasar.
    """
    spline_df = df_window.copy()
    spline_df["IR_EUR_10Y"] = interpolate_series_spline(spline_df["IR_EUR_10Y"])
    spline_df = spline_df.reset_index(drop=True)
    return spline_df


def compute_log_returns(
    df: pd.DataFrame,
    cols: Optional[list] = None,
    exclude_gap: bool = False,
) -> pd.DataFrame:
    """Menghitung log-return harian r_t = ln(S_t / S_{t-1}).

    Persamaan 2.7: Delta c_{i,t} = ln(C_{i,t} / C_{i,t-1}).

    Untuk varian intersection (exclude_gap=True), baris log-return yang
    melintasi celah 163 hari (step tanggal > 4 hari kerja) dikeluarkan
    untuk menghindari lompatan artifisial bernilai 230 hari kalender.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame deret waktu bersih (tidak ada NaN).
    cols : Optional[list]
        Kolom yang dihitung log-return-nya. Default: semua kolom pasar.
    exclude_gap : bool
        Jika True, buang baris transisi tanggal dengan step > 4 hari kerja.

    Returns
    -------
    pd.DataFrame
        DataFrame log-return dengan kolom yang sama, tanpa baris NaN.
    """
    if cols is None:
        cols = ALL_MARKET_COLS

    vals = df[cols].to_numpy(dtype=float)
    log_returns = np.log(vals[1:] / vals[:-1])
    dates_ret = df["Tanggal"].iloc[1:].reset_index(drop=True)
    dates_prev = df["Tanggal"].iloc[:-1].reset_index(drop=True)

    result = pd.DataFrame(log_returns, columns=cols)
    result.insert(0, "Tanggal", dates_ret.values)
    result.insert(1, "Tanggal_prev", dates_prev.values)

    if exclude_gap:
        # Buang baris di mana lompatan tanggal > 4 hari kerja (gap 163 hari)
        step_days = (
            pd.to_datetime(result["Tanggal"]) - pd.to_datetime(result["Tanggal_prev"])
        ).dt.days
        gap_mask = step_days <= 4
        result = result.loc[gap_mask].reset_index(drop=True)

    result = result.drop(columns=["Tanggal_prev"])
    return result


def verify_intersection_vs_legacy(
    df_intersection: pd.DataFrame,
    legacy_dir: Union[str, Path] = "legacy/data_v0",
) -> dict:
    """Memeriksa kesamaan 100% dataset intersection dengan file acuan legacy.

    Parameters
    ----------
    df_intersection : pd.DataFrame
        Dataset intersection 2.028 baris.
    legacy_dir : Union[str, Path]
        Direktori legacy/.

    Returns
    -------
    dict
        Hasil perbandingan; 'is_identical' harus True.
    """
    df_ir_part = df_intersection[["Tanggal", KATEGORI_COL] + IR_COLS].copy()
    df_fx_part = df_intersection[["Tanggal"] + FX_COLS].copy()
    return compare_with_legacy(df_ir_part, df_fx_part, legacy_dir=legacy_dir)


def compute_comparison_stats(
    df_inter: pd.DataFrame,
    df_spline: pd.DataFrame,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Menghitung statistik komparasi log-return EUR_10Y dan korelasi lintas-variabel.

    Parameters
    ----------
    df_inter : pd.DataFrame
        Dataset intersection bersih (2.028 baris).
    df_spline : pd.DataFrame
        Dataset spline bersih (2.191 baris).

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame]
        (df_stats, df_corr): tabel statistik dasar dan tabel korelasi.
    """
    # Log-returns
    lr_inter = compute_log_returns(df_inter, exclude_gap=True)
    lr_spline = compute_log_returns(df_spline, exclude_gap=False)

    records = []
    for col in ALL_MARKET_COLS:
        ri = lr_inter[col].values
        rs = lr_spline[col].values
        records.append(
            {
                "seri": col,
                "n_inter": len(ri),
                "mean_inter": float(np.mean(ri)),
                "std_inter": float(np.std(ri, ddof=1)),
                "n_spline": len(rs),
                "mean_spline": float(np.mean(rs)),
                "std_spline": float(np.std(rs, ddof=1)),
            }
        )
    df_stats = pd.DataFrame(records)

    # Korelasi log-return EUR_10Y terhadap semua seri
    corr_inter = lr_inter[ALL_MARKET_COLS].corr()["IR_EUR_10Y"]
    corr_spline = lr_spline[ALL_MARKET_COLS].corr()["IR_EUR_10Y"]
    df_corr = pd.DataFrame(
        {
            "seri": ALL_MARKET_COLS,
            "corr_EUR10Y_inter": corr_inter.values,
            "corr_EUR10Y_spline": corr_spline.values,
        }
    )

    return df_stats, df_corr
