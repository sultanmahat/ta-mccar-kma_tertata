# Keputusan D4: Detail Parameter dan Mekanisme KMA yang Tidak Ditentukan Proposal

- **Tanggal Usulan**: 2026-10-18
- **Tanggal Konfirmasi**: 2026-10-24
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (Parameter default Suyanto 2022 & proposal: p_bm=0.5, gamma=0.1, mating=0.5, delta_n=5)**

## Ringkasan Keputusan

Seluruh parameter KMA yang tidak ditentukan secara eksplisit dalam proposal ditetapkan mengikuti makalah penemu algoritma: **Suyanto, Ariyanto, & Ariyanto (2022), "Komodo Mlipir Algorithm", *Applied Soft Computing*, Vol. 114, 108043**.

| Parameter | Simbol | Nilai | Sumber Rujukan |
|---|---|---|---|
| Proporsi Big Males | $p_{bm}$ | $0{,}5$ | Suyanto dkk. 2022, Tabel 1 & Bagian 3.1 |
| Radius Partenogenesis | $\gamma$ | $0{,}1$ | Suyanto dkk. 2022, Bagian 2.8 & Pers. 7 |
| Jumlah Big Male Interaksi | $q$ | $n_{bm}$ (seluruh) | Suyanto dkk. 2022, Bagian 2.7 & Pers. 4 |
| Probabilitas Kawin | $p_{\text{mating}}$ | $0{,}5$ | Suyanto dkk. 2022, Bagian 2.8 |
| Toleransi Stagnasi | $\epsilon_{\text{stag}}$ | $10^{-7}$ | Suyanto dkk. 2022, Bagian 2.10 |
| Langkah Adaptasi Populasi | $\Delta n$ | $5$ | Suyanto dkk. 2022, Bagian 2.10 |
| Serah-Terima Fase 1 → 2 | — | Warisi solusi terbaik + 199 acak baru | Disesuaikan untuk desain dua fase |

Nilai di `configs/params.yaml`:
```yaml
algorithms:
  kma:
    p_bm: 0.5
    gamma: 0.1
    q_interactions: null  # null = seluruh n_bm
    p_mating: 0.5
    stagnation_patience: 2
    stagnation_tol: 1.0e-7
    delta_n: 5
    phase_transition_strategy: "inherit_best_with_random_diversity"
```

---

## Alasan Keputusan

1. **Kepatuhan terhadap Literatur Penemu**: Menggunakan parameter default dari makalah asli menjamin keabsahan komparasi algoritma dan mempermudah justifikasi dalam laporan skripsi.
2. **Desain Dua Fase Proposal**: Proposal menetapkan Fase 1 ($n=5$, anggaran 5.000) dan Fase 2 ($n$ awal 200, anggaran 20.000). Mekanisme serah-terima yang mewariskan solusi terbaik Fase 1 sambil memulihkan diversitas pada Fase 2 menjembatani deteksi cepat global (Fase 1) dengan eksploitasi lokal padat (Fase 2).
3. **Nilai $\gamma = 0{,}1$** (10% rentang) sesuai dengan literatur partenogenesis KMA yang menyeimbangkan eksplorasi tanpa terlalu mengganggu eksploitasi *female*.

---

## Implikasi ke Tahap Selanjutnya

1. `src/mccar_kma/optimizers/kma.py` mengimplementasikan KMA sesuai keputusan ini.
2. Semua parameter dapat diubah via `configs/params.yaml` tanpa memodifikasi kode.
3. GA dan PSO akan menggunakan antarmuka `BaseOptimizer` yang sama (Tahap berikutnya).
