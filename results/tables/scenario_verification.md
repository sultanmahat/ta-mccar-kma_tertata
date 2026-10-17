# Laporan Verifikasi Pembangkitan Skenario GBM & Biaya Portofolio (Tahap 04)

- **Waktu Pembuatan**: 2026-10-17 19:12:32 UTC
- **Horizon**: $T = 1$ tahun (252 hari kerja), mode `terminal_1step`
- **Bank Latih**: $N = 5.000$ skenario (`train_seed = 42`)
- **Bank Validasi**: $N = 20.000$ skenario (`validation_seed = 2026`)

## 1. Verifikasi Log-Return Simultan vs Parameter Target

Log-return tahunan teoritis: $R_j = \ln(S_{T,j}/S_{0,j}) \sim \mathcal{N}(\text{drift}_j, \sigma_j^2)$ dengan $\text{drift}_j = \mu_j - \frac{1}{2}\sigma_j^2 = 252 \cdot m_j$.

| Variabel | Target Drift (%) | Train Mean (%) | Selisih / SE | Target σ (%) | Train Std (%) | Valid Mean (%) | Valid Std (%) |
|---|---|---|---|---|---|---|---|
| `IR_USD_5Y` | +4.34% | +4.73% | 1.23 SE | 22.04% | 22.51% | +4.33% | 22.12% |
| `IR_USD_10Y` | +3.17% | +3.33% | 0.50 SE | 23.37% | 23.74% | +3.33% | 23.46% |
| `IR_USD_30Y` | +0.89% | +1.04% | 0.62 SE | 17.84% | 18.09% | +0.87% | 17.89% |
| `IR_EUR_7Y` | +3.69% | +4.22% | 1.29 SE | 29.12% | 29.88% | +3.76% | 29.20% |
| `IR_EUR_10Y` | +0.50% | +0.97% | 1.57 SE | 20.95% | 21.40% | +0.54% | 20.96% |
| `IR_JPY_5Y` | +12.76% | +12.46% | 0.63 SE | 34.36% | 34.36% | +13.07% | 34.11% |
| `IR_JPY_10Y` | +18.47% | +18.19% | 0.48 SE | 41.27% | 41.07% | +18.28% | 41.56% |
| `FX_USD/EUR` | -0.56% | -0.44% | 1.17 SE | 7.31% | 7.18% | -0.50% | 7.31% |
| `FX_USD/JPY` | +3.44% | +3.45% | 0.11 SE | 8.91% | 8.90% | +3.58% | 8.88% |

> [!NOTE]
> Selisih korelasi maksimum terhadap target $C$:
> - Bank Latih ($N=5.000$): **0.0304** (< 0.05)
> - Bank Validasi ($N=20.000$): **0.0239** (< 0.025)

## 2. Ringkasan Biaya Instrumen Portofolio per Skenario

### 2.1 Biaya Bruto (Persamaan 2.2 — Definisi UTAMA)

| Instrumen | Valuta | Tenor | Train Mean | Train Std Dev | Valid Mean | Valid Std Dev |
|---|---|---|---|---|---|---|
| `USD_Fixed_5Y` | USD | 5 thn | 1.045498 | 0.010382 | 1.045274 | 0.010103 |
| `USD_Fixed_10Y` | USD | 10 thn | 1.052349 | 0.012688 | 1.052306 | 0.012419 |
| `USD_Fixed_30Y` | USD | 30 thn | 1.054932 | 0.010025 | 1.054816 | 0.009871 |
| `EUR_Fixed_7Y` | EUR | 8 thn | 1.045086 | 0.075001 | 1.045564 | 0.076272 |
| `EUR_Fixed_10Y` | EUR | 10 thn | 1.048459 | 0.075281 | 1.048972 | 0.076590 |
| `JPY_Fixed_5Y` | JPY | 5 thn | 0.993109 | 0.089064 | 0.991857 | 0.088417 |
| `JPY_Fixed_10Y` | JPY | 10 thn | 1.004210 | 0.090823 | 1.002923 | 0.090468 |

### 2.2 Biaya Bunga (Persamaan 2.3 — Definisi SENSITIVITAS)

| Instrumen | Valuta | Tenor | Train Mean | Train Std Dev | Valid Mean | Valid Std Dev |
|---|---|---|---|---|---|---|
| `USD_Fixed_5Y` | USD | 5 thn | 0.045498 | 0.010382 | 0.045274 | 0.010103 |
| `USD_Fixed_10Y` | USD | 10 thn | 0.052349 | 0.012688 | 0.052306 | 0.012419 |
| `USD_Fixed_30Y` | USD | 30 thn | 0.054932 | 0.010025 | 0.054816 | 0.009871 |
| `EUR_Fixed_7Y` | EUR | 8 thn | 0.038098 | 0.011671 | 0.037875 | 0.011416 |
| `EUR_Fixed_10Y` | EUR | 10 thn | 0.041472 | 0.009233 | 0.041283 | 0.009076 |
| `JPY_Fixed_5Y` | JPY | 5 thn | 0.023192 | 0.008551 | 0.023251 | 0.008342 |
| `JPY_Fixed_10Y` | JPY | 10 thn | 0.034294 | 0.015314 | 0.034317 | 0.015221 |

## 3. Checklist Verifikasi Integritas & Matematis

- [x] **Rata-rata log-return**: Seluruh variabel berada dalam toleransi statistical confidence interval ($< 3 \times \text{SE}$).
- [x] **Simpangan baku log-return**: Mendekati $\sigma$ tahunan target pada kedua bank.
- [x] **Korelasi empiris**: Matriks korelasi sampel mendekati target korelasi 9×9 Cholesky.
- [x] **Kepositifan nilai**: Semua yield, kurs, faktor $q$, dan biaya $> 0$ (sifat log-normal terpenuhi).
- [x] **Integritas data**: 0 NaN dan 0 Inf di kedua bank skenario.
- [x] **Reproduksibilitas seed**: Generator acak berbasis seed menghasilkan array identik bit-by-bit saat seed diulang.
- [x] **Arah konversi $q$**: Terkonfirmasi bahwa pelemahan valuta asing (kurs $X_{USD/c}$ naik) menurunkan $q$ dan menurunkan beban biaya ekuivalen USD.
