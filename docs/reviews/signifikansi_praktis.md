# Signifikansi Praktis 360 Run — Selisih Biaya, Kendala Aktif, Waktu, Kelayakan

**Tahap**: 19-20 (`scripts/19_measure_single_worker_timing.py`, `scripts/20_analyze_practical_significance.py`)

Laporan ini **melengkapi** Tahap 13 (`results/tables/stats_summary.md`), tidak menggantikannya. Kruskal-Wallis/Dunn Tahap 13 valid secara statistik ($p\ll0{,}001$, $\epsilon^2$ besar) — pertanyaannya di sini adalah seberapa **bermakna secara praktis** selisih itu, bukan apakah selisihnya nyata secara statistik (selisih yang sangat kecil pun bisa signifikan dengan presisi numerik tinggi dan $n=30$).

Margin ekivalensi (D12): **0.01%** relatif terhadap median biaya grup pembanding (Opsi A, lihat `docs/decisions/0012-*.md`).

> **Tidak ada klaim algoritma 'terbaik' di laporan ini.** Tabel di bawah melaporkan selisih, interval, dan status ekivalensi/kelayakan apa adanya.

---

## 1. Selisih praktis, Hodges-Lehmann, dan ekivalensi (TOST)

### `gross_free`

gross_free: kendala risiko aktif pada sebagian besar run (J aktif 68%, CCaR aktif 1%) -- solusi ditahan oleh batas J/CCaR, bukan oleh batas kotak.

| Pasangan | Median A | Median B | Selisih (satuan) | Selisih (%) | Hodges-Lehmann | CI 95% HL | TOST ekivalen? | CI-margin ekivalen? |
|---|---:|---:|---:|---:|---:|---|:---:|:---:|
| kma_vs_ga | `1.038063` | `1.037069` | `9.94e-04` | `0.0958%` | `9.65e-04` | [`7.18e-04`, `1.26e-03`] | Tidak | Tidak |
| kma_vs_pso | `1.038063` | `1.037056` | `1.01e-03` | `0.0971%` | `9.09e-04` | [`6.12e-04`, `1.23e-03`] | Tidak | Tidak |
| ga_vs_pso | `1.037069` | `1.037056` | `1.37e-05` | `0.0013%` | `1.05e-05` | [`6.57e-06`, `1.67e-05`] | Ya | Ya |

### `gross_djppr`

gross_djppr: kendala risiko aktif pada sebagian besar run (J aktif 100%, CCaR aktif 98%) -- solusi ditahan oleh batas J/CCaR, bukan oleh batas kotak.

| Pasangan | Median A | Median B | Selisih (satuan) | Selisih (%) | Hodges-Lehmann | CI 95% HL | TOST ekivalen? | CI-margin ekivalen? |
|---|---:|---:|---:|---:|---:|---|:---:|:---:|
| kma_vs_ga | `1.041919` | `1.041869` | `4.98e-05` | `0.0048%` | `4.95e-05` | [`3.53e-05`, `8.32e-05`] | Ya | Ya |
| kma_vs_pso | `1.041919` | `1.041866` | `5.34e-05` | `0.0051%` | `5.32e-05` | [`3.93e-05`, `9.06e-05`] | Ya | Ya |
| ga_vs_pso | `1.041869` | `1.041866` | `3.53e-06` | `0.0003%` | `3.46e-06` | [`2.45e-06`, `3.90e-06`] | Ya | Ya |

### `interest_free`

interest_free: kendala risiko aktif pada sebagian besar run (J aktif 68%, CCaR aktif 0%) -- solusi ditahan oleh batas J/CCaR, bukan oleh batas kotak.

| Pasangan | Median A | Median B | Selisih (satuan) | Selisih (%) | Hodges-Lehmann | CI 95% HL | TOST ekivalen? | CI-margin ekivalen? |
|---|---:|---:|---:|---:|---:|---|:---:|:---:|
| kma_vs_ga | `0.031472` | `0.031049` | `4.23e-04` | `1.3622%` | `4.14e-04` | [`2.62e-04`, `7.11e-04`] | Tidak | Tidak |
| kma_vs_pso | `0.031472` | `0.031038` | `4.34e-04` | `1.3985%` | `3.92e-04` | [`2.60e-04`, `6.85e-04`] | Tidak | Tidak |
| ga_vs_pso | `0.031049` | `0.031038` | `1.11e-05` | `0.0358%` | `8.23e-06` | [`4.51e-06`, `1.59e-05`] | Tidak | Tidak |

### `interest_djppr`

interest_djppr: optimum didominasi vertex kotak-simpleks (rata-rata 6.0/7 bobot di batas), kendala risiko tidak aktif pada 97% run -- ketiga algoritma konvergen ke titik yang hampir identik secara geometris, bukan karena satu algoritma lebih unggul.

