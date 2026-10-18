# Optimasi Portofolio Utang Negara Multivaluta Menggunakan Marginal Conditional Cost at Risk (MCCaR) dan Komodo Mlipir Algorithm (KMA)

**Penulis:** Sultan Bakri Baihaqi Mahat (NRP: 5002221016)  
**Departemen:** Matematika, Fakultas Sains dan Analitika Data (FSAD), Institut Teknologi Sepuluh Nopember (ITS), Surabaya  
**Dosen Pembimbing:** Prof. Dr. Mohammad Isa Irawan, M.T.  
**Dokumen Proposal:** `docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf`  
**Sumber Kebenaran Model:** `docs/context/spesifikasi_model.md`

---

## 1. Ikhtisar Penelitian

Repositori ini memuat implementasi komputasi ilmiah penuh untuk optimasi portofolio utang pemerintah Indonesia berdenominasi valuta asing (7 instrumen obligasi negara berbunga tetap dalam mata uang USD, EUR, dan JPY) dengan pendekatan:
1. **Model Risiko:** *Marginal Conditional Cost at Risk* (MCCaR) dan batasan risiko ekor *Conditional Cost at Risk* (CCaR) pada tingkat kepercayaan 95%.
2. **Algoritma Utama:** *Komodo Mlipir Algorithm* (KMA) dua-fase (eksplorasi pejantan besar dan eksploitasi pergerakan *mlipir*).
3. **Algoritma Pembanding:** *Genetic Algorithm* (GA) dan *Particle Swarm Optimization* (PSO) pada bank skenario *Geometric Brownian Motion* (GBM) yang identik.
4. **Matriks Evaluasi:** 4 konfigurasi eksperimen ($\{ \text{gross}, \text{interest} \} \times \{ \text{free}, \text{djppr} \}$) $\times$ 3 algoritma $\times$ 30 replikasi independen = **360 run eksperimen penuh** (anggaran 25.000 evaluasi per run).
5. **Validasi Independen:** Evaluasi ketahanan out-of-sample pada bank validasi terpisah berukuran $N=20.000$ skenario.

---

## 2. Persiapan Lingkungan Kerja (Setup)

Repositori ini dirancang agar dapat direproduksi secara deterministik pada sistem operasi **Windows, Linux, maupun macOS** menggunakan **Python 3.11+**.

### a. Kloning Repositori & Pembuatan Virtual Environment

```bash
# 1. Kloning repositori (atau navigasi ke direktori kerja)
cd ta-mccar-kma

# 2. Buat virtual environment
python -m venv .venv

# 3. Aktivasi virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate
```

### b. Instalasi Dependensi Eksak (Pinning)

Untuk menjamin kesamaan versi pustaka numerik (`numpy 2.5.4`, `scipy 1.18.1`, `pandas 3.0.6`, `matplotlib 3.11.2`, dll.):

```bash
# Menggunakan requirements.lock (direkomendasikan)
pip install --upgrade pip
pip install -r requirements.lock

# Atau instalasi mode pengembangan standar:
pip install -e ".[dev]"
```

---

## 3. Eksekusi Cepat Satu Perintah (One-Click Pipeline)

Untuk mereproduksi seluruh alur penelitian dari data mentah, estimasi GBM, simulasi, optimasi, validasi, uji statistik, hingga grafik dan tabel skripsi:

### Mode Pilot Cepat (~5–7 Menit)
Sangat disarankan untuk pengujian instalasi awal dan verifikasi fungsi menyeluruh:
```powershell
# Windows (PowerShell)
.\scripts\run_all.ps1 -Pilot
```
```bash
# Linux / macOS (Bash)
chmod +x scripts/run_all.sh
./scripts/run_all.sh --pilot
```

### Mode Eksperimen Penuh (Full Replication)
Menjalankan 360 run eksperimen (resume aktif jika berkas JSON sudah tersedia di `results/runs/`):
```powershell
# Windows (PowerShell)
.\scripts\run_all.ps1
```
```bash
# Linux / macOS (Bash)
./scripts/run_all.sh
```

