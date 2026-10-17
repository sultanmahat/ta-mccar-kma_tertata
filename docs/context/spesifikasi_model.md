# Spesifikasi Model — TA Sultan (MCCaR + KMA)

Sumber kebenaran untuk seluruh pekerjaan kode. Diturunkan dari proposal revisi pasca-sempro (Bab 2–3) dan audit dataset. Nomor persamaan mengikuti proposal. Hal yang belum ditentukan ada di §12 (Keputusan Terbuka) dan TIDAK boleh diputuskan sendiri oleh agen.

## 1. Ringkasan

Mencari komposisi bobot `w` (7 instrumen utang valas berbunga tetap) yang meminimumkan biaya rata-rata portofolio pada bank skenario GBM, dengan kendala keseimbangan risiko marjinal (`J_MCCaR ≤ η`), risiko ekor (`CCaR ≤ τ`), `Σw = 1`, dan batas proporsi. Masalah diselesaikan dengan Komodo Mlipir Algorithm (KMA), dibandingkan dengan Genetic Algorithm (GA) dan Particle Swarm Optimization (PSO) pada bank skenario, kendala, dan anggaran evaluasi yang sama. Kebaruan: MCCaR yang di kajian DJPPR hanya dipakai menyaring 1.000 kombinasi acak, di sini dijadikan kendala dalam optimasi.

## 2. Data

File: `data/raw/Dataset_Utama_Optimum_Utang_Valas.xlsx` (read-only).

| Sheet | Isi |
|---|---|
| `Data IR` | Tanggal, 7 kolom yield (%), Kategori (Sebelum Covid / Covid / Setelah Covid) |
| `Data FX` | Tanggal, `FX_USD/EUR`, `FX_USD/JPY` = unit mata uang per 1 USD |
| `Data Awal` | Instrumen, mata uang, tenor, komposisi eksisting 2024, batas min, batas max |
| `Data IR_formula` | Duplikat `Data IR` — diabaikan |

Penanda data hilang: teks `#N/A N/A` dan `#N/A` → harus dibaca sebagai NaN.

Hasil audit awal (harus dikonfirmasi ulang di Tahap 1):
- 3.104 baris hari kerja, 1 Jan 2014 – 24 Nov 2025.
- `IR_JPY_5Y` baru tersedia sejak 3 Jul 2017 → awal jendela analisis. Jendela 3 Jul 2017 – 24 Nov 2025 = 2.191 baris.
- Di jendela itu satu-satunya data hilang: `IR_EUR_10Y`, 163 hari berurutan (1 Feb – 15 Sep 2021). Jadi 2.191 − 163 = 2.028 baris lengkap. Ini satu blok panjang, bukan celah hari libur.
- Semua yield dan kurs di jendela bernilai > 0 (yield minimum 0,521 pada `IR_JPY_5Y`), sehingga log-return dan GBM valid.
- Tidak ada celah hari libur (hari libur terisi nilai sebelumnya).
- `legacy/data_v0/ir_data_clean.csv` dan `fx_data_clean.csv` (2.028 baris) identik dengan irisan lengkap dari xlsx. Hasil Tahap 2 varian `intersection` harus cocok dengan keduanya. Dokumen rujukan teks (`.md`) tersedia di `docs/references/core/` dan `docs/references/prior_theses/`.

### Instrumen dan batas proporsi (Tabel 2.1, 2.2; presisi penuh dari `Data Awal`)

| i | Instrumen | Mata uang | Tenor | Kolom yield | Eksisting 2024 `w0` | lb | ub |
|---|---|---|---|---|---|---|---|
| 1 | USD_Fixed_5Y | USD | 5 | IR_USD_5Y | 0.459485835 | 0.425 | 0.490 |
| 2 | USD_Fixed_10Y | USD | 10 | IR_USD_10Y | 0.113620854 | 0.100 | 0.125 |
| 3 | USD_Fixed_30Y | USD | 30 | IR_USD_30Y | 0.147798763 | 0.130 | 0.165 |
| 4 | EUR_Fixed_7Y | EUR | 8 | IR_EUR_7Y | 0.143927407 | 0.130 | 0.155 |
| 5 | EUR_Fixed_10Y | EUR | 10 | IR_EUR_10Y | 0.024401992 | 0.015 | 0.030 |
| 6 | JPY_Fixed_5Y | JPY | 5 | IR_JPY_5Y | 0.066688212 | 0.050 | 0.085 |
| 7 | JPY_Fixed_10Y | JPY | 10 | IR_JPY_10Y | 0.044076937 | 0.030 | 0.055 |

