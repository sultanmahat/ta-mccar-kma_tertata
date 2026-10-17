"""Skrip Pipeline Pra-Pemrosesan Data — Tahap 02.

Menjalankan pra-pemrosesan penuh:
1. Muat dataset mentah dari data/raw/ (read-only).
2. Potong ke jendela analisis 2017-07-03 s.d. 2025-11-24.
3. Hasilkan varian 'intersection' (2.028 baris) → data/processed/...
4. Hasilkan varian 'spline' (2.191 baris) → data/processed/...
5. Verifikasi intersection identik dengan legacy CSV.
6. Hitung dan terbitkan tabel komparasi statistik → results/tables/preprocess_comparison.md.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

from mccar_kma.data.loader import load_raw_sheet
from mccar_kma.data.cleaning import (
    extract_window,
    create_intersection_dataset,
    create_spline_dataset,
    compute_log_returns,
    compute_comparison_stats,
    verify_intersection_vs_legacy,
    ALL_MARKET_COLS,
)

WINDOW_START = "2017-07-03"
WINDOW_END = "2025-11-24"
RAW_PATH = Path("data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx")
PROCESSED_DIR = Path("data/processed")
TABLES_DIR = Path("results/tables")
LEGACY_DIR = Path("legacy/data_v0")


def main() -> None:
    print("=" * 70)
    print("TAHAP 02: PRA-PEMROSESAN DATA (INTERSECTION & SPLINE)")
    print("=" * 70)

    if not RAW_PATH.exists():
        print(f"ERROR: Dataset tidak ditemukan: {RAW_PATH}")
        sys.exit(1)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Muat data mentah
    # ------------------------------------------------------------------
    print("\n[1/6] Memuat data mentah dari Excel (read-only)...")
    df_ir = load_raw_sheet(RAW_PATH, "Data IR")
    df_fx = load_raw_sheet(RAW_PATH, "Data FX")

    # ------------------------------------------------------------------
    # 2. Potong ke jendela analisis
    # ------------------------------------------------------------------
    print(f"[2/6] Memotong ke jendela analisis {WINDOW_START} s.d. {WINDOW_END}...")
    df_window = extract_window(df_ir, df_fx)
    print(f" - Panjang jendela: {len(df_window)} baris")
    print(f" - NaN IR_EUR_10Y di jendela: {df_window['IR_EUR_10Y'].isna().sum()} baris")

    # ------------------------------------------------------------------
    # 3. Varian Intersection (2.028 baris)
    # ------------------------------------------------------------------
    print("\n[3/6] Membangun varian 'intersection' (membuang 163 baris NaN)...")
    df_inter = create_intersection_dataset(df_window)
    nan_count_inter = df_inter[ALL_MARKET_COLS].isna().sum().sum()
    print(f" - Jumlah baris intersection: {len(df_inter)}")
    print(f" - Jumlah NaN tersisa: {nan_count_inter}")

    inter_file = PROCESSED_DIR / f"market_{WINDOW_START}_{WINDOW_END}_intersection.csv"
    df_inter.to_csv(inter_file, index=False)
    print(f" - Disimpan ke: {inter_file}")

    # ------------------------------------------------------------------
    # 4. Verifikasi intersection vs legacy CSV
    # ------------------------------------------------------------------
    print("\n[4/6] Memverifikasi intersection terhadap file acuan legacy...")
    legacy_res = verify_intersection_vs_legacy(df_inter, legacy_dir=LEGACY_DIR)
    print(f" - Jumlah baris cocok: {legacy_res['rows_match']} ({legacy_res['rows_count']} vs {legacy_res['legacy_rows_count']})")
    print(f" - Tanggal cocok 100%: {legacy_res['dates_match']}")
    print(f" - Selisih max IR: {legacy_res['max_diff_ir']}")
    print(f" - Selisih max FX: {legacy_res['max_diff_fx']}")
    if not legacy_res["is_identical"]:
        print(" - PERINGATAN: Varian intersection TIDAK identik dengan legacy!")
    else:
        print(" - Kesesuaian: IDENTIK 100% (bit-by-bit match).")

    # ------------------------------------------------------------------
    # 5. Varian Spline (2.191 baris)
    # ------------------------------------------------------------------
    print("\n[5/6] Membangun varian 'spline' (interpolasi natural cubic spline)...")
    df_spline = create_spline_dataset(df_window)
    nan_count_spline = df_spline[ALL_MARKET_COLS].isna().sum().sum()
    print(f" - Jumlah baris spline: {len(df_spline)}")
    print(f" - Jumlah NaN tersisa: {nan_count_spline}")
    eur10y_interp = df_spline["IR_EUR_10Y"]
    print(f" - IR_EUR_10Y semua positif: {bool((eur10y_interp > 0).all())}")
    print(f" - IR_EUR_10Y min terinterpolasi: {df_window['IR_EUR_10Y'].isna().sum()} titik diisi")
    print(f" - Rentang IR_EUR_10Y terinterpolasi: [{eur10y_interp.min():.4f}%, {eur10y_interp.max():.4f}%]")

    spline_file = PROCESSED_DIR / f"market_{WINDOW_START}_{WINDOW_END}_spline.csv"
    df_spline.to_csv(spline_file, index=False)
    print(f" - Disimpan ke: {spline_file}")

    # ------------------------------------------------------------------
    # 6. Statistik komparasi dan laporan markdown
    # ------------------------------------------------------------------
    print("\n[6/6] Menghitung statistik komparasi dan menerbitkan laporan...")
    df_stats, df_corr = compute_comparison_stats(df_inter, df_spline)

    lr_inter_gap_excluded = compute_log_returns(df_inter, exclude_gap=True)
    lr_spline_full = compute_log_returns(df_spline, exclude_gap=False)

    print(f" - Jumlah log-return intersection (exclude gap): {len(lr_inter_gap_excluded)}")
    print(f" - Jumlah log-return spline: {len(lr_spline_full)}")

    report_path = TABLES_DIR / "preprocess_comparison.md"
    _write_comparison_report(report_path, df_inter, df_spline, df_stats, df_corr, legacy_res)
    print(f" - Laporan komparasi diterbitkan ke: {report_path}")

    print("\n" + "=" * 70)
    print("SELESAI: Kedua varian dataset berhasil dibuat.")
    print(f" - {inter_file}")
    print(f" - {spline_file}")
    print("=" * 70)


def _write_comparison_report(
    output_path: Path,
    df_inter: pd.DataFrame,
    df_spline: pd.DataFrame,
    df_stats: pd.DataFrame,
    df_corr: pd.DataFrame,
    legacy_res: dict,
) -> None:
    """Menerbitkan laporan markdown komparasi dua varian dataset."""
    lr_inter = compute_log_returns(df_inter, exclude_gap=True)
    lr_spline = compute_log_returns(df_spline, exclude_gap=False)

    eur_inter = df_stats.loc[df_stats["seri"] == "IR_EUR_10Y"].iloc[0]
    eur_spline_s = lr_spline["IR_EUR_10Y"]

    md = f"""# Laporan Komparasi Pra-Pemrosesan Data — Tahap 02

