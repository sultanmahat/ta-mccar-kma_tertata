# Laporan Penataan Folder

Sumber: `TA_UTANG_VALAS_SULTAN.zip` (folder `TA UTANG VALAS SULTAN`, 169 file). Hasil: folder `ta-mccar-kma` ini. Folder lama Anda tidak diubah; semua perubahan dilakukan pada salinan. Setiap file lama tercatat di `docs/peta_perpindahan.csv` (130 dipindah/diganti nama, 39 tidak dibawa beserta alasannya; tidak ada file yang tidak terhitung).

## 1. Masalah pada struktur lama

| # | Temuan | Dampak |
|---|---|---|
| 1 | Nama folder berspasi dan huruf kapital (`TA UTANG VALAS SULTAN`, `DAFTAR PUSTAKA`, `FILE PROPOSAL UTAMA`); nama file memuat sitasi lengkap, tanda kutip, hingga lebih dari 150 karakter | Sulit diketik di terminal, rawan error di skrip dan LaTeX |
| 2 | Folder `AGENTS/` berisi kode (`execution/`), skill umum, dan template, bukan hanya aturan agen | Agen membaca semuanya sebagai konteks; kode lama dan aturan bercampur |
| 3 | `AGENTS.md` lama adalah template umum "3-layer" (directives → orchestration → execution, hasil ke Google Sheets/Slides). Di dalamnya agen diminta memperbaiki skrip sendiri ("self-anneal") dan memperbarui directive | Bertentangan dengan alur `/plan` yang Anda pilih: agen tidak berhenti untuk meminta persetujuan |
| 4 | Empat skill tidak terkait skripsi di dalam `AGENTS/`: `brand-guidelines`, `brand-scraper`, `frontend-design`, `skill-creator` | Noise; tidak dibawa |
| 5 | Kode lama (`execution/*.py`) mengikuti proposal sebelum revisi | Tidak cocok dengan model sekarang; lihat `legacy/README.md` |
| 6 | 6 PDF duplikat persis (SHA-256 sama), 2 arsip zip template yang isinya sama dengan foldernya | Boros dan membingungkan |
| 7 | Pustaka tidak dikelompokkan (angka 0–20 dicampur dengan folder topik) | Sulit menemukan rujukan per bab |
| 8 | `DATASET/raw/SUMBER_DATA.md` menyebut `python -m src.experiments.run_00_preprocessing` dan "xlsx di root proyek" | Tidak ada modul itu; dataset ada di `DATASET/` dengan nama berbeda. Diperbaiki |
| 9 | `DATASET/results/` dan `.env` kosong | Tidak dibawa |

## 2. Susunan baru

| Folder lama | Folder baru |
|---|---|
| `DATASET/Dataset Utama Optimum Utang Valas.xlsx` | `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` |
| `DATASET/processed/*.csv` | `legacy/data_v0/` |
| `FILE PROPOSAL UTAMA/` | `docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf` |
| `DAFTAR PUSTAKA/` (angka 0–20, MCCaR, KMA, TA UTANG VALAS) | `docs/references/{core, debt_management, risk_measures, optimization, kma, prior_theses}/` |
| `TEMPLATE PROPOSAL/`, `TEMPLATE TUGAS AKHIR/` | `report/proposal_latex/`, `report/skripsi_latex/` (struktur internal sama persis) |
| `AGENTS/execution/*.py`, `AGENTS/AGENTS.md` | `legacy/execution_v0/`, `legacy/agent_template_v0/` |
| (baru) | `AGENTS.md` aturan thesis, `docs/context/spesifikasi_model.md`, `docs/panduan_prompt_antigravity.md` |

Penamaan pustaka: `penulis_tahun_topik.pdf`, huruf kecil, tanpa spasi; versi teks (`.md`) memakai nama dasar yang sama. Contoh: `suyanto_2022_komodo_mlipir_algorithm.pdf`.

## 3. Label pustaka yang perlu Anda periksa (berpengaruh ke Daftar Pustaka skripsi)

Saya membuka halaman pertama file-file ini. Nama pada folder lama tidak cocok dengan isinya:

| File lama | Isi sebenarnya | Tindakan |
|---|---|---|
| `MCCaR/Gorton, G., & Rosen, R. (1995). Measuring Marginal Risk Contributions in Credit Portfolios. FDIC Working Paper 2005-01.pdf` | FDIC CFR Working Paper 2005-01 oleh **Paul Glasserman**, Des 2004. Identik dengan file "2. Paul Glasserman" | Rujuk sebagai Glasserman, bukan Gorton & Rosen (1995). Satu salinan dipakai |
| `MCCaR/Bauer, D., & Zanjani, G. (2015). [digunakan dalam diskusi…].pdf` | Laporan Bauer & Zanjani, Georgia State University, **November 2013**. Identik dengan "1. George State Univ (2013)" | Periksa tahun yang benar sebelum dikutip (2013 menurut halaman judul) |
| `MCCaR/Modeling_Measuring_and_Managing_Risk.pdf` | Hochrainer-Stigler dkk. (2019), risiko sistemik, *Journal of Risk Research* | Tampaknya tidak terkait MCCaR; pastikan memang dikutip |
| `3. Athanasopoulou … (2019_2023)` | Proposal mengutip "Working Paper 31, 2018" | Samakan tahun dengan sumber |
| `17. Brezonnik …` | Nama penulis: Brezočnik | Perbaiki ejaan di Daftar Pustaka |

Duplikat persis yang hanya disimpan satu kali: `5. Direktorat…` = `0. JURNAL UTAMA KEMENKEU`; `MAIN KMA` = `7. Suyanto`; `Stochastic Komodo Algorithm` = `8. Kusuma`; `6. Fauzan` = `1B. LAPORAN FINAL TA IRFAN` (Fauzan = Irfan).

## 4. Keputusan yang menunggu Anda

1. **Kode lama**: setuju tidak dipakai dan hanya jadi referensi di `legacy/`? (Rekomendasi saya: ya; agen menulis ulang mengikuti spesifikasi.)
2. **Varian data (D1)**: data lama sudah memakai irisan 2.028 baris tanpa pernah diputuskan secara tertulis. Putuskan bersama pembimbing apakah tetap irisan atau isi spline (proposal menyebut keduanya).
3. **Label pustaka** pada bagian 3.
