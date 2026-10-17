# Panduan Prompt Antigravity — TA MCCaR + KMA

Dokumen ini berisi: (1) cara mengatur Antigravity sekali di awal, (2) struktur folder dan penamaan, (3) peta model per tahap, (4) prompt siap tempel untuk tahap 0–15, (5) template perbaikan.

Aturan kerja yang berlaku di semua tahap ada di `AGENTS.md` (dibaca agen otomatis dari root proyek). Rumus, parameter, dan keputusan terbuka ada di `docs/context/spesifikasi_model.md`. Karena itu prompt di bawah sengaja pendek dan menunjuk ke dua file tersebut, tidak menempel ulang rumus.

---

## 1. Pengaturan sekali di awal

1. Unzip `ta-mccar-kma_tertata.zip`, lalu buka foldernya: **File → Open Folder → `ta-mccar-kma`**. Isinya sudah: `AGENTS.md`, spesifikasi model, dataset di `data/raw/`, proposal di `docs/proposal/`, pustaka yang sudah dikelompokkan di `docs/references/`, template LaTeX di `report/`, dan kode/data lama di `legacy/` (hanya referensi). Penjelasan penataan: `docs/laporan_penataan_folder.md`.
2. Di pengaturan agen, atur **Artifact Review Policy** ke opsi yang meminta review (bukan "Always proceed"), dan kebijakan eksekusi terminal ke opsi yang meminta persetujuan. Dengan begitu agen berhenti di plan dan bertanya sebelum menjalankan perintah.
3. **Satu tahap = satu percakapan baru.** Konteks panjang membuat agen lupa aturan. Konteks antartahap dibawa oleh file (`AGENTS.md`, spesifikasi, `docs/decisions/`), bukan oleh riwayat chat.
4. Pilih **model di dropdown sebelum** mengirim prompt (lihat tabel di bagian 3).
5. Mode percakapan: **Planning** untuk semua tahap yang mengubah kode. Mode Fast hanya untuk perubahan kecil atau tugas read-only (tahap 9 dan 15b).

### Alur di setiap tahap

```
ketik /plan + prompt  →  agen menulis Implementation Plan (belum ada kode)
→ Anda baca  →  beri komentar inline di plan  →  klik Review untuk mengirim komentar
→ agen merevisi plan  →  ulangi sampai puas  →  klik Proceed
→ agen mengerjakan  →  baca Walkthrough  →  jalankan sendiri / cek output  →  commit
```

`/plan` adalah perintah resmi Antigravity untuk memicu perencanaan terstruktur kapan saja ([dokumentasi Implementation Plan](https://www.antigravity.google/docs/implementation-plan)). Format prompt di bawah (Konteks / Tugas / Output / Batasan / Selesai bila) bukan format wajib; itu hanya membuat maksud Anda tidak ambigu.

### Cara memilah isi plan

Jangan klik Proceed sebelum plan memuat empat hal: daftar file yang akan dibuat/diubah, daftar **KEPUTUSAN DIBUTUHKAN**, cara verifikasi (tes dan angka yang akan ditampilkan), dan hal yang sengaja tidak dikerjakan.

Contoh komentar yang jelas untuk plan:

- `Pilih opsi B. Alasan: sesuai proposal Bab 3 langkah 3.`
- `Setuju, tapi ubah nama file jadi 02_preprocess_data.py.`
- `Tolak bagian ini. Jangan tambah dependensi numba dulu; ukur dulu waktunya tanpa numba.`
- `Tambahkan tes: hasil harus identik untuk seed yang sama.`
- `Belum bisa saya putuskan. Siapkan perbandingan angka kedua opsi dan berhenti.`

Setelah Proceed: buka Walkthrough, **jalankan sendiri** perintah yang disebutnya, lihat angkanya, baru commit (`git commit`). Jangan percaya klaim "lolos" tanpa melihat output tes.

---

## 2. Struktur folder dan penamaan

```
ta-mccar-kma/
├── AGENTS.md                    aturan kerja agen
├── README.md
├── pyproject.toml
├── .gitignore
├── configs/
│   └── params.yaml              semua parameter (Tabel 3.1 dll.)
├── data/
│   ├── raw/                     READ-ONLY: dataset asli
│   ├── interim/                 hasil antara
│   └── processed/               data bersih, parameter GBM, bank skenario, batas η/τ
├── docs/
│   ├── context/                 spesifikasi_model.md
│   ├── proposal/                READ-ONLY
│   ├── references/              READ-ONLY: core, debt_management, risk_measures,
│   │                            optimization, kma, prior_theses
│   ├── decisions/               0001-..., 0002-... (keputusan yang Anda setujui)
│   └── reviews/                 laporan review/audit
├── report/                      proposal_latex/ dan skripsi_latex/ (template ITS)
├── legacy/                      READ-ONLY: kode dan data versi lama (execution_v0, data_v0)
├── src/mccar_kma/
│   ├── data/                    loader, cleaning, interpolation
│   ├── scenarios/               estimation, gbm, cost
│   ├── risk/                    ccar, mccar, evaluator
│   ├── model/                   constraints, penalty, limits
│   ├── optimizers/              base, kma, ga, pso
│   ├── experiments/             runner, seeds, io
│   ├── analysis/                summary, stats_tests, validation
│   ├── viz/                     style, figures
│   └── utils/                   config, logging
├── scripts/                     01_audit_data.py ... 14_make_figures_tables.py
├── tests/                       test_<modul>.py
├── notebooks/                   eksplorasi saja
├── results/
│   ├── runs/<config_id>/<algo>/ satu JSON per replikasi
│   ├── tables/                  tab_*.csv / .tex / ringkasan .md
│   └── figures/                 fig_*.pdf / fig_*.png
└── logs/
```

Prinsip yang membuatnya mudah dikelola:

| Pertanyaan Anda | Jawabannya ada di |
|---|---|
| Rumus ini ada di kode mana? | `src/mccar_kma/` — tiap modul = satu konsep (`ccar.py`, `kma.py`), docstring menyebut nomor persamaan |
| Skrip mana dijalankan dulu? | `scripts/` — **nomor skrip = nomor tahap** di panduan ini |
| Angka ini dari mana? | `configs/params.yaml` untuk parameter; `docs/decisions/` untuk alasannya |
| Hasil eksperimen mana? | `results/runs/<config_id>/<algo>/rep_<kk>_seed<seed>.json` |
| Tabel/gambar untuk skripsi? | `results/tables/tab_*`, `results/figures/fig_*` |

Aturan penamaan:

- Folder dan file: huruf kecil, `snake_case`, tanpa spasi.
- `config_id` = `<biaya>_<batas>`: `gross_free`, `gross_djppr`, `interest_free`, `interest_djppr`. `algo`: `kma`, `ga`, `pso`.
- Tanggal ISO `YYYY-MM-DD`. Data olahan menyebut jendela dan varian: `market_2017-07-03_2025-11-24_intersection.csv`.
- Commit: `<jenis>(tahap-NN): ringkasan`, jenis = `feat`, `fix`, `test`, `docs`, `data`, `exp`, `chore`. Contoh: `feat(tahap-05): evaluator CCaR dan MCCaR`.
- Aturan lengkap ada di `AGENTS.md`, jadi agen ikut mematuhinya.

---

## 3. Peta model per tahap

Pembagian ini penilaian saya: model terkuat untuk tahap yang kesalahannya mahal dan sulit terlihat (inti matematis, KMA), model menengah untuk implementasi yang rumusnya sudah jelas, Flash untuk pekerjaan prosedural. Nama model mengikuti daftar yang Anda berikan; sesuaikan bila dropdown Anda berbeda.

| Tahap | Pekerjaan | Model | Alasan |
|---|---|---|---|
| 0 | Kerangka proyek | Gemini 3.8 Flash (Low) | Murni prosedural |
| 1 | Audit data | Gemini 3.8 Flash (High) | Pemeriksaan deterministik, banyak item |
| 2 | Pra-pemrosesan + spline | Claude Sonnet 4.6 (Thinking) | Ada keputusan data (D1) dan spline buatan sendiri |
| 3 | Estimasi parameter GBM | Claude Sonnet 4.6 (Thinking) | Keputusan kalibrasi μ/σ (D2) |
| 4 | Bank skenario | Claude Sonnet 4.6 (Thinking) | Simulasi berkorelasi, banyak cek statistik |
| 5 | Inti risiko: CCaR, MCCaR, J, penalti | **Claude Opus 4.6 (Thinking)** | Jantung skripsi; kesalahan kecil merusak semua hasil |
| 6 | Batas η/τ + baseline DJPPR | Claude Sonnet 4.6 (Thinking) | Memakai evaluator yang sudah diuji |
| 7 | KMA dua fase | **Claude Opus 4.6 (Thinking)** | Algoritma rumit, banyak detail tidak ditentukan |
| 8 | GA dan PSO | Claude Sonnet 4.6 (Thinking) | Algoritma baku, rumus jelas |
| 9 | Review independen | GPT-OSS 120B (Medium) | Keluarga model berbeda → kesalahan tidak ikut berkorelasi. Dipakai hanya untuk membaca/menilai, bukan menulis kode inti |
| 10 | Pelari eksperimen | Gemini 3.8 Flash (High) | Rekayasa prosedural (paralel, resume, CLI) |
| 11 | Pilot lalu eksperimen penuh | Gemini 3.8 Flash (Medium) | Menjalankan dan memantau |
| 12 | Validasi independen | Claude Sonnet 4.6 (Thinking) | Perbandingan dan interpretasi angka |
| 13 | Uji statistik | Claude Sonnet 4.6 (Thinking) | Implementasi Dunn/ε² dan cek silang |
| 14 | Gambar dan tabel | Gemini 3.8 Flash (Medium) | Plotting dari file hasil |
| 15a | Paket reproduksibilitas | Gemini 3.8 Flash (Medium) | Dokumentasi dan skrip |
| 15b | Audit akhir | **Claude Opus 4.6 (Thinking)** | Menilai konsistensi seluruh proyek vs proposal |

Jika kuota Opus terbatas, prioritaskan Opus untuk tahap 5 dan 7; tahap 15b bisa diganti Sonnet.

---

## 4. Prompt per tahap

Semua prompt diawali `/plan` kecuali tahap 9 dan 15b. Tempel isi di dalam kotak apa adanya. Setiap tahap punya **Cek di plan** (apa yang perlu Anda perhatikan sebelum Proceed).

### Fase A — Fondasi

#### Tahap 0 — Kerangka proyek

Model: **Gemini 3.8 Flash (Low)** · Mode: Planning

Sebelum prompt, pastikan Anda sudah unzip starter dan membuka foldernya (bagian 1). Jalankan `git --version` di terminal; jika belum ada, pasang Git dulu.

```
/plan
## Konteks
Ini proyek skripsi saya. Baca AGENTS.md dan docs/context/spesifikasi_model.md sampai habis sebelum membuat rencana.

## Tugas
Siapkan kerangka proyek Python yang rapi dan bisa dijalankan, tanpa logika model sama sekali.
1. Buat folder dan file kosong yang BELUM ada sesuai bagian "Struktur folder" di AGENTS.md (src-layout, paket mccar_kma, setiap subpaket punya __init__.py). Folder data/raw, docs/, report/, dan legacy/ sudah terisi: jangan diubah.
2. pyproject.toml (paket editable, Python 3.11+, hanya dependensi yang diizinkan di AGENTS.md).
3. Buat virtual environment .venv, install editable, jalankan pytest.
4. .gitignore yang sesuai (.venv, __pycache__, results/runs/, logs/, file .npz besar) dan README.md singkat (tujuan, cara setup, urutan skrip; diisi bertahap).
5. configs/params.yaml berisi semua parameter dari spesifikasi §6, §7, §8 (Tabel 3.1) dengan komentar sumbernya. Parameter yang belum ditentukan diisi null dengan komentar "KEPUTUSAN TERBUKA Dx".
6. tests/test_smoke.py yang mengimpor paket.
7. git init lalu commit awal "chore(tahap-00): kerangka proyek".

## Batasan
Jangan membuat logika model. Jangan menyentuh data/raw, docs/, report/, dan legacy/. Jangan mengimpor apa pun dari legacy/. Jangan memasang paket di luar daftar izin.

## Selesai bila
pytest hijau, `python -c "import mccar_kma"` berhasil, pohon folder cocok dengan AGENTS.md.

Berhenti di Implementation Plan. Jangan kerjakan apa pun sebelum saya Proceed.
```

**Cek di plan:** versi Python yang dipakai; apakah agen mengusulkan numba (tolak dulu, putuskan setelah tahap 5 mengukur waktu); folder `data/raw` tidak disentuh.

#### Tahap 1 — Audit data

Model: **Gemini 3.8 Flash (High)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md dan spesifikasi §2 (Data). File: data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx.

## Tugas
Buat skrip audit read-only: scripts/01_audit_data.py (logika di src/mccar_kma/data/loader.py). Laporkan dengan angka:
- sheet, kolom, tipe data; penanda hilang ('#N/A N/A', '#N/A') dibaca sebagai NaN
- rentang tanggal, jumlah baris, duplikat tanggal, urutan tanggal, hari akhir pekan
- jendela analisis (mulai saat semua 9 seri ada; JPY_5Y baru mulai 3 Jul 2017) dan jumlah barisnya
- semua blok data hilang per kolom (tanggal awal, akhir, panjang)
- nilai <= 0 pada yield dan kurs (penting untuk log-return dan GBM)
- lonjakan harian ekstrem (|Δln| > 5 simpangan baku): tampilkan daftar, jangan hapus
- apakah sheet 'Data IR' dan 'Data IR_formula' identik
- sheet 'Data Awal': bobot eksisting berjumlah 1, min <= eksisting <= max, jumlah min <= 1 <= jumlah max
- sebaran kolom Kategori (Sebelum Covid / Covid / Setelah Covid) di jendela analisis
- arah kurs: FX_USD/EUR dan FX_USD/JPY = unit mata uang per 1 USD
- bandingkan irisan lengkap (9 seri) dengan legacy/data_v0/ir_data_clean.csv dan fx_data_clean.csv: jumlah baris, tanggal, dan nilai harus sama (hanya baca, jangan diubah)

## Output
results/tables/audit_data.md (ringkas, bisa ditempel ke laporan) dan results/tables/audit_data_gaps.csv.
Bandingkan dengan angka di spesifikasi §2 dan tandai setiap selisih.

## Batasan
Jangan mengubah, mengisi, atau menghapus data apa pun. Tidak ada interpolasi di tahap ini.

## Selesai bila
Skrip jalan dari nol, laporan terbit, dan setiap angka di spesifikasi §2 terkonfirmasi atau selisihnya ditandai.

Berhenti di Implementation Plan.
```

**Cek di plan:** tidak ada langkah yang menulis ke `data/raw`; semua poin audit tercakup. Hasil yang diharapkan: 3.104 baris, jendela 2.191 baris, blok hilang 163 hari di EUR_10Y. Selisih apa pun = berita penting, tulis di `docs/decisions/`.

### Fase B — Data dan skenario

#### Tahap 2 — Pra-pemrosesan dan interpolasi

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

Di sini ada keputusan D1 (2.028 vs 2.191 baris). Proposal menyebut dua-duanya; plan harus menyajikan perbandingan, dan Anda memutuskan bersama pembimbing.

```
/plan
## Konteks
Baca AGENTS.md, spesifikasi §2, §4, §12 (D1), dan results/tables/audit_data.md.

## Tugas
Bangun pipeline pra-pemrosesan: scripts/02_preprocess_data.py + src/mccar_kma/data/cleaning.py + interpolation.py.
1. Muat data, ubah penanda hilang jadi NaN, potong ke jendela analisis.
2. Implementasikan natural cubic spline SENDIRI sesuai Persamaan 2.4–2.6 (sistem tridiagonal, c_1 = c_M = 0). Uji terhadap scipy.interpolate.CubicSpline(bc_type='natural'): selisih maksimum harus < 1e-8.
3. Hasilkan DUA varian dataset:
   - intersection: hanya baris dengan 9 seri lengkap (2.028 baris)
   - spline: EUR_10Y yang hilang diisi spline (2.191 baris)
   Sertakan perbandingan: jumlah baris, rata-rata dan simpangan baku log-change EUR_10Y, dan korelasi EUR_10Y dengan seri lain, per varian.
4. Pilihan varian dikendalikan configs/params.yaml → data.window_mode. Jangan memutuskan sendiri: tulis di plan sebagai KEPUTUSAN DIBUTUHKAN lengkap dengan rekomendasi dan risikonya (blok hilang adalah 163 hari berurutan, bukan celah hari libur).

## Output
data/processed/market_2017-07-03_2025-11-24_intersection.csv dan ..._spline.csv, results/tables/preprocess_comparison.md, tests/test_interpolation.py.
Tambahkan cek: varian intersection harus identik dengan legacy/data_v0/ir_data_clean.csv dan fx_data_clean.csv (hanya baca).

## Batasan
data/raw tidak boleh berubah. Pada varian intersection, log-change yang melintasi blok 163 hari harus dikeluarkan (jangan dihitung sebagai satu perubahan harian).

## Selesai bila
Tes spline lolos, kedua varian terbit dengan jumlah baris tepat, tidak ada NaN tersisa, tabel perbandingan siap saya baca.

Berhenti di Implementation Plan.
```

**Cek di plan:** agen tidak memilih varian sendiri; log-change yang melintasi blok dikeluarkan. Setelah memutuskan, isi `data.window_mode` dan minta agen mencatatnya di `docs/decisions/0002-jendela-data.md`.

#### Tahap 3 — Estimasi parameter GBM

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md, spesifikasi §3, §4, §11, dan keputusan D1/D2 (§12). Pakai varian data yang sudah saya tetapkan di configs/params.yaml (data.window_mode).

## Tugas
Bangun estimasi parameter GBM: scripts/03_estimate_gbm_params.py + src/mccar_kma/scenarios/estimation.py.
1. Hitung log-change harian 9 variabel pasar (7 yield + 2 kurs).
2. Estimasi per variabel: rata-rata dan simpangan baku harian; anualisasi 252 hari: σ = s·√252, μ = 252·m + σ²/2. Jelaskan di plan; ini KEPUTUSAN DIBUTUHKAN (D2).
3. Matriks korelasi 9×9: periksa simetris, diagonal 1, positif definit (Cholesky berhasil).
4. Laporkan juga statistik biaya historis Persamaan 2.7–2.10 (Δc, rata-rata, varians, kovarians) sebagai tabel deskriptif. Definisi C_{i,t} historis (X_0 yang dipakai) = KEPUTUSAN DIBUTUHKAN (D2).
5. Jangan menaruh hasil estimasi di dalam kode; simpan ke data/processed/gbm_params_<varian>.csv dan corr_<varian>.csv.

## Verifikasi
Uji estimator pada deret sintetis dengan μ, σ, ρ yang diketahui. Tampilkan tabel μ dan σ dalam %/tahun dan bandingkan arahnya dengan spesifikasi §11 (drift biaya JPY negatif, USD dan EUR dekat nol).

## Selesai bila
Parameter tersimpan, uji sintetis lolos, tabel μ/σ/korelasi tersaji.

Berhenti di Implementation Plan.
```

**Cek di plan:** kalibrasi μ dijelaskan dan Anda setujui; drift yang dipakai tidak dipotong atau diubah diam-diam.

#### Tahap 4 — Bank skenario GBM

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md, spesifikasi §3 dan §4. Parameter dari data/processed/gbm_params_*.csv.

## Tugas
Bangun pembangkit skenario: src/mccar_kma/scenarios/gbm.py, cost.py, dan scripts/04_generate_scenarios.py.
1. Bangkitkan N = 5.000 skenario horizon 1 tahun (252 hari) untuk 9 variabel dengan guncangan normal berkorelasi (Cholesky), S_0 = observasi terakhir jendela. Keputusan terbuka: simulasi langsung nilai terminal vs jalur 252 langkah (distribusi terminal sama); jelaskan dan sarankan satu.
2. Hitung faktor konversi q (Persamaan 2.1), biaya bruto C_{i,s} (2.2), dan biaya bunga (2.3) untuk 7 instrumen × 5.000 skenario.
3. Simpan SATU bank skenario (seed tercatat) yang dipakai semua algoritma: data/processed/bank_train_seed<seed>_N5000.npz + metadata JSON (seed, N, varian data, tanggal, hash konfigurasi).
4. Bangkitkan juga bank validasi independen (seed berbeda, N lebih besar, usulkan N di plan / D3) dengan fungsi yang sama: bank_valid_....

## Verifikasi (tampilkan angkanya)
Rata-rata dan simpangan baku log-return simulasi vs parameter; korelasi sampel vs target; semua nilai > 0; tidak ada NaN; seed sama → hasil identik, seed beda → hasil berbeda; arah q benar (kurs EUR naik → q turun → biaya USD-ekuivalen turun).

## Selesai bila
Kedua bank terbit dan semua cek di atas lolos dan dilaporkan.

Berhenti di Implementation Plan.
```

**Cek di plan:** satu bank latih saja untuk semua algoritma (adil); seed dicatat; bank validasi terpisah.

### Fase C — Inti model

#### Tahap 5 — Evaluator risiko dan kendala (inti skripsi)

Model: **Claude Opus 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Ini inti matematis skripsi saya. Baca AGENTS.md dan spesifikasi §5, §6, §10, §11 dengan teliti. Setiap fungsi wajib menyebut nomor persamaan proposal.

## Tugas
Implementasikan evaluator risiko dan model kendala:
- src/mccar_kma/risk/ccar.py: CCaR (2.13), rata-rata m = ceil((1−α)N) biaya tertinggi, dengan np.partition.
- src/mccar_kma/risk/mccar.py: MC_i (2.16), MCCaR_i (2.17), θ_i (2.18), θ̄ (2.19), J_MCCaR (2.20). Himpunan ekor dipilih ULANG pada biaya yang sudah ditambah δ·C_{s,i} (2.14). Tangani MC_i ≈ 0 secara eksplisit (D5).
- src/mccar_kma/risk/evaluator.py: kelas PortfolioEvaluator(bank, cost_def, alpha, delta) yang menghitung Cost̄, CCaR, MC, MCCaR, θ, J untuk satu bobot, plus versi batch untuk populasi (P×7).
- src/mccar_kma/model/constraints.py dan penalty.py: proyeksi bobot (clip ke [lb,ub], normalisasi jumlah 1, ulangi sampai dalam toleransi 1e-8), pelanggaran relatif v_J dan v_R (2.23), fungsi kualitas f(w) (2.24) dengan ρ_J = ρ_R = 1e6, dan arsip solusi layak terbaik.
- Penghitung evaluasi fungsi (budget counter) yang nanti dipakai semua algoritma.

## Kinerja
Satu evaluasi (bobot → f(w)) akan dipanggil ± 9 juta kali. Ukur ms/evaluasi pada N = 5.000 dan perkirakan total waktu eksperimen penuh (4 konfigurasi × 3 algoritma × 30 replikasi × 25.000 evaluasi). Usulkan optimisasi di plan (vektorisasi, np.partition; numba hanya bila perlu dan saya setujui).

## Tes wajib (tests/test_risk.py, tests/test_constraints.py)
1. Kasus sintetis kecil yang bisa dihitung tangan (mis. N=20, α=0,90, 2–3 instrumen): CCaR, MCCaR, θ, J cocok dengan hitungan tangan yang ditulis di dalam tes.
2. Sifat analitik: MC_i = δ·rata-rata(C_i) persis; CCaR >= biaya rata-rata; CCaR^(+i) >= CCaR.
3. Proyeksi: hasil selalu Σw=1 dan lb <= w <= ub dalam 1e-8, untuk skenario batas free dan djppr, dari 10.000 titik acak.
4. Versi batch identik dengan versi satu-per-satu.

## Batasan
Jangan implementasikan algoritma optimasi di tahap ini. Jangan mengubah arti formula; ambiguitas = KEPUTUSAN DIBUTUHKAN.

## Selesai bila
Semua tes lolos; benchmark waktu dan estimasi total waktu eksperimen tersaji.

Berhenti di Implementation Plan.
```

**Cek di plan:** ekor dipilih ulang untuk CCaR^(+i) (bukan memakai ekor lama); J memakai pembagi n; ceil untuk m; hasil akhir diambil dari arsip layak. Ini tahap yang paling layak Anda baca pelan-pelan; jika perlu bawa plan-nya ke pembimbing.

#### Tahap 6 — Batas η/τ, baseline DJPPR, pembanding kasar

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md, spesifikasi §6, §8, §11, §12 (D8). Evaluator dari tahap 5 sudah ada. Jurnal acuan DJPPR ada di docs/references/core/ (baca versi .md; jika tidak cukup, katakan dan nanti saya tempelkan bagian prosedurnya).

## Tugas
scripts/06_compute_limits_and_baseline.py + src/mccar_kma/model/limits.py:
1. Hitung η dan τ dari komposisi eksisting 2024 (Persamaan 2.22) pada bank latih, untuk DUA definisi biaya (bruto dan bunga) → data/processed/risk_limits_<bank>.json. Pasangan batas ditetapkan sekali dan tidak berubah setelah melihat hasil optimasi.
2. Replikasi acuan historis DJPPR: 1.000 kombinasi bobot acak di dalam batas proporsi (skenario djppr), hitung Cost̄, CCaR, J tiap kombinasi, tandai yang lolos J <= η dan CCaR <= τ. Simpan lengkap ke results/tables/baseline_djppr_<costdef>.csv.
3. Cek kelayakan ruang solusi: eksisting memenuhi kendalanya sendiri (v = 0). Tambahkan satu solusi referensi independen dengan scipy.optimize (SLSQP dari beberapa titik awal) sebagai pembanding kasar. Ini BUKAN hasil utama skripsi, hanya pemeriksaan bahwa KMA/GA/PSO nanti tidak jauh berbeda.

## Verifikasi
Tampilkan η dan τ untuk kedua definisi biaya, persentase kombinasi acak yang layak, dan biaya terbaik referensi SLSQP vs eksisting.

## Selesai bila
File batas dan baseline terbit dan angkanya masuk akal (eksisting layak; biaya referensi <= biaya eksisting).

Berhenti di Implementation Plan.
```

**Cek di plan:** cara membangkitkan 1.000 acak mengikuti jurnal (D8); η, τ dihitung sekali dan dikunci.

### Fase D — Algoritma

#### Tahap 7 — KMA

Model: **Claude Opus 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md, spesifikasi §7.1 dan §12 (D4, D6). Evaluator, proyeksi, penalti, arsip, dan penghitung evaluasi dari tahap 5 sudah ada dan DIPAKAI ULANG; jangan menulis ulang. legacy/execution_v0/kma_algorithm.py adalah versi lama satu fase: boleh dibaca sebagai bahan perbandingan, tetapi implementasi baru mengikuti spesifikasi dan tidak mengimpor dari legacy/.

## Tugas
1. src/mccar_kma/optimizers/base.py: antarmuka bersama (kelas dasar Optimizer: run(evaluator, bounds, budget, rng) → hasil) yang memuat penghitung evaluasi, arsip solusi layak terbaik, dan log konvergensi (biaya layak terbaik tiap 250 evaluasi). GA dan PSO nanti memakai antarmuka yang persis sama.
2. src/mccar_kma/optimizers/kma.py: Komodo Mlipir Algorithm dua fase sesuai Algoritma 1 dan Persamaan 2.25–2.32:
   - Fase 1: n_pop = 5, d = (D−1)/D, anggaran 5.000 evaluasi.
   - Fase 2: n_pop awal 200, batas 20 <= n_pop <= 200, langkah Δn adaptif (membesar saat stagnan, mengecil saat membaik); sisa anggaran 20.000 evaluasi.
   - Big males (tarik/tolak, 2.26–2.27), female (kawin 2.28–2.29 atau partenogenesis 2.30), small males (mlipir 2.31–2.32).
3. Beberapa detail TIDAK ditentukan proposal: p_bm, γ, jumlah big male yang berinteraksi (q), aturan memilih kawin vs partenogenesis, definisi stagnasi, besar Δn, serah-terima fase 1 → 2. Untuk tiap detail tulis KEPUTUSAN DIBUTUHKAN dengan nilai usulan dan rujukannya (Suyanto dkk., 2022); nilai final disimpan di configs/params.yaml.

## Tes (tests/test_kma.py)
- Anggaran evaluasi tidak pernah terlampaui (tepat 25.000 pada jalan penuh).
- Reproduksibel: seed sama → hasil identik.
- Setiap solusi yang dikembalikan lolos Σw=1 dan batas proporsi (1e-8).
- Masalah uji kecil dengan optimum diketahui (objektif linear di dalam batas, jawaban bisa dihitung tangan): KMA mendekati optimum dalam toleransi yang diusulkan.
- Smoke test 3 replikasi pada evaluator sungguhan (bank latih, config gross_djppr): laporkan biaya, kelayakan, waktu.

## Batasan
Jangan menyentuh GA/PSO. Jangan mengubah evaluator.

## Selesai bila
Semua tes lolos dan hasil smoke test tersaji.

Berhenti di Implementation Plan.
```

**Cek di plan:** tiap KEPUTUSAN DIBUTUHKAN punya nilai usulan + rujukan; nilai yang Anda setujui dicatat di `docs/decisions/`. Pembimbing sebaiknya melihat daftar D4 karena ini bagian orisinal skripsi.

#### Tahap 8 — GA dan PSO

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md dan spesifikasi §7.2–7.3, §12 (D6). Pakai antarmuka Optimizer di optimizers/base.py yang sudah ada.

## Tugas
Implementasikan optimizers/ga.py dan optimizers/pso.py persis sesuai Tabel 3.1:
- GA: n_pop 50, seleksi turnamen ukuran 2, persilangan aritmetika (2.33–2.34) peluang 0,9, mutasi Gaussian peluang 1/D per dimensi dengan σ_m = 0,1 × lebar rentang.
- PSO: n_pop 50, inersia turun linear 0,9 → 0,4, c1 = c2 = 1,49618, v_max,i = 0,2 (ub_i − lb_i), pembaruan (2.35–2.36).
- Keduanya memakai proyeksi, penalti, arsip, penghitung evaluasi, dan anggaran 25.000 evaluasi yang SAMA dengan KMA.
Hal yang tidak ditentukan (elitisme GA, inisialisasi populasi, perlakuan kecepatan saat bobot dipotong proyeksi, jadwal inersia terhadap jumlah evaluasi) → KEPUTUSAN DIBUTUHKAN dengan rekomendasi. Inisialisasi populasi harus sama untuk ketiga algoritma (cek juga KMA) agar perbandingan adil.

## Tes
Sama dengan tes KMA (anggaran, reproduksibilitas, kelayakan, masalah uji berjawaban diketahui) + smoke test 3 replikasi per algoritma pada config yang sama dengan KMA; tampilkan tabel perbandingan awal (biaya layak terbaik, waktu).

## Batasan
Jangan mengubah base.py, KMA, atau evaluator. Jika perlu perubahan di sana, berhenti dan tanyakan.

## Selesai bila
Tes lolos dan ketiga algoritma bisa dipanggil lewat antarmuka yang sama.

Berhenti di Implementation Plan.
```

**Cek di plan:** tidak ada perubahan ke file tahap sebelumnya; inisialisasi sama untuk ketiganya.

#### Tahap 9 — Review independen (read-only)

Model: **GPT-OSS 120B (Medium)** · Mode: **Fast**, tanpa `/plan` (tidak mengubah kode)

Tujuannya mencari bug yang lolos dari model yang menulis kodenya. Model dari keluarga lain cenderung tidak mengulangi kesalahan yang sama. Perlakukan temuannya sebagai dugaan yang harus dibuktikan, bukan kebenaran.

```
## Peran
Kamu auditor independen. Kamu TIDAK menulis atau mengubah kode. Satu-satunya file yang boleh kamu buat: docs/reviews/review_tahap05-08_<YYYY-MM-DD>.md.

## Tugas
Bandingkan implementasi di src/mccar_kma/ (risk/, model/, optimizers/, scenarios/) dengan docs/context/spesifikasi_model.md, baris per baris, untuk:
1. Setiap persamaan 2.1–2.36 yang diimplementasikan: rumus, indeks, tanda, pembulatan (ceil/floor), pembagi (N−1 vs N) sudah benar?
2. Kebocoran kelayakan: apakah solusi akhir yang dilaporkan benar-benar dari arsip layak, bukan sekadar nilai f terendah?
3. Keadilan perbandingan: apakah KMA, GA, PSO memakai bank, anggaran, proyeksi, penalti, dan inisialisasi yang sama?
4. Penghitung anggaran: adakah jalur evaluasi yang tidak terhitung atau terhitung ganda?
5. RNG: adakah penggunaan RNG global yang membuat hasil tidak reproduksibel?
6. Tes yang ada: apakah benar menguji sifatnya, atau lolos kebetulan?

## Format laporan
Tabel temuan: ID, severity (kritis/penting/minor), file:baris, apa yang salah, bukti (kutip rumus dan potongan kode), saran perbaikan. Akhiri dengan daftar singkat "yang sudah benar".
```

Setelah laporan terbit, bawa temuan yang masuk akal ke model penulis kode (Sonnet/Opus) dengan **template perbaikan** di bagian 5.

### Fase E — Eksperimen

#### Tahap 10 — Pelari eksperimen

Model: **Gemini 3.8 Flash (High)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md dan spesifikasi §8. Tiga optimizer, evaluator, bank latih, dan batas η/τ sudah ada.

## Tugas
Bangun pelari eksperimen: src/mccar_kma/experiments/{runner,seeds,io}.py + scripts/10_run_experiments.py.
1. Matriks: 4 konfigurasi (gross_free, gross_djppr, interest_free, interest_djppr) × 3 algoritma (kma, ga, pso) × 30 replikasi = 360 run; 25.000 evaluasi per run.
2. Daftar seed replikasi sama untuk ketiga algoritma (seed_k = base_seed + k; base_seed di params.yaml).
3. Tiap run menyimpan satu JSON di results/runs/<config_id>/<algo>/rep_<kk>_seed<seed>.json: bobot terbaik layak, Cost̄, CCaR, J, θ_i, status layak, jumlah evaluasi, waktu (detik), kurva konvergensi, hash konfigurasi.
4. Paralel dengan multiprocessing (worker = jumlah core − 1, bisa diatur), RESUME (lewati run yang sudah ada), progress bar, log ke logs/.
5. Opsi CLI: --pilot (2 replikasi, 2.000 evaluasi), --config, --algo, --dry-run (hanya daftar run), --workers.
6. Agregator: results/tables/runs_summary.csv (satu baris per run).

## Tes
Dry-run menampilkan 360 run; pilot kecil menghasilkan JSON valid; menjalankan ulang pilot tidak mengulang run (resume bekerja); hasil identik untuk seed yang sama walau jumlah worker berbeda.

## Batasan
Jangan menjalankan eksperimen penuh. Hanya pilot kecil untuk tes.

## Selesai bila
Tes lolos dan estimasi waktu eksperimen penuh (dari pilot) tertulis.

Berhenti di Implementation Plan.
```

#### Tahap 11 — Pilot, lalu eksperimen penuh

Model: **Gemini 3.8 Flash (Medium)** · Mode: Planning

Dua prompt terpisah. Kirim yang kedua hanya setelah Anda membaca laporan pilot. Untuk run panjang, jaga komputer tetap menyala dan terhubung daya.

Prompt 11a — pilot:

```
/plan
## Tugas
Jalankan pilot dari scripts/10_run_experiments.py, lalu 1 replikasi penuh (25.000 evaluasi) untuk tiap algoritma di config gross_djppr. Laporkan: waktu per run, jumlah evaluasi, kelayakan, biaya terbaik, kurva konvergensi (gambar cepat), dan estimasi total waktu 360 run dengan jumlah worker di komputer ini.

## Batasan
Berhenti setelah laporan. Jangan menjalankan eksperimen penuh.
```

Prompt 11b — eksperimen penuh (setelah pilot Anda setujui):

```
/plan
Pilot sudah saya setujui. Jalankan eksperimen penuh (360 run) di latar belakang dengan resume aktif dan log ke logs/. Pantau progres tiap beberapa menit; bila ada run gagal, catat dan ulangi hanya run itu. Setelah selesai, laporkan: jumlah run per konfigurasi dan algoritma (harus tepat 30), tidak ada JSON rusak, dan semua solusi layak pada toleransi 1e-8 (sebutkan yang tidak). Perbarui results/tables/runs_summary.csv.
```

**Cek di plan:** jumlah worker wajar untuk laptop Anda; perintah dijalankan di latar belakang dan dapat dilanjutkan jika terputus.

### Fase F — Validasi, analisis, dan keluaran

#### Tahap 12 — Validasi independen dan pembanding

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md dan spesifikasi §10. Eksperimen penuh selesai (results/runs/).

## Tugas
scripts/12_validate_solutions.py + src/mccar_kma/analysis/validation.py:
1. Evaluasi ulang setiap solusi terbaik (360) pada bank validasi independen: hitung Cost̄, CCaR, J, dan apakah J <= η dan CCaR <= τ (batas dari bank latih, tidak diubah).
2. Periksa ulang kendala bobot semua solusi: Σw=1 dan batas proporsi dalam 1e-8.
3. Bandingkan per konfigurasi: eksisting 2024, baseline DJPPR (1.000 acak yang layak), dan solusi terbaik tiap algoritma: biaya, CCaR, J, komposisi, penghematan relatif terhadap eksisting dan baseline.
4. Tingkat kelayakan di bank validasi per algoritma. Pelanggaran kecil di bank validasi adalah temuan yang dilaporkan, bukan bug.

## Output
results/tables/validation_<config_id>.csv dan ringkasan results/tables/validation_summary.md.

## Selesai bila
Semua 360 solusi terevaluasi, ringkasan terbit, dan temuan tak terduga ditandai jelas.

Berhenti di Implementation Plan.
```

#### Tahap 13 — Analisis statistik

Model: **Claude Sonnet 4.6 (Thinking)** · Mode: Planning

```
/plan
## Konteks
Baca AGENTS.md dan spesifikasi §9, §12 (D7).

## Tugas
scripts/13_analyze_stats.py + src/mccar_kma/analysis/summary.py dan stats_tests.py. Pada nilai objektif solusi layak terbaik tiap replikasi, per konfigurasi:
1. Ringkasan per algoritma: terbaik, median, rata-rata, simpangan baku, IQR; waktu komputasi; jumlah evaluasi menuju konvergensi.
2. Asumsi: Shapiro–Wilk per kelompok dan Levene antarkelompok.
3. Kruskal–Wallis (2.37), Dunn (2.38) dengan koreksi Holm, ε² (2.39), dan korelasi rank-biserial tiap pasangan.
4. Tulis sendiri Dunn dan ε² sesuai persamaan; cek silang H terhadap scipy.stats.kruskal. Penanganan ties pada Dunn = KEPUTUSAN DIBUTUHKAN (D7).
5. Keluaran: results/tables/stats_<config_id>.csv dan tab_stats_<config_id>.tex.

## Tes
Data sintetis yang jawabannya diketahui; H sama dengan scipy.stats.kruskal.

## Selesai bila
Tabel statistik terbit untuk keempat konfigurasi dan tes lolos.

Berhenti di Implementation Plan.
```

#### Tahap 14 — Gambar dan tabel skripsi

Model: **Gemini 3.8 Flash (Medium)** · Mode: Planning

```
/plan
## Tugas
Bangun src/mccar_kma/viz/{style,figures}.py + scripts/14_make_figures_tables.py.
Gambar (PDF vektor + PNG 300 dpi, label Bahasa Indonesia, font serif, warna konsisten untuk KMA/GA/PSO/eksisting/DJPPR, tetap terbaca bila dicetak hitam-putih):
1. Kurva konvergensi (median + pita IQR 30 replikasi) per konfigurasi
2. Boxplot nilai objektif per algoritma per konfigurasi
3. Komposisi portofolio: eksisting vs DJPPR vs tiap algoritma (batang bertumpuk 7 instrumen)
4. Rasio θ_i per instrumen untuk eksisting dan solusi terbaik
5. Waktu komputasi per algoritma
6. Deret waktu yield dan kurs pada jendela analisis
Tabel LaTeX (booktabs): parameter eksperimen, statistik deskriptif data, batas η/τ, ringkasan hasil, uji statistik.
Nama: fig_<topik>_<config_id>.pdf dan tab_<topik>.tex di results/figures dan results/tables. Tidak ada angka yang diketik tangan; semua dibaca dari file hasil.

## Selesai bila
Skrip menghasilkan semua gambar dan tabel dari nol dan setiap file bisa dibuka.

Berhenti di Implementation Plan.
```

#### Tahap 15a — Paket reproduksibilitas

Model: **Gemini 3.8 Flash (Medium)** · Mode: Planning

```
/plan
## Tugas
Buat paket reproduksibilitas:
1. README.md lengkap: setup, urutan skrip 01 → 14 beserta perkiraan waktu tiap tahap.
2. scripts/run_all.sh dan scripts/run_all.ps1 (Windows) dengan opsi --pilot.
3. requirements.lock (versi persis paket terpasang).
4. docs/decisions/: pastikan semua keputusan terbuka (D1 dst.) tercatat beserta tanggal dan alasannya; tandai yang belum diputuskan.
5. results/MANIFEST.md: daftar file hasil + SHA-256 + konfigurasi + seed.

## Tes
Salin proyek ke folder bersih → setup dari README → run_all --pilot sukses.

Berhenti di Implementation Plan.
```

#### Tahap 15b — Audit akhir

Model: **Claude Opus 4.6 (Thinking)** · Mode: **Fast** (read-only), tanpa `/plan`

```
## Peran
Auditor akhir. Kamu TIDAK mengubah kode, data, atau hasil. Satu-satunya file yang boleh kamu buat: docs/reviews/audit_akhir_<YYYY-MM-DD>.md.

## Tugas
Bandingkan seluruh proyek dengan proposal (docs/proposal/) dan spesifikasi:
1. Angka di proposal vs data dan hasil: jumlah hari data, parameter Tabel 3.1, definisi biaya, batas proporsi.
2. Setiap klaim di abstrak: apakah hasil eksperimen mendukung, melemahkan, atau tidak menguji? Laporkan apa adanya (hipotesis "KMA kompetitif atau lebih baik" bisa saja tidak terbukti).
3. Konsistensi definisi: konvensi kurs q, bruto vs bunga, pembagi N vs N−1, pembulatan m.
4. Risiko validitas: GBM tanpa mean reversion, ekstrapolasi drift satu tahun, bank skenario tunggal, batas η/τ dari portofolio eksisting.
5. Daftar revisi yang disarankan untuk proposal dan Bab 4–5, berurutan menurut pentingnya, dengan bukti (file dan angka).

## Format
Ringkasan 10 baris di awal, lalu tabel temuan (ID, severity, bukti, saran).
```

---

## 5. Template cadangan

### Memperbaiki temuan review atau bug

Model: model penulis kode tahap itu (Sonnet atau Opus) · `/plan`

```
/plan
Perbaiki temuan berikut dari docs/reviews/<nama_file>.md: #3, #5, #8. Abaikan #4 dan #6 (alasan: ...).
Untuk tiap temuan: pertama buktikan bahwa itu memang bug (jalankan tes atau tunjukkan angka). Jika tidak terbukti, jelaskan mengapa dan jangan ubah apa pun. Perbaiki hanya yang terbukti, dan tambahkan tes regresi untuk tiap perbaikan.
Jangan mengubah hal lain. Berhenti di Implementation Plan.
```

### Hasil terlihat janggal

```
/plan
Hasil ini terlihat janggal: <tempel angka/pesan> pada <config_id>/<algo>.
Jangan langsung mengubah kode. Susun rencana diagnosis: hipotesis penyebab berurutan dari yang paling mungkin, cek tercepat untuk tiap hipotesis, dan angka apa yang akan membuktikan atau menggugurkannya. Berhenti di Implementation Plan.
```

### Agen menyimpang dari aturan

Ketik di percakapan yang sama:

```
Berhenti. Kamu melakukan <hal yang menyimpang> yang bertentangan dengan AGENTS.md butir <n>. Kembali ke Implementation Plan, tandai hal itu sebagai KEPUTUSAN DIBUTUHKAN, dan jangan lanjut sebelum saya Proceed.
```

### Kebiasaan yang membantu

- Satu tahap selesai → `git commit` → baru mulai tahap berikutnya.
- Setiap keputusan yang Anda setujui dicatat di `docs/decisions/` (minta agen menulisnya di akhir tahap).
- Jangan menempel ulang rumus di prompt; edit `docs/context/spesifikasi_model.md` jika ada rumus yang berubah, agar semua tahap berikutnya ikut.
- Jika agen mengajukan dependensi atau perubahan parameter Tabel 3.1, tolak di komentar plan dan tanyakan alasannya.
