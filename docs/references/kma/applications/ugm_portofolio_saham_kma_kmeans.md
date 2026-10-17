

## SKRIPSI
## OPTIMISASI PORTOFOLIO SAHAM MENGGUNAKANKOMODO
## MLIPIR ALGORITHMBERDASARKAN KLASTERK-MEANS
## (STOCK PORTFOLIO OPTIMIZATION USING KOMODO MLIPIR
## ALGORITHM BASED ONK-MEANS CLUSTERING)
## BRYAN FLORENTINO LEO
## 21/473767/PA/20429
## PROGRAM SARJANA PROGRAM STUDI STATISTIKA
## DEPARTEMEN MATEMATIKA
## FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM
## UNIVERSITAS GADJAH MADA
## YOGYAKARTA
## 2025

## SKRIPSI
## OPTIMISASI PORTOFOLIO SAHAM MENGGUNAKANKOMODO
## MLIPIR ALGORITHMBERDASARKAN KLASTERK-MEANS
## (STOCK PORTFOLIO OPTIMIZATION USING KOMODO MLIPIR
## ALGORITHM BASED ONK-MEANS CLUSTERING)
Diajukan untuk memenuhi salah satu syarat memperoleh derajat
## Sarjana Statistika Program Sarjana Program Studi Statistika
## BRYAN FLORENTINO LEO
## 21/473767/PA/20429
## PROGRAM SARJANA PROGRAM STUDI STATISTIKA
## DEPARTEMEN MATEMATIKA
## FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM
## UNIVERSITAS GADJAH MADA
## YOGYAKARTA
## 2025

## HALAMAN
## PENGESAHAN
## SKRIPSI
## OPTIMISASI
## PORTOFOLIO
## SAHAM MENGGUNAKAN
## KOMODO
## MLIPIR
## ALGORITHM
## BERDASARKAN KLASTER
## IC-MEANS
## Telah
dipersiapkan dan
disusun oleh
## BRYAN FLORENTINO
## LEO
## 21/473767/PA/20429
## Telah
dipertahankan
di depan TimPenguji
pada tanggal 16 Jull 2025
## Susunan Tim Penguji
Dr. Dwi rtinifigsih, M.Si.
## Pembimbing
## Utama
getahui,
a.n. Dekan
## PA
## U
## GM
akil
## Dekan
## Bidang
## Pendi
an
## Kemahasiswa
n
tu
rs.
## Roto,
M.Eng.,
## Prof.
## Dr.
bdurakhman,
S.Si.,
M.Si.
## Kei-ua
im
## Penguji
## Dr.
## Adhitya
## Ratnfie
fendie,
M.Sc
## Penguji
## Dr.
## Solikhatun,
s.Si., M
## NIP.
## 196711171993031020



Untuk Bapa dan Papa di surga.
iv

”Aku mengucap syukur kepada Allahku setiap kali aku mengingat kamu.”
Filipi 1:3 (TB)
v

## PRAKATA
Segala puji dan syukur Penulis naikkan kepada Tuhan Yesus, yang oleh ka-
rena kasih dan perkenanan-Nya, Penulis dapat menyelesaikan skripsi berjudul ”Op-
timisasi Portofolio Saham MenggunakanKomodo Mlipir AlgorithmBerdasarkan
KlasterK-Means”.  Keberadaan  tugas  akhir  ini  menandakan  tersisanya  beberapa
langkah lagi sebelum perjalanan Penulis dalam menuntut ilmu di Program Studi
Sarjana Statistika Fakultas Matematika dan Ilmu Pengetahuan Alam (MIPA) Uni-
versitas Gadjah Mada (UGM) mencapai penghujungnya dan Penulis dapat meraih
gelar Sarjana Statistika.
Adapun dalam menyusun skripsi ini, Penulis mengucapkan terima kasih ke-
pada:
-  Tuhan Yesus, Bapa yang setia dan kawan yang sejati;
-  Alm. Papa, Mama, serta adik-adik, Agnes dan Albert, yang membawa Penulis
dalam doa dan kasih tanpa mengenal jarak dan waktu;
-  Prof. Dr. Eng. Kuwat Triyana, M.Si., selaku Dekan Fakultas Matematika dan
## Ilmu Pengetahuan Alam Universitas Gadjah Mada;
-  Dr. Nanang Susyanto, S.Si., M.Sc., selaku Ketua Departemen Matematika
Fakultas Matematika dan Ilmu Pengetahuan Alam Universitas Gadjah Mada;
-  Dr. Dwi Ertiningsih, M.Si., selaku Dosen Pembimbing Tugas Akhir atas penga-
rahan yang telah dikerahkan bagi Penulis dalam menyusun tugas akhir ini;
-  Prof. Dr. Abdurakhman, M.Si., selaku Dosen Pembimbing Akademik atas pe-
ngarahan dan dukungan akademik selama perjalanan studi Penulis;
-  Drs. Zulaela, Dipl.Med.Stats., M.Si., selaku Dosen Pembimbing Akademik pur-
natugas;
-  Seluruh dosen Program Studi Sarjana Statistika Fakultas Matematika dan Ilmu
Pengetahuan Alam Universitas Gadjah Mada atas bekal pengetahuan yang sung-
guh bermakna dan bermanfaat;
-  Rekan-rekan seperjuangan dari Statistika 2021 ”SIRIUS” atas kebersamaan dan
vi

vii
uluran tangan selama Penulis menjalankan proses studi;
-  Dafi, Jordan, Amelia, Chandra, Melodia, Pramana, Saprina, dan Syafiqa selaku
rekan-rekan seperbimbingan Tugas Akhir;
-  Dhea, Chia, dan Priska selaku saudari-saudari seiman yang saling membersamai
dalam perjalanan iman di GPdI Hagios Family Sosrowijayan, Yogyakarta serta
menghadapi gunung dan lembah dalam perjalanan studi masing-masing;
-  Syachnaz, Putri, Angela, Iren, Tessa, Dhea, Chia, dan Icil selaku sesama Pengu-
rus Harian dan Pengurus Inti Persekutuan Mahasiswa Kristen (PMK) Fakultas
MIPA UGM periode 2023;
-  Ace, Indah, Owen, Angel, Nanta, dan Syela selaku rekan-rekan sekerja Allah
dalam Badan Pengurus Harian Unit Kegiatan Mahasiswa Kerohanian Kristen
(UKK) UGM periode 2024;
-  Seluruh anggota KKN-PPM ”Buru Basudara” Periode 2 Tahun 2024, terkhusus
Subunit Waemangit beserta keluarga piara dan warga Desa Waemangit, Kabu-
paten Buru yang tiada hentinya saling merangkul dalam doa;
-  Keluarga  besar  yang  telah  memberi  dukungan  materiil  maupun  non-materiil;
serta
-  Seluruh pihak yang telah memberikan berbagai bentuk dukungan yang tidak bisa
Penulis sebutkan satu per satu.
Penulis menyadari bahwa skripsi ini tidak luput dari kekurangan dan kesa-
lahan. Oleh karena itu, Penulis sangat terbuka terhadap masukan, kritik, dan saran
sebagai bekal bagi Penulis untuk menyempurnakan skripsi ini maupun karya-karya
yang akan datang. Besar harapan Penulis agar skripsi ini bermanfaat bagi para pem-
bacanya. Tuhan memberkati.
## Yogyakarta, 16 Juli 2025
## Penulis

## DAFTAR ISI
HALAMAN JUDUL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .i
HALAMAN PENGESAHAN. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .ii
HALAMAN PERNYATAAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .iii
HALAMAN PERSEMBAHAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .iv
HALAMAN MOTTO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .v
PRAKATA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .vi
DAFTAR ISI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  viii
DAFTAR TABEL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  xiii
DAFTAR LAMBANG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  xiv
INTISARI  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    xv
ABSTRACT. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  xvi
## BAB I
PENDAHULUAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
1.1.  Latar Belakang  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
1.2.  Pembatasan Masalah. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
1.3.  Tujuan dan Manfaat Penelitian  . . . . . . . . . . . . . . . . . . . . . . . . .4
1.4.  Tinjauan Pustaka . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
1.5.  Metodologi Penelitian  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6
1.6.  Sistematika Penulisan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
## BAB II
LANDASAN TEORI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.1.  Aljabar Vektor dan Matriks . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.1.1.  Vektor. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.1.2.  Matriks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    10
2.1.3.  Eigenvektor dan Eigennilai . . . . . . . . . . . . . . . . . . . . . .    13
2.1.4.  Bentuk Kuadrat . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
2.1.5.  Matriks Definit Positif dan Matriks Semidefinit Po-
sitif  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
2.2.  Derivatif Parsial. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    15
2.3.  Ruang Sampel dan Kejadian . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
2.4.  Probabilitas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
viii

ix
2.5.  Variabel Random. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
2.5.1.  Variabel Random Diskret . . . . . . . . . . . . . . . . . . . . . . . .    18
2.5.2.  Variabel Random Kontinu . . . . . . . . . . . . . . . . . . . . . . .    19
2.5.3.  Penyokong Variabel Random  . . . . . . . . . . . . . . . . . . . .    20
2.5.4.  Distribusi Probabilitas Gabungan . . . . . . . . . . . . . . . . .    20
2.5.5.  Distribusi Probabilitas Marginal . . . . . . . . . . . . . . . . . .    23
2.6.  Sifat-Sifat Variabel Random  . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
2.6.1.  Ekspektasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
2.6.2.  Variansi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    24
2.6.3.  Deviasi Standar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    25
2.6.4.  Kovariansi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    25
2.6.5.  Korelasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    26
2.7.  Analisis Multivariat  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    26
2.7.1.  Vektor Mean . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    27
2.7.2.  Matriks Kovariansi . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    28
2.7.3.  Jarak Euclid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
2.7.4.  Analisis Klaster. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
2.8.  Distribusi Probabilitas  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    31
2.8.1.  Distribusi Bernoulli  . . . . . . . . . . . . . . . . . . . . . . . . . . . .    31
2.8.2.  Distribusi Binomial. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
2.8.3.  Distribusi Poisson . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
2.8.4.  Distribusi Uniform . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    33
2.8.5.  Distribusi Normal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    33
2.9.  BilanganPseudo-Random. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    34
2.10.  Sampel Random  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    35
2.11.  Pengujian Hipotesis  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    35
2.12.  Uji Kolmogorov-Smirnov  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    37
2.13.  Proses Stokastik  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    38
2.13.1.  Rantai Markov  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    38
2.13.2.  ProsesRandom Walk. . . . . . . . . . . . . . . . . . . . . . . . . .    39
2.14.  Perusahaan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    40
2.15.  Investasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    41
2.16.  Saham. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    42
2.16.1.Returndan Risiko Saham  . . . . . . . . . . . . . . . . . . . . . .    43

x
2.16.2.Short Sale. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    44
2.17.  Pasar Saham. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    44
2.18.  Portofolio Saham  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    45
2.18.1.Returndan Risiko Portofolio Saham  . . . . . . . . . . . . .    45
2.18.2.  Beta Portofolio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    48
2.18.3.  Ukuran Performa Portofolio  . . . . . . . . . . . . . . . . . . . .    49
2.18.4.Sharpe Ratio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    50
2.18.5.  Portofolio Tangen . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    50
2.18.6.  Portofolio Efisien . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    51
2.18.7.Capital Asset Pricing Model. . . . . . . . . . . . . . . . . . . .    52
2.18.8.Jensen’s Alpha. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    53
2.18.9.Treynor Ratio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    54
2.19.  Indeks Saham LQ45 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    54
2.20.  Metode Pengali Lagrange. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    56
2.21.  Syarat-Syarat Kuhn-Tucker untuk Permasalahan Minimisa-
si . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    57
2.22.  Pemrograman Kuadratik. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    59
2.23.  Algoritma Optimisasi Metaheuristik . . . . . . . . . . . . . . . . . . . . .    60
## BAB III
## ANALISIS KLASTERK-MEANSDAN ALGORITMA-ALGORITMA
OPTIMISASI PORTOFOLIO. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    62
3.1.  Analisis KlasterK-Means. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    62
3.2.  Metode PortofolioMinimum Variance. . . . . . . . . . . . . . . . . . .    65
3.3.Genetic Algorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    69
3.3.1.  Terminologi Genetika. . . . . . . . . . . . . . . . . . . . . . . . . . .    69
3.3.2.  Konsep MatematisGenetic Algorithm. . . . . . . . . . . . .    70
3.3.3.  StrukturGenetic Algorithmdan Variasinya . . . . . . . . .    71
3.4.Komodo Mlipir Algorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    74
3.4.1.  Komodo . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    75
3.4.2.  Perilaku Komodo  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    76
3.4.3.  Konsep MatematisKomodo Mlipir Algorithm. . . . . . .    78
3.4.4.  Struktur UmumKomodo Mlipir Algorithm. . . . . . . . .    81
3.4.5.  PercobaanKomodo Mlipir Algorithm. . . . . . . . . . . . . .    82

xi
## BAB IV
STUDI KASUS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    84
4.1.  Deskripsi Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    84
4.2.ReturnTerealisasi Harian Saham  . . . . . . . . . . . . . . . . . . . . . . .    84
4.3.  Uji NormalitasReturnHarian Saham . . . . . . . . . . . . . . . . . . . .    84
4.4.  Analisis KlasterK-Means. . . . . . . . . . . . . . . . . . . . . . . . . . . . .    85
4.5.  Pembobotan PortofolioMinimum Variance. . . . . . . . . . . . . . .    87
4.6.  Pembobotan Portofolio MenggunakanGenetic Algorithm. . .    91
4.7.  Penyesuaian Konsep MatematisKomodo Mlipir Algorithm. .    95
4.8.  Pembahasan PercobaanKomodo Mlipir Algorithm. . . . . . . . .    96
4.9.  Pembobotan Portofolio MenggunakanKomodo Mlipir Al-
gorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    97
4.10.  Pembobotan Portofolio MenggunakanParticle Swarm Op-
timization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  101
4.11.  Perhitungan Beta Portofolio. . . . . . . . . . . . . . . . . . . . . . . . . . . .  102
4.12.  Perbandingan Performa Portofolio . . . . . . . . . . . . . . . . . . . . . .  103
## BAB V
PENUTUP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  105
5.1.  Kesimpulan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  105
5.2.  Saran. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  105
DAFTAR PUSTAKA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  107
LAMPIRAN  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  114
Lampiran 1.  Daftar Saham dalam Indeks LQ45  . . . . . . . . . . . . . . . . . . . . . .  114
Lampiran 2.Pseudocode Genetic Algorithm(GA) . . . . . . . . . . . . . . . . . . . .  116
Lampiran 3.Pseudocode Komodo Mlipir Algorithm(KMA). . . . . . . . . . . .  117
Lampiran 4.  Data Riwayat Harga Saham . . . . . . . . . . . . . . . . . . . . . . . . . . . .  118
Lampiran 5.  KomputasiReturnSaham. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  120
Lampiran 6.  Uji Kolmogorov-Smirnov terhadap NormalitasReturnHa-
rian Saham . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  121
Lampiran 7.  Vektor MeanReturn, Deviasi Standar, danSharpe Ratioda-
ri Saham denganReturnHarian Berdistribusi Normal . . . . . .  124
Lampiran 8.  Diagram Pencar MeanReturndan Risiko dari Saham de-
nganReturnHarian Berdistribusi Normal . . . . . . . . . . . . . . . .  126
Lampiran 9.  VisualisasiSilhouette Score. . . . . . . . . . . . . . . . . . . . . . . . . . . .  127
Lampiran 10.  Analisis KlasterK-Means. . . . . . . . . . . . . . . . . . . . . . . . . . . . .  128

xii
Lampiran 11.  Pembobotan PortofolioMinimum Variance. . . . . . . . . . . . . . .  129
Lampiran 12.  AplikasiGenetic  Algorithmuntuk  Menyelesaikan  Fungsi
Sphere  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  132
Lampiran 13.  Pembobotan Portofolio MenggunakanGenetic Algorithm. . .  134
Lampiran 14.  FungsiKomodo Mlipir Algorithm. . . . . . . . . . . . . . . . . . . . . . .  136
Lampiran 15.  AplikasiKomodo  Mlipir  Algorithmuntuk  Menyelesaikan
Fungsi Sphere . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  146
Lampiran 16.  Pembobotan Portofolio MenggunakanKomodo Mlipir Al-
gorithm. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  148
Lampiran 17.  Pembobotan Portofolio MenggunakanParticle Swarm Op-
timization. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  149
Lampiran 18.  Data Riwayat Harga IHSG . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  151
Lampiran 19.  KomputasiReturnIHSG  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  152
## Lampiran 20.  Komputasi  Portofolio  Saham  Relatif  Terhadap  Portofolio
Pasar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  153
Lampiran 21.  Komputasi Beta Portofolio. . . . . . . . . . . . . . . . . . . . . . . . . . . . .  154
Lampiran 22.  KomputasiSharpe Ratio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  156
Lampiran 23.  KomputasiTreynor Ratio. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  157
Lampiran 24.  KomputasiJensen’s Alpha. . . . . . . . . . . . . . . . . . . . . . . . . . . . .  158

## DAFTAR TABEL
2.1Tabel Keputusan 2×2 Pengujian Hipotesis   .  .  .  .  .  .  .  .  .  .  .  .  .    36
4.1Pembagian klaster untuk saham-saham denganreturnberdistribusi
normal.   .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .    86
4.2Perbandingan penelitian Suyanto dkk. (2022) dengan penelitian ini.97
4.3Perbandingan ukuran performa portofoliominimum variance, GA,
KMA, dan PSO. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  103
xiii

## DAFTAR LAMBANG
e: Bilangan Euler
x!:xfaktorial,x! =x(x−1)···(1)
x: Vektorx(dinotasikan dengan huruf kecil yang dicetak tebal)
x
## ′
:Transposevektorx
X:  MatriksX(dinotasikan  dengan  huruf  kapital  yang  dicetak
tebal)
|X|: Determinan matriks
## X
## ′
:TransposematriksX
x
i
: Elemen ke-i(pada himpunan atau vektor)
x
ij
: Elemen pada baris ke-idan kolom ke-j(pada matriks)
Z: Himpunan semua bilangan bulat
R: Himpunan semua bilangan real
## A
c
: Komplemen dari himpunanA
|A|: Kardinalitas atau jumlah elemen dalam himpunanA
⊆: Subhimpunan atau himpunan bagian (dari himpunan)
## P(·): Probabilitas
∼: Mengikuti distribusi probabilitas
xiv

## INTISARI
## OPTIMISASI PORTOFOLIO SAHAM MENGGUNAKANKOMODO
## MLIPIR ALGORITHMBERDASARKAN KLASTERK-MEANS
oleh
## BRYAN FLORENTINO LEO
## 21/473767/PA/20429
Sejak pandemi COVID-19 melanda Indonesia pada tahun 2020, jumlah in-
vestor individu di Indonesia telah bertumbuh pesat, khususnya dari kalangan Ge-
nerasi  Z.  Saham  merupakan  salah  satu  instrumen  investasi  berisiko  yang  paling
digemari oleh generasi tersebut. Portofolio yang optimal merupakan sarana untuk
mendiversifikasi risiko investasi, seperti yang termuat pada saham. Pada masa ki-
ni, banyak permasalahan optimisasi diselesaikan menggunakan algoritma-algoritma
metaheuristik.
Penelitian ini ditujukan untuk menguji performaKomodo Mlipir Algorithm
(KMA), salah satu algoritma metaheuristik terbaru, dalam mengoptimisasi porto-
folio saham. Pemilihan saham dilakukan berdasarkan analisis klasterK-Meansatas
saham-saham dari indeks LQ45 denganreturnyang berdistribusi normal. Performa
portofolio yang dihasilkan melalui KMA dibandingkan dengan metode portofolio
minimum variancedanGenetic Algorithm(GA) menggunakanSharpe ratio,Tre-
ynor ratio, danJensen’s alpha. Melalui komputasi dari ketiga ukuran ini, diperoleh
bahwa KMA menghasilkan portofolio dengan performa terbaik dari antara ketiga
portofolio yang dibentuk.
xv

## ABSTRACT
## STOCK PORTFOLIO OPTIMIZATION USING KOMODO MLIPIR
## ALGORITHM BASED ONK-MEANS CLUSTERING
by
## BRYAN FLORENTINO LEO
## 21/473767/PA/20429
Since the COVID-19 pandemic occurred in Indonesia in 2020, the number of
individual investors in Indonesia has grown swiftly, especially from the Generation
Z. Stocks are one of the risky investing instruments which were the most preferred
by the generation. An optimal portfolio acts to diversify investing risks, as obtained
in a stock. These days, a lot of optimization problems are solved using metaheuristic
algorithms.
This  research  aims  to  test  the  performance  of  Komodo  Mlipir  Algorithm
(KMA), one of the novel metaheuristic algorithms, on optimizing stock portfolio.
Stocks are selected based onK-Means clustering on stocks from the LQ45 index
which returns are normally distributed. The performance of the portfolio produced
through KMA is then compared with the portfolios produced from the minimum
variance method and Genetic Algorithm (GA) based on Sharpe ratio, Treynor ratio,
and Jensen’s alpha. The result of these three measures from computation shows that
the KMA portfolio has the best performance out of the three portfolios.
xvi

## BAB I
## PENDAHULUAN
## 1.1.  Latar Belakang
Pada tahun 2021 yang lalu, Presiden Joko Widodo menetapkan pembentuk-
an sebuah kementerian baru bernama Kementerian Investasi dan Hilirisasi Repub-
lik Indonesia. Kementerian ini menggantikan Badan Koordinasi Penanaman Modal
(BKPM) dengan tujuan untuk meningkatkan investasi negara, menciptakan lapang-
an pekerjaan, serta merespons peresmian Undang-Undang Cipta Kerja dan kenaik-
an pagu anggaran untuk BKPM yang mencapai 147,9 persen (Finaka, 2021; Putri,
2021). Hadirnya Kementerian Investasi dan Hilirisasi telah menunjukkan dampak
yang  signifikan  terhadap  kegiatan  investasi  pemerintahan  Indonesia.  Pada  akhir
tahun  2023,  Badan  Pusat  Statistik  (BPS)  mencatat  bahwa  realisasi  investasi  pe-
nanaman modal dalam negeri nasional mencapai nominal 674,9234 triliun rupiah
pada 266.722 unit proyek. Angka ini berturut-turut meningkat sebanyak 50,96 per-
sen dan 151,62 persen dari tahun 2021, menandakan peran positif kementerian ter-
sebut dalam mengoptimalisasi anggaran negara untuk proyek-proyek investasi yang
semakin beragam. Lebih lanjut, statistik ini tidak melibatkan investasi pada sektor
minyak bumi dan gas, keuangan, asuransi, pasar modal, dan rumah tangga. Maka,
andaikan investasi di kalangan masyarakat turut dipertimbangkan, aktivitas investa-
si di Indonesia sejatinya jauh lebih luas daripada ukuran statistik-statistik tersebut.
Dengan kata lain, kontribusi investor-investor individu sejatinya memegang peran
yang tidak kalah penting.
Sejak  beberapa  tahun  silam,  banyak  masyarakat  Indonesia  telah  memilih
investasi sebagai upaya menunjang situasi keuangan pribadi. Sejak masa pandemi
COVID-19 melanda pada tahun 2020 hingga awal tahun 2024, PT Kustodian Sen-
tral Efek Indonesia (KSEI) mencatat pertumbuhan jumlah angka investor individu
hingga lebih dari tiga kali lipat. Tujuan investasi masyarakat didominasi untuk dana
## 1

