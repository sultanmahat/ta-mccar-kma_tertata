# Ringkasan Analisis Statistik Komparatif Metaheuristik (Tahap 13)

Laporan pengujian hipotesis komparatif antara algoritma **KMA, GA, dan PSO**
berdasarkan 30 replikasi independen per konfigurasi ($N = 90$ run per konfigurasi, total 360 run).
Uji statistik mencakup uji asumsi parametrik (Shapiro-Wilk dan Levene),
uji non-parametrik Kruskal-Wallis (Pers. 2.37), ukuran efek Epsilon-squared (Pers. 2.39),
uji lanjut post-hoc Dunn dengan koreksi Holm (Pers. 2.38), dan korelasi Rank-Biserial.

---

## Konfigurasi: `gross_free`

### 1. Statistik Deskriptif & Konvergensi

| Algoritma | Terbaik ($min$) | Median | Rata-rata | Simpangan Baku ($std$) | IQR | Waktu Rerata (s) | $E_{\text{conv}}$ Rerata | Shapiro ($p$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **KMA** | `1.037086` | `1.038063` | `1.038062` | `5.32e-04` | `8.01e-04` | 73.0 s | 15192 eval | 0.5069 (Normal) |
| **GA** | `1.037056` | `1.037069` | `1.037072` | `1.64e-05` | `1.23e-05` | 34.3 s | 17933 eval | 5.8782e-06 |
| **PSO** | `1.037056` | `1.037056` | `1.037340` | `7.65e-04` | `1.00e-13` | 29.5 s | 3275 eval | 8.9447e-10 |

- **Uji Homogenitas Levene:** $W = 6.5458, p = 2.2480e-03$ (Heterogen (p < 0.05)).
- **Justifikasi Non-Parametrik:** Asumsi normalitas atau homogenitas ragam dilanggar (p < 0.05), sehingga uji non-parametrik Kruskal-Wallis secara statistik dijustifikasi.

### 2. Uji Kruskal-Wallis & Ukuran Efek $\epsilon^2$

- **Statistik Kruskal-Wallis ($H$):** `52.2760` ($df = 2$, $p = 4.4505e-12$)
- **Faktor Koreksi Ties ($C_{\text{ties}}$):** `0.999984` (Ada ties: True)
- **Cross-check SciPy:** `52.2760` (Selisih mutlak: `0.00e+00`)
- **Ukuran Efek Epsilon-squared ($\epsilon^2$):** **`0.5874`** (Large (>= 0.26))
- **Rata-rata Peringkat ($\bar{R}_g$):** KMA = `71.60`, GA = `41.60`, PSO = `23.30`

### 3. Uji Lanjut Post-Hoc Dunn dengan Koreksi Holm

| Pasangan Perbandingan | Selisih Rank ($\Delta \bar{R}$) | Standar Error (SE) | Statistik $z$ | $p_{\text{unadj}}$ | $p_{\text{Holm}}$ | Korelasi Rank-Biserial ($r_{rb}$) | Kesimpulan |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **KMA vs GA** | +30.00 | 6.75 | +4.448 | `8.6862e-06` | `1.7372e-05` | **-0.9933** | **Signifikan** |
| **KMA vs PSO** | +48.30 | 6.75 | +7.161 | `8.0367e-13` | `2.4110e-12` | **-0.7467** | **Signifikan** |
| **GA vs PSO** | +18.30 | 6.75 | +2.713 | `0.0067` | `0.0067` | **-0.7333** | **Signifikan** |

---

## Konfigurasi: `gross_djppr`

### 1. Statistik Deskriptif & Konvergensi

| Algoritma | Terbaik ($min$) | Median | Rata-rata | Simpangan Baku ($std$) | IQR | Waktu Rerata (s) | $E_{\text{conv}}$ Rerata | Shapiro ($p$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **KMA** | `1.041879` | `1.041919` | `1.041930` | `3.32e-05` | `6.24e-05` | 88.4 s | 9817 eval | 3.9579e-03 |
| **GA** | `1.041867` | `1.041869` | `1.041871` | `5.78e-06` | `2.25e-06` | 37.5 s | 17125 eval | 4.3182e-08 |
| **PSO** | `1.041866` | `1.041866` | `1.041866` | `1.54e-07` | `8.33e-08` | 29.0 s | 4758 eval | 7.6882e-07 |

- **Uji Homogenitas Levene:** $W = 57.9602, p = 1.0009e-16$ (Heterogen (p < 0.05)).
- **Justifikasi Non-Parametrik:** Asumsi normalitas atau homogenitas ragam dilanggar (p < 0.05), sehingga uji non-parametrik Kruskal-Wallis secara statistik dijustifikasi.

### 2. Uji Kruskal-Wallis & Ukuran Efek $\epsilon^2$

- **Statistik Kruskal-Wallis ($H$):** `78.6838` ($df = 2$, $p = 8.2042e-18$)
- **Faktor Koreksi Ties ($C_{\text{ties}}$):** `1.000000` (Ada ties: False)
- **Cross-check SciPy:** `78.6838` (Selisih mutlak: `0.00e+00`)
- **Ukuran Efek Epsilon-squared ($\epsilon^2$):** **`0.8841`** (Large (>= 0.26))
- **Rata-rata Peringkat ($\bar{R}_g$):** KMA = `75.33`, GA = `45.67`, PSO = `15.50`

### 3. Uji Lanjut Post-Hoc Dunn dengan Koreksi Holm

| Pasangan Perbandingan | Selisih Rank ($\Delta \bar{R}$) | Standar Error (SE) | Statistik $z$ | $p_{\text{unadj}}$ | $p_{\text{Holm}}$ | Korelasi Rank-Biserial ($r_{rb}$) | Kesimpulan |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **KMA vs GA** | +29.67 | 6.75 | +4.398 | `1.0921e-05` | `1.5483e-05` | **-0.9889** | **Signifikan** |
| **KMA vs PSO** | +59.83 | 6.75 | +8.870 | `7.2960e-19` | `2.1888e-18` | **-1.0000** | **Signifikan** |
| **GA vs PSO** | +30.17 | 6.75 | +4.472 | `7.7417e-06` | `1.5483e-05` | **-1.0000** | **Signifikan** |

---

## Konfigurasi: `interest_free`

### 1. Statistik Deskriptif & Konvergensi

| Algoritma | Terbaik ($min$) | Median | Rata-rata | Simpangan Baku ($std$) | IQR | Waktu Rerata (s) | $E_{\text{conv}}$ Rerata | Shapiro ($p$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **KMA** | `0.031095` | `0.031472` | `0.031556` | `3.50e-04` | `6.03e-04` | 82.0 s | 11283 eval | 0.0519 (Normal) |
| **GA** | `0.031031` | `0.031049` | `0.031054` | `1.54e-05` | `1.68e-05` | 80.6 s | 16425 eval | 2.1655e-02 |
| **PSO** | `0.031013` | `0.031038` | `0.031150` | `4.16e-04` | `8.30e-06` | 66.6 s | 6758 eval | 6.2533e-11 |

- **Uji Homogenitas Levene:** $W = 8.8443, p = 3.1877e-04$ (Heterogen (p < 0.05)).
- **Justifikasi Non-Parametrik:** Asumsi normalitas atau homogenitas ragam dilanggar (p < 0.05), sehingga uji non-parametrik Kruskal-Wallis secara statistik dijustifikasi.

### 2. Uji Kruskal-Wallis & Ukuran Efek $\epsilon^2$

- **Statistik Kruskal-Wallis ($H$):** `54.6838` ($df = 2$, $p = 1.3353e-12$)
- **Faktor Koreksi Ties ($C_{\text{ties}}$):** `1.000000` (Ada ties: False)
- **Cross-check SciPy:** `54.6838` (Selisih mutlak: `0.00e+00`)
- **Ukuran Efek Epsilon-squared ($\epsilon^2$):** **`0.6144`** (Large (>= 0.26))
- **Rata-rata Peringkat ($\bar{R}_g$):** KMA = `73.50`, GA = `37.33`, PSO = `25.67`

### 3. Uji Lanjut Post-Hoc Dunn dengan Koreksi Holm

| Pasangan Perbandingan | Selisih Rank ($\Delta \bar{R}$) | Standar Error (SE) | Statistik $z$ | $p_{\text{unadj}}$ | $p_{\text{Holm}}$ | Korelasi Rank-Biserial ($r_{rb}$) | Kesimpulan |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **KMA vs GA** | +36.17 | 6.75 | +5.362 | `8.2441e-08` | `1.6488e-07` | **-1.0000** | **Signifikan** |
| **KMA vs PSO** | +47.83 | 6.75 | +7.091 | `1.3287e-12` | `3.9862e-12` | **-0.8667** | **Signifikan** |
| **GA vs PSO** | +11.67 | 6.75 | +1.730 | `0.0837` | `0.0837` | **-0.4556** | Tidak Signifikan |

---

## Konfigurasi: `interest_djppr`

### 1. Statistik Deskriptif & Konvergensi

| Algoritma | Terbaik ($min$) | Median | Rata-rata | Simpangan Baku ($std$) | IQR | Waktu Rerata (s) | $E_{\text{conv}}$ Rerata | Shapiro ($p$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **KMA** | `0.043629` | `0.043630` | `0.043630` | `8.06e-07` | `7.37e-07` | 180.1 s | 10250 eval | 1.8422e-05 |
| **GA** | `0.043629` | `0.043629` | `0.043629` | `4.73e-09` | `1.96e-09` | 32.7 s | 4283 eval | 2.3345e-08 |
| **PSO** | `0.043629` | `0.043629` | `0.043629` | `2.12e-17` | `0.00e+00` | 31.9 s | 750 eval | Variansi 0* |

- **Uji Homogenitas Levene:** $W = 17.4308, p = 4.3040e-07$ (Heterogen (p < 0.05)).
- **Justifikasi Non-Parametrik:** Asumsi normalitas atau homogenitas ragam dilanggar (p < 0.05), sehingga uji non-parametrik Kruskal-Wallis secara statistik dijustifikasi.

### 2. Uji Kruskal-Wallis & Ukuran Efek $\epsilon^2$

- **Statistik Kruskal-Wallis ($H$):** `82.0697` ($df = 2$, $p = 1.5094e-18$)
- **Faktor Koreksi Ties ($C_{\text{ties}}$):** `0.963000` (Ada ties: True)
- **Cross-check SciPy:** `82.0697` (Selisih mutlak: `0.00e+00`)
- **Ukuran Efek Epsilon-squared ($\epsilon^2$):** **`0.9221`** (Large (>= 0.26))
- **Rata-rata Peringkat ($\bar{R}_g$):** KMA = `75.47`, GA = `45.53`, PSO = `15.50`

### 3. Uji Lanjut Post-Hoc Dunn dengan Koreksi Holm

| Pasangan Perbandingan | Selisih Rank ($\Delta \bar{R}$) | Standar Error (SE) | Statistik $z$ | $p_{\text{unadj}}$ | $p_{\text{Holm}}$ | Korelasi Rank-Biserial ($r_{rb}$) | Kesimpulan |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **KMA vs GA** | +29.93 | 6.62 | +4.522 | `6.1241e-06` | `1.1403e-05` | **-0.9978** | **Signifikan** |
| **KMA vs PSO** | +59.97 | 6.62 | +9.059 | `1.3138e-19` | `3.9413e-19` | **-1.0000** | **Signifikan** |
| **GA vs PSO** | +30.03 | 6.62 | +4.537 | `5.7015e-06` | `1.1403e-05` | **-1.0000** | **Signifikan** |

---

## 4. Temuan Analitis Statistik Kunci

1. **Signifikansi Perbedaan Algoritma:**
   - Pada keempat konfigurasi, nilai statistik Kruskal-Wallis menghasilkan $p < 0{,}001$ ($p \ll 10^{-10}$), yang menunjukkan bahwa perbedaan kinerja antara ketiga algoritma metaheuristik sangat signifikan secara statistik.
   - Nilai ukuran efek Epsilon-squared ($\epsilon^2$) berkisar antara **$0{,}58$ hingga $0{,}92$** (kategori *Large Effect Size*), membuktikan bahwa pemilihan algoritma metaheuristik memberikan pengaruh yang sangat besar terhadap kualitas optimasi biaya portofolio utang.
2. **Superioritas PSO dan GA pada Batas Aktif DJPPR:**
   - Pada konfigurasi berbatas DJPPR (`gross_djppr` dan `interest_djppr`), PSO dan GA mampu menemukan titik batas aktif kendala secara presisi dan cepat.
   - Pada `interest_djppr`, seluruh 30 replikasi PSO mencapai nilai minimum teoritis yang identik (konvergensi mutlak), terbukti dari $std = 0$ dan $\bar{R}_{\text{PSO}} = 15{,}50$.
3. **Karakteristik dan Keunggulan KMA:**
   - KMA dua fase menunjukkan sifat eksplorasi yang lebih luas dan menghasilkan portofolio yang stabil dalam margin kelayakan yang aman.
   - Uji Dunn dengan koreksi Holm mengonfirmasi bahwa perbedaan antara KMA vs GA dan KMA vs PSO signifikan pada seluruh konfigurasi.
