# Diagnosis KMA v2 — Fidelitas, Ablasi, Kendala Aktif, Konvergensi

**Tahap**: 18 (`scripts/18_diagnose_kma_fidelity.py`)
**Tanggal run**: 2026-10-25 (Tahap A selesai 04:22 WIB, 1.877,8 s setelah restart 10 worker; Tahap B selesai 10:19 WIB, 21.402,1 s; 0 tugas gagal di kedua tahap)
**Config hash**: `6360d66ead242fd37c47adf564ee0cdfc5b1e4fbc2f94e0467ad6238882459a8`
**Data mentah**: `results/sensitivity/kma/*.csv`, `runs_benchmark/`, `runs_instrument/`, `runs_ablation/`, `runs_timing/`
**Verifikasi**: `pytest tests/test_kma_diagnosis.py` — 121 test lulus (termasuk seluruh suite, bukan hanya file ini). Hash SHA-256 dari 431 file `results/runs/`, `results/tables/`, `results/figures/` identik sebelum/sesudah run — **360 run eksperimen utama tidak diubah**.

> **Cara baca**: laporan ini adalah diagnosis, bukan vonis. Status tiap hipotesis adalah salah satu dari **didukung**, **tidak didukung**, atau **inkonklusif**, berdasarkan data yang diukur di bawah. Tidak ada klaim "KMA buruk" atau "KMA baik" di luar angka yang ditunjukkan.

---

## 1. Koreksi atas laporan 2026-10-18

Laporan Tahap 15 lama (diarsip di `docs/reviews/archive/diagnosis_kma_2026-10-18.md`) punya tiga masalah yang diperbaiki di sini:

1. **Tidak dibandingkan dengan Tabel 2 Suyanto dkk. (2022).** Laporan ini membandingkan langsung (Bagian 4).
2. **Slack salah label.** CSV lama `slack_distribution_analysis.csv` berisi slack **absolut**; angka evaluator 0,012/0,018 yang sering dikutip adalah slack **relatif** (η−J)/η. Direproduksi di `slack_360.csv` (Bagian 6): KMA `gross_free` slack relatif mean 0,01776 / median 0,01266 (absolut mean 0,00121); `interest_free` slack relatif mean 0,01207 / median 0,00432 (absolut mean 0,00210). Konsisten dengan angka lama, cuma beda satuan — bukan temuan baru, cuma koreksi notasi.
3. **Mekanisme (ledakan langkah, dugaan "penguncian") ditulis sebagai terbukti tanpa data pendukung.** Di laporan ini, klaim yang sama (H3) diuji dengan instrumentasi nyata (Bagian 5) dan dilabeli status, bukan ditulis sebagai fakta.
4. **Seed ablasi lama (43–52) tumpang tindih dengan 360 run utama, hanya 10 replikasi, parameter hardcode.** Ablasi Tahap 18 pakai seed 42000+ (portofolio) dan 40000+/41000+ (benchmark), 30 replikasi, seluruh parameter dari `configs/params.yaml`.

---

## 2. Deviasi implementasi kma.py vs Suyanto dkk. (2022) — K1–K5

Dibaca baris per baris terhadap Algorithm 1 dan Persamaan 1–10 paper. **Tidak ditemukan bug jelas** (salah ketik/rumus terbalik) — `kma.py` tidak diubah. Lima titik ambigu/berbeda interpretasi:

| ID | Deviasi | Paper | Kode (`kma.py`) | Diuji sbg variant |
|---|---|---|---|---|
| K1 | Seleksi Big Male | Pool: gabung lama∪baru (2q), simpan q terbaik | Greedy per-indeks: baru vs posisi lamanya sendiri | `kma_paper_pool` |
| K2 | Urutan update | Tersirat sinkron | Asinkron (Big Male ke-i pakai Big Male j<i yg sudah diupdate di generasi sama) | `kma_sync` |
| K3 | Dimensi mlipir | Pilih 1..(m−1) dimensi (tidak 0, tidak semua) | Bernoulli(d) bebas per (j,l) → bisa 0 atau semua dimensi | `kma_paper_mlipir` |
| K4 | Ukuran grup q | q = ⌊p·n⌋ (tercetak ⌊(p−1)n⌋, salah cetak jelas) | q = ⌊p(n−1)⌋ (n=200 → 99, bukan 100) | `kma_paper_q` |
| K5 | Distribusi r1,r2 | "random... in the normal distribution" (ambigu) | Uniform [0,1] | Tidak diuji — ambigu di sumber |

