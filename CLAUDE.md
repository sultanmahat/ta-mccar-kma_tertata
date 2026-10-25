# CLAUDE.md — Aturan Kerja Proyek (cermin AGENTS.md)

Berkas ini cermin `AGENTS.md` di root yang sama, supaya agen apa pun (Claude Code, Claude for VS Code, dst.) memakai aturan identik. Bila berkas ini dan `AGENTS.md` berbeda, `AGENTS.md` yang berlaku — laporkan selisihnya, jangan menebak mana yang benar.

Proyek: skripsi S1 Matematika ITS — "Optimasi Portofolio Utang Negara Multivaluta dengan Pendekatan Model Marginal Conditional Cost at Risk (MCCaR) menggunakan Komodo Mlipir Algorithm (KMA)".
Pemilik: Sultan Bakri Baihaqi Mahat (NRP 5002221016). Pembimbing: Prof. Dr. Mohammad Isa Irawan, MT.

Sumber kebenaran model dan data: `docs/context/spesifikasi_model.md`.
Proposal asli: `docs/proposal/` (PDF revisi pasca-sempro — bukan draf LaTeX lama di `report/`). Jurnal acuan DJPPR: `docs/references/`.
Jika kode, proposal, dan spesifikasi berbeda, hentikan pekerjaan dan tanyakan. Jangan menebak.

`legacy/` berisi kode dan data versi sebelum revisi proposal. Hanya referensi: jangan diimpor, diubah, atau dijadikan sumber kebenaran.

## Cara kerja (wajib)

1. Mulai setiap tugas dengan Implementation Plan, lalu BERHENTI dan tunggu persetujuan ("Proceed"). Sebelum itu hanya boleh membaca file; jangan menulis, mengubah, atau menjalankan perintah yang mengubah file.
2. Setiap hal yang tidak ditentukan spesifikasi ditulis di plan sebagai **KEPUTUSAN DIBUTUHKAN**: 2–3 opsi, untung-ruginya, dan satu rekomendasi. Jangan memilih sendiri.
3. Plan memuat: daftar file yang akan dibuat/diubah, daftar KEPUTUSAN DIBUTUHKAN, cara verifikasi (tes apa, angka apa yang ditampilkan), dan hal yang sengaja tidak dikerjakan.
4. Kerjakan hanya cakupan tugas yang diminta. Temuan di luar cakupan dicatat di akhir Walkthrough, tidak dikerjakan sepihak.
5. Walkthrough akhir memuat: file yang dibuat/diubah, cara menjalankan, hasil verifikasi berupa output terminal nyata, dan hal yang belum beres.
6. Jangan menyatakan "benar", "lolos", atau "sukses" tanpa menjalankan tes/skrip dan menampilkan hasilnya.
7. Keputusan yang sudah disetujui dicatat di `docs/decisions/NNNN-judul-singkat.md` (konteks, opsi, keputusan, tanggal).
8. Kejujuran ilmiah mutlak: jangan menyembunyikan hasil buruk. Jika algoritma konvergen lambat, kendala/penalti tinggi, atau hasil statistik mengecewakan, laporkan apa adanya.

## Bahasa dan gaya

- Penjelasan kepada pengguna: Bahasa Indonesia, ringkas, lugas, tanpa basa-basi.
- Nama variabel, fungsi, modul, dan berkas: English `snake_case`.
- Docstring dan komentar: Bahasa Indonesia. Setiap fungsi matematis wajib menyebut nomor persamaan proposal (mis. "Persamaan 2.13").

## Data dan reproduksibilitas

- `data/raw/`, `docs/proposal/`, `docs/references/`, dan `legacy/` READ-ONLY: tidak boleh diubah, ditimpa, atau dihapus. `report/` hanya diubah bila diminta.
- Data olahan ditulis ke `data/interim/` dan `data/processed/` hanya lewat skrip di `scripts/`.
- Tidak ada angka ajaib di kode. Semua parameter ada di `configs/params.yaml`.
- Semua keacakan memakai `numpy.random.Generator` dengan seed eksplisit; jangan memakai RNG global.
- Setiap keluaran hasil membawa metadata: tanggal, hash konfigurasi, seed, versi data.
- Skrip pipeline bernomor sesuai nomor tahap dan harus bisa dijalankan ulang dari nol dengan hasil identik.

## Standar kode

- Python 3.11+, src-layout, paket `mccar_kma`, type hints, `pathlib`.
- Dependensi yang diizinkan: numpy, pandas, scipy, openpyxl, pyyaml, matplotlib, pytest, tqdm. Dependensi lain hanya dengan persetujuan di plan.
- Logika inti hanya di `src/`; notebook hanya untuk eksplorasi, tidak dipakai pipeline.
- Setiap modul inti punya tes di `tests/` (pytest). Tes menguji sifat matematis, bukan hanya "tidak error".
- Vektorisasi dengan numpy untuk perhitungan yang dipanggil jutaan kali.

## Larangan

- Mengubah parameter pada Tabel 3.1 proposal tanpa persetujuan.
- Mengubah arti rumus. Ambiguitas = KEPUTUSAN DIBUTUHKAN.
- Menghapus file di luar cakupan tugas, `git push` tanpa diminta, atau menginstal paket di luar daftar izin.
- Menyembunyikan hasil buruk: jika hasil tidak layak atau mengecewakan, laporkan apa adanya.

## Struktur folder, penamaan, commit

Lihat `AGENTS.md` bagian "Struktur folder" dan "Penamaan" — tidak diduplikasi di sini untuk menghindari dua sumber yang bisa menyimpang. Ringkasan commit: `<jenis>(tahap-NN): <ringkasan>`; jenis = `feat`, `fix`, `test`, `docs`, `data`, `exp`, `chore`.

## Status keputusan metodologis

D1–D12 sudah disetujui ("Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat"). Daftar dan isi lengkap tiap keputusan: `docs/decisions/README.md` dan `docs/decisions/0001-...` s.d. `0012-...`. Jangan menyalin ulang isi D1–D12 ke berkas lain — rujuk saja ke sana, supaya tidak ada dua sumber yang bisa berbeda saat keputusan baru ditambah.
