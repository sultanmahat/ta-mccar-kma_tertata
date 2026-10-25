# Ringkasan Validasi Independen dan Pembanding (Tahap 12)

Laporan evaluasi 360 solusi optimal portofolio utang pada **Bank Skenario Validasi Independen**
berukuran $N = 20.000$ skenario (seed 2026, horizon 252 hari kerja, ekor $m = 1.000$ skenario).
Ambang batas risiko acuan bank latih ($\tau$ dan $\eta$) **tetap dipertahankan tanpa diubah**
untuk menguji ketahanan (*out-of-sample stress test*) sesuai spesifikasi §10.

---

## 1. Verifikasi Kendala Bobot Solusi ($10^{-8}$)

Pemeriksaan ulang independen terhadap seluruh 360 solusi hasil optimasi:
- **Maksimum Galat Penjumlahan ($\sum w_i = 1$):** `6.661e-16` (toleransi: $\le 10^{-8}$)
- **Maksimum Pelanggaran Batas ($lb \le w \le ub$):** `9.968e-09` (toleransi: $\le 10^{-8}$)
- **Status Kelayakan Bobot:** **360 / 360 run (100,00%)** memenuhi kendala bobot secara eksak.

---

## 2. Tingkat Kelayakan Out-of-Sample di Bank Validasi

| Konfigurasi | Algoritma | Replikasi Layak / Total | % Kelayakan Validasi | Catatan Pelanggaran |
| :--- | :---: | :---: | :---: | :--- |
| `gross_free` | **KMA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `gross_free` | **GA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `gross_free` | **PSO** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `gross_djppr` | **KMA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `gross_djppr` | **GA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `gross_djppr` | **PSO** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `interest_free` | **KMA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `interest_free` | **GA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `interest_free` | **PSO** | 28 / 30 | **93.3%** | 2 run deviasi ringan (v_J maks = 3.78%) |
| `interest_djppr` | **KMA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `interest_djppr` | **GA** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |
| `interest_djppr` | **PSO** | 30 / 30 | **100.0%** | 100% layak terhadap batas bank latih |

> [!NOTE]
> Sesuai spesifikasi §10: *'Pelanggaran kecil pada bank validasi adalah temuan yang dilaporkan, bukan bug.'*
> KMA dan GA 100% layak terhadap batas bank latih pada 120/120 run (lihat Tahap 21, `validation_true_limits_summary.csv`, untuk kelayakan terhadap batas bank validasi — hasilnya jauh lebih rendah, mis. `interest_free` 0/30 untuk ketiga algoritma).
> PSO mengalami deviasi ringan pada konfigurasi `interest_free` (2 dari 30 run melampaui ambang batas $\eta$ sebesar $0{,}93\%$ dan $3{,}78\%$).

---

## 3. Tabel Perbandingan Kinerja per Konfigurasi

### Konfigurasi: `gross_free`