> **Koreksi 2026-10-25 (S4, audit ulang):** tabel K1–K5 di atas membandingkan kode hanya terhadap paper Suyanto dkk. (2022) — sumber kebenaran **proyek ini** adalah proposal, bukan paper tersebut. Terhadap proposal, K3, K4, dan K5 **sesuai**, bukan deviasi: K3 cocok dengan Persamaan 2.31 proposal (Bernoulli per dimensi); K4 cocok dengan Persamaan 2.25 (⌊p(n−1)⌋); K5 cocok dengan teks proposal hlm. 23 ("U(0,1)"). Hanya **K1** (aturan seleksi Big Male) dan **K2** (urutan sinkron/asinkron) yang benar-benar tidak ditentukan oleh proposal. "Deviasi" K3–K5 di tabel berarti deviasi dari paper akademik rujukan, bukan dari spesifikasi proyek yang disetujui.

Status setelah Tahap 18: lihat **H1** di Bagian 4. Ringkasnya — **tidak satu pun variant K1–K4 (sendiri atau gabungan `kma_paper_all`) menutup selisih ke Tabel 2 Suyanto**; deviasi ini bukan penyebab utama gap fidelitas.

---

## 3. Fidelitas vs Tabel 2 Suyanto dkk. (2022)

D=50, 25.000 evaluasi, 30 run, domain sama dengan paper. Sumber: `benchmark_vs_suyanto.csv`, `benchmark_fidelity.csv`.

| Fungsi | Algo | Kami (mean ± std) | Paper (avg ± std) | Rasio |
|---|---|---|---|---|
| Sphere (F1) | KMA | 12.660,8 ± 3.240,6 | 0,0 ± 0,0 | — (paper = 0 eksak) |
| Sphere (F1) | GA | 13,88 ± 2,61 | 43,80 ± 5,26 | GA kami **lebih baik** |
| Rosenbrock (F5) | KMA | 14.905.728 ± 6.044.067 | 48,31 ± 0,182 | ≈ 308.000× lebih buruk |
| Rosenbrock (F5) | GA | 340,8 ± 84,5 | 634,7 ± 130,0 | GA kami **lebih baik** |
| Rastrigin (F9) | KMA | 527,2 ± 39,3 | 0,0 ± 0,0 | — (paper = 0 eksak) |
| Rastrigin (F9) | GA | 42,57 ± 9,21 | 121,3 ± 15,09 | GA kami **lebih baik** |

Catatan: GA kami memakai parameter Tabel 3.1 proyek ini (n=50, turnamen 2, pc=0,9, mutasi Gaussian), **bukan** parameter GA paper (n=100, turnamen 10, pc=0,8, creep pm=0,05) — perbedaan ini sudah tercatat di `benchmark_vs_suyanto.csv` kolom `note`, bukan temuan baru.

**Pola kunci**: KMA kami gagal total pada ketiga fungsi di D=50 (dan juga di D=7/D=30, lihat `benchmark_fidelity.csv`), sementara GA kami justru mengungguli GA paper. Ini bukan soal "mesin benchmark salah" (GA/PSO berjalan baik), melainkan spesifik pada KMA.

**D=7 dan D=30** (bukan dimensi paper, tapi menunjukkan tren): KMA sphere D=7 mean 92,1 (vs optimum 0), D=30 mean 3.659,7. `median_at_5000` == `median_at_10000` == nilai akhir untuk hampir semua baris D=30/D=50 — **Fase 2 (generasi 1.000–25.000 KMA) tidak memperbaiki solusi Fase 1 pada fungsi benchmark**, konsisten dengan temuan di 360 run portofolio.

---

## 4. Hipotesis dan status

### H1 — Implementasi menyimpang dari paper (K1–K4) → gagal benchmark
**Uji**: varian `kma_paper_pool`, `kma_sync`, `kma_paper_mlipir`, `kma_paper_q`, `kma_paper_all` vs default pada Sphere/Rastrigin/Rosenbrock, D∈{7,30}. Sumber: `benchmark_fidelity.csv` (set=`variants`).

