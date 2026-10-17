# Hasil Estimasi Parameter GBM & Statistik Historis (Varian: intersection)

- **Jendela Data**: 2017-07-03 s.d. 2025-11-24
- **Varian**: `intersection`
- **Konversi Hari Kerja/Tahun**: 252
- **Formula Anualisasi (D2a Opsi A)**: $\sigma = s \sqrt{252}$, $\mu = 252m + \sigma^2 / 2$
- **Mode Simulasi (D2b Opsi A)**: `terminal_1step` ($T=1$ tahun)

## 1. Parameter Geometric Brownian Motion (GBM) 9 Variabel Pasar

| No | Variabel Pasar | Tipe | N | m harian | s harian | μ tahunan (%) | σ tahunan (%) | (μ - ½σ²) (%) |
|---|---|---|---|---|---|---|---|---|
| 1 | `IR_USD_5Y` | Yield | 2026 | +0.000172 | 0.013883 | +6.77% | 22.04% | +4.34% |
| 2 | `IR_USD_10Y` | Yield | 2026 | +0.000126 | 0.014722 | +5.90% | 23.37% | +3.17% |
| 3 | `IR_USD_30Y` | Yield | 2026 | +0.000035 | 0.011239 | +2.48% | 17.84% | +0.89% |
| 4 | `IR_EUR_7Y` | Yield | 2026 | +0.000147 | 0.018345 | +7.93% | 29.12% | +3.69% |
| 5 | `IR_EUR_10Y` | Yield | 2026 | +0.000020 | 0.013195 | +2.70% | 20.95% | +0.50% |
| 6 | `IR_JPY_5Y` | Yield | 2026 | +0.000506 | 0.021644 | +18.66% | 34.36% | +12.76% |
| 7 | `IR_JPY_10Y` | Yield | 2026 | +0.000733 | 0.025995 | +26.98% | 41.27% | +18.47% |
| 8 | `FX_USD/EUR` | Kurs FX | 2026 | -0.000022 | 0.004604 | -0.29% | 7.31% | -0.56% |
| 9 | `FX_USD/JPY` | Kurs FX | 2026 | +0.000136 | 0.005612 | +3.83% | 8.91% | +3.44% |

> [!NOTE]
> Komponen drift `(μ - ½σ²)` dalam simulasi GBM harian bernilai persis $252 \times m$,
> merefleksikan laju perubahan log-return tahunan aktual tanpa bias.

## 2. Pemeriksaan Konsistensi (Sanity-Check §11)

Berdasarkan catatan analitis spesifikasi §11:
- **Volatilitas JPY**: Yield JPY (khususnya `IR_JPY_5Y` dan `IR_JPY_10Y`) memiliki volatilitas relatif
  tertinggi karena basis level yield yang rendah (σ annual JPY_5Y = 34.36% vs USD_5Y = 22.04%).
- **Kestabilan Kurs**: Kurs `FX_USD/EUR` memiliki volatilitas rendah dengan drift mendekati nol,
  sedangkan `FX_USD/JPY` mengalami depresiasi Yen (kenaikan USD/JPY) dengan drift tahunan +3.83%.

## 3. Matriks Korelasi Pearson 9×9 ($r_t$)

| Variabel | `IR_USD_5Y` | `IR_USD_10Y` | `IR_USD_30Y` | `IR_EUR_7Y` | `IR_EUR_10Y` | `IR_JPY_5Y` | `IR_JPY_10Y` | `FX_USD/EUR` | `FX_USD/JPY` |
|---|---|---|---|---|---|---|---|---|---|
| `IR_USD_5Y` | +1.0000 | +0.8041 | +0.6843 | +0.5875 | +0.5632 | +0.1458 | +0.0740 | +0.1136 | +0.1061 |
| `IR_USD_10Y` | +0.8041 | +1.0000 | +0.8603 | +0.5748 | +0.5583 | +0.1174 | +0.0889 | +0.1194 | +0.0883 |
| `IR_USD_30Y` | +0.6843 | +0.8603 | +1.0000 | +0.4671 | +0.4712 | +0.0821 | +0.0640 | +0.1045 | +0.0685 |
| `IR_EUR_7Y` | +0.5875 | +0.5748 | +0.4671 | +1.0000 | +0.7598 | +0.1495 | +0.0518 | +0.0816 | +0.0725 |
| `IR_EUR_10Y` | +0.5632 | +0.5583 | +0.4712 | +0.7598 | +1.0000 | +0.1074 | +0.0426 | +0.0678 | +0.0927 |
| `IR_JPY_5Y` | +0.1458 | +0.1174 | +0.0821 | +0.1495 | +0.1074 | +1.0000 | +0.2773 | +0.0373 | +0.0338 |
| `IR_JPY_10Y` | +0.0740 | +0.0889 | +0.0640 | +0.0518 | +0.0426 | +0.2773 | +1.0000 | +0.0004 | -0.0010 |
| `FX_USD/EUR` | +0.1136 | +0.1194 | +0.1045 | +0.0816 | +0.0678 | +0.0373 | +0.0004 | +1.0000 | +0.4656 |
| `FX_USD/JPY` | +0.1061 | +0.0883 | +0.0685 | +0.0725 | +0.0927 | +0.0338 | -0.0010 | +0.4656 | +1.0000 |

