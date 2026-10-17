# AGENTS.md — Aturan Kerja Proyek

Proyek: skripsi S1 Matematika ITS — "Optimasi Portofolio Utang Negara Multivaluta dengan Pendekatan Model Marginal Conditional Cost at Risk (MCCaR) menggunakan Komodo Mlipir Algorithm (KMA)".
Pemilik: Sultan Bakri Baihaqi Mahat (NRP 5002221016). Pembimbing: Prof. Dr. Mohammad Isa Irawan, MT.

Sumber kebenaran model dan data: `docs/context/spesifikasi_model.md`.
Proposal asli: `docs/proposal/`. Jurnal acuan DJPPR: `docs/references/`.
Jika kode, proposal, dan spesifikasi berbeda, hentikan pekerjaan dan tanyakan. Jangan menebak.

`legacy/` berisi kode dan data versi sebelum revisi proposal (lihat `legacy/README.md`). Itu hanya referensi: jangan diimpor, diubah, atau dijadikan sumber kebenaran. Aturan agen lama (template "3-layer", self-anneal) tidak berlaku.

## Cara kerja (wajib)

1. Mulai setiap tugas dengan Implementation Plan, lalu BERHENTI dan tunggu saya menekan Proceed. Sebelum itu hanya boleh membaca file; jangan menulis, mengubah, atau menjalankan perintah yang mengubah file.
2. Setiap hal yang tidak ditentukan spesifikasi ditulis di plan sebagai **KEPUTUSAN DIBUTUHKAN**: 2–3 opsi, untung-ruginya, dan satu rekomendasi. Jangan memilih sendiri.
3. Plan harus memuat: daftar file yang akan dibuat/diubah, daftar KEPUTUSAN DIBUTUHKAN, cara verifikasi (tes apa, angka apa yang akan ditampilkan), dan hal yang sengaja tidak dikerjakan.
4. Kerjakan hanya cakupan tugas yang diminta. Temuan di luar cakupan dicatat di akhir Walkthrough, tidak dikerjakan.
5. Walkthrough akhir memuat: file yang dibuat/diubah, cara menjalankan, hasil verifikasi berupa output nyata, dan hal yang belum beres.
6. Jangan menyatakan "benar" atau "lolos" tanpa menjalankan tes dan menampilkan hasilnya.
7. Keputusan yang sudah saya setujui dicatat di `docs/decisions/NNNN-judul-singkat.md` (konteks, opsi, keputusan, tanggal).

## Bahasa dan gaya

- Penjelasan kepada saya: Bahasa Indonesia, ringkas, tanpa basa-basi.
- Nama variabel, fungsi, dan file: English `snake_case`.
- Docstring dan komentar: Bahasa Indonesia. Setiap fungsi matematis wajib menyebut nomor persamaan proposal (mis. "Persamaan 2.13").

## Data dan reproduksibilitas

- `data/raw/`, `docs/proposal/`, `docs/references/`, dan `legacy/` READ-ONLY: tidak boleh diubah, ditimpa, atau dihapus. `report/` hanya diubah bila saya minta.
- Data olahan ditulis ke `data/interim/` dan `data/processed/` hanya lewat skrip di `scripts/`.
- Tidak ada angka ajaib di kode. Semua parameter ada di `configs/params.yaml`.
- Semua keacakan memakai `numpy.random.Generator` dengan seed eksplisit; jangan memakai RNG global.
- Setiap keluaran hasil membawa metadata: tanggal, hash konfigurasi, seed, versi data.
- Skrip pipeline bernomor sesuai nomor tahap dan harus bisa dijalankan ulang dari nol dengan hasil identik.

## Standar kode

- Python 3.11+, src-layout, paket `mccar_kma`, type hints, `pathlib`.
- Dependensi yang diizinkan: numpy, pandas, scipy, openpyxl, pyyaml, matplotlib, pytest, tqdm. Dependensi lain (mis. numba) hanya dengan persetujuan saya di plan.
- Logika inti hanya di `src/`; notebook hanya untuk eksplorasi dan tidak boleh dipakai pipeline.
- Setiap modul inti punya tes di `tests/` (pytest). Tes harus menguji sifat matematis, bukan hanya "tidak error".
- Vektorisasi dengan numpy untuk perhitungan yang dipanggil jutaan kali.