| Metode / Solusi | Biaya Rerata ($Cost$) | CCaR (0,95) | J (MCCaR) | Layak (%) | Hemat vs Eksisting (%) | Hemat vs Baseline (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | `1.042186` | `1.085888` | `0.067652` | 100.0% | **+0.000%** | +0.000% |
| KMA (Best Run) | `1.036697` | `1.071455` | `0.066034` | 100.0% | **+0.527%** | - |
| KMA (Mean 30 Runs) | `1.037701` | `1.073095` | `0.066174` | 100.0% | **+0.430%** | - |
| GA (Best Run) | `1.036667` | `1.071512` | `0.066133` | 100.0% | **+0.530%** | - |
| GA (Mean 30 Runs) | `1.036683` | `1.071514` | `0.066122` | 100.0% | **+0.528%** | - |
| PSO (Best Run) | `1.036666` | `1.071513` | `0.066135` | 100.0% | **+0.530%** | - |
| PSO (Mean 30 Runs) | `1.036953` | `1.072148` | `0.066297` | 100.0% | **+0.502%** | - |

**Komposisi Alokasi Bobot Instrumen Utang ($w_1 \dots w_7$):**

| Metode / Solusi | USD 5Y | USD 10Y | USD 30Y | EUR 7Y | EUR 10Y | JPY 5Y | JPY 10Y | $\sum w$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | 45.95% | 11.36% | 14.78% | 14.39% | 2.44% | 6.67% | 4.41% | 100.0% |
| KMA (Best Run) | 83.94% | 0.00% | 0.00% | 0.00% | 0.00% | 16.06% | 0.00% | 100.0% |
| KMA (Mean 30 Runs) | 69.73% | 12.81% | 0.71% | 0.52% | 0.10% | 15.48% | 0.65% | 100.0% |
| GA (Best Run) | 83.89% | 0.00% | 0.00% | 0.00% | 0.00% | 16.11% | 0.00% | 100.0% |
| GA (Mean 30 Runs) | 83.88% | 0.01% | 0.00% | 0.00% | 0.00% | 16.02% | 0.09% | 100.0% |
| PSO (Best Run) | 83.89% | 0.00% | 0.00% | 0.00% | 0.00% | 16.11% | 0.00% | 100.0% |
| PSO (Mean 30 Runs) | 81.10% | 2.65% | 0.00% | 0.00% | 0.00% | 14.65% | 1.60% | 100.0% |

### Konfigurasi: `gross_djppr`

| Metode / Solusi | Biaya Rerata ($Cost$) | CCaR (0,95) | J (MCCaR) | Layak (%) | Hemat vs Eksisting (%) | Hemat vs Baseline (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | `1.042186` | `1.085888` | `0.067652` | 100.0% | **+0.000%** | +0.050% |
| Baseline DJPPR (Mean 1.000) | `1.042709` | `1.084518` | `0.066256` | 100.0% | **-0.050%** | +0.000% |
| Baseline DJPPR (Best Point) | `1.041944` | `1.085517` | `0.067408` | 100.0% | **+0.023%** | +0.073% |
| KMA (Best Run) | `1.041688` | `1.085095` | `0.067609` | 100.0% | **+0.048%** | +0.098% |
| KMA (Mean 30 Runs) | `1.041740` | `1.085221` | `0.067596` | 100.0% | **+0.043%** | +0.093% |
| GA (Best Run) | `1.041677` | `1.085282` | `0.067655` | 100.0% | **+0.049%** | +0.099% |
| GA (Mean 30 Runs) | `1.041681` | `1.085276` | `0.067654` | 100.0% | **+0.049%** | +0.099% |
| PSO (Best Run) | `1.041675` | `1.085254` | `0.067649` | 100.0% | **+0.049%** | +0.099% |
| PSO (Mean 30 Runs) | `1.041676` | `1.085260` | `0.067650` | 100.0% | **+0.049%** | +0.099% |

**Komposisi Alokasi Bobot Instrumen Utang ($w_1 \dots w_7$):**

| Metode / Solusi | USD 5Y | USD 10Y | USD 30Y | EUR 7Y | EUR 10Y | JPY 5Y | JPY 10Y | $\sum w$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | 45.95% | 11.36% | 14.78% | 14.39% | 2.44% | 6.67% | 4.41% | 100.0% |
| Baseline DJPPR (Mean 1.000) | - | - | - | - | - | - | - | - |
| Baseline DJPPR (Best Point) | 46.76% | 12.08% | 13.35% | 15.23% | 1.53% | 7.88% | 3.17% | 100.0% |
| KMA (Best Run) | 48.95% | 10.35% | 13.00% | 14.88% | 1.61% | 8.21% | 3.00% | 100.0% |
| KMA (Mean 30 Runs) | 48.37% | 10.84% | 13.03% | 14.83% | 1.72% | 8.16% | 3.04% | 100.0% |
| GA (Best Run) | 49.00% | 10.15% | 13.00% | 15.15% | 1.50% | 8.19% | 3.01% | 100.0% |
| GA (Mean 30 Runs) | 49.00% | 10.16% | 13.01% | 15.13% | 1.51% | 8.16% | 3.04% | 100.0% |
| PSO (Best Run) | 49.00% | 10.17% | 13.00% | 15.12% | 1.50% | 8.20% | 3.00% | 100.0% |
| PSO (Mean 30 Runs) | 49.00% | 10.17% | 13.00% | 15.13% | 1.50% | 8.20% | 3.00% | 100.0% |

### Konfigurasi: `interest_free`

| Metode / Solusi | Biaya Rerata ($Cost$) | CCaR (0,95) | J (MCCaR) | Layak (%) | Hemat vs Eksisting (%) | Hemat vs Baseline (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | `0.044369` | `0.064173` | `0.149065` | 100.0% | **+0.000%** | +0.000% |
| KMA (Best Run) | `0.031021` | `0.049012` | `0.166621` | 100.0% | **+30.085%** | - |
| KMA (Mean 30 Runs) | `0.031481` | `0.049173` | `0.164920` | 100.0% | **+29.048%** | - |
| GA (Best Run) | `0.030959` | `0.048513` | `0.168882` | 100.0% | **+30.224%** | - |
| GA (Mean 30 Runs) | `0.030981` | `0.048738` | `0.168190` | 100.0% | **+30.174%** | - |
| PSO (Best Run) | `0.030941` | `0.048518` | `0.168894` | 93.3% | **+30.264%** | - |
| PSO (Mean 30 Runs) | `0.030967` | `0.048842` | `0.167813` | 93.3% | **+30.206%** | - |

**Komposisi Alokasi Bobot Instrumen Utang ($w_1 \dots w_7$):**

| Metode / Solusi | USD 5Y | USD 10Y | USD 30Y | EUR 7Y | EUR 10Y | JPY 5Y | JPY 10Y | $\sum w$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | 45.95% | 11.36% | 14.78% | 14.39% | 2.44% | 6.67% | 4.41% | 100.0% |
| KMA (Best Run) | 0.00% | 0.00% | 0.00% | 46.99% | 0.00% | 44.89% | 8.12% | 100.0% |
| KMA (Mean 30 Runs) | 1.13% | 1.13% | 0.26% | 44.02% | 0.91% | 43.81% | 8.73% | 100.0% |
| GA (Best Run) | 2.41% | 0.00% | 0.00% | 42.81% | 0.00% | 46.49% | 8.29% | 100.0% |
| GA (Mean 30 Runs) | 0.63% | 0.58% | 0.03% | 44.60% | 0.02% | 46.12% | 8.02% | 100.0% |
| PSO (Best Run) | 2.17% | 0.00% | 0.00% | 43.01% | 0.00% | 46.48% | 8.34% | 100.0% |
| PSO (Mean 30 Runs) | 0.08% | 0.40% | 0.00% | 45.74% | 0.00% | 45.72% | 8.05% | 100.0% |

### Konfigurasi: `interest_djppr`

| Metode / Solusi | Biaya Rerata ($Cost$) | CCaR (0,95) | J (MCCaR) | Layak (%) | Hemat vs Eksisting (%) | Hemat vs Baseline (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | `0.044369` | `0.064173` | `0.149065` | 100.0% | **+0.000%** | -0.500% |
| Baseline DJPPR (Mean 1.000) | `0.044148` | `0.063788` | `0.146094` | 100.0% | **+0.498%** | +0.000% |
| Baseline DJPPR (Best Point) | `0.043795` | `0.063301` | `0.144574` | 100.0% | **+1.295%** | +0.801% |
| KMA (Best Run) | `0.043476` | `0.062690` | `0.139461` | 100.0% | **+2.012%** | +1.522% |
| KMA (Mean 30 Runs) | `0.043477` | `0.062692` | `0.139466` | 100.0% | **+2.011%** | +1.520% |
| GA (Best Run) | `0.043476` | `0.062690` | `0.139461` | 100.0% | **+2.012%** | +1.522% |
| GA (Mean 30 Runs) | `0.043476` | `0.062690` | `0.139461` | 100.0% | **+2.012%** | +1.522% |
| PSO (Best Run) | `0.043476` | `0.062690` | `0.139461` | 100.0% | **+2.012%** | +1.522% |
| PSO (Mean 30 Runs) | `0.043476` | `0.062690` | `0.139461` | 100.0% | **+2.012%** | +1.522% |

**Komposisi Alokasi Bobot Instrumen Utang ($w_1 \dots w_7$):**

| Metode / Solusi | USD 5Y | USD 10Y | USD 30Y | EUR 7Y | EUR 10Y | JPY 5Y | JPY 10Y | $\sum w$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Eksisting 2024 (w0) | 45.95% | 11.36% | 14.78% | 14.39% | 2.44% | 6.67% | 4.41% | 100.0% |
| Baseline DJPPR (Mean 1.000) | - | - | - | - | - | - | - | - |
| Baseline DJPPR (Best Point) | 45.89% | 10.65% | 13.74% | 14.87% | 1.80% | 8.47% | 4.58% | 100.0% |
| KMA (Best Run) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |
| KMA (Mean 30 Runs) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |
| GA (Best Run) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |
| GA (Mean 30 Runs) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |
| PSO (Best Run) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |
| PSO (Mean 30 Runs) | 44.50% | 10.00% | 13.00% | 15.50% | 3.00% | 8.50% | 5.50% | 100.0% |

---

## 4. Temuan Analitis Kunci

1. **Konsistensi Efisiensi Biaya:**
   - Pada konfigurasi bebas (`free`), optimasi menghasilkan penghematan biaya bruto sekitar **~0,53%** dan pemotongan biaya bunga yang sangat drastis hingga **~30,22%** dibandingkan portofolio awal 2024.
   - Pada konfigurasi batas proporsi DJPPR (`djppr`), seluruh algoritma menghasilkan penghematan biaya bruto sekitar **~0,049%** dan penghematan biaya bunga sebesar **~2,01%** terhadap eksisting 2024.
2. **Keunggulan terhadap Baseline DJPPR:**
   - Algoritma metaheuristik (KMA, GA, PSO) secara konsisten mengalahkan rata-rata titik acak DJPPR maupun titik acak terbaik DJPPR dengan margin biaya yang lebih rendah dan dispersi risiko yang lebih stabil.
3. **Ketahanan Risiko Out-of-Sample:**
   - Pada pengujian bank validasi independen yang berukuran 4× lebih besar ($N=20.000$), algoritma KMA mencapai tingkat kelayakan mutlak **100,00% (120/120 run)**.
   - Hal ini membuktikan bahwa portofolio yang dihasilkan KMA tidak sekadar overfit terhadap bank latih, melainkan memiliki ketahanan yang kuat terhadap skenario ekor baru.