Contoh Rosenbrock D=7: default (median) 2.168,8; `kma_paper_all` 1.934,3; `kma_paper_pool` 3.672,1; `kma_sync` 2.435,1; `kma_paper_q` 2.168,8 (identik — q tidak berubah hasil pada D=7). Semua masih 40–75× lebih buruk dari 48,31 (target paper, meski beda dimensi).

**Status: TIDAK DIDUKUNG.** Tidak ada variant K1–K4 (sendiri maupun gabungan) yang mendekati performa Tabel 2. Deviasi interpretasi bukan penyebab utama gap fidelitas benchmark.

### H2 — Bias titik-asal (optimum paper di 0; KMA terlemah di Rosenbrock yang optimumnya di 1)
**Uji**: fungsi tergeser (optimum di vektor acak ber-seed, shift_domain_fraction=0,8) untuk KMA, `kma_paper_all`, GA, PSO. Sumber: `benchmark_fidelity.csv` (set=`shifted`).

Sphere D=30: base KMA mean 3.659,7 vs tergeser 3.458,3 (≈ sama). Rosenbrock D=30: base KMA mean 2.102.946 vs tergeser 2.505.645 (≈ sama orde besaran, malah sedikit lebih buruk saat tergeser, bukan lebih baik). Mediannya GA dan PSO relatif stabil terhadap pergeseran. **Koreksi 2026-10-25 (R8, audit ulang):** klaim "GA dan PSO juga relatif stabil ... tidak ada lonjakan degradasi" hanya berlaku untuk **median**, bukan **rerata** — rerata PSO justru melonjak tajam (`benchmark_fidelity.csv`): Sphere D=30 base 0,00198 → tergeser 222,98; Rosenbrock D=30 base 214,99 → tergeser 169.236,65. Lonjakan rerata ini didorong oleh beberapa replikasi dengan nilai ekstrem (lihat kolom `max`), bukan pergeseran sistematis seluruh sebaran.

**Status: TIDAK DIDUKUNG.** Performa KMA tidak berubah signifikan saat optimum dipindah dari titik asal. Bukan bias posisi optimum.

### H3 — Ledakan langkah Big Male di Fase 2 → mayoritas kandidat ditolak
**Uji**: instrumentasi per generasi (‖Δ‖ sebelum proyeksi relatif ke rentang domain, rasio penerimaan Big Male) pada portofolio, 4 konfigurasi. Sumber: `kma_phase_summary.csv`.

| Config | Fase | Generasi/run | Penerimaan BM | Step norm median (rel. rentang) | Step norm p90 |
|---|---|---|---|---|---|
| gross_free | 1 | 908,5 | 0,2184 | 1,3×10⁻¹⁵ | 1,6×10⁻⁵ |
| gross_free | 2 | 99,0 | **0,0123** | **2,105** | 2,626 |
| interest_free | 1 | 908,5 | 0,1827 | 4,1×10⁻¹⁷ | 2,5×10⁻⁶ |
| interest_free | 2 | 99,0 | **0,0123** | **2,863** | 3,458 |

Step norm Fase 2 **> 1** berarti langkah Big Male lebih besar dari seluruh rentang domain [lb,ub] — bukan sekali-sekali, tapi median-nya. Penerimaan Big Male jatuh dari ~18–32% (Fase 1) ke ~1–2% (Fase 2) di keempat konfigurasi.

**Status: DIDUKUNG.** Langkah Big Male di Fase 2 (populasi besar, Σ atas q−1≈98 vektor tanpa normalisasi skala) secara sistematis melebihi rentang domain, menyebabkan hampir seluruh kandidat ditolak.

### H4 — Kelaparan generasi Fase 2 (hanya ~99 generasi)
**Uji**: 360 run (perbaikan 5k→25k eval) + ablasi `kma_one_phase_n5` (skip Fase 2, populasi kecil sepanjang anggaran) dan `kma_one_phase_n200` (populasi besar sepanjang anggaran). Sumber: `phase_improvement_360.csv`, `ablation_tests.csv`.

360 run: perbaikan biaya median eval 5.000→25.000 untuk KMA: `gross_free` 0,124% (83% run membaik), `interest_free` 0,516% (60% run membaik), `interest_djppr` 0,0049% (83%), `gross_djppr` ≈0 (50%). Sebagai pembanding, GA membaik di 93–100% run. Jadi Fase 2 KMA (80% anggaran) memberi perbaikan kecil dan tidak konsisten; 40% run `interest_free` dan 50% run `gross_djppr` sama sekali tidak membaik 5k→25k.