## 2
darurat, penghasilan tambahan, atau dana pensiun (Wiranto, 2022). Terkini, inves-
tasi tidak hanya dilakukan oleh mereka yang telah berkeluarga, tetapi juga di tengah
kalangan anak muda. Berdasarkan data KSEI pula, jumlah investor Generasi Z pa-
da akhir tahun 2023 telah mencapai lebih dari dua belas juta orang, memenuhi 56,4
persen demografi investor individu di Indonesia. Peristiwa ini tidak hanya terjadi di
Indonesia, tetapi juga di beberapa negara maju. Hal ini diyakini karena informasi
tentang investasi digital dan edukasi literasi keuangan mulai menjamur di media so-
sial. Bertambahnya aplikasi investasi digital dan naiknya tren mata uang kripto juga
diduga mendorong fenomena ini. Lebih lanjut, investasi juga merupakan alternatif
yang sejalan dengan karakter Generasi Z yang tidak menggemari pekerjaan kan-
toran dan hendak mencapai kebebasan finansial dalam waktu yang cepat (Pramuji,
2024). Didukung dengan tingkat keamanan yang tinggi dan kebutuhan modal yang
minimum, hasil survei Populix menyatakan bahwa 67 persen masyarakat Indonesia
berencana untuk melanjutkan kegiatan investasi pada tahun 2025 mendatang (Fitri,
## 2024).
Reksa dana, emas, dan saham merupakan tiga instrumen investasi yang pa-
ling banyak diincar oleh investor individu. Investor emas didominasi oleh Generasi
X dan Generasi Y (alias Milenial), sedangkan reksa dana dan saham lebih digemari
oleh Generasi Z. Pertimbangan masyarakat dalam berinvestasi pada emas didasari
oleh profil risiko emas yang rendah. Sementara, reksa dana dan saham dinilai aman
karena telah terdaftar di Otoritas Jasa Keuangan (OJK) dan telah tersedia di berba-
gai aplikasi digital maupun perdagangan elektronik (e-commerce) (Wiranto, 2022).
Meski dirasa lebih praktis dan dekat dengan genggaman kalangan dewasa muda,
tidak dapat dipungkiri bahwa reksa dana dan saham merupakan dua instrumen in-
vestasi yang berisiko.
Penanganan  risiko  dalam  berinvestasi,  khususnya  pada  sekuritas  keuang-
an  seperti  reksa  dana  dan  saham,  dapat  diperantarai  oleh  portofolio.  Portofolio
membobotkan dua sekuritas atau lebih dengan mempertimbangkan potensireturn
dan  risiko  yang  terasosiasi  dengan  tiap  sekuritas  tersebut.  Perkembangan  popu-
laritas portofolio diawali dengan penemuan Teori Portofolio Modern oleh Harry

## 3
Markowitz pada tahun 1952. Seiring berjalannya waktu, berbagai metode optimi-
sasi portofolio konvensional hadir, lalu tergantikan oleh algoritma-algoritma heu-
ristik. Selanjutnya, algoritma-algoritma heuristik semakin dikembangkan menjadi
algoritma-algoritma metaheuristik yang becermin terhadap fenomena alam dan pe-
rilaku makhluk hidup pada alam.
Salah satu algoritma metaheuristik terbaru ialahKomodo Mlipir Algorithm
(KMA). KMA ditemukan oleh ilmuwan asal Indonesia, Prof. Suyanto, dalam pe-
ngukuhannya sebagai guru besar di Telkom University pada tahun 2022. Penemuan
KMA terinspirasi dari perilaku komodo jantan dewasa, komodo betina, dan komo-
do jantan muda di habitatnya. Literatur perdana tentang KMA oleh Suyanto dkk.
(2022) membandingkan performa KMA dengan enam algoritma metaheuristik ter-
dahulu dalam optimisasi fungsi-fungsi matematis berdimensi besar. Penelitian ini
menyimpulkan  bahwa  KMA  merupakan  algoritma  optimisasi  baru  yang  unggul.
KMA selanjutnya digunakan dalam berbagai eksperimen untuk menyelesaikan ber-
bagai permasalahan optimisasi praktis. Akan tetapi, hingga saat ini, belum terdapat
penelitian ilmiah yang mengulas pemanfaatan KMA pada bidang keuangan, khu-
susnya permasalahan optimisasi portofolio yang cukup populer dalam bidang ini.
Oleh karena itu, Penulis termotivasi untuk mengimplementasikan KMA serta mem-
bandingkannya dengan model portofoliominimum variancedanGenetic Algorithm
(GA) pada permasalahan optimisasi portofolio saham yang didasarkan pada klaster
K-Means.
## 1.2.  Pembatasan Masalah
Pada penelitian ini, Penulis membatasi metode optimisasi pada model por-
tofoliominimum variance,Genetic Algorithm(GA), danKomodo Mlipir Algori-
thm(KMA). Menimbang aplikasi KMA yang masih terbatas pada permasalahan-
permasalahan optimisasi di dunia nyata, KMA menjadi metode utama yang difo-
kuskan dalam laporan ini. Penulis menggunakan data riwayat harga dari 45 saham
yang termuat dalam indeks LQ45 menurut pembaruan terkini pada bulan Agustus
- Rincian nama-nama saham tersebut dapat diamati pada Lampiran 1. Data ri-

## 4
wayat harga saham diperoleh dari situs webinvesting.comdan dibatasi pada periode
Desember 2023 hingga November 2024 agar data bersifat terkini dan utuh. Model
permasalahan optimisasi yang dilibatkan dibatasi pada permasalahan minimalisasi
risiko dan tidak terdapatshortselling. Dengan kata lain, tiap saham yang terlibat
dalam portofolio harus berbobot nonnegatif.
Performa portofolio yang terbentuk dari tiga metode yang digunakan akan
diukur dan dibandingkan melalui ukuranSharpe ratio,Treynor ratio, danJensen’s
alpha. Agar ketiga ukuran ini berlaku, diberlakukan asumsi bahwa risiko bernilai
konstan selama periode data yang digunakan.
1.3.  Tujuan dan Manfaat Penelitian
Tujuan penelitian ini adalah:
-  Mempelajari teori-teori penyusunan portofolio saham yang optimal.
-  MempelajariKomodo Mlipir Algorithmsebagai salah satu algoritma optimisasi
metaheuristik terbaru.
-  MengaplikasikanKomodo Mlipir Algorithmpada pembentukan portofolio sa-
ham yang optimal berdasarkan klasterK-Means.
-  Menganalisis keoptimalan portofolio saham yang didasarkan pada kemampuan
meminimasi risiko menggunakanKomodo Mlipir Algorithmberdasarkan klas-
terK-Meansterhadap metode-metode optimisasi portofolio klasik, yaitu model
portofoliominimum variancedanGenetic Algorithm.
Adapun manfaat penelitian ini adalah:
-  Mengembangkan aplikasiKomodo Mlipir Algorithmpada bidang statistika keu-
angan, khususnya optimisasi portofolio saham.
-  Mendukung  perluasan  aplikasiKomodo  Mlipir  Algorithmdalam  berbagai  bi-
dang ilmu.
-  MempromosikanKomodo Mlipir Algorithmsebagai karya ilmuwan nasional.

## 5
## 1.4.  Tinjauan Pustaka
Ide optimisasi portofolio pertama kali dicetuskan oleh Markowitz pada ta-
hun  1952.  Penemuan  Markowitz,  yang  dikenal  sebagai  model  portofoliomean-
varianceatauminimum variance, didasarkan pada kesetimbanganreturndan risi-
ko yang diperoleh dalam melakukan investasi terhadap aset-aset yang terlibat.Re-
turndan risiko berturut-turut diukur melalui vektor ekspektasireturndan matriks
kovariansi. Sensitivitas terhadap mean dan kovariansi menjadikan model portofo-
liomean-variancetidak optimal (Dai, 2019). Permasalahan ini ditangani dengan
menggunakan estimasi matriks kovariansi yang tak bias, seperti matriks kovarian-
si terboboti eksponensial, kovariansi tersusutkan Ledoit-Wolf, kovariansi Gerber,
matriks kovariansi sampel, estimator kovariansiOrdinary Least Square(OLS), dan
estimatoreigenvalue  clipping(Zhou,  2020;  Bitar  dkk.,  2023).  Selain  itu,  model
mean-variancejuga dapat dikembangkan dan diperbaiki pada skala yang lebih be-
sar, seperti menuju modelglobal minimum variance(GMV) dan model faktor (Sun
dkk., 2019).  Kelemahan lain dari model portofoliomean-varianceialah kompo-
nen bobot portofolio dapat bernilai negatif. Jagannathan dan Ma (2003) mengatasi
permasalahan ini dengan melibatkan suatu kendala pertidaksamaan dalam model.
Algoritma optimisasi metaheuristik merupakan salah satu kebaruan dalam
cabang ilmu matematika optimisasi yang masih terus dikembangkan oleh para il-
muwan hingga hari ini. Salah satu pionir perkembangan algoritma metaheuristik
ialahGenetic Algorithm(GA). Ditemukan oleh John Holland pada tahun 1975, GA
terinspirasi  dari  fenomena  mutasi  dan  rekombinasi  genetika.  Reeves  (2010)  me-
maparkan bahwa GA dapat dimanfaatkan untuk menyelesaikan permasalahan opti-
misasi biner, diskret, permutasi, maupun nonbiner. Seiring berjalannya waktu, GA
telah diaplikasikan secara luas pada berbagai bidang ilmu. Bahkan, GA merupak-
an algoritma metaheuristik terpopuler kedua yang dirujuk atau dimuat dalam lebih
dari tujuh puluh ribu publikasi ilmiah pada tahun 2022 (Rajwar dkk., 2023). Dalam
mengatasi permasalahan optimisasi portofolio, beberapa penelitian menggunakan
GA  secara  murni,  seperti  Zhu  (2016),  Dubinskas  dan  Urb
## ˇ
sien
## ̇
e  (2017),  Cheong
dkk. (2017), dan Li dan Shi (2022). Sementara, beberapa penelitian lainnya meng-

## 6
gabungkan GA dengan pendekatan, ukuran numerik, atau algoritma pemelajaran
mesin (machine learning), seperti pendekatan jumlah terbobot (Faia dkk., 2018),
valuasi aset (Lim dkk., 2020), indeks prioritas (Vasiani dkk., 2020), pemrogram-
an linear (Sukono dkk., 2018), dan jaringan saraf tiruanLong-Short Term Memory
(LSTM) (Flores-Fernandez dkk., 2024).
GA dan algoritma-algoritma turunannya tidak dapat diskalakan dan tidak
stabil.Komodo Mlipir Algorithm(KMA) ditemukan dan telah teruji sebagai algo-
ritma metaheuristik baru yang mampu mengatasi kelemahan-kelemahan ini. Dalam
perbandingan  antara  KMA  dengan  enam  algoritma  terdahulu  oleh  Suyanto  dkk.
(2022), KMA menempati urutan terbaik dalam aspek kestabilan dan skalabilitas,
sedangkan GA berada pada urutan terakhir. Studi-studi lanjutan mengaplikasi-kan
KMA pada permasalahan deteksi partikel udara PM2.5 (Li dan Zhao, 2022), pen-
jadwalan  generator  listrik  (Aditya  dkk.,  2022),  penentuan  mekanisme  rute  opti-
mal (Soundarayaa dan Balasubramanian, 2024), dan efisiensi energi pada jaringan-
jaringan radio kognitif (Dharmapuri dan Reddy, 2024). Lebih lanjut, beberapa studi
bahkan telah mengembangkan KMA atau meleburkan KMA dengan algoritma lain
untuk membentuk algoritma metaheuristik baru, yakni antara lainStochastic Ko-
modo Algorithm(SKA) (Kusuma dan Kallista, 2022),Improved Adaptive Komo-
do Mlipir Algorithm(IKMA) (Liu dan Zhang, 2022),Discrete Komodo Algorithm
(DKA) (Jati dkk., 2023), danHybrid Pelican Komodo Algorithm(HPKA) (Kusuma
dan Dinimaharawati, 2022).
## 1.5.  Metodologi Penelitian
Penelitian dalam skripsi ini berupa studi literatur dan studi kasus. Studi li-
teratur dilakukan dengan mengumpulkan informasi dan merangkum pengetahuan
yang terkait dengan topik penelitian penulis dari berbagai buku, jurnal, dan arti-
kel secara daring. Informasi dan pengetahuan yang diperoleh menjadi acuan da-
lam menyusun skripsi ini dan melaksanakan studi kasus. Adapun studi kasus yang
dilakukan ialah berupa pembandingan metode portofoliominimum variance,Ge-
netic Algorithm(GA), danKomodo Mlipir Algorithm(KMA) dalam memperoleh

## 7
portofolio saham yang optimal, yaitu portofolio yang meminimisasi risiko inves-
tasi. Sebagai tambahan, untuk tujuan yang serupa, KMA juga akan dibandingkan
denganParticle Swarm Optimization(PSO) sebagai algoritma metaheuristik yang
sama-sama berbasis kecerdasan kawanan. Data yang digunakan merupakan data se-
kunder berupa data riwayat harga saham-saham yang termuat dalam indeks saham
LQ45 yang diperoleh dari situs webinvesting.com. Riwayat dibatasi pada bingkai
waktu Desember 2023 hingga November 2024. Studi kasus didukung secara kom-
putasional menggunakan bahasa pemrograman R yang diperantarai oleh aplikasi
RStudio.  Padanan-padanan  istilah  mengacu  pada  padanan  yang  telah  ditentukan
oleh Badan Pengembangan dan Pembinaan Bahasa Kementerian Pendidikan Dasar
dan Menengah dan diluncurkan pada aplikasi PASTI (Padanan Istilah).
## 1.6.  Sistematika Penulisan
Dalam menyusun skripsi ini, Penulis mengacu pada sistematika penulisan
sebagai berikut:
## BAB I PENDAHULUAN
Bab I (Pendahuluan) memuat latar belakang, pembatasan masalah, tujuan
dan  manfaat  penelitian,  tinjauan  pustaka,  metodologi  penelitian,  dan  sistematika
penulisan. Secara umum, bab ini ditujukan untuk menjelaskan alasan diusungnya
topik penelitian, cakupan permasalahan, perbandingan dengan penelitian-penelitian
terdahulu, dan susunan laporan.
## BAB II LANDASAN TEORI
Bab II (Landasan Teori) berisi dasar-dasar teori yang digunakan untuk mem-
bahas topik penelitian dan permasalahan di dalamnya. Pada penelitian ini, termuat
dasar-dasar teori yang berasal dari tiga rumpun keilmuan, yaitu matematika (aljabar
vektor dan matriks, derivatif parsial, dan topik-topik seputar teori optimisasi), sta-
tistika (topik-topik seputar probabilitas, pengujian hipotesis, dan proses stokastik),
dan ekonomika (perusahaan, investasi, serta topik-topik seputar saham dan porto-
folio).

## 8
## BAB III ANALISIS KLASTERK-MEANSDAN ALGORITMA-ALGORITMA
## OPTIMISASI PORTOFOLIO
Bab  III  (Analisis  KlasterK-Meansdan  Algoritma-Algoritma  Optimisasi
Portofolio) berisi penjabaran metodologi-metodologi yang digunakan dalam pene-
litian, yaitu analisis klasterK-Means, metode portofoliominimum variance,Gene-
tic Algorithm(GA), danKomodo Mlipir Algorithm(KMA).
## BAB IV STUDI KASUS
Bab  IV  (Studi  Kasus)  memuat  studi  kasus,  yaitu  aplikasi  analisis  klaster
K-Means, algoritma-algoritma optimisasi portofolio, dan ukuran-ukuran performa
portofolio  dalam  suatu  kerangka  yang  terstruktur  untuk  membentuk  portofolio-
portofolio atas beberapa saham yang bersumber dari indeks saham LQ45.
## BAB V PENUTUP
Bab V (Penutup) memuat kesimpulan dari penelitian yang dilakukan serta
saran yang ditujukan untuk perkembangan pada penelitian-penelitian di masa yang
akan datang.
## DAFTAR PUSTAKA
Daftar Pustaka memuat sumber-sumber pustaka ilmiah yang dijadikan refe-
rensi dalam laporan ini. Sumber-sumber tersebut disusun menggunakan gaya penu-
lisan American Psychological Association (APA) Style edisi ketujuh.
## LAMPIRAN
Lampiran memuat konten-konten tambahan yang turut dilibatkan dalam pe-
nelitian, meliputi data,pseudocode, sintaksis, dan luaran komputasi.

## BAB II
## LANDASAN TEORI
2.1.  Aljabar Vektor dan Matriks
Dalam ilmu matematika, nilai-nilai dari sekumpulan variabel dapat dimu-
at dalam sebuah vektor atau matriks. Berikut merupakan definisi serta sifat-sifat
vektor dan matriks dalam matematika.
## 2.1.1.  Vektor
Vektor didefinisikan sebagai berikut.
Definisi 2.1.1(Johnson dan Winchern, 2007) Vektor adalah suatu larik,x, yang
beranggotakannbilangan real,x
## 1
## ,x
## 2
## ,...,x
n
, dan dinotasikan sebagai:
x=
## 
## 
## 
## 
## 
## 
## 
## 
x
## 1
x
## 2
## .
## .
## .
x
n
## 
## 
## 
## 
## 
## 
## 
## 
## .
Beberapa operasi vektor, sifat vektor, dan vektor khusus diberikan sebagai
berikut.
-  Penjumlahan vektor
Hasil penjumlahan dua buah vektor dengan panjang yang sama,xdany, adalah:
x+y=
## 
## 
## 
## 
## 
## 
## 
## 
x
## 1
x
## 2
## .
## .
## .
x
n
## 
## 
## 
## 
## 
## 
## 
## 
## +
## 
## 
## 
## 
## 
## 
## 
## 
y
## 1
y
## 2
## .
## .
## .
y
n
## 
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 
x
## 1
## +y
## 1
x
## 2
## +y
## 2
## .
## .
## .
x
n
## +y
n
## 
## 
## 
## 
## 
## 
## 
## 
## .
-  Perkalian vektor dengan skalar
## 9

## 10
Hasil perkalian sembarang konstanta,c, dengan sembarang vektor,x, adalah:
cx=
## 
## 
## 
## 
## 
## 
## 
## 
cx
## 1
cx
## 2
## .
## .
## .
cx
n
## 
## 
## 
## 
## 
## 
## 
## 
## .
3.Transposevektor
Transposesuatu vektor mengubah kolom-kolom vektor menjadi baris-baris vek-
tor.Transposesembarang vektor,x, diberikan sebagai:
x
## ′
## =
h
x
## 1
x
## 2
## ···x
n
i
## .
-  Vektor nol
Vektor nol dengan panjangnadalah sebuah vektor yang seluruhnelemennya
bernilai nol. Vektor nol didefinisikan:
## 0
n
## =
## 
## 
## 
## 
## 
## 
## 
## 
## 0
## 0
## .
## .
## .
## 0
## 
## 
## 
## 
## 
## 
## 
## 
## .
-  Vektor satu
Vektor satu (disebut jugavector of onesatauall-ones vector) dengan panjang
nadalah  sebuah  vektor  yang  seluruhnelemennya  bernilai  satu.  Vektor  satu
didefinisikan:
## 1
n
## =
## 
## 
## 
## 
## 
## 
## 
## 
## 1
## 1
## .
## .
## .
## 1
## 
## 
## 
## 
## 
## 
## 
## 
## .
## 2.1.2.  Matriks
Perluasan dari sebuah vektor dikenal sebagai sebuah matriks. Definisi mat-
riks diberikan sebagai berikut.

## 11
Definisi 2.1.2(Johnson dan Winchern, 2007) Matriks adalah suatu larik persegi
panjang  sembarang  yang  beranggotakan  bilangan  real.  Suatu  matriks,A,  yang
berukurannbaris danpkolom, dirumuskan sebagai berikut:
## A
## (n×p)
## =
## 
## 
## 
## 
## 
## 
## 
## 
a
## 11
a
## 12
## ···a
## 1p
a
## 21
a
## 22
## ···a
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
a
n1
a
n2
## ···a
np
## 
## 
## 
## 
## 
## 
## 
## 
## .(2.1)
Beberapa operasi matriks, sifat matriks, dan matriks khusus diberikan seba-
gai berikut.
-  Penjumlahan matriks
Hasil penjumlahan dua buah matriks dengan dimensi yang sama,AdanB, ada-
lah:
## A+B=
## 
## 
## 
## 
## 
## 
## 
## 
a
## 11
a
## 12
## ···a
## 1p
a
## 21
a
## 22
## ···a
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
a
n1
a
n2
## ···a
np
## 
## 
## 
## 
## 
## 
## 
## 
## +
## 
## 
## 
## 
## 
## 
## 
## 
b
## 11
b
## 12
## ···b
## 1p
b
## 21
b
## 22
## ···b
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
b
n1
b
n2
## ···b
np
## 
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 
a
## 11
## +b
## 11
a
## 12
## +b
## 12
## ···a
## 1p
## +b
## 1p
a
## 21
## +b
## 21
a
## 22
## +b
## 22
## ···a
## 2p
## +b
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
a
n1
## +b
n1
a
n2
## +b
n2
## ···a
np
## +b
np
## 
## 
## 
## 
## 
## 
## 
## 
## .
-  Perkalian matriks dengan skalar
Hasil perkalian sembarang konstanta,c, dengan sembarang matriks,A, adalah:
cA=
## 
## 
## 
## 
## 
## 
## 
## 
ca
## 11
ca
## 12
## ···ca
## 1p
ca
## 21
ca
## 22
## ···ca
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
ca
n1
ca
n2
## ···ca
np
## 
## 
## 
## 
## 
## 
## 
## 
## .
3.Transposematriks
Transposesuatu matriks menukar kolom-kolom matriks menjadi baris-baris ma-
triks.Transposesembarang matriks dengan dimensi(n×p),A, sebagaimana

## 12
didefinisikan sebelumnya pada Persamaan (2.1), diberikan sebagai:
## A
## ′
## (p×n)
## =
## 
## 
## 
## 
## 
## 
## 
## 
a
## 11
a
## 21
## ···a
n1
a
## 12
a
## 22
## ···a
n2
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
a
## 1p
a
## 2p
## ···a
np
## 
## 
## 
## 
## 
## 
## 
## 
## .
-  Perkalian dua buah matriks
Hasil perkalian dua buah matriks,A
## (n×k)
danB
## (k×p)
, ialah matriks berdimensi(n×
p)dengan elemen pada baris ke-idan kolom ke-jadalahinner productdari baris
ke-idariAdan kolom ke-jdariB, yaitu:
elemen ke-(i,j)dariAB=a
i1
b
## 1j
## +a
i2
b
## 2j
## +···+a
## 1k
b
kj
## =
k
## X
l=1
a
il
b
lj
## .
-  Matriks persegi
Suatu matriks disebut matriks persegi jika ia memiliki banyak baris yang sama
dengan banyak kolom.
-  Matriks simetris
Sembarang matriks persegi,A
## (n×n)
, disebut simetris jikaA=A
## ′
ataua
ij
## =a
ji
untuk tiapidanj.
-  Matriks identitas
Matriks identitas adalah matriks persegi dengan nilai satu pada diagonal utama-
nya dan nol untuk elemen lainnya. Matriks identitas didefinisikan:
## I=
## 
## 
## 
## 
## 
## 
## 
## 
## 1   0···0
## 0   1···0
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 0   0···1
## 
## 
## 
## 
## 
## 
## 
## 
## .
Untuk sembarang matriks persegi,A, dengan dimensi yang sama denganI, di-
penuhi sifat:
## IA=AI=A.

## 13
-  Determinan matriks
Determinan dari suatu matriks persegi,A, berukurann×ndidefinisikan sebagai:
## |A|=
n
## X
i=1
## (−1)
f(i
## 1
## ,...,i
n
## )
a
## 1i
## 1
a
## 2i
## 2
## ···a
ni
n
## =
n
## X
i=1
## (−1)
f(i
## 1
## ,...,i
n
## )
a
i
## 1
## 1
a
i
## 2
## 2
## ···a
i
n
n
## ,
dengana
ij
melambangkan  elemen  matriksApada  baris  ke-idan  kolom  ke-
jsertaf(i
## 1
## ,...,i
n
)melambangkan banyak transposisi yang diperlukan untuk
mengubah(i
## 1
## ,...,i
n
)menuju(1,...,m). Transposisi dimaknai sebagai pertu-
karan dua buah bilangan.
Determinan  matriks  juga  dapat  diperoleh  melalui  ekspansi  baris  atau
kolom, yaitu untuk suatu matriks persegi,A:
## |A|=
m
## X
j=1
a
ij
## A
ij
atau
## |A|=
m
## X
i=1
a
ij
## A
ij
## .
Untuk sembarang matriks dengan determinan nol, matriks tersebut di-
sebut matriks singular.
-  Matriks invers
Jika untuk sembarang matriks persegi nonsingular,A, terdapat matriks persegi
nonsingularBsedemikian sehingga:
## BA=AB=I,
makaBdisebut matriks invers dariAdan dinotasikanA
## −1
## .
2.1.3.  Eigenvektor dan Eigennilai
Definisi eigenvektor dan eigennilai diberikan sebagai berikut.
Definisi 2.1.3(Schott, 2017) JikaAmerupakan sebuah matriks berukurann×n,
maka sembarang skalar,λ, yang memenuhi persamaan berikut:
## Ax=λx

## 14
untuk beberapa vektor berukurann×1,x̸=0, disebut eigennnilai dariA. Vektor
xdisebut eigenvektor dariAyang berkorespondensi dengan eigennilaiλ.
Eigennilai dari suatu matriks,A, dapat diperoleh sebagai akar-akar dari per-
samaan karakteristikA, yaitu:
|A−λI
n
## |= 0,
dengan|·|melambangkan determinan matriks danI
n
merupakan matriks identi-
tas berukurann×n. Hal ini dikarenakan melalui definisi determinan, persamaan
karakteristik dapat dipandang sebagai polinomial derajatnatasλ:
## (−λ)
n
## +α
n−1
## (−λ)
n−1
## +···+α
## 1
λ+α
## 0
## = 0,
denganα
## 0
## ,α
## 1
## ,...,α
n−1
adalah skalar-skalar.
## 2.1.4.  Bentuk Kuadrat
Bentuk kuadrat dari suatu vektor didefinisikan sebagai berikut.
Definisi 2.1.4(Schott, 2017) Diberikan vektorxberukurann×1dan matriks per-
segi simetrisAberukurann×n. Bentuk kuadrat darixdirumuskan sebagai:
x
## ′
## Ax=
n
## X
i=1
n
## X
j=1
x
i
x
j
a
ij
## .(2.2)
Adisebut matriks bentuk kuadrat.
2.1.5.  Matriks Definit Positif dan Matriks Semidefinit Positif
Suatu matriks persegi dapat disebut matriks definit positif atau matriks semi-
definit positif berdasarkan bentuk kuadratnya atau eigennilai-eigennilainya. Untuk
sifat bentuk kuadrat tertentu, dipenuhi sifat sebagai berikut:
## 1.  Jikax
## ′
Ax>0untuk semuax̸=0
n
, makaAbersifat definit positif.
## 2.  Jikax
## ′
Ax≥0untuk semuaxdanx
## ′
Ax= 0untuk sebagianx̸=0
n
, makaA
bersifat semidefinit positif.
Di sisi lain, berdasarkan eigennilai-eigennilainya, sifat definit positif dan semidefi-
nit positif dari suatu matriks diberikan oleh teorema berikut.

## 15
Teorema 2.1.5(Schott, 2017) Diberikanλ
## 1
## ,...,λ
n
, eigennilai-eigennilai dari su-
atu matriks persegi,A, berukurann×n. Maka, berlaku:
1.Abersifat definit positif jika dan hanya jikaλ
i
>0untuk seluruhi; dan
2.Abersifat semidefinit positif jika dan hanya jikaλ
i
≥0untuk seluruhidan
λ
i
= 0untuk setidaknya satui.
## 2.2.  Derivatif Parsial
Definisi derivatif parsial perlu diawali dengan memahami fungsi multivari-
abel yang didefinisikan sebagai berikut.
Definisi 2.2.1(Stewart, 2015) Fungsinvariabel adalah fungsi bernilai real yang
memetakan suatu bilangan,z=f(x
## 1
## ,x
## 2
## ,...,x
n
), menuju rangkapn(n-tuple),
## (x
## 1
## ,x
## 2
## ,...,x
n
). Domain fungsifadalah subhimpunan dariR
n
## .
Suatu  fungsi  multivariabel  dapat  dipandang  sebagai  fungsi  atasnvariabel  real,
x
## 1
## ,x
## 2
## ,...,x
n
; suatu variabel titik,(x
## 1
## ,x
## 2
## ,...,x
n
); atau suatu variabel vektor,x
## ′
## =
## [x
## 1
## ,x
## 2
## ,...,x
n
## ].
Derivatif parsial dari suatu fungsi multivariabel didefinisikan sebagai beri-
kut.
Definisi 2.2.2(Stewart, 2015) Diberikan suatu fungsinvariabel,f(x
## 1
## ,x
## 2
## ,...,x
n
## ).
Derivatif parsialfterhadap variabel ke-i,x
i
, didefinisikan:
## ∂f
## ∂x
i
= lim
h→0
f(x
## 1
## ,...,x
i−1
## ,x
i
## +h,x
i+1
## ,...,x
n
## )−f(x
## 1
## ,...,x
i
## ,...,x
n
## )
h
dan dapat dinotasikan pula sebagai:
## ∂f
## ∂x
i
## =f
x
i
## =f
i
## =D
i
f.
Konsep derivatif parsial dapat diperluas untuk fungsi atas vektor atau ma-
triks. Menurut Schott (2017), jikafadalah suatu fungsi bernilai real atas suatu vek-
tor berukurann×1,x= [x
## 1
## ,x
## 2
## ,...,x
n
## ]
## ′
, maka derivatiffterhadapxdiberikan
sebagai vektor baris:
## ∂f(x)
## ∂x
## ′
## =
h
## ∂
## ∂x
## 1
f(x)···
## ∂
## ∂x
n
f(x)
i
## ,

## 16
yaitu derivatiffterhadap tiap elemen vektorx, jika derivatif tersebut ada.
Jikafmempunyai bentuk khusus:
f(x) =a
## ′
x
denganaadalah suatu vektorn×1berelemen konstanta, elemen (kolom) ke-hdari
derivatiffterhadapxdirumuskan:
## ∂f
## ∂x
h
## =
## ∂
## ∂x
h
n
## X
i=1
a
i
x
i
## =
n
## X
i=1
a
i
## 
## ∂
## ∂x
h
x
i
## 
## .(2.3)
## Karena
## ∂
## ∂x
h
x
i
## =
## 
## 
## 
## 
## 
## 1,jikai=h,
## 0,jikai̸=h.
## ,
Persamaan (2.3) menjadi:
## ∂f
## ∂x
h
## =a
h
sehingga diperoleh:
## ∂f
## ∂x
## ′
## =a
## ′
## .
Di sisi lain, jikafmempunyai bentuk khusus:
f(x) =x
## ′
## Ax
denganAadalah suatu matriks simetrisn×nberelemen konstanta, elemen ke-h
dari derivatiffterhadapxdirumuskan:
## ∂f
## ∂x
h
## =
## ∂
## ∂x
h
n
## X
i=1
n
## X
j=1
a
ij
x
i
x
j
## =
n
## X
i=1
n
## X
j=1
a
ij
## 
## ∂
## ∂x
h
x
i
x
j
## 
## =
n
## X
i=1
n
## X
j=1
a
ij
## "
## 
## ∂
## ∂x
h
x
i
## 
x
j
## +x
i
## 
## ∂
## ∂x
h
x
j
## 
## #
## =
n
## X
j=1
a
hj
x
j
## +
n
## X
i=1
a
ih
x
i

## 17
## =
n
## X
j=1
a
jh
x
j
## +
n
## X
i=1
a
ih
x
i
## = 2
n
## X
i=1
a
ih
x
i
karenaa
jh
## =a
hj
. Derivatif ini dapat dinotasikan:
## ∂f
## ∂x
## = 2x
## ′
## A.
2.3.  Ruang Sampel dan Kejadian
Menurut Bain dan Engelhardt (1992), eksperimen adalah proses mengamati
atau memperoleh hasil dari suatu fenomena. Penyelenggaraan sebuah eksperimen
disebut percobaan dan hasil yang diamati disebut luaran (outcome). Ruang sampel
diartikan sebagai himpunan semua luaran yang memungkinkan dari suatu eksperi-
men dan umumnya dinotasikanS.
Kejadian adalah subhimpunan (subset) dari ruang sampel. JikaAmelam-
bangkan suatu kejadian, makaAdisebut sudah terjadi jikaAberanggotakan luaran-
luaran yang sudah terjadi. Kejadian-kejadianA
## 1
## ,A
## 2
## ,A
## 3
,...dikatakan saling lepas
(mutually exclusive) jika tiap pasangan yang memungkinkan saling lepas, yaitu jika
## A
i
## ∩A
j
=∅untuk tiapi̸=j.
## 2.4.  Probabilitas
Secara  sederhana,  probabilitas  dapat  dipandang  sebagai  suatu  fungsi  atas
himpunan, yaitu fungsi yang memetakan sekumpulan kejadian menuju suatu sub-
himpunan bilangan real. Secara formal, probabilitas didefinisikan sebagai berikut.
Definisi 2.4.1(Bain dan Engelhardt, 1992) Jika diberikanS, suatu ruang sampel,
danA,A
## 1
## ,A
## 2
,..., sekumpulan kejadian yang memungkinkan,P(A)disebut pro-
babilitas atasAjika memenuhi sifat-sifat berikut:
0≤P(A)untuk tiapA;
P(S) = 1;dan
## P

## ∞
## [
i=1
## A
i
## !
## =
## ∞
## X
i=1
## P(A
i
## ).

## 18
## 2.5.  Variabel Random
Teori statistika matematik mengenai pengujian hipotesis, proses stokastik,
dan algoritma optimisasi melibatkan variabel random dan distribusinya. Variabel
random didefinisikan sebagai berikut.
Definisi  2.5.1(Bain  dan  Engelhardt,  1992)  Variabel  random,X,  adalah  sebuah
fungsi yang terdefinisi pada suatu ruang sampel,S, yang memasangkan tiap ke-
mungkinan,s∈S, dengan suatu bilangan real,x. Secara matematik, definisi vari-
abel random sebagai fungsi dapat dinotasikan sebagai:
## X(s) =x.
Variabel random umumnya dinotasikan menggunakan huruf kapital, sedang-
kan nilai-nilai yang dipasangkan oleh variabel random dilambangkan dengan huruf
kecil.
Berdasarkan sifat distribusi probabilitas suatu variabel random, terdapat dua
jenis variabel random, yaitu variabel random diskret dan kontinu.
## 2.5.1.  Variabel Random Diskret
Secara sederhana, variabel random diskret diartikan sebagai variabel ran-
dom yang memetakan bilangan-bilangan bulat. Secara matematis, variabel random
diskret dimaknai sebagai berikut.
Definisi 2.5.2(Bain dan Engelhardt, 1992) Suatu variabel random,X, disebut se-
bagai  variabel  random  diskret  jika  himpunan  semua  kemungkinannya  (possible
values),{x
## 1
## ,x
## 2
,... x
n
## }atau{x
## 1
## ,x
## 2
,...}, adalah suatu himpunan tercacah yang
berhingga atau tak berhingga dan beranggotakan bilangan-bilangan bulat.
Fungsi yang memetakan tiap nilai massa dariX, yaitux
i
, dengan probabi-
litas disebut sebagai fungsi massa peluang (probability mass functionatau PMF)
atau fungsi kepadatan peluang diskret (discrete probability density functionatau
PDF diskret) dan dinotasikan:
f
## X
(x) =P[X=x],  x=x
## 1
## ,x
## 2
## ,...∈Z.

## 19
Suatu fungsi,f
## X
(x), disebut PMF jika dan hanya jika ia memenuhi sifat-sifat:
f
## X
## (x
i
## )≥0
dan
## X
## ∀x
i
f
## X
## (x
i
## ) = 1
untuk sembarang himpunan bilangan real tercacah,{x
i
## },i= 1,2,....
Di  sisi  lain,  fungsi  distribusi  kumulatif  (cumulative  distribution  function
atau CDF) atas suatu variabel random,X, ialah fungsi yang memetakan interval-
interval(−∞,x]menuju probabilitasnya. Menurut Ross (2010), CDF diskret dino-
tasikan:
## F
## X
(x) =P[X≤x] =
## X
## ∀x
i
## ≤x
f
## X
## (x
i
## )
dan terdefinisi untuk tiapx∈R. Suatu fungsiF
## X
(x)disebut CDF atas variabel
randomXjika dan hanya jika ia memenuhi sifat-sifat:
lim
x→−∞
## F
## X
## (x) = 0,(2.4)
lim
x→∞
## F
## X
## (x) = 1,(2.5)
lim
h→0
## +
## F
## X
(x+h) =F
## X
## (x),dan(2.6)
jikaa < b,makaF
## X
(a)≤F
## X
## (b).(2.7)
## 2.5.2.  Variabel Random Kontinu
Definisi variabel random kontinu diberikan sebagai berikut.
Definisi 2.5.3(Bain dan Engelhardt, 1992) Suatu variabel random,X, disebut va-
riabel random kontinu jika terdapat suatu fungsi,f
## X
(x), yang disebut fungsi kepa-
datan peluang kontinu (continuous probability density function atau PDF kontinu)
dariXsedemikian sehingga CDF (kontinu) atasXdapat dirumuskan:
## F
## X
(x) =P[X≤x] =
## Z
x
## −∞
f
## X
## (t)dt
dan memenuhi sifat-sifat yang tertuang pada Persamaan (2.4) hingga (2.7).

## 20
Dengan demikian, PDF kontinu dapat diperoleh sebagai derivatif dari CDF
kontinu, yaitu:
f
## X
## (x) =
d
dx
## F
## X
(x) =F
## ′
## X
## (x)
jika derivatifnya ada. Suatu fungsif
## X
(x)disebut PDF kontinu jika dan hanya jika
ia memenuhi sifat-sifat:
f
## X
## (x)≥0
dan
## Z
## ∞
## −∞
f
## X
## (x)dx= 1
untuk semuax∈R.
## 2.5.3.  Penyokong Variabel Random
Penyokong (support) suatu variabel random didefinisikan sebagai berikut.
Definisi 2.5.4(Hogg dkk., 2005) Penyokong dari suatu variabel random,X, adalah
nilai-nilaiXyang memungkinkan,x, sedemikian sehinggaf
## X
## (x)>0.
Dengan kata lain, penyokong dari suatu variabel random ialah himpunan nilai vari-
abel random tersebut yang mempunyai probabilitas positif.
## 2.5.4.  Distribusi Probabilitas Gabungan
Dalam  menyelesaikan  berbagai  permasalahan  yang  melibatkan  lebih  dari
satu variabel random, misalnyapvariabel random yang termuat dalam vektorX=
## (X
## 1
## ,X
## 2
## ,...,X
p
)dengan  nilai-nilai  termuat  dalam  vektorx=  (x
## 1
## ,x
## 2
## ,...,x
p
## ),
umumnya distribusi probabilitas gabungan (joint probability distribution) akan di-
libatkan. Untuk kasus diskret, PDF gabungan didefinisikan sebagai berikut.
Definisi 2.5.5(Bain dan Engelhardt, 1992) Fungsi kepadatan peluang gabungan
(joint probability density function atau joint PDF) dari variabel random diskret
berdimensip,X= (X
## 1
## ,X
## 2
## ,...,X
p
), didefinisikan sebagai:
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) =P(X
## 1
## =x
## 1
## ,X
## 2
## =x
## 2
## ,...,X
p
## =x
p
## )
untuk semua nilaiXyang mungkin, yaitux= (x
## 1
## ,x
## 2
## ,...,x
p
## ).

## 21
Notasi(X
## 1
## =x
## 1
## ,X
## 2
## =x
## 2
## ,...,X
p
## =x
p
)dapat dipahami sebagai irisan darip
kejadian,(X
## 1
## =x
## 1
## )∩(X
## 2
## =x
## 2
## )∩···∩(X
p
## =x
p
## ).
Suatu PDF gabungan diskret memenuhi sifat-sifat yang tertuang pada teore-
ma berikut.
Teorema 2.5.6(Bain dan Engelhardt, 1992) Suatu fungsi,f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
), me-
rupakan PDF gabungan diskret dari beberapa vektor variabel random,X=
## (X
## 1
## ,X
## 2
## ,...,X
p
), jika dan hanya jika dipenuhi sifat-sifat berikut:
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
)≥0untuk semua nilai yang mungkin,(x
## 1
## ,x
## 2
## ,...,x
p
## ),
dan
## X
## ∀x
## 1
## ···
## X
## ∀x
p
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) = 1.
Lebih lanjut, CDF gabungan diskret didefinisikan sebagai berikut.
Definisi 2.5.7(Bain dan Engelhardt, 1992) Fungsi distribusi kumulatif gabungan
(joint cumulative distribution function) daripvariabel random,X=
## (X
## 1
## ,X
## 2
## ,...,X
p
), didefinisikan sebagai:
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) =P(X
## 1
## ≤x
## 1
## ,X
## 2
## ≤x
## 2
## ,...,X
p
## ≤x
p
## ).
Sifat-sifat CDF gabungan dinyatakan dalam teorema di bawah ini.
Teorema 2.5.8(Bain dan Engelhardt, 1992) Suatu fungsi,F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
), me-
rupakan CDF gabungan daripvariabel random,X= (X
## 1
## ,X
## 2
## ,...,X
p
), jika dan
hanya jika dipenuhi sifat-sifat berikut:
lim
x
i
## →−∞
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
) = 0untuk semuax
i
, i= 1,...,p;
lim
## (x
## 1
## ,x
## 2
## ,...,x
p
## )→(∞,∞,...,∞)
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) = 1;
## P(x
## 1a
## < X
## 1
## ≤x
## 1b
, x
## 2a
## < X
## 2
## ≤x
## 2b
, ..., x
pa
## < X
p
## ≤x
pb
## )≥0
untuk semuax
## 1a
< x
## 1b
, x
## 2a
< x
## 2b
, ..., x
pa
< x
pb
## ;

## 22
dan
lim
h→0
## +
## F
## X
## (x
## 1
## +h,x
## 2
## ,...,x
p
) =  lim
h→0
## +
## F
## X
## (x
## 1
## ,x
## 2
## +h,...,x
p
## )
=···=  lim
h→0
## +
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## +h)
## =F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## )
untuk semuax
## 1
## ,x
## 2
## ,...,x
p
## .
Di sisi lain, untuk kumpulan variabel random kontinu, suatu PDF gabungan
kontinu memenuhi sifat-sifat yang tertuang pada teorema berikut.
Teorema 2.5.9(Bain dan Engelhardt, 1992) Suatu fungsi,f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
), me-
rupakan PDF gabungan kontinu dari beberapa vektor variabel random,X=
## (X
## 1
## ,X
## 2
## ,...,X
p
), jika dan hanya jika dipenuhi sifat-sifat berikut:
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
)≥0untuk semua nilai yang mungkin,(x
## 1
## ,x
## 2
## ,...,x
p
## ),
dan
## Z
## ∞
## −∞
## ···
## Z
## ∞
## −∞
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## )dx
## 1
## ···dx
p
## = 1.
Lebih lanjut, CDF gabungan kontinu didefinisikan sebagai berikut.
Definisi 2.5.10(Bain dan Engelhardt, 1992) Fungsi distribusi kumulatif gabungan
(joint cumulative distribution function) daripvariabel random,X=
## (X
## 1
## ,X
## 2
## ,...,X
p
), didefinisikan sebagai:
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) =
## Z
x
## 1
## −∞
## ···
## Z
x
p
## −∞
f
## X
## (t
## 1
## ,t
## 2
## ,...,t
p
## )dt
## 1
## ···dt
p
untuk semuax= (x
## 1
## ,...,x
k
## ).
Sama halnya pada kasus variabel random tunggal, PDF gabungan kontinu
dapat diperoleh sebagai derivatif parsial dari CDF gabungan, yaitu:
f
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ) =
## ∂
k
## ∂x
## 1
## ···∂x
p
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## )
jika nilai derivatif parsial tersebut ada.

## 23
## 2.5.5.  Distribusi Probabilitas Marginal
Nilai-nilai distribusi probabilitas gabungan dari dua buah variabel random
umumnya dirangkum dalam sebuah tabel. Pada tabel tersebut, tepi (margin) kanan
dan bawah menyajikan probabilitas dari tiap nilai yang memungkinkan dari tiap
variabel random. Oleh karena itu, dapat didefinisikan suatu fungsi bernama PDF
marginal sebagai berikut.
Definisi  2.5.11(Bain  dan  Engelhardt,  1992)  DiberikanX=  (X
## 1
## ,X
## 2
## ,...,X
p
## ),
variabel random berdimensipdengan PDF gabunganf
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
). JikaX
diskret, PDF marginal dariX
j
adalah:
f
## X
j
## (x
j
## ) =
## X
## ···
## X
## ∀i̸=j
f
## X
## 1
## ,...,X
j
## ,...,X
p
## (x
## 1
## ,...,x
j
## ,...,x
p
## ),
sedangkan jikaXkontinu, PDF marginal dariX
j
adalah:
f
## X
j
## (x
j
## ) =
## Z
## ···
## Z
## ∀i̸=j
f
## X
## 1
## ,...,X
j
## ,...,X
p
## (x
## 1
## ,...,x
j
## ,...,x
p
## )dx
## 1
## ···dx
p
## .
Secara umum, pendekatan umum untuk mendefinisikan distribusi marginal
ialah melalui CDF marginal yang didefinisikan sebagai berikut.
Definisi  2.5.12(Bain  dan  Engelhardt,  1992)  DiberikanX=  (X
## 1
## ,X
## 2
## ,...,X
p
## ),
variabel  random  berdimensipdengan  CDF  gabunganF
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ).  CDF
marginal dariX
j
adalah:
## F
## X
j
## (x
j
) =  lim
x
i
## →∞
## F
## X
## (x
## 1
## ,x
## 2
## ,...,x
p
## ),∀i̸=j.
2.6.  Sifat-Sifat Variabel Random
Variabel random mempunyai berbagai sifat yang dinyatakan sebagai ukuran-
ukuran deskriptif. Beberapa sifat tersebut ialah ekspektasi, variansi, deviasi standar,
kovariansi, dan korelasi.
## 2.6.1.  Ekspektasi
Ekspektasi dari suatu variabel random diskret didefinisikan sebagai berikut.

## 24
Definisi 2.6.1(Bain dan Engelhardt, 1992) Ekspektasi dari suatu variabel random
diskret,X, dengan PDF diskretf
## X
(x)didefinisikan sebagai:
## E[X] =
## X
## ∀x
xf
## X
## (x)(2.8)
denganxadalah semua nilai yang mungkin dariX,x=x
## 1
## ,x
## 2
## ,....
Sementara, ekspektasi dari suatu variabel random kontinu diberikan sebagai beri-
kut.
Definisi 2.6.2(Bain dan Engelhardt, 1992) Untuk suatu variabel random kontinu,
X, dengan PDF kontinuf
## X
(x), ekspektasi dariXdidefinisikan sebagai:
## E[X] =
## Z
## ∞
## −∞
xf
## X
## (x)dx(2.9)
jika integralnya konvergen.
Akibat dari Definisi 2.6.2 ialah jika integral tidak konvergen, makaE[X]tidak ada.
Ekspektasi juga disebut sebagai ”mean” atau ”nilai harapan” dan untuk sembarang
variabel random,X, ekspektasi dapat dinotasikan pula sebagaiμ
## X
## .
Salah satu sifat yang terdapat pada ekspektasi ialah linearitas, yang diberik-
an pada teorema berikut.
Teorema 2.6.3(Bain dan Engelhardt, 1992) JikaXadalah suatu variabel random
dengan PDFf
## X
(x), nilai-nilai yang mungkinx
## 1
## ,x
## 2
,..., dan suatu fungsi bernilai
realu(x)yang domainnya adalahx={x
## 1
## ,x
## 2
,...}, maka:
E[u(X)] =
## X
## ∀x
u(x)f
## X
(x),jikaXdiskret; dan(2.10)
E[u(X)] =
## Z
## ∞
## −∞
u(x)f
## X
(x)dx,jikaXkontinu.(2.11)
## 2.6.2.  Variansi
Variansi dari suatu variabel random didefinisikan sebagai berikut.
Definisi 2.6.4(Bain dan Engelhardt, 1992) Variansi dari suatu variabel random,
X, dirumuskan sebagai:
Var(X) =E
## 
## (X−E[X])
## 2
## 
## .(2.12)

