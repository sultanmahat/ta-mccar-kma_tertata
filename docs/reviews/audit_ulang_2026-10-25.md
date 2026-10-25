# Audit Ulang 2026-10-25 — Proposal Revisi vs Kode, Klaim Laporan, Keputusan, dan Tes

- **Sifat**: audit READ-ONLY. Satu-satunya file yang ditulis adalah dokumen ini. Tidak ada kode, data, hasil, atau keputusan yang diubah.
- **Rujukan**: `docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf` (48 halaman fisik) dan `docs/context/spesifikasi_model.md`. Draf LaTeX lama tidak dipakai.
- **Konvensi halaman**: "hlm. X (fisik Y)" — X = nomor cetak, Y = halaman PDF; untuk isi Bab 1–3, Y = X + 10.
- **Commit yang diaudit**: `0e35594` (HEAD `master`).
- **Aturan bukti**: setiap temuan berbasis angka direproduksi dengan membaca `results/` dan `data/processed/` (perintah dijalankan tanpa menulis file). Temuan disebut "bug" hanya bila direproduksi; tidak ada yang dikategorikan bug kode di audit ini.

## Ringkasan

| Tingkat | Jumlah |
|---|---:|
| Kritis | 0 |
| Tinggi | 6 |
| Sedang | 8 |
| Rendah | 11 |
| **Total** | **25** |

Persamaan inti pada proposal (2.1–2.3, 2.13–2.20, 2.22–2.24, 2.25–2.36) **cocok** dengan kode. Batas DJPPR, w₀, tenor EUR 7Y = 8, rentang data, ukuran bank, dan desain 4×3×30×25.000 juga cocok. Masalah utama ada di tempat lain:
- parameter KMA fase 2 (`d`) yang tidak tercatat di mana pun;
- config yang tidak benar-benar dibaca eksperimen;
- sejumlah klaim di laporan review yang tidak didukung atau bertentangan dengan angka di `results/` — termasuk dua laporan yang ditulis pada sesi ini.

---

## Bagian 1 — Proposal vs kode dan config

### 1.1 Tabel kesesuaian

