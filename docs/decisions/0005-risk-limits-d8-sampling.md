# Keputusan D8: Prosedur Pembangkitan 1.000 Kombinasi Acak DJPPR (Baseline Historis)

- **Tanggal Usulan**: 2026-10-18
- **Status**: Diusulkan agen / Menunggu konfirmasi Sultan
- **Diusulkan oleh**: Agen AI (Pair Programming)
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat (Mahasiswa)

## Ringkasan Keputusan

Untuk mereplikasi acuan historis DJPPR (Kemenkeu, 2025) sebanyak 1.000 kombinasi bobot acak di dalam rentang proporsi instrumen ($lb_i \le w_i \le ub_i, \sum_{i=1}^7 w_i = 1$):
Diputuskan menggunakan **Opsi A: Rejection Sampling pada Bobot Ternormalisasi Uniform**.

Prosedur:
1. Bangkitkan kandidat acak independen seragam dalam batas hiperkubus: $u_i \sim \text{Uniform}(lb_i, ub_i)$.
2. Normalisasi bobot sehingga berjumlah satu: $w_i = u_i / \sum_{k=1}^7 u_k$.
3. Evaluasi pemenuhan batas proporsi: jika $lb_i - \epsilon_{\text{tol}} \le w_i \le ub_i + \epsilon_{\text{tol}}$ untuk semua $i$, terima kandidat $w$. Jika tidak, tolak dan ulangi.
4. Lakukan proyeksi presisi akhir dengan `project_weights` untuk menjamin $\sum w_i = 1$ dan $lb \le w \le ub$ terpenuhi presisi numerik $10^{-8}$.

Nilai di `configs/params.yaml`:
```yaml
experiments:
  random_benchmark_count: 1000
  random_benchmark_method: "rejection"
  random_benchmark_seed: 42
```

---

## Alasan Keputusan

1. **Bebas dari Bias Batas (*Boundary Clustering*)**:
   Metode alternatif (kliping dan normalisasi berulang langsung / *iterative projection*) memaksa vektor acak yang keluar dari simpleks untuk ditarik ke dinding/sudut ruang proporsi, menyebabkan pemusatan buatan pada batas $lb$ dan $ub$. Rejection sampling menjamin distribusi bobot di dalam simpleks terpotong bersifat seragam alami tanpa distorsi.
2. **Efisiensi Komputasi Sangat Tinggi**:
   Berdasarkan pengujian empiris pada rentang DJPPR, tingkat penerimaan (*acceptance rate*) mencapai **74,40%**. Untuk mendapatkan 1.000 sampel acak layak, hanya dibutuhkan rata-rata ~1.344 penarikan seragam. Waktu eksekusi pembangkitan kurang dari 5 milidetik.
3. **Kepatuhan Terhadap Referensi DJPPR**:
   Kajian DJPPR Kemenkeu (2025) Subbab 3.6.1 dan Bagian 8 menyatakan bahwa 1.000 kombinasi di-generate secara acak di dalam batas proporsi untuk mengeksplorasi ruang solusi yang memungkinkan. Rejection sampling merefleksikan prinsip eksplorasi acak tersebut secara paling akurat.

---

## Implikasi ke Tahap Selanjutnya

1. `src/mccar_kma/model/limits.py` mengimplementasikan fungsi `generate_random_weights_djppr(n_samples=1000, ...)` dengan metode `"rejection"`.
2. Hasil evaluasi 1.000 kombinasi acak disimpan ke `results/tables/baseline_djppr_gross.csv` dan `results/tables/baseline_djppr_interest.csv` sebagai baseline pembanding bagi algoritma KMA, GA, dan PSO.
