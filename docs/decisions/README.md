# Register Keputusan Metodologis Model & Eksperimen (Decisions Log)

Dokumen ini mencatat seluruh keputusan metodologis terbuka (*open decisions*) yang telah dibahas dan disetujui bersama pengguna sepanjang pelaksanaan tahapan penelitian tugas akhir optimasi portofolio utang negara multivaluta (MCCaR + KMA).

---

## Matriks Status Keputusan (D1 – D9)

| ID | Topik Keputusan | Berkas Keputusan | Tanggal | Status | Pilihan Terpilih & Dasar Pertimbangan |
|:---:|:---|:---|:---:|:---:|:---|
| **D1** | Pemilihan Varian Jendela Data Historis | [0001-window-mode-intersection.md](0001-window-mode-intersection.md) | 2026-10-18 | **DIPUTUSKAN** | **Opsi A (`intersection`)**: Memotong 163 baris libur/gap untuk memperoleh 2.028 hari kerja lengkap tanpa interpolasi buatan. |
| **D2** | Kalibrasi Parameter GBM & Simulasi | [0002-gbm-calibration.md](0002-gbm-calibration.md) | 2026-10-18 | **DIPUTUSKAN** | **Opsi A**: Kalibrasi drift Ito $\mu = 252\bar{m} + \sigma^2/2$, simulasi terminal 1-step horizon 1 tahun ($T=252$ hari), dan $S_0$ hari terakhir jendela. |
| **D3** | Spesifikasi Bank Validasi Independen | [0003-validation-bank-specification.md](0003-validation-bank-specification.md) | 2026-10-18 | **DIPUTUSKAN** | $N_{\text{valid}} = 20.000$ skenario, seed independen `2026`, ekor $m = 1.000$ skenario (4x lipat bank latih $N=5.000$). |
| **D4** | Detail Parameter & Mekanisme KMA 2-Fase | [0006-kma-parameters-d4.md](0006-kma-parameters-d4.md) | 2026-10-18 | **DIPUTUSKAN** | Parameter Suyanto dkk. (2022): $p_{\text{bm}} = 0{,}1$, $\gamma = 0{,}5$, $q = 2$, $\Delta n = 2$, kriteria stagnasi biaya rerata $\Delta Cost < 10^{-6}$. |
| **D5** | Penanganan Pembagian Nol pada $\theta_i$ | [0004-risk-evaluator-d5.md](0004-risk-evaluator-d5.md) | 2026-10-18 | **DIPUTUSKAN** | Nilai $\theta_i = 1{,}0$ dan penalti kuadratik halus jika marginal cost $|MC_i| < 10^{-12}$, menjaga kestabilan diferensial. |
| **D6** | Parameter Pembanding Metaheuristik GA & PSO | [0007-ga-pso-parameters-d6.md](0007-ga-pso-parameters-d6.md) | 2026-10-18 | **DIPUTUSKAN** | Inisialisasi seragam bersama pada simpleks (tanpa membocorkan $w_0$), elitisme GA $n_{\text{elite}}=2$, penyesuaian kecepatan efektif PSO pasca-proyeksi. |
| **D7** | Penanganan Koreksi Ties pada Uji Dunn | [0008-dunn-ties-d7.md](0008-dunn-ties-d7.md) | 2026-10-18 | **DIPUTUSKAN** | Menggunakan faktor koreksi ties $C_{\text{ties}}$ pada variansi standar $SE$ uji Dunn (Pers. 2.38) agar sinkron dengan uji Kruskal-Wallis. |
| **D8** | Prosedur Sampling 1.000 Titik Acak DJPPR | [0005-risk-limits-d8-sampling.md](0005-risk-limits-d8-sampling.md) | 2026-10-18 | **DIPUTUSKAN** | Sampling Dirichlet/uniform box berulang dengan proyeksi ketat hingga diperoleh tepat 1.000 kombinasi layak koridor DJPPR. |
| **D9** | Standar Tipografi, Visualisasi, & Tabel | [0009-thesis-figures-tables-d9.md](0009-thesis-figures-tables-d9.md) | 2026-10-18 | **DIPUTUSKAN** | Format ganda PDF vektor + PNG 300 dpi, tipografi serif, ramah cetak hitam-putih (hatching 7 instrumen), dan tabel LaTeX `booktabs` otomatis. |

---

## Rekapitulasi Status

- **Total Keputusan Terbuka**: 9
- **Keputusan Disetujui / Selesai**: 9 (100%)
- **Keputusan Tertunda / Belum Diputuskan**: **0**

> [!NOTE]
> Seluruh keputusan di atas telah diuji, diverifikasi integritas numeriknya, dan diimplementasikan secara penuh pada modul `src/mccar_kma/` dan konfigurasi `configs/params.yaml`.