| Butir | Proposal | Kode / config | Status |
|---|---|---|---|
| Pers. 2.1 faktor kurs q = X₀/X_s, q_USD=1 | hlm. 10 (fisik 20) | `src/mccar_kma/scenarios/cost.py:63-65` | Cocok |
| Pers. 2.2 biaya bruto q(1+y/100), utama | hlm. 11 (fisik 21) | `cost.py:124` | Cocok |
| Pers. 2.3 biaya bunga q·y/100, sensitivitas | hlm. 11 (fisik 21) | `cost.py:127` | Cocok |
| Tabel 2.1 instrumen, EUR Fixed 7Y tenor 8 | hlm. 10 (fisik 20) | `configs/params.yaml:36-97` (`tenor: 8` di baris 66) | Cocok (direproduksi: ketujuh tenor sama) |
| Tabel 2.2 w₀, lb, ub | hlm. 11 (fisik 21) | `params.yaml:41-97`; `src/mccar_kma/model/constraints.py:17-18,25-33` | Cocok (direproduksi: `np.array_equal` = True untuk lb, ub, w₀; Σw₀ = 1,0) |
| Pers. 2.13 CCaR, m = ⌈(1−α)N⌉ = 250 | hlm. 15–16 (fisik 25–26) | `src/mccar_kma/risk/ccar.py:40` (dengan pembulatan pengaman), `:72` | Cocok |
| Pers. 2.14–2.17 MC, MCCaR (δ = 0,01, tanpa penyeimbangan) | hlm. 16–17 (fisik 26–27) | `src/mccar_kma/risk/mccar.py:45, 86-90` | Cocok |
| Pers. 2.18 θ = MCCaR/MC, MC ≠ 0 | hlm. 17 (fisik 27) | `mccar.py:129-130` (D5: θ = 0 bila \|MC\| ≤ 1e-12) | Cocok; kasus MC = 0 diisi keputusan D5 |
| Pers. 2.19–2.20 θ̄ dan J (pembagi n) | hlm. 17 (fisik 27) | `mccar.py:132, 163` (`ddof=0`) | Cocok |
| Pers. 2.21 min Cost̄ dengan kendala J≤η, CCaR≤τ, Σw=1, lb≤w≤ub | hlm. 18 (fisik 28) | evaluator, proyeksi `constraints.py`, arsip layak `src/mccar_kma/model/penalty.py:126-162` | Cocok |
| Pers. 2.22 η = J(w₀), τ = CCaR(w₀) pada bank yang sama | hlm. 19 (fisik 29) | `data/processed/risk_limits_bank_train_seed42_N5000.json`; `src/mccar_kma/experiments/runner.py:55-59` | Cocok |
| Pers. 2.23 v_J, v_R relatif, penyebut max(\|·\|, ε_tol) | hlm. 20 (fisik 30) | `constraints.py:217-221` | Cocok |
| Pers. 2.24 f = Cost̄ + ρ_J v_J² + ρ_R v_R² | hlm. 20 (fisik 30) | `penalty.py:49` | Cocok |
| Pers. 2.25 n* = ⌊p_bm(n_pop−1)⌋, n_bm = min{max{n*,2}, n_pop−3} | hlm. 22 (fisik 32) | `src/mccar_kma/optimizers/kma.py:56-57` | Cocok |
| Pers. 2.26–2.27 gerak big male, r₁,r₂ ~ U(0,1) | hlm. 23 (fisik 33) | `kma.py:297-306` | Cocok. Aturan seleksi setelah gerak tidak ditentukan proposal |
| Pers. 2.30 partenogenesis γ\|ub−lb\| | hlm. 23 (fisik 33) | `kma.py:349-350` | Cocok |
| Pers. 2.31–2.32 mlipir per dimensi bila r₂ < d | hlm. 23 (fisik 33) | `kma.py:370-373` | Cocok |
| Adaptasi n fase 2: membesar saat stagnan, mengecil saat membaik | hlm. 31 (fisik 41) | `kma.py:408-418` | Cocok |
| Pers. 2.33–2.34 crossover aritmetika, mutasi Gaussian σ_m | hlm. 26 (fisik 36) | `src/mccar_kma/optimizers/ga.py:136-150` | Cocok |
| Pers. 2.35–2.36 PSO, r₁,r₂ ~ U[0,1] elemen-per-elemen | hlm. 27 (fisik 37) | `src/mccar_kma/optimizers/pso.py:139-152` | Cocok |
| Pers. 2.39 ε² = H/(N−1) | hlm. 28 (fisik 38) | `src/mccar_kma/analysis/stats_tests.py:126` | Cocok |
| Tabel 3.1 parameter | hlm. 32 (fisik 42) | default kelas KMA/GA/PSO/evaluator ↔ `params.yaml` | Nilai identik (direproduksi via `inspect.signature`); lihat S1 |
| Rentang data 2.028 hari, 3 Jul 2017–24 Nov 2025 | hlm. 3 & 30 (fisik 13 & 40) | `data/processed/market_2017-07-03_2025-11-24_intersection.csv`: 2.028 baris, 0 NaN | Cocok |
| Bank 5.000 skenario; validasi lebih besar dengan benih berbeda | hlm. 32 (fisik 42) | latih (5000, 7); validasi (20000, 7), seed 2026 | Cocok |
| 4 konfigurasi × 3 algoritma × 30 replikasi, 25.000 evaluasi, benih sama | hlm. 31–32 (fisik 41–42) | `results/tables/runs_summary.csv`: 360 baris, 30 per grup, `evaluations` = {25000}, daftar seed 43–72 identik di 12 grup, 1 `config_hash` | Cocok |

**Catatan "kendala 3.x"**: proposal revisi **tidak** memuat persamaan bernomor (3.x). Kendala di Bab 3 (tahap 6–9, hlm. 30–31) hanya merujuk Pers. (2.21)–(2.24). Label "Pers. 3.2" di audit lama berasal dari draf LaTeX usang.

### 1.2 Temuan Bagian 1