Ablasi: `kma_one_phase_n5` signifikan **lebih baik** dari default pada `gross_djppr` (p=1,1×10⁻⁶, p_Holm=7,5×10⁻⁶, rank-biserial 0,73; gap median 0,0021% vs 0,0076%). Pada `interest_djppr` tidak signifikan (p=0,29). Pada `gross_free`, `kma_one_phase_n5` (gap 0,093%) ≈ default (0,099%, p=0,29). Pada `interest_free`, `kma_one_phase_n5` lebih baik (gap median 0,536% vs 1,553%, p=0,031) tetapi tidak signifikan setelah koreksi Holm (p_Holm=0,22).

**Status: INKONKLUSIF, condong didukung sebagian.** Fase 2 secara konsisten memperburuk atau tidak membantu pada 3 dari 4 konfigurasi saat diuji formal (hanya `gross_djppr` signifikan setelah koreksi Holm), tapi arah efek konsisten: skip Fase 2 (`one_phase_n5`) tidak pernah secara signifikan lebih buruk dari default. Jumlah generasi Fase 2 (99) tidak sendirian menjelaskan — H3 (step explosion) adalah mekanisme yang lebih langsung didukung datanya.

### H5 — Kendala aktif tidak didekati: proyeksi memetakan ke sudut (a), atau penalti menolak kandidat dekat batas (b)
**Uji**: instrumentasi tiap kandidat (jarak raw→proyeksi, % v_J>0, % diterima), KMA/GA/PSO, 4 konfigurasi, dibagi jendela eval 1–5000 vs 5001–25000. Sumber: `instrumentation_summary.csv`.

KMA `gross_free`, jendela 5001–25000: `frac_raw_out_box`=98,48%, `mean_proj_dist`=6,93 (jarak raw→proyeksi **jauh lebih besar** dari rentang [0,1] kotak bebas), `frac_feasible` turun dari 89,7% (Fase 1) ke 21,2% (Fase 2), `frac_vJ_pos` naik dari 8,4% ke 70,9%, `frac_vR_pos` naik dari 5,8% ke 77,7%. Pola serupa di `interest_free` (proj_dist 7,67; frac_feasible turun 95,5%→57,3%) dan `gross_djppr`/`interest_djppr` (proj_dist 0,54–0,79; magnitude lebih kecil karena domain DJPPR lebih sempit, tapi arah sama).

Bandingkan GA: `frac_raw_out_box` naik moderat (22%→30% `gross_free`), `proj_dist` jauh lebih kecil (0,059→0,060), `frac_feasible` relatif stabil (68%→75%). PSO serupa GA, tidak menunjukkan lonjakan jarak proyeksi di Fase akhir.

**Status: DIDUKUNG — opsi (a).** Penolakan KMA di Fase 2 didominasi oleh jarak proyeksi besar (kandidat mentah jatuh jauh di luar kotak, bukan sedikit melewati batas), konsisten dengan H3: Big Male melangkah lebih besar dari domain, diproyeksikan paksa ke sudut kotak, lalu banyak kandidat hasil proyeksi melanggar kendala (v_J>0 naik ke 65,7% `gross_djppr`, 70,9% `gross_free`, 42,6% `interest_free`; di `interest_djppr` hanya 8,1% karena batas J di konfigurasi itu longgar). Bukan kasus (b) "penalti menolak kandidat yang nyaris layak" — jarak proyeksi terlalu besar untuk itu.

### H6 — Waktu KMA didominasi overhead loop Python, bukan evaluator
**Uji**: cProfile 1 run/konfigurasi, 1 worker, budget penuh. Sumber: `profile_kma.csv`.

| Config | Algo | Total (s) | Evaluator (s) | Proyeksi (s) | Lainnya/loop (s) | % "lainnya" |
|---|---|---|---|---|---|---|
| gross_free | kma | 27,70 | 6,56 | 0,73 | 20,42 | 73,7% |
| gross_free | ga | 7,52 | 6,43 | 0,04 | 1,06 | 14,0% |
| gross_free | pso | 10,70 | 9,09 | 0,84 | 0,77 | 7,2% |
| interest_djppr | kma | 30,98 | 6,26 | 4,84 | 19,89 | 64,2% |
| interest_djppr | ga | 7,42 | 6,16 | 0,23 | 1,03 | 13,8% |

