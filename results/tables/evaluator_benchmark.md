# Hasil Benchmark Kinerja Evaluator Risiko & Nilai Acuan Baseline (Tahap 05)

- **Waktu Benchmark**: 2026-10-17 19:25:12 UTC
- **Bank Skenario**: `data/processed/bank_train_seed42_N5000.npz` ($N=5.000$)

## 1. Nilai Acuan Baseline Portofolio Eksisting 2024 ($w_0$)

| Parameter | Biaya Bruto (Definisi UTAMA) | Biaya Bunga (SENSITIVITAS) | Keterangan |
|---|---|---|---|
| $\overline{\text{Cost}}(w_0)$ | **1.042370** | **0.044526** | Rata-rata biaya portofolio eksisting |
| $\tau = \text{CCaR}_{95\%}(w_0)$ | **1.085986** | **0.064949** | Batas atas risiko ekor (Persamaan 2.22) |
| $\eta = J_{\text{MCCaR}}(w_0)$ | **0.068115** | **0.173944** | Batas atas dispersi risiko (Persamaan 2.22) |
| $v_J(w_0), v_R(w_0)$ | $0{,}000000, 0{,}000000$ | $0{,}000000, 0{,}000000$ | Layak by construction ($v=0$) |
| $f(w_0)$ | **1.042370** | **0.044526** | Fitness awal tanpa penalti |

## 2. Pengukuran Waktu Eksekusi Evaluator (Single & Batch)

| Mode Evaluasi | Waktu per Evaluasi | Waktu 25.000 Eval (1 Run) | Estimasi Total 9.000.000 Evaluasi (360 Runs) |
|---|---|---|---|
| **Single Evaluate** (`evaluate(w)`) | **0.1780 ms** | 4.45 detik | **26.7 menit** (0.44 jam) |
| **Batch Evaluate** (`evaluate_batch(W)`, P=50) | **0.2727 ms** | 6.82 detik | **40.9 menit** (0.68 jam) |

> [!NOTE]
> Seluruh 9.000.000 evaluasi eksperimen penuh (4 konfigurasi x 3 algoritma x 30 replikasi x 25.000 eval)
> dapat diselesaikan hanya dalam waktu **~26.7 menit** dengan Pure NumPy tanpa dependensi eksternal Numba.

## 3. Ringkasan Pengujian Matematis (Tests)

- **Hitungan Tangan Kasus Sintetis**: CCaR = 3.20, MCCaR = [0.30, 0.35], theta = [1.20, 1.40], J = 0.10 cocok 100% sampai presisi $10^{-12}$.
- **Sifat Analitik**: $\text{MC}_i = \delta \cdot \overline{C}_i$ persis; $\text{CCaR} \ge \overline{\text{Cost}}$; $\text{CCaR}^{(+i)} \ge \text{CCaR}$.
- **Pembagi J**: Memakai $n=7$ (bukan $n-1$).
- **Proyeksi Bobot**: 10.000 titik acak pada batas Free dan DJPPR 100% konvergen ke $\sum w = 1$ dan $lb \le w \le ub$ dalam $10^{-8}$.
- **Budget Counter & Archive**: Pelacakan anggaran 25.000 evaluasi dan arsip solusi layak berbiaya terendah terverifikasi.