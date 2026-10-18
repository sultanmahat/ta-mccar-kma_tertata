# Ringkasan Batas Risiko, Baseline DJPPR, dan Solusi Referensi SLSQP

- **Tanggal Eksekusi**: 2026-10-17 22:49:09 UTC
- **Bank Latih**: `bank_train_seed42_N5000.npz` (N = 5,000, seed = 42)
- **Metode Sampling Acak (D8)**: `rejection` (1,000 sampel, seed = 42)

## 1. Batas Risiko Acuan Portofolio Eksisting 2024 ($w_0$)

| Definisi Biaya | Biaya Rata-rata $\overline{\text{Cost}}(w_0)$ | Batas Ekor $\tau = \text{CCaR}_{0.95}(w_0)$ | Batas Dispersi $\eta = J_{\text{MCCaR}}(w_0)$ | Status Kelayakan |
|---|---|---|---|---|
| **Gross** | 1.04236992 | 1.08598587 | 0.06811472 | Layak ($v_J=0, v_R=0$) |
| **Interest** | 0.04452591 | 0.06494889 | 0.17394359 | Layak ($v_J=0, v_R=0$) |

## 2. Replikasi Baseline Historis DJPPR (1.000 Kombinasi Acak)

| Definisi Biaya | Total Sampel | Lolos Kendala ($J \le \eta$ & $\text{CCaR} \le \tau$) | % Layak | Min Biaya Layak | Rata-rata Biaya Layak | Maks Biaya Layak |
|---|---|---|---|---|---|---|
| **Gross** | 1,000 | 397 | 39.70% | 1.04212814 | 1.04288532 | 1.04384805 |
| **Interest** | 1,000 | 434 | 43.40% | 0.04394834 | 0.04430194 | 0.04466165 |

## 3. Komparasi Solusi: Eksisting ($w_0$) vs DJPPR vs Referensi SLSQP

| Definisi Biaya | Metode Solusi | $\overline{\text{Cost}}$ | $\text{CCaR}_{0.95}$ | $J_{\text{MCCaR}}$ | Status Layak | Reduksi vs $w_0$ (%) |
|---|---|---|---|---|---|---|
| **Gross** | Eksisting ($w_0$) | 1.04236992 | 1.08598587 | 0.06811472 | Layak | 0.0000% |
| | DJPPR Random Filtering (Terbaik) | 1.04212814 | 1.08562076 | 0.06786982 | Layak | +0.0232% |
| | Solusi Referensi SLSQP | 1.04186946 | 1.08534479 | 0.06811472 | Layak | +0.0480% |
| **Interest** | Eksisting ($w_0$) | 0.04452591 | 0.06494889 | 0.17394359 | Layak | 0.0000% |
| | DJPPR Random Filtering (Terbaik) | 0.04394834 | 0.06405726 | 0.16497922 | Layak | +1.2972% |
| | Solusi Referensi SLSQP | 0.04362937 | 0.06341825 | 0.15969792 | Layak | +2.0135% |