`Σ w0 = 1`. Σlb = 0,88 dan Σub = 1,105 sehingga ruang layak batas DJPPR tidak kosong.
Dua skenario batas: `free` (0 ≤ wᵢ ≤ 1) dan `djppr` (tabel di atas).

## 3. Notasi dan biaya (Persamaan 2.1–2.3)

9 variabel pasar: 7 yield + 2 kurs (`X_USD/EUR`, `X_USD/JPY`, unit mata uang per USD).

```
q_{c,s} = 1                          , c = USD                                  (2.1)
        = X_{USD/c,0} / X_{USD/c,s}  , c ∈ {EUR, JPY}

C_{i,s}   = q_{c(i),s} · (1 + y_{i,s}/100)    biaya bruto  (definisi UTAMA)     (2.2)
C^I_{i,s} = q_{c(i),s} · (y_{i,s}/100)        biaya bunga  (SENSITIVITAS)       (2.3)

Cost_s(w)  = Σ_i w_i · C_{i,s}                biaya portofolio skenario s (linear dalam w)
Cost̄(w)    = (1/N) Σ_s Cost_s(w)                                                (2.15)
```

`X_0` = nilai kurs awal simulasi (observasi terakhir di jendela). Konvensi q: kurs naik (mata uang asing melemah terhadap USD) → q turun → biaya USD-ekuivalen turun. Model dijalankan dua kali: definisi bruto (utama) dan bunga (sensitivitas); keduanya punya pasangan (η, τ) sendiri.

## 4. Pembangkitan skenario (Persamaan 2.4–2.12)

Interpolasi natural cubic spline (2.4–2.6): `g_i(x) = a_i + b_i(x−x_i) + c_i(x−x_i)² + d_i(x−x_i)³`, `a_i = z_i`, syarat `c_1 = c_M = 0`, sistem tridiagonal
`h_{i−1}c_{i−1} + 2(h_{i−1}+h_i)c_i + h_i c_{i+1} = 3((z_{i+1}−z_i)/h_i − (z_i−z_{i−1})/h_{i−1})`, lalu
`b_i = (z_{i+1}−z_i)/h_i − (h_i/3)(2c_i + c_{i+1})`, `d_i = (c_{i+1}−c_i)/(3h_i)`. Dipakai hanya bila varian data `spline` dipilih (D1).

Statistik historis (2.7–2.10): `Δc_{i,t} = ln(C_{i,t}/C_{i,t−1})`, rata-rata `1/T Σ Δc`, varians dan kovarians dengan pembagi `T−1`, matriks Σ. Dilaporkan sebagai tabel deskriptif; bukan masukan GBM kecuali diputuskan lain (D2).

GBM (2.11–2.12), per variabel pasar `S`:

```
S_{t+Δt} = S_t · exp( (μ_S − ½σ_S²)·Δt + σ_S·√Δt · Z ),   Z ~ N(0,1)
```

- Estimasi dari log-change harian `r_t = ln(S_t/S_{t−1})` pada jendela analisis, 252 hari/tahun. Kalibrasi default yang diusulkan: `σ = s·√252`, `μ = 252·m + σ²/2` (m, s = rata-rata dan simpangan baku harian). Agen harus menjelaskan dan meminta persetujuan (D2).
- Guncangan berkorelasi: `Z = L·ε`, `L` = Cholesky matriks korelasi 9×9 dari `r_t`.
- `N = 5.000` skenario, horizon 1 tahun (252 hari), `S_0` = observasi terakhir jendela.
- Satu bank skenario dipakai SEMUA algoritma. Bank validasi independen: seed berbeda, ukuran lebih besar.
- Keterbatasan GBM (tidak ada mean reversion) dicatat di laporan; bukan alasan mengubah model.