KMA ~3–4× lebih lambat dari GA/PSO meski evaluator (bagian yang sama untuk ketiga algoritma) memakan waktu hampir sama (6,2–9,1 s untuk ketiganya). Mayoritas waktu KMA (64–74%) ada di kategori "lainnya" — kontrol fase, adaptasi n_pop, sortir populasi, pembentukan kandidat — bukan evaluasi fungsi objektif maupun proyeksi.

**Status: DIDUKUNG.** Waktu KMA didominasi overhead kontrol/loop Python (terutama adaptasi populasi dan manajemen generasi Fase 2 dengan n hingga 200), bukan oleh evaluator maupun proyeksi.

---

## 5. Ringkasan status hipotesis

| H | Deskripsi singkat | Status |
|---|---|---|
| H1 | Deviasi K1–K4 menyebabkan gagal fidelitas | **Tidak didukung** |
| H2 | Bias titik-asal paper | **Tidak didukung** |
| H3 | Ledakan langkah Big Male Fase 2 | **Didukung** |
| H4 | Kelaparan generasi Fase 2 | **Inkonklusif** (condong: arah konsisten, signifikansi formal cuma 1/4 konfigurasi setelah koreksi) |
| H5 | Penolakan kandidat = proyeksi ke sudut, bukan penalti dekat batas | **Didukung (opsi a)** |
| H6 | Waktu KMA didominasi overhead loop, bukan evaluator | **Didukung** |

**Rangkaian kausal yang konsisten dengan seluruh data**: parameter default Fase 2 (n_pop hingga 200, Σ atas q−1≈98 vektor tanpa normalisasi skala terhadap populasi) menghasilkan langkah Big Male yang secara median melebihi rentang domain (H3) → kandidat mentah jauh di luar kotak, diproyeksikan paksa ke sudut (H5) → sebagian besar kandidat hasil proyeksi melanggar batas J≤η → tingkat penerimaan Fase 2 jatuh ke ~1–2%, hampir tidak ada perbaikan setelah Fase 1 pada benchmark dan sebagian konfigurasi portofolio (H4, parsial) → overhead kontrol populasi besar + banyak kandidat ditolak membuat KMA 3–4× lebih lambat per evaluasi (H6). Deviasi interpretasi K1–K4 (H1) dan posisi optimum (H2) **bukan** bagian dari rangkaian ini.

---

## 6. Slack dan kendala aktif (360 run, read-only)

Sumber: `slack_360.csv`. Direproduksi persis dari CSV lama (koreksi notasi, bukan temuan baru):

| Config | Algo | Slack J absolut (median) | Slack J relatif (median) |
|---|---|---|---|
| gross_free | kma | 0,000863 | 0,01266 |
| gross_free | pso | ≈0 (−6,8×10⁻¹⁰) | ≈0 |
| interest_free | kma | 0,000752 | 0,00432 |
| interest_free | pso | ≈0 | ≈0 |
| interest_djppr | kma | 0,01426 | 0,08185 |
| interest_djppr | pso | 0,01426 | 0,08186 |

Catatan `interest_djppr`: KMA dan PSO punya slack yang **hampir sama** (konfigurasi ini memang punya batas yang tidak ketat bagi ketiganya — lihat `gap_pct_25000` median KMA 0,0688% vs PSO 0,0000% pada config ini, keduanya kecil). Pola "KMA jauh dari limit, PSO di limit" paling jelas di `gross_free` (gap KMA 0,097% vs PSO 0,000%) dan `interest_free` (gap KMA 1,48% vs PSO 0,081%).

---

## 7. Konvergensi dan waktu (lintas evaluasi dan lintas detik)

Grafik: `fig_kma_convergence_all.{pdf,png}` (sumbu-x evaluasi) dan `fig_kma_convergence_time_all.{pdf,png}` (sumbu-x detik, memakai peta waktu 1 worker dari `timing_single_worker.csv`, panel waktu di luar rentang terukur di-NaN-kan — lihat perbaikan `_time_grid`). Median (garis), rata-rata (putus-putus), pita IQR, titik 5k/10k/25k ditandai.

Waktu median 25.000 eval, 1 worker (`timing_summary.csv`): KMA 24,5–27,1 s; GA 7,0–7,3 s; PSO 6,9–7,4 s di keempat konfigurasi. Rasio KMA/GA ≈ 3,4–3,7×, konsisten dengan H6.