**T5 — Tinggi. Mlipir rate fase 2 (`d = 0,5`) adalah parameter tak tercatat.**
- **Bukti**:
  - `src/mccar_kma/optimizers/kma.py:187` berisi `mlipir_rate_2 = 0.5` sebagai literal di kode.
  - Nilai ini tidak ada di:
    - Tabel 3.1 proposal (hlm. 32, fisik 42), yang hanya menyebut d fase pertama;
    - `docs/context/spesifikasi_model.md:154`;
    - D4 (`docs/decisions/0006-kma-parameters-d4.md`);
    - `configs/params.yaml` (blok `algorithms.kma.phase_2` hanya berisi `n_pop_*` dan `budget`).
  - Parameter ini berpengaruh pada hasil. Ablasi Tahap 18 (`results/sensitivity/kma/ablation_tests.csv`) menunjukkan `kma_d2_low` signifikan lebih baik dari default pada `gross_free` (p_Holm = 0,0031) dan `interest_free` (p_Holm = 0,047).
- **Saran**: daftarkan sebagai KEPUTUSAN (aturan AGENTS.md no. 2), pindahkan ke `params.yaml`, dan sebutkan di Bab 3. Tidak perlu mengubah nilainya.

**S1 — Sedang. Config tidak dialirkan ke eksperimen utama; konstanta diduplikasi di kode.**
- **Bukti**:
  - `src/mccar_kma/experiments/runner.py:118` membuat optimizer dengan `algo_cls()` tanpa argumen.
  - `runner.py:110` (dalam `execute_single_run`) membuat `PortfolioEvaluator(cost_matrix=…, tau=…, eta=…)` tanpa α, δ, ρ, ε_tol.
  - `constraints.py:17-18,25-33` meng-hardcode LB/UB/W₀.
  - Saat ini semua nilai identik dengan `params.yaml` (direproduksi), jadi **tidak ada dampak pada hasil**. Tetapi mengubah `params.yaml` tidak akan mengubah eksperimen.
  - Tidak ada tes yang membandingkan default kelas atau konstanta kode dengan `params.yaml`. `tests/test_decisions_consistency.py` hanya membandingkan `params.yaml` dengan README keputusan.
- **Saran**: alirkan blok config ke konstruktor, atau tambahkan tes kesetaraan default-vs-config.

**S2 — Sedang. Proposal menjanjikan interpolasi spline yang tidak dipakai di pipeline utama.**
- **Bukti**:
  - Bab 3 tahap 3 (hlm. 30, fisik 40): "Nilai yang hilang akibat perbedaan hari libur pasar diisi menggunakan interpolasi cubic spline … Persamaan (2.4) sampai (2.6)." Pers. 2.4–2.6 diuraikan di hlm. 12–13 (fisik 22–23).
  - D1 Opsi A (`intersection`) memakai 2.028 baris tanpa interpolasi. Spline hanya dipakai sebagai varian sensitivitas (2.191 baris).
  - `audit_akhir_v2.md:17` menyatakan kesesuaian "100%" tanpa membahas hal ini.
- **Saran**: Bab 3 skripsi perlu menyelaraskan: spline hanya untuk sensitivitas D1-B, atau jelaskan bahwa irisan tanggal tidak menyisakan nilai hilang.

**S3 — Sedang. Salah hitung pada contoh ilustrasi J_MCCaR di proposal.**
- **Bukti**: hlm. 19 (fisik 29) menulis √(⅓[(0,10)² + (−0,15)² + (0,05)²]) ≈ 0,0855. Nilai benar: √(0,035/3) = **0,1080**. Dengan η = 0,09, contoh itu justru **melanggar** kendala (0,108 > 0,09). Kesimpulan paragraf ("masih memenuhi kendala") terbalik.
- **Saran**: perbaiki di naskah skripsi (PDF proposal read-only, tidak diubah).

**R4 — Rendah. Inkonsistensi notasi dan penamaan di proposal.**
- **Bukti**:
  - Batasan Masalah hlm. 3 (fisik 13) menulis "EUR 8Y", sedangkan Tabel 2.1 menulis "EUR Fixed 7Y" (tenor 8).
  - Tabel 2.3 (hlm. 17, fisik 27) memakai r_i dan r̄, padahal teks memakai θ_i dan θ̄.
- **Saran**: seragamkan di skripsi.