---

## 4. Urutan Skrip Pipeline (01 → 14) & Estimasi Waktu

Pipeline eksekusi dibagi menjadi 13 skrip modular bernomor di dalam direktori `scripts/`:

| No | Skrip Eksekusi | Deskripsi / Tujuan Metodologis | Berkas Input Utama | Berkas Output Utama | Estimasi Waktu (Pilot) | Estimasi Waktu (Penuh) |
|:---:|:---|:---|:---|:---|:---:|:---:|
| **01** | `01_audit_data.py` | Audit kelengkapan & gap dataset mentah DJPPR (2017–2025) | `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` | `results/tables/audit_data.md`, `audit_data_gaps.csv` | ~5 detik | ~5 detik |
| **02** | `02_preprocess_data.py` | Pembersihan data, interpolasi spline, dan pemotongan jendela `intersection` | `data/raw/...` | `data/processed/market_*_intersection.csv` | ~10 detik | ~10 detik |
| **03** | `03_estimate_gbm_params.py` | Kalibrasi drift $\mu$ dan volatilitas $\sigma$ tahunan GBM (Pers. 2.1–2.2) | `data/processed/market_*_intersection.csv` | `data/processed/gbm_params_intersection.csv` | ~5 detik | ~5 detik |
| **04** | `04_generate_scenarios.py` | Pembangkitan bank skenario latih ($N=5.000$) dan validasi ($N=20.000$) | `data/processed/gbm_params_intersection.csv` | `bank_train_seed42_N5000.npz`, `bank_valid_seed2026_N20000.npz` | ~25 detik | ~25 detik |
| **05** | `05_benchmark_evaluator.py` | Benchmarking kecepatan dan akurasi evaluator risiko vectorized | `bank_train_seed42_N5000.npz` | `results/tables/evaluator_benchmark.md` | ~15 detik | ~15 detik |
| **06** | `06_compute_limits_and_baseline.py` | Hitung batas risiko $\tau,\eta$ portofolio $w_0$ & sampling 1.000 acak DJPPR | `bank_train_seed42_N5000.npz` | `risk_limits_*.json`, `baseline_djppr_*.csv` | ~1.5 menit | ~1.5 menit |
| **07** | `07_run_kma_smoke.py` | Uji coba fungsi (smoke test) algoritma KMA 2-fase | `configs/params.yaml`, `bank_train_*.npz` | Log konvergensi KMA di terminal | ~25 detik | ~25 detik |
| **08** | `08_compare_optimizers.py` | Komparasi awal KMA, GA, dan PSO pada anggaran mini | `bank_train_*.npz` | Ringkasan perbandingan awal | ~40 detik | ~40 detik |
| **09** | `09_run_audit_check.py` | Verifikasi kepatuhan kode vs formula matematis model (§2–§8) | Kode sumber `src/mccar_kma/` | 12/12 uji verifikasi internal PASS | ~10 detik | ~10 detik |
| **10** | `10_run_experiments.py` | Pelari eksperimen optimasi (mode pilot: 2 run, mode penuh: 360 run) | `configs/params.yaml`, `bank_train_*.npz` | `results/runs/<config_id>/<algo>/rep_*.json`, `runs_summary.csv` | ~1–2 menit | ~3–5 jam (4 worker) |
| **12** | `12_validate_solutions.py` | Validasi independen solusi optimal pada bank skenario $N=20.000$ | `results/tables/runs_summary.csv`, `bank_valid_*.npz` | `results/tables/validation_all_runs.csv`, `validation_summary.md` | ~45 detik | ~1 menit |
| **13** | `13_analyze_stats.py` | Analisis inferensial: Kruskal-Wallis, $\epsilon^2$, Dunn-Holm, Rank-Biserial | `results/tables/runs_summary.csv` | `results/tables/stats_*.csv`, `tab_stats_*.tex` | ~15 detik | ~15 detik |
| **14** | `14_make_figures_tables.py` | Pembuatan 18 pasang gambar (PDF+PNG 300 dpi) dan tabel LaTeX booktabs | Berkas hasil `results/` | `results/figures/fig_*.pdf/.png`, `results/tables/tab_*.tex` | ~20 detik | ~20 detik |