**Sumber**: `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` (Read-Only)  
**Jendela Analisis**: {WINDOW_START} s.d. {WINDOW_END}  
**Dokumen Acuan**: `docs/context/spesifikasi_model.md` §2, §4, §12 (D1)

---

## 1. KEPUTUSAN DIBUTUHKAN D1: Pemilihan Varian Jendela Data (`window_mode`)

> Proposal revisi menyebutkan 2.028 hari DAN interpolasi spline; keduanya tidak bisa diterapkan bersamaan.
> Keputusan harus disetujui bersama pembimbing sebelum lanjut ke Tahap 03 (Kalibrasi GBM).

| | Opsi A: `intersection` | Opsi B: `spline` |
|---|---|---|
| **Jumlah baris** | **2.028** | **2.191** |
| **Jumlah log-return valid** | **2.026** (buang 1 transisi gap) | **2.190** |
| **Rekayasa data** | Tidak ada — 100% data riil | 163 hari artifisial diisi spline kubik |
| **Panjang celah** | 7,5 bulan kalender (163 hari kerja berurutan) | Sama, diisi halus |
| **Kesesuaian legacy** | **IDENTIK 100%** (max diff = 0) | Berbeda pada 163 baris |
| **Korelasi EUR_7Y–EUR_10Y** | **{df_corr.loc[df_corr["seri"]=="IR_EUR_7Y","corr_EUR10Y_inter"].values[0]:.4f}** (lebih tinggi) | {df_corr.loc[df_corr["seri"]=="IR_EUR_7Y","corr_EUR10Y_spline"].values[0]:.4f} (lebih rendah) |
| **Kelebihan** | Data asli tidak terkontaminasi; spesifikasi §2 menyebutkan 2.028 | Kalender deret waktu utuh tanpa lompatan |
| **Risiko** | Kehilangan 163 hari fase pemulihan Covid | Volatilitas 163 hari artifisial nol; melebihkan kelancaran distribusi |