## 5. Ukuran risiko (Persamaan 2.13–2.20)

```
α = 95%, N = 5000  →  m = ceil((1−α)·N) = 250
CCaR_α(w) = (1/m) Σ_{s ∈ S_α(w)} Cost_s(w)          S_α = indeks m biaya tertinggi    (2.13)

δ = 0.01
Cost_s^{(+i)}(w;δ) = Cost_s(w) + δ·C_{s,i}                                           (2.14)
MC_i(w)       = Cost̄^{(+i)}(w;δ) − Cost̄(w)        ( = δ·mean_s(C_{s,i}) )            (2.16)
MCCaR_{α,i}(w) = CCaR^{(+i)}_α(w;δ) − CCaR_α(w)                                       (2.17)
θ_i(w)  = MCCaR_{α,i}(w) / MC_i(w),   MC_i ≠ 0                                        (2.18)
θ̄(w)    = (1/n) Σ_i θ_i(w)                                                           (2.19)
J_MCCaR(w) = sqrt( (1/n) Σ_i (θ_i − θ̄)² )         (pembagi n, bukan n−1)             (2.20)
```

Aturan: himpunan ekor `S_α` dipilih ULANG pada biaya yang sudah ditambah `δ·C_{s,i}` (CCaR^{(+i)}). Portofolio awal dan portofolio tambahan dihitung pada bank skenario yang sama. Tambahan δ tidak diimbangi pengurangan instrumen lain (total 101%).

## 6. Model optimasi dan kendala (Persamaan 2.21–2.24)

```
min_w   Cost̄(w)
s.t.    J_MCCaR(w) ≤ η
        CCaR_α(w)  ≤ τ
        Σ_i w_i = 1
        lb_i ≤ w_i ≤ ub_i                                                             (2.21)

η = J_MCCaR(w0),   τ = CCaR_α(w0)          dihitung SEKALI pada bank latih, per definisi biaya  (2.22)
```

Penanganan kendala pada metaheuristik:
1. Proyeksi untuk `Σw = 1` dan batas proporsi: clip tiap bobot ke `[lb_i, ub_i]`, normalisasi ke jumlah 1, ulangi sampai keduanya terpenuhi dalam toleransi numerik `1e-8`.
2. Penalti kuadratik untuk J dan CCaR:

```
v_J(w) = max(0, (J_MCCaR(w) − η) / max(|η|, ε_tol))
v_R(w) = max(0, (CCaR_α(w) − τ) / max(|τ|, ε_tol))                                    (2.23)
f(w)   = Cost̄(w) + ρ_J·v_J(w)² + ρ_R·v_R(w)²,   ρ_J = ρ_R = 1e6,  ε_tol = 1e-8        (2.24)
```

3. Arsip solusi layak terpisah: solusi akhir adalah solusi layak terbaik di arsip (v_J ≤ ε_tol dan v_R ≤ ε_tol), BUKAN sekadar nilai f terendah.

## 7. Algoritma

Dimensi `D = 7`. Semua algoritma: anggaran 25.000 evaluasi fungsi per replikasi, bank skenario sama, proyeksi/penalti/arsip sama, seed replikasi sama.

### 7.1 KMA (Subbab 2.8, Algoritma 1)

Populasi dibagi tiga kelompok setelah diurutkan berdasarkan `f`:

```
n* = floor(p_bm · (n_pop − 1))
n_bm = min(max(n*, 2), n_pop − 3),   n_sm = n_pop − n_bm − 1,   1 female                 (2.25)

Big male i terhadap big male j:
  u_ij = r1·(k_j − k_i)   jika f(k_j) < f(k_i) atau r2 < 0,5
       = r1·(k_i − k_j)   lainnya                                                       (2.26)
  k_i' = k_i + Σ_{j≠i}^{q} u_ij                                                          (2.27)

Female (i) kawin dengan big male terbaik (j), per dimensi l:
  k'_il = r_l·k_il + (1−r_l)·k_jl ,   k'_jl = r_l·k_jl + (1−r_l)·k_il                    (2.28–2.29)
Partenogenesis:
  k'_il = k_il + (2r_l − 1)·γ·|ub_l − lb_l|                                              (2.30)

Small male i mengikuti big male j pada sebagian dimensi (mlipir rate d):
  u_ij,l = r1·(k_jl − k_il) jika r2 < d, selain itu 0                                    (2.31)
  k_i' = k_i + Σ_j u_ij                                                                  (2.32)
```

