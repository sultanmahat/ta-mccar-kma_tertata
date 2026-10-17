# Laporan Audit Data Mentah DJPPR — Tahap 01

**Sumber File**: `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` (Read-Only)  
**Dokumen Acuan**: `docs/context/spesifikasi_model.md` §2  

---

## 1. Konfirmasi Ringkasan Spesifikasi §2 vs Data Riil

| Butir Spesifikasi §2 | Klaim Spesifikasi | Hasil Audit Riil | Status |
|---|---|---|:---:|
| **Sheet Tersedia** | `Data IR`, `Data FX`, `Data Awal`, `Data IR_formula` | 4 sheet persis | **SESUAI** |
| **Total Observasi** | 3.104 baris hari kerja | 3.104 baris (0 duplikat, 0 akhir pekan) | **SESUAI** |
| **Rentang Tanggal Total** | 1 Jan 2014 – 24 Nov 2025 | 2014-01-01 s.d. 2025-11-24 | **SESUAI** |
| **Awal Ketersediaan JPY_5Y** | 3 Jul 2017 | 2017-07-03 | **SESUAI** |
| **Jendela Analisis 9 Seri** | 3 Jul 2017 – 24 Nov 2025 (2.191 baris) | 2.191 baris | **SESUAI** |
| **Data Hilang di Jendela** | `IR_EUR_10Y` 163 hari (1 Feb – 15 Sep 2021) | 163 baris (2021-02-01 s.d. 2021-09-15) | **SESUAI** |
| **Irisan Lengkap (Intersection)** | 2.028 baris lengkap | 2.028 baris (2.191 − 163) | **SESUAI** |
| **Nilai Non-Positif (<= 0)** | Tidak ada (semua > 0, min JPY_5Y = 0,521%) | 0 nilai <= 0 (min JPY_5Y = 0.521%) | **SESUAI** |
| **Duplikat Sheet Data IR** | `Data IR_formula` duplikat `Data IR` | Identik 100% pada 9 kolom utama | **SESUAI** (ada catatan) |
| **Sheet Data Awal** | $\Sigma w_0 = 1$, $\Sigma lb = 0,88$, $\Sigma ub = 1,105$, $lb \le w_0 \le ub$ | $\Sigma w_0 = 1.0000$, $\Sigma lb = 0.880$, $\Sigma ub = 1.105$ | **SESUAI** |
| **Arah Kurs Valas** | Unit mata uang per 1 USD (EUR/USD & JPY/USD) | FX_USD/EUR ~ 0,8–0,9; FX_USD/JPY ~ 102–160 | **SESUAI** |
| **Validasi Acuan Legacy CSV** | Identik dengan ir_data_clean.csv & fx_data_clean.csv | 2.028 baris identik 100% (selisih = 0.0) | **SESUAI** |

*(Catatan: Ditemukan 1 kolom ekstra `Unnamed: 9` pada `Data IR` berisi nilai tunggal 2014.0 di baris pertama, sedangkan `Data IR_formula` bersih dari kolom ini.)*

---

## 2. Struktur Sheet & Tipe Data

| Sheet | Dimensi | Kolom Tanggal | Kolom Data | Tipe Data |
|---|---|---|---|---|
| `Data IR` | 3104 × 10 | `Tanggal` (datetime64) | 7 yield, 1 kategori, 1 unindexed | float64, string |
| `Data FX` | 3104 × 3 | `Tanggal` (datetime64) | `FX_USD/EUR`, `FX_USD/JPY` | float64 |
| `Data Awal` | 7 × 6 | — | `Instrument`, `Curr`, `Tenor (yr)`, `Existing (2024)`, `Min`, `Max` | object, int64, float64 |
| `Data IR_formula` | 3.104 × 9 | `Tanggal` (datetime64) | 7 yield, 1 kategori | float64, string |

---

## 3. Ringkasan Blok Data Hilang (Tersimpan di `audit_data_gaps.csv`)

| Sheet | Kolom | Tanggal Mulai | Tanggal Selesai | Jumlah Baris Hilang | Catatan |
|---|---|---|---|:---:|---|
| `Data IR` | `IR_EUR_7Y` | 2014-01-01 | 2014-07-03 | 132 | Sebelum jendela analisis |
| `Data IR` | `IR_EUR_10Y` | 2014-01-01 | 2015-07-23 | 407 | Sebelum jendela analisis |
| `Data IR` | `IR_EUR_10Y` | 2021-02-01 | 2021-09-15 | 163 | **Satu-satunya gap dalam jendela analisis** |
| `Data IR` | `IR_JPY_5Y` | 2014-01-01 | 2017-06-30 | 913 | Sebelum jendela analisis |
| `Data IR` | `IR_JPY_10Y` | 2014-01-01 | 2016-05-10 | 615 | Sebelum jendela analisis |

---

## 4. Validasi Nilai Minimum & Kelayakan Model (GBM & Log-Return)

Seluruh 9 variabel pasar pada jendela analisis memiliki nilai strictly positive (> 0), sehingga transformasi log-return $r_t = \ln(S_t / S_{t-1})$ dan asumsi Geometric Brownian Motion (GBM) terjamin valid secara matematis tanpa singularitas:

| Variabel Pasar | Satuan / Konvensi | Nilai Minimum di Jendela | Jumlah $\le 0$ | Status Validitas |
|---|---|:---:|:---:|:---:|
| `IR_USD_5Y` | % per tahun | 1.200% | 0 | Valid |
| `IR_USD_10Y` | % per tahun | 1.849% | 0 | Valid |
| `IR_USD_30Y` | % per tahun | 2.995% | 0 | Valid |
| `IR_EUR_7Y` | % per tahun | 0.539% | 0 | Valid |
| `IR_EUR_10Y` | % per tahun | 0.856% | 0 | Valid |
| `IR_JPY_5Y` | % per tahun | 0.521% | 0 | Valid |
| `IR_JPY_10Y` | % per tahun | 0.597% | 0 | Valid |
| `FX_USD/EUR` | EUR per 1 USD | 0.7997 | 0 | Valid |
| `FX_USD/JPY` | JPY per 1 USD | 102.40 | 0 | Valid |

---

## 5. Parameter Portofolio Eksisting & Batas Proporsi (Tabel 2.1 & 2.2)

Hasil verifikasi sheet `Data Awal`:
- Jumlah bobot eksisting: $\sum w_{0,i} = 1.0000000000$ (tepat 1).
- Jumlah batas bawah: $\sum lb_i = 0.880$.
- Jumlah batas atas: $\sum ub_i = 1.105$.
- Relasi kelayakan: $\sum lb_i = 0,88 \le 1 \le \sum ub_i = 1,105$ (ruang layak DJPPR dipastikan tidak kosong).
- Bobot eksisting berada sepenuhnya di dalam batas: $lb_i \le w_{0,i} \le ub_i$ untuk seluruh $i=1,\dots,7$.

---

## 6. Sebaran Kolom Kategori Pandemi

| Kategori | Baris di Jendela (2.191 baris) | Baris di Irisan Lengkap (2.028 baris) | Rentang Tanggal |
|---|:---:|:---:|---|
| **Sebelum Covid** | 914 (41.7%) | 914 (45.1%) | 2017-07-03 s.d. 2020-12-31 |
| **Covid** | 521 (23.8%) | 358 (17.7%) | 2021-01-01 s.d. 2022-12-30 |
| **Setelah Covid** | 756 (34.5%) | 756 (37.3%) | 2023-01-02 s.d. 2025-11-24 |

*Catatan: Seluruh 163 baris data hilang `IR_EUR_10Y` jatuh pada periode Covid (1 Feb – 15 Sep 2021), sehingga kategori Covid berkurang dari 521 menjadi 358 baris pada varian irisan lengkap.*

---

## 7. Lonjakan Harian Ekstrem ($|\Delta \ln S_t| > 5\sigma$)

Ditemukan sebanyak **87 kejadian** pergerakan ekstrem harian pada jendela analisis. Sesuai prinsip kerja, seluruh data riil ini **dipertahankan (tidak dihapus)** karena mencerminkan volatilitas pasar sesungguhnya (terutama guncangan likuiditas global Maret 2020 dan intervensi valuta asing BoJ 2022).

Sepuluh kejadian dengan deviasi paling signifikan:

| Tanggal | Variabel | Nilai Sebelumnya | Nilai Hari Tersebut | Log-Change ($\Delta \ln$) | $z$-score ($|\Delta \ln| / \sigma$) |
|---|---|:---:|:---:|:---:|:---:|
| 2019-01-01 | `IR_JPY_10Y` | 0.602 | 1.169 | +0.6636 | +25.47σ |
| 2021-09-16 | `IR_EUR_10Y` | 0.967 | 1.352 | +0.3351 | +22.13σ |
| 2020-04-21 | `IR_JPY_10Y` | 0.956 | 1.7 | +0.5756 | +22.09σ |
| 2021-08-02 | `IR_EUR_7Y` | 0.678 | 0.97 | +0.3581 | +17.96σ |
| 2019-11-01 | `IR_EUR_10Y` | 1.113 | 1.422 | +0.2450 | +16.18σ |
| 2020-03-12 | `IR_EUR_7Y` | 0.983 | 1.346 | +0.3143 | +15.76σ |
| 2020-03-13 | `IR_USD_5Y` | 2.628 | 3.187 | +0.1929 | +13.64σ |
| 2025-07-01 | `IR_JPY_5Y` | 1.414 | 1.807 | +0.2452 | +11.66σ |
| 2020-03-12 | `IR_EUR_10Y` | 1.348 | 1.604 | +0.1739 | +11.48σ |
| 2020-03-13 | `IR_EUR_10Y` | 1.604 | 1.907 | +0.1730 | +11.42σ |

---

## 8. Verifikasi Kesamaan dengan File Acuan Legacy

Perbandingan irisan lengkap 9 seri dari Excel asli dengan file `legacy/data_v0/ir_data_clean.csv` dan `legacy/data_v0/fx_data_clean.csv`:
- Kesamaan jumlah baris: **True** (2028 baris).
- Kesamaan tanggal (urutan persis): **True**.
- Kesamaan kolom Kategori: **True**.
- Selisih maksimum nilai Yield (IR): **0.0**.
- Selisih maksimum nilai Kurs (FX): **0.0**.
- Status kesesuaian: **IDENTIK 100% (Bit-by-Bit Numerical Match)**.
