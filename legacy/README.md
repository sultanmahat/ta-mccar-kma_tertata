# legacy/ — referensi lama, BUKAN bagian pipeline

Isi folder ini dibuat sebelum proposal direvisi pasca-sempro. Disimpan agar tidak hilang dan bisa dijadikan pembanding. Agen tidak boleh mengimpor, mengubah, atau menjadikannya sumber kebenaran; sumber kebenaran adalah `docs/context/spesifikasi_model.md`.

| Subfolder | Isi |
|---|---|
| `execution_v0/` | Draf kode: `data_loader`, `gbm_simulation`, `risk_metrics`, `optimizer_filtering`, `optimizer_numerical`, `kma_algorithm` |
| `data_v0/` | `ir_data_clean.csv`, `fx_data_clean.csv` (2.028 baris, 3 Jul 2017 – 24 Nov 2025), `portfolio_data.csv` |
| `agent_template_v0/` | `AGENTS_3layer_template.md`: aturan agen lama (template umum 3-layer: directives/execution) |

## Selisih kode lama vs spesifikasi saat ini

| Aspek | Kode lama (`execution_v0`) | Spesifikasi (revisi proposal) |
|---|---|---|
| Variabel yang disimulasikan | GBM langsung pada deret biaya tiap instrumen, 7 deret, **independen** (seed+i), tanpa korelasi | GBM pada 9 variabel pasar (7 yield + 2 kurs) dengan guncangan berkorelasi (Cholesky), lalu biaya dihitung dari nilai terminal (Bab 3 langkah 5) |
| Biaya skenario | Rasio `C_terminal / C_0` | `C_{i,s} = q_s (1 + y_{i,s}/100)`, `q = X_0 / X_s` (Pers. 2.1–2.2) |
| Fungsi objektif | `μᵀw`, μ = rata-rata log-change **harian** biaya | `Cost̄(w)` = rata-rata biaya portofolio atas 5.000 skenario (Pers. 2.15) |
| Biaya marginal `MC_i` | `δ·μ_i` (bisa ≈ 0 atau negatif sehingga θ_i tidak bermakna; hanya bila |MC| < 1e-9 dipaksa `1e-9`) | `δ·mean(C_{s,i})` > 0 (Pers. 2.16) |
| CCaR | `np.percentile` lalu rata-rata biaya ≥ batas | Rata-rata tepat `m = ceil((1−α)N) = 250` biaya tertinggi (Pers. 2.13) |
| Kendala keseimbangan MCCaR | **Tidak ada** | `J_MCCaR(w) ≤ η`, `η = J(w0)` (Pers. 2.20–2.22) |
| Kriteria "efisiensi" pada filtering | Rata-rata `abs(θ_i − 1)` | Proposal menyatakan `θ_i = 1` bukan target; ukurannya simpangan baku θ (J) |
| Batas risiko τ | `CCaR(bobot tengah) × 1,05` (heuristik) | `τ = CCaR(w0)` portofolio eksisting 2024 (Pers. 2.22) |
| Penalti | `100 · pelanggaran²`, hanya CCaR, tanpa normalisasi | `ρ = 1e6`, pelanggaran relatif ternormalisasi untuk J dan CCaR (Pers. 2.23–2.24), arsip solusi layak |
| KMA | Satu fase, `n_pop=50`, `p_big=0,3`, 200 iterasi, henti bila norma selisih ≤ ε | Dua fase (n_pop 5 lalu 200 adaptif), anggaran 25.000 evaluasi (Tabel 3.1) |
| Anggaran evaluasi | Tidak dihitung | Dihitung dan dibatasi 25.000 |
| RNG | `np.random.seed` global | `numpy.random.Generator` per replikasi |
| Nomor persamaan di docstring | Penomoran proposal lama (mis. CCaR = 2.10) | Penomoran revisi (CCaR = 2.13) |

Ide yang masih layak dipertimbangkan sebagai masukan Tahap 5/7 (keputusan tetap di plan, bukan disalin): proyeksi bobot berbasis pergeseran-bisection di `kma_algorithm.project_to_feasible_weights` (proyeksi eksak ke irisan batas dan Σw = 1), dan pembanding SLSQP di `optimizer_numerical.py` (hanya untuk sanity check).

## Data lama

`data_v0/ir_data_clean.csv` dan `fx_data_clean.csv` identik dengan irisan lengkap dari `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` (2.028 baris, selisih yield maksimum 0). Berarti varian `intersection` (D1-A) sudah dipakai secara implisit dan interpolasi spline belum pernah diterapkan. Perhitungan log-change per baris pada data ini melintasi celah 1 Feb – 15 Sep 2021 sebagai satu langkah (−2,7% pada EUR_10Y, ≈ 5,9 simpangan baku). Dampaknya pada σ tahunan kecil (7,35% vs 7,29%) tetapi harus ditangani eksplisit.