## 25
Variansi dapat dipandang sebagai bentuk khusus dari sifat linearitas ekspek-
tasi, yaitu Persamaan (2.10) atau (2.11) denganu(x)  =  (x−μ
## X
## )
## 2
. Variansi dari
suatu variabel random,X, juga dapat dinotasikan sebagaiσ
## 2
## X
atauV(X). Variansi
menyatakan ukuran variabilitas atau sebaran dari distribusi suatu variabel random.
## 2.6.3.  Deviasi Standar
Definisi deviasi standar diberikan sebagai berikut.
Definisi  2.6.5(Bain  dan  Engelhardt,  1992)  Deviasi  standar  dari  suatu  variabel
random,X, adalah akar kuadrat positif dari variansinya, yaitu:
σ
## X
## =
p
Var(X).
Deviasi  standar  dari  suatu  variabel  random,X,  juga  dapat  dinotasikan  sebagai
## SD(X).
## 2.6.4.  Kovariansi
Kovariansi merupakan salah satu sifat variabel random yang melibatkan dua
buah variabel random. Kovariansi didefinisikan sebagai berikut.
Definisi 2.6.6(Bain dan Engelhardt, 1992) Kovariansi dari dua buah variabel ran-
dom,XdanY, ialah ukuran hubungan antara kedua variabel random yang diru-
muskan sebagai:
Cov(X,Y) =E
## 
## (X−E[X])(Y−E[Y])
## 
## =E[XY]−E[X]E[Y].(2.13)
Kovariansi dari dua buah variabel random,XdanY, juga dapat dinotasikan dengan
lambangσ
## XY
## .
Sifat-sifat kovariansi diberikan sebagai berikut.
Teorema 2.6.7(Bain dan Engelhardt, 1992) JikaXdanYadalah dua buah vari-
abel random sertaadanbadalah dua buah konstanta, maka terpenuhi sifat-sifat
kovariansi berikut:
Cov(aX,bY) =abCov(X,Y);

## 26
Cov(X+a,Y+b) = Cov(X,Y);dan
Cov(X,aX+b) =aVar(X).
Selain itu, untuk dua buah variabel random yang saling independen, berlaku
pula sifat kovariansi berikut.
Teorema 2.6.8(Bain dan Engelhardt, 1992) JikaXdanYadalah dua buah vari-
abel random yang saling independen, makaCov(X,Y) = 0.
## 2.6.5.  Korelasi
Korelasi antara dua buah variabel random didefinisikan sebagai berikut.
Definisi 2.6.9(Bain dan Engelhardt, 1992) JikaXdanYadalah dua buah variabel
random  dengan  variansi  berturut-turutσ
## 2
## X
danσ
## 2
## Y
serta  kovariansiσ
## XY
,  maka
koefisien korelasi dariXdanYdiberikan sebagai:
ρ
## XY
## =
σ
## XY
σ
## X
σ
## Y
## .(2.14)
Korelasi dari dua buah variabel random,XdanY, juga dapat dinotasikan sebagai
Cor(X,Y).
Jika variabel randomXdanYmempunyaiρ= 0, kedua variabel random
tersebut dikatakan tidak berkorelasi. Pada keadaan lainnya, kedua variabel random
disebut berkorelasi.
## 2.7.  Analisis Multivariat
Menurut Johnson dan Winchern (2007), analisis multivariat adalah metode-
metode statistik dan pengukuran terhadap data yang terdiri atas banyak variabel.
Analisis multivariat bertujuan untuk mengumpulkan informasi berdasarkan kum-
pulan variabel yang terlibat dalam penelitian-penelitian ilmiah.
Berdasarkan tujuannya, terdapat lima kelompok analisis multivariat, yaitu:
-  Reduksi data atau penyederhanaan struktur data, yang ditujukan untuk mema-
parkan suatu fenomena dengan cara yang sesederhana mungkin tanpa menghi-
langkan informasi yang bernilai;

## 27
-  Pengurutan dan pengelompokan objek atau variabel berdasarkan kesamaan ciri-
ciri tertentu;
-  Identifikasi dependensi antarvariabel;
-  Prediksi yang didasarkan pada hubungan antarvariabel; dan
-  Penyusunan dan pengujian hipotesis atas parameter-parameter populasi multiva-
riat, yang ditujukan untuk memvalidasi asumsi-asumsi tertentu atau memperkuat
temuan-temuan ilmiah terdahulu.
Data yang dilibatkan dalam analisis multivariat terdiri atas banyak variabel.
Secara umum, data multivariat tersaji dalam wujud larikXsebagai berikut:
## X=
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
x
## 11
x
## 12
## ···x
## 1k
## ···x
## 1p
x
## 21
x
## 22
## ···x
## 2k
## ···x
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
x
j1
x
j2
## ···x
jk
## ···x
jp
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
x
n1
x
n2
## ···x
nk
## ···x
np
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## .
LarikXdi atas terdiri atasnbaris danp≥1kolom. Baris melambangkanitem,
individu, atau unit eksperimen, sedangkan kolom mewakili variabel atau karakte-
ristik yang diamati dari tiapitem. Notasix
jk
dapat diinterpretasikan sebagai nilai
variabel ke-kdariitemke-j.
Serupa halnya dengan data multivariat itu sendiri, statistik-statistik deskrip-
tif dari suatu data multivariat, seperti mean, variansi, dan kovariansi, juga disajik-
an sebagai larik. Vektor mean dan matriks kovariansi didefinisikan pada subbab-
subbab di bawah ini.
## 2.7.1.  Vektor Mean
Misalkanpvariabel random terkumpul dalam sebuah vektor,
## X
## ′
## = [X
## 1
## ,X
## 2
## ,...,X
p
## ].(2.15)
Maka, tiap elemenX
## ′
, yaituX
i
, i= 1,...,p, adalah suatu variabel random dengan
distribusi probabilitas marginal masing-masing. Ekspektasi marginal dari tiapX
i

## 28
didefinisikan sebagai:
μ
i
## =E[X
i
## ] =
## 
## 
## 
## 
## 
## P
## ∀x
i
x
i
f
## X
i
## (x
i
),jikaX
i
adalah variabel random diskret;
## R
## ∞
## −∞
x
i
f
## X
i
## (x
i
## )dx
i
,jikaX
i
adalah variabel random kontinu;
denganf
## X
i
## (x
i
)adalah PDF dariX
i
## .
Kumpulan ekspektasi dari vektor randomXpada Persamaan (2.15) dapat
dinyatakan sebagai vektor mean berikut:
## E[X] =
## 
## 
## 
## 
## 
## 
## 
## 
## E[X
## 1
## ]
## E[X
## 2
## ]
## .
## .
## .
## E[X
p
## ]
## 
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 
μ
## 1
μ
## 2
## .
## .
## .
μ
p
## 
## 
## 
## 
## 
## 
## 
## 
## =μ.
(Johnson dan Winchern, 2007)
## 2.7.2.  Matriks Kovariansi
Misalkanpvariabel random dikumpulkan dalam sebuah vektor sebagaima-
na diberikan pada Persamaan (2.15). Variansi dari tiapX
i
didefinisikan sebagai:
σ
## 2
i
## =
## 
## 
## 
## 
## 
## P
## ∀x
i
## (x
i
## −μ
i
## )
## 2
f
## X
i
## (x
i
),jikaX
i
adalah variabel random diskret;
## R
## ∞
## −∞
## (x
i
## −μ
i
## )
## 2
f
## X
i
## (x
i
## )dx
i
,jikaX
i
adalah variabel random kontinu;
denganf
## X
i
## (x
i
)adalah  PDF  dariX
i
.  Lebih  lanjut,  hubungan  antara  tiap  pasang
variabel random,X
i
danX
k
, dapat dinyatakan sebagai kovariansi yang dirumuskan
sebagai berikut:
σ
ik
## =E[(X
i
## −μ
i
## )(X
k
## −μ
k
## )](2.16)
## =
## 
## 
## 
## 
## 
## P
## ∀x
i
## P
## ∀x
k
## (x
i
## −μ
i
## )(x
k
## −μ
k
## )f
## X
i
## ,X
k
## (x
i
## ,x
k
## );
## R
## ∞
## −∞
## R
## ∞
## −∞
## (x
i
## −μ
i
## )(x
k
## −μ
k
## )f
## X
i
## ,X
k
## (x
i
## ,x
k
## )dx
i
dx
k
## (2.17)
denganf
## X
i
## ,X
k
## (x
i
## ,x
k
)adalah PDF gabungan dariX
i
danX
k
sertai,k= 1,...,p.
Kasus pertama berlaku untukX
i
danX
k
merupakan variabel-variabel random dis-
kret, sedangkan kasus kedua untukX
i
danX
k
merupakan variabel-variabel random

## 29
kontinu. Melalui definisi kovariansi pada Persamaan (2.17), variansi marginal dari
tiapX
i
juga dapat dinotasikan sebagaiσ
ii
## .
Serupa  halnya  dengan  vektor  mean,  berdasarkan  Johnson  dan  Winchern
(2007), kumpulan variansi dan kovariansi dari vektor random,X, dapat dinyatakan
sebagai matriks variansi-kovariansi yang didefinisikan sebagai berikut:
Σ= Cov(X)
## =E
## 
(X−μ)(X−μ)
## ′
## 
## =E
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## X
## 1
## −μ
## 1
## X
## 2
## −μ
## 2
## .
## .
## .
## X
p
## −μ
p
## 
## 
## 
## 
## 
## 
## 
## 
h
## X
## 1
## −μ
## 1
## X
## 2
## −μ
## 2
## ···X
p
## −μ
p
i
## 
## 
## 
## 
## 
## 
## 
## 
## =E
## 
## 
## 
## 
## 
## 
## 
## 
## (X
## 1
## −μ
## 1
## )
## 2
## (X
## 1
## −μ
## 1
## )(X
## 2
## −μ
## 2
## )···(X
## 1
## −μ
## 1
## )(X
p
## −μ
p
## )
## (X
## 2
## −μ
## 2
## )(X
## 1
## −μ
## 1
## )(X
## 2
## −μ
## 2
## )
## 2
## ···(X
## 2
## −μ
## 2
## )(X
p
## −μ
p
## )
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## (X
p
## −μ
p
## )(X
## 1
## −μ
## 1
## )   (X
p
## −μ
p
## )(X
## 2
## −μ
## 2
## )···(X
p
## −μ
p
## )
## 2
## 
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## E[(X
## 1
## −μ
## 1
## )
## 2
## ]E[(X
## 1
## −μ
## 1
## )(X
## 2
## −μ
## 2
## )]···E[(X
## 1
## −μ
## 1
## )(X
p
## −μ
p
## )]
## E[(X
## 2
## −μ
## 2
## )(X
## 1
## −μ
## 1
## )]E[(X
## 2
## −μ
## 2
## )
## 2
## ]···E[(X
## 2
## −μ
## 2
## )(X
p
## −μ
p
## )]
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## E[(X
p
## −μ
p
## )(X
## 1
## −μ
## 1
## )]E[(X
p
## −μ
p
## )(X
## 2
## −μ
## 2
## )]···E[(X
p
## −μ
p
## )
## 2
## ]
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 
σ
## 11
σ
## 12
## ···σ
## 1p
σ
## 21
σ
## 22
## ···σ
## 2p
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
σ
p1
σ
p2
## ···σ
pp
## 
## 
## 
## 
## 
## 
## 
## 
## .(2.18)
Salah satu sifat matriks kovariansi ialah semidefinit positif. Jika ditentukan
suatu vektor sembarang berukuranm×1,a, diperoleh bentuk kuadrat dari suatu
matriks kovariansi yang dibangun daripvariabel random,Σ, sebagai:
a
## ′
## Σa=a
## ′
## E
## 
(X−μ)(X−μ)
## ′
## 
a.(2.19)
Oleh karena sifat linearitas ekspektasi, Persamaan (2.19) dapat dituliskan kembali

## 30
sebagai:
a
## ′
Σa=E
## 
a
## ′
(X−μ)(X−μ)
## ′
a
## 
## .
Diperhatikan bahwaa
## ′
(X−μ)dan(X−μ)
## ′
amerupakan dua buah skalar yang sa-
ma. Jika kedua skalar tersebut dinyatakan sebagai suatu variabel random,Y, maka:
a
## ′
Σa=E
## 
## Y
## 2
## 
## .(2.20)
## Y
## 2
juga dapat dipandang sebagai suatu variabel random yang nonnegatif. Mengi-
ngat bahwa PMF dan PDF selalu bernilai nonnegatif untuk tiap nilai yang mungkin
dari suatu variabel random, ekspektasi dariY
## 2
bernilai nonnegatif. Dengan demiki-
an, bentuk kuadrat pada Persamaan (2.20) bernilai nonnegatif, membuktikan bahwa
matriks kovariansi merupakan sebuah matriks semidefinit positif.
Selayaknya matriks persegi lainnya, matriks kovariansi invers,Σ
## −1
, terdefi-
nisi untuk suatu matriks kovariansi,Σ, jikaΣnonsingular.
## 2.7.3.  Jarak Euclid
Johnson dan Winchern (2007) menyebutkan bahwa kebanyakan analisis mul-
tivariat didasarkan pada konsep sederhana tentang jarak. Salah satu ukuran jarak
yang cukup terkenal adalah jarak Euclid (Euclidean distance). Rumusan jarak Eu-
clid diberikan sebagai berikut.
Definisi 2.7.1(Johnson dan Winchern, 2007) Jarak garis lurus atau jarak Euclid
antara dua titik sembarang,P= (x
## 1
## ,x
## 2
## ,...,x
p
)danQ= (y
## 1
## ,y
## 2
## ,...,y
p
), dibe-
rikan sebagai:
d(P,Q) =
q
## (x
## 1
## −y
## 1
## )
## 2
## + (x
## 2
## −y
## 2
## )
## 2
## +...+ (x
p
## −y
p
## )
## 2
## .(2.21)
Dengan memandang titikPsebagai vektorpdan titikQsebagai vektorq, Persa-
maan (2.21) ekuivalen dengan operasi vektor berikut:
d(p,q) =
p
## (p−q)
## ′
## (p−q).
## 2.7.4.  Analisis Klaster
Menurut Johnson dan Winchern (2007), analisis klaster adalah metode pe-
ngelompokan data yang tidak mengasumsikan banyak atau struktur kelompok. Pe-

## 31
ngelompokan dilakukan berdasarkan kesamaan atau ketaksamaan yang umumnya
diindikasikan oleh jarak. Jarak Euclid merupakan pilihan jarak yang baik dalam
analisis klaster.
Secara umum, Han dkk. (2012) mengelompokkan metode-metode analisis
klaster  menjadi  empat,  yaitu  partisi,  hierarkis,  berbasis  kepadatan,  dan  berbasis
grid. Metode-metode partisi mempartisi sekumpulan data mula-mula menjadiK
klaster, lalu mengembangkan kualitas klaster-klaster yang terbentuk melalui relo-
kasi  iteratif.  Partisi  yang  baik  mengelompokkan  objek-objek  yang  serupa  dalam
satu klaster dan objek-objek yang berbeda dalam klaster yang berbeda. Metode-
metode hierarkis melibatkan peleburan (aglomerasi) atau pembagian (divisi) dari
sekumpulan data. Sementara, metode-metode berbasis kepadatan merupakan pe-
ngembangan dari metode-metode partisi. Metode-metode berbasis kepadatan mem-
bentuk  klaster-klaster  sedemikian  sehingga  jumlah  objek  tetangga  di  sekitar  su-
atu objek pada radius tertentu setidaknya mencapai batas jumlah tertentu. Adapun
metode-metode berbasisgridmenguantisasi ruang objek menjadi sejumlah sel yang
membentuk  suatu  strukturgrid.  Metode-metode  ini  efisien  untuk  permasalahan-
permasalahan data spasial.
## 2.8.  Distribusi Probabilitas
Berikut merupakan beberapa jenis distribusi probabilitas.
## 2.8.1.  Distribusi Bernoulli
Menurut Bain dan Engelhardt (1992), percobaan Bernoulli ialah pelaksa-
naan suatu eksperimen dengan hanya dua kemungkinan luaran. Jika kemungkinan
luaran tersebut dilambangkan denganEdanE
## ′
, maka variabel Bernoulli dapat di-
definisikan melalui persamaan:
## X(e) =
## 
## 
## 
## 
## 
1,jikae∈E
0,jikae∈E
## ′
## .
Distribusi yang berkorespondensi dengan variabel Bernoulli disebut distri-
busi Bernoulli, yang didefinisikan sebagai berikut.

## 32
Definisi 2.8.1(Bain dan Engelhardt, 1992) Suatu variabel random,X, mengikuti
distribusi Bernoulli jika variabel random tersebut mempunyai PDF:
f
## X
## (x) =p
x
q
## 1−x
,  x= 0,1.
Dengan kata lain,f
## X
## (0) =qdanf
## X
## (1) =p.
## 2.8.2.  Distribusi Binomial
Percobaan Bernoulli sering kali dilakukan secara berulang dan saling inde-
penden. Jika terdapatnpercobaan Bernoulli yang saling independen dan peluang
sukses pada tiap percobaan ialahp, maka dapat didefinisikan suatu variabel random,
X, yang menyatakan banyaknya sukses dari serangkaian percobaan tersebut. Vari-
abel randomXtersebut mempunyai distribusi binomial yang didefinisikan sebagai
berikut.
Definisi 2.8.2(Bain dan Engelhardt, 1992) Suatu variabel random,X, mengikuti
distribusi binomial jika variabel random tersebut mempunyai PDF:
f
## X
## (x;n,p) =
## 
## 
n
x
## 
## 
p
x
q
n−x
,  x= 0,1,...,n.
Variabel random pada Definisi 2.8.2 di atas dapat dinotasikan sebagaiX∼
BIN(n,p).
## 2.8.3.  Distribusi Poisson
Distribusi Poisson didefinisikan sebagai berikut.
Definisi 2.8.3(Bain dan Engelhardt, 1992) Suatu variabel random diskret,X, meng-
ikuti  distribusi  Poisson  dengan  parameterμ >0jika  variabel  random  tersebut
mempunyai PDF:
f
## X
## (x;μ) =
e
## −μ
μ
x
x!
,  x= 0,1,2,....
Variabel random pada Definisi 2.8.3 di atas dapat dinotasikan sebagaiX∼
POI(μ).

## 33
## 2.8.4.  Distribusi Uniform
Barisan bilangan random berkaitan erat dengan distribusi uniform. Definisi
dari distribusi uniform diberikan sebagai berikut.
Definisi 2.8.4(Bain dan Engelhardt, 1992) Suatu variabel random,X, mengikuti
distribusi uniform pada interval(a,b)jika variabel random tersebut mempunyai
## PDF:
f
## X
## (x;a,b) =
## 1
b−a
,  a < x < b,
dan bernilai nol untuk nilaixlainnya.
Variabel random pada Definisi 2.8.4 di atas dapat dinotasikan sebagaiX∼
UNIF(a,b).
## 2.8.5.  Distribusi Normal
Distribusi normal didefinisikan sebagai berikut.
Definisi 2.8.5(Bain dan Engelhardt, 1992) Suatu variabel random,X, mengikuti
distribusi normal atau distribusi Gauss dengan meanμdan variansiσ
## 2
jika varia-
bel random tersebut mempunyai PDF (kontinu):
f
## X
## (x;μ,σ
## 2
## ) =
## 1
σ
## √
## 2π
exp
## 
## −
## (
x−μ
σ
## )
## 2
## 2
## 
## (2.22)
untuk−∞< x <∞, dengan−∞< μ <∞dan0< σ <∞.
Variabel random pada Definisi 2.8.5 dapat dinotasikan sebagaiX∼N(μ,σ
## 2
## ).
Dengan melakukan substitusiz=  (x−μ)/σterhadap PDF normal pada
Persamaan (2.22), diperoleh PDF normal standar yang dinotasikan sebagaiφ(z)
dan dirumuskan sebagai:
φ(z) =
## 1
## √
## 2π
exp
## 
## −
z
## 2
## 2
## 
,−∞< z <∞.(2.23)
CDF normal standar yang berkorespondensi dirumuskan sebagai:
## Φ(z) =
## Z
z
## −∞
φ(t)dt.(2.24)

## 34
Suatu variabel random,Z, yang berdistribusi normal standar dapat dinotasikan se-
bagaiZ∼N(0,1).
Suatu variabel random yang berdistribusi normal memenuhi teorema beri-
kut.
Teorema  2.8.6(Bain  dan  Engelhardt,  1992)  Jika  suatu  variabel  randomX∼
## N(μ,σ
## 2
), maka terpenuhi teorema bahwa:
## Z=
## X−μ
σ
## ∼N(0,1)
dan
## F
## X
## (x) = Φ
## 
## X−μ
σ
## 
## .
Distribusi normal umum digunakan dalam pengambilan keputusan, penen-
tuan jenis uji hipotesis, hingga pembangkitan bilangan random.
2.9.  BilanganPseudo-Random
Sebagai istilah yang lebih umum, barisan bilangan random perlu dipahami
terlebih dahulu.
Definisi 2.9.1(Ripley, 1987) Barisan bilangan random,{U
i
}, adalah sebuah ba-
risan beranggotakan variabel-variabel random independen yang berdistribusi uni-
form pada interval(0,1).
Dari segi kebahasaan, awalan ”pseudo-” berarti palsu. Maka, definisi bilang-
anpseudo-randomsangat erat dengan bilangan random, tetapi tidak serupa.
Definisi 2.9.2(Ripley, 1987) Suatu barisan bilangan pseudo-random,{U
i
}, adalah
sebuah barisan bilangan deterministik dalam interval[0,1]yang mempunyai sifat-
sifat statistik yang relevan dengan suatu barisan bilangan random.
Pada Definisi 2.9.2 di atas, ”sifat statistik yang relevan” bermaksud bahwa pengu-
jian statistik apapun yang bertujuan untuk menguji kerandoman terhadap bagian
berhingga dari{U
i
}tidak menolak hipotesis nol, yaitu bahwa data bilangan terse-
but bersifat random (Ripley, 1987).

## 35
## 2.10.  Sampel Random
Suatu kumpulan variabel random dapat disebut sebagai sampel random jika
memenuhi definisi berikut.
Definisi 2.10.1(Bain dan Engelhardt, 1992) Suatu himpunan variabel random,
## X
## 1
## ,...,X
n
,  disebut  sampel  random  berukuranndari  sebuah  populasi  dengan
PDFf
## X
(x)jika PDF gabungan dari himpunan variabel random tersebut berben-
tuk:
f
## X
## 1
## ,...,X
n
## (x
## 1
## ,x
## 2
## ,...,x
n
## ) =f
## X
## 1
## (x
## 1
## )f
## X
## 2
## (x
## 2
## )···f
## X
n
## (x
n
## ) =
n
## Y
i=1
f
## X
i
## (x
i
## ).
Dengan kata lain, himpunan variabel random,X
## 1
## ,...,X
n
, disebut sampel random
dari suatu variabel random,X, jika variabel-variabel random tersebut saling inde-
penden dan mempunyai distribusi yang sama denganX. Pada peristiwa ini, dapat
disebutkan bahwaX
## 1
## ,...,X
n
bersifat IID (independent and identically distribu-
ted).
## 2.11.  Pengujian Hipotesis
Berdasarkan Hogg dkk. (2005), salah satu permasalahan dalam bidang sta-
tistik adalah diberikan suatu variabel random,X, dengan PDFf
## X
(x;θ), tetapi para-
meter distribusinya, yaituθ, tidak diketahui. Parameterθadalah elemen dari suatu
himpunan tertentu,Ω. Jika ditentukanω
## 0
danω
## 1
adalah dua buah sub-himpunan
dariΩsertaω
## 0
## ∪ω
## 1
= Ω, pasangan hipotesis diberikan sebagai berikut:
## H
## 0
## :θ∈ω
## 0
versusH
## 1
## :θ∈ω
## 1
## .
## H
## 0
disebut hipotesis nol (null hypothesis), sedangkanH
## 1
disebut hipotesis alterna-
tif.
MisalkanSadalah penyokong dari sampel random,X
## ′
## =  (X
## 1
## ,...,X
n
## ).
PengujianH
## 0
terhadapH
## 1
didasarkan pada himpunanC⊆ Syang disebut daerah
kritik.  Daerah  kritik  berkorespondensi  dengan  penolakan  hipotesis  nol  sehingga
aturan pengambilan keputusan dari suatu pengujian hipotesis ialah:
tolakH
## 0
,jikaX∈C;

## 36
terimaH
## 0
,jikaX∈C
c
## .
Untuk suatu daerah kritik, terdapat empat kemungkinan hasil yang terang-
kum pada Tabel 2.1. Galat tipe I (type I error) terjadi apabilaH
## 0
ditolak ketikaH
## 0
## Tabel 2.1 Tabel Keputusan 2×2 Pengujian Hipotesis
## Keputusan
## Kejadian Sesungguhnya
## H
## 0
benarH
## 1
benar
TolakH
## 0
Galat tipe IKeputusan tepat
TerimaH
## 0
Keputusan tepatGalat tipe II
benar, sedangkan galat tipe II (type II error) terjadi apabilaH
## 0
diterima ketikaH
## 1
benar. Galat tipe I sering kali dipandang lebih buruk daripada galat tipe II sehing-
ga dalam suatu pengujian hipotesis, dipilih daerah-daerah kritik dengan batasanα
yang didefinisikan sebagai berikut.
Definisi 2.11.1(Hogg dkk., 2005) Suatu daerah kritik,C, dikatakan berukuranα
jika
α= max
θ∈ω
## 0
## P
θ
## [(X
## 1
## ,...,X
n
## )∈C].
Selain sebagai ukuran uji,αjuga dapat dipahami sebagai probabilitas terjadinya ga-
lat tipe I yang disebut juga tingkat signifikansi suatu uji hipotesis (Bain dan Engel-
hardt, 1992). Dari antara daerah-daerah kritik berukuranαini, dipilih daerah kritik
yang meminimalkan probabilitas galat tipe II, yaituβ. Dengan kata lain, daerah
kritik yang dipilih memaksimalkan probabilitasH
## 0
ditolak ketikaH
## 1
benar, yaitu
memaksimalkan:
1−β=P
θ
## [(X
## 1
## ,...,X
n
)∈C],  θ∈ω
## 1
## .(2.25)
Probabilitas pada ruas kanan Persamaan (2.25) disebut kekuatan pengujian diθ.
Probabilitas ini dapat didefinisikan sebagai fungsi kekuatan (power function) seba-
gai berikut.
Definisi  2.11.2(Hogg  dkk.,  2005)  Fungsi  kekuatan  dari  suatu  daerah  kritik,C,

## 37
didefinisikan sebagai:
γ
## C
(θ) =P
θ
## [(X
## 1
## ,...,X
n
)∈C],  θ∈ω
## 1
## .
Jika diberikan dua buah daerah kritik,C
## 1
danC
## 2
, yang keduanya berukuranα,C
## 1
dikatakan lebih baik daripadaC
## 2
jikaγ
## C
## 1
(θ)> γ
## C
## 2
(θ)untuk seluruhθ∈ω
## 1
## .
Sejauh perkembangan ilmu statistika dan implementasinya pada penelitian
di berbagai bidang ilmu, tidak pernah ditentukan ukuranαyang terbaik untuk me-
nolakH
## 0
dan mendukungH
## 1
secara kuat, maka tiap peneliti dapat menentukan
nilaiαsecara subjektif dan memperoleh kesimpulan yang berbeda untuk sekum-
pulan data yang sama dan penelitian yang sama. Guna menangani permasalahan
ini, diperlukan suatu ukuran bernamap-value(nilaip) yang didefinisikan sebagai
berikut.
Definisi 2.11.3(Bain dan Engelhardt, 1992) Suatu p-value dari suatu pengujian
hipotesis ialah nilaiαterkecil yang mampu menolakH
## 0
berdasarkan nilai teramati
dari statistik uji yang bersangkutan.
2.12.  Uji Kolmogorov-Smirnov
Uji Kolmogorov-Smirnov merupakan suatu ujigoodness-of-fit, yaitu uji sta-
tistik yang membandingkan kesamaan distribusi suatu sampel data teramati dengan
suatu distribusi populasi teoritis yang diharapkan berdasarkan distribusi frekuen-
si kumulatif dari kedua distribusi tersebut. Data yang dilibatkan dalam suatu uji
Kolmogorov-Smirnov  diasumsikan  berasal  dari  suatu  distribusi  kumulatif  konti-
nu sehingga uji ini dapat digunakan untuk data yang setidaknya berskala ordinal
(Kraska-Miller, 2013).
Dalam menguji normalitas data, yaitu apakah suatu sampel data mengiku-
ti  distribusi  normal  dengan  parameter-parameter  tertentu,  pasangan  hipotesis  uji
Kolmogorov-Smirnov dinyatakan sebagai:
## H
## 0
:Data terdistribusi normal;
## H
## 1
:Data tidak terdistribusi normal.

## 38
Statistik uji yang digunakan adalah selisih maksimum antara distribusi sampel de-
ngan distribusi teoritis yang disebut deviansi maksimum (D) dan didefinisikan se-
bagai:
D= max|F
## 0
## (x
i
## )−S
n
## (x
i
)|,  i= 1,2,...,N
denganF
## 0
## (x
i
)adalah nilai terduga (terhipotesis) darix
i
danS
n
## (x
i
)adalah nilai
teramati darix
i
. Hipotesis nol ditolak jikaDbernilai lebih besar dari nilai kritik,
## D
α,N
, yang bergantung pada ukuran uji,α, dan ukuran sampel,N.
Uji-ujigoodness-of-fit, seperti uji Kolmogorov-Smirnov, berperan penting
ketika terdapat asumsi distribusi teoritis yang perlu dipenuhi oleh data sampel da-
lam kerangka suatu metode statistik. Akan tetapi, ketika berhadapan dengan sampel
data runtun waktu, diperlukan metode-metode lain untuk menginterpretasikan dan
memodelkan dinamika data tersebut dalam kurun waktu data yang bersangkutan.
Pada umumnya, metode-metode dengan kapabilitas tersebut didasari oleh konsep
proses stokastik, yang diberikan pada subbab berikut.
## 2.13.  Proses Stokastik
Menurut Ross (2010), proses stokastik adalah sekumpulan variabel random
yang menjelaskan evolusi suatu proses seiring waktu. Secara umum, proses sto-
kastik dinotasikan sebagai{X(t),t∈T}.tsering kali diinterpretasikan sebagai
waktu yang termuat dalam himpunan indeks,T. JikaTadalah himpunan tercacah,
maka proses stokastik disebut proses waktu diskret (discrete-time process). Semen-
tara, jikaTadalah himpunan nilai dalam suatu interval bilangan real, maka proses
stokastik disebut proses waktu kontinu (continuous-time process).X(t)dimaknai
sebagaistateproses pada waktu ke-tdan juga dapat dinotasikan sebagaiX
t
## . Him-
punan semua nilai yang memungkinkan dariX(t)disebut ruangstate(state space)
dari proses stokastik.
## 2.13.1.  Rantai Markov
Rantai Markov merupakan salah satu proses stokastik khusus dengan defi-
nisi diberikan sebagai berikut.

