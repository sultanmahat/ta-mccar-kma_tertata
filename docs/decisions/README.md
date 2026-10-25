# Register Keputusan Metodologis Model & Eksperimen (Decisions Log)

Dokumen ini mencatat seluruh keputusan metodologis teknis yang melengkapi rincian komputasi yang tidak ditentukan secara eksplisit dalam proposal tugas akhir optimasi portofolio utang negara multivaluta (MCCaR + KMA).

> [!NOTE]
> **Status Persetujuan Formal:** Seluruh keputusan D1–D9 dan D11 telah resmi ditinjau dan dikonfirmasi (**"Dikonfirmasi oleh Sultan"**) oleh Sultan Bakri Baihaqi Mahat pada tanggal 24 Oktober 2026 (Seluruh opsi Opsi A); D10 dikonfirmasi 25 Oktober 2026 (Opsi C); D12 dikonfirmasi 25 Oktober 2026 (Opsi A); D13 dikonfirmasi 25 Oktober 2026 (Opsi A).

---

## Matriks Status Keputusan (D1 – D13)

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
| **D10** | Perlakuan Ketidakpastian Monte Carlo pada Batas Risiko (η, τ) | [0010-limit-stability-d10.md](0010-limit-stability-d10.md) | 2026-10-24 | 2026-10-25 | **Dikonfirmasi oleh Sultan** | **Opsi C (Pertahankan Bank 42, Laporkan Ketidakpastian)**: Batas η dan τ tetap dihitung dari bank seed 42 (360 run tidak diulang); temuan studi 20-bank independen (Tahap 17) — terutama kelayakan validasi rendah pada `interest_free` — dilaporkan sebagai keterbatasan di Bab 4/5, bukan dipakai merevisi hasil utama. **Addendum 2026-10-25**: dasar angka dikoreksi dengan evaluasi langsung 360 run terhadap batas bank validasi (Tahap 21; `interest_free` 0/90 layak, `gross_djppr` 51/90, pelanggaran hanya pada kendala J); Opsi C dipertahankan. |
| **D11** | Kebijakan Penalaan Parameter yang Adil (*Fair Tuning Policy*) | [0011-fair-tuning-policy-d11.md](0011-fair-tuning-policy-d11.md) | 2026-10-18 | 2026-10-24 | **Dikonfirmasi oleh Sultan** | **Opsi A (Default Literatur / Status Quo Proposal)**: Ketiga algoritma (KMA, GA, PSO) menggunakan parameter default rujukan literatur masing-masing (Suyanto 2022, Goldberg, Eberhart/Shi) sesuai Tabel 3.1 proposal tanpa penalaan selektif tambahan. Ditinjau ulang 2026-10-25 setelah Diagnosis KMA v2 (Tahap 18): tetap Opsi A. |
| **D12** | Margin Ekivalensi Praktis untuk Uji TOST | [0012-practical-equivalence-margin-d12.md](0012-practical-equivalence-margin-d12.md) | 2026-10-25 | 2026-10-25 | **Dikonfirmasi oleh Sultan** | **Opsi A (Margin Seragam 0,01%)**: `practical_significance.equivalence_margin_pct: 0.01`, margin relatif 0,01% dari median biaya grup pembanding, diterapkan seragam di keempat konfigurasi untuk uji ekivalensi (TOST) pada analisis signifikansi praktis Tahap 19-20. |
| **D13** | Laju Mlipir ($d$) Fase 2 KMA | [0013-kma-phase2-mlipir-rate-d13.md](0013-kma-phase2-mlipir-rate-d13.md) | 2026-10-25 | 2026-10-25 | **Dikonfirmasi oleh Sultan** | **Opsi A (Pertahankan $d_2=0{,}5$)**: `algorithms.kma.phase_2.mlipir_rate: 0.5`, `algorithms.kma.phase_2.population_adapt_floor: 1.0e-12` — nilai yang sudah dipakai sejak 360 run utama, tidak diubah (konsisten D11 Fair Tuning Policy). Temuan ablasi `kma_d2_low` (Tahap 18) dicatat sebagai limitasi/arah penelitian lanjutan, bukan revisi hasil utama. |

---

## Rekapitulasi Status

- **Total Keputusan Teknis**: 13
- **Status Dikonfirmasi oleh Sultan**: **13** (D1–D9, D11, D12, D13 - Opsi A; D10 - Opsi C)
- **Status Menunggu Konfirmasi Sultan**: **0**
- **Status Ditolak**: **0**

> [!NOTE]
> Seluruh keputusan metodologis D1–D13 telah dikonfirmasi secara sah oleh mahasiswa peneliti (Sultan Bakri Baihaqi Mahat) pada 24–25 Oktober 2026 dan menjadi dasar metodologi komputasi resmi untuk draf naskah skripsi Bab 3, 4, dan 5.