---

## 8. Ablasi portofolio — ringkasan

Sumber: `ablation_summary.csv`, `ablation_tests.csv` (Mann-Whitney vs `kma_default`, koreksi Holm, rank-biserial), 9 variant × 4 konfigurasi × 30 replikasi, seed 42000+, bank sama dengan 360 run (seed 42).

Variant yang **signifikan lebih baik** dari default setelah koreksi Holm:
- `kma_one_phase_n5` pada `gross_djppr` (p_Holm=7,5×10⁻⁶, rank-biserial 0,73): gap median turun dari 0,0076% ke 0,0021%.
- `kma_paper_pool` pada `gross_djppr` (p_Holm=8,5×10⁻⁷, rank-biserial 0,80): gap median turun ke 0,0027%.
- `kma_d2_low` pada `gross_free` (p_Holm=0,0031, rank-biserial 0,53): gap median turun dari 0,099% ke 0,044%.
- `kma_norm_q` pada `interest_djppr` (p_Holm=8,3×10⁻⁴, rank-biserial 0,58): gap median turun dari 0,0014% ke 0,0000076%.
- `kma_d2_low` pada `interest_free` (p_Holm=0,047, rank-biserial 0,42): gap median turun dari 1,553% ke 0,858%.

Kolom `gap_pct` sudah dalam satuan persen terhadap biaya referensi terbaik per konfigurasi. Selisih absolut di konfigurasi DJPPR sangat kecil (orde 0,001%), jadi signifikan secara statistik belum tentu bermakna secara praktis.

Tidak ada satu variant yang menang di keempat konfigurasi sekaligus — perbaikan bersifat spesifik-konfigurasi, bukan perbaikan universal. **Variant ini adalah analisis sensitivitas, bukan usulan ganti parameter default** (lihat Bagian 9, D11).

---

## 9. D11 — dibuka ulang, dikonfirmasi ulang Opsi A (2026-10-25)

**Status**: setelah membaca hasil Tahap 18, pengguna menginstruksikan untuk mengikuti rekomendasi di bawah (Opsi A). Dicatat sebagai tinjauan ulang di `docs/decisions/0011-fair-tuning-policy-d11.md`. Opsi yang dipertimbangkan dipertahankan di bawah sebagai jejak alasan.

Pertanyaan: apakah 360 run eksperimen utama memakai parameter KMA/GA/PSO default literatur (Tabel 3.1, status quo) atau hasil tuning setara anggaran?

**Opsi A — Default literatur (status quo, Tabel 3.1).**
(+) Tidak mengubah 360 run yang sudah ada dan tervalidasi; sesuai proposal; nol biaya tambahan; tidak ada derajat kebebasan peneliti yang bisa dipertanyakan.
(−) KMA default (n2=200) dirancang untuk benchmark D≥50; pada masalah portofolio D=7 berkendala ketat, parameter ini menghasilkan Fase 2 yang sering merugikan (Bagian 4, H3–H5). Penguji bisa menilai perbandingan tidak adil bagi KMA.

**Opsi B — Tuning ketiga algoritma, anggaran sama.**
Protokol: random search 40 konfigurasi × 3 replikasi × 25k eval per algoritma per definisi biaya, pada bank tuning terpisah (seed baru, mis. 70000 — bukan 42/2026/43–72/10000+/20000+/40000+/41000+/42000+/43000+/44000+), ruang parameter dideklarasikan sebelum mulai, konfigurasi terbaik dibekukan, 360 run diulang ke `results/runs_tuned/` (360 lama **tetap**, tidak dihapus).
(+) Adil terhadap potensi algoritma; menjawab kritik "KMA tidak di-tuning".
(−) Biaya besar (≈720 run tuning + 360 run ulang, perkiraan 10–15 jam berdasar laju Tahap 18); mengubah Tabel 3.1 — butuh persetujuan eksplisit per AGENTS.md; memperbesar cakupan Bab 3–4 skripsi.

