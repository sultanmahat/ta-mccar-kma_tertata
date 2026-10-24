# Register Keputusan Metodologis Model & Eksperimen (Decisions Log)

Dokumen ini mencatat seluruh keputusan metodologis teknis yang melengkapi rincian komputasi yang tidak ditentukan secara eksplisit dalam proposal tugas akhir optimasi portofolio utang negara multivaluta (MCCaR + KMA).

> [!NOTE]
> **Status Persetujuan Formal:** Seluruh keputusan D1–D9 dan D11 telah resmi ditinjau dan dikonfirmasi (**"Dikonfirmasi oleh Sultan"**) oleh Sultan Bakri Baihaqi Mahat pada tanggal 24 Oktober 2026. Seluruh opsi yang ditetapkan adalah **Opsi A** (rekomendasi metodologis berbasis literatur dan data pasar riil).

---

## Matriks Status Keputusan (D1 – D9 & D11)

| ID | Topik Keputusan | Berkas Keputusan | Tanggal Usulan | Tanggal Konfirmasi | Status | Pilihan yang Dikonfirmasi & Nilai Persis `configs/params.yaml` |
|:---:|:---|:---|:---:|:---:|:---:|:---|
| **D1** | Pemilihan Varian Jendela Data Historis | [0001-window-mode-intersection.md](0001-window-mode-intersection.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A (intersection)**: Memotong 163 baris libur/gap untuk memperoleh 2.028 hari kerja lengkap (3 Juli 2017 s.d. 24 November 2025) tanpa interpolasi buatan. *(Tercantum di naskah resmi proposal)*. |
| **D2** | Kalibrasi Parameter GBM & Simulasi | [0002-gbm-calibration.md](0002-gbm-calibration.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: `scenarios.drift_calibration: "ito_annualized"` ($\mu = 252\bar{m} + \sigma^2/2$, $\sigma = s\sqrt{252}$), `simulation_path_mode: "terminal_1step"` ($T=252$ hari), dan `historical_cost_x0: "window_end"` (kurs 24 Nov 2025). |
| **D3** | Spesifikasi Bank Validasi Independen | [0003-validation-bank-specification.md](0003-validation-bank-specification.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: `scenarios.validation_scenarios: 20000`, `validation_seed: 2026`: $N_{\text{valid}} = 20.000$ skenario, ekor $m = 1.000$ skenario pada $\alpha = 0{,}95$ (4x lipat bank latih $N=5.000$). |
| **D4** | Detail Parameter & Mekanisme KMA 2-Fase | [0006-kma-parameters-d4.md](0006-kma-parameters-d4.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: **Fase 1:** $n_{\text{pop}}=5$, $d=6/7$, budget 5.000. **Fase 2:** $n_{\text{pop\_init}}=200$, rentang $n \in [20, 200]$, budget 20.000.<br>**Parameter:** $p_{\text{bm}} = 0{,}5$; $\gamma = 0{,}1$; $p_{\text{mating}} = 0{,}5$; $\Delta n(a) = 5$; $q_{\text{interactions}} = \text{null}$ (seluruh $n_{\text{bm}}$); $\epsilon_{\text{stag}} = 10^{-7}$; kesabaran = 2; transisi fase = warisi solusi terbaik + 199 acak baru. |
| **D5** | Penanganan Pembagian Nol pada $\theta_i$ | [0004-risk-evaluator-d5.md](0004-risk-evaluator-d5.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: `risk.zero_tolerance_mc: 1.0e-12`: Jika nilai mutlak $|\text{MC}_i| \le 10^{-12}$, maka rasio $\theta_i$ ditetapkan sama dengan **$0{,}0$ (netral)** untuk mencegah `ZeroDivisionError` tanpa manipulasi gradien. |
| **D6** | Parameter Pembanding Metaheuristik GA & PSO | [0007-ga-pso-parameters-d6.md](0007-ga-pso-parameters-d6.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: **GA:** $n_{\text{pop}}=50$, turnamen 2, $p_{\text{cross}}=0{,}9$, $p_{\text{mut}}=1/7$, $\sigma_m=0{,}1 \times \text{rentang}$, elitisme $n_{\text{elite}}=2$.<br>**PSO:** $n_{\text{pop}}=50$, inersia $0{,}9 \to 0{,}4$ linear, $c_1=c_2=1{,}49618$, $v_{\text{max}}=0{,}2 \times \text{rentang}$, peredaman kecepatan berbasis perpindahan efektif. |
| **D7** | Penanganan Koreksi Ties pada Uji Dunn | [0008-dunn-ties-d7.md](0008-dunn-ties-d7.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: `analysis.dunn_ties_correction: true`: Menggunakan faktor koreksi ties $C_{\text{ties}}$ pada variansi standar $SE$ uji Dunn (Pers. 2.38) agar sinkron dengan uji omnibus Kruskal-Wallis. |
| **D8** | Prosedur Sampling 1.000 Titik Acak DJPPR | [0005-risk-limits-d8-sampling.md](0005-risk-limits-d8-sampling.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: `experiments.random_benchmark_count: 1000`, `method: "rejection"`, `seed: 42`: Sampling acak seragam dengan proyeksi dan filter ketat hingga diperoleh tepat 1.000 titik layak di dalam batas alokasi DJPPR. |
| **D9** | Standar Tipografi, Visualisasi, & Tabel | [0009-thesis-figures-tables-d9.md](0009-thesis-figures-tables-d9.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A**: Format ganda PDF vektor + PNG 300 dpi, tipografi serif (`DejaVu Serif`), pola arsir (*hatching*) 7 instrumen untuk cetak hitam-putih, dan tabel LaTeX `booktabs` otomatis tanpa *hardcoded numbers*. |
| **D11** | Kebijakan Penalaan Parameter yang Adil (*Fair Tuning Policy*) | [0011-fair-tuning-policy-d11.md](0011-fair-tuning-policy-d11.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A (Default Literatur / Status Quo Proposal)**: Ketiga algoritma (KMA, GA, PSO) menggunakan parameter default rujukan literatur masing-masing (Suyanto 2022, Goldberg, Eberhart/Shi) sesuai Tabel 3.1 proposal tanpa penalaan selektif tambahan. |

---

## Rekapitulasi Status

- **Total Keputusan Teknis**: 10
- **Status Dikonfirmasi oleh Sultan**: **10** (D1–D9, D11 - Seluruh Opsi A)
- **Status Menunggu Konfirmasi Sultan**: **0**
- **Status Ditolak**: **0**

> [!NOTE]
> Seluruh keputusan metodologis di atas telah dikonfirmasi secara sah oleh mahasiswa peneliti (Sultan Bakri Baihaqi Mahat) pada 24 Oktober 2026 dan menjadi dasar metodologi komputasi resmi untuk draf naskah skripsi Bab 3, 4, dan 5.
