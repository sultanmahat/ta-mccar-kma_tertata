# Keputusan D10: Perlakuan Ketidakpastian Monte Carlo pada Batas Risiko (η, τ)

- **Tanggal Usulan**: 2026-10-24 (referensi dicatat di `configs/params.yaml` blok `sensitivity_limits`, Tahap 17)
- **Tanggal Konfirmasi**: 2026-10-25
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi C (Pertahankan Bank Seed 42, Laporkan Ketidakpastian sebagai Keterbatasan)**

---

## Ringkasan Keputusan

Batas risiko η = J_MCCaR(w0) dan τ = CCaR(w0) di 360 run eksperimen utama dihitung **sekali** dari portofolio eksisting pada satu bank latih (seed 42, N = 5.000), lalu dipakai sebagai kendala optimasi. Studi stabilitas limit (Tahap 17, `scripts/17_analyze_limit_stability.py`, 20 bank latih independen seed 10000–10019) mengukur seberapa besar galat Monte Carlo pada batas ini dan dampaknya ke penghematan, bobot, dan kelayakan validasi — lihat `docs/reviews/studi_stabilitas_limit.md`.

Ditetapkan:
1. **Batas risiko (η, τ) tetap dihitung dari bank seed 42**, konsisten dengan desain proposal yang sudah disetujui. **360 run eksperimen utama tidak diulang.**
2. Temuan Tahap 17 — terutama bahwa η (definisi biaya *interest*) punya variabilitas antar-bank terbesar (CV 4,34%), bank 42 adalah outlier longgar pada metrik ini (z = 3,44), dan solusi `interest_free` hanya tetap layak di 1–2 dari 20 bank independen saat divalidasi dengan batas presisi tinggi — **dilaporkan sebagai keterbatasan metodologis** di Bab 4/5 naskah skripsi, bukan dipakai untuk merevisi angka 360 run.
3. Konfigurasi `interest_djppr`, `gross_djppr`, dan `gross_free` tidak menunjukkan masalah stabilitas sebesar `interest_free` (kelayakan validasi 40–100% vs 5–10%) — catatan keterbatasan difokuskan ke `interest_free`.

---

## Alasan & Justifikasi Keputusan

1. **Konsistensi terhadap desain yang disetujui**: mengganti batas ke statistik multi-bank (Opsi B pada laporan) berarti mengubah definisi masalah optimasi di Tabel 3.1 dan mengulang 360 run — di luar cakupan yang disetujui komisi pembimbing, dan tidak diajukan tanpa persetujuan terpisah.
2. **Keterbukaan terhadap keterbatasan empiris**: dibanding mengabaikan temuan (Opsi A murni) atau mengulang eksperimen (Opsi B), melaporkan ketidakpastian secara eksplisit menjaga integritas angka 360 run sekaligus jujur soal generalisasinya — sejalan dengan pola D11.
3. **Proporsionalitas**: masalah stabilitas terkonsentrasi pada satu kombinasi (biaya *interest*, batas *free*), bukan menyeluruh — tidak sepadan dengan biaya mengulang seluruh 360 run (120 run × 4 konfigurasi) untuk masalah yang spesifik-konfigurasi.

---

## Implikasi ke Dokumen & Kode

1. `configs/params.yaml` blok `experiments`/`scenarios` (termasuk `train_seed: 42`) **tidak berubah**. Blok `sensitivity_limits` (Tahap 17) dipertahankan sebagai studi tambahan, bukan pengganti desain utama.
2. 360 run (`results/runs/`, `results/tables/`), dan 360 run yang dipakai Tahap 17/18 sebagai referensi, **tidak diubah** (diverifikasi hash SHA-256 sebelum/sesudah Tahap 17 dan 18).
3. Bab 4/5 naskah skripsi mencantumkan ringkasan Tahap 17 (`docs/reviews/studi_stabilitas_limit.md` Bagian 2–4) sebagai subbab keterbatasan/analisis sensitivitas, dengan penekanan pada konfigurasi `interest_free`.

---

## Addendum 2026-10-25 — Koreksi dasar angka (temuan T3 audit ulang) dan konfirmasi ulang Opsi C

**Konteks.** Audit ulang (`docs/reviews/audit_ulang_2026-10-25.md`, temuan T3) menemukan bahwa butir 3 di atas memakai angka dari solusi yang dioptimasi di 20 bank Tahap 17, bukan dari solusi 360 run. Tahap 21 (`scripts/21_validate_true_limits.py`) mengevaluasi langsung 360 solusi utama pada bank validasi N = 20.000 terhadap batas "benar" dari w0 pada bank yang sama (η_v = 0,149065, τ_v = 0,064173 untuk *interest*; η_v = 0,067652, τ_v = 1,085888 untuk *gross*; cocok dengan Tahap 17 dengan selisih relatif ≤ 8,2×10⁻¹⁶). Sumber angka: `results/tables/validation_true_limits_summary.csv`.

| Konfigurasi | KMA | GA | PSO | v_J maks (relatif) |
|---|---:|---:|---:|---:|
| `gross_free` | 27/30 | 30/30 | 29/30 | 0,0056 |
| `gross_djppr` | 24/30 | 10/30 | 17/30 | 0,00082 |
| `interest_free` | 0/30 | 0/30 | 0/30 | 0,2127 |
| `interest_djppr` | 30/30 | 30/30 | 30/30 | 0 |

Semua pelanggaran berasal dari kendala J (dispersi rasio MCCaR); tidak ada pelanggaran CCaR.

**Koreksi butir 3.** Rentang "40–100%" tidak tepat: `gross_djppr` GA hanya 10/30 (33%). Namun pelanggaran pada `gross_*` berukuran sangat kecil (v_J ≤ 0,56%), sedangkan pada `interest_free` seluruh 90 solusi melanggar dengan besaran sampai 21%. Kesimpulan arahnya tetap: masalah stabilitas terkonsentrasi pada `interest_free`, tetapi solusi `gross_djppr` juga berada sangat dekat batas J sehingga kelayakannya sensitif terhadap estimasi η.

**Keputusan.** Opsi C **dipertahankan** (dikonfirmasi Sultan pada 2026-10-25 melalui persetujuan rekomendasi plan "D10 Opsi A: addendum, tanpa membuka ulang"). Temuan di atas justru memperkuat alasan Opsi C: yang dibutuhkan adalah pelaporan ketidakpastian, bukan pengulangan 360 run. Implikasi tambahan:
1. Bab 4 subbab validasi *out-of-sample* menyajikan dua tabel kelayakan berdampingan: terhadap batas bank latih (Tahap 12) dan terhadap batas benar (Tahap 21), beserta besaran pelanggaran.
2. Headline penghematan `interest_free` tidak boleh disajikan tanpa catatan bahwa solusinya tidak layak terhadap batas η presisi tinggi.
3. Tidak ada angka 360 run yang berubah.