**R11 — Rendah. Angka literal kecil di KMA.**
- **Bukti**: `kma.py:399-400` memakai lantai `1e-12` sebagai literal.
- **Saran**: pindahkan ke config bersama S1.

---

## Bagian 2 — Klaim di `docs/reviews` dan hasil Tahap 16–20 vs angka di `results/`

### 2.1 Tinggi

**T1 — Rincian pelanggaran PSO di `audit_akhir_v2.md` tidak cocok dengan data.**
- **Klaim**:
  - `audit_akhir_v2.md:73-79`: run PSO yang tidak layak adalah `rep_04` dan `rep_21`.
  - Keduanya disebut melanggar **τ = 0,028889** dengan slack latih +0,000003/+0,000002 dan CCaR validasi 0,029053/0,029171.
  - `:47` mengulang klaim "melanggar τ … slack ≈ 10⁻⁵".
- **Data** (`results/tables/validation_interest_free.csv`):
  - Run yang tidak layak adalah **PSO rep 25 dan rep 28**.
  - Yang dilanggar adalah **η**: `val_v_J` = 0,0378 dan 0,0093, sedangkan `val_v_R` = 0.
  - τ `interest_free` = 0,064969, CCaR latih 0,04944 dan 0,04910, jadi slack τ ≈ 0,0155, jauh dari batas.
  - Angka 0,028889 tidak ada di tabel `results/tables` mana pun.
  - Ringkasan Tahap 12 (`results/tables/validation_summary.md`) sendiri sudah benar menyebut pelanggaran η.
- **Saran**: tarik §4.2 dan AUD-V2-02, lalu tulis ulang dari CSV. Jangan dikutip ke Bab 4.

**T2 — Kesalahan skala 100× di laporan Tahap 17 (ditulis pada sesi ini).**
- **Klaim** di `docs/reviews/studi_stabilitas_limit.md`:
  - `:45` `gross_djppr` 6,6% / 4,8%
  - `:46` `gross_free` 56,6–58,5% / 50,9–51,0%
  - `:47` `interest_djppr` 200,7% / 201,4%
  - `:52` |optimism gap| ≤ 1,4 poin persen
- **Data** (`results/sensitivity/limits/summary_savings.csv` × 100):
  - `gross_djppr` **0,066% / 0,048%**
  - `gross_free` **0,566–0,585% / 0,509–0,510%**
  - `interest_djppr` **2,007% / 2,014%**
  - optimism gap ≤ **0,014** poin persen
  - Angka `interest_free` (27,58–27,66% / 30,27–30,29%) benar.
  - Arah kesimpulan "bank-42 lebih rendah/lebih tinggi" tetap benar.
- **Saran**: koreksi keempat baris tersebut.

**T3 — Solusi 360-run `interest_free` 0/30 layak terhadap batas "benar"; klaim "~5–10%" keliru.**
- **Klaim**:
  - `studi_stabilitas_limit.md:106`: solusi "layak" eksperimen utama hanya tetap layak di ~5–10% bank lain.
  - `docs/decisions/0010-limit-stability-d10.md:18` dan `studi_stabilitas_limit.md:117`: tiga konfigurasi lain "kelayakan validasi 40–100%".
- **Data**:
  - Angka 5–10% di Tahap 17 berasal dari solusi yang dioptimasi di **20 bank lain**, bukan solusi 360-run.
  - Reproduksi: solusi 360-run dievaluasi di bank validasi N = 20.000 dengan η_v, τ_v dihitung dari w₀ pada bank itu (η_v = 0,149065, τ_v = 0,064173 untuk interest; η_v = 0,067652, τ_v = 1,085888 untuk gross).

  | Konfigurasi | KMA | GA | PSO |
  |---|---:|---:|---:|
  | `interest_free` | **0/30** | **0/30** | **0/30** |
  | `gross_djppr` | 24/30 | **10/30** | 17/30 |
  | `gross_free` | 27/30 | 30/30 | 29/30 |
  | `interest_djppr` | 30/30 | 30/30 | 30/30 |

  - Hasil `gross_djppr` GA (33%) juga di bawah rentang "40–100%".
  - Ini **tidak** bertentangan dengan Tahap 12. Spesifikasi §10 memang mempertahankan batas bank latih saat validasi, dan dengan aturan itu kelayakan ≈ 100%. Tetapi besaran yang dipakai sebagai dasar D10 tercatat terlalu ringan.
