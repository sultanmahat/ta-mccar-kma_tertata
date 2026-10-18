# Ringkasan Batas Risiko, Baseline DJPPR, dan Solusi Referensi SLSQP

- **Tanggal Eksekusi**: 2026-10-18 04:17:54 UTC
- **Bank Latih**: `bank_train_seed42_N5000.npz` (N = 5,000, seed = 42)
- **Metode Sampling Acak (D8)**: `rejection` (1,000 sampel, seed = 42)

## 1. Batas Risiko Acuan Portofolio Eksisting 2024 ($w_0$)

| Definisi Biaya | Biaya Rata-rata $\overline{\text{Cost}}(w_0)$ | Batas Ekor $\tau = \text{CCaR}_{0.95}(w_0)$ | Batas Dispersi $\eta = J_{\text{MCCaR}}(w_0)$ | Status Kelayakan |
|---|---|---|---|---|
| **Gross** | 1.04236992 | 1.08602313 | 0.06819428 | Layak ($v_J=0, v_R=0$) |
| **Interest** | 0.04452591 | 0.06496906 | 0.17418784 | Layak ($v_J=0, v_R=0$) |

## 2. Replikasi Baseline Historis DJPPR (1.000 Kombinasi Acak)

| Definisi Biaya | Total Sampel | Lolos Kendala ($J \le \eta$ & $\text{CCaR} \le \tau$) | % Layak | Min Biaya Layak | Rata-rata Biaya Layak | Maks Biaya Layak |
|---|---|---|---|---|---|---|
| **Gross** | 1,000 | 398 | 39.80% | 1.04212814 | 1.04288416 | 1.04384805 |
| **Interest** | 1,000 | 440 | 44.00% | 0.04394834 | 0.04430286 | 0.04466165 |

## 3. Komparasi Solusi: Eksisting ($w_0$) vs DJPPR vs Referensi SLSQP

| Definisi Biaya | Metode Solusi | $\overline{\text{Cost}}$ | $\text{CCaR}_{0.95}$ | $J_{\text{MCCaR}}$ | Status Layak | Reduksi vs $w_0$ (%) |
|---|---|---|---|---|---|---|
| **Gross** | Eksisting ($w_0$) | 1.04236992 | 1.08602313 | 0.06819428 | Layak | 0.0000% |
| | DJPPR Random Filtering (Terbaik) | 1.04212814 | 1.08565746 | 0.06794381 | Layak | +0.0232% |
| | Solusi Referensi SLSQP | 1.04186769 | 1.08543594 | 0.06818792 | Layak | +0.0482% |
| **Interest** | Eksisting ($w_0$) | 0.04452591 | 0.06496906 | 0.17418784 | Layak | 0.0000% |
| | DJPPR Random Filtering (Terbaik) | 0.04394834 | 0.06407719 | 0.16535431 | Layak | +1.2972% |
| | Solusi Referensi SLSQP | 0.04362937 | 0.06343748 | 0.15992899 | Layak | +2.0135% |