## Larangan

- Mengubah parameter pada Tabel 3.1 proposal tanpa persetujuan saya.
- Mengubah arti rumus. Ambiguitas = KEPUTUSAN DIBUTUHKAN.
- Menghapus file di luar cakupan tugas, `git push`, atau menginstal paket di luar daftar izin.
- Menyembunyikan hasil buruk: jika hasil tidak layak atau mengecewakan, laporkan apa adanya.

## Struktur folder

```
ta-mccar-kma/
├── AGENTS.md
├── README.md
├── pyproject.toml
├── .gitignore
├── configs/
│   └── params.yaml                  # semua parameter (Tabel 3.1 dan lainnya)
├── data/
│   ├── raw/                         # READ-ONLY: Dataset_Utama_Optimum_Utang_Valas.xlsx
│   ├── interim/                     # hasil antara
│   └── processed/                   # data bersih, parameter GBM, bank skenario, batas risiko
├── docs/
│   ├── context/                     # spesifikasi_model.md
│   ├── proposal/                    # READ-ONLY
│   ├── references/                  # READ-ONLY: core, debt_management, risk_measures,
│   │                                #   optimization, kma, prior_theses (nama: penulis_tahun_topik)
│   ├── decisions/                   # catatan keputusan 0001-..., 0002-...
│   └── reviews/                     # laporan review/audit
├── report/
│   ├── proposal_latex/              # template + proposal LaTeX (struktur internal jangan diubah)
│   └── skripsi_latex/               # template skripsi LaTeX
├── legacy/                          # READ-ONLY: execution_v0/, data_v0/, agent_template_v0/
├── src/mccar_kma/
│   ├── data/                        # loader.py, cleaning.py, interpolation.py
│   ├── scenarios/                   # estimation.py, gbm.py, cost.py
│   ├── risk/                        # ccar.py, mccar.py, evaluator.py
│   ├── model/                       # constraints.py, penalty.py, limits.py
│   ├── optimizers/                  # base.py, kma.py, ga.py, pso.py
│   ├── experiments/                 # runner.py, seeds.py, io.py
│   ├── analysis/                    # summary.py, stats_tests.py, validation.py
│   ├── viz/                         # style.py, figures.py
│   └── utils/                       # config.py, logging.py
├── scripts/                         # 01_audit_data.py, 02_preprocess_data.py, ... (nomor = tahap)
├── tests/                           # test_<modul>.py
├── notebooks/                       # eksplorasi saja
├── results/
│   ├── runs/<config_id>/<algo>/     # satu JSON per replikasi
│   ├── tables/                      # tab_*.csv / tab_*.tex / ringkasan .md
│   └── figures/                     # fig_*.pdf / fig_*.png
└── logs/
```

## Penamaan

- Folder dan file: huruf kecil, `snake_case`, tanpa spasi (pengecualian: `AGENTS.md`, `README.md`).
- Skrip: `NN_kata_kerja_objek.py`, NN = nomor tahap (contoh `04_generate_scenarios.py`).
- Modul: nama benda (`ccar.py`), kelas `PascalCase`, fungsi `snake_case`.
- `config_id` = `<definisi_biaya>_<batas>`: `gross_free`, `gross_djppr`, `interest_free`, `interest_djppr`.
- `algo` ∈ {`kma`, `ga`, `pso`}.
- Hasil per replikasi: `results/runs/<config_id>/<algo>/rep_<kk>_seed<seed>.json` (kk dua digit).
- Tabel: `tab_<topik>[_<config_id>].csv|tex`. Gambar: `fig_<topik>[_<config_id>].pdf|png`.
- Tanggal ISO `YYYY-MM-DD`. Data olahan menyertakan jendela & varian: `market_2017-07-03_2025-11-24_<varian>.csv`.
- Pesan commit: `<jenis>(tahap-NN): <ringkasan>`; jenis = `feat`, `fix`, `test`, `docs`, `data`, `exp`, `chore`.