r1, r2, r_l ~ U(0,1). Setelah pembaruan: perbaiki batas (proyeksi §6), hitung kualitas, simpan terbaik, sesuaikan ukuran populasi.

Dua fase (Tabel 3.1):
- Fase 1: `n_pop = 5`, `d = (D−1)/D`, anggaran 5.000 evaluasi.
- Fase 2: `n_pop` awal 200, batas 20 ≤ n_pop ≤ 200, langkah `Δn`: membesar saat pencarian stagnan, mengecil saat membaik; sisa anggaran 20.000 evaluasi.

### 7.2 GA (Subbab 2.9.1)

`n_pop = 50`, seleksi turnamen ukuran 2, persilangan aritmetika peluang 0,9, mutasi Gaussian peluang `1/D` per dimensi dengan `σ_m = 0,1 × lebar rentang`.

```
x_l^{(c1)} = λ_l·x_l^{(p1)} + (1−λ_l)·x_l^{(p2)},   x_l^{(c2)} = λ_l·x_l^{(p2)} + (1−λ_l)·x_l^{(p1)},   λ_l ∈ [0,1]   (2.33–2.34)
x_l' = x_l + ε_l,   ε_l ~ N(0, σ_m²)
```

### 7.3 PSO (Subbab 2.9.2)

`n_pop = 50`, bobot inersia turun linear 0,9 → 0,4, `c1 = c2 = 1,49618`, `v_max,i = 0,2·(ub_i − lb_i)`.

```
v_i^{(t+1)} = ω·v_i^{(t)} + c1·r1 ⊙ (p_i − x_i^{(t)}) + c2·r2 ⊙ (g − x_i^{(t)})          (2.35)
x_i^{(t+1)} = x_i^{(t)} + v_i^{(t+1)}                                                    (2.36)
```

Setelah pembaruan, kandidat diproyeksikan ke kendala bobot (§6).

## 8. Desain eksperimen (Bab 3, Tabel 3.1)

| Komponen | Nilai |
|---|---|
| Bank skenario | 5.000, horizon 1 tahun, 252 hari |
| Kepercayaan / ekor | α = 95%, m = 250 |
| Tambahan penerbitan | δ = 0,01 |
| Anggaran evaluasi | 25.000 per replikasi |
| Replikasi | 30 per konfigurasi per algoritma, daftar seed sama |
| Penalti & toleransi | ρ_J = ρ_R = 1e6, ε_tol = 1e-8 |

Konfigurasi = definisi biaya {gross, interest} × batas {free, djppr} = 4 (`gross_free`, `gross_djppr`, `interest_free`, `interest_djppr`). Total 4 × 3 algoritma × 30 replikasi = 360 run, ± 9 juta evaluasi.
Acuan historis: 1.000 kombinasi bobot acak di dalam batas proporsi, disaring dengan kriteria J ≤ η dan CCaR ≤ τ (replikasi prosedur DJPPR).
Keluaran tiap run: bobot terbaik layak, Cost̄, CCaR, J, θ_i, status layak, jumlah evaluasi, waktu, kurva konvergensi.

## 9. Analisis statistik (Subbab 2.10)

Per konfigurasi, pada nilai objektif solusi layak terbaik tiap replikasi: ringkasan (terbaik, median, rata-rata, simpangan baku, IQR); asumsi Shapiro–Wilk (normalitas) dan Levene (homogenitas ragam); lalu

