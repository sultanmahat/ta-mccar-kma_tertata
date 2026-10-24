# Keputusan D9: Standar Tipografi, Visualisasi Ilmiah, dan Format Tabel LaTeX Skripsi

- **Tanggal Usulan**: 2026-10-18
- **Status**: Diusulkan agen / Menunggu konfirmasi Sultan
- **Diusulkan oleh**: Agen AI (Pair Programming)
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat (Mahasiswa)

---

## Ringkasan Keputusan

Untuk menghasilkan aset visual dan tabel skripsi berkualitas tinggi yang siap dicetak (*camera-ready*) sesuai pedoman penulisan Departemen Matematika FSAD-ITS, ditetapkan keputusan sebagai berikut:

| Butir Keputusan | Pilihan Terpilih | Dasar Pertimbangan / Rujukan |
|---|---|---|
| **D9.1: Format Ekspor Gambar** | **Format Ganda**: PDF Vektor (`.pdf`) + PNG Raster 300 dpi (`.png`) | PDF vektor menjamin ketajaman tak terbatas saat di-render LaTeX; PNG 300 dpi siap digunakan pada pratinjau dokumen dan slide presentasi sidang. |
| **D9.2: Tata Letak Konfigurasi** | **Opsi C (Hibrida)**: Berkas individual per konfigurasi (`fig_<topik>_<config_id>`) **sekaligus** panel gabungan $2 \times 2$ grid (`fig_<topik>_all`) | Memberikan fleksibilitas penuh bagi penyusunan naskah Bab 4 (bisa menggunakan 1 halaman panel penuh atau pembahasan terpisah per subbab). |
| **D9.3: Tipografi & Notasi Matematika** | Font keluarga `serif` (`DejaVu Serif`, `Times New Roman`) dan Computer Modern math text | Menjamin keharmonisan estetika visual antara grafik dan tipografi dokumen LaTeX skripsi ITS. |
| **D9.4: Keterbacaan Cetak Hitam-Putih** | Kombinasi pola garis (*line style*), bentuk penanda (*marker*), dan 7 tekstur arsir (*hatching*) | Gambar tetap dapat dibedakan dan dibaca dengan jelas jika naskah dicetak pada printer monokrom (hitam-putih). |
| **D9.5: Titik Solusi Komparasi Komposisi & Rasio $\theta_i$** | Solusi Layak Terbaik (*Best Run*) dari 30 replikasi per algoritma vs Eksisting $w_0$ & Baseline DJPPR | Merepresentasikan strategi portofolio optimal nyata yang dicapai oleh masing-masing metode metaheuristik. |
| **D9.6: Integritas Tabel LaTeX** | Format standar `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), **100% dibaca otomatis dari file hasil** tanpa angka ketik manual | Menjamin reprodusibilitas dan mengeliminasi risiko kesalahan pengetikan (*human transcription error*). |

---

## Alasan Keputusan

1. **Kepatuhan Terhadap Standar Skripsi ITS**:
   Format tipografi serif dan tata letak `booktabs` adalah standar baku publikasi akademik.
2. **Keterbacaan Monokrom**:
   Penggunaan warna saja (*color-only differentiation*) tidak ramah bagi pembaca buta warna maupun cetak fisik hitam-putih. Penambahan tekstur arsir (`//`, `\\`, `xx`, `..`, `++`, `**`, `OO`) pada diagram batang komposisi instrumen menjamin setiap instrumen valas dapat diidentifikasi secara visual tanpa warna.
3. **Reproduksibilitas Total**:
   Seluruh tabel dihasilkan dari skrip `scripts/14_make_figures_tables.py` yang membaca langsung berkas hasil empiris (`runs_summary.csv`, `validation_all_runs.csv`, `stats_*.csv`), memastikan sinkronisasi angka di tabel dengan data simulasi.