| Pasangan | Median A | Median B | Selisih (satuan) | Selisih (%) | Hodges-Lehmann | CI 95% HL | TOST ekivalen? | CI-margin ekivalen? |
|---|---:|---:|---:|---:|---:|---|:---:|:---:|
| kma_vs_ga | `0.043630` | `0.043629` | `3.00e-07` | `0.0007%` | `2.94e-07` | [`1.56e-07`, `7.07e-07`] | Ya | Ya |
| kma_vs_pso | `0.043630` | `0.043629` | `3.00e-07` | `0.0007%` | `3.00e-07` | [`1.65e-07`, `7.09e-07`] | Ya | Ya |
| ga_vs_pso | `0.043629` | `0.043629` | `6.74e-10` | `0.0000%` | `6.74e-10` | [`1.05e-10`, `1.49e-09`] | Ya | Ya |

---

## 2. Kendala aktif dan vertex kotak-simpleks ("optimum LP")

| Konfigurasi | J aktif | CCaR aktif | Vertex kotak-simpleks | Vertex & kendala risiko tidak aktif | Rata-rata bobot di batas |
|---|---:|---:|---:|---:|---:|
| `gross_free` | 68% | 1% | 0% | 0% | 4.3/7 |
| `gross_djppr` | 100% | 98% | 0% | 0% | 2.9/7 |
| `interest_free` | 68% | 0% | 0% | 0% | 3.0/7 |
| `interest_djppr` | 0% | 0% | 97% | 97% | 6.0/7 |

---

## 3. Waktu komputasi: 1 proses vs 6-worker

Mesin: `12th Gen Intel(R) Core(TM) i5-12450H`, 12 core logis, `Windows 11 (10.0.26300)`. 1-proses = median 5 replikasi baru (seed terpisah, tidak menimpa 360 run utama); 6-worker = rata-rata 30 replikasi eksperimen utama Tahap 10/13.

| Konfigurasi | Algo | Waktu 1-proses (median, s) | Waktu 6-worker (mean, s) | Rasio |
|---|---|---:|---:|---:|
| `gross_free` | KMA | 25.38 | 73.02 | 0.35x |
| `gross_free` | GA | 8.03 | 34.31 | 0.23x |
| `gross_free` | PSO | 7.87 | 29.53 | 0.27x |
| `gross_djppr` | KMA | 26.51 | 88.39 | 0.30x |
| `gross_djppr` | GA | 8.33 | 37.54 | 0.22x |
| `gross_djppr` | PSO | 8.34 | 28.98 | 0.29x |
| `interest_free` | KMA | 23.62 | 82.04 | 0.29x |
| `interest_free` | GA | 8.28 | 80.64 | 0.10x |
| `interest_free` | PSO | 7.97 | 66.55 | 0.12x |
| `interest_djppr` | KMA | 25.24 | 180.13 | 0.14x |
| `interest_djppr` | GA | 8.30 | 32.68 | 0.25x |
| `interest_djppr` | PSO | 7.94 | 31.90 | 0.25x |

---

## 4. Kelayakan validasi OOS: Fisher dan Barnard (koreksi Holm per konfigurasi)

| Konfigurasi | Pasangan | k/n A | k/n B | p Fisher | p Fisher Holm | p Barnard | p Barnard Holm |
|---|---|---|---|---:|---:|---:|---:|
| `gross_free` | kma_vs_ga | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `gross_free` | kma_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `gross_free` | ga_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `gross_djppr` | kma_vs_ga | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `gross_djppr` | kma_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `gross_djppr` | ga_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `interest_free` | kma_vs_ga | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `interest_free` | kma_vs_pso | 30/30 | 28/30 | `0.4915` | `1.0000` | `0.1987` | `0.5961` |
| `interest_free` | ga_vs_pso | 30/30 | 28/30 | `0.4915` | `1.0000` | `0.1987` | `0.5961` |
| `interest_djppr` | kma_vs_ga | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `interest_djppr` | kma_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |
| `interest_djppr` | ga_vs_pso | 30/30 | 30/30 | `1.0000` | `1.0000` | `1.0000` | `1.0000` |

---

## Keterbatasan

- Margin ekivalensi 0,01% seragam (D12 Opsi A) relatif longgar secara absolut untuk `interest_free`/`interest_djppr` (biaya absolut kecil, ~0,03-0,17) dibanding `gross_*` (~1,04) — lihat `docs/decisions/0012-practical-equivalence-margin-d12.md`.
- "Optimum LP layak" bukan hasil solve LP sungguhan (`scipy.optimize.linprog`), melainkan diagnosis dari status kendala aktif dan jumlah bobot di batas kotak per run — pendekatan, bukan pembuktian formal bahwa kendala risiko benar-benar tidak berperan di titik optimum global.
- Waktu 1-proses diukur dengan seed baru (bukan seed eksperimen utama) — perbandingan ke waktu 6-worker bersifat indikatif (kontensi CPU berbeda), bukan replikasi run yang sama persis.