```
H = 12/(N(N+1)) · Σ_g R_g²/n_g − 3(N+1)                              Kruskal–Wallis       (2.37)
z_gh = (R̄_g − R̄_h) / sqrt( N(N+1)/12 · (1/n_g + 1/n_h) )            Dunn, koreksi Holm    (2.38)
ε² = H / (N − 1)                                                      ukuran efek           (2.39)
```

ditambah korelasi rank-biserial per pasangan algoritma.

## 10. Verifikasi dan validasi (Bab 3 langkah 11)

- CCaR dan MCCaR diuji pada kasus sintetis kecil yang jawabannya dihitung manual.
- Setiap solusi akhir diperiksa ulang: `Σw = 1`, batas proporsi, `J ≤ η`, `CCaR ≤ τ`, toleransi relatif 1e-8.
- Reproduksibilitas: seed yang dicatat harus mengulang hasil persis.
- Evaluasi ulang solusi terbaik pada bank validasi independen (seed berbeda, ukuran lebih besar). Pelanggaran kecil pada bank validasi adalah temuan yang dilaporkan, bukan bug.
- Konsistensi data, perhitungan risiko, pemenuhan kendala, dan reproduksibilitas diperiksa SEBELUM hasil ditafsirkan.

## 11. Catatan analitis (untuk sanity check, bukan target)

- Biaya linear dalam `w`, sehingga `MC_i = δ·mean(C_{s,i})` konstan terhadap `w`. Nonlinearitas masalah hanya berasal dari pemilihan skenario ekor (CCaR) dan kendala J/CCaR. Tes wajib: `MC_i` cocok dengan rumus ini persis.
- Dengan konvensi q di atas, perkiraan awal drift biaya per tahun: JPY ≈ −3,5% (termurah, volatilitas tertinggi), USD ≈ +0,1%, EUR ≈ +0,3%. Verifikasi di Tahap 3. Hasil optimasi TIDAK otomatis "100% USD 30Y".
- Tugas akhir pembanding (Irfan, Ida, Rico, Zalfa) memakai konvensi kurs dan metode risiko berbeda (arah JPY terbalik); hasilnya tidak bisa dibandingkan langsung angka-ke-angka.
- `w0` layak by construction pada kedua skenario batas (v = 0). Jangan memasukkan `w0` ke populasi awal algoritma kecuali disetujui (agar perbandingan adil).

## 12. Keputusan terbuka (agen TIDAK boleh memutuskan sendiri)

| ID | Keputusan | Opsi / catatan |
|---|---|---|
| D1 | Jendela data | (A) `intersection`: buang 163 baris, 2.028 baris, log-change yang melintasi blok dikeluarkan. (B) `spline`: isi EUR_10Y dengan natural cubic spline, 2.191 baris. Proposal menyebut 2.028 hari DAN interpolasi spline — keduanya tidak bisa sekaligus. Putuskan bersama pembimbing. Kendalikan lewat `data.window_mode`. |
| D2 | Spesifikasi GBM | Kalibrasi μ (§4), simulasi terminal vs jalur 252 langkah, dan definisi `C_{i,t}` historis (nilai `X_0`) untuk statistik Persamaan 2.7–2.10. |
| D3 | Ukuran bank validasi | Usulan N lebih besar dari 5.000 (mis. 20.000); seed berbeda. |
| D4 | Detail KMA yang tidak ditentukan | `p_bm`, `γ`, jumlah big male berinteraksi `q`, aturan kawin vs partenogenesis, definisi stagnasi, `Δn`, serah-terima fase 1 → 2. Usulkan nilai dengan rujukan Suyanto dkk. (2022). |
| D5 | Pembagian nol | Perlakuan `MC_i ≈ 0` pada θ_i, dan toleransi. |
| D6 | Detail GA/PSO | Elitisme GA, inisialisasi populasi (harus sama untuk ketiga algoritma), perlakuan kecepatan PSO saat bobot dipotong proyeksi, jadwal inersia terhadap jumlah evaluasi. |
| D7 | Ties pada uji Dunn | Dengan atau tanpa koreksi ties. |
| D8 | Cara membangkitkan 1.000 kombinasi acak DJPPR | Ikuti prosedur di jurnal DJPPR (`docs/references/`); bila tidak jelas, tanyakan. |
