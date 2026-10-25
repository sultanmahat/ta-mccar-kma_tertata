# Studi Stabilitas Batas Risiko (η, τ) Antar Bank Latih Independen

**Tahap**: 17 (`scripts/17_analyze_limit_stability.py`)
**Tanggal run**: 2026-10-25 11:15–11:33 WIB, 1.070,7 detik, 10 worker, 0 tugas gagal
**Config hash**: dicatat per run di `results/sensitivity/limits/runs/**/*.json` (`metadata.config_hash`)
**Data mentah**: `results/sensitivity/limits/*.csv`, `runs/<config>/<algo>/bank_*.json`
**Verifikasi**: preflight lulus — bank seed 42 yang dibangun ulang oleh studi ini identik bit-by-bit dengan `data/processed/bank_train_seed42_N5000.npz`. `pytest tests/test_limit_stability.py` — 9 test baru lulus, termasuk cek bahwa η dan τ hasil hitung ulang bank 42 sama persis dengan `risk_limits_bank_train_seed42_N5000.json`. Hash SHA-256 431 file `results/runs/`, `results/tables/`, `results/figures/` identik sebelum/sesudah — **360 run utama tidak diubah**.

> **Cara baca**: studi ini mengukur galat Monte Carlo pada batas risiko (η = J_MCCaR(w0), τ = CCaR(w0)) yang di eksperimen utama dihitung sekali dari bank seed 42, lalu dipakai sebagai kendala. Pertanyaannya bukan "apakah bank 42 salah" — bank 42 tetap pilihan sah sesuai proposal — tapi seberapa jauh angka hasil (penghematan, kelayakan, peringkat algoritma) akan bergeser kalau bank latihnya diganti dengan draw independen lain.

---

## 1. Desain

- **B = 20 bank latih independen**, seed 10000–10019 (terpisah dari 42, 2026, dan seed eksperimen lain).
- Tiap bank: hitung η_b, τ_b dari w0 (Persamaan 2.22), lalu optimasi **PSO dan GA** (1 replikasi, anggaran 25.000 eval sama dengan eksperimen utama) pada 4 konfigurasi (gross/interest × free/djppr), pakai batas bank sendiri.
- **Evaluasi validasi** tiap solusi pada bank independen N=20.000 (seed 2026, dipakai read-only) dengan dua batas:
  - **(A) batas sendiri** — η_b, τ_b dari bank tempat solusi dioptimasi;
  - **(B) batas "benar"** — η_v, τ_v dari w0 dihitung di bank validasi N=20.000.
- KMA tidak diikutkan (`sensitivity_limits.algorithms = [pso, ga]`) — studi ini soal stabilitas batas, bukan perbandingan algoritma; KMA sudah dibahas tersendiri di Tahap 18.

---

## 2. Variabilitas batas antar bank

Sumber: `limits_summary.csv`, 20 bank.

| Biaya | Metrik | Mean | SD | CV% | Bank-42 | z bank-42 | Batas "benar" (valid, N=20k) |
|---|---|---|---|---|---|---|---|
| gross | η | 0,067841 | 0,002187 | 3,22% | 0,068194 | **0,16** | 0,067652 |
| gross | τ | 1,086762 | 0,000939 | 0,09% | 1,086023 | −0,79 | 1,085888 |
| interest | η | 0,151573 | 0,006577 | **4,34%** | 0,174188 | **3,44** | 0,149065 |
| interest | τ | 0,064422 | 0,000522 | 0,81% | 0,064969 | 1,05 | 0,064173 |

**Temuan kunci**: η (definisi biaya *interest*) adalah satu-satunya metrik dengan variabilitas antar bank yang besar (CV 4,34%) **dan** bank 42 adalah outlier jauh di ekor kanan (z = 3,44 — hanya ~0,03% probabilitas seberat ini di bawah normalitas). Tiga metrik lain (η gross, τ gross, τ interest) punya CV di bawah 3,3% dan bank 42 dalam rentang wajar (|z| < 1,1). Batas "benar" (dari bank validasi N=20.000, jauh lebih stabil karena N besar) untuk η interest = 0,149065 — **lebih rendah 14,3% dari nilai bank 42** (0,174188). Ini berarti: kendala J≤η yang dipakai di eksperimen utama untuk konfigurasi *interest* **lebih longgar** dari yang seharusnya kalau memakai estimasi presisi tinggi.

---

## 3. Dampak ke penghematan yang dilaporkan

Sumber: `summary_savings.csv` (rata-rata antar 20 bank, `savings_in` = penghematan di bank sendiri, `savings_val` = penghematan saat divalidasi dengan batas sendiri, `ref_bank42_median` = median 30 replikasi bank-42 dari 360 run utama, hanya dibaca).

