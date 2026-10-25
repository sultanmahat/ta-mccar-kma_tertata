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
