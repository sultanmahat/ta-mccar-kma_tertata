# TA — Optimasi Portofolio Utang Negara Multivaluta (MCCaR + KMA)

Sultan Bakri Baihaqi Mahat (5002221016) · Departemen Matematika FSAD-ITS · Pembimbing: Prof. Dr. Mohammad Isa Irawan, MT

Proposal revisi pasca-sempro (disetujui): `docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf`.

---

## 1. Tujuan Proyek

Proyek ini bertujuan mengoptimalkan portofolio utang negara multivaluta (7 instrumen utang valas berbunga tetap: USD, EUR, JPY) menggunakan pendekatan **Marginal Conditional Cost at Risk (MCCaR)** dan algoritma metaheuristik **Komodo Mlipir Algorithm (KMA)**, serta membandingkannya dengan **Genetic Algorithm (GA)** dan **Particle Swarm Optimization (PSO)** pada bank skenario Geometric Brownian Motion (GBM) yang identik.

---

## 2. Cara Setup Lingkungan Kerja

Proyek ini menggunakan **Python 3.11+** dengan layout direktori berbasis `src-layout`.

### a. Membuat Virtual Environment & Aktivasi

```bash
# Membuat virtual environment
python -m venv .venv

# Aktivasi di Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Aktivasi di Linux/macOS
source .venv/bin/activate
```

### b. Instalasi Dependensi & Paket (Editable Mode)

```bash
pip install --upgrade pip
pip install -e ".[dev]"
```

### c. Menjalankan Pengujian (Pytest)

```bash
pytest -v
```

---

## 3. Peta Folder Proyek

```
ta-mccar-kma/
├── AGENTS.md                        # Aturan kerja agen AI & standar pengerjaan
├── README.md                        # Dokumentasi ringkas proyek & instruksi setup
├── pyproject.toml                   # Konfigurasi paket & dependensi resmi
├── .gitignore                       # Aturan ignore git
├── configs/
│   └── params.yaml                  # Seluruh parameter model (§6, §7, §8) & keputusan terbuka
├── data/
│   ├── raw/                         # READ-ONLY: Dataset asli DJPPR
│   ├── interim/                     # Data hasil antara
│   └── processed/                   # Data bersih, parameter GBM, bank skenario
├── docs/
│   ├── context/                     # spesifikasi_model.md (sumber kebenaran model)
│   ├── proposal/                    # READ-ONLY: proposal PDF
│   ├── references/                  # READ-ONLY: pustaka rujukan
│   ├── decisions/                   # Catatan keputusan resmi (0001-..., 0002-...)
│   └── reviews/                     # Laporan audit & review berkala
├── report/
│   ├── proposal_latex/              # LaTeX proposal
│   └── skripsi_latex/               # LaTeX skripsi
├── legacy/                          # READ-ONLY: kode & data versi lama (hanya referensi)
├── src/mccar_kma/                   # Kode sumber utama (src-layout)
│   ├── data/                        # loader, cleaning, interpolation
│   ├── scenarios/                   # estimation, gbm, cost
│   ├── risk/                        # ccar, mccar, evaluator
│   ├── model/                       # constraints, penalty, limits
│   ├── optimizers/                  # base, kma, ga, pso
│   ├── experiments/                 # runner, seeds, io
│   ├── analysis/                    # summary, stats_tests, validation
│   ├── viz/                         # style, figures
│   └── utils/                       # config, logging
├── scripts/                         # Pipeline eksekusi bertahap (01_..., 02_..., dst.)
├── tests/                           # Pengujian unit & matematis (pytest)
├── notebooks/                       # Eksplorasi saja (bukan untuk pipeline)
├── results/
│   ├── runs/<config_id>/<algo>/     # JSON log per replikasi
│   ├── tables/                      # Rekap tabel CSV/TeX
│   └── figures/                     # Grafik PDF/PNG
└── logs/                            # File log eksekusi
```

---

## 4. Urutan Pipeline Skrip (`scripts/`)

Pipeline dijalankan secara bertahap menggunakan skrip bernomor:
*(Akan diperbarui bertahap seiring berjalannya tahapan proyek)*

1. `01_audit_data.py`: Audit dan validasi integritas dataset asli DJPPR.
2. `02_preprocess_data.py`: Pembersihan data, interpolasi spline, dan pemotongan jendela analisis.
3. `03_estimate_gbm_params.py`: Estimasi parameter $\mu, \sigma$, matriks korelasi Cholesky, dan statistik biaya historis.
4. `04_generate_scenarios.py`: Pembangkitan bank skenario stokastik GBM (bank latih $N=5.000$ dan bank validasi $N=20.000$).
5. `05_benchmark_evaluator.py`: Benchmark kinerja komputasi evaluator risiko portofolio MCCaR/CCaR.
6. `06_compute_limits_and_baseline.py`: Perhitungan batas risiko acuan ($\eta, \tau$), replikasi baseline acak DJPPR (1.000 sampel), dan optimasi referensi SLSQP.
7. `07_run_experiments.py`: Eksekusi eksperimen optimasi metaheuristik (KMA, GA, PSO).
8. `08_statistical_analysis.py`: Uji statistik komparasi (Kruskal-Wallis, Dunn-Holm).
9. `09_generate_reports.py`: Pembangkitan tabel dan grafik hasil untuk laporan skripsi.