## 39
Definisi 2.13.1(Ross, 2010) Diberikan suatu proses stokastik,{X
t
## ,t= 0,1,2,...},
dengan ruang state tercacah. Rantai Markov adalah sebuah model probabilitas da-
ri suatu barisan nilai proses stokastik yang berurutan,X
## 0
## ,X
## 1
## ,X
## 2
,..., yang meme-
nuhi asumsi berikut:
## P
##  
## X
t+1
=j|X
t
## =i, X
t−1
## =i
t−1
## ,..., X
## 1
## =i
## 1
## , X
## 0
## =i
## 0
## 
## =P
ij
## ,
denganX
t
=iberarti proses berada pada stateipada waktutdanP
ij
adalah pro-
babilitas proses pada stateimenuju statej, untuk seluruh state,i
## 0
## ,i
## 1
## ,...,i
t−1
## ,i,j≥
0, dan seluruht≥0.
Dengan kata lain, rantai Markov memenuhi asumsi bahwa jika diberikan proses-
proses saat ini dan masa lalu, probabilitas bersyarat dari proses yang akan datang,
## X
t+1
, hanya bergantung pada proses saat ini,X
t
## .
Dengan adanya sifat probabilitas, rantai Markov memenuhi:
## P
ij
## ≥0;
i,j≥0;dan
## ∞
## X
j=0
## P
ij
= 1,  i= 0,1,....
Nilai-nilai  probabilitas  transisi  satu  tahap,P
ij
,  dapat  dikumpulkan  dalam
matriksPyang didefinisikan sebagai:
## P=
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## P
## 00
## P
## 01
## P
## 02
## ···
## P
## 10
## P
## 11
## P
## 12
## ···
## .
## .
## .
## .
## .
## .
## .
## .
## .
## P
i0
## P
i1
## P
i2
## ···
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## .
MatriksPdi atas disebut sebagai matriks transisi.
2.13.2.  ProsesRandom Walk
Definisi prosesrandom walkdiberikan sebagai berikut.

## 40
Definisi 2.13.2(Ross, 2010) Suatu rantai Markov dengan ruang state berupa bilangan-
bilangan bulat,i=  0,±1,±2,..., disebut random walk jika untuk beberapa bi-
langan,0< p <1, dipenuhi:
## P
i,i+1
=p= 1−P
i,i−1
,  i= 0,±1,....
Prosesrandom walkdinamakan demikian karena dapat dimodelkan seperti
seseorang  yang  berjalan  pada  suatu  garis  lurus  yang  pada  tiap  titik  waktu  akan
berjalan ke salah satu arah dengan peluangpatau ke arah lainnya dengan peluang
## (1−p).
Salah satu aplikasi umum dari prosesrandom walkialah peramalan harga
aset perusahaan. Dalam hal ini, prosesrandom walkmendasari bahwa harga aset
merupakan suatu nilai acak yang tidak dapat diprediksi menggunakan informasi
historisnya. Keacakan ini dipengaruhi oleh situasi ekonomi yang tidak terlepas dari
peran dan kondisi perusahaan-perusahaan dalam suatu negara. Bahasan mengenai
perusahaan termuat pada subbab berikut.
## 2.14.  Perusahaan
Menurut Berk dan DeMarzo (2016), perusahaan atau korporasi merupak-
an salah satu bentuk badan usaha yang diakui secara hukum sebagai suatu entitas
hukum yang terpisah dari pemilik-pemilik-nya. Perusahaan dicirikan dengan tidak
adanya batasan jumlah pemilik. Ke-pemilikan perusahaan terbagi-bagi dalam wu-
jud saham.
Perusahaan melaporkan performa keuangannya secara triwulanan (quarter-
ly) atau tahunan melalui pelaporan akuntansi yang disebut laporan keuangan (finan-
cial statement). Salah satu laporan keuangan yang perlu disusun oleh perusahaan
adalah neraca keuangan (balance sheet). Neraca keuangan adalah pernyataan posisi
keuangan perusahaan yang memuat harta, utang, dan modal. Dalam ilmu ekonomi,
ketiga komponen neraca keuangan ini disebut juga aset, liabilitas, dan ekuitas. Se-
lanjutnya, Penulis hanya akan memperdalam bahasan mengenai aset.
Aset terbagi menjadi aset tetap dan aset jangka panjang. Aset tetap ialah kas
atau aset yang dapat dialihkan menjadi kas dalam kurun waktu satu tahun, seperti

## 41
sekuritas, piutang, persediaan, sewa, dan pembayaran di muka. Di sisi lain, aset
jangka panjang termasuk peralatan,plant(meliputi tanah, bangunan, dan mesin),
dan perlengkapan.
## 2.15.  Investasi
Menurut Virlics (2013), investasi adalah pengeluaran yang dikeluarkan oleh
seseorang atau sebuah perusahaan untuk memperoleh keuntungan pada waktu men-
datang. Pertimbangan untuk melakukan suatu investasi didasarkan padareturndan
risiko yang mungkin diperoleh dari suatu aset perusahaan atau sekuritas keuangan.
Returndidefinisikan sebagai persentase peningkatan nilai untuk tiap satuan
mata uang yang diinvestasikan, sedangkan risiko, ialah hal-hal yang menghambat
kembalinyareturndalam berinvestasi, seperti situasi ekonomi dan finansial yang
sedang terjadi (Virlics, 2013). Terdapat dua jenis risiko investasi, yaitu risiko umum
(common risk) dan risiko independen. Risiko umum ialah risiko dengan korelasi
sempurna. Di sisi lain, risiko independen ialah risiko yang tidak berkorelasi. Berk
dan DeMarzo (2016) mengangkat contoh kasus di suatu permukiman untuk mem-
perjelas pemahaman dari kedua risiko ini. Gempa bumi yang menyerang wilayah
suatu permukiman merupa-kan contoh risiko umum karena merugikan semua ru-
mah secara merata, sedangkan perampokan merupakan risiko independen karena
kejadian perampokan untuk satu rumah independen terhadap rumah lainnya, me-
nurut tingkat ketidakberuntungan yang menimpa pemilik tiap rumah.
Berdasarkan adanya risiko yang dimiliki, instrumen investasi dapat dibeda-
kan menjadi instrumen berisiko (risky) dan bebas risiko (risk-free). Instrumen be-
risiko mempunyai risiko atau volatilitas senilai tertentu. Contoh instrumen berisiko
ialah ekuitas, komoditas, obligasi, lahan yasan (real estate), dan valuta asing (Chen,
2022). Di sisi lain, instrumen bebas risiko menjamin sejumlahreturntertentu tanpa
probabilitas kerugian apapun. Contoh instrumen bebas risiko adalah obligasi dan
surat utang yang diterbitkan oleh negara (Chen, 2021).
Bagi suatu perusahaan, investasi ditujukan untuk mempertahankan kebera-
daannya di tengah pasar kompetitif. Melalui peran manajer finansial, suatu peru-

## 42
sahaan dapat mengambil keputusan-keputusan investasi dengan menimbang biaya,
keuntungan, dan risiko yang ada (Berk dan DeMarzo, 2016). Di sisi lain, bagi per-
orangan, salah satu tujuan investasi ialah memperoleh penghasilan pasif.
Salah satu sekuritas yang umum dilibatkan sebagai instrumen bagi para in-
vestor individu muda di Indonesia ialah saham. Selain karena adanya jaminan ke-
amanan melalui perlindungan Otoritas Jasa Keuangan (OJK), investasi saham juga
dipermudah melalui keberadaan berbagai aplikasi digital. Pemahaman akan saham
dapat disimak pada subbab berikut.
## 2.16.  Saham
Menurut Berk dan DeMarzo (2016), saham adalah porsi kepemilikan sese-
orang atas suatu perusahaan. Saham merupakan instrumen investasi yang bersifat
likuid karena mampu dijual dengan cepat dan mudah dengan harga jual yang cukup
dekat dengan harga beli pada suatu waktu tertentu. Pemilik saham suatu perusahaan
dikenal juga sebagaishareholder,stakeholder, atauequity holder. Pemilik saham
berhak atas deviden, yaitu pembayaran sejumlah keuntungan perusahaan kepada
pemilik saham pada frekuensi tertentu atas dasar kebijakan tertentu. Besar devi-
den yang dibayarkan umumnya proporsional dengan banyak saham yang dimiliki
seorang pemilik saham.
Nilai suatu saham dan deviden yang terasosiasi dengan saham tersebut sela-
lu berfluktuasi seiring waktu. Fenomena ini terjadi karena saham merupakan instru-
men investasi yang berisiko (risky). Wujud risiko umum saham ialah berita-berita
meluas dari pasar ekonomi (market-wide news), sedangkan risiko independennya
berupa  berita-berita  spesifik  dari  perusahaan  emiten  saham  (firm-specific  news).
Dalam konteks investasi saham, risiko umum disebut juga risiko tak terdiversifikasi
atau risiko sistematis, sedangkan risiko independen disebut juga risiko terdiversifi-
kasi atau risikofirm-specific. Karena memengaruhi seluruh saham, risiko sistematis
tidak dapat didiversifikasi. Sementara, risikofirm-specificdapat didiversifikasi me-
lalui portofolio saham.

## 43
2.16.1.Returndan Risiko Saham
Sebagai suatu instrumen investasi yang berisiko, investasi saham dapat meng-
embalikan bermacam nilaireturndengan besar kemungkinan (likelihood) masing-
masing. Maka, tiap nilaireturnyang memungkinkan,R, terasosiasi dengan suatu
nilai probabilitas,p
## R
, membentuk suatu distribusi probabilitas. Ekspektasireturn
dapat dihitung melalui rumus:
## E[R] =
## X
## R
p
## R
## R
sebagai rata-rata terbobot dari tiap nilaireturnyang memungkinkan. Sementara,
risiko dapat diukur sebagai variansireturn, yaitu:
Var(R) =E
## 
## (R−E[R])
## 2
## 
## =
## X
## R
p
## R
## (R−E[R])
## 2
## ,
atau deviasi standarreturn, yaitu:
## SD(R) =
p
Var(R).
Deviasi standarreturndikenal juga sebagai volatilitas.
Returnyang  dapat dihitung  berdasarkan riwayat  harga  saham dalam  per-
iode waktu tertentu disebutreturnterealisasi (realized return).Returnterealisasi
mempunyai suatu distribusi empiris dan merupakan komponen dasar untuk meng-
estimasi volatilitas. Jika investasi pada suatu saham dilakukan pada waktutdengan
hargaP
t
, kemudian pada waktut+ 1, dividen sebesarDiv
t+1
dibayarkan dan sa-
ham dijual dengan hargaP
t+1
,returnterealisasi dari investasi saham dari waktut
ket+ 1dirumuskan sebagai:
## R
t+1
## =
## Div
t+1
## P
t
## +
## P
t+1
## −P
t
## P
t
## .(2.26)
Pada umumnya, waktu diukur dalam satuan tahun. Dengan mengasumsikan satuan
ini, rata-ratareturntahunan untuk tahun investasi pertama hingga tahun ke-Tdapat
dihitung sebagai:
## ̄
## R=
## 1
## T
## T
## X
t=1
## R
t
## .(2.27)

## 44
Estimasi variansireturndiberikan oleh rumus:
Var(R) =
## 1
## T−1
## T
## X
t=1
## (R
t
## −
## ̄
## R)
## 2
## .(2.28)
Di sisi lain, kovariansi antara dua buah kumpulanreturndapat dirumuskan sebagai:
Cov(R
## 1
## ,R
## 2
## ) =
## 1
## T−1
## T
## X
t=1
## (R
## 1t
## −
## ̄
## R
## 1
## )(R
## 2t
## −
## ̄
## R
## 2
## ).(2.29)
2.16.2.Short Sale
Short saleataushortsellingmerupakan perilaku menjual sekuritas yang se-
orang investor tidak miliki.  Dalam suatushort sale, seorang investor meminjam
sekuritas yang hendak ia jual kepada investor lain yang sudah mempunyai seku-
ritas tersebut. Pada kemudian hari, sekuritas tersebut akan dikembalikan melalui
pembelian senilai harga asli sekuritas tersebut atau disertai dengan arus kas yang
menyertainya (Berk dan DeMarzo, 2016).
## 2.17.  Pasar Saham
Menurut Berk dan DeMarzo (2016), pasar saham (stock market) atau bursa
efek (stock exchange) merupakan tempat terjadinya jual-beli saham dari perusahaan-
perusahaan terbuka. Pasar saham menyediakan likuiditas bagi saham perusahaan-
perusahaan yang terlibat di dalamnya. Terdapat dua jenis pasar saham, yaitu pasar
primer dan pasar sekunder. Pasar primer terjadi ketika suatu perusahaan menjual
lembar-lembar saham terbarunya kepada investor, sedangkan pasar sekunder terja-
di ketika saham diperjualbelikan antarinvestor.
Pasar saham mengunggah dua buah harga selama jam tertentu pada hari-hari
kerja, yaitu harga penawaran (bid price) dan harga permintaan (ask price). Harga
penawaran adalah harga saham tertinggi yang bersedia dibayar oleh pembeli. Di
sisi lain, harga permintaan adalah harga saham terendah yang dapat diterima oleh
penjual. Kedua harga ini diperhitungkan oleh para pembuat pasar (market makers).
Harga permintaan selalu bernilai lebih tinggi daripada harga penawaran. Selisih an-
tara kedua harga ini disebutbid-ask spreaddan merupakan keuntungan bagi pem-
buat pasar yang dibayar oleh investor sebagai biaya transaksi.

## 45
## 2.18.  Portofolio Saham
Portofolio adalah gabungan dari dua sekuritas keuangan atau lebih (Berk
dan DeMarzo, 2016). Portofolio merupakan sarana untuk memeratakan risikofirm-
specificdari tiap sekuritas yang tergabung di dalamnya. Pemerataan risiko ini dike-
nal sebagai diversifikasi. Risikofirm-specifichadir dalam rupa informasi maupun
peristiwa yang dapat bersifat baik atau buruk. Melalui diversifikasi, dampak risiko-
risiko ini akan lebih merata dan relatif konstan.
2.18.1.Returndan Risiko Portofolio Saham
Suatu  portofolio  didefinisikan  menurut  bobot-bobot  (weights)  portofolio,
w
i
, yang didefinisikan proporsi suatu investasi sekuritas tunggal terhadap nilai total
yang diinvestasikan dalam portofolio tersebut, yaitu:
w
i
## =
Nilai investasii
Nilai total portofolio
dengan:
## X
## ∀i
w
i
## = 1.(2.30)
Jika suatu portofolio memuatninvestasi dengan nilai-nilai bobot termuat dalam
vektorw
## ′
## =  [w
## 1
## ,w
## 2
## ,...,w
n
]danreturndalam  vektorR
## ′
## =  [R
## 1
## ,R
## 2
## ,...,R
n
## ],
maka Persamaan (2.30) dapat dinyatakan juga sebagai operasi vektor:
w
## ′
## 1
n
## = 1.(2.31)
Selain itu,returnportofolio dapat dihitung sebagai:
## R
## P
## =w
## 1
## R
## 1
## +w
## 2
## R
## 2
## +...+w
n
## R
n
## =
n
## X
i=1
w
i
## R
i
## =w
## ′
## R.
Jika dimisalkanE[R
i
## ] =μ
i
dan dibentuk vektorμ
## ′
## = [μ
## 1
## ,μ
## 2
## ,...,μ
n
], ekspektasi
returnportofolio dirumuskan sebagai:
μ
## P
## =E[R
## P
## ] =E
## "
n
## X
i=1
w
i
## R
i
## #

## 46
## =
n
## X
i=1
## E[w
i
## R
i
## ]
## =
n
## X
i=1
w
i
## E[R
i
## ]
## =
n
## X
i=1
w
i
μ
i
## =w
## ′
μ.(2.32)
Derajat pergerakan risiko umum danreturnsaham diukur melalui kovariansi
return. Antarareturndari dua buah investasi,R
i
danR
j
, kovariansi dirumuskan:
σ
ij
## =E
## 
## (R
i
## −E[R
i
## ])(R
j
## −E[R
j
## ])
## 
## .
Jika diestimasi secara empiris dari data riwayat harga saham, estimasi kovariansi
diberikan sebagai berikut:
## ˆσ
ij
## =
## 1
## T−1
## T
## X
t=1
## (R
i,t
## −
## ̄
## R
i
## )(R
j,t
## −
## ̄
## R
j
## )
dengan
## ̄
## R
i
dan
## ̄
## R
j
berturut-turut merupakan rata-ratareturndari investasi ke-idan
jberdasarkan Persamaan (2.27).
Jika  dimisalkanCov(R
i
## ,R
j
## )  =σ
ij
dan  dibentuk  matriks  kovariansi,Σ,
sebagaimana didefinisikan oleh Persamaan (2.18), maka variansi portofolio dapat
dipandang sebagai kovariansireturnportofolio dengan dirinya sendiri, yaitu:
σ
## 2
## P
= Cov(R
## P
## ,R
## P
## )
## = Cov

n
## X
i=1
w
i
## R
i
## ,R
## P
## !
## =
n
## X
i=1
w
i
Cov(R
i
## ,R
## P
## )(2.33)
## =
n
## X
i=1
w
i
## Cov

## R
i
## ,
n
## X
j=1
w
j
## R
j
## !
## =
n
## X
i=1
n
## X
j=1
w
i
w
j
Cov(R
i
## ,R
j
## )
## =
n
## X
i=1
n
## X
j=1
w
i
w
j
σ
ij

## 47
## =w
## ′
## Σw.(2.34)
Dengan demikian, volatilitas portofolio diperoleh sebagai berikut:
σ
## P
## =
q
σ
## 2
## P
## =
v
u
u
t
n
## X
i=1
n
## X
j=1
w
i
w
j
Cov(R
i
## ,R
j
## ).(2.35)
Ekspektasireturnpada Persamaan (2.32) dan volatilitas portofolio pada Per-
samaan (2.35) dibangun darireturnharian. Keduanya dapat distandarisasi kembali
untuk jangka waktu tahunan melalui proses penyetahunan (annualization). Menu-
rut Bodie, Kane, dan Marcus (2014), penyetahunan ekspektasireturndan volatilitas
diestimasi melalui asumsi bahwa mean dan variansi bertumbuh secara proporsio-
nal terhadap waktu. Dalam hal ini, waktu merujuk pada kelipatan durasi dari data
sampel dalam satu tahun. Oleh karena itu, jika diberikan ekspektasireturnporto-
folio,μ
## D
, dan volatilitas portofolio,σ
## D
, yang masing-masing diperoleh darireturn
harian serta asumsi bahwa terdapat 252 hari kerja dalam satu tahun, estimasi untuk
ekspektasireturndan volatilitas yang telah disetahunkan ialah:
μ
## A
## = 252μ
## D
dan:
σ
## 2
## A
## = 252σ
## 2
## D
## ⇐⇒σ
## A
## =
## √
## 252σ
## D
## ,
secara berturut-turut.
Adapun nilai kovariansi cukup sulit untuk diinterpretasikan sehingga ukuran
risiko portofolio alternatif, yaitu korelasi, dapat digunakan. Korelasi antarareturn
dua buah saham,R
i
danR
j
, didefinisikan sebagai:
ρ
ij
## =
σ
ij
σ
i
σ
j
## .(2.36)
Melalui ukuran korelasi, dapat dibuktikan bahwa portofolio mendiversifikasi risiko
dalam berinvestasi. Pertama, Persamaan (2.36) disubstitusikan ke Persamaan (2.33)

## 48
sehingga diperoleh:
σ
## 2
## P
## =
n
## X
i=1
w
i
Cov(R
i
## ,R
## P
## )
## =
n
## X
i=1
w
i
σ
iP
## =
n
## X
i=1
w
i
σ
i
σ
## P
ρ
iP
## .
Dengan membagi kedua ruas denganσ
## P
, diperoleh:
σ
## 2
## P
σ
## P
## =
## P
n
i=1
w
i
σ
i
σ
## P
ρ
iP
σ
## P
## ⇐⇒σ
## P
## =
n
## X
i=1
w
i
σ
i
ρ
ij
## ≤
n
## X
i=1
w
i
σ
i
## ,
dengan
## P
n
i=1
w
i
σ
i
adalah jumlah volatilitas tiap saham secara independen.
## 2.18.2.  Beta Portofolio
Beta dari suatu investasi pada sekuritasidalam portofolioPdirumuskan:
β
## P
i
## =
σ
i
ρ
iP
σ
## P
## (2.37)
denganσ
i
melambangkan volatilitas sekuritas,σ
## P
melambangkan volatilitas porto-
folio, danρ
iP
melambangkan korelasi antarareturnsekuritas danreturnportofolio.
Dengan mensubstitusikan Persamaan (2.36), Persamaan (2.37) dapat dirumuskan
juga sebagai:
β
## P
i
## =
σ
i
σ
iP
σ
i
σ
## P
σ
## P
## =
σ
iP
σ
## 2
## P
## (2.38)
denganσ
iP
adalah kovariansi antarareturnsekuritas danreturnportofolio sertaσ
## 2
## P
adalah variansi portofolio. Beta adalah ukuran risiko sistematis berupa sensitivitas
returnsekuritas terhadapreturnportofolio.

## 49
Beta dapat digunakan untuk menghitungreturnyang dibutuhkan (required
return), yaitu ekspektasireturnyang diperlukan sebagai kompensasi atas risiko su-
atu investasi dalam suatu portofolio.Required return,r
i
, dirumuskan:
r
i
## =r
f
## +β
## P
i
## (E[R
## P
## ]−r
f
## )
denganr
f
adalah suku bunga bebas risiko (disebut juga tingkatreturnbebas risiko)
danE[R
## P
]adalah ekspektasireturnportofolio. Di Indonesia, sebagaimana diatur
oleh Bank Indonesia, BI-Rate (dahulu bernama BI7DRR) adalah suku bunga ke-
bijakan yang diterapkan sebagai acuan utama di pasar keuangan (Bank Indonesia,
t.t.). Dengan demikian,r
f
yang berlaku di Indonesia sama dengan BI-Rate yang
berlaku pada suatu periode.
## 2.18.3.  Ukuran Performa Portofolio
Portofolio denganreturnyang lebih tinggi dan risiko yang lebih rendah me-
rupakan sesuatu yang memungkinkan. Untuk mencapainya,returnterhadap risiko
portofolio dengan berbagai variasi bobot dapat dipetakan sebagai suatu kurva hiper-
bola. Secara visual, seorang investor dapat menemukan portofolio yang diharapkan
berdasarkanreturndan risiko yang diinginkan melalui kurva ini. Hal ini akan diba-
has lebih lanjut pada subbab-subbab selanjutnya.
Cara lain untuk menilai kualitas suatu portofolio ialah menggunakan ber-
bagai  ukuran  performa.  Cogneau  dan  H
## ̈
ubner  (2009)  mengelompokkan  ukuran-
ukuran performa portofolio berdasarkan empat acuan, yaitu kemampuan investor
(pemilihan aset atau waktu pasar), individualisasi (standarisasi atau preferensi sub-
jektif investor), penciptaan nilai (gainataureturn), dan translasi (rasio atau selisih).
Pada penelitian ini, Penulis akan berfokus padaSharpe ratio(SR),Treynor
ratio(TR), danJensen’s alpha, yaitu tiga ukuran performa portofolio berbasisre-
turnyang diutamakan dalam berbagai literatur terdahulu (Marhfor, 2016). Ketiga
ukuran tersebut berlaku di bawah asumsi bahwa risiko bernilai konstan selama ku-
run waktu yang dilibatkan dalam penilaian performa portofolio.

## 50
2.18.4.Sharpe Ratio
Sharpe ratiomerupakan salah satu ukuran performa portofolio pertama di
dunia yang ditemukan oleh William F. Sharpe pada tahun 1966.Sharpe ratiodiru-
muskan sebagai:
## S
## P
## =
## E[R
## P
## ]−r
f
## SD(R
## P
## )
## (2.39)
denganE[R
## P
]adalah ekspektasireturnportofolio yang telah disetahunkan,r
f
ada-
lah tingkatreturnbebas risiko, danSD(R
## P
)adalah volatilitas portofolio yang telah
disetahunkan. Pembilang pada rumusanSharpe ratiodisebutexcess returnsehingga
Sharpe ratiodapat dipandang sebagai rasioreturnterhadap volatilitas yang diberik-
an oleh suatu portofolio. Nilai rasio yang semakin tinggi menandakanreturndari
suatu portofolio bernilai lebih tinggi dengan besar risiko tertentu. Portofolio yang
optimal mempunyaiSharpe ratioyang tinggi, yaitu mempunyaiexcess returnyang
tinggi dan volatilitas yang rendah (Berk dan DeMarzo, 2016).
Sharpe ratiojuga dapat digunakan untuk menilai kualitas saham. Rumus
Sharpe ratiountuk menilai kualitas saham diperoleh dengan mengganti ekspektasi
returndan volatilitas portofolio menjadi ekspektasireturndan volatilitas saham,
yaitu:
## S
i
## =
## E[R
i
## ]−r
f
## SD(R
i
## )
## (2.40)
denganS
i
adalahSharpe ratiosuatu sahamidanR
i
adalahreturnsahami.
## 2.18.5.  Portofolio Tangen
Pemahaman akan portofolio tangen berawal dari studi kasus investasi pa-
da portofolio aset-aset berisiko dan aset bebas risiko, seperti Surat Utang Nega-
ra (SUN). Portofolio atas aset-aset berisiko mempunyai ekspektasireturnsenilai
## E[R
## P
]dan volatilitas sebesarσ
## 2
## P
, sedangkan SUN mempunyai tingkatreturnsebe-
sarr
f
dan tidak mempunyai risiko. Jika seorang investor menabung kepemilikannya
sebesarxpada portofolio dan(1−x)pada SUN, ekspektasireturndari portofolio
baru dapat dihitung sebagai:
## E[R
## P
## ′
] =E[xR
## P
## + (1−x)r
f
## ]

## 51
=xE[R
## P
## ] + (1−x)r
f
=xE[R
## P
## ] +r
f
## −xr
f
## =r
f
+x(E[R
## P
## ]−r
f
## ).
Di sisi lain, volatilitas portofolio baru dapat dihitung sebagai:
σ
## P
## ′
## =
q
## Var
##  
xR
## P
## + (1−x)r
f
## 
## =
q
x
## 2
Var(R
## P
## ) + (1−x)
## 2
## Var(r
f
) + 2x(1−x)Cov(R
## P
## ,r
f
## )
## =
p
x
## 2
Var(R
## P
## ) + (1−x)
## 2
## (0) + 2x(1−x)(0)
## =
p
x
## 2
Var(R
## P
## )
## =xσ
## P
## .
Dengan demikian, jika suatu portofolio terdiri atas aset-aset berisiko dan aset bebas
risiko, ekspektasireturndan volatilitasnya berbanding lurus terhadap jumlah bobot
investasi pada aset-aset berisiko saja.
Jika ekspektasireturndan volatilitas dari portofolio baru ini dipetakan, ku-
rva yang terbentuk ialah sebuah garis dengan kemiringan senilaiSharpe ratioporto-
folio tersebut. Kurva hiperbola dari portofolio-portofolio lain yang hanya memuat
aset-aset berisiko terletak di bawah garis ini dan hanya menyinggung garis terse-
but pada satu titik. Oleh karena itu, portofolio yang menghasilkan garis ini disebut
portofolio tangen. Kurva garis dari portofolio tangen merupakan garis dengan ke-
miringan paling curam atau nilaiSharpe ratiotertinggi (Berk dan DeMarzo, 2016).
## 2.18.6.  Portofolio Efisien
Secara umum, portofolio efisien dapat dimaknai sebagai portofolio yang ti-
dak dapat didiversifikasi lebih jauh. Pada portofolio efisien, risiko tidak dapat di-
kurangi jika ekspektasireturntidak dikurangi. Jika divisualisasikan sebagai kurva
yang memetakan ekspektasireturnterhadap volatilitas, portofolio efisien merupak-
an portofolio yang bersinggungan dengan portofolio tangen.
Secara matematis, suatu portofolio bersifat efisien jika dan hanya jika untuk

## 52
tiap sekuritas di dalamnya, ekspektasireturnsama denganrequired return, yaitu:
## E[R
i
## ] =r
i
## =r
f
## +β
eff
i
## (E[R
eff
## ]−r
f
## )(2.41)
denganr
f
adalah suku bunga bebas risiko,β
eff
i
adalah beta sekuritasipada porto-
folio efisien, danE[R
eff
]adalah ekspektasireturnportofolio efisien.
Potensi diversifikasi yang dimiliki suatu portofolio semakin berkembang se-
iring bertambah banyaknya saham yang termuat dalam portofolio tersebut. Oleh
karena itu, salah satu kandidat portofolio efisien adalah portofolio pasar, yaitu por-
tofolio dari semua saham dan sekuritas yang diperdagangkan di pasar saham (Berk
dan DeMarzo, 2016).
2.18.7.Capital Asset Pricing Model
Capital Asset Pricing Model(CAPM) merupakan model yang memampuk-
an identifikasi portofolio atas sekuritas-sekuritas berisiko jika ekspektasireturndan
volatilitas dari tiap sekuritas serta korelasi antarsekuritas yang termuat di dalam
portofolio tersebut tidak diketahui. Menurut Berk dan DeMarzo (2016), terdapat
tiga asumsi yang mendasari CAPM, yaitu:
-  Semua investor dapat membeli dan menjual semua sekuritas pada harga pasar
kompetitif (tanpa pajak dan biaya transaksi) serta meminjam dan memberi pin-
jaman pada tingkat suku bunga bebas risiko.
-  Semua investor hanya bergantung pada portofolio efisien atas sekuritas-seku-
ritas yang ia perjualbelikan.
-  Semua investor mempunyai ekspektasi yang homogen akan volatilitas, korela-
si, dan ekspektasireturnsekuritas, yakni estimasi yang seragam akan investasi
mendatang danreturn.
Asumsi-asumsi CAPM memuat pola perilaku investor yang menjadikan pa-
sar dalam keadaan setimbang dan portofolio pasar berlaku sebagai portofolio efi-
sien. Akibatnya, Persamaan (2.41) dapat didefinisikan kembali sebagai Persamaan
CAPM berikut:
## E[R
i
## ] =r
i
## =r
f
## +β
## M
i
## (E[R
## M
## ]−r
f
## )(2.42)

## 53
denganβ
## M
i
adalah beta sekuritasipada portofolio pasar danE[R
## M
]adalah ekspek-
tasireturnportofolio pasar. Dengan memandang Persamaan (2.42) di atas sebagai
suatu persamaan linear, beta dapat diinterpretasikan sebagai persentase ekspektasi
perubahanreturnsekuritas tersebut untuk tiap perubahanreturnportofolio pasar
sebesar satu persen (Berk dan DeMarzo, 2016).
Jika portofolio pasar diacu sebagai portofolio efisien, maka perubahan nilai
portofolio pasar mencerminkan guncangan perekonomian negara tempat diperjual-
belikannya sekuritas-sekuritas dalam portofolio tersebut. Oleh karena itu, notasiβ
## M
i
sering disederhanakan menjadiβ
i
. Lebih lanjut, sebuah portofolio dapat dipandang
sebagai aset tersendiri karena ia mempunyaireturndan risiko selayaknya sekuritas-
sekuritas yang termuat di dalamnya. Dengan demikian, dapat didefinisikan ukuran
beta portofolio yang relatif terhadap portofolio pasar,β
## P
## .
2.18.8.Jensen’s Alpha
Pada kasus di mana asumsi-asumsi CAPM tidak berlaku, terdapat selisih
antara ekspektasireturndanrequired returndari suatu saham yang dikenal seba-
gai alfa saham (stock’s alpha). Alfa suatu saham,i, dilambangkan denganα
i
dan
dirumuskan sebagai:
α
i
## =E[R
i
## ]−r
i
## =E[R
i
## ]−
##  
r
f
## +β
i
## (E[R
## M
## ]−r
f
## )
## 
denganE[R
i
]adalah ekspektasireturndari sahami,r
f
adalah tingkatreturnbebas
risiko,β
i
adalah beta saham, danE[R
## M
]adalah ekspektasireturndari indeks pasar
acuan.
Berdasarkan Marhfor (2016), alfa saham dapat digeneralisasi untuk suatu
portofolio menjadi suatu ukuran yang disebutJensen’s alpha. Ukuran ini dilam-
bangkan denganα
## P
dan dirumuskan sebagai:
α
## P
## =E[R
## P
## ]−
##  
r
f
## +β
## P
## (E[R
## M
## ]−r
f
## )
## 
## (2.43)
denganE[R
## P
]adalah ekspektasireturnportofolio danβ
## P
adalah beta portofolio.

## 54
Alfa saham danJensen’s alphayang bernilai positif merupakan salah satu
dasar untuk melahirkan lebih banyak persaingan pada pasar sehingga pasar mende-
kati keadaan efisien. Oleh karena itu, portofolio yang optimal turut dicirikan dengan
Jensen’s alphayang positif (Berk dan DeMarzo, 2016).
2.18.9.Treynor Ratio
Treynor ratioditemukan oleh Jack Treynor, seorang ekonom asal Ameri-
ka Serikat.Treynor ratiomelibatkan risiko sistematis portofolio pada rumusannya,
menjadikannya berbeda dariSharpe ratioyang menggunakan risiko keseluruhan.
Treynor ratiodirumuskan sebagai:
## T
## P
## =
## E[R
## P
## ]−r
f
β
## P
## (2.44)
denganT
## P
adalahTreynor ratioportofolio,E[R
## P
]adalah ekspektasireturnporto-
folio yang telah disetahunkan,r
f
adalah tingkatreturnbebas risiko, danβ
## P
adalah
beta portofolio (Marhfor, 2016).
Treynor ratioyang semakin tinggi bermakna bahwareturnsuatu portofolio
bernilai lebih tinggi untuk risiko sistematis dengan besar tertentu.
2.19.  Indeks Saham LQ45
Menurut  Berk  dan  DeMarzo  (2016),  indeks  saham  merupakan  portofolio
umum atas sekumpulan saham tertentu. Mayoritas indeks saham dibobotkan atas
dasar nilai (value-weighted), yaitu bahwa bobot tiap saham bergantung pada harga
pasar tiap perusahaan yang mengeluarkan saham yang terlibat dalam indeks saham
tersebut. Akan tetapi, terdapat pula indeks-indeks saham yang dibobotkan atas da-
sar harga (price-weighted), yaitu bahwa bobot tiap saham bergantung pada nilai
tiap saham yang sedang berlaku.
Selayaknya saham, seorang investor juga dapat melakukan jual-beli atas in-
deks saham. Investasi indeks saham sejatinya merupakan suatu bentuk strategi ar-
bitrase, yaitu membeli dan menjual suatu instrumen investasi di pasar-pasar yang
berbeda untuk meraih keuntungan dari selisih harga yang ada. Arbitrase melalui
indeks saham dapat dilakukan dengan membeli indeks dan menjual saham-saham

## 55
tersebut  secara  terpisah-pisah,  jika  diketahui  harga  indeks  lebih  rendah  daripada
total harga saham-saham yang tergabung di dalamnya.
Dikarenakan datareturnberbagai sekuritas dan saham kecil sering kali ti-
dak tersedia, portofolio pasar yang sempurna tidak mudah untuk diperoleh. Dalam
hal ini, indeks saham dapat digunakan sebagai aproksimasi untuk portofolio pasar
(Berk dan DeMarzo, 2016). Beberapa contoh indeks saham yang berlaku di Indo-
nesia ialah antara lain Indeks Harga Saham Gabungan (IHSG), IDX30, LQ45, dan
## KOMPAS100.
Indeks LQ45 (Liquid 45) merupakan indeks saham yang terdiri atas 45 sa-
ham dengan likuiditas yang tinggi. Indeks LQ45 diluncurkan oleh Bursa Efek Indo-
nesia (BEI) pada bulan Februari 1977 dan telah menjadi salah satu indikator penting
bagi investor-investor saham di Indonesia.
Secara spesifik, tiga puluh saham pertama yang digolongkan dalam indeks
LQ45 harus memenuhi kriteria-kriteria berikut:
-  Saham resmi tercatat di BEI selama tiga bulan terakhir.
-  Perusahaan emiten saham mempunyai kondisi finansial dan prospek pertumbuh-
an yang baik.
-  Perusahaan mempunyai kapitalisasi pasar yang tinggi selama satu hingga dua
bulan terakhir.
-  Dalam dua belas bulan terakhir, saham tergabung dalam enam puluh saham de-
ngan nilai transaksi tertinggi dalam pasar reguler.
Setelahnya, lima belas saham tambahan akan ditentukan berdasarkan kriteria-krite-
ria  tambahan,  yaitu  hari  transaksi  dan  frekuensi  transaksi  di  pasar  reguler  serta
kapitalisasi pasar. Melalui kriteria-kriteria ini, saham-saham dalam indeks LQ45
berpotensi memberikanreturnyang stabil dalam jangka panjang. Oleh karena itu,
indeks LQ45 merupakan indikator yang baik untuk mendukung investasi yang cer-
mat, khususnya bagi investor-investor pemula (Nurawan dan Mahendra, 2023).
Saham-saham yang termuat dalam indeks LQ45 pada periode Agustus 2024
hingga Januari 2025 dijabarkan pada Lampiran 1.

## 56
## 2.20.  Metode Pengali Lagrange
Suatu permasalahan optimisasi klasik dirumuskan sebagai:
max(ataumin)f
## 0
## (x)
dengan kendalaf
i
(x) = 0,  i= 1,2,...,m(2.45)
denganf
## 0
adalah fungsi objektif,x
## ′
## = [x
## 1
## ,x
## 2
## ,...,x
n
]adalah vektor atas variabel-
variabel keputusan, danf
i
adalah fungsi-fungsi kendala (constraint). Didefinisikan
pula himpunan kesempatan:
K={x|x∈R
n
## ,f
i
## (x)≤0,i= 1,2,...,m},(2.46)
yaitu himpunan atas solusi-solusi fisibel (feasible solutions). Secara umum, him-
punanKdiasumsikan tidak kosong sehingga terdapat suatu vektor,x, yang layak
jika dan hanya jikax∈K(Lupt
## ́
a
## ˇ
cik, 2010).
Menurut Schott (2017), metode pengali Lagrange ialah metode penyelesai-
an permasalahan optimisasi dengan persamaan-persamaan kendala tertentu meng-
gunakan fungsi Lagrange. Fungsi Lagrange memuat vektor atas variabel-variabel
keputusan,x
n
, dan vektor pengali Lagrange,u
## ′
## = [u
## 1
## ,u
## 2
## ,...,u
m
]. Dengan men-
definisikan vektorf
## ′
## = [f
## 1
## ,f
## 2
## ,...,f
m
], fungsi Lagrange untuk permasalahan opti-
misasi pada Persamaan (2.45) dirumuskan:
## L(x,u) =f
## 0
## (x) +u
## ′
f(x)
## =f
## 0
## (x) +
m
## X
i=1
u
i
f
i
## (x)(2.47)
dengan Nilai-nilai stasionerL(x,u)adalah solusi berpasangan,(x,u), yang me-
menuhi:
## ∂
## ∂x
## ′
## L(x,u) =
## ∂
## ∂x
## ′
f
## 0
## (x) +u
## ′
## 
## ∂
## ∂x
## ′
f(x)
## 
## =0
## ′
dan(2.48)
## ∂
## ∂u
## ′
## L(x,u) =f(x) =0
## ′
## .(2.49)
Perumuman dari permasalahan optimisasi klasik ialah model pemrograman
matematis. Perumuman ditunjukkan pada bentuk kendala yang tidak terkhusus pada

## 57
persamaan, tetapi juga pertidaksamaan, yakni sebagai berikut:
max(ataumin)f
## 0
## (x)
dengan kendalaf
i
(x)≤0,  i= 1,2,...,m(2.50)
denganf
## 0
adalah fungsi objektif,x
## ′
## = [x
## 1
## ,x
## 2
## ,...,x
n
]adalah vektor atas variabel-
variabel  keputusan,  danf
i
adalah  fungsi-fungsi  kendala.  Metode  pengali  Lagra-
nge dapat diterapkan untuk menyelesaikan program matematis dengan didahului
transformasi terhadap bentuk kendala menjadi persamaan. Transformasi dilakukan
dengan menambahkanmvariabelslacksedemikian sehingga program matematis
dapat dituliskan kembali sebagai:
max(ataumin)f
## 0
## (x)
dengan kendalaf
i
## (x) +y
## 2
i
= 0,  i= 1,2,...,m,(2.51)
menjadikannya suatu permasalahan optimisasi klasik. Dengan cara yang sama, fung-
si Lagrange yang berkorespondensi dengan permasalahan optimisasi pada Persama-
an (2.51) ialah:
## L(x,y,u) =f
## 0
## (x) +u
## ′
f(x)
## =f
## 0
## (x) +
m
## X
i=1
u
i
##  
f
i
## (x) +y
## 2
i
## 
## .(2.52)
Permasalahan  pemrograman  matematis  dapat  diperumum  dengan  adanya
kendala-kendala pertidaksamaan. Dalam menyelesaikan pemrograman matematis
umum, metode pengali Lagrange juga diperumum menuju syarat-syarat Kuhn-Tuck-
er.
2.21.  Syarat-Syarat Kuhn-Tucker untuk Permasalahan Minimisasi
Secara matematis, permasalahan pemrograman matematis umum dinotasik-
an:
max(ataumin)f
## 0
## (x,y)
dengan kendalaf
i
(x,y)≤0,  i= 1,2,...,m,

## 58
g
h
(x,y) = 0,  h=m+ 1,...,r,
x≥0,dan
y∈R
l
## .(2.53)
Fungsi Lagrange yang berkorespondensi dengan program matematis umum pada
Persamaan (2.53) didefinisikan sebagai:
## L(x,y,u,v) =f
## 0
## (x,y) +
m
## X
i=1
u
i
f
i
## (x,y) +
r
## X
h=m+1
v
h
g
h
## (x,y)
denganu
## ′
## = [u
## 1
## ,...,u
m
## ]danv
## ′
## = [v
m+1
## ,...,v
r
]berturut-turut merupakan vek-
tor atas pengali-pengali Lagrange yang berkorespondensi dengan kendala-kendala
berbentuk pertidaksamaan dan persamaan.
Diasumsikan bahwa fungsif
## 0
## ,f
## 1
## ,...,f
m
## ,g
m+1
## ,...g
r
seluruhnya diferensi-
abel. Jika fungsi objektiff
## 0
mencapai minimum lokal pada(x
## 0
## ,y
## 0
)terhadap him-
punan fisibel:
## K={(x,y)|f
i
## (x,y)≤0,i= 1,2,...,mdang
h
## (x,y) = 0,h=m+ 1,...,r},
maka  terdapat  vektor  pengali  Lagrangeu
## 0
danv
## 0
sedemikian  sehingga  syarat-
syarat berikut terpenuhi:
## ∂L
## 0
## ∂x
## ≥0,(2.54)
x
## 0
## ∂L
## 0
## ∂x
## = 0,(2.55)
## ∂L
## 0
## ∂u
## ≤0,(2.56)
u
## 0
## ∂L
## 0
## ∂u
## = 0,(2.57)
## ∂L
## 0
## ∂y
## =0,(2.58)
## ∂L
## 0
## ∂v
## =0,(2.59)
x
## 0
## ≥0,dan(2.60)
u
## 0
## ≥0,(2.61)

## 59
denganL
## 0
=L(x
## 0
## ,y
## 0
## ,u
## 0
## ,v
## 0
). Kedelapan syarat pada Persamaan (2.54) hingga
Persamaan (2.61) di atas disebut syarat-syarat Kuhn-Tucker (Lupt
## ́
a
## ˇ
cik, 2010). De-
ngan kata lain, penurunan syarat-syarat Kuhn-Tucker untuk permasalahan minimi-
sasi dapat dirangkum dalam tiga tahap berikut:
-  Notasikan semua kendala pertidaksamaan dalam bentuk:
f
i
## (x,y)≤0.
-  Susun  fungsi  Lagrange  yang  terdiri  dari  jumlah  fungsi  objektif  dan  kendala-
kendala terbobot.
-  Hitung derivatif-derivatif parsial dari fungsi Lagrange, dengan derivatif parsial:
a.  terhadap variabel-variabel nonnegatif,x, bersifat nonnegatif dan kondisi ke-
lampaian komplementer (complementary slackness) pada Persamaan (2.55)
terpenuhi;
b.  terhadap variabel-variabel bebas,y, sama dengan nol;
c.  terhadap pengali-pengali Lagrange yang berkorespondensi dengan kendala
pertidaksamaan,u, bersifat nonpositif dan kondisi kelampaian komplemen-
ter pada Persamaan (2.57) terpenuhi; dan
d.  terhadap pengali-pengali Lagrange yang berkorespondensi dengan kendala
persamaan,v, sama dengan nol.
## Lupt
## ́
a
## ˇ
cik  (2010)  menyebutkan  bahwa  tidak  terdapat  cara  yang  sederhana
dalam menyelesaikan syarat-syarat Kuhn-Tucker, bahkan secara komputasional se-
kalipun. Salah satu pendekatan yang dapat dimanfaatkan untuk menyelesaikan per-
masalahan ini ialah pemrograman kuadratik.
## 2.22.  Pemrograman Kuadratik
Menurut Nocedal dan Wright (2006), program kuadratik merupakan sebuah
permasalahan optimisasi yang mengandung fungsi objektif berbentuk kuadrat dan
kendala-kendala linear. Secara umum, suatu program kuadratik dinyatakan sebagai:
min
x
q(x) =
## 1
## 2
x
## ′
## Dx+x
## ′
d
dengan kendalap
## ′
i
x≥q
i
,  i= 1,2,...,l,

## 60
r
## ′
j
x=s
j
,  j= 1,2,...,m,(2.62)
denganx,d,p
i
, danr
j
merupakan vektor berukurann×1,Dmerupakan ma-
triks simetris berukurann×n, sertaq
i
dans
j
merupakan skalar. Beberapa sumber
pustaka lain, seperti Taha (2007), menotasikan kendala sebagai:
## Px=q(2.63)
dan
## Rx=s,(2.64)
denganP,q,R, dansberturut-turut memuatp
i
## ,q
i
, danr
j
, dans
j
yang ditum-
puk secara vertikal. Dengan demikian,Pberdimensil×n,qberdimensil×1,R
berdimensim×n, dansberdimensim×1.
## 2.23.  Algoritma Optimisasi Metaheuristik
Istilah  ”metaheuristik”  bersumber  dari  dua  kata,  yaitu  ”meta”  dan  ”heu-
ristik”. Dikutip dari Rajwar dkk. (2023), algoritma heuristik adalah suatu metode
untuk menghasilkan solusi-solusi terhadap permasalahan-permasalahan optimisasi
melalui percobaan dan kegagalan (trial and error). Di sisi lain, kata ”meta” berarti
”di atas” atau ”pada tingkat yang lebih tinggi”. Oleh karena itu, algoritma optimi-
sasi metaheuristik dapat didefinisikan sebagai metode tingkat lanjut dari pencarian
solusi optimal atas suatu permasalahan.
Algoritma-algoritma metaheuristik yang berbasis perilaku dan seleksi ala-
miah mulai dikembangkan oleh para ilmuwan sejak tahun 1950-an. Penemuan ini
ditujukan  untuk  menggantikan  metode-metode  konvensional  yang  tidak  lagi  efi-
sien, tangguh (robust), dan akurat dalam menangani permasalahan-permasalahan
optimisasi  yang  semakin  diskontinu  dan  nonlinear.  Alam  menjadi  dasar  inspira-
si algoritma-algoritma metaheuristik karena berbagai fenomena alam yang dinilai
optimal dalam menyelesaikan permasalahan yang bersumber dari alam itu sendiri.
Secara umum, sebuah algoritma metaheuristik bergantung pada pergerakan
individu dan interaksi antarindividu dalam populasi. Secara matematis, ”individu”

## 61
dan ”populasi” dapat dimaknai sebagai kandidat solusi dan himpunan penyelesai-
an suatu fungsi matematika. Pergerakan individu dapat melibatkan operasi-operasi
evolusioner atau metoderandom walkyang didasarkan pada distribusi probabilitas
tertentu, sedangkan interaksi antarindividu umumnya didasarkan pada teori evolusi
makhluk hidup, fenomena alamiah, atau perilaku hewan (Suyanto dkk., 2022).
Berdasarkan sumber inspirasi yang lebih spesifik terhadap penemuannya,
Rajwar dkk. (2023) menggolongkan algoritma-algoritma metaheuristik menjadi em-
pat kelompok, yaitu:
-  Algoritma-algoritma evolusioner
Algoritma-algoritma evolusioner dikembangkan dari teori evolusi Darwin. Alur
algoritma-algoritma dalam kelompok ini bermula dari simulasi reproduksi sek-
sual dan mutasi pada sekelompok individu secara berulang guna menemukan
dan mempertahankan materi genetik yang menjadikan suatu individu lebih tang-
guh dalam beradaptasi dan bertahan hidup.
-  Algoritma-algoritma kecerdasan kawanan (swarm intelligence algorithms)
Algoritma-algoritmaswarm intelligenceterinspirasi dari perilaku hewan yang
membentuk kawanan pada fenomena-fenomena tertentu, seperti melindungi diri
dari pemangsa, berburu, dan mencari makan. Kualitas-kualitas yang diperhatik-
an dari suatu kawanan hewan ialah kemampuan beradaptasi, komunikasi, dan
cara berbagi pengetahuan.
-  Algoritma-algoritma berbasis hukum fisik
Algoritma-algoritma berbasis hukum fisik dikembangkan dari hukum-hukum fi-
sika dan kimia.
-  Algoritma-algoritma lainnya
Algoritma-algoritma  dalam  kelompok  ini  dikembangkan  dari  berbagai  dasar,
mulai dari fenomena dalam kehidupan sehari-hari, perilaku manusia, hingga te-
orema matematik dan politik.

## BAB III
## ANALISIS KLASTERK-MEANSDAN
## ALGORITMA-ALGORITMA OPTIMISASI PORTOFOLIO
3.1.  Analisis KlasterK-Means
Analisis klasterK-Meansmerupakan salah satu metode analisis klaster par-
tisi  yang mengelompokkan  tiap objek  menuju  klaster dengan  pusat klaster  yang
berjarak  paling  dekat.  Pusat  klaster  disebut  juga  sentroida.  Pada  analisis  klaster
K-means, sentroida diperoleh sebagai mean dari objek-objek dalam klaster yang
bersesuaian (Johnson dan Winchern, 2007).
Johnson dan Winchern (2007) dan Han dkk. (2012) menjabarkan metode
analisis klasterK-meanssebagai berikut:
-  TentukanK, jumlah klaster ideal atau jumlah klaster yang dikehendaki.
-  TentukanKobjek sembarang daridatasetDsebagaiKsentroida mula-mula.
-  Kelompokkan objek dengan klaster yang mempunyai sentroida terdekat dengan
objek tersebut. Umumnya, digunakan jarak Euklides.
-  Hitung kembali sentroida klaster setelah menerima objek baru dan melepas-kan
objek lama.
-  Ulangi langkah 3 dan 4 hingga tidak terjadi perubahan klaster pada semua objek.
Langkah-langkah di atas juga diberikan pada diagram alur pada Gambar 3.1.
Salah satu cara memperoleh nilaiKoptimal ialah melalui koefisiensilhou-
etteatausilhouette score. Misalkan diberikan suatudataset,D, yang terdiri atasn
objek dan dipartisi menjadiKklaster,C
## 1
## ,C
## 2
## ,...,C
k
. Objek dalamdatasetmeru-
pakan data multivariat yang disusun sebagai suatu vektor. Dimisalkan jugad(p,q)
sebagai  ukuran  jarak  antara  dua  buah  vektor  objek,pdanq.  Untuk  tiap  objek,
o∈D, dan misalkano∈C
i
, dirumuskana(o)danb(o)sebagai:
a(o) =
## P
o
## ′
## ∈C
i
## ,o̸=o
## ′
d(o,o
## ′
## )
## |C
i
## |−1
## 62

## 63
Gambar 3.1 Diagram alur analisis klasterK-Means.
dan
b(o) =min
## C
j
## :1≤j≤k,j̸=i
## (
## P
o
## ′
## ∈C
j
d(o,o
## ′
## )
## |C
j
## |
## )
## .
a(o)adalah jarak rata-rata antaraodengan semua objek lain dalam klasternya, se-
dangkanb(o)adalah  jarak  rata-rata minimum  antaraodengan  klaster  lain yang
tidak memuato. Nilaia(o)mencerminkan kepadatan klaster yang memuato. Se-
makin kecil nilaia(o), klaster tersebut semakin padat. Sementara, nilaib(o)men-
cerminkan seberapa terpisahodari klaster-klaster lain. Semakin besar nilaib(o),
objekosemakin terpisah dari klaster-klaster lain.Silhouette scoredarioselanjut-
nya dirumuskan sebagai:
s(o) =
b(o)−a(o)
max{a(o),b(o)}
## .(3.1)
## Jikad(o,o
## ′
)merujuk pada jarak Euclid antara objekodano
## ′
sebagaimana
dirumuskan pada Persamaan (2.21),d(o,o
## ′
)bernilai nonnegatif sehinggaa(o)ma-
upunb(o)bernilai nonnegatif. Maka, nilai minimum daria(o)maupunb(o)adalah
nol. Lebih lanjut, rumusansilhouette scorepada Persamaan (3.1) di atas dapat dide-
finisikan kembali untuk kasus:a(o)lebih besar darib(o),a(o)sama denganb(o),
dana(o)kurang darib(o). Untuk kasusa(o)lebih besar darib(o),silhouette score

## 64
dapat didefinisikan kembali sebagai:
s(o) =
b(o)−a(o)
b(o)
## =
b(o)
b(o)
## −
a(o)
b(o)
## = 1−
a(o)
b(o)
## .
Karena syarat kasus dana(o)nonnegatif, maka:
## 0≤
a(o)
b(o)
## <1
sehingga
0< s(o)≤1.
Untuk kasusa(o)sama denganb(o),silhouette scoredapat didefinisikan kembali
sebagai:
s(o) =
b(o)−a(o)
b(o)
## =
b(o)−b(o)
b(o)
## = 0.
Terakhir, untuk kasusa(o)kurang darib(o),silhouette scoredapat didefinisikan
kembali sebagai:
s(o) =
b(o)−a(o)
a(o)
## =
b(o)
a(o)
## −
a(o)
a(o)
## =
b(o)
a(o)
## −1.
Karena syarat kasus danb(o)nonnegatif, maka:
## 0≤
b(o)
a(o)
## <1
sehingga
−1< s(o)≤0.

## 65
Dengan menggabungkan interval nilais(o)dari ketiga kasus tersebut, telah dibuk-
tikan dan disimpulkan bahwa nilaisilhouette scoreberkisar antara−1 hingga 1.
Analisis  klaster  yang  baik  diharapkan  terasosiasi  dengan  nilaia(o)yang
kecil danb(o)yang besar sehinggasilhouette scorebernilai mendekati 1. Untuk
menilai kebaikan hasil analisis klaster secara umum, nilai rata-ratasilhouette score
dari semua objek dalamdatasetjuga dapat digunakan (Han dkk., 2012).
Untuk  suatudatasettertentu,  perbedaan  hasil  akhir  analisis  klaster  dapat
terjadi karena bergantung pada pemilihan sentroida mula-mula (Johnson dan Win-
chern, 2007) . Namun, kualitas klaster yang lebih baik dapat diperoleh pada da-
ta yang terdistribusi normal atau normal standar. Hal ini dikarenakan normalisasi
atau standarisasi data mampu menghilangkan variabilitas dengan mempertahankan
karakteristik intrinsik data yang diperlukan untuk pembentukan klaster (Stoddard,
1979). Eltibi dan Ashour (2011) juga mendapati bahwa analisis klasterK-Means
pada data terdistribusi normal berlangsung lebih cepat dan menghasilkan taraf ga-
lat yang lebih rendah.
3.2.  Metode PortofolioMinimum Variance
Dalam berinvestasi, seorang investor pasti mengharapkanreturnsemaksi-
mal  mungkin  dengan  tingkat  volatilitas  yang  ia  dapat  terima.  Model  portofolio
minimum variance, yang dikenal juga sebagai modelmean-varianceatau model
Markowitz, merupakan suatu metode statistik yang ditemukan oleh Harry Marko-
witz, seorang ekonom asal Amerika Serikat, pada tahun 1952 yang ditujukan untuk
membentuk portofolio optimal.
Misalkan suatu portofolio mengandungnsaham. Ditentukanradalah vek-
torreturn,μadalah vektor ekspektasireturn,Σadalah matriks kovariansi yang
dibangun darireturnyang didefinisikan menurut Persamaan (2.18), danwadalah
vektor bobot yang memenuhi batasan pada Persamaan (2.31). Rumusan ekspek-
tasireturndan  variansi  portofolio  telah  dirumuskan  pada  Persamaan  (2.32)  dan
Persamaan (2.34). Model portofoliominimum variancedengan batasan tidak ada

## 66
shortselling(no-short-sale-constrained) dirumuskan sebagai:
min
w∈R
n
## 1
## 2
w
## ′
## Σw,
dengan kendala
n
## X
i=1
w
i
## = 1dan
w
i
≥0,  i= 1,...,n,(3.2)
denganw
i
,i= 1,...,nmerupakan elemen dari vektorw. Model ini disebut juga
constrained minimum variance portfolio(disingkat CMVP) (Dai, 2019).
Dengan memandang kendala pertidaksamaan pada Persamaan (3.2) sebagai:
## −w≤0
n
## ,
fungsi pengali Lagrange yang berkorespondensi dengan model CMVP tersebut di-
berikan sebagai:
L(w,λ,Λ) =
## 1
## 2
w
## ′
## Σw+λ(1−w
## ′
## 1
n
## ) + (−w
## ′
## )Λ
## =
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)−w
## ′
## Λ
denganΛ
## ′
## = [λ
## 1
## ,...,λ
n
]adalah vektor pengali Lagrange yang berkorespondensi
dengan kendala pertidaksamaan. Maka, syarat-syarat Kuhn-Tucker yang bersesua-
ian ialah:
## ∂L
## ∂w
## ′
## =
## ∂
## ∂w
## ′
## 
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)−w
## ′
## Λ
## 
=Σw−λ1
n
## −Λ
## ≥0
n
## ,(3.3)
w
## ′
## ∂L
## ∂w
## ′
## =w
## ′
(Σw−λ1
n
## −Λ)
## =w
## ′
## Σw−λw
## ′
## 1
n
## −w
## ′
## Λ
## = 0,(3.4)
## ∂L
## ∂Λ
## =
## ∂
## ∂Λ
## 
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)−w
## ′
## Λ
## 
## =−w
## ′
## ≤0
## ′
n
## ,(3.5)

## 67
## Λ
## ∂L
## ∂Λ
## = (−w
## ′
## )Λ
## =−w
## ′
## Λ
## = 0,(3.6)
## ∂L
## ∂λ
## =
## ∂
## ∂λ
## 
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)−w
## ′
## Λ
## 
## =−(w
## ′
## 1
n
## −1)
## = 0,(3.7)
w≥0
n
## ,dan(3.8)
λ≥0.(3.9)
Dengan banyak dan kompleksnya syarat-syarat Kuhn-Tucker, solusi opti-
mum untuk model CMVP dapat diselesaikan dengan lebih mudah melalui pende-
katan metode pengali Lagrange dengan fungsi Lagrange termodifikasi:
## L(w,λ) =
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1),(3.10)
yaitu  fungsi  Lagrange  yang  hanya  melibatkan  kendala  persamaan.  Mengacu  pa-
da Persamaan (2.48) dan Persamaan (2.49), solusi optimum fungsi Lagrange pada
Persamaan (3.10) di atas dapat diperoleh melalui derivatif-derivatif parsial terhadap
tiap parameter fungsi, yaitu:
∂L(w,λ)
## ∂w
## =
## ∂
## ∂w
## 
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)
## 
=Σw−λ1
n
## =0
n
## (3.11)
dan
∂L(w,λ)
## ∂λ
## =
## ∂
## ∂λ
## 
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)
## 
## =w
## ′
## 1
n
## −1
## = 0.(3.12)
Persamaan (3.11) diselesaikan untuk memperolehwsebagai berikut:
## Σw−λ1
n
## =0
n

## 68
⇐⇒Σw=λ1
n
⇐⇒w=λΣ
## −1
## 1
n
## .(3.13)
Nilaiwpada Persamaan (3.13) disubstitusikan ke Persamaan (3.10) sehingga dipe-
roleh:
## L(w,λ) =
## 1
## 2
w
## ′
## Σw−λ(w
## ′
## 1
n
## −1)
## =
## 1
## 2
(λΣ
## −1
## 1
n
## )
## ′
Σ(λΣ
## −1
## 1
n
## )−λ
##  
(λΣ
## −1
## 1
n
## )
## ′
## 1
n
## −1
## 
## =
## 1
## 2
λ
## 2
## 1
## ′
n
## (Σ
## −1
## )
## ′
## ΣΣ
## −1
## 1
n
## −λ
##  
λ1
## ′
n
## (Σ
## −1
## )
## ′
## 1
n
## −1
## 
## =
## 1
## 2
λ
## 2
## 1
## ′
n
## Σ
## −1
## ΣΣ
## −1
## 1
n
## −λ(λ1
## ′
n
## Σ
## −1
## 1
n
## −1)
## =
## 1
## 2
λ
## 2
## 1
## ′
n
## I
n
## Σ
## −1
## 1
n
## −λ
## 2
## 1
## ′
n
## Σ
## −1
## 1
n
## +λ
## =
## 1
## 2
λ
## 2
## 1
## ′
n
## Σ
## −1
## 1
n
## −λ
## 2
## 1
## ′
n
## Σ
## −1
## 1
n
## +λ
## =−
## 1
## 2
λ
## 2
## 1
## ′
n
## Σ
## −1
## 1
n
## +λ.
Maka, Persamaan (3.12) dapat dikerjakan kembali sebagai:
∂L(w,λ)
## ∂λ
## = 0
## ⇐⇒
## ∂
## ∂λ
## 
## −
## 1
## 2
λ
## 2
## 1
## ′
n
## Σ
## −1
## 1
n
## +λ
## 
## = 0
## ⇐⇒−λ1
## ′
n
## Σ
## −1
## 1
n
## + 1 = 0
## ⇐⇒−λ1
## ′
n
## Σ
## −1
## 1
n
## =−1
## ⇐⇒λ1
## ′
n
## Σ
## −1
## 1
n
## = 1
## ⇐⇒λ=
## 1
## 1
## ′
n
## Σ
## −1
## 1
n
## .(3.14)
Dengan menyubstitusikanλpada Persamaan (3.14) ke Persamaan (3.13), diperoleh
vektor bobot yang meminimalisasi variansi portofolio sebagai:
w
min
=λΣ
## −1
## 1
n
## =
## 
## 1
## 1
## ′
n
## Σ
## −1
## 1
n
## 
## Σ
## −1
## 1
n
## =
## Σ
## −1
## 1
n
## 1
## ′
n
## Σ
## −1
## 1
n
## .(3.15)

## 69
Langkah-langkah penyelesaian fungsi pengali Lagrange termodifikasi di atas di-
rangkum pada diagram alur pada Gambar 3.2 berikut.
Gambar 3.2 Diagram alur penyelesaian fungsi pengali Lagrange termodifikasi untuk CMVP.
Pendekatan lain untuk menyelesaikan syarat-syarat Kuhn-Tucker ialah pem-
rograman kuadratik yang penyelesaiannya dapat diperantarai oleh aplikasi kompu-
tasi statistik.
3.3.Genetic Algorithm
Genetic Algorithm(GA) merupakan algoritma optimisasi yang ditemukan
oleh John Holland pada tahun 1975. Sebagaimana namanya, inspirasi Holland da-
lam menemukan GA ialah bermacam karakteristik makhluk hidup yang dihasilkan
dari rekombinasi genetik. GA melibatkan populasi dengan anggota-anggota yang
disebutstringyang dianalogikan sebagai kromosom (Reeves, 2010).
## 3.3.1.  Terminologi Genetika
Suatu kromosom terdiri atas serangkaian gen. Suatu gen mempunyai posisi
fisik tertentu yang disebut lokus. Berbagai kemungkinan variasi gen-gen pada lokus
tertentu disebut alel. Kumpulan informasi genetik pada kromosom disebut genoti-
pe. Fenotipe adalah ciri-ciri fisik yang teramati pada suatu makhluk hidup yang
terasosiasi dengan genotipe tertentu (Mahner dan Kary, 1997).

## 70
Rekombinasi genetik dapat terjadi ketika dua buah kromosom mengalami
persilangan (crossover) atau mutasi. Persilangan adalah peristiwa bertukarnya se-
kumpulan gen di lokus tertentu pada sebuah kromosom dengan gen-gen di lokus
yang sama pada kromosom lain. Sementara, mutasi adalah peristiwa sekumpulan
gen yang terpilih secara acak mengalami pergantian nilai alel (Reeves, 2010).
3.3.2.  Konsep MatematisGenetic Algorithm
Pemahaman terhadap GA diawali dengan memahami permasalahan optimi-
sasi kombinatorial (combinatorial optimization problem, disingkat COP).
Definisi  3.3.1(Reeves,  2010)  Diberikan  ruang  pencarian  (search  space)  diskrit,
X, dan suatu fungsi,f, yang memetakanXmenujuR. Permasalahan optimisasi
kombinatorial didefinisikan sebagai:
min
x∈X
f(x),
denganxadalah vektor yang memuat variabel-variabel keputusan (decision vari-
ables) danfdisebut fungsi objektif.
Pada GA, kandidat solusi terhadap suatu COP dinyatakan sebagai representasi dari
variabel-variabel keputusan yang sesungguhnya. Kumpulan variabel keputusan ini
diibaratkan sebagai fenotipe, sedangkan representasinya diibaratkan sebagai geno-
tipe. Secara matematis, vektor representasi variabel keputusan didefinisikan sebagai
berikut.
Definisi 3.3.2(Reeves, 2010) Diberikan suatu permasalahan optimisasi kombina-
torial yang melibatkan ruang pencarian diskrit,X, fungsi objektif,f, dan vektor
variabel keputusan,x. Vektor representasi variabel keputusan dilambangkan oleh
lariksdengan panjangldan beranggotakan simbol-simbol dari ruang alfabet,A,
melalui pemetaan:
c:A
l
## 7→X.
Pada Definisi 3.3.2, elemen lariksdiibaratkan sebagai gen. Selain itu, pemetaanc
sering disebut pemetaan genotipe-fenotipe. Pada beberapa kasus, digunakan ruang

## 71
pencarianS ⊆A
l
karena beberapa solusi umum mula-mula mengakibatkan fungsi
menjadi tidak terdefinisi setelah melalui pemetaanc. Melalui representasi variabel,
permasalahan optimisasi pada Definisi 3.3.1 berubah menjadi
min
s∈S
g(s)
dengang(s) =f(c(s)).
Pada GA, persilangan ekuivalen dengan pertukaran sekumpulan elemen su-
atustringpada urutan tertentu dengan kumpulan elemenstringlain pada urutan
yang sama, sedangkan mutasi sama dengan mengubah sekumpulan elemen random
pada suatustringdengan nilai-nilai komplemennya.
3.3.3.  StrukturGenetic Algorithmdan Variasinya
Secara garis besar, langkah-langkah GA tersusun atas inisiasi populasi, se-
leksi, persilangan, mutasi, dan evaluasi populasi baru. Langkah-langkah ini dirang-
kum dalampseudocodeyang dapat dilihat pada Lampiran 2. Seiring berjalannya
waktu, GA mengalami berbagai modifikasi dan pengembangan. Mengacu pada Re-
eves (2010), penjelasan dari tiap langkah GA beserta variasi pada masing-masing
langkah ialah sebagai berikut:
-  Inisiasi populasi
Terdapat dua buah aspek yang perlu diperhatikan dalam menginisiasi populasi,
yaitu ukuran populasi dan metode pemilihan populasi. Menurut Reeves (1993,
dalam Reeves, 2010), ukuran populasi minimum harus mampu menjangkau tiap
titik dalam ruang pencarian hanya dengan persilangan. Hal ini mampu dicapai
jika setidaknya satu elemen alel di suatu lokus pada suatu populasistringbernilai
sama. Di sisi lain, metode pemilihan populasi sangat disarankan untuk bersifat
random, seperti pengambilan sampel tanpa pengembalian atauLatin hypercube
sampling(LHS).
## 2.  Seleksi
Pada mulanya, Holland mendasarkan seleksi pada metode roda rolet (roulette
wheel selection, disingkat RWS). Konsep di balik metode RWS mencermikan
putaran panah pada suatu roda rolet yang berakhir di antara batas-batas nilai ter-

## 72
tentu. Pada metode ini, setelah memperolehfitness, yaitu kualitas atau kebaikan
suatustringsebagai solusi optimum dari suatu fungsi objektif, dibangun sua-
tu fungsi sepenggal (piecewise function) yang didasarkan pada distribusi pro-
babilitas kumulatif yang proporsional terhadap nilai-nilaifitnesstersebut. Ke-
mudian, bilangan-bilanganpseudo-randomdibangkitkan untuk memilihstring-
stringyang  kemudian  menjadi  kumpulanstringinduk.  Pemilihan  didasarkan
pada interval-interval probabilitas pada fungsi sepenggal tersebut.
Metode RWS identik dengan variabilitas stokastik yang tinggi. Salah
satu metode alternatif yang mampu menangkal kekurangan ini ialah pemering-
katan (ranking). Metode pemeringkatan paling sederhana adalah pemeringkatan
linear yang mendefinisikan peluang suatustringberada pada peringkatkdalam
suatu populasi berukuranMsebagai:
## P[k] =α+βk,
denganαdanβmerupakan dua buah konstanta. AgarP[k]merupakan distribusi
probabilitas, diperlukan syarat:
## M
## X
k=1
## (α+βk) = 1.
Selanjutnya, kumpulan kromosom induk akan melalui tahap persilangan
dan/atau mutasi.
## 3.  Persilangan (crossover)
Persilangan dijalankan dengan suatu aturan terandomisasi, yaitu jika suatu bi-
langanpseudo-randomuniform bernilai lebih dari taraf persilangan (crossover
rate),χ. Persilangan dapat terjadi di satu atau lebih titik pada suatustring. Da-
lam hal ini, persilangan multititik dinilai lebih baik karena mampu mencegah
bias (Eshelman dkk., 1989 dalam Reeves, 2010).
Aturan randomisasi ini juga dapat dimodifikasi melalui metode persi-
langan uniform (uniform crossover). Pada metode ini, dilakukanmaskingde-
ngan memanipulasi operator persilangan menjadi suatustringbiner, yaitu berni-
lai 0 untuk menukar dan 1 untuk tidak menukar. Pola nilai 0 dan 1 dalamstring
tersebut dibangkitkan dari distribusi Bernoulli dengan parameterpyang bernilai

## 73
umum 0,5. Nilaipdapat diubah-ubah untuk menghasilkan bias terhadap salah
satu kromosom yang terlibat dalam persilangan (Syswerda, 1989 dalam Reeves,
## 2010).
## 4.  Mutasi
Tahap mutasi melibatkanmasking, yaitu dengan memanipulasi operator mutasi
menjadi  nilai  0  dan  1,  dengan  0  berarti  mutasi  tidak  dilakukan  dan  1  berarti
mutasi dilakukan. Mutasi dapat dipraktikkan dengan membangkitkan bilangan
random untuk tiap elemen padastringdan dibandingkan terhadap taraf mutasi,
μ. Mutasi dijalankan jika bilangan random tersebut bernilai lebih dariμ. Konsep
ini serupa dengan aturan terandomisasi pada tahap persilangan.
Algoritma di balik aturan randomisasi ini memerlukan komputasi yang
mahal (computationally expensive), terlebih jikastringberukuran panjang dan
populasi berukuran besar. Oleh karena itu, salah satu alternatif yang dapat dila-
kukan ialah dengan membandingkan suatu bilangan random yang dibangkitkan
dari distribusi POI(λ) dengan tingkat mutasi yang dihitung berdasarkan rumus
μ=λ/l, denganλadalah rata-rata banyak mutasi per kromosom danladalah
panjangstring. Melalui alternatif ini, jika terdapatmmutasi pada suatu kromo-
som, diambilmbilangan random yang terdistribusi uniform antaraλhinggal,
lalu tiap bilangan random dibandingkan denganμguna menentukan lokus-lokus
di mana mutasi akan dijalankan. Adapunλumumnya bernilai 1.
-  Populasi baru
Pendekatan umum Holland menerapkan seleksi, persilangan, dan mutasi pada
suatu populasi beranggotakanMkromosom secara berulang hingga memper-
olehMkromosom baru sebagai populasi baru. De Jong (1975, dalam Reeves,
2010)  mengembangkan  pendekatan  yang  melibatkan  konsep  elitisme  dan  pe-
numpangtindihan populasi (population overlapping). Konsep elitisme memper-
tahankan satustringterbaik dan menggantikan(M−1)stringlainnya dengan
stringbaru. Di sisi lain, konsep penumpangtindihan populasi menggantikan ha-
nya sebanyak suatu pecahan,G, dari populasi pada tiap iterasi pembangkitan.
## 6.  Terminasi
Syarat terminasi diperlukan untuk memastikan GA berlangsung dalam interval

## 74
waktu yang terbatas. Batasan yang umumnya digunakan sebagai syarat termina-
si adalah perulangan evaluasi, waktu, atau tingkat keberagaman di dalam popu-
lasi. Tingkat keberagaman yang cukup umum adalah statistik genotipe, seperti
proporsi suatu nilai alel tertentu.
Langkah-langkah GA di atas dirangkum pada diagram alur pada Gambar
3.3 berikut.
Gambar 3.3 Diagram alurGenetic Algorithm.
Beragamnya variasi GA beriringan dengan berkembangnya aplikasi dan pe-
nelitian terhadap algoritma ini. Terlebih, GA juga dirujuk dalam berbagai jurnal
terkait kecerdasan buatan dan riset operasi (Reeves, 2010).
3.4.Komodo Mlipir Algorithm
Komodo Mlipir Algorithm(KMA) merupakan salah satu metode optimisasi
matematis metaheuristik terbaru. Algoritma ini ditemukan oleh Prof. Dr. Suyanto,

## 75
S.T., M.Sc. dan dipresentasikan pada pengukuhannya sebagai guru besar bidang
Kecerdasan Buatan di Telkom University pada akhir tahun 2021.
Kelahiran KMA terinspirasi dari perilaku dan interaksi komodo di alam li-
ar serta gerakanmlipiryang berasal dari bahasa Jawa. Terdapat tiga jenis indivi-
du yang diperkenalkan dalam KMA, yaitu komodo jantan dewasa, komodo betina,
dan komodo jantan muda. Adaptasi perilaku komodo pada algoritma ini ditujuk-
an agar terdapat keseimbangan perilaku eksplorasi dan eksploitasi di antara ketiga
jenis komodo. Eksplorasi berarti pencarian solusi secara meluas pada himpunan pe-
nyelesaian untuk menghindari solusi optimum lokal, sedangkan eksploitasi adalah
pencarian di sekitar kandidat-kandidat solusi yang mendekati optimum global.
## 3.4.1.  Komodo
Komodo (Varanus komodoensis) atau biawak komodo merupakan reptil en-
demik yang berasal dari Nusa Tenggara Timur, Indonesia. Sebagaimana diatur da-
lam Peraturan Menteri Lingkungan Hidup dan Kehutanan (LHK) Nomor 92 Tahun
2018, komodo termasuk salah satu spesies satwa dilindungi di Indonesia. Populasi
komodo saat ini hanya tersebar di Taman Nasional Komodo, Pulau Flores, dan se-
jumlah pulau di sekitarnya (Fauzia dkk., 2024). Seekor komodo dewasa dapat ber-
kembang hingga mencapai panjang tiga meter dan berat 135 kilogram (The Editors
of Encyclopaedia Britannica, 2024). Perawakan komodo yang besar menjadikannya
suatu daya tarik bagi turis lokal hingga mancanegara.
Habitat yang cocok untuk kelangsungan hidup komodo ialah ekosistem sa-
bana tropis dan hutan kering. Sutomo (2020) mencatat bahwa terdapat tujuh belas
spesies tumbuhan yang mencirikan habitat komodo. Tumbuh-tumbuhan ini dido-
minasi dari famili Asteraceae (kenikir-nikiran), Fabaceae (polong-polongan), dan
Poaceae (rumput). Sayangnya, beberapa spesies tumbuhan ini mulai tergeser de-
ngan spesies-spesies asing invasif (invasive alien species) yang berpotensi meng-
ancam ekosistem habitat komodo menjadi hutan tropis kering musiman (seasonally
dry tropical forest). Ditambah dengan kehadiran sumber daya manusia yang tidak
bertanggung jawab, konservasi komodo merupakan upaya yang menantang.

## 76
## 3.4.2.  Perilaku Komodo
Fauzia dkk. (2024) mengelompokkan perilaku komodo secara umum menja-
di tujuh golongan, yaitu pemeliharaan diri, pencernaan, investigatif, perlindungan
diri, agonistik (berkelahi), bergerak, dan beristirahat. Sehari-hari, komodo gemar
berjemur di bawah sinar matahari, biasanya pada pagi dan sore hari. Untuk mem-
peroleh sumber energi, komodo berpindah-pindah (forage) untuk mencari sumber
makanan dan minuman dengan berjalan, berlari, atau melompat. Ketika komodo
merasa terganggu, ia akan menunjukkan sikap siaga pada kakinya, mengangkat ke-
palanya,  dan  menjulurkan  lidahnya.  Sementara,  dalam  keadaan  bahaya,  komodo
akan bersikap agresif dengan menghampiri sumber bahaya atau justru menjauhi-
nya. Sikap agresif dicirikan dengan mengejar, mendengus, mengibaskan ekor, dan
melakukan perlawanan. Di sisi lain, pergerakan menjauh lebih umum ditunjukkan
oleh komodo-komodo muda. Pada waktu beristirahat, komodo dapat berteduh di
bawah pohon yang rindang atau hinggap dan tidur di atas dahan pohon.
Komodo yang telah mencapai usia dewasa juga mampu melakukan perilaku
seksual dan parental. Perilaku seksual komodo meliputi pendekatan komodo jantan
kepada komodo betina dan bersetubuh. Perilaku seksual hanya dilakukan saat mu-
sim kawin. Oleh karenanya, komodo betina mempunyai perilaku reproduksi yang
bersifat fakultatif. Hal ini berarti bahwa komodo betina tidak selalu berkembang
biak secara seksual, tetapi juga dapat melakukan reproduksi aseksual melalui par-
tenogenesis. Pada partenogenesis, anakan yang dihasilkan akan menurunkan susun-
an gen (genotipe) yang sepenuhnya berasal dari induk betinanya. Meskipun dapat
memperbanyak jumlah populasi komodo sebagai satwa dilindungi, partenogenesis
secara terus-menerus mampu mengurangi keberagaman genetika. Selain itu, par-
tenogenesis juga terasosiasi dengan risiko penguranganfitnesspada anakan, yaitu
kualitas dirinya untuk melakukan reproduksi. Dalam hal ini, partenogenesis justru
berisiko meningkatkan probabilitas kepunahan hewan yang melakukannya (Watts
dkk., 2007). Adapun ketika sudah mencapai waktunya untuk bertelur, komodo be-
tina akan membangun sarang untuk menampung telur-telurnya dan menjaga sarang
tersebut dari pemangsa.

## 77
DalamKomodo Mlipir Algorithm, Suyanto dkk. (2022) hanya memfokuskan
beberapa ciri perilaku komodo jantan dewasa, komodo betina, dan komodo jantan
muda yang terkait dengan keseimbangan eksplorasi dan eksploitasi solusi dalam
menyelesaikan  permasalahan  optimisasi.  Komodo  jantan  dewasa  gemar  memak-
an mangsa, baik hewan lain, komodo jantan muda, maupun sesama komodo jant-
an dewasa. Ia memiliki naluri bertarung untuk mempertahankan mangsanya atau
memperebutkan seekor komodo betina. Antara dua ekor komodo jantan dewasa,
komodo yang berkualitas lebih rendah akan dikuasai oleh komodo yang berkualitas
lebih tinggi. Sementara, komodo yang berkualitas lebih tinggi dapat menghampiri
atau menjauh dari komodo berkualitas rendah. Oleh karena itu, komodo jantan de-
wasa berpeluang lebih tinggi untuk melakukan eksploitasi daripada eksplorasi dan
mempunyai perilakuhigh-exploitation low-exploration(HILE).
Jika seekor komodo jantan dewasa menang, komodo betina dapat dikawini
olehnya dan melakukan reproduksi seksual secara ovipar. Akan tetapi, jika komo-
do betina tersebut tidak merasakan ketertarikan akan sang komodo jantan, ia dapat
melakukan reproduksi aseksual melalui partenogenesis. Oleh karenanya, peluang
eksploitasi komodo betina sama dengan peluang eksplorasinya sehingga ia mem-
punyai perilakumedium-exploitation medium-exploration(MIME).
Sementara itu, komodo jantan muda menjaga jarak dari komodo jantan de-
wasa dan melahap mangsa yang tersisa ketika sudah merasa aman. Strategi perge-
rakan komodo jantan muda ini dijuluki sebagaimlipiryang berarti ”bergerak di tepi
secara berhati-hati”. Berdasarkan perilaku ini, komodo jantan muda cenderung me-
lakukan eksplorasi daripada eksploitasi. Perilaku ini dinamakanlow-exploitation
high-exploration(LIHE).
Ketiga jenis komodo dipandang sebagai tiga strata dengan kualitas yang ber-
urutan berdasarkan tingkat perilaku eksploitasinya. Oleh karena itu, komodo jantan
dewasa, komodo betina, dan komodo jantan muda acap kali juga dijuluki sebagai
komodo strata tinggi, sedang, dan rendah secara berturut-turut. Selanjutnya, agar le-
bih sederhana, komodo jantan dewasa akan disebut ”komodo dewasa” dan komodo
jantan muda akan dirujuk sebagai ”komodo muda”.

## 78
3.4.3.  Konsep MatematisKomodo Mlipir Algorithm
Tiap individu komodo dinyatakan sebagai vektor bernilai real,k, denganm
dimensi yang menyatakan posisi komodo tersebut pada ruang permasalahan. Kua-
litas seekor komodo ialah nilai fungsi yang hendak dioptimisasi atas vektor posisi
komodo tersebut, yaituf(k). Untuk tiap kasus optimisasi, ditentukannindividu
komodo sebagai populasi. Populasi komodo ini akan dibagi menjadi tiga kelompok
dengan porsi komodo dewasa sebesarp, yaitu suatu bilangan random dalam interval
(0,1), sedemikian sehingga terdapatqkomodo dewasa, satu komodo betina, dans
komodo muda dengan:
q=⌊(1−p)n⌋(3.16)
dan
s=n−q−1.(3.17)
pumumnya ditentukan sebesar 0,5 agarqdanstidak konvergen menuju nol. Se-
mentara, fungsifloordigunakan karenaqharus merupakan bilangan bulat.
Pergerakan komodo dewasa ke-idari posisi awal,k
i
, menuju posisi baru,
k
## ′
i
, didefinisikan sebagai berikut:
w
ij
## =
## 
## 
## 
## 
## 
r
## 1
## (k
j
## −k
i
## ),jikaf(k
j
)< f(k
i
## )ataur
## 2
## <0,5
r
## 1
## (k
i
## −k
j
## ),lainnya,
k
## ′
i
## =k
i
## +
q
## X
j=1
w
ij
,   j̸=i(3.18)
denganw
ij
melambangkan vektor pergerakan komodo dewasa ke-iterhadap ko-
modo dewasa ke-j,f(k
i
## )danf(k
j
)berturut-turut melambangkan kualitas komodo
dewasa ke-idan ke-j, sertar
## 1
danr
## 2
merupakan bilangan-bilangan random dari
distribusi normal dalam interval[0,1].
Pergerakan  komodo  betina  ditentukan  dari  metode  reproduksi  yang  dila-
kukan, yaitu reproduksi seksual (perkawinan) atau aseksual (partenogenesis). Re-
produksi seksual digambarkan melalui persamaan-persamaan berikut:
k
## ′
il
## =r
l
## ·k
il
## + (1−r
l
## )·k
jl
## (3.19)

## 79
k
## ′
jl
## =r
l
## ·k
jl
## + (1−r
l
## )·k
il
## (3.20)
denganl=  1,2,...,m;k
il
dank
jl
merupakan dimensi ke-ldari komodo jantan
dewasa ke-idan komodo betina ke-j,k
## ′
il
dank
## ′
jl
merupakan dimensi ke-ldari dua
ekor komodo anakan, sertar
l
adalah bilangan random dari distribusi normal dalam
interval[0,1]. Di sisi lain, reproduksi aseksual digambarkan sebagai penambahan
nilai kecil pada tiap dimensi posisi komodo betina, yaitu untuk komodo betina ke-i,
k
i
## :
## (k
i1
## ,k
i2
## ,...,k
im
## )→(k
## ′
i1
## ,k
## ′
i2
## ,...,k
## ′
im
## ).
Perubahan nilai tiap dimensi dirumuskan sebagai berikut:
k
## ′
il
## =k
il
## + (2r−1)α|a
l
## −b
l
## |,(3.21)
denganl=  1,...,m;k
i1
## ,k
i2
## ,...,k
im
## ∈[b
l
## ,a
l
## ];b
l
dana
l
berturut-turut melam-
bangkan batas bawah dan batas atas dimensi ke-l,radalah bilangan random yang
dibangkitkan dari distribusi normal, danαadalah jari-jari partenogenesis senilai
0,1 yang berarti penyelesaian baru dapat dibangkitkan dalam jari-jari sebesar sepu-
luh persen dari ruang pencarian (search space). Komodo betina akan membersamai
komodo anakan dengan kualitas terbaik. Maka, posisi baru komodo betina sama
dengan posisi komodo anakan tersebut.
Pergerakan komodo muda dirancang untuk mencari penyelesaian secara me-
luas dengan sedikit eksploitasi. Gerakanmlipirdiaplikasikan sebagai gerakan pada
salah satu dimensi komodo dengan probabilitas tertentu yang disebut tingkatmli-
pir(mlipir rate),d.dumumnya ditentukan sebesar 0,5. Pergerakanmlipirkomodo
muda ke-iuntuk mengikuti komodo dewasa ke-jdirumuskan:
w
ijl
## =
## 
## 
## 
## 
## 
r
## 1
## (k
jl
## −k
il
),jikalterpilih danr
## 2
< d;
## 0,lainnya
w
ij
## = [w
ij1
## ,w
ij2
## ,···,w
ijm
## ]
k
## ′
i
## =k
i
## +
q
## X
j=1
w
ij
## (3.22)

## 80
denganw
ij
adalah gerakan komodo muda ke-imengikuti komodo dewasa ke-j,k
il
dank
jl
adalah dimensi ke-ldari komodo muda ke-idan komodo dewasa ke-j,k
i
dank
## ′
i
adalah vektor posisi lama dan baru dari komodo muda ke-i,r
## 1
danr
## 2
adalah
bilangan-bilangan random dalam interval[0,1]yang dibangkitkan dari distribusi
normal; danladalah indeks dimensi yang dipilih secara random berdasarkan dis-
tribusi uniform,l= 1,2,...,m.r
## 1
berperan sebagai pengali pergerakan komodo
muda. Dengan nilai kurang dari satu,r
## 1
mengakibatkan pergerakan seekor komo-
do muda menuju komodo dewasa pada tiap dimensi tidak melebihi jarak di antara
dimensi keduanya. Sementara,r
## 2
digunakan untuk menentukan apakah pergerakan
pada dimensi komodo muda yang terpilih akan dilakukan.
Kualitas  tiap  komodo  dihitung  kembali.  Kemudian,  satu  komodo  dengan
kualitas terbaik dipilih sebagai solusi optimum sementara. Komodo ini dinotasikan
sebagaik
best
## .
Pada tiap iterasi dari KMA, ukuran populasindiperbarui menjadin
## ′
melalui
rumus berikut:
n
## ′
## =
## 
## 
## 
## 
## 
n−a,jikaδf
## 1
## >0danδf
## 2
## >0,
n+a,jikaδf
## 1
## = 0danδf
## 2
## = 0
## (3.23)
dengan:
δf
## 1
## =
## |f
i−2
## (k
best
## )−f
i−1
## (k
best
## )|
f
i−2
## (k
best
## )
## ,(3.24)
yaitu selisih kualitas solusi optimum antara pembangkitan ke-(i−2)dan pembang-
kitan ke-(i−1),
δf
## 2
## =
## |f
i−1
## (k
best
## )−f
i
## (k
best
## )|
f
i−1
## (k
best
## )
## ,(3.25)
yaitu selisih kualitas solusi optimum antara pembangkitan ke-(i−1)dan pembang-
kitan ke-i, danamelambangkan banyak komodo yang akan dikeluarkan atau di-
bangkitkan. Dalam kata-kata, jika dua pembangkitan berturut-turut meningkatkan
kualitas, ukuran populasi dikurangi sebanyakakomodo, sedangkan jika dua pem-
bangkitan berturut-turut justru menurunkan kualitas, ukuran populasi akan bertam-
bah sebanyakakomodo. Pada umumnya,aditentukan sebesar lima karena penemu
menganggap nilai ini cukup kecil dibandingkan dengan ukuran populasi optimal,
n, yang umumnya bernilai antara dua puluh hingga dua ratus ekor komodo.

## 81
3.4.4.  Struktur UmumKomodo Mlipir Algorithm
Langkah  awalKomodo  Mlipir  Algorithm(KMA)  diawali  dengan  menen-
tukann,p, dand, yaitu banyak individu dalam populasi komodo, porsi komodo
dewasa,  dan  tingkatmlipirsecara  berturut-turut.  Kemudian,nindividu  komodo
atasmdimensi diinisiasikan. Selanjutnya, kualitas tiap komodo, yaitu nilai fungsi
objektif atas tiap komodo, dihitung dan diurutkan sesuai peringkat. Pada permasa-
lahan minimisasi, semakin kecil nilai fungsi objektif, semakin besar peringkat suatu
komodo. Berdasarkan peringkat dan porsip, individu-individu komodo dipisahkan
menjadiqkomodo dewasa, satu komodo betina, danskomodo muda menurut Per-
samaan (3.16) dan Persamaan (3.17).
Selanjutnya, posisi tiap komodo, yaitu nilai tiap vektor, diperbarui menurut
jenis komodo yang bersesuaian. Vektor-vektor yang terasosiasi sebagai komodo de-
wasa akan bergerak menurut Persamaan (3.18). Vektor posisi komodo betina akan
diperbarui menurut Persamaan (3.19) atau Persamaan (3.21), yaitu secara berturut-
turut jika komodo betina memutuskan untuk mengawini komodo dewasa atau me-
lakukan partenogenesis. Masing-masing keputusan ini memiliki probabilitas untuk
terjadi sebesar 0,5. Terakhir, tiap vektor yang terasosiasi dengan komodo muda a-
kan diperbarui menurut Persamaan (3.22). Kualitas seluruh komodo diukur kembali
dan ditentukan satu komodo dengan kualitas terbaik,k
best
, sebagai solusi terbaik
sementara.
Pembaruan posisi komodo dalam KMA akan dijalankan setidaknya selama
tiga kali. Hal ini dikarenakan pembaruan ukuran populasi bergantung pada kualitas
solusi terbaik sementara dari tiga iterasi sebelum suatu iterasi. Setelah iterasi keti-
ga, ukuran populasi diperbarui menurut Persamaan (3.23). Jika populasi dikurangi,
akomodo dengan kualitas terburuk akan dikeluarkan dari populasi. Sementara, jika
populasi bertambah,akomodo akan dibangkitkan selayaknya inisiasi pada langkah
awal algoritma. Kondisi terminasi dicapai seandainya ukuran populasi baru untuk
iterasi  berikutnya,n
## ′
=n−a,  bernilai  nonpositif.  Jika  syarat  ini  terjadi,  itera-
si tersebut merupakan iterasi terakhir dan algoritma berhenti. Solusi terbaik yang
diperoleh dari iterasi terakhir menjadi solusi optimum untuk fungsi objektif.

## 82
Langkah-langkah KMA terangkum melalui diagram alur pada Gambar 3.4
di bawah danpseudocodeyang terdapat pada Lampiran 3.
Gambar 3.4 Diagram alurKomodo Mlipir Algorithm.
3.4.5.  PercobaanKomodo Mlipir Algorithm
Suyanto dkk. (2022) menguji performaKomodo Mlipir Algorithm(KMA)
dalam mengoptimisasi 23 fungsi acuan yang termuat dalam Rao (2020). Fungsi-
fungsi acuan tersebut dikelompokkan menjadi tiga golongan, yaitu fungsi-fungsi
high-dimension unimodal(HDU),high-dimension multimodal(HDM), danfixed-
dimen-sion multimodal(FDM). Fungsi-fungsihigh-dimensionmempunyai dimen-
si yang nilainya perlu ditentukan oleh pengguna, sedangkan fungsi-fungsifixed-

## 83
dimensionmempunyai besar dimensi yang tentu dan konstan. Di sisi lain,unimodal
danmultimodalmerujuk pada banyaknya nilai optimum pada suatu fungsi, yaitu sa-
tu atau lebih dari satu.
Pengujian kemampuan KMA terhadap fungsi-fungsiunimodaldirujuk se-
bagai ”evolusi fase pertama” atau fase pertama dari keseluruhan percobaan yang
dilakukan. Pada fase ini, ditentukann= 5,p=0,5, dand= (m−1)/m, yaitu
”tarafmlipirmaksimum”, dengan algoritma dilaksanakan sebanyak seribu iterasi.
Pada fase kedua, yaitu implementasi KMA pada fungsi-fungsimultimodal, digu-
nakan ukuran populasi mula-mula sebesarn=  200,p=0,5, dand=0,5. Fase
ini juga melibatkan penyetelan (tuning) mandiri terhadap ukuran populasi dalam
intervaln
min
= 20sampai dengann
max
= 200sebagai wujudself-adaptation. Pro-
sedur penyetelan mandiri ini tidak dijelaskan dalam literatur Suyanto dkk. (2022)
maupun penelitian-penelitian aplikatif yang terkait.

## BAB IV
## STUDI KASUS
## 4.1.  Deskripsi Data
Data riwayat harga keempat puluh lima saham dalam indeks saham LQ45
pada periode Desember 2023 sampai dengan November 2024 diunduh dari situs
webinvesting.comdan termuat pada Lampiran 4. Dalam bahasa pemrograman R,
data tersaji sebagai suatudataframeberukuran 237 baris dan 45 kolom. Artinya,
jual-beli saham berlangsung selama 237 hari kerja dalam periode waktu yang telah
ditentukan. Selain itu, dari situs web Bank Indonesia, diperoleh bahwa BI-Rate,
yang ekuivalen dengan tingkat bunga bebas risiko (r
f
), pada periode pengambilan
data ialah sebesar 6,00%.
4.2.ReturnTerealisasi Harian Saham
Dari data riwayat harga saham, nilaireturnterealisasi harian untuk tiap sa-
ham dihitung menurut Persamaan (2.26). Karena melangkahi satu satuan waktu,
dataframe returnhanya terdiri atas 236 baris.Dataframe returnsaham terdapat pa-
da Lampiran 5.
4.3.  Uji NormalitasReturnHarian Saham
Guna menghasilkan klasterK-Meansdengan kualitas yang baik,returnhari-
an saham diharapkan berdistribusi normal. Oleh karena itu, dilakukan uji Kolmogo-
rov-Smirnov terhadapreturnharian saham dengan distribusi normal. Sintaksis dan
luaran uji Kolmogorov-Smirnov tersaji pada Lampiran 6. Berdasarkan luaran yang
ada, terdapat hanya sembilan belas saham yangreturnhariannya berdistribusi nor-
mal. Saham-saham ini sajalah yang selanjutnya akan dilibatkan dalam analisis klas-
terK-Means.
Dari datareturnyang ada, diperoleh vektor meanreturndan deviasi standar
## 84

## 85
yang selanjutnya digunakan untuk menghitungSharpe ratiotiap saham, sebagai-
mana termuat pada Lampiran 7. Sebaran saham menurut meanreturndan deviasi
standar divisualisasikan melalui diagram pencar pada Lampiran 8.
4.4.  Analisis KlasterK-Means
Pada penelitian ini, pemilihan saham didasari oleh analisis klasterK-Means
danSharpe ratio. Bulani dkk. (2025) mengusulkan empat strategi pemilihan aset
untuk membentuk suatu portofolio melalui analisis klaster, yaitu sejumlah klaster
ataupun dengan penambahan beberapa aset menurut kedekatan aset dengan pusat
klasternya,  performa  aset,  atau  kriteria-kriteria  evaluasi  tertentu.  Pada  penelitian
ini,Sharpe ratiodigunakan sebagai ukuran acuan yang mampu mengevaluasi rasio
returnterhadap risiko yang terasosiasi dengan suatu saham.
Meski demikian, strategi Bulani dkk. (2025) tidak meliputi penentuan jum-
lah aset yang optimal dalam portofolio akhir. Hal ini didukung oleh ulasan literatur
oleh Zaimovic dkk. (2021), yaitu bahwa tidak terdapat definisi yang eksak akan
ukuran portofolio optimal untuk pasar, periode, maupun kalangan investor terten-
tu. Selain karena beragamnya opini ahli tentang diversifikasi risiko yang efektif,
besarnya risiko-risiko tak sistematis dipengaruhi oleh berbagai faktor, mulai dari
jenis kelamin investor, tingkat kepercayaan diri investor terhadap risiko, daya beli
investor yang dipengaruhi oleh besar pendapatan dan tingkat inflasi di negara asal
investor yang bersangkutan, hingga perubahan karakteristik aset seiring berjalannya
waktu. Karena penelitian ini dilatarbelakangi oleh karakter Generasi Z yang minim
modal dalam berinvestasi, Penulis menentukan jumlah saham akhir sebanyak dua
kali jumlah klaster yang terbentuk.
Jumlah klaster optimal dalam analisis klasterK-Meansditentukan berda-
sarkansilhouette score. Angka klaster dengansilhouette scoretertinggi menandak-
an jumlah klaster yang paling optimal. Percobaan pembentukan klaster dilakukan
untukKbernilai dua hingga sepuluh. NilaiKbesertasilhouette scoreyang berse-
suaian dipetakan pada diagram pada Lampiran 9. Diagram tersebut menunjukkan
bahwa berdasarkan meanreturndan risiko, pengelompokkan saham menjadi dua

## 86
klaster akan menghasilkan klaster-klaster dengan kualitas terbaik. Diperolehsilho-
uette scoreuntukK= 2sebesar 0,6767037.
Analisis klasterK-Meansdilakukan denganK= 2. Diperoleh pembagian
klaster pada Tabel 4.1 di bawah ini.
Tabel 4.1 Pembagian klaster untuk saham-saham denganreturnberdistribusi normal.
SahamKlaster
## AMMN1
## AMRT2
## ANTM2
## ASII2
## BBCA2
## BBNI2
## BBRI2
## BBTN2
## BMRI2
## HRUM1
## ICBP2
## INDF2
## INKP2
## ITMG2
## MBMA1
## PGAS2
## SMGR2
## TLKM2
## UNTR2
Visualisasi hasil analisis klasterK-Meansterdapat pada Lampiran 10.
BerdasarkanSharpe  ratiotiap  saham  dan  hasil  analisis  klasterK-Means,
dua saham dari tiap klaster denganSharpe ratiotertinggi dipilih untuk digabungk-
an sebagai suatu portofolio saham. Empat saham yang terpilih ialah MBMA dan

## 87
AMMN dari klaster 1 serta ANTM dan BBTN dari klaster 2 denganSharpe ra-
tioberturut-turut senilai –1,748777, –2,027074, –2,637897, dan –2,783715. Nilai
Sharpe ratiodari saham-saham denganreturnharian berdistribusi normal termuat
pada Lampiran 7.
4.5.  Pembobotan PortofolioMinimum Variance
Sebagaimana disebutkan pada Subbab 3.2, pembobotan portofolioconstrai-
ned minimum variance portfolio(CMVP) dapat dilakukan melalui dua pendekatan
yang  lebih  mudah,  yaitu  metode  pengali  Lagrange  dengan  fungsi  Lagrange  ter-
modifikasi dan pemrograman kuadratik. Kedua pendekatan tersebut akan digunak-
an pada penelitian ini. Lebih lanjut, Penulis akan membuktikan bahwa keduanya
menghasilkan pembobotan yang sama atas kasus dan data yang sama.
Pendekatan metode Lagrange diawali dengan membangkitkan matriks ko-
variansi sampel dari datareturn. Didefinisikan sebuah matriks,R, yang memuat
returnterealisasi harian dari keempat saham anggota portofolio, sebagai berikut:
## R
## ′
## =
## 
## 
## 
## 
## 
## 
## 
## 
## 0,0805084750,0263929620,015748031–0,041322314
## 0,035294118–0,002857143   –0,003875969   –0,025862069
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## –0,0270270270,007042254–0,0038759690,019607843
## 
## 
## 
## 
## 
## 
## 
## 
dengan kolom pertama hingga keempat berturut-turut mewakilireturnterealisasi
harian dari saham AMMN, ANTM, BBTN, dan MBMA. Keempat saham ini selan-
jutnya akan diwakili oleh indeks 1 sampai dengan 4. Ekspektasireturndiestima-
si oleh rata-ratareturntahunan yang dirumuskan pada Persamaan (2.27). Dengan
bantuan komputasi, diperoleh rata-ratareturntahunan yang dikelompokkan dalam
vektor mean berikut:
μ=
## 
## 
## 
## 
## 
## 
## 
## ̄
## R
## 1
## ̄
## R
## 2
## ̄
## R
## 3
## ̄
## R
## 4
## 
## 
## 
## 
## 
## 
## 

## 88
## =
## 
## 
## 
## 
## 
## 
## 
## 0,002186107
## –0,0004830982
## 0,0002767127
## –0.0002213262
## 
## 
## 
## 
## 
## 
## 
## .(4.1)
Lebih lanjut, estimasi variansi dan kovariansireturndirumuskan pada Persamaan
(2.28) dan Persamaan (2.29) dan dikomputasikan sebagai matriks kovariansi beri-
kut:
## Σ=
## 
## 
## 
## 
## 
## 
## 
Var(R
## 1
)Cov(R
## 1
## ,R
## 2
)   Cov(R
## 1
## ,R
## 3
)   Cov(R
## 1
## ,R
## 4
## )
Cov(R
## 2
## ,R
## 1
)Var(R
## 2
)Cov(R
## 2
## ,R
## 3
)   Cov(R
## 2
## ,R
## 4
## )
Cov(R
## 3
## ,R
## 1
)   Cov(R
## 3
## ,R
## 2
)Var(R
## 3
)Cov(R
## 3
## ,R
## 4
## )
Cov(R
## 4
## ,R
## 1
)   Cov(R
## 4
## ,R
## 2
)   Cov(R
## 4
## ,R
## 3
)Var(R
## 4
## )
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 0,0008134398–0,00004392384   –0,00000652270   –0,000043720495
## –0,000043923840,00052571760,000088367100,0001934192
## –0,000006522700,000088367100,00046029680,0001780035
## –0,0000437204950,00019341920,00017800350,001185855
## 
## 
## 
## 
## 
## 
## 
## .
## (4.2)
Selanjutnya, matriks kovariansi invers dikomputasikan dan diperoleh hasil sebagai
berikut:
## Σ
## −1
## =
## 
## 
## 
## 
## 
## 
## 
## 1.236,3251092,33711–14,2414836,29104
## 92,337112.064,29666    –282,61282    –290,60007
## –14,24148–282,61282    2.345,08624   –306,48186
## 36,29104–290,60007–306,48186938,12071
## 
## 
## 
## 
## 
## 
## 
## .
Bobot yang meminimumkan model CMVP pada Persamaan (3.2) diberikan
oleh Persamaan (3.15) dan dilambangkanw
min
. Pembilang dariw
min
ialah:
## Σ
## −1
## 1
## 4
## =
## 
## 
## 
## 
## 
## 1.236,32510···36,29104
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 36,29104···938,12071
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 1
## 1
## 1
## 1
## 
## 
## 
## 
## 
## 
## 

## 89
## =
## 
## 
## 
## 
## 
## 
## 
## 1.350,7118
## 1.583,4209
## 1.741,7501
## 377,3298
## 
## 
## 
## 
## 
## 
## 
## ,
sedangkan penyebutnya ialah:
## 1
## ′
## 4
## Σ
## −1
## 1
## 4
## =
h
## 1   1   1   1
i
## 
## 
## 
## 
## 
## 1.236,32510···36,29104
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 36,29104···938,12071
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 1
## 1
## 1
## 1
## 
## 
## 
## 
## 
## 
## 
## =5.053,213.(4.3)
Dengan demikian, diperoleh bobot portofoliominimum variance:
w
min
## =
## Σ
## −1
## 1
## 4
## 1
## ′
## 4
## Σ
## −1
## 1
## 4
## =
## 
## 
## 
## 
## 
## 
## 
## 1.350,7118
## 1.583,4209
## 1.741,7501
## 377,3298
## 
## 
## 
## 
## 
## 
## 
## 5.053,213
## =
## 1
## 5.053,213
## 
## 
## 
## 
## 
## 
## 
## 1.350,7118
## 1.583,4209
## 1.741,7501
## 377,3298
## 
## 
## 
## 
## 
## 
## 
## =
## 
## 
## 
## 
## 
## 
## 
## 0,26729764
## 0,31334935
## 0,34468174
## 0,07467127
## 
## 
## 
## 
## 
## 
## 
dengan:
f(w
min
## ) =0,00009894696.

## 90
Oleh karena itu, pada kasus ini, metode pengali Lagrange dengan fungsi Lagra-
nge termodifikasi terbukti menghasilkan bobot-bobot portofolio yang nonnegatif,
sebagaimana kendala pertidaksamaan pada model CMVP.
Di sisi lain, pendekatan pemrograman kuadratik diperantarai oleh fungsiso-
lve.QPdalam bahasa pemrograman R. Fungsi ini terdiri atas empat argumen wajib,
yaituDmat,dvec,Amat, danbvec. Keempat argumen ini merupakan masukan ber-
bentuk vektor dan matriks yang secara berturut-turut berkorespondensi denganD,
d,
## A
## ′
## =
## 
## 
## P
## R
## 
## 
## ,
dan
b=
## 
## 
q
s
## 
## 
yang  terdapat  pada  Persamaan  (2.62),  Persamaan  (2.63),  dan  Persamaan  (2.64).
Dengan menyesuaikan model CMVP pada Persamaan 3.2, masukan untuk keempat
argumen fungsisolve.QPsecara berturut-turut ialah:
## D=Σ,
d=0
## 4
## ,
## A
## ′
## =
## 
## 
## 1
## ′
## 4
## I
## 4
## 
## 
## ,dan
b=
## 
## 
## 1
## 0
## 4
## 
## 
## .
Dalam komputasi, didefinisikan pula argumenmeq, yaitu banyaknya kendala ber-
bentuk persamaan dari model pemrograman kuadratik yang hendak diselesaikan.
Pada kasus ini, hanya terdapat satu kendala persamaan sehinggameqbernilai 1.
Komputasi dan hasil komputasi untuk portofoliominimum varianceterlam-
pir pada Lampiran 11. Pendekatan metode pengali Lagrange dan pemrograman ku-
adratik terbukti mengembalikan nilai pengali Lagrange dan bobot-bobot portofolio
yang sama.

## 91
4.6.  Pembobotan Portofolio MenggunakanGenetic Algorithm
KomputasiGenetic  Algorithm(GA)  menggunakan  bahasa  pemrograman
R diperantarai oleh fungsigadalamlibrary GA. Ditemukan oleh Luca Scrucca,
seorang  peneliti  dalam  bidang  Statistika  Terapan  asal  Italia,  fungsigamemuat
argumen-argumen berikut:
ga(type =c("binary", "real-valued", "permutation"),
fitness = ...,
lower,upper, nBits,
population = gaControl(type)$population,
selection = gaControl(type)$selection,
crossover = gaControl(type)$crossover,
mutation = gaControl(type)$mutation,
popSize = 50,
pcrossover = 0.8,
pmutation = 0.1,
elitism = base::max(1,round(popSize
## *
## 0.05)),
updatePop = FALSE,
postFitness = NULL,
maxiter = 100,
run = maxiter,
maxFitness = Inf,
names= NULL,
suggestions = NULL,
optim= FALSE,
optimArgs =list(method = "L-BFGS-B",
poptim = 0.05,
pressel = 0.5,
control=list(fnscale = -1,
maxit = 100)),
keepBest = FALSE,
parallel = FALSE,
monitor =if(interactive()) gaMonitorelseFALSE,

## 92
seed = NULL)
Fungsigadapat digunakan untuk melangsungkan tiga jenis kasus GA, ya-
itu biner (binary), bernilai real (real-valued), dan permutasi (permutation). Jenis
kasus menjadi argumen utama yang wajib dinyatakan oleh pengguna fungsi kare-
na masukan dari argumen ini terhubung secara otomatis dengan metode pemilihan
populasi mula-mula, seleksi, persilangan, dan mutasi yang sesuai. Metode-metode
bawaan dari tahap-tahap ini diaktifkan melalui subfungsigaControl. Akan tetapi,
pengguna juga dapat mendefinisikan metode-metode yang diinginkan secara spesi-
fik.
Fungsigadirancang untuk menyelesaikan permasalahan maksimisasi. Fung-
si objektif yang akan dioptimisasi menjadi masukan bagi argumenfitness. Jika per-
masalahan yang hendak diselesaikan adalah minimisasi, pengguna dapat menega-
sikan fungsi objektif sehingga fungsigamemaksimisasi negatif dari fungsi objektif
yang dikehendaki.
Kendala-kendala yang didefinisikan secara matematis juga dapat dilibatkan
dalam fungsiga. Secara komputasional, batasan-batasan nilai (boundaries) dapat
dinyatakan untuk tiap variabel dalam fungsi objektif pada argumenlowerdanup-
per, sedangkan kendala-kendala persamaan dan/atau pertidaksamaan didefinisikan
secara bersamaan dengan fungsi objektif untuk argumenfitness.
Argumen-argumen lain dalam fungsigabersifat opsional. Argumen-argu-
men ini telah mempunyai definisi nilai bawaan, tetapi pengguna juga dapat men-
definisikan nilai-nilai argumen ini secara mandiri. Argumen-argumen ini antara la-
in ukuran populasi (popSize), taraf persilangan (pcrossover), taraf mutasi (pmuta-
tion), taraf elitisme untuk pemilihan populasi baru (elitism), pembaharuan populasi
(updatePop), dan jumlah iterasi maksimum (maxiter).
Sebagai contoh, diperhatikan fungsi Sphere dalam Rao (2020) yang didefi-
nisikan sebagai berikut:
f(x) =
n
## X
i=1
x
## 2
i
## .(4.4)
Fungsi tersebut mempunyai nilai minimum global sebesar nol yang dicapai melalui

## 93
solusi(0,0,...,0). Menggunakan fungsiga, fungsi Sphere berdimensin= 30di-
minimisasi dalam ruang pencarian berupa interval[−100,100]untuk tiapx
i
## . Meng-
acu pada eksperimen Suyanto dkk. (2022), ditentukan ukuran populasi sebanyak
seratus, taraf persilangan sebesar 0,8, dan taraf mutasi sebesar 0,05. Dengan iterasi
sebanyak seribu kali, sintaksis dijalankan sebagaimana termuat pada Lampiran 12.
Nilai minimum fungsi Sphere yang diperoleh ialah sebesar 0,3148834.
Untuk menciptakan kesebandingan antara GA dan model portofoliomini-
mum  variance,  GA  juga  akan  diuji  pada  model  CMVP  yang  termuat  pada  Per-
samaan (3.2). Guna memuat fungsi objektif dan kendala secara bersamaan dalam
argumenfitnessdari fungsiGA, fungsi Lagrange pada Persamaan (3.10) akan di-
gunakan. Diperhatikan bahwa fungsi objektif dari model CMVP dapat dijabarkan
sebagai jumlahan ganda berikut:
## 1
## 2
w
## ′
## Σw=
## 1
## 2
## 4
## X
i=1
## 4
## X
j=1
w
i
w
j
σ
ij
## =
## 1
## 2
## 4
## X
i=1
## (w
i
w
## 1
σ
i1
## +w
i
w
## 2
σ
i2
## +w
i
w
## 3
σ
i3
## +w
i
w
## 4
σ
i4
## )
## =
## 1
## 2
## (w
## 2
## 1
σ
## 2
## 1
## +w
## 1
w
## 2
σ
## 12
## +w
## 1
w
## 3
σ
## 13
## +w
## 1
w
## 4
σ
## 14
## +w
## 2
w
## 1
σ
## 21
## +w
## 2
## 2
σ
## 2
## 2
## +w
## 2
w
## 3
σ
## 23
## +w
## 2
w
## 4
σ
## 24
## +w
## 3
w
## 1
σ
## 31
## +w
## 3
w
## 2
σ
## 32
## +w
## 2
## 3
σ
## 2
## 3
## +w
## 3
w
## 4
σ
## 34
## +w
## 4
w
## 1
σ
## 41
## +w
## 4
w
## 2
σ
## 42
## +w
## 4
w
## 3
σ
## 43
## +w
## 2
## 4
σ
## 2
## 4
## )
## =
## 1
## 2
##  
w
## 2
## 1
σ
## 2
## 1
## +w
## 2
## 2
σ
## 2
## 2
## +w
## 2
## 3
σ
## 2
## 3
## +w
## 2
## 4
σ
## 2
## 4
## + 2(w
## 1
w
## 2
σ
## 12
## +w
## 1
w
## 3
σ
## 13
## +w
## 1
w
## 4
σ
## 14
## +w
## 2
w
## 3
σ
## 23
## +w
## 2
w
## 4
σ
## 24
## +w
## 3
w
## 4
σ
## 34
## )
## 
## =
## 1
## 2
## (w
## 2
## 1
σ
## 2
## 1
## +w
## 2
## 2
σ
## 2
## 2
## +w
## 2
## 3
σ
## 2
## 3
## +w
## 2
## 4
σ
## 2
## 4
## )
## + (w
## 1
w
## 2
σ
## 12
## +w
## 1
w
## 3
σ
## 13
## +w
## 1
w
## 4
σ
## 14
## +w
## 2
w
## 3
σ
## 23
## +w
## 2
w
## 4
σ
## 24
## +w
## 3
w
## 4
σ
## 34
## ).(4.5)
denganw
i
melambangkan bobot saham ke-idalam portofolio danσ
ij
melambangk-
an kovariansi antara saham ke-idan ke-j. Dengan menyubstitusikan nilai-nilai va-

## 94
riansi dan kovariansi dari Persamaan (4.2), fungsi objektif berupa jumlahan ganda
pada Persamaan (4.5) dapat dituliskan kembali sebagai:
## 1
## 2
w
## ′
## Σw=
## 1
## 2
## (0,0008134398w
## 2
## 1
## +0,0005257176w
## 2
## 2
## +0,0004602968w
## 2
## 3
## +0,001185855w
## 2
## 4
## )
## + (−0,00004392384w
## 1
w
## 2
## −0,00000652270w
## 1
w
## 3
## −0,000043720495w
## 1
w
## 4
## +0,00008836710w
## 2
w
## 3
## +0,0001934192w
## 2
w
## 4
## +0,0001780035w
## 3
w
## 4
## )
## =0,0004067199w
## 2
## 1
## +0,0002628588w
## 2
## 2
## +0,0002301484w
## 2
## 3
## +0,0005929275w
## 2
## 4
## −0,00004392384w
## 1
w
## 2
## −0,00000652270w
## 1
w
## 3
## −0,000043720495w
## 1
w
## 4
## +0,00008836710w
## 2
w
## 3
## +0,0001934192w
## 2
w
## 4
## +0,0001780035w
## 3
w
## 4
## .
## (4.6)
Lebih lanjut, pengali Lagrange dari fungsi Lagrange pada Persamaan (3.10) telah
diberikan pada Persamaan (3.14) serta dikomputasikan pada Persamaan (4.3) dan
kendala persamaan pada model CMVP dapat dijabarkan sebagai berikut:
w
## ′
## 1
## 4
## = 1
## ⇐⇒w
## 1
## +w
## 2
## +w
## 3
## +w
## 4
## = 1
## ⇐⇒w
## 1
## +w
## 2
## +w
## 3
## +w
## 4
## −1 = 0.(4.7)
Dengan demikian, fungsi Lagrange yang ekuivalen dengan fungsifitnessdiberikan
sebagai berikut:
## L(w,λ) =0,0004067199w
## 2
## 1
## +0,0002628588w
## 2
## 2
## +0,0002301484w
## 2
## 3
## +0,0005929275w
## 2
## 4
## −0,00004392384w
## 1
w
## 2
## −0,00000652270w
## 1
w
## 3
## −0,000043720495w
## 1
w
## 4
## +0,00008836710w
## 2
w
## 3
## +0,0001934192w
## 2
w
## 4
## +0,0001780035w
## 3
w
## 4
## −0,0001978939(w
## 1
## +w
## 2
## +w
## 3
## +w
## 4
## −1).

## 95
Adapun kendala nilai dari CMVP dapat dipenuhi dengan membatasi ruang penca-
rianWdalam interval:
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 0
## 0
## 0
## 0
## 
## 
## 
## 
## 
## 
## 
## ,
## 
## 
## 
## 
## 
## 
## 
## 1
## 1
## 1
## 1
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## .(4.8)
Studi kasus optimisasi portofolio saham dalam penelitian ini ditujukan un-
tuk menemukan bobot-bobot portofolio bernilai real yang meminimalisasi risiko.
Oleh karenanya, studi kasus ini termasuk dalam jenis kasus bernilai real. Penulis
menggunakan metode-metode bawaan untuk tahap inisiasi populasi, persilangan,
dan mutasi, sedangkan metode pemeringkatan linear (linear ranking) akan didefi-
nisikan secara spesifik untuk tahap seleksi. Batas bawah dan atas ruang pencarian
Wpada Persamaan (4.8) menjadi masukan untuk argumenlowerdanupper.
Komputasi GA dijalankan menurut sintaksis yang termuat pada Lampiran
- Berdasarkan hasil komputasi tersebut, diperoleh bahwa bobot yang meminima-
lisasi fungsi objektif adalah:
w
## GA
## =
## 
## 
## 
## 
## 
## 
## 
## 0,2673440
## 0,3133429
## 0,3446411
## 0,07478484
## 
## 
## 
## 
## 
## 
## 
dengan
f(w
## GA
## ) =0,00009896927.
4.7.  Penyesuaian Konsep MatematisKomodo Mlipir Algorithm
Pada pemaparan konsepKomodo Mlipir Algorithmoleh Suyanto dkk. (2022),
rumusan pergerakan komodo muda diberikan sebagai berikut:
w
ij
## =
## 
## 
## 
## 
## 
## P
m
l=1
r
## 1
## (k
jl
## −k
il
## ),jikar
## 2
< d;
## 0,lainnya
k
## ′
i
## =k
i
## +
q
## X
j=1
w
ij
,  i̸=j.

## 96
Rumusan di atas kurang tepat karena vektork
i
tidak dapat dijumlahkan dengan ska-
larw
ij
. Selain itu, keterangan ”i̸=j” tidak relevan karena keduanya berturut-turut
melambangkan indeks dari komodo muda dan komodo jantan, yakni dua golong-
an komodo yang berbeda. Oleh karena itu, dengan menyesuaikan narasi deskriptif
pada Suyanto dkk. (2022), rumusan di atas disesuaikan menjadi Persamaan (3.22).
Selain itu, distribusi probabilitas acuan untuk memilihlsecara random turut
dialihkan dari distribusi normal menjadi distribusi uniform. Penyesuaian ini dila-
kukan karena tidak terdapat penjelasan lebih lanjut akan pemetaan probabilitas dari
distribusi normal terhadap tiap nilailyang memungkinkan, yaitu1,2,...,m.
4.8.  Pembahasan PercobaanKomodo Mlipir Algorithm
Penulis  mendapati  bahwa  percobaan  pengujian  performaKomodo  Mlipir
Algorithm(KMA) oleh Suyanto dkk. (2022) memuat beberapa inkonsistensi dan
kejanggalan. Pada evolusi fase pertama, ukuran populasi sebanyak lima individu
komodo tidak sejalan dengan ketentuan ukuran populasi optimal, yaitu sebanyak
dua puluh hingga dua ratus. Pada fase ini pula, tidak terdapat penjelasan mengapa
d= (m−1)/mdirujuk sebagai ”tarafmlipirmaksimum”, mengingatdmerupakan
suatu nilai probabilitas yang bernilai maksimum satu. Syarat terminasi tidak lagi
didasarkan pada ukuran populasi yang telah mengalami adaptasi (n
## ′
), tetapi batas-
an jumlah iterasi. Di sisi lain, pada evolusi fase kedua, konsep maupun prosedur
penyetelan mandiri ukuran populasi tidak dijabarkan sehingga tidak dapat diprak-
tikkan kembali pada penelitian-penelitian berikutnya.
Secara umum, pemisahan percobaan menjadi dua fase berdasarkan golong-
an fungsi merupakan keunikan yang terdapat pada penelitian Suyanto dkk. (2022).
Pada penelitian ini, algoritma hanya akan dijalankan sebanyak satu fase menurut
alur yang telah digambarkan melaluipseudocodepada Lampiran 3. Perbandingan
antara percobaan pada penelitian Suyanto dkk. (2022) dan penelitian ini diberikan
pada Tabel 4.2 berikut.

## 97
Tabel 4.2 Perbandingan penelitian Suyanto dkk. (2022) dengan penelitian ini.
## Aspek
## Penelitian
Suyanto dkk. (2022)
Penelitian ini
Banyak faseDuaSatu
Ukuran populasi
mula-mula
LimaDua ratus
## Tarafmlipir(d)(m−1)/m0,5
Syarat terminasiJumlah iterasiUkuran populasi baru (n
## ′
## )
Penyetelan mandiri
ukuran populasi
AdaTidak ada
4.9.  Pembobotan Portofolio MenggunakanKomodo Mlipir Algorithm
Sebagai algoritma optimisasi baru, fungsi bawaanKomodo Mlipir Algori-
thm(KMA) saat ini hanya tersedia dalam bahasa pemrograman MATLAB. Agar
dapat diimplementasikan menggunakan bahasa pemrograman R, Penulis menyu-
sun fungsiKMAmenurut kerangka algoritma pada Lampiran 3. Susunan lengkap
fungsiKMAtersebut terdapat pada Lampiran 14.
Dalam  KMA,  terdapat  beberapa  operasi  yang  dijalankan  secara  berulang
pada tiap iterasi, yaitu pengukuran kualitas komodo, penggerakan komodo menu-
rut golongannya (jantan, betina, atau muda), dan pembandingan kualitas komodo
terbaik dari tiga iterasi terakhir sebagai dasar untuk memperbarui ukuran populasi.
Agar  algoritma  berjalan  secara  efisien,  operasi-operasi  ini  dimuat  dalam  fungsi-
fungsi buatan secara terpisah. Fungsivektor
kualitasmengukur kualitas seekor ko-
modo, yang ekuivalen dengan nilai sebuah fungsi objektif atas komodo tersebut.
Fungsigerakjantan,gerakbetina, dangerakmudasecara berturut-turut memper-
barui posisi komodo jantan, betina, dan muda menurut Persamaan (3.18), Persa-
maan (3.19), dan Persamaan (3.22). Terdapat beberapa fungsi bawaan dari bahasa
pemrograman R yang sama-sama digunakan dalam ketiga fungsi ini, yakni antara
lainset.seed,qnorm,runif,pnorm,  danmapply.  Fungsiset.seeddiaktifkan  agar

## 98
fungsi  pembangkit  bilangan  random  menghasilkan  bilangan  random  yang  sama
setiap  kali  pembangkitan  dilakukan.qnorm,runif,  danpnormdigunakan  secara
bersamaan untuk membangkitkan bilangan random berdistribusi normal dalam in-
terval  nilai(0,1).runifmembangkitkan  bilangan  random  berdistribusi  uniform.
Dengan argumenmin = pnorm(0)danmax = pnorm(1), ditentukan bahwa batas
minimum dan maksimum dari bilangan random uniform yang akan dibangkitkan
ialahφ(0) =0,5 danφ(1) = 1, denganφ(x)merupakan PDF normal standar yang
diberikan oleh Persamaan (2.23). Bilangan random uniform menjadi masukan ba-
gi fungsiqnormyang ekuivalen dengan invers CDF normal standar, yaitu invers
dari Persamaan (2.24), mentransformasi bilangan random uniform menjadi suatu
bilangan random dari distribusi normal standar. Terakhir, fungsidf1dandf2secara
berturut-turut ekuivalen dengan Persamaan (3.24) dan Persamaan (3.25).
FungsiKMAmemerlukan tiga argumen wajib, yaitu ukuran populasi komo-
do, dimensi tiap komodo, dan fungsi objektif. Ketiga argumen ini secara berturut-
turut dinyatakan sebagaiN,m, danfunc. Selain itu, terdapat tujuh argumen pilihan,
yaitup,d,a,max
iter,lower,upper, dannormalize.p,d, danasecara berturut-turut
melambangkan porsi komodo dewasa, tingkatmlipir, dan banyak pertambahan atau
pengurangan ukuran populasi. Sebagai bawaan, ketiga argumen ini bernilai 0,5, 0,5,
dan 5.maxitermerupakan banyak iterasi maksimum dengan nilai bawaan sebesar
seratus, sedangkanlowerdanupperialah batas minimum dan maksimum untuk tiap
elemen komodo dengan nilai bawaan sebesar nol dan satu, sebagaimana interval ni-
lai bobot portofolio CMVP.normalizemerupakan variabel biner, dengan nilaiTrue
atauTberarti bahwa normalisasi akan dilakukan pada saat algoritma berlangsung.
Pada tiap iterasinya, fungsiKMAterlebih dahulu mengukur kualitas komo-
do mula-mula dan mengurutkannya dari kualitas tertinggi hingga terendah. Fungsi
kemudian  menghitung  banyaknya  komodo  jantan  dan  muda,  lalu  melakukan  se-
gmentasi terhadap komodo-komodo dalam populasi berdasarkan strata kualitasnya.
Setelah itu, fungsi memanggil fungsi-fungsi penggerak yang telah disusun sebe-
lumnya untuk menggerakan tiap komodo menurut golongannya. Komodo-komodo
yang telah digerakkan kemudian disatukan dalam sebuah vektor dan dinormalisasi.

## 99
Normalisasi merupakan tahap yang Penulis tambahkan terhadap algoritma
Suyanto dkk. (2022) yang bertujuan agar jumlah elemen dari seluruh dimensi ko-
modo bernilai sama dengan satu. Modifikasi lainnya ialahclipping, yaitu meng-
embalikan nilai satu dimensi komodo atau lebih ke dalam interval(0,1).Clipping
melibatkan fungsipmindanpmax. Fungsipmaxmengembalikan maksimum anta-
ra elemen tiap dimensi dan nol guna mencegah elemen bernilai negatif, sedangkan
fungsipminmengembalikan minimum antara luaran fungsipmaxdan satu untuk
menghindari elemen bernilai lebih dari satu.  Setelah melalui prosesclipping, ti-
ap komodo dinormalisasi kembali untuk memastikan jumlah elemen dari seluruh
dimensinya bernilai sama dengan satu.
Terakhir,  kualitas  tiap  komodo  diukur  kembali  dan  seluruh  komodo  diu-
rutkan secara menurun berdasarkan nilai kualitas barunya. Komodo terbaik ialah
komodo dengan kualitas paling kecil, yaitu komodo yang meminimisasi fungsi ob-
jektif. Memasuki iterasi ketiga, komodo terbaik dari tiga iterasi terakhir akan ditin-
jau untuk memperbarui ukuran populasi komodo. Algoritma memasuki terminasi
jika pembaruan ukuran populasi komodo bernilai nonpositif. FungsiKMAdiakhiri
dengan visualisasi evolusi komodo terbaik dari iterasi pertama hingga terakhir.
KMA terlebih dahulu diaplikasikan pada fungsi Sphere yang telah diberikan
pada Persamaan (4.4). Ukuran populasi mula-mula dan dimensi tiap komodo seca-
ra berturut-turut ditentukan sebesar dua ratus dan tiga puluh, sama dengan aplika-
siGenetic Algorithm(GA) untuk mengoptimisasi fungsi tersebut. Setelah melalui
42 iterasi, diperoleh solusi terbaik akhir dengan kualitas sebesar 133.796,9. Nilai
ini sangat jauh dari minimum global fungsi tersebut yang bernilai nol. Visualisasi
menunjukkan adanya peningkatan nilai optimum yang sangat ekstrem dari iterasi
kedua ke iterasi ketiga, diikuti tren penurunan yang landai dan fluktuatif hingga ite-
rasi terakhir. Hal ini menunjukkan bahwa KMA yang dibangun berdasarkan konsep
matematisnya tidak stabil dalam mencari solusi optimum untuk fungsi Sphere. Ak-
an tetapi, jika ukuran populasi mula-mula ditambah guna memperbanyak iterasi,
solusi optimum global memungkinkan untuk dicapai. Sintaksis dan luaran untuk
aplikasi ini dapat diamati pada Lampiran 15.

## 100
Selanjutnya, KMA diaplikasikan untuk mencari solusi optimum CMVP yang
telah dirancang untuk penelitian ini. Diperoleh bahwa bobot yang meminimisasi
fungsi objektif ialah:
w
## KMA
## =
## 
## 
## 
## 
## 
## 
## 
## 0,3122141
## 0,2713546
## 0,4036373
## 0,01279399
## 
## 
## 
## 
## 
## 
## 
dengan:
f(w
## KMA
## ) =0,0001031325.
Kualitas solusi terbaik akhir dari KMA tidak lebih baik daripada kualitas solusi
terbaik akhir yang diperoleh dari GA. Lebih lanjut, visualisasi juga menunjukkan
ketidakstabilan KMA dalam mencari solusi terbaik untuk permasalahan ini.
Penulis mendapati dua buah faktor yang diduga menyebabkan masalah fluk-
tuasi solusi terbaik pada kelangsungan KMA. Pertama, ruang pencarian solusi op-
timal untuk permasalahan ini cukup sempit dengan adanya kendala persamaan dan
kendala nilai (berbentuk pertidaksamaan). Jika diilustrasikan, irisan antara kedua
kendala ini terdapat pada kurvaw
## 1
## +w
## 2
## +w
## 3
## +w
## 4
=  1berbentuk garis yang
dibatasi oleh batas-batas luar kurva kendala nilai. Hal ini mengakibatkan solusi op-
timal yang berlaku hanya terdapat di sepanjang garis tersebut. Kedua, pembaruan
posisi suatu komodo dilakukan melalui randomisasi dan operasi penjumlahan. Ma-
ka, tidak dapat dipungkiri bahwa jumlahan tersebut menghasilkan posisi baru di
luar kendala permasalahan, yaitu dimensi yang bernilai negatif atau lebih dari satu.
Peristiwa ini belum pernah disebutkan atau dicantumkan pada penelitian-penelitian
terdahulu, termasuk oleh Suyanto dkk. (2022) selaku pionir KMA, sehingga tidak
terdapat solusi eksak untuk menyelesaikannya.
Sintaksis dan luaran untuk aplikasi KMA terhadap CMVP dapat dilihat pada
## Lampiran 16.

## 101
4.10.  Pembobotan Portofolio MenggunakanParticle Swarm Optimization
Serupa denganKomodo Mlipir Algorithm(KMA),Particle Swarm Optimi-
zation(PSO) merupakan salah satu algoritma metaheuristik lain yang berbasis ke-
cerdasan kawanan. Secara khusus, PSO terinspirasi dari pergerakan serangga atau
hewan bersayap lainnya dalam terbang menyusuri suatu wilayah dan mencari titik-
titik terbaik untuk mendarat. Fenomena ini melandasi konsep pencarian solusi ter-
baik dari suatu ruang pencarian.
PSO dijalankan pada bahasa pemrograman R menggunakan bantuan fungsi
psoptimyang termuat dalamlibrary pso. Fungsi ini memuat dua argumen wajib,
yaitupardanfn.pardiisi  dengan  dimensi  permasalahan  optimisasi,  sedangkan
fndiisi  dengan  fungsi  objektif.  Secara  bawaan,  jenis  optimisasi  yang  dilakukan
melalui fungsipsoadalah minimisasi. Oleh karena itu, pada penelitian ini, fungsi
yang akan dimasukkan ke dalam argumenfntidak perlu dinegasikan. Selain itu,
beberapa argumen lain yang dapat didefinisikan secara opsional ialahlowerdan
upperyang  secara  berturut-turut  diisi  oleh  batas  bawah  dan  batas  atas  dari  tiap
dimensi.
Sintaksis dan luaran untuk pembobotan portofolio menggunakan PSO terda-
pat pada Lampiran 17. Berdasarkan luaran yang ada, diperoleh bahwa bobot porto-
folio yang meminimisasi fungsi objektif yang tertuang pada Persamaan (3.2) ialah:
## 
## 
## 
## 
## 
## 
## 
## 0,26729764
## 0,31334935
## 0,34468174
## 0,07467127
## 
## 
## 
## 
## 
## 
## 
dengan:
f(w
min
## ) =0,00009894696.
Luaran ini diperoleh setelah seribu iterasi dan bernilai sama dengan portofolio yang
dibobotkan melalui metodeminimum variance.

## 102
## 4.11.  Perhitungan Beta Portofolio
Treynor ratiodanJensen’s alphamelibatkan beta portofolio dalam perhitu-
ngannya. Sebagaimana tertuang pada subbab mengenaiCapital Asset Pricing Mo-
del(CAPM), beta portofolio bersifat relatif terhadap portofolio pasar. Pada kasus
ini, asumsi-asumsi CAPM dianggap berlaku sehingga Indeks Harga Pasar Gabung-
an (IHSG) ditentukan sebagai portofolio pasar.
Menyesuaikan Persamaan (2.38), beta tiap sekuritas di dalam suatu porto-
folio terhadap portofolio pasar dirumuskan sebagai:
β
## M
i
## =
σ
iM
σ
## 2
## M
## ,
denganσ
iM
adalah kovariansi antarareturnsekuritas danreturnportofolio pasar
sertaσ
## 2
## M
adalah  variansi  portofolio  pasar.  Dengan  menggabungkan  beta  seluruh
sekuritas menjadi suatu vektor,β
## M
, beta portofolio kemudian diperoleh melalui
rumus berikut:
β
## P
## =w
## ′
β
## M
## .
Data riwayat harga harian IHSG termuat pada Lampiran 18. Komputasire-
turndari data harga harian termuat pada Lampiran 19. DatareturnIHSG selanjut-
nya digabungkan denganreturnharian keempat saham yang tergabung dalam por-
tofolio yang diteliti untuk menghitung beta tiap saham relatif terhadap portofolio
pasar. Diperoleh vektor atas beta-beta saham sebagai berikut:
β
## M
## =
## 
## 
## 
## 
## 
## 
## 
## 0,5538391
## 0,7996983
## 1,3914885
## 1,1772685
## 
## 
## 
## 
## 
## 
## 
## ,
berdasarkan komputasi yang termuat pada Lampiran 20.
Komputasi  beta  dari  ketiga  portofolio  terdapat  pada  Lampiran  21.  Hasil
komputasi menunjukkan bahwa beta portofolio yang dibangun menggunakan meto-
deminimum variance,Genetic Algorithm(GA),Komodo Mlipir Algorithm(KMA),
danParticle Swarm Optimization(PSO) bernilai 0,9661536, 0,9662512, 0,9666368,

## 103
dan 0,9661536 secara berturut-turut. Nilai-nilai ini bermakna bahwa portofolio KMA
menghasilkan ekspektasi perubahanreturnyang paling tinggi untuk tiap persen per-
ubahanreturnIHSG, yakni sebesar 96,66 persen. Meski demikian, keempat porto-
folio tidak lebih volatil daripada portofolio pasar.
## 4.12.  Perbandingan Performa Portofolio
Sejauh komputasi yang telah dilakukan hingga subbab sebelumnya, porto-
foliominimum variancemerupakan portofolio yang paling meminimisasi risiko da-
lam model CMVP. Meski demikian, dalam penelitian ini, kualitas portofolio juga
akan dibandingkan melalui tiga ukuran performa portofolio yang telah Penulis ten-
tukan, yaituSharpe ratio,Treynor ratio, danJensen’s alpha. Rumusan tiap ukuran
yang secara berturut-turut termuat pada Persamaan (2.39), Persamaan (2.44), dan
Persamaan (2.43) diimplementasikan menjadi fungsi-fungsi buatan, lalu diterapk-
an pada portofoliominimum variance,Genetic Algorithm(GA),Komodo Mlipir
Algorithm(KMA), danParticle Swarm Optimization(PSO).
Hasil komputasi untuk ketiga ukuran diberikan pada Tabel 4.3 di bawah ini.
Tabel 4.3 Perbandingan ukuran performa portofoliominimum variance, GA, KMA, dan PSO.
PortofolioSharpe ratioTreynor ratioJensen’s alpha
Minimum variance0,28305410,063447370,1192077
## GA0,28309660,063457650,1192297
## KMA0,43641850,09982210,1544285
## PSO0,28305410,063447370,1192077
Tabel di atas menunjukkan bahwa ukuran performa seluruh portofolio bernilai ku-
rang dari satu. Untuk ukuran-ukuran berbasis rasio, hal ini berarti bahwa portofolio-
portofolio yang dibentuk tidak mampu mengembalikanreturnyang sebanding atau
lebih besar daripada risiko keseluruhan maupun risiko sistematis semata. Secara
statistik,  peristiwa  ini  mungkin  terjadi  karena  pemilihan  kombinasi  saham  yang
kurang maksimal atau metode analisis klaster yang kurang baik karena sensitif ter-
hadap pencilan. Di sisi lain, pada realitasnya, nilaiTreynor ratioyang lebih rendah

## 104
daripadaSharpe ratiodapat mengindikasikan bahwa risiko sistematis pada peri-
ode observasi saham, yaitu Desember 2023 sampai dengan November 2024, ber-
kontribusi lebih banyak daripada risikofirm-specificpada perhitungan nilai risiko
keseluruhan. Peristiwa ini menandakan bahwa dalam satu hingga dua tahun tera-
khir, guncangan pada perekonomian Indonesia menimpa seluruh sektor ekonomi
sehingga berdampak lebih besar daripada perubahan-perubahan yang berasal dari
badan-badan usaha. Meski demikian,Jensen’s alphayang bernilai positif menci-
rikan bahwa ekspektasireturndari ketiga portofolio mampu melebihirequired re-
turnyang diperlukan. Artinya, meskipun ekspektasireturntidak sebanding dengan
risiko investasi, nilai yang diharapkan masih melebihi minimum yang dikompensa-
sikan terhadap risiko tersebut.
Untuk  masing-masing  ukuran,  portofolio  yang  dibobotkan  melalui  KMA
terasosiasi dengan nilai yang tertinggi, sedangkan portofolio yang dibobotkan me-
lalui metodeminimum variancedan PSO terasosiasi dengan nilai yang terendah.
Hal ini menunjukkan bahwa KMA merupakan alternatif algoritma yang baik terha-
dap metode-metode optimisasi yang telah diuji dan digunakan pada masa lampau,
khususnya untuk permasalahan optimisasi portofolio.

## BAB V
## PENUTUP
## 5.1.  Kesimpulan
Penelitian ini dapat disimpulkan sebagai berikut:
-  Normalitasreturnharian dan analisis klasterK-Meansditentukan sebagai dasar
pemilihan saham dari indeks saham LQ45 untuk pembentukan portofolio. Dari
45 saham, terdapat sembilan belas saham denganreturnharian berdistribusi nor-
mal. Dua klaster terbentuk dari sembilan belas saham tersebut. Dua saham dari
tiap klaster dilibatkan dalam portofolio berdasarkan nilaiSharpe ratiotertinggi.
-  Dengan adanya kendala persamaan dan kendala batas dalam modelno-short-
sale-constrained minimum variance portfolio(CMVP), metodeminimum vari-
ancedanGenetic Algorithm(GA) mampu membangun portofolio dengan bobot-
bobot positif, sedangkan metodeKomodo Mlipir Algorithm(KMA) masih me-
munculkan bobot-bobot negatif dalam iterasi-iterasinya. Dengan kata lain, in-
vestor yang menggunakan metode KMA perlu mempraktikkanshortsellingatau
melanggar kendala batas yang ditentukan.
-  Berdasarkan tiga ukuran performa portofolio, yaituSharpe ratio,Treynor ratio,
danJensen’s alpha, portofolio yang dihasilkan melalui KMA mempunyai per-
forma terbaik, sedangkan portofolio yang dihasilkan melalui metodeminimum
variancedanParticle Swarm Optimization(PSO) menunjukkan performa terbu-
ruk.
## 5.2.  Saran
Guna menunjang perkembangan penelitian di masa yang akan datang, Pe-
nulis memberikan saran-saran berikut:
-  Analisis klaster untuk pemilihan saham dapat divariasikan dengan metode-metode
analisis klaster dengan basis yang berbeda, seperti hierarki, kepadatan, dangrid.
## 105

## 106
-  Algoritma-algoritma yang diturunkan atau dileburkan dengan KMA, sepertiSto-
chastic Komodo Algorithm(SKA),Improved Adaptive Komodo Mlipir Algori-
thm(IKMA), danHybrid Pelican Komodo Algorithm(HPKA), dapat digunakan
dalam eksperimen penyelesaian permasalahan optimisasi, khususnya optimisasi
portofolio.
-  Sintaksis  KMA  pada  penelitian  ini  masih  dapat  disempurnakan  dan  disusun
menjadilibraryyang terintegrasi pada berbagai bahasa pemrograman yang di-
pakai secara lebih meluas, seperti R dan Python.
-  Performa KMA dapat diteliti lebih jauh untuk permasalahan optimisasi portofo-
lio, misalnya dengan:
a.  menambah keragaman jenis instrumen investasi dalam portofolio, seperti lo-
gam mulia dan mata uang kripto, atau
b.  menggunakan jenis portofolio yang lebih kompleks, sepertiL
## 1
## -norm-constrained
minimum variance portfolio(L
## 1
-NCMVP) danL
## 1
-regularization minimum
variance portfolio(L
## 1
## -RMVP).

## DAFTAR PUSTAKA
Aditya, I. A., Simaremare, A. A., Raharjo, J., Suyanto, dan Wijayanto, I. (2022).
”Komodo Mlipir Algorithm to Solve Generator Scheduling Problems”.2nd In-
ternational Conference on Electronic and Electrical Engineering and Intelligent
System (ICE3IS), Indonesia, 84—88.
Bain, L. J. dan Engelhardt, M. (1992).Introduction to Probability and Mathemati-
cal Statistics(Edisi 2). Duxbury.
Bank  Indonesia.  (t.t.)BI-Rate.  Bank  Indonesia.  https://www.bi.go.id/id/fungsi-
utama/moneter/bi-rate/default.aspx.
Berk, J. dan DeMarzo, P. (2016).Corporate Finance(Edisi 4). Pearson.
Bitar, A. W., de Curvalho, N., dan Gatignol, V. (2023).Covariance matrix estima-
tion for robust portfolio allocation. HAL Open Science.
Bodie, Z., Kane, A., dan Marcus, A. J. (2014).Investments(Edisi 10). McGraw-Hill
## Education.
Bulani, V., Bezbradica, M., dan Crane, M. (2025).Improving Portfolio Management
Using Clustering and Particle Swarm Optimization.Mathematics, 13, 1623—
## 1650.
Chen,J.(2021,28Januari).Risk-FreeAsset:Defi-
nitionandExamplesofAssetTypes.Investopedia.
https://www.investopedia.com/terms/r/riskfreeasset.asp#:∼:text=A%20risk%2D
free%20asset%20is,the%20U.S.%20government%20backs%20them.
Chen,  J.  (2022,  29  September).Risk  Asset:  Definition  and  Examples  From
Stocks   to   Crypto.   Investopedia.   https://www.investopedia.com/terms/r/risk-
asset.asp#:∼:text=A%20risk%20asset%20is%20any,%2C%20real%20estate%2
## C%20and%20currencies.
## 107

## 108
Cheong, D., Kim, Y. M., Byun, H. B., Oh, K. J., dan Kim, T. Y. (2017). ”Using
genetic algorithm to support clustering-based portfolio optimization by investor
information”.Applied Soft Computing, 61, 593—602.
Cogneau,   P.   dan   H
## ̈
ubner,   G.   (2009).   ”The   101   ways   to   measure   portfo-
lio   performance”.   [Naskah   tidak   terpublikasi].   University   of   Li
## `
ege.   ht-
tps://dx.doi.org/10.2139/ssrn.1326076.
Dai, Z. (2019). ”A Closer Look at the Minimum-Variance Portfolio Optimization
Model”.Mathematical Problems in Engineering, 2019, 1—8.
Data Services Division Bursa Efek Indonesia. (2024).IDX Company Fact Sheet:
LQ45, August 2024 - January 2025.
Dharmapuri, C. M. dan Reddy, B. V. R. (2024). ”Spectrum and Energy Efficiency in
CRNs Using Dynamic Channel Reservation and Komodo Mlipir Optimization”.
IETE Journal of Research, 70, 11, 8291—8299.
Dubinskas,  P.  dan  Urb
## ˇ
sien
## ̇
e.  (2017).  ”Investment  Portfolio  Optimization  by  Ap-
plying a Genetic Algorithm-based Approach”.Ekonomika, 96(2), 66—78.
Eltibi, M. F. dan Ashour, W. M. (2011). ”Initializing K-Means Clustering Algorithm
using Statistical Information”.International Journal of Computer Applications,
## 29(7), 51—55.
Faia, R., Pinto, T., Vale, Z., Corchado, J. M., Soares, J., dan Lezama, F. (2018).
”Genetic  Algorithms  for  Portfolio  Optimization  with  Weighted  Sum  Approa-
ch”.2018 IEEE Symposium Series on Computational Intelligence (SSCI), India,
1823—1829. https://doi.org/10.1109/SSCI.2018.8628773.
Fauzia, A. M., Kusrini, M. D., Mulyani, Y. A., Nusantara, M. G. G., Sari, F. E., Se-
tiawan, R. A., dan Ariefiandy, A. (2024). ”Community Perspectives in Ethogram
for Komodo Dragon (Varanus komodoensis) in the Wild”.Media Konservasi, 29
## (2), 91—100.

## 109
Finaka,  A.  W.  (2021).Peleburan  dan  Pembentukan  Kementerian  Baru.  Indone-
siabaik.id.https://indonesiabaik.id/videografis/peleburan-dan-pembentukan-
kementerian-baru.
Fitri,A.N.(2024).TrenInvestasiDigitalNaik,67%Masyara-
katIndonesiaBerencanaInvestasiTahunDepan.Kontan.co.id.
https://investasi.kontan.co.id/news/tren-investasi-digital-naik-67-masyarakat-
indonesia-berencana-investasi-tahun-depan.
Flores-Fernandez,   G.   A.,   Jimenez-Carrion,   M.,   Gutierrez,   F.,   dan   Sanchez-
Ancajima, R. A. (2024). ”Genetic Algorithm and LSTM Artificial Neural Ne-
twork for Investment Portfolio Optimization”.Journal of Wireless Mobile Ne-
tworks, Ubiquitous Computing, and Dependable Applications, 15(2), 27—46.
Han, J., Kamber, M., dan Pei, J. (2012).Data Mining Concepts and Techniques
(Edisi 3). Morgan Kaufmann Publishers.
Hogg, R. V., McKean, J. W., dan Craig, A. T. (2005).Introduction to Mathematical
Statistics(Edisi 6). Pearson Prentice Hall.
Jagannathan, R. dan Ma, T. (2003). ”Risk Reduction in Large Portfolios: Why Im-
posing the Wrong Constraints Helps”.NBER Working Paper Series.
Jati, G. K., Kuwanto, G., Hashmi, T., dan Widjaja, H. (2023). ”Discrete komodo
algorithm for traveling salesman problem”.Applied Soft Computing, 139, 1—
## 21.
Johnson, R. A. dan Winchern, D. W. (2007).Applied Multivariate Statistical Ana-
lysis(Edisi 6). Pearson Prentice Hall.
Kraska-Miller, M. (2013).Nonparametric Statistics for Social and Behavioral Sci-
ences. CRC Press.
Kuhn, H. W. dan Tucker, A. W. (1951). ”Nonlinear Programming”.Proceedings
of the 2nd Berkeley Symposium on Mathematics, Statistics and Probability, 2,
## 481—492.

## 110
Kusuma, P. D. dan Dinimaharawati, A. (2022). ”Hybrid Pelican Komodo Algori-
thm”.International Journal of Advanced Computer Science and Applications,
## 13, 6, 46—55.
Kusuma, P. D. dan Kallista, M. (2022). ”Stochastic Komodo Algorithm”.Interna-
tional Journal of Intelligent Engineering and Systems, 15, 4, 156—166.
Li,  H.  dan  Shi,  N.  (2022).  ”Application  of  Genetic  Optimization  Algorithm  in
Financial  Portfolio  Problem”.Computational  Intelligence  and  Neuroscience,
## 2022(1), 1—9.
Li, L. dan Zhao, M. (2022). ”A Novel Komodo Mlipir Algorithm and Its Applica-
tion in PM2.5 Detection”.Atmosphere2022, 13(12), 2051, 1—17.
Lim, S., Kim, M., dan Ahn, C. J. (2020). ”A Genetic Algorithm (GA) Approach to
the Portfolio Design Based on Market Movements and Asset Valuations”.IEEE
## Access, 8, 140234—140249.
Liu, Q. dan Zhang, X. (2022). ”Improved Adaptive Komodo Mlipir Algorithm”.
IEEE Access, 10, 67883—67897.
## Lupt
## ́
a
## ˇ
cik, M. (2010).Mathematical Optimization and Economic Analysis. Springer.
Mahner, M. dan Kary, M. (1997). ”What Exactly Are Genomes, Genotypes and
Phenotypes? And What About Phenomes?”.Journal of Theoretical Biology, 186
## (1), 55—63.
Marhfor,  A.  (2016).  ”Portfolio  Performance  Measurement:  Review  of  Literature
and Avenues of Future Research”.American Journal of Industrial and Business
## Management, 6, 432—438.
Nocedal, J. dan Wright, S. J. (2006).Numerical Optimization(Edisi 2). Springer.
Nurawan,M.R.danMahendra,R.(2023)ApaituIn-
deksLQ45?IniKriteriaDanDaftarSahamnya.Bisnis.com.
https://market.bisnis.com/read/20231110/7/1712648/apa-itu-indeks-lq45-
ini-kriteria-dan-daftar-sahamnya.

## 111
Pramuji, S. (2024).Gen Z Serbu Bursa Saham. Datanesia. https://datanesia.id/gen-
z-dominasi-investor-individu/.
Putri, B. U. (2021).Pembentukan Kementerian Investasi Disebut Demi Naikkan Wi-
bawa BKPM. Tempo. https://www.tempo.co/politik/pembentukan-kementerian-
investasi-disebut-demi-naikkan-wibawa-bkpm-522693.
Rajwar, K., Deep, K., dan Das, S. (2023). ”An exhaustive review of the metaheu-
ristic algorithms for search and optimization: taxonomy, applications, and open
challenges”.Artificial Intelligence Review, 56, 13187—13257.
Rao,  R.  V.  (2020).  ”Rao  algorithms:  Three  metaphor-less  simple  algorithms  for
solving optimization problems”.International Journal of Industrial Engineering
## Computations, 11, 107—130.
Reeves, C. R. (2010). ”Genetic algorithms”. Dalam Gendreau, M. dan Potvin, J.
(Eds.),Handbook of Metaheuristics(Edisi 2, hlm. 109—139). Springer.
Ripley, B. D. (1987).Stochastic Simulation. John Wiley & Sons.
Ross, S. M. (2010).Introduction to Probability Models(Edisi 10). Academic Press.
Schott, J. R. (2017).Matrix Analysis for Statistics(Edisi 3). John Wiley & Sons,
## Inc.
Soundarayaa, R. K. dan Balasubramanian, C. (2024). ”Komodo Mlipir Algorithm-
based optimal route determination mechanism for improving Quality of Service
in Vehicular ad hoc network”.Sustainable Computing: Informatics and Systems,
## 42, 1—19.
Stewart, J. (2015).Calculus: Early Transcendentals(Edisi 8). Cengage Learning.
Stoddard, A. M. (1979). ”Standardization of Measures Prior to Cluster Analysis”.
## Biometrics, 35(4), 765—773.

## 112
Sukono,  Hidayat,  Y.,  Lesmana,  E.,  Putra,  A.  S.,  Napitupulu,  H.,  dan  Supian,  S.
(2018). ”Portfolio optimization by using linear programing models based on ge-
netic algorithm”.IOP Conference Series: Materials Science and Engineering,
## Indonesia, 300, 1—9.
Sun,  R.,  Ma,  T.,  Liu,  S.,  dan  Sathye,  M.  (2019).  ”Improved  Covariance  Matrix
Estimation  for  Portfolio  Risk  Measurement:  A  Review”.Journal  of  Risk  and
## Financial Management, 12(1), 48.
Sutomo. (2020). ”Vegetation Composition of Savanna Ecosystem as a Habitat For
The Komodo Dragon (Varanus komodoensis) on Padar and Komodo Islands, Flo-
res East Nusa Tenggara Indonesia”.Journal of Tropical Biodiversity and Biote-
chnology, 5(1), 10—15.
Suyanto, Ariyanto, A. A., dan Ariyanto, A. F. (2022). ”Komodo Mlipir Algorithm”.
## Applied Soft Computing, 114, 1—17.
Taha, H. A. (2007).Operations Research: An Introduction(Edisi 8). Pearson Pren-
tice Hall.
The  Editors  of  Encyclopaedia  Britannica.  (2024,  22  Oktober).Komodo  dragon.
https://www.britannica.com/animal/Komodo-dragon.
Vasiani, V. D., Handari, B. D., dan Hertono, G. F. (2020). ”Stock portfolio optimiza-
tion using priority index and genetic algorithm”.Journal of Physics: Conference
## Series, 1442, 1—5.
Virlics, A. (2013). ”Investment Decision Making and Risk”.Procedia Economics
and Finance, 6, 169—177.
Watts, P., Buley, K., Sanderson, S., Boardman, W. S. J., Ciofi, C., dan Gibson, R.
(2007). ”Parthenogenesis in Komodo dragons”.Nature, 444, 1021—1022.
Wiranto, A. A. (2022).Tren Investasi Meningkat, 71% Orang Indonesia Berinvesta-
si Lewat Aplikasi. SWA. https://swa.co.id/read/377717/tren-investasi-meningkat-
## 71-orang-indonesia-berinvestasi-lewat-aplikasi.

## 113
Zaimovic, A., Omanovic, A., dan Arnaut-Berilo, A. (2021). ”How Many Stocks
Are Sufficient for Equity Portfolio Diversification? A Review of the Literature”.
Journal of Risk and Financial Management, 14, 551—580.
Zhou, Q. (2020).Portfolio Optimization with Robust Covariance and Conditional
Value-at-Risk Constraints. Cornell University.
Zhu, S. (2016). ”Research on the Portfolio Optimization Model under Quantitative
Constraint Based on Genetic Algorithm”.Journal of Mathematical Finance, 6,
## 465—470.

## LAMPIRAN
Lampiran 1.  Daftar Saham dalam Indeks LQ45
No.Nama perusahaanKode saham
1.Aspirasi Hidup Indonesia TbkACES
2.Adaro Energy Indonesia TbkADRO
3.AKR Corporindo TbkAKRA
4.Amman Mineral Internasional TbkAMMN
5.Sumber Alfaria Trijaya TbkAMRT
6.Aneka Tambang TbkANTM
7.Bank Jago TbkARTO
8.Astra International TbkASII
9.Bank Central Asia TbkBBCA
10.Bank Negara Indonesia (Persero) TbkBBNI
11.Bank Rakyat Indonesia (Persero) TbkBBRI
12.Bank Tabungan Negara (Persero) TbkBBTN
13.Bank Mandiri (Persero) TbkBMRI
14.Bank Syariah Indonesia TbkBRIS
15.Barito Pacific TbkBRPT
16.Bukalapakcom TbkBUKA
17.Charoen Pokphand Indonesia TbkCPIN
18.ESSA Industries Indonesia TbkESSA
19.xL Axiata TbkEXCL
20.Gudang Garam TbkGGRM
21.GoTo Gojek Tokopedia TbkGOTO
22.Harum Energy TbkHRUM
23.Indofood CBP Sukses Makmur TbkICBP
## 114

## 115
No.Nama perusahaanKode saham
24.Vale Indonesia TbkINCO
25.Indofood Sukses Makmur TbkINDF
26.Indah Kiat Pulp & Paper TbkINKP
27.Indocement Tunggal Prakarsa TbkINTP
28.Indosat TbkISAT
29.Indo Tambangraya Megah TbkITMG
30.Jasa Marga (Persero) TbkJSMR
31.Kalbe Farma TbkKLBF
32.Mitra Adiperkasa TbkMAPI
33.Merdeka Battery Materials TbkMBMA
34.Merdeka Copper Gold TbkMDKA
35.Medco Energi Internasional TbkMEDC
36.Dayamitra Telekomunikasi TbkMTEL
37.Perusahaan Gas Negara TbkPGAS
38.Pertamina Geothermal Energy TbkPGEO
39.Bukit Asam TbkPTBA
40.Industri Jamu dan Farmasi Sido Muncul TbkSIDO
41.Semen Indonesia (Persero) TbkSMGR
42.Telkom Indonesia (Persero) TbkTLKM
43.Sarana Menara Nusantara TbkTOWR
44.United Tractors TbkUNTR
45.Unilever Indonesia TbkUNVR
(Bursa Efek Indonesia, 2024)

## 116
Lampiran 2.Pseudocode Genetic Algorithm(GA)
Tentukan populasi kromosom mula-mula;
WHILEKondisi terminasi tidak terpenuhiDO:
## REPEAT
IFkondisi persilangan terpenuhiTHEN
{Pilih kromosom induk;
Pilih parameter-parameter persilangan;
Lakukan persilangan};
IFkondisi mutasi terpenuhiTHEN
{Pilih titik-titik mutasi;
Lakukan persilangan};
Evaluasifitnesskromosom anakan
UNTILkromosom anakan yang dihasilkan berjumlah cukup;
Pilih populasi baru;
## END WHILE
(Reeves, 2010)

## 117
Lampiran 3.Pseudocode Komodo Mlipir Algorithm(KMA)
Tentukann,p, dand;
Inisiasikannindividu yang masing-masing terdiri atasmdimensi;
WHILEKondisi terminasi tidak terpenuhiDO:
FORtiap komodo:
Hitung kualitasnya, lalu urutkan sesuai peringkat;
## END FOR
Berdasarkan peringkat dan porsip, pisahkan populasi menjadiqkomodo
dewasa, satu komodo betina, danskomodo muda;
FORtiap komodo dewasa:
Lakukan pergerakan dan perbarui posisi;
## END FOR
Perbarui posisi komodo betina dengan mengawini komodo dewasa
terbaik atau melakukan partenogenesis;
FORtiap komodo muda:
Lakukan pergerakan dan perbarui posisi;
## END FOR
Pilih satu komodo dengan kualitas terbaik dari antara ketiga kelompok
sebagai solusi terbaik,k
best
## ;
Mulai iterasi ketiga, perbarui ukuran populasi;
## END WHILE
(Suyanto dkk., 2022)

## 118
## Lampiran 4.  Data Riwayat Harga Saham
## Sintaksis:
#Library
library(cluster)
library(ClusterR)
library(dplyr)
library(factoextra)
library(GA)
library(ggplot2)
library(openxlsx)
library(pso)
library(quadprog)
library(tidyr)
library(tidyverse)
#Impor data
dt=read.xlsx(’Data
LQ45.xlsx’)
dt=dt[, -1]
## View(dt)
## Luaran:
TanggalACESADROAKRA···UNTRUNVR
## 01-12-20237352,5601,435···22,1503,630
## 04-12-20237202,5601,405···22,4253,630
## 05-12-20237102,5101,405···22,0503,620
## 06-12-20237302,5301,400···21,6253,510
## 07-12-20236952,5301,335···21,7003,570
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 22-11-20247903,7501,305···27,0001,795
## 25-11-20247853,7701,265···27,6001,915
## 26-11-20247803,6701,230···27,5001,870

## 119
## 28-11-20247752,7601,225···27,3751,885
## 29-11-20247702,0801,230···26,7751,865
Luaran selengkapnya dapat diakses pada tautan bit.ly/DataTA473767 pada
sheet”Saham”.

## 120
Lampiran 5.  KomputasiReturnSaham
## Sintaksis:
#Returns
late_dt=rbind(dt, 0)
late_dt= late_dt[-1,]
## View(late_dt)
returns = (late_dt-dt)/dt
returns = returns[-nrow(returns),]
## View(returns)
## Luaran:
## ACESADROAKRA···TOWRUNTRUNVR
## -0.020410-0.02091···0.0265960.0124150
## -0.01389-0.019530···0.015544-0.01672-0.00275
## 0.0281690.007968-0.00356···-0.03061-0.01927-0.03039
## -0.047950-0.04643···-0.047370.0034680.017094
## 00.0118580.044944···00.02765-0.01681
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## .
## -0.01250.0190220···00.0121840.031609
## -0.006330.005333-0.03065···-0.020830.0222220.066852
## -0.00637-0.02653-0.02767···0-0.00362-0.0235
## -0.00641-0.24796-0.00407···0-0.004550.008021
## -0.00645-0.246380.004082···0-0.02192-0.01061
Luaran selengkapnya dapat diakses pada tautan bit.ly/DataTA473767 pada
sheet”Return”.

## 121
Lampiran 6.  Uji  Kolmogorov-Smirnov  terhadap  NormalitasReturnHarian
## Saham
## Sintaksis:
#Uji normalitas Kolmogorov-Smirnov
kstest =function(data){
ks.test(data, "pnorm",mean=mean(data),
sd=sd(data))$p.value
## }
normality =data.frame(sapply(returns, kstest))
names(normalitas)[1] = "p-value"
normalitas$Kesimpulan = with(normalitas,
ifelse(‘p-value‘ < 0.05,
’Tidak
normal’,
’Normal’))
normalitas =rownames_to_column(normalitas)
names(normalitas)[names(normalitas) == "rowname"] = "Saham"
## View(normalitas)
## Luaran:
Sahamp-valueKesimpulan
ACES0.01593687Tidak normal
ADRO6.0089E-07Tidak normal
AKRA0.02719894Tidak normal
AMMN0.05312296Normal
AMRT0.05907301Normal
ANTM0.17005662Normal
ARTO0.04517903Tidak normal
ASII0.20873054Normal
BBCA0.24127884Normal

## 122
BBNI0.165671Normal
BBRI0.60607667Normal
BBTN0.08754043Normal
BMRI0.06227151Normal
BRIS0.01929534Tidak normal
BRPT0.00011725Tidak normal
BUKA0.00026998Tidak normal
CPIN0.04420635Tidak normal
ESSA0.02028507Tidak normal
EXCL0.04231043Tidak normal
GGRM0.00029227Tidak normal
GOTO2.718E-05Tidak normal
HRUM0.08640976Normal
ICBP0.10030574Normal
INCO0.00871974Tidak normal
INDF0.09751483Normal
INKP0.17763771Normal
INTP0.00338442Tidak normal
ISAT7.3011E-12Tidak normal
ITMG0.19979133Normal
JSMR0.01195846Tidak normal
KLBF0.01481037Tidak normal
MAPI0.0076848Tidak normal
MBMA0.0805751Normal
MDKA0.03384926Tidak normal
MEDC0.04398079Tidak normal
MTEL2.4624E-05Tidak normal
PGAS0.06054331Normal
PGEO0.00013651Tidak normal
PTBA0.0164985Tidak normal

## 123
SIDO6.4403E-05Tidak normal
SMGR0.06393687Normal
TLKM0.06085432Normal
TOWR0.00018635Tidak normal
UNTR0.22113616Normal
UNVR0.03585209Tidak normal

## 124
Lampiran 7.  Vektor MeanReturn, Deviasi Standar, danSharpe Ratiodari Sa-
ham denganReturnHarian Berdistribusi Normal
## Sintaksis:
#Fungsi Sharpe ratio
sharpe_ratio =function(data){
(mean(data) - 0.06)/ sd(data)
## }
returns = returns[c(’AMMN’, ’AMRT’, ’ANTM’, ’ASII’,
## ’BBCA’, ’BBNI’, ’BBRI’, ’BBTN’,
## ’BMRI’, ’HRUM’, ’ICBP’, ’INDF’,
## ’INKP’, ’ITMG’, ’MBMA’, ’PGAS’,
## ’SMGR’, ’TLKM’, ’UNTR’)]
stock_stats = gather(returns,factor_key = TRUE)
stock_stats = stock_stats %>% group_by(key) %>%
summarise(Mean =mean(value),
‘Deviasi Standar‘ =sd(value),
‘Sharpe ratio‘ = sharpe_ratio(value))
stock_stats = stock_stats %>%remove_rownames%>%
column_to_rownames(var= ’key’)
## View(stock_stats)
## Luaran:
SahamMeanDeviasi StandarSharpe Ratio
## AMMN0.002186110.028520866-2.0270735
## AMRT6.9472E-050.016924599-3.5410308
## ANTM-0.00048310.022928533-2.6378966
## ASII-0.00036260.017044122-3.5415508
## BBCA0.0005610.013524238-4.3949978
## BBNI-5.582E-050.018308605-3.2801964

## 125
## BBRI-0.00080920.018213773-3.3386396
## BBTN0.000276710.021454528-2.7837148
## BMRI0.00035150.018730919-3.1844938
## HRUM-0.00066450.028252371-2.1472352
## ICBP0.000663820.016955066-3.4996137
## INDF0.000833130.01288752-4.5910205
## INKP-0.00045490.020392259-2.9645984
## ITMG0.000444230.013870487-4.2937041
## MBMA-0.00022130.034436253-1.748777
## PGAS0.001479210.019268461-3.0371286
## SMGR-0.00243280.020979092-2.9759521
## TLKM-0.00131230.017473873-3.5087969
## UNTR0.000937880.016400037-3.6013406

## 126
Lampiran 8.  Diagram  Pencar  MeanReturndan  Risiko  dari  Saham  dengan
ReturnHarian Berdistribusi Normal
## Sintaksis:
#Diagram pencar
plot(stock_stats$Mean, stock_stats$‘Deviasi Standar‘,
main = "Diagram
PencarMeanReturnvs.Deviasi
## Standar",
xlab = "MeanReturn",
ylab = "DeviasiStandar")
## Luaran:

## 127
Lampiran 9.  VisualisasiSilhouette Score
## Sintaksis:
#Silhouette score
set.seed(20429)
fviz_nbclust(stock_stats[. 1:2], kmeans,
method = ’silhouette’) +
ggtitle("Nilai
klasteroptimalberdasarkanSilhouette
## Score") +
theme(plot.title= element_text(hjust = 0.5)) +
xlab("k") +
ylab("Rata-rata
silhouettescore")
## Luaran:

## 128
Lampiran 10.  Analisis KlasterK-Means
## Sintaksis:
#Analisis Klaster K-Means
set.seed(20429)
km.final = kmeans(stock_stats[, 1:2], 2)
stock_stats$Klaster = km.final$cluster
mean(silhouette(km.final$cluster,
dist(stock_stats[, 1:2]))[,3])
fviz_cluster(km.final,data= stock_stats[, 1:2],
geom = ’text’, stand = FALSE) +
ggtitle(’Analisis
KlasterK-Means’) +
theme(plot.title= element_text(hjust = 0.5))
## Luaran:

## 129
Lampiran 11.  Pembobotan PortofolioMinimum Variance
## Sintaksis:
#### Pembobotan portofolio minimum variance ####
returns = returns[c(’AMMN’, ’ANTM’, ’BBTN’, ’MBMA’)]
#Vektor mean
mean_vector=list()
for(i in 1:4){
mean_vector[i] =mean(returns[, i])
## }
#Matriks kovariansi
cov_matrix=cov(returns)
#Invers matriks kovariansi
inv_cov_matrix=solve(cov_matrix)
#Pembilang
voo_4 =c(1, 1, 1, 1)
dim(voo_4) =c(4, 1)
pembilang = inv_cov_matrix%
## *
## %voo_4
#Penyebut
penyebut =t(voo_4) %
## *
## %inv_cov_matrix%
## *
## %voo_4
lambda = 1/penyebut
lambda
#Bobot
w_min=matrix(pembilang %
## *
## %(1/penyebut))
w_min
#Pemrograman kuadrat

## 130
qp.out =solve.QP(Dmat =cov_matrix, dvec =rep(0, 4),
## Amat =cbind(rep(1, 4),diag(4)),
bvec =c(1,rep(0, 4)), meq = 1)
qp.out
## Luaran:
> lambda
## [,1]
## [1,] 0.0001978939
> w_min
## [,1]
## [1,] 0.26729764
## [2,] 0.31334935
## [3,] 0.34468174
## [4,] 0.07467127
> qp.out
## $solution
## [1] 0.26729764 0.31334935 0.34468174 0.07467127
## $value
## [1] 9.894696e-05
## $unconstrained.solution
## [1] 0 0 0 0
## $iterations
## [1] 2 0
$Lagrangian
## [1] 0.0001978939 0.0000000000
## [3] 0.0000000000 0.0000000000

## 131
## [5] 0.0000000000
## $iact
## [1] 1

## 132
Lampiran 12.  AplikasiGenetic Algorithmuntuk Menyelesaikan Fungsi Sphe-
re
## Sintaksis:
#GA untuk Fungsi Sphere
sphere =function(x){
sum(xˆ2)
## }
GA = ga(type = "real-valued",
fitness =function(x) -sphere(x),
lower=rep(-100, 30),upper=rep(100, 30),
popSize = 100, pcrossover = 0.8,
pmutation = 0.05,
selection = "gareal_lrSelection",
maxiter = 1000,
elitism = 10, seed = 20429)
GA@solution
sphere(GA@solution)
## Luaran:
> GA@solution
x1        x2          x3          x4
## [1,] 0.1214132 0.1133256 -0.09313949 -0.02602403
x5         x6        x7        x8
## [1,] -0.07227723 0.01455089 0.0206798 0.1020251
x9         x10x11x12
## [1,] 0.09103018 -0.04956427 -0.1292126 -0.03447824
x13          x14         x15        x16
## [1,] -0.095729 -0.009619393 -0.05007007 0.03640013
x17       x18        x19        x20
## [1,] 0.2044053 0.1053586 -0.1115318 -0.1096968
x21        x22         x23         x24
## [1,] -0.1253595 -0.1557265 -0.08741097 -0.01377968

## 133
x25        x26        x27       x28
## [1,] -0.09794862 0.05134507 0.05969794 0.2596163
x29       x30
## [1,] 0.03662251 0.1013489
> sphere(GA@solution)
## [1] 0.3148834

## 134
Lampiran 13.  Pembobotan Portofolio MenggunakanGenetic Algorithm
## Sintaksis:
#### Pembobotan portofolio Genetic Algorithm ####
f0 =function(w){
## 0.5
## *
## (cov_matrix[1, 1]
## *
w[1]ˆ2 +
cov_matrix[2, 2]
## *
w[2]ˆ2 +
cov_matrix[3, 3]
## *
w[3]ˆ2 +
cov_matrix[4, 4]
## *
w[4]ˆ2) +
## (cov_matrix[1, 2]
## *
w[1]
## *
w[2] +
cov_matrix[1, 3]
## *
w[1]
## *
w[3] +
cov_matrix[1, 4]
## *
w[1]
## *
w[4] +
cov_matrix[2, 3]
## *
w[2]
## *
w[3] +
cov_matrix[2, 4]
## *
w[2]
## *
w[4] +
cov_matrix[3, 4]
## *
w[3]
## *
w[4])
## }
lambda = 1/penyebut
g =function(w){
f0 = 0.5
## *
## (cov_matrix[1, 1]
## *
w[1]ˆ2 +
cov_matrix[2, 2]
## *
w[2]ˆ2 +
cov_matrix[3, 3]
## *
w[3]ˆ2 +
cov_matrix[4, 4]
## *
w[4]ˆ2) +
## (cov_matrix[1, 2]
## *
w[1]
## *
w[2] +
cov_matrix[1, 3]
## *
w[1]
## *
w[3] +
cov_matrix[1, 4]
## *
w[1]
## *
w[4] +
cov_matrix[2, 3]
## *
w[2]
## *
w[3] +
cov_matrix[2, 4]
## *
w[2]
## *
w[4] +
cov_matrix[3, 4]
## *
w[3]
## *
w[4])
f1 = w[1] + w[2] + w[3] + w[4] - 1
f = f0 - lambda
## *
f1
return(f)

## 135
## }
GA = ga(type = "real-valued",
fitness =function(w) -g(w),
lower=c(0, 0, 0, 0),upper=c(1, 1, 1, 1),
popSize = 100, pcrossover = 0.8,
pmutation = 0.05,
selection = "gareal_lrSelection",
maxiter = 1000, elitism = 10,
names=c("w1", "w2", "w3", "w4"),
seed = 20429)
w_GA =matrix(GA@solution)
w_GA
f0(w_GA)
## Luaran:
> w_GA
## [,1]
## [1,] 0.26734397
## [2,] 0.31334285
## [3,] 0.34464106
## [4,] 0.07478484
> f0(w_GA)
## [1] 9.896927e-05

## 136
Lampiran 14.  FungsiKomodo Mlipir Algorithm
## Sintaksis:
#### Pembobotan portofolio Komodo Mlipir Algorithm ####
## Vektor kualitas
vektor_kualitas =function(K, func){
f =list()
for(n in 1:length(K)){
f[[n]] = func(K[[n]])
## }
return(f)
## }
## Vektor penggerak komodo jantan
gerak_jantan =function(K, f){
q=length(K)
## K_new=list()
for(i in 1:q){
sum_w = 0
for(j in 1:q){
if(j == i){
next
## }
set.seed(1000 + j + i)
r1 =qnorm(runif(1,min=pnorm(0),max=pnorm(1)))
if(f[[j]] < f[[i]]){
w_ij = r1
## *
(K[[j]] - K[[i]])

## 137
## }
else{
w_ij = r1
## *
(K[[i]] - K[[j]])
## }
sum_w = mapply("+",sum_w, w_ij)
## }
K_new[[i]] = mapply("+", K[[i]],sum_w)
## }
return(K_new)
## }
gerak_betina =function(iter, K, f, m, k_jantan_best, func){
## K1 =list()
## K2 =list()
## K_new=list()
alpha = 0.1
b = 0
a = 1
kual_K = vektor_kualitas(K, func)
#Bangkitkan satu bilangan random
set.seed(2000 + iter)
r =runif(1)
if(r >= 0.5){
#Berkawin
for(l in 1:m){
set.seed(3000 + l)
rl =qnorm(runif(1,min=pnorm(0),max=pnorm(1)))

## 138
K1[[l]] = rl
## *
k_jantan_best[[l]] +
(1 - rl)
## *
## K[[1]][[l]]
K2[[l]] = rl
## *
## K[[1]][[l]] +
(1 - rl)
## *
k_jantan_best[[l]]
## }
kual_K1 =unlist(vektor_kualitas(list(unlist(K1)),
func))
kual_K2 =unlist(vektor_kualitas(list(unlist(K2)),
func))
if(kual_K1 >= kual_K2){
if(kual_K1 >= kual_K){
K_new=unlist(K1)
## }
else{
K_new=unlist(K)
## }
## }
else{
if(kual_K2 >= kual_K){
K_new=unlist(K2)
## }
else{
K_new=unlist(K)
## }
## }
## }
else{
#Partenogenesis

## 139
set.seed(4000 + iter)
rl =rnorm(1)
for(l in 1:m){
## K1[[l]] = K[[1]][[l]] +
## (2
## *
rl - 1)
## *
alpha
## *
abs(a - b)
## }
kual_K1 =unlist(vektor_kualitas(list(unlist(K1)),
func))
if(kual_K1 >= kual_K){
K_new=unlist(K1)
## }
else{
K_new=unlist(K)
## }
## }
return(K_new)
## }
##Vektor penggerak komodo muda
gerak_muda =function(iter, K_muda, f_muda, K_jantan, m, d){
s =length(K_muda)
q=length(K_jantan)
## K_new=list()
for(i in 1:s){
sum_w = 0
for(j in 1:q){
w_ij =list()

## 140
for(l in 1:m){
#Bangkitkan bilangan random
set.seed(5000 + iter + i + j + l)
r2 =qnorm(runif(1,min=pnorm(0),max=pnorm(1)))
set.seed(6000 + iter + i + j + l)
r1 =qnorm(runif(1,min=pnorm(0),max=pnorm(1)))
set.seed(7000 + iter + i + j + l)
l_select =sample(c(1:m), size = 1)
if(l == l_select){
if(r2 < d){
w_ij[[l]] = r1
## *
(K_jantan[[j]][[l]] -
## K_muda[[i]][[l]])
## }
else{
w_ij[[l]] = 0
## }
## }
else{
w_ij[[l]] = 0
## }
## }
w_ij =unlist(w_ij)
sum_w = mapply("+",sum_w, w_ij)
## }
K_new[[i]] = mapply("+", K_muda[[i]],sum_w)
## }
return(K_new)

## 141
## }
##Selisih kualitas solusi optimum
df1 =function(f, iter){
diff=abs(f[[iter - 2]] - f[[iter - 1]])/
f[[iter - 2]]
return(diff)
## }
df2 =function(f, iter){
diff=abs(f[[iter - 1]] - f[[iter]])/
f[[iter - 1]]
return(diff)
## }
## ##KMA
KMA =function(N, m, func, p = 0.5, d = 0.5,
a = 5,max_iter = 100,
lower= 0,upper= 1, normalize = F){
## K =list()
for(n in 1:N){
set.seed(n)
## K[[n]] =runif(m)
## }
## K_best =list()
f_best =list()
iter = 1
while(iter <=max_iter){
##Mengurutkan
f = vektor_kualitas(K, func)
f =sort(unlist(f),index.return= T)

## 142
## K_sorted =list()
for(n in f$ix){
## K_sorted[[n]] = K[[f$ix[n]]]
## }
## K = K_sorted
#Definisi
q=floor((1 - p)
## *
## N)
s = N -q- 1
K_jantan = head(K,q)
f_jantan = head(f$x,q)
## K_betina = K[q+ 1]
f_betina = f$x[q+ 1]
K_muda = tail(K, s)
f_muda = tail(f$x, s)
##Gerakan komodo jantan
K_jantan_baru = gerak_jantan(K_jantan, f_jantan)
f_jantan_baru = vektor_kualitas(K_jantan_baru, func)
#Komodo jantan terbaik
f_jantan_baru_sorted =sort(unlist(f_jantan_baru),
index.return= T)
k_jantan_best = K_jantan_baru[[f_jantan_baru_sorted$ix[1]]]
##Gerakan komodo betina
K_betina_baru = gerak_betina(iter, K_betina, f_betina,
m, k_jantan_best, func)
f_betina_baru = vektor_kualitas(list(K_betina_baru),
func)
##Gerakan komodo muda

## 143
K_muda_baru = gerak_muda(iter, K_muda, f_muda, \
K_jantan_baru, m, d)
f_muda_baru = vektor_kualitas(K_muda_baru, func)
##Gabungan
K_baru =c(K_jantan_baru,list(K_betina_baru),
## K_muda_baru)
f_baru =c(f_jantan_baru, f_betina_baru, f_muda_baru)
for(n in 1:N){
if(normalize == T){
K_baru[[n]] = K_baru[[n]]/ sum(K_baru[[n]])
## }
K_baru[[n]] =pmin(pmax(K_baru[[n]],lower),upper)
if(normalize == T){
K_baru[[n]] = K_baru[[n]]/ sum(K_baru[[n]])
## }
## }
f_baru = vektor_kualitas(K_baru, func)
##Mengurutkan
f_baru =sort(unlist(f_baru),index.return= T)
## K_baru_sorted =list()
for(n in f_baru$ix){
## K_baru_sorted[[n]] = K_baru[[f_baru$ix[n]]]
## }
## K_baru = K_baru_sorted
f_baru = f_baru$x
K_best[[iter]] =list(K_baru[[1]])
f_best[[iter]] = f_baru[[1]]

## 144
cat("Iterasi:", iter, "\nKbest:\n",
## K_best[[iter]][[1]],
## "\nf_best:
", f_best[[iter]][[1]],
"\nPopulasi:", N, "\n==========\n")
if(iter >= 3){
df_1 = df1(f_best, iter)
df_2 = df2(f_best, iter)
if((df_1 > 0)&&(df_2 > 0)){
N = N - a
if(N <= 0){
break
## }
else{
K = head(K_baru, N)
f = head(f_baru, N)
## }
## }
else{
for(n in (N + 1):(N + a)){
set.seed(n)
## K_baru[[n]] =runif(m)
## }
N = N + a
## }
## }
## K = K_baru
iter = iter + 1
## }

## 145
cat("\nKomodoterbaik:\n", K_best[[iter]][[1]], "\n")
cat("Kualitas:", f_best[[iter]][[1]], "\n")
cat("Iterasi:
", iter)
#Grafik
data_plot=data.frame(c(1:length(unlist(f_best))),
unlist(f_best))
colnames(data_plot) =c(’Iterasi’, ’f_best’)
ggplot(data_plot, aes(x = Iterasi, y = f_best)) +
geom_line(color = ’black’, size = 1.5) +
geom_point(shape = 19 , color = ’chartreuse3’,
size = 2.5) +
ggtitle("Evolusi
nilaioptimumglobal") +
xlab(’Iterasi’) + ylab(’f_best’)
## }

## 146
Lampiran 15.  AplikasiKomodo Mlipir Algorithmuntuk Menyelesaikan Fungsi
## Sphere
## Sintaksis:
KMA(200, 30, func = sphere,
lower= -100,upper= 100)
## Luaran:
## Iterasi:  1
K best:
## 0.1075015 0.4877447 -0.8911181 -1.599486
## -0.1505463 0.3040065 -0.7689105 0.2373138
## -1.332546 -2.077841 0.5462063 -0.8351033
## 2.865099 0.6534056 0.4767018 -0.3828899
## -0.8728847 -0.8638896 -0.2833719 -0.3499226
## 0.3000031 1.263627 -1.105993 0.6055739
## -1.076051 -1.485405 0.2256191 1.666111
## 0.2943031 -0.7564637
f_best:  32.30061
## Populasi:  200
## ==========
## ...
## ==========
Komodo terbaik:
## -60.81865 -100 100 -100
## -100 62.10844 31.41833 37.04374
## 25.69892 31.41833 -72.91459 68.82071
## -77.09571 100 16.88959 -100
## -100 -31.41833 -54.7052 27.10437
## -41.81451 29.7871 23.12563 16.88959
## 4.340415 -100 -100 -56.00618
## 65.88495 16.88959
## Kualitas:  133796.9

## 147
## Iterasi:  42

## 148
Lampiran 16.  Pembobotan  Portofolio  MenggunakanKomodo Mlipir Algori-
thm
## Sintaksis:
KMA(200, 4, func = g, normalize = T)
## Luaran:
## Iterasi:  1
K best:
## 0.3021235 0.3478262 0.2838541 0.06619618
f_best:  0.0001004718
## Populasi:  200
## ==========
## Iterasi:  2
K best:
## 0.2481816 0.3312667 0.4205517 0
f_best:  0.0001026208
## Populasi:  200
## ==========
## ...
## ==========
Komodo terbaik:
## 0.3122141 0.2713546 0.4036373 0.01279399
## Kualitas:  0.0001031325
## Iterasi:  42

## 149
Lampiran 17.  Pembobotan Portofolio MenggunakanParticle Swarm Optimi-
zation
## Sintaksis:
psoptim(par=rep(NA, 4), fn = g,
lower=rep(0, 4),upper=rep(1, 4))
## Luaran:
## $par
## [1] 0.26729762 0.31334934 0.34468171 0.07467127
## $value
## [1] 9.894696e-05
## $counts
functioniteration  restarts
## 14000      1000         0
## $convergence
## [1] 2

## 150
## $message
[1] "Maximalnumberofiterationsreached"

## 151
Lampiran 18.  Data Riwayat Harga IHSG
## Sintaksis:
#Data IHSG
IHSG =read.xlsx(’Data
IHSG.xlsx’)
## IHSG = IHSG[, -1]
## Luaran:
TanggalHarga
## 01-12-20237.059,91
## 04-12-20237.093,60
## 05-12-20237.100,85
## 06-12-20237.087,40
## 07-12-20237.134,62
## .
## .
## .
## .
## .
## .
## 22-11-20247.195,56
## 25-11-20247.314,11
## 26-11-20247.245,89
## 28-11-20247.200,16
## 29-11-20247.114,27

## 152
Lampiran 19.  KomputasiReturnIHSG
## Sintaksis:
#Return IHSG
late_IHSG = IHSG[-1]
return_IHSG = (late_IHSG - IHSG)/IHSG
return_IHSG =return_IHSG[-length(return_IHSG)]
## Luaran:
## Harga
## 0,00477202
## 0,00102205
## -0,0018941
## 0,00666253
## 0,00350124
## .
## .
## .
## -0,00549
## 0,00765309
## 0,01647544
## -0,0093272
## -0,0063112

## 153
## Lampiran 20.  Komputasi Portofolio Saham Relatif Terhadap Portofolio Pasar
## Sintaksis:
#Beta saham terhadap pasar
BM =apply(returns, 2,function(saham){
cov(saham,return_IHSG)/ var(return_IHSG)
## })
BM =matrix(BM)
## BM
## Luaran:
## > BM
## [,1]
## [1,] 0.5538391
## [2,] 0.7996983
## [3,] 1.3914885
## [4,] 1.1772685

## 154
## Lampiran 21.  Komputasi Beta Portofolio
## Sintaksis:
w_KMA =matrix(c(0.3122141, 0.2713546, 0.4036373, 0.01279399))
w_PSO =matrix(c(0.26729762, 0.31334934, 0.34468171, 0.07467127))
#Beta portofolio
B_MV =t(w_min) %
## *
## %BM
## B_MV
B_GA =t(w_GA) %
## *
## %BM
## B_GA
B_KMA =t(w_KMA) %
## *
## %BM
## B_KMA
B_PSO =t(w_PSO) %
## *
## %BM
## B_PSO
## Luaran:
## > B_MV
## [,1]
## [1,] 0.9661536
## > B_GA
## [,1]
## [1,] 0.9662512
## > B_KMA
## [,1]
## [1,] 0.9666368
## > B_PSO
## [,1]

## 155
## [1,] 0.9661536

## 156
Lampiran 22.  KomputasiSharpe Ratio
## Sintaksis:
#Sharpe ratio
sharpe_ratio =function(w,mean_vec,cov_mat){
## Mean =t(w) %
## *
% unlist(mean_vec)
## Var =t(w) %
## *
% cov_mat%
## *
## %w
## Mean = Mean
## *
## 237
SD =sqrt(Var)
## *
sqrt(237)
r_f = 0.06
SR = (Mean - r_f)/SD
return(SR)
## }
sharpe_ratio(w_min,mean_vector,cov_matrix)
sharpe_ratio(w_GA,mean_vector,cov_matrix)
sharpe_ratio(w_KMA,mean_vector,cov_matrix)
sharpe_ratio(w_PSO,mean_vector,cov_matrix)
## Luaran:
> sharpe_ratio(w_min,mean_vector,cov_matrix)
## [,1]
## [1,] 0.2830541
> sharpe_ratio(w_GA,mean_vector,cov_matrix)
## [,1]
## [1,] 0.2830966
> sharpe_ratio(w_KMA,mean_vector,cov_matrix)
## [,1]
## [1,] 0.4364185
> sharpe_ratio(w_PSO,mean_vector,cov_matrix)
## [,1]
## [1,] 0.2830541

## 157
Lampiran 23.  KomputasiTreynor Ratio
## Sintaksis:
#Treynor ratio
treynor_ratio =function(w,mean_vec){
## Mean =t(w) %
## *
% unlist(mean_vec)
## Mean = Mean
## *
## 237
## Beta =t(w) %
## *
## %BM
r_f = 0.06
TR = (Mean - r_f)/Beta
return(TR)
## }
treynor_ratio(w_min,mean_vector)
treynor_ratio(w_GA,mean_vector)
treynor_ratio(w_KMA,mean_vector)
treynor_ratio(w_PSO,mean_vector)
## Luaran:
> treynor_ratio(w_min,mean_vector)
## [,1]
## [1,] 0.06344737
> treynor_ratio(w_GA,mean_vector)
## [,1]
## [1,] 0.06345765
> treynor_ratio(w_KMA,mean_vector)
## [,1]
## [1,] 0.0998221
> treynor_ratio(w_PSO,mean_vector)
## [,1]
## [1,] 0.06344737

## 158
Lampiran 24.  KomputasiJensen’s Alpha
## Sintaksis:
#Ekspektasi return pasar
mean_M =mean(return_IHSG)
mean_M
#Jensen’s alpha
jensen_alpha =function(w,mean_vec){
## Mean =t(w) %
## *
% unlist(mean_vec)
## Mean = Mean
## *
## 237
Mean_M =mean_M
## *
## 237
## Beta =t(w) %
## *
## %BM
r_f = 0.06
JA = Mean - (0.06 + Beta
## *
(mean_M - r_f))
return(JA)
## }
jensen_alpha(w_min,mean_vector)
jensen_alpha(w_GA,mean_vector)
jensen_alpha(w_KMA,mean_vector)
jensen_alpha(w_PSO,mean_vector)
## Luaran:
>mean_M
## [1] 6.353708e-05
> jensen_alpha(w_min,mean_vector)
## [,1]
## [1,] 0.1192077
> jensen_alpha(w_GA,mean_vector)
## [,1]

## 159
## [1,] 0.1192297
> jensen_alpha(w_KMA,mean_vector)
## [,1]
## [1,] 0.1544285
> jensen_alpha(w_PSO,mean_vector)
## [,1]
## [1,] 0.1192077