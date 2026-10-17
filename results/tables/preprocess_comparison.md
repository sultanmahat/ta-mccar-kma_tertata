# Laporan Komparasi Pra-Pemrosesan Data — Tahap 02

**Sumber**: `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` (Read-Only)  
**Jendela Analisis**: 2017-07-03 s.d. 2025-11-24  
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
| **Korelasi EUR_7Y–EUR_10Y** | **0.7598** (lebih tinggi) | 0.6728 (lebih rendah) |
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
| **Jumlah baris** | 2028 | 2191 |
| **NaN pada 9 seri** | 0 | 0 |
| **Kolom** | Tanggal, Kategori, 7 IR, 2 FX | Tanggal, Kategori, 7 IR, 2 FX |
| **IR_EUR_10Y positif** | Ya | Ya (min terinterpolasi = 0.8560%) |
| **Kesesuaian legacy** | IDENTIK 100% | N/A (berbeda di 163 baris gap) |

---

## 3. Statistik Log-Return per Variabel Pasar

| Variabel | Mean (Intersection) | Std (Intersection) | N (Intersection) | Mean (Spline) | Std (Spline) | N (Spline) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `IR_USD_5Y` | 1.7237e-04 | 1.3883e-02 | 2026 | 1.3197e-04 | 1.4137e-02 | 2190 |
| `IR_USD_10Y` | 1.2563e-04 | 1.4722e-02 | 2026 | 1.2859e-04 | 1.5152e-02 | 2190 |
| `IR_USD_30Y` | 3.5137e-05 | 1.1239e-02 | 2026 | 5.3761e-05 | 1.1229e-02 | 2190 |
| `IR_EUR_7Y` | 1.4654e-04 | 1.8345e-02 | 2026 | 3.2046e-04 | 1.9943e-02 | 2190 |
| `IR_EUR_10Y` | 2.0028e-05 | 1.3195e-02 | 2026 | 1.7156e-04 | 1.2739e-02 | 2190 |
| `IR_JPY_5Y` | 5.0638e-04 | 2.1644e-02 | 2026 | 3.7833e-04 | 2.1029e-02 | 2190 |
| `IR_JPY_10Y` | 7.3278e-04 | 2.5995e-02 | 2026 | 5.3614e-04 | 2.6054e-02 | 2190 |
| `FX_USD/EUR` | -2.2222e-05 | 4.6043e-03 | 2026 | -6.4800e-06 | 4.5309e-03 | 2190 |
| `FX_USD/JPY` | 1.3640e-04 | 5.6120e-03 | 2026 | 1.4739e-04 | 5.4695e-03 | 2190 |

*Catatan: Log-return intersection tidak mencakup 1 baris transisi 29 Jan 2021 → 16 Sep 2021 (lompatan 230 hari kalender).*

---

## 4. Korelasi Log-Return IR_EUR_10Y terhadap 8 Variabel Pasar Lainnya

| Variabel | Korelasi (Intersection) | Korelasi (Spline) | Selisih |
|---|:---:|:---:|:---:|
| `IR_USD_5Y` | 0.5632 | 0.5262 | +0.0371 |
| `IR_USD_10Y` | 0.5583 | 0.5189 | +0.0395 |
| `IR_USD_30Y` | 0.4712 | 0.4509 | +0.0202 |
| `IR_EUR_7Y` | 0.7598 | 0.6728 | +0.0869 |
| `IR_JPY_5Y` | 0.1074 | 0.1067 | +0.0008 |
| `IR_JPY_10Y` | 0.0426 | 0.0401 | +0.0025 |
| `FX_USD/EUR` | 0.0678 | 0.0668 | +0.0010 |
| `FX_USD/JPY` | 0.0927 | 0.0902 | +0.0024 |

*Observasi: Korelasi EUR_7Y–EUR_10Y turun signifikan dari 0,7598 (intersection) menjadi 0,6728 (spline)
karena 163 data spline yang halus mengurangi fluktuasi bersama antar-seri EUR.*

---

## 5. Verifikasi Kesamaan Intersection vs Legacy CSV

| Pemeriksaan | Hasil |
|---|:---:|
| Jumlah baris cocok | True (2028 baris) |
| Tanggal cocok 100% | True |
| Kategori cocok 100% | True |
| Selisih max nilai IR | 0.0 |
| Selisih max nilai FX | 0.0 |
| **Status Akhir** | **IDENTIK 100%** |