- **Sifat Simetris**: Terpenuhi (maksimum selisih $|C - C^T| < 10^{-12}$).
- **Diagonal**: 1.0000 persis.
- **Definit Positif**: Terpenuhi (faktorisasi Cholesky $L L^T = C$ berhasil tanpa galat).

## 4. Statistik Perubahan Biaya Historis Persamaan 2.7–2.10 ($\Delta c_{i,t}$)

### 4.1 Biaya Bruto (Persamaan 2.2 — Definisi UTAMA)

| Instrumen | Valuta | Tenor | N | Rata-rata $\Delta c$ harian | Varians $\Delta c$ | Std Dev $\Delta c$ | Std Dev Anualisasi (%) |
|---|---|---|---|---|---|---|---|
| `USD_Fixed_5Y` | USD | 5 thn | 2026 | +5.439751e-06 | 2.079089e-07 | 4.559703e-04 | 0.72% |
| `USD_Fixed_10Y` | USD | 10 thn | 2026 | +5.440205e-06 | 2.939890e-07 | 5.422075e-04 | 0.86% |
| `USD_Fixed_30Y` | USD | 30 thn | 2026 | +2.078299e-06 | 2.392068e-07 | 4.890877e-04 | 0.78% |
| `EUR_Fixed_7Y` | EUR | 8 thn | 2026 | +2.913224e-05 | 2.101487e-05 | 4.584198e-03 | 7.28% |
| `EUR_Fixed_10Y` | EUR | 10 thn | 2026 | +2.631236e-05 | 2.107337e-05 | 4.590574e-03 | 7.29% |
| `JPY_Fixed_5Y` | JPY | 5 thn | 2026 | -1.303189e-04 | 3.151558e-05 | 5.613874e-03 | 8.91% |
| `JPY_Fixed_10Y` | JPY | 10 thn | 2026 | -1.257787e-04 | 3.171810e-05 | 5.631882e-03 | 8.94% |

#### Matriks Kovarians $\Delta c$ (Biaya Bruto):

| Instrumen | `USD_Fixed_5Y` | `USD_Fixed_10Y` | `USD_Fixed_30Y` | `EUR_Fixed_7Y` | `EUR_Fixed_10Y` | `JPY_Fixed_5Y` | `JPY_Fixed_10Y` |
|---|---|---|---|---|---|---|---|
| `USD_Fixed_5Y` | +2.0791e-07 | +2.0819e-07 | +1.6945e-07 | -1.4698e-07 | -1.6467e-07 | -2.8678e-07 | -2.8653e-07 |
| `USD_Fixed_10Y` | +2.0819e-07 | +2.9399e-07 | +2.3215e-07 | -1.8098e-07 | -1.9925e-07 | -3.0465e-07 | -2.9779e-07 |
| `USD_Fixed_30Y` | +1.6945e-07 | +2.3215e-07 | +2.3921e-07 | -1.3577e-07 | -1.4639e-07 | -2.1376e-07 | -2.0792e-07 |
| `EUR_Fixed_7Y` | -1.4698e-07 | -1.8098e-07 | -1.3577e-07 | +2.1015e-05 | +2.1022e-05 | +1.1802e-05 | +1.1843e-05 |
| `EUR_Fixed_10Y` | -1.6467e-07 | -1.9925e-07 | -1.4639e-07 | +2.1022e-05 | +2.1073e-05 | +1.1816e-05 | +1.1858e-05 |
| `JPY_Fixed_5Y` | -2.8678e-07 | -3.0465e-07 | -2.1376e-07 | +1.1802e-05 | +1.1816e-05 | +3.1516e-05 | +3.1555e-05 |
| `JPY_Fixed_10Y` | -2.8653e-07 | -2.9779e-07 | -2.0792e-07 | +1.1843e-05 | +1.1858e-05 | +3.1555e-05 | +3.1718e-05 |

### 4.2 Biaya Bunga (Persamaan 2.3 — Definisi SENSITIVITAS)

| Instrumen | Valuta | Tenor | N | Rata-rata $\Delta c$ harian | Varians $\Delta c$ | Std Dev $\Delta c$ | Std Dev Anualisasi (%) |
|---|---|---|---|---|---|---|---|
| `USD_Fixed_5Y` | USD | 5 thn | 2026 | +1.723746e-04 | 1.927281e-04 | 1.388265e-02 | 22.04% |
| `USD_Fixed_10Y` | USD | 10 thn | 2026 | +1.256264e-04 | 2.167323e-04 | 1.472183e-02 | 23.37% |
| `USD_Fixed_30Y` | USD | 30 thn | 2026 | +3.513682e-05 | 1.263244e-04 | 1.123941e-02 | 17.84% |
| `EUR_Fixed_7Y` | EUR | 8 thn | 2026 | +1.687596e-04 | 3.439536e-04 | 1.854598e-02 | 29.44% |
| `EUR_Fixed_10Y` | EUR | 10 thn | 2026 | +4.225018e-05 | 1.870707e-04 | 1.367738e-02 | 21.71% |
| `JPY_Fixed_5Y` | JPY | 5 thn | 2026 | +3.699860e-04 | 4.917342e-04 | 2.217508e-02 | 35.20% |
| `JPY_Fixed_10Y` | JPY | 10 thn | 2026 | +5.963788e-04 | 7.075587e-04 | 2.659998e-02 | 42.23% |