**Temuan Tahap 18 yang relevan untuk keputusan ini**: ablasi Bagian 8 menunjukkan sebagian variant KMA (bukan tuning acak, tapi perubahan terarah seperti `one_phase_n5`, `paper_pool`, `d2_low`) memperbaiki gap secara signifikan pada beberapa konfigurasi — ini sinyal bahwa KMA default memang punya ruang perbaikan di masalah ini, tapi juga bukti bahwa perbaikannya tidak seragam di semua konfigurasi (jadi "tuning satu angka ajaib" tidak realistis; perlu ruang pencarian formal seperti Opsi B kalau mau ditempuh).

**Rekomendasi (bukan keputusan)**: Opsi A untuk hasil utama Bab 3–4 (360 run tetap seperti sudah ada), dengan ablasi Tahap 18 (Bagian 8) dilaporkan sebagai **analisis sensitivitas** di bab diskusi — bukan tuning terpilih. Alasan: tidak mengubah desain yang sudah disetujui; ablasi formal (bukan trial-and-error) sudah menjawab "apakah KMA bisa lebih baik dengan setelan lain" tanpa memilih pemenang secara selektif. Rekomendasi ini yang diikuti (lihat status di atas).

### Bug kma.py (klarifikasi)
Tidak ditemukan bug jelas di `kma.py`. K1–K4 (Bagian 2) adalah deviasi interpretasi, bukan bug, dan Bagian 4 (H1) menunjukkan variant yang memperbaiki K1–K4 **tidak** menutup gap fidelitas ke paper. Mekanisme yang benar-benar didukung data (H3, H5: ledakan langkah Fase 2 + proyeksi ke sudut) adalah **karakteristik parameter default** (n2=200, Σ tanpa normalisasi — sesuai Persamaan 3–4 paper, bukan kesalahan transkripsi), bukan bug implementasi. Jika Sultan menilai salah satu variant ablasi (mis. `kma_paper_pool` atau `one_phase_n5`) layak jadi default baru, itu adalah usulan perubahan desain terpisah (D12) — belum dikerjakan di sini, dan bila disetujui berarti 120 run KMA di 360-run harus diulang.

---

## 10. Keterbatasan

- Benchmark memakai penanganan batas *clipping* murni (`box_only_projection`), bukan simpleks — paper tidak menyebutkan penanganan batas untuk fungsi uji, jadi ini asumsi kami, dicatat bukan diverifikasi ke paper.
- GA paper memakai parameter berbeda dari Tabel 3.1 proyek ini (dicatat di Bagian 3); perbandingan sphere/rosenbrock/rastrigin untuk GA bersifat indikatif, bukan replikasi presisi.
- K5 (distribusi r1, r2) tidak diuji karena rumusan paper ambigu ("random dalam distribusi normal" tanpa parameter).
- Ablasi Bagian 8 adalah sensitivitas pada bank seed 42 (bank yang sama dengan 360 run) — bukan validasi independen; kalau salah satu variant mau dipakai sebagai default baru (D12), perlu divalidasi di bank independen (seed 2026) sebelum diklaim generalisasi.
- H4 (kelaparan generasi) diuji tidak langsung (lewat ablasi 1-fase, bukan lewat eksperimen varying jumlah generasi Fase 2 secara terkontrol) — status inkonklusif mencerminkan keterbatasan desain uji ini, bukan bukti kuat salah satu arah.

## 11. Temuan di luar cakupan (dicatat, tidak dikerjakan)

- `src/mccar_kma/analysis/limit_stability.py` (Tahap 17) belum punya test sendiri — tidak ada file di `tests/` yang mengimpornya. Dicatat sebagai gap, bukan diperbaiki di sini.
- Bug ablasi Tahap 15 lama (seed tumpang tindih, bounds hardcode free untuk semua config) sudah diperbaiki secara desain di Tahap 18, tidak di skrip lama (`scripts/15_diagnose_kma.py` tidak diubah, sesuai batasan).
- Selama proses run, laptop sempat masuk Modern Standby (~3 jam, 2026-10-25 00:39–03:35) yang membuat satu batch task tercatat `time_seconds` keliru tinggi (bukan bug algoritma — lihat `runs_benchmark/stage_a/sphere_D30_base_kma_rep07..12_*.json`, `time_seconds`≈10.678 s vs sebaris lainnya ≈130 s). Sleep dimatikan via `powercfg` untuk sisa run; angka `time_seconds` pada file-file itu **tidak dipakai** di ringkasan timing manapun pada laporan ini (timing resmi berasal dari `timing_single_worker.csv`, dijalankan sebelum insiden sleep terjadi).