- **Saran**: perbarui angka di laporan Tahap 17 dan catatan D10, lalu pertimbangkan apakah Opsi C masih memadai. Keputusan tetap di tangan Sultan; audit ini tidak mengubahnya.

**T4 — Dekomposisi "88% kupon / 12% depresiasi" di Tahap 16 tidak didukung.**
- **Klaim**:
  - `docs/reviews/sensitivitas_drift.md:71`: ~88% penghematan `interest_free` berasal dari kupon (26,51/30,29).
  - `:170`: model "terbukti memiliki ketahanan (*robustness*) tinggi".
- **Data**:
  - Tiap skenario memakai **bank berbeda** (seed 42/1042/2042/3042; `scripts/16_analyze_drift_sensitivity.py:69-90`). Efek drift tercampur dengan galat Monte Carlo antar-bank.
  - Tahap 17 mengukur galat itu dengan **drift historis yang sama** pada 20 bank (`summary_savings.csv`):
    - penghematan `interest_free` PSO: rerata 27,58%, sd 1,50, q05–q95 **24,97–29,67%**, rentang 24,55–30,50;
    - nilai skenario "drift kurs = 0" (26,51%) **berada di dalam** sebaran itu;
    - bank-42 (basis, 30,29%) justru di ekor atas.
  - Urutan antarskenario juga tidak monoton: martingale 31,78% dan shrinkage 31,99% > basis 30,29%.
- **Saran**: ulang dengan *common random numbers* (Z sama, hanya μ berbeda; `src/mccar_kma/scenarios/gbm.py` sudah memungkinkan ini karena Z hanya bergantung pada seed dan korelasi) dan beberapa bank per skenario. Sebelum itu, hapus klaim persentase dekomposisi.

**T6 — Klaim "KMA kompetitif, selisih < 0,05%" di `audit_akhir_v2.md:93` keliru.**
- **Data** (`runs_summary.csv`, selisih rerata biaya):

  | Konfigurasi | KMA vs PSO | KMA vs GA |
  |---|---:|---:|
  | `interest_free` | **+1,30%** | **+1,62%** |
  | `gross_free` | +0,070% | +0,096% |
  | `gross_djppr` | +0,006% | +0,006% |
  | `interest_djppr` | +0,0015% | +0,0015% |

- **Saran**: jangan dikutip. Pakai tabel selisih praktis Tahap 20 (`results/tables/stats_praktis.csv`).

### 2.2 Sedang

**S4 — Pembingkaian K3/K4/K5 di `docs/reviews/diagnosis_kma.md:24-36` tidak menyebut bahwa kode sesuai proposal.**
- **Bukti**:
  - K3 (mlipir Bernoulli per dimensi), K4 (⌊p(n−1)⌋), dan K5 (uniform) disebut "deviasi" terhadap paper Suyanto.
  - Proposal (sumber kebenaran proyek) menetapkan ketiganya persis seperti kode: Pers. 2.31, Pers. 2.25, dan "U(0,1)" pada hlm. 23 (fisik 33).
  - Klaim "K5 ambigu" (`:34, :211`) sudah terjawab oleh proposal.
  - Hanya K1 (aturan seleksi big male) dan K2 (urutan sinkron) yang tidak ditentukan proposal.
- **Saran**: tulis "berbeda dari paper, sesuai proposal". Kesimpulan H1 tidak berubah.

