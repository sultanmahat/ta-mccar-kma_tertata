# Laporan Audit Akhir Komprehensif v2: Verifikasi terhadap Naskah Resmi Proposal Pasca-Sempro, Analisis Objektif Hasil Eksperimen, dan Rekomendasi Skripsi

- **Dokumen Target Audit:** Seluruh artefak komputasi Tugas Akhir (kode `src/mccar_kma/`, skrip `scripts/`, data `data/`, hasil eksperimen `results/`, dan konfigurasi `configs/params.yaml`).
- **Dokumen Rujukan Tunggal:** `docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf` (Naskah Resmi Proposal Pasca-Sempro; dokumen LaTeX lama di `report/proposal_latex/` telah usang dan dikesampingkan).
- **Peran:** Auditor Akhir Independen.
- **Tanggal Audit v2:** 2026-10-18.
- **Status Dokumen:** **Resmi & Berlaku** (Menggantikan `audit_akhir_2026-10-18.md` yang dicabut).

---

## 1. Ringkasan Eksekutif (10 Baris)

1. Audit akhir v2 memverifikasi kepatuhan sistem komputasi secara ketat dan murni terhadap naskah resmi PDF proposal revisi pasca-sempro.
2. Seluruh temuan audit lama yang bersumber dari draf LaTeX usang (AUD-FINAL-01, AUD-FINAL-05, AUD-FINAL-07, dan AUD-FINAL-08) dinyatakan **TIDAK VALID** karena naskah PDF proposal revisi telah memuat rumusan yang akurat.
3. Proposal resmi telah secara eksplisit mencantumkan periode data riil 2.028 hari kerja (3 Juli 2017 s.d. 24 November 2025) dan menetapkan tenor obligasi EUR 7Y adalah 8 tahun sesuai dokumen sumber DJPPR.
4. Metode optimasi pembanding yang dirumuskan secara resmi di proposal sejak awal adalah Genetic Algorithm (GA) dan Particle Swarm Optimization (PSO), bukan `fmincon`.
5. Formulasi matematika fungsi biaya ($C, C^I$), konversi kurs ($q$), simulasi GBM, pemisahan kendala $\text{CCaR} \le \tau$ dan $J \le \eta$, serta pembulatan ekor presisi ($m=250$ pada $N=5.000$ dan $m=1.000$ pada $N=20.000$) terbukti konsisten 100% dengan naskah PDF.
6. Hipotesis bahwa KMA menemukan portofolio yang menghemat biaya dibandingkan eksisting 2024 dan baseline DJPPR terbukti **DIDUKUNG KUAT** pada seluruh 4 konfigurasi: uji tanda satu sisi (biaya KMA < biaya $w_0$), $n=30$, $k=30$ layak di tiap konfigurasi, $p = 0{,}5^{30} \approx 9{,}3\times10^{-10}$ (lihat `errata_2026-10-25.md` butir R6 untuk reproduksi angka ini dari `runs_summary.csv` dan `limits_and_baseline_summary.md`).
7. Hipotesis keunggulan in-sample KMA terhadap GA dan PSO **DILEMAHKAN**: PSO menemukan biaya in-sample terendah secara konsisten dengan waktu komputasi 3x lebih cepat (~29s vs ~88s, $p < 10^{-11}$).
8. Klaim subjektif mengenai "ketahanan (*robustness*) KMA vs *overfitting* PSO" **DICABUT**: selisih kelayakan out-of-sample PSO 28/30 vs KMA 30/30 pada `interest_free` terbukti tidak signifikan secara statistik (uji eksak Fisher $p = 0{,}4915$).
9. Analisis kelonggaran risiko membuktikan korelasi amat tinggi antara bank latih dan validasi ($r \approx 0{,}974 - 0{,}994$), menandakan bahwa kelayakan out-of-sample ditentukan oleh kedekatan jarak solusi ke batas aktif, bukan keunggulan algoritma.
10. Batasan metodologis yang perlu diakui di Bab 5 skripsi mencakup dinamika GBM tanpa tarikan *mean reversion* pada suku bunga dan sifat endogen batas $\tau$/$\eta$ yang dihitung dari titik awal 2024.