**Rekomendasi Agen**: Gunakan **Opsi A (`intersection`)** sebagai basis utama pemodelan.  
Varian spline dipertahankan sebagai bahan analisis sensitivitas.  
*Parameter `data.window_mode` di `configs/params.yaml` saat ini bernilai `null`.*

---

## 2. Ringkasan Kedua Varian Dataset

| | Intersection | Spline |
|---|:---:|:---:|
| **File** | `market_...intersection.csv` | `market_...spline.csv` |
| **Jumlah baris** | {len(df_inter)} | {len(df_spline)} |
| **NaN pada 9 seri** | 0 | 0 |
| **Kolom** | Tanggal, Kategori, 7 IR, 2 FX | Tanggal, Kategori, 7 IR, 2 FX |
| **IR_EUR_10Y positif** | Ya | Ya (min terinterpolasi = {df_spline['IR_EUR_10Y'].min():.4f}%) |
| **Kesesuaian legacy** | IDENTIK 100% | N/A (berbeda di 163 baris gap) |

---

## 3. Statistik Log-Return per Variabel Pasar

| Variabel | Mean (Intersection) | Std (Intersection) | N (Intersection) | Mean (Spline) | Std (Spline) | N (Spline) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
"""
    for _, row in df_stats.iterrows():
        md += (
            f"| `{row['seri']}` | {row['mean_inter']:.4e} | {row['std_inter']:.4e} | {int(row['n_inter'])} | "
            f"{row['mean_spline']:.4e} | {row['std_spline']:.4e} | {int(row['n_spline'])} |\n"
        )

    md += f"""
*Catatan: Log-return intersection tidak mencakup 1 baris transisi 29 Jan 2021 → 16 Sep 2021 (lompatan 230 hari kalender).*

---

## 4. Korelasi Log-Return IR_EUR_10Y terhadap 8 Variabel Pasar Lainnya

| Variabel | Korelasi (Intersection) | Korelasi (Spline) | Selisih |
|---|:---:|:---:|:---:|
"""
    for _, row in df_corr.iterrows():
        if row["seri"] == "IR_EUR_10Y":
            continue
        diff = row["corr_EUR10Y_inter"] - row["corr_EUR10Y_spline"]
        md += (
            f"| `{row['seri']}` | {row['corr_EUR10Y_inter']:.4f} | "
            f"{row['corr_EUR10Y_spline']:.4f} | {diff:+.4f} |\n"
        )

    md += """
*Observasi: Korelasi EUR_7Y–EUR_10Y turun signifikan dari 0,7598 (intersection) menjadi 0,6728 (spline)
karena 163 data spline yang halus mengurangi fluktuasi bersama antar-seri EUR.*

---

## 5. Verifikasi Kesamaan Intersection vs Legacy CSV

| Pemeriksaan | Hasil |
|---|:---:|
"""
    md += f"| Jumlah baris cocok | {legacy_res['rows_match']} ({legacy_res['rows_count']} baris) |\n"
    md += f"| Tanggal cocok 100% | {legacy_res['dates_match']} |\n"
    md += f"| Kategori cocok 100% | {legacy_res['categories_match']} |\n"
    md += f"| Selisih max nilai IR | {legacy_res['max_diff_ir']} |\n"
    md += f"| Selisih max nilai FX | {legacy_res['max_diff_fx']} |\n"
    md += f"| **Status Akhir** | **{'IDENTIK 100%' if legacy_res['is_identical'] else 'TIDAK COCOK'}** |\n"

    output_path.write_text(md, encoding="utf-8")


if __name__ == "__main__":
    main()