**S5 — Teks "Temuan Analitis" Tahap 13 (`results/tables/stats_summary.md`) melebihi data.**
- **Bukti**:
  - `:139`: ε² besar "membuktikan … pengaruh yang sangat besar terhadap kualitas optimasi biaya". Padahal Tahap 20 menunjukkan **semua pasangan** ekuivalen dalam margin 0,01% di `gross_djppr` dan `interest_djppr` (`stats_praktis.csv`).
  - `:141`: "PSO dan GA mampu menemukan titik batas aktif kendala" pada DJPPR. Padahal di `interest_djppr` kendala J/CCaR aktif pada 0% run; optimum ditentukan oleh vertex kotak (97% run, rata-rata 6/7 bobot di batas; `stats_praktis.csv`).
  - `:142`: "nilai minimum teoritis … std = 0". Tidak ada pembuktian optimum teoritis, dan std tercatat 2,12×10⁻¹⁷, bukan 0.
  - `:144`: "KMA … stabil dalam margin kelayakan yang aman" tidak didukung. Std KMA paling besar di 4 konfigurasi.
- **Saran**: sajikan berdampingan dengan Tahap 20, dan hapus kalimat yang melebihi data. Bagian inferensial (H, p, Dunn) tetap valid.

**S6 — Waktu "1 proses" `gross_free/KMA` di Tahap 19 tidak bersih.**
- **Bukti**:
  - `results/tables/timing_single_worker_360.csv`: `gross_free/KMA` rep 1–4 = 42,6 / 43,8 / 44,3 / 34,3 s, rep 5 = 24,5 s.
  - Sel KMA lain 23–27 s, dan run pertama yang terputus (log 2026-10-25 12:00) memberi 24,5–25,0 s untuk sel yang sama.
  - Anomali ini bertepatan dengan perubahan `PROCTHROTTLEMAX` 80%→100% di tengah run (dilakukan pada sesi ini).
  - `docs/reviews/signifikansi_praktis.md:74` melaporkan median 42,64 s (rasio 0,58×) sebagai waktu bersih.
- **Saran**: ulang sel itu dengan pengaturan daya tetap, atau beri catatan.

**S7 — Label "100% Layak (Robust)" di `results/tables/validation_summary.md:23-34` berlebihan.**
- **Bukti**: label itu sesuai prosedur spesifikasi §10 (batas bank latih). Tetapi temuan T3 menunjukkan kelayakan sangat bergantung pada estimasi batas bank-42, sehingga kata "Robust" berlebihan.
- **Saran**: ganti menjadi "layak terhadap batas bank latih".

**S8 — Klaim deskriptif di `audit_akhir_v2.md` tidak didukung.**
- **Bukti**:
  - `:46` (AUD-V2-01): "pada seluruh konfigurasi PSO terendah, disusul GA, lalu KMA". Pada `interest_free`, GA vs PSO tidak signifikan (p_Holm = 0,0837, `stats_dunn_interest_free.csv`). Pada `gross_djppr` dan `interest_djppr` ketiganya ekuivalen praktis (Tahap 20).
  - `:96`: "meningkatkan porsi JPY dan EUR … θ_i di sekitar 1,0". Solusi `gross_free` memberi EUR 0% (`validation_summary.md`, komposisi). θ_i pada solusi interest berkisar ~1,12–1,54 (`results/runs/interest_djppr/pso/rep_01_seed43.json`).
  - `:94`: waktu KMA "disebabkan mlipir yang memeriksa tetangga secara intensif". Profil Tahap 18 hanya menunjukkan overhead loop/kontrol (64–74%) tanpa mengatribusikannya ke mlipir (`results/sensitivity/kma/profile_kma.csv`).
- **Saran**: revisi ketiga klaim.

### 2.3 Rendah

- **R2 — Jumlah worker eksperimen utama.**
  - Log `logs/run_experiments_20261018_050402.log` mencatat 357 run dengan **6 worker**.
  - 3 run (`gross_djppr` rep 1 KMA/GA/PSO; waktu 32,7 / 8,6 / 9,2 s) dijalankan sebelumnya dengan 1 worker (`logs/run_experiments_20261018_045810.log`). Ketiganya tercampur ke statistik waktu Tahap 13.
  - `README.md:103` dan `scripts/run_all.ps1:86` menyebut 4 worker.
- **R3 — Definisi margin D12 berbeda dengan implementasi.**
  - D12 dan `params.yaml:364` mendefinisikan margin relatif terhadap "median grup pembanding".
  - `scripts/20_analyze_practical_significance.py:59` memakai median gabungan ketiga algoritma.
  - Selisih numeriknya dapat diabaikan, tetapi definisinya tidak sama.
