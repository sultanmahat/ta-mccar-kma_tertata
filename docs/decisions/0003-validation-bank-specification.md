# Keputusan D3: Spesifikasi Bank Validasi Independen

- **Tanggal Usulan**: 2026-10-18
- **Tanggal Konfirmasi**: 2026-10-24
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (N=20.000 skenario, seed 2026, m=1.000)**

## Ringkasan Keputusan

Bank validasi independen ditetapkan dengan ukuran **$N_{\text{valid}} = 20.000$ skenario** dan seed generator acak terpisah (`validation_seed = 2026`), sedangkan bank latih utama menggunakan $N_{\text{train}} = 5.000$ skenario dengan `train_seed = 42`.

Nilai di `configs/params.yaml`:
```yaml
scenarios:
  n_scenarios: 5000
  train_seed: 42
  validation_scenarios: 20000
  validation_seed: 2026
```

---

## Alasan Keputusan

1. **Kestabilan Estimasi Ekor Risiko ($\alpha = 95\%$)**:
   - Pada bank latih ($N = 5.000$), jumlah skenario ekor adalah $m = \lceil(1 - 0{,}95) \times 5.000\rceil = 250$ skenario.
   - Pada bank validasi ($N = 20.000$), jumlah skenario ekor adalah $m = \lceil(1 - 0{,}95) \times 20.000\rceil = 1.000$ skenario (4× lipat lebih padat).
   - Densitas sampel yang lebih tinggi ini memberikan presisi yang jauh lebih baik untuk menguji apakah portofolio optimal dari KMA, GA, dan PSO tetap memenuhi kendala $\text{CCaR} \le \tau$ dan $J_{\text{MCCaR}} \le \eta$ secara *out-of-sample*.
2. **Efisiensi Komputasi**:
   - Array $20.000 \times 9$ float64 hanya membutuhkan memori RAM $\approx 1{,}44\text{ MB}$.
   - Waktu pembangkitan terminal 1-step hanya memakan waktu $< 0{,}2$ detik.
3. **Independensi Stokastik**:
   - Seed yang berbeda menjamin tidak terjadi *data leakage* antara tahap pelatihan/optimasi dan tahap evaluasi akhir/validasi independen (§10 spesifikasi).

---

## Implikasi ke Tahap Selanjutnya

1. **Tahap 04**: `scripts/04_generate_scenarios.py` membangkitkan dua pasang file:
   - `data/processed/bank_train_seed42_N5000.npz` (+ JSON metadata)
   - `data/processed/bank_valid_seed2026_N20000.npz` (+ JSON metadata)
2. **Tahap 05–07 (Optimasi)**: Semua 360 replikasi metaheuristik (KMA, GA, PSO) mengevaluasi fungsi objektif pada bank latih ($N=5.000$) yang sama persis.
3. **Tahap 08–09 (Analisis & Pelaporan)**: Solusi bobot terbaik yang dihasilkan dievaluasi ulang pada bank validasi ($N=20.000$) untuk mengukur ketahanan risiko.