| Config | Algo | Penghematan 20-bank (mean) | Median bank-42 (360 run) | Selisih |
|---|---|---|---|---|
| gross_djppr | ga/pso | 6,6% | 4,8% | bank-42 **lebih rendah** |
| gross_free | ga/pso | 56,6–58,5% | 50,9–51,0% | bank-42 **lebih rendah** |
| interest_djppr | ga/pso | 200,7% | 201,4% | ≈ sama |
| interest_free | ga/pso | 27,58–27,66% | **30,27–30,29%** | bank-42 **lebih tinggi** |

**Interest_free adalah satu-satunya konfigurasi di mana bank 42 melaporkan penghematan lebih besar dari rata-rata 20 bank independen** (30,27% vs 27,6%, selisih ~2,6 poin persentase) — konsisten dengan temuan Bagian 2: η interest di bank 42 adalah outlier longgar, jadi kendala di bank 42 lebih mudah dipenuhi dengan biaya lebih rendah. Untuk tiga konfigurasi lain, bank 42 justru melaporkan penghematan yang **lebih kecil** dari rata-rata — artinya bank 42 bukan "bank paling menguntungkan" secara sistematis, efeknya spesifik ke kombinasi (interest, η).

`optimism_gap_mean` (savings_in − savings_val, dampak memvalidasi dengan batas sendiri vs performa aktual) kecil di semua konfigurasi (|gap| ≤ 1,4 poin persentase) — jadi solusi yang ditemukan tidak "overfit" ke bank latihnya sendiri secara berarti; isu utamanya bukan optimisme internal, melainkan posisi bank 42 relatif terhadap populasi bank (Bagian 2).

---

## 4. Kelayakan validasi — temuan paling signifikan

Sumber: `summary_feasibility.csv`. `k_in` = layak terhadap batas yang dipakai saat optimasi (selalu 20/20, layak secara definisi karena itu kendala optimasinya). `k_own` = solusi tetap layak saat dievaluasi ulang di bank validasi N=20.000 pakai batas bank sendiri. `k_true` = layak terhadap batas "benar" (dari bank validasi).

| Config | Algo | k_own (dari 20) | k_true (dari 20) | CI 95% k_true |
|---|---|---|---|---|
| gross_djppr | ga/pso | 9 | 8 | [0,19 ; 0,64] |
| gross_free | ga/pso | 9–10 | 9 | [0,23 ; 0,68] |
| interest_djppr | ga/pso | 19 | **20** | [0,83 ; 1,00] |
| interest_free | ga | 5 | **1** | [0,001 ; 0,25] |
| interest_free | pso | 3 | **2** | [0,01 ; 0,32] |

**interest_free gagal validasi secara drastis**: hanya **1 dari 20 bank (GA)** dan **2 dari 20 (PSO)** yang solusinya tetap layak kendala J≤η ketika dievaluasi dengan batas "benar" presisi tinggi. Untuk `gross_djppr`/`gross_free`, tingkat kelayakan juga hanya ~40–50% (bukan 100%), tapi jauh tidak separah `interest_free`. Hanya `interest_djppr` yang stabil (19–20/20 layak) — konsisten dengan Bagian 2 (η dan τ interest_djppr tidak ekstrem di bank 42, dan batas relatif longgar untuk konfigurasi ini — lihat gap 25.000 KMA/PSO di Tahap 18 yang juga kecil untuk `interest_djppr`).

**Catatan interpretasi**: `k_in`=20/20 selalu, by construction (solusi dioptimasi untuk memenuhi batas bank sendiri, jadi infeasibility di `k_in` hanya terjadi kalau optimizer gagal konvergen). Jatuhnya ke `k_own` dan `k_true` murni dari varians Monte Carlo evaluasi ulang (m=250 ekor pada N=5.000 saat optimasi vs N=20.000 saat validasi) dan dari pergeseran batas itu sendiri — bukan dari kegagalan optimizer.

---

## 5. Stabilitas peringkat PSO vs GA

Sumber: `rank_stability.csv`. Win-Tie-Loss PSO vs GA (menang = biaya lebih kecil), toleransi seri relatif 1×10⁻⁸.

| Config | PSO menang (in-sample) | Wilcoxon p | Rel. diff rata-rata |
|---|---|---|---|
| gross_djppr | 20/20 | 2×10⁻⁶ | PSO 0,0009% lebih murah |
| gross_free | 18/20 | 0,012 | PSO 0,019% lebih mahal |
| interest_djppr | 13/20 (7 seri) | 2×10⁻⁶ | ≈0 (seri teknis, beda <1e-4%) |
| interest_free | 15/20 | 0,036 | PSO 0,11% lebih mahal |

Peringkat PSO vs GA relatif stabil antar bank: PSO menang mayoritas bank di `gross_djppr` dan `gross_free` (konsisten dengan 360 run utama di mana PSO juga unggul tipis), hasil serupa saat dievaluasi dengan batas validasi (kolom `space=validation`, tidak berubah pola). `interest_djppr` dominan seri (perbedaan di bawah presisi praktis). Tidak ada pembalikan peringkat drastis antar bank — kesimpulan algoritma mana lebih baik di 360 run utama **tidak bergantung secara sensitif** pada pilihan bank seed 42.

---