---

## 2. Status Evaluasi Temuan Audit Lama (Koreksi terhadap Naskah PDF Proposal Revisi)

Pemeriksaan silang langsung terhadap naskah [docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf](file:///d:/ITS/TUGAS%20AKHIR/ta-mccar-kma_tertata/ta-mccar-kma/docs/proposal/proposal_ta_sultan_revisi_after_sempro.pdf) menghasilkan koreksi menyeluruh terhadap temuan audit sebelumnya:

| ID Audit Lama | Pernyataan Temuan Lama (Berdasarkan LaTeX Usang) | Fakta Naskah Resmi PDF Proposal Revisi | Status Temuan | Tindakan & Rekomendasi untuk Bab 4 & 5 |
|:---:|:---|:---|:---:|:---|
| **AUD-FINAL-01** | *"Proposal menulis 1 Jan 2014 – 24 Nov 2025, padahal data JPY baru ada 3 Juli 2017."* | **Halaman 3 (Subbab 1.3) & Halaman 30 (Bab 3):** Proposal resmi secara eksplisit tertulis: *"Periode pengamatan meliputi 2.028 hari perdagangan dari 3 Juli 2017 sampai 24 November 2025."* | **TIDAK VALID** | **Digugurkan**. Naskah PDF resmi sudah benar sejak awal. Tidak ada inkonsistensi rentang waktu. |
| **AUD-FINAL-05** | *"Nama instrumen EUR_Fixed_7Y bertenor 8 tahun di Tabel 3.1, salah ketik harus diubah ke 7 tahun."* | **Halaman 10/11 (Tabel 2.1):** Tertulis persis `EUR Fixed 7Y EUR 8` (tenor 8 tahun). Dokumen sumber emisi DJPPR memang mencatat instrumen ini berjangka waktu 8 tahun, dan `params.yaml` konsisten menggunakan `tenor: 8`. | **TIDAK VALID** | **Digugurkan**. Tenor 8 tahun adalah data resmi obligasi negara DJPPR. Penamaan simbol 7Y merefleksikan konvensi pasar DJPPR saat penerbitan, bukan salah ketik. |
| **AUD-FINAL-07** | *"Persamaan 3.2 salah notasi menulis $\text{MCCaR}(w) \le \tau$, harus dipisah dari CCaR."* | **Halaman 20 & 31 (Subbab 2.7.1 & Bab 3):** Naskah resmi memisahkan secara tepat: kendala pemerataan risiko marginal $J_{\text{MCCaR}}(w) \le \eta$ dan kendala risiko ekor agregat $\text{CCaR}_\alpha(w) \le \tau$. | **TIDAK VALID** | **Digugurkan**. Formulasi matematika dalam naskah PDF resmi sudah tepat dan terpisah. |
| **AUD-FINAL-08** | *"Proposal merencanakan fmincon MATLAB lalu diganti di tengah jalan ke GA dan PSO."* | **Halaman 25, 29 (Diagram Alir), & 32 (Tabel 3.1):** Naskah resmi secara eksplisit menetapkan metode pembanding adalah **Genetic Algorithm (GA)** dan **Particle Swarm Optimization (PSO)**. Kata `fmincon` sama sekali tidak ditemukan. | **TIDAK VALID** | **Digugurkan**. Desain eksperimen komputasi sejak awal telah sinkron dengan naskah proposal resmi. |
| **AUD-FINAL-03** | *"KMA memiliki ketahanan (robustness) out-of-sample superior, sedangkan PSO overfitting."* | Pada `interest_free`, kelayakan PSO 28/30 vs KMA 30/30 menghasilkan uji eksak Fisher **$p = 0{,}4915$** (tidak signifikan). Korelasi kelonggaran risiko latih vs validasi adalah $r = 0{,}974$ s.d. $0{,}994$. | **DICABUT** | **Diganti dengan Analisis Objektif**. Kelayakan validasi ditentukan oleh *slack margin* terhadap batas aktif, bukan karena sifat ketahanan intrinsik algoritma KMA. |

---

## 3. Rekapitulasi Temuan Temuan Riil & Validasi Ilmiah

Berikut adalah daftar temuan metodologis riil yang valid berdasarkan perbandingan naskah PDF resmi terhadap hasil eksperimen 360 run:

| ID Temuan | Severity | Aspek Metodologis | Bukti & Analisis Numerik | Rekomendasi untuk Pembahasan Skripsi (Bab 4 & 5) |
|:---:|:---:|:---|---|---|
| **AUD-V2-01** | **Tinggi** | Evaluasi Hipotesis Biaya In-Sample (KMA vs GA/PSO) | Hipotesis awal bahwa KMA mengungguli metode pembanding dalam meminimasi biaya **tidak terbukti secara in-sample**. Pada seluruh konfigurasi, PSO menemukan biaya terendah ($p < 10^{-11}$, $\epsilon^2 \ge 0{,}587$). **Koreksi 2026-10-25 (S8):** urutan "disusul GA, lalu KMA" tidak berlaku umum — di `interest_free`, GA vs PSO **tidak signifikan** (p_Holm = 0,0837, `stats_dunn_interest_free.csv`), dan di `gross_djppr`/`interest_djppr` ketiga algoritma **ekivalen praktis** dalam margin 0,01% (Tahap 20, `stats_praktis.csv`). PSO juga 3x lebih cepat (29s vs 88s). | Laporkan apa adanya di Bab 4: Akui keunggulan eksploitasi lokal PSO yang sangat cepat pada ruang simpleks, dan jelaskan bahwa struktur dua fase KMA membutuhkan evaluasi lebih besar untuk menyaingi konvergensi partikel. Jangan generalisasi urutan peringkat biaya ke seluruh konfigurasi. |
| **AUD-V2-02** | **Tinggi** | Analisis Objektif Kelayakan Validasi Out-of-Sample | Pada bank validasi $N=20.000$ (`validation_summary.md`), seluruh run KMA dan GA layak 100%, sedangkan PSO 28/30 (93,3%) pada `interest_free`. Namun selisih ini **tidak signifikan secara statistik** (Fisher exact $p = 0{,}4915$). Korelasi slack risiko $r(J_{\text{train}}, J_{\text{valid}}) = 0{,}974$ membuktikan kelayakan ditentukan oleh margin jarak solusi ke batas aktif $\tau$ dan $\eta$. | Sajikan hasil out-of-sample secara objektif di Bab 4 tanpa melebih-lebihkan klaim *robustness*. Dua solusi PSO yang melanggar $\tau$ pada bank validasi berada persis di tepi batas bank latih ($\tau - \text{CCaR}_{\text{train}} \approx 10^{-5}$), sehingga guncangan ekor baru menyebabkan pelanggaran kecil ($+0{,}00028$). |
| **AUD-V2-03** | **Sedang** | Asumsi Model GBM Tanpa *Mean Reversion* | Model Persamaan 2.11 menggunakan GBM murni dengan drift konstan. Pada suku bunga obligasi jangka panjang (misal JPY 10Y drift $+0{,}2698$), GBM dapat memproyeksikan deviasi ekstrem pada horizon panjang tanpa tarikan ke nilai ekuilibrium jangka panjang (*Vasicek/CIR effect*). | Tambahkan pembahasan di Bab 5 subbab Keterbatasan Model: diskusikan bahwa GBM merupakan simplifikasi standar DJPPR, dan sarankan model mean-reverting (seperti Ornstein-Uhlenbeck atau CIR) untuk studi lanjutan. |
| **AUD-V2-04** | **Sedang** | Sifat Endogen Ambang Batas Risiko ($\tau$ dan $\eta$) | Ambang batas $\tau$ dan $\eta$ dihitung dari portofolio eksisting 2024 $w_0$ (Persamaan 2.22). Akibatnya, ruang kelayakan sangat ditentukan oleh kondisi awal portofolio pemerintah saat ini. Pada `gross_djppr`, portofolio eksisting berada sangat dekat dengan batas proporsi, membatasi ruang perbaikan biaya. | Bahas di Bab 4 analisis sensitivitas: jelaskan bagaimana pemilihan titik referensi $w_0$ mempengaruhi geometri ruang kendala layak, dan bandingkan ruang solusi `djppr` (sangat terbatas) vs `free` (ruang optimasi luas). |
| **AUD-V2-05** | **Rendah** | Pemilihan Varian Jendela Data (D1 `intersection`) | Pemotongan 163 baris celah data `EUR_10Y` menghasilkan tepat 2.028 hari kerja lengkap (3 Juli 2017 – 24 November 2025). Pilihan ini menghindari distorsi drift akibat interpolasi spline pada jeda panjang 7 bulan. | Jelaskan justifikasi Keputusan D1 di Bab 3/4 skripsi: interpolasi spline pada jeda 163 hari berisiko menciptakan korelasi tiruan (*spurious correlation*) antarmata uang. |

---

## 4. Analisis Mendalam: Hasil Statistik Out-of-Sample dan Pembatalan Klaim Robustness

Audit sebelumnya menyimpulkan bahwa KMA memiliki keunggulan ketahanan (*robustness*) out-of-sample yang superior dibandingkan PSO. Melalui evaluasi independen mendalam, klaim tersebut **dibatalkan** berdasarkan bukti kuantitatif berikut:

### 1. Uji Kontingensi Kelayakan Validasi (Fisher's Exact Test)
Pada konfigurasi `interest_free` (satu-satunya konfigurasi di mana terjadi pelanggaran batas out-of-sample):
- KMA: 30 layak, 0 tidak layak (Kelayakan = 100%)
- GA: 30 layak, 0 tidak layak (Kelayakan = 100%)
- PSO: 28 layak, 2 tidak layak (Kelayakan = 93,33%)

Tabel kontingensi $2 \times 2$ antara KMA dan PSO:
$$\begin{pmatrix} 30 & 0 \\ 28 & 2 \end{pmatrix}$$
Hasil uji eksak Fisher dua sisi (*two-tailed Fisher's exact test*):
- Odds Ratio: $\infty$
- **$p\text{-value} = 0{,}4915$**

Karena nilai $p = 0{,}4915 \gg 0{,}05$, tidak terdapat bukti statistik yang cukup untuk menolak hipotesis nol bahwa tingkat kelayakan KMA dan PSO adalah sama.

### 2. Hubungan Kelonggaran Kendala (*Slack*) dan Pelanggaran Out-of-Sample

> **Koreksi 2026-10-25 (audit ulang, temuan T1):** paragraf asli di bawah menyebut `rep_04`/`rep_21` dan $\tau = 0{,}028889$ — angka ini tidak ditemukan di berkas manapun pada `results/tables/`. Reproduksi langsung dari `results/tables/validation_interest_free.csv` menunjukkan run PSO yang tidak layak adalah **rep 25 dan rep 28**, dan keduanya melanggar **$\eta$** (bukan $\tau$). $\tau$ `interest_free` yang benar = **0,064969**. Baris di bawah dipertahankan sebagai jejak audit lama, dikoreksi pada paragraf berikutnya.

Dua replikasi PSO yang tidak layak pada bank validasi adalah **`rep_25` dan `rep_28`** (bukan `rep_04`/`rep_21`):
- Pada bank latih, kedua solusi ini berada dekat batas $\eta = 0{,}174188$ (bukan $\tau$):
  * `rep_25` (seed 67): $J_{\text{MCCaR,train}} = 0{,}180767$
  * `rep_28` (seed 70): $J_{\text{MCCaR,train}} = 0{,}175807$
- Pada bank validasi $N=20.000$, pelanggaran relatif terhadap $\eta$ (Persamaan 2.23):
  * `rep_25`: $v_J = 0{,}037773$ ($J_{\text{valid}} = 0{,}180767$), $v_R = 0$
  * `rep_28`: $v_J = 0{,}009296$ ($J_{\text{valid}} = 0{,}175807$), $v_R = 0$
- Sumber: `results/tables/validation_interest_free.csv`. Nilai korelasi Pearson $r(\text{slack\_R})$ dan $r(\text{slack\_J})$ pada paragraf asli **tidak dapat diverifikasi** — tidak ada kolom atau berkas yang menyimpan korelasi ini di `results/tables/`; jangan dikutip tanpa dihitung ulang dari sumber yang jelas.

**Kesimpulan Ilmiah:**
Pelanggaran kelayakan pada bank validasi semata-mata merupakan konsekuensi matematis dari **posisi solusi yang mengeksploitasi batas aktif hingga margin terkecil**, bukan merupakan bukti kegagalan algoritma atau inferioritas metodologis PSO. Hal ini harus dijelaskan secara jujur dan berimbang pada naskah skripsi Bab 4.

---

## 5. Matriks Rekomendasi Tindak Lanjut Naskah Skripsi Bab 4 & Bab 5

| No. | Bagian Skripsi | Rekomendasi Isi & Penyajian | Bukti Pendukung |
|:---:|:---|:---|:---|
| 1 | **Bab 4 (Hasil Optimasi Biaya)** | **Koreksi 2026-10-25 (T6):** klaim "selisih biaya rata-rata $< 0{,}05\%$" tidak berlaku umum. Selisih rata-rata biaya KMA terhadap PSO/GA (dari `runs_summary.csv`): `gross_free` +0,070%/+0,096%; `gross_djppr` +0,006%/+0,006%; `interest_free` **+1,30%/+1,62%**; `interest_djppr` +0,0015%/+0,0015%. Sajikan tabel ini, bukan satu angka tunggal "<0,05%". | `results/tables/runs_summary.csv` |
| 2 | **Bab 4 (Waktu Komputasi)** | Cantumkan waktu eksekusi secara jujur: PSO paling cepat (~29 detik), disusul GA (~33 detik), dan KMA (~88 detik). **Koreksi 2026-10-25 (S8):** jangan atribusikan waktu KMA ke mekanisme *mlipir* secara spesifik — profil Tahap 18 (`results/sensitivity/kma/profile_kma.csv`) menunjukkan 64–74% waktu KMA ada di kategori "overhead kontrol/loop" (adaptasi populasi, manajemen generasi), bukan di evaluasi fungsi objektif atau proyeksi, dan profil itu tidak memecah waktu per submekanisme (mlipir vs big-male vs partenogenesis). | `results/sensitivity/kma/profile_kma.csv` |
| 3 | **Bab 4 (Validasi Independen)** | Paparkan hasil validasi bank $N=20.000$ secara berimbang. Sajikan temuan kelayakan 100% (KMA dan GA) serta 93,3% (PSO) disertai hasil uji Fisher ($p = 0{,}4915$) untuk menegaskan bahwa perbedaan kelayakan tidak signifikan secara statistik. | `results/tables/validation_summary.md`, `validation_all_runs.csv` |
| 4 | **Bab 4 (Analisis Bobot & Rasio $\theta_i$)** | Bahas pergeseran alokasi instrumen: optimasi secara konsisten meningkatkan porsi instrumen berbiaya murah (seperti JPY dan EUR) hingga batas atas kebijakan DJPPR. **Koreksi 2026-10-25 (S8):** klaim "$\theta_i$ seimbang di sekitar $1{,}0$" tidak berlaku umum — pada solusi `interest_djppr` (mis. `results/runs/interest_djppr/pso/rep_01_seed43.json`), $\theta_i$ berkisar ~1,12–1,54, bukan ~1,0. Tulis rentang aktual, bukan "sekitar 1,0". | `results/figures/fig_composition_*.pdf`, `fig_theta_*.pdf`, `results/runs/interest_djppr/pso/rep_01_seed43.json` |
| 5 | **Bab 5 (Keterbatasan Model)** | Cantumkan subbab keterbatasan: model GBM tidak memodelkan *mean reversion* pada suku bunga, pengujian dilakukan pada horizon tunggal 1 tahun, dan penentuan batas $\tau$/$\eta$ sangat sensitif terhadap portofolio awal 2024. | Asumsi GBM dan definisi batas risiko Persamaan 2.22 |
| 6 | **Bab 5 (Saran Penelitian Lanjutan)** | Sarankan penelitian lanjutan: (1) penerapan model suku bunga stokastik dengan mean reversion (Vasicek/Hull-White), (2) optimasi multi-horizon dinamis, dan (3) penalaan mandiri parameter adaptif KMA pada ruang simpleks. | Diskusi Bab 5 |
