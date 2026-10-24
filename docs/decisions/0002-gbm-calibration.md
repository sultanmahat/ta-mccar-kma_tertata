# Keputusan D2: Spesifikasi Kalibrasi dan Simulasi GBM

- **Tanggal Usulan**: 2026-10-18
- **Tanggal Konfirmasi**: 2026-10-24
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (ito_annualized, terminal_1step, window_end)**

## Ringkasan Keputusan

Tiga sub-keputusan D2 terkait spesifikasi Geometric Brownian Motion (GBM) dan analisis biaya historis disetujui menggunakan seluruh rekomendasi agen (Opsi A pada D2a, D2b, dan D2c).

Nilai di `configs/params.yaml`:
```yaml
scenarios:
  drift_calibration: "ito_annualized"
  simulation_path_mode: "terminal_1step"
  historical_cost_x0: "window_end"
```

---

## 1. D2a — Rumus Kalibrasi Drift $\mu$ dari Log-Return Harian

### Keputusan: Opsi A (Definisi Ito/GBM Standar)

Dari rata-rata harian $m$ dan simpangan baku harian $s$ ($ddof=1$):
$$\sigma = s \cdot \sqrt{252}$$
$$\mu = 252 \cdot m + \frac{\sigma^2}{2}$$

### Alasan
1. **Konsistensi Teori GBM**: Sesuai dengan spesifikasi model §4 ("Kalibrasi default yang diusulkan") dan literatur proses stokastik (Glasserman, 2004).
2. **Kompensasi Lemma Ito**: Dalam persamaan GBM:
   $$S_{t+\Delta t} = S_t \cdot \exp\left( \left(\mu - \frac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t} Z \right)$$
   Komponen drift log-return harian $(\mu - \frac{1}{2}\sigma^2)\cdot \frac{1}{252} = m$, persis sama dengan mean log-return teramati tanpa deviasi drift artifisial.
3. Ekspektasi nilai masa depan terminal memenuhi $\mathbb{E}[S_T] = S_0 e^{\mu T}$.

---

## 2. D2b — Mode Simulasi GBM: Terminal 1-Step vs Jalur 252-Step

### Keputusan: Opsi A (Terminal 1-Step)

Simulasi skenario melompat langsung ke horizon $T = 1$ tahun ($\Delta t = 1$):
$$S_{T, s} = S_0 \cdot \exp\left( \left(\mu - \frac{1}{2}\sigma^2\right) + \sigma Z_s \right), \quad Z_s = L \varepsilon_s, \quad \varepsilon_s \sim \mathcal{N}(0, I_9)$$

### Alasan
1. **Identitas Distribusi Marginal**: Karena model GBM standar tidak memiliki komponen ketergantungan jalur (*path-dependent*) maupun *mean-reversion*, distribusi marginal terminal $S_T$ dari 252 langkah kumulatif identik secara matematis dengan 1 langkah terminal.
2. **Efisiensi Komputasi**: Matriks skenario berukuran $5.000 \times 9$, menghemat alokasi memori dan waktu komputasi secara signifikan tanpa mengorbankan akurasi distribusi biaya pada horizon 1 tahun.

---

## 3. D2c — Nilai $X_0$ Historis untuk Statistik Biaya Persamaan 2.7–2.10

### Keputusan: Opsi A (Observasi Terakhir Jendela / 2025-11-24)

Nilai kurs acuan $X_0$ untuk EUR dan JPY diambil dari observasi terakhir jendela analisis ($t = \text{2025-11-24}$):
$$X_{USD/EUR, 0} = X_{USD/EUR, 2025-11-24}, \quad X_{USD/JPY, 0} = X_{USD/JPY, 2025-11-24}$$

### Alasan
1. **Konsistensi dengan $S_0$ GBM**: Simulasi GBM Tahap 04 menggunakan observasi terakhir sebagai $S_0$ (§4 spesifikasi). Memakai titik acuan yang sama membuat perbandingan biaya historis dan skenario konsisten.
2. **Sifat Invarian Rasio**: Pada perhitungan $\Delta c_{i,t} = \ln(C_{i,t} / C_{i,t-1})$, konstanta $X_0$ saling meniadakan dalam rasio kuotasi kurs ($q_{c,t} / q_{c,t-1} = X_{t-1} / X_t$), sehingga mean dan kovarians $\Delta c$ invarian terhadap pemilihan skala $X_0$, namun menetapkan $X_0$ secara eksplisit diperlukan untuk definisi level biaya $C_{i,t}$ historis.

---

## Implikasi ke Tahap Selanjutnya

1. **Tahap 03**: `scripts/03_estimate_gbm_params.py` menghitung $\mu$ dan $\sigma$ tahunan dengan Opsi A, mengecek kestabilan Cholesky korelasi, dan mencatat statistik biaya historis.
2. **Tahap 04**: Pembangkitan skenario GBM langsung mengevaluasi formula terminal 1-step dengan input $\mu$, $\sigma$, $L = \text{chol}(\text{corr})$, dan $S_0$.