---

## 5. Pengujian Unit Matematis (Test Suite)

Repositori ini dilengkapi suite pengujian otomatis berbasis `pytest` untuk memvalidasi kendala simpleks bobot, kontinuitas diferensial penalti, fungsi risiko CCaR/MCCaR, kalibrasi GBM, keadilan inisialisasi optimizer, formula uji non-parametrik, dan integritas visualisasi:

```bash
# Menjalankan seluruh pengujian unit
pytest -v

# Menjalankan pengujian analitik dan visualisasi saja
pytest tests/test_viz.py tests/test_stats.py tests/test_validation.py -v
```
*(Seluruh 15 unit test terverifikasi 100% lulus).*

---

## 6. Struktur Direktori Repositori

```
ta-mccar-kma/
├── configs/
│   └── params.yaml                  # Konfigurasi parameter model, skenario, dan algoritma
├── data/
│   ├── raw/                         # READ-ONLY: Dataset historis mentah DJPPR 2017-2025
│   ├── interim/                     # Data antara pembersihan
│   └── processed/                   # Data bersih, parameter GBM, bank latih & validasi
├── docs/
│   ├── context/
│   │   └── spesifikasi_model.md     # Sumber kebenaran matematis model TA
│   ├── decisions/                   # Log keputusan terbuka D1 s.d. D9 (README.md)
│   ├── proposal/                    # Dokumen proposal PDF pasca-sempro
│   └── reviews/                     # Laporan audit kode independen
├── results/
│   ├── figures/                     # 18 pasang grafik publikasi (PDF vektor + PNG 300 dpi)
│   ├── tables/                      # 8 tabel LaTeX booktabs + CSV rekapitulasi data
│   ├── runs/                        # 360 berkas JSON log optimasi per replikasi
│   └── MANIFEST.md                  # Manifes kriptografis SHA-256 seluruh hasil
├── scripts/
│   ├── run_all.ps1                  # Skrip pelari otomatis lengkap (Windows PowerShell)
│   ├── run_all.sh                   # Skrip pelari otomatis lengkap (Linux/macOS Bash)
│   ├── build_manifest.py            # Pembangkit berkas MANIFEST.md
│   └── 01_... s.d. 14_...           # Skrip pipeline bertahap
├── src/mccar_kma/                   # Pustaka utama model optimasi (src-layout)
│   ├── analysis/                    # stats_tests.py, summary.py, validation.py
│   ├── data/                        # cleaning.py, interpolation.py, loader.py
│   ├── experiments/                 # io.py, runner.py, seeds.py
│   ├── model/                       # constraints.py, limits.py, penalty.py
│   ├── optimizers/                  # base.py, kma.py, ga.py, pso.py
│   ├── risk/                        # ccar.py, evaluator.py, mccar.py
│   ├── scenarios/                   # cost.py, estimation.py, gbm.py
│   └── viz/                         # figures.py, style.py
├── tests/                           # Berkas pengujian unit pytest
├── requirements.lock                # Pinning versi dependensi eksak
└── pyproject.toml                   # Metadata paket Python resmi
```

---

## 7. Integritas dan Manifes Hasil Penelitian

Semua berkas hasil simulasi, validasi, grafik, dan tabel LaTeX dienkripsi dengan nilai hash kriptografis **SHA-256** untuk menjamin keaslian data tanpa modifikasi manual. Silakan merujuk ke berkas:
👉 **[results/MANIFEST.md](results/MANIFEST.md)**.

Log seluruh keputusan metodologis tercatat rapi di:
👉 **[docs/decisions/README.md](docs/decisions/README.md)**.