- **R5 — Pembulatan.** `studi_stabilitas_limit.md:35` menulis "14,3%". Nilai (0,174188 − 0,149065)/0,174188 = **14,4%**.
- **R6 — Uji yang tidak tercatat.**
  - `audit_akhir_v2.md:18` menulis "KMA hemat vs eksisting … p < 0,001", tetapi uji itu tidak ada di `results/`.
  - Datanya mendukung arah klaim: KMA < biaya w₀ pada 30/30 run di tiap konfigurasi (uji tanda p = 9,3×10⁻¹⁰).
  - Cantumkan uji yang dipakai.
- **R7 — Klaim dan detail `sensitivitas_drift.md` tanpa dukungan data.**
  - `:162`: "penghematan 0,5% setara puluhan triliun rupiah" tanpa data nominal.
  - `:158`: istilah "sidang munaqasyah" (bukan istilah ITS).
  - Seed optimizer 43–52 beririsan dengan seed eksperimen utama.
  - Evaluator di skrip 16 tidak membaca config.
- **R8 — Klaim stabilitas GA/PSO pada H2 di `diagnosis_kma.md`.**
  - Klaim "GA dan PSO juga relatif stabil terhadap pergeseran" hanya berlaku untuk median.
  - Rerata PSO melonjak (`results/sensitivity/kma/benchmark_fidelity.csv`): Sphere D30 0,00198 → 222,98; Rosenbrock D30 215,0 → 169.236,6.
- **R1 — Komentar usang.** `params.yaml:260` masih menulis "KEPUTUSAN D10 TERBUKA", padahal D10 sudah diputuskan (0010).
- **R10 — Nomor berkas keputusan ≠ nomor D.** Contoh: `0004`=D5, `0005`=D8, `0006`=D4. Pemetaan hanya ada di README, sehingga membingungkan saat merujuk.
- **R9 — Celah tes.** Fungsi analisis di `scripts/16_analyze_drift_sensitivity.py` tidak punya tes. Logikanya berada di skrip, bukan di `src/`.

---

## Bagian 3 — Keputusan dan tes

- **Status keputusan**: 12 berkas keputusan (D1–D12) berstatus "Dikonfirmasi oleh Sultan" (diverifikasi via grep). Nilai di README cocok dengan `params.yaml` untuk D2, D3 (20000/2026), D5 (1e-12), D7 (`true`), D8 (1000/rejection/42), dan D12 (0,01). Default kelas untuk D4 dan D6 juga cocok (lihat S1 untuk risikonya).
- **Celah keputusan**: d fase 2 (T5) tidak tercakup D4.
- **Tes**: hasil `pytest tests/ -q -p no:cacheprovider` dicantumkan di bawah. Fungsi inti punya tes sifat matematis:
  - `cost.py` dan `build_scenario_bank` di `tests/test_gbm.py`;
  - CCaR/MCCaR/J dengan kasus hitung tangan dan pembagi n di `tests/test_risk.py:40,106`;
  - violasi relatif dan proyeksi di `tests/test_constraints.py`;
  - ukuran grup KMA di `tests/test_kma.py`.
- **Celah tes**: lihat S1 (tidak ada tes default kode = config) dan R9.

Hasil: `pytest tests/ -q -p no:cacheprovider` → **142 passed in 244.64s (0:04:04)**, exit code 0. Catatan: lulusnya tes tidak menutup temuan S1 (tidak ada tes yang mengikat konstanta kode ke `params.yaml`), T5 (`mlipir_rate_2` tidak diuji terhadap config), dan R9 (script 16 tanpa tes).

---

## Hal yang sengaja tidak dikerjakan

- Tidak ada perbaikan file. Semua saran di atas menunggu persetujuan.
- `docs/reviews/rekap_chat_instruksi_dan_jawaban.md` (1.774 baris) adalah log percakapan, bukan laporan klaim. Hanya diperiksa sekilas, tidak diaudit per klaim.
- `docs/reviews/review_tahap05-08_2026-10-18.md` dan audit lama yang sudah dicabut tidak diaudit ulang per baris. Status "dicabut" pada audit lama sudah tercantum di kepalanya.