## 6. Korelasi optimisme dan dekomposisi varians

Sumber: `optimism_correlation.csv`, `variance_decomposition.csv`.

- Korelasi Spearman galat batas (η_b atau τ_b relatif terhadap rata-rata) vs penghematan in-sample: signifikan positif untuk `gross_free` (ρ=0,50–0,53, p<0,024) dan `interest_free` (ρ_η=0,62, p=0,0034, GA). Artinya: bank dengan batas η/τ kebetulan lebih longgar memang melaporkan penghematan lebih besar — sesuai intuisi, dan mengonfirmasi mekanisme di Bagian 3 bukan kebetulan statistik.
- `variance_decomposition.csv`: rasio SD-antar-bank terhadap SD-antar-replikasi-bank-42 sangat bervariasi (1,1× sampai >900×) — untuk GA rasio hampir selalu >25×, artinya **variasi akibat pilihan bank latih jauh lebih besar dari variasi akibat seed RNG optimizer pada bank yang sama**. Pengujian ulang dengan replikasi lebih banyak di bank 42 saja tidak akan menangkap sumber ketidakpastian yang dominan.

---

## 7. D10 — dikonfirmasi: Opsi C (2026-10-25)

**Status**: dikonfirmasi oleh Sultan Bakri Baihaqi Mahat pada 2026-10-25. Dicatat di `docs/decisions/0010-limit-stability-d10.md`. Opsi yang dipertimbangkan dipertahankan di bawah sebagai jejak alasan.

Pertanyaan yang dijawab: apakah batas risiko (η, τ) di 360 run eksperimen utama — dihitung sekali dari bank latih seed 42 — dipertahankan sebagai status quo, atau perlu prosedur lain mengingat temuan Bagian 2–4?

**Opsi A — Pertahankan bank seed 42 (status quo proposal).**
(+) Tidak mengubah 360 run; sesuai desain yang sudah disetujui; nol biaya tambahan.
(−) Bagian 4 menunjukkan untuk `interest_free`, solusi yang dilaporkan sebagai "layak" di eksperimen utama hanya akan tetap layak di ~5–10% bank latih independen lain — generalisasi hasil `interest_free` lemah.

**Opsi B — Ganti batas ke statistik multi-bank (mis. median 20 bank, atau bank validasi N besar) dan ulang 360 run.**
(+) Batas lebih presisi/stabil, terutama untuk η interest.
(−) Mengubah Tabel 3.1/desain yang disetujui; 360 run harus diulang (120 run × 4 konfigurasi); technically mengubah definisi masalah optimasi (bukan sekadar tuning algoritma).

**Opsi C — Pertahankan bank 42 (360 run tidak diulang), tapi laporkan ketidakpastian batas secara eksplisit di Bab 4/5.**
Tambahkan interval ketidakpastian batas (CV%, posisi bank-42 relatif ke populasi bank — Bagian 2) dan tingkat kelayakan validasi lintas-bank (Bagian 4) sebagai bagian dari pembahasan keterbatasan, khususnya untuk `interest_free`. Tidak mengubah angka 360 run, hanya menambah konteks interpretasi.
(+) Tidak mengubah desain yang disetujui; jujur mengenai keterbatasan tanpa biaya run ulang.
(−) Headline savings `interest_free` (30,27%) tetap dilaporkan sebagai angka utama, meski Bagian 3–4 menunjukkan itu mendekati titik paling optimis dari distribusi 20-bank, bukan titik tengahnya.

**Keputusan: Opsi C.** Konsisten dengan pola D11 (tidak mengubah 360 run yang sudah disetujui, melaporkan sensitivitas sebagai analisis tambahan bukan revisi hasil utama). `interest_djppr`, `gross_djppr`, `gross_free` tidak menunjukkan masalah besar (kelayakan validasi 40–100%, bukan 5–10%) — isu stabilitas batas terkonsentrasi di `interest_free`, jadi catatan keterbatasan di Bab 4/5 difokuskan ke konfigurasi itu saja.

---

## 8. Keterbatasan

- 1 replikasi per bank per algoritma (bukan 30 seperti 360 run utama) — dipilih karena fokus studi ini adalah variabilitas **antar-bank**, bukan antar-seed-RNG-optimizer (lihat Bagian 6, rasio varians menunjukkan antar-bank memang dominan, jadi pilihan ini masuk akal, tapi berarti estimasi `savings_in` per bank punya galat RNG optimizer tunggal yang tidak dirata-ratakan).
- KMA tidak diuji di studi ini (lihat `docs/reviews/diagnosis_kma.md` untuk KMA).
- Bank validasi (N=20.000, seed 2026) dipakai sebagai proksi "batas benar" — ini juga estimasi Monte Carlo (bukan nilai populasi eksak), hanya jauh lebih presisi (m=1.000 ekor vs m=250) daripada bank N=5.000.
- 20 bank (bukan lebih banyak) dipilih sesuai `configs/params.yaml`; CI bootstrap di `summary_savings.csv` mencerminkan ukuran sampel ini.
