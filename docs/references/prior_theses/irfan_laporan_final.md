

## TUGAS AKHIR - SM234801
## OPTIMASI PORTOFOLIO UTANG NEGARA
## MULTIVALUTA MENGGUNAKAN ALGORITMA
## KOMODO MLIPIR
## R. IRFAN AULIYA FAUZAN
## NRP 5002221129
## Dosen Pembimbing
Prof. Dr. Dra. Mardlijah, MT
## NIP 19670114 199102 2 001
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
## Program Sarjana
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
## Surabaya

## 2025
## 2

## TUGAS AKHIR - SM234801
## OPTIMASI PORTOFOLIO UTANG NEGARA
## MULTIVALUTA MENGGUNAKAN ALGORITMA
## KOMODO MLIPIR
## R. IRFAN AULIYA FAUZAN
## NRP 5002221129
## Dosen Pembimbing
Prof. Dr. Dra. Mardlijah, MT
## NIP 19670114 199102 2 001
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
## Program Studi Sarjana
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
## Surabaya
## 2025



## FINAL PROJECT - SM234801
## OPTIMIZATION OF A MULTICURRENCY
## SOVEREIGN DEBT PORTFOLIO USING THE
## KOMODO MLIPIR ALGORITHM
## R. IRFAN AULIYA FAUZAN
## NRP 5002221129
## Supervisors
Prof. Dr. Dra. Mardlijah, MT
## NIP 19670114 199102 2 001
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
## Bachelor Program
Departement of Mathematics
Faculty of Scientics
## Institut Teknologi Sepuluh Nopember
## Surabaya
## 2025



## LEMBAR PENGESAHAN
## Optimasi Portofolio Utang Negara Multivaluta Menggunakan Algoritma
Komodo MLIPIR
## TUGAS AKHIR
Diajukan untuk memenuhi salah satu syarat
memperoleh gelar Sarjana Matematika pada
## Program Studi S-1 Matematika
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
Oleh:R. Irfan Auliya Fauzan
## NRP. 5002221129
## Surabaya, Desember 2025
Disetujui oleh Tim Penguji Tugas Akhir:
## Pembimbing
-  Prof.  Dr.  Dra.  Mardlijah, MT(. . . . . . . . . . . . . . . . . . )
## NIP. 19670114 199102 2 001
-  Sena Safarina, S.Si., M.Sc., D.Sc.(. . . . . . . . . . . . . . . . . . )
## NIP. 1990202012052
## Penguji
-  Dra.  Nur Asiyah, M.Si(. . . . . . . . . . . . . . . . . . )
## NIP. 19610822 198701 2 001
-  Drs.  Kamiran, M.Si(. . . . . . . . . . . . . . . . . . )
## NIP. 19630623 198903 1 001
-  Soleha, S.Si, M.Si(. . . . . . . . . . . . . . . . . . )
## NIP. 19830107 200604 2 001
## Mengetahui
## Kepala Departemen Matematika
Fakultas Sains dan Analitika Data
Dr.  Didik Khusnul Arif, S.Si, M.Si
## NIP. 19730930 199702 1 001
i



## PERNYATAAN ORISINALITAS
Yang bertanda tangan disini:
Nama Mahasiswa / NRP:    R. Irfan Auliya Fauzan / 5002221129
## Departemen:    Matematika
Dosen Pembimbing / NIP    :    1.   Prof.  Dr.  Dra.  Mardlijah, MT / 19670114 199102 2 001
-   Sena Safarina, S.Si., M.Sc., D.Sc. / 1990202012052
dengan  ini  menyatakan  bahwa  Tugas  Akhir  dengan  judul  “Optimasi  Portofolio  Utang
Negara  Multivaluta  Menggunakan  Algoritma  Komodo  MLIPIR”  adalah  hasil  karya
sendiri, bersifat orisinal, dan ditulis dengan mengikuti kaidah penulisan ilmiah.
Bilamana di kemudian hari ditemukan ketidaksesuaian dengan pernyataan ini, maka saya
bersedia  menerima  sanksi  sesuai  dengan  ketentuan  yang  berlaku  di  Institut  Teknologi
## Sepuluh Nopember.
## Surabaya, 22 Desember 2025
## Mengetahui
Dosen Pembimbing 1Dosen Pembimbing 2
Prof.  Dr.  Dra.  Mardlijah, MTSena Safarina, S.Si., M.Sc., D.Sc.
## NIP. 19670114 199102 2 001NIP. 1990202012052
## Mahasiswa
## R. Irfan Auliya Fauzan
## NRP. 5002221129
iii



## ABSTRAK
## Optimasi Portofolio Utang Negara Multivaluta Menggunakan Algoritma Komodo
## MLIPIR
Nama Mahasiswa / NRP    :    R. Irfan Auliya Fauzan / 5002221129
Departemen:    Matematika FSAD -ITS
Dosen Pembimbing:    1.   Prof.  Dr.  Dra.  Mardlijah, MT
-   Sena Safarina, S.Si., M.Sc., D.Sc.
## Abstrak
Pengelolaan utang negara dalam berbagai mata uang asing menimbulkan tantangan
berupa  keseimbangan  antara  biaya  pinjaman  dan  risiko  pasar,  khususnya  risiko  nilai
tukar   dan   risiko   suku   bunga   yang   dapat   meningkatkan   volatilitas   biaya   layanan
utang.Kondisi  tersebut  menuntut  adanya  strategi  kuantitatif  untuk  menentukan
komposisi portofolio utang multivaluta yang mampu meminimalkan risiko dengan tetap
mempertimbangkan  biaya  yang  diharapkan.Dalam  konteks  ini,  optimasi  portofolio
utang  negara  yang  terdiri  atas  Euro  (EUR),  Yen  Jepang  (JPY),  dan  Dolar  Amerika
Serikat (USD) dimodelkan menggunakan kerangkaMean-Variance Optimization(MVO).
Risiko portofolio direpresentasikan oleh variansi perubahancostyang dihitung dari data
historis  suku  bunga  dan  nilai  tukar,  sedangkan  keputusan  alokasi  dinyatakan  dalam
bentuk  bobot  masing-masing  instrumen  utang.   Model  dirumuskan  dalam  dua  bentuk,
yaitu  model  skalarisasicost-risiko  dan  model  minimumcostdengan  kendala  risiko,
serta  dilengkapi  kendala  anggaran  dan  batasan  bobot  instrumen.   Penyelesaian  model
dilakukan  melalui  dua  pendekatan,  yaitufminconsebagai  solusi  acuan  (benchmark)
dan   metode   metaheuristikKomodo   Mlipir   Algorithm(KMA)   sebagai   pendekatan
alternatif.Evaluasi  dilakukan  dengan  membandingkan  komposisi  bobot,  nilaicost,
risiko,  pemenuhan  kendala,  dan  efisiensi  komputasi.Hasil  penelitian  menunjukkan
bahwa  KMA  mampu  menghasilkan  solusi  portofolio  utang  negara  multivaluta  yang
mendekati solusi acuan pada seluruh skenario.  Pada skenario batasan umum, portofolio
cenderung  terkonsentrasi  pada  instrumen  USD  30Y,  sedangkan  pada  skenario  batasan
yang ditentukan, komposisi portofolio menjadi lebih tersebar sesuai batas minimum dan
maksimum bobot.  Meskipun demikian, metodefminconmemiliki waktu komputasi yang
lebih  rendah  dibandingkan  KMA.  Dengan  demikian,  KMA  dapat  digunakan  sebagai
metode alternatif dalam optimasi portofolio utang negara multivaluta, khususnya untuk
pengembangan model yang lebih kompleks.
Kata kunci:Optimasiportofolio,Utangnegaramultivaluta,Mean-Variance
## Optimization,fmincon, Komodo Mlipir Algorithm.
v



## ABSTRACT
Optimization of a Multicurrency Sovereign Debt Portfolio Using the Komodo MLIPIR
## Algorithm
Student Name / NRP    :    R. Irfan Auliya Fauzan / 5002221129
Departement:    Mathematics SCIENTICS - ITS
Advisor:    1.   Prof.  Dr.  Dra.  Mardlijah, MT
-   Sena Safarina, S.Si., M.Sc., D.Sc.
## Abstract
Managing   sovereign   debt   in   various   foreign   currencies   presents   challenges   in
balancing borrowing costs with market risks, particularly exchange rate and interest rate
risks,  which  can  increase  the  volatility  of  debt  service  costs.   This  situation  requires  a
quantitative  strategy  to  determine  the  composition  of  a  multicurrency  debt  portfolio
that  can  minimize  risk  while  still  considering  expected  cost  changes.   In  this  context,
the  optimization  of  a  sovereign  debt  portfolio  consisting  of  the  Euro  (EUR),  Japanese
Yen  (JPY),  and  United  States  Dollar  (USD)  is  modeled  using  the  Mean-Variance
Optimization  (MVO)  framework.   Portfolio  risk  is  represented  by  the  variance  of  cost
changes calculated from historical interest rate and exchange rate data, while allocation
decisions are expressed in terms of the weights of each debt instrument.  The model is
formulated  in  two  forms,  namely  a  cost-risk  scalarization  model  and  a  minimum-cost
model with a risk constraint, both with budget and instrument-weight constraints.  The
model  is  solved  using  two  approaches:fminconas  the  benchmark  solution  and  the
Komodo  Mlipir  Algorithm  (KMA)  metaheuristic  method  as  an  alternative  approach.
The evaluation is conducted by comparing portfolio weights, cost values, risk, constraint
satisfaction, and computational efficiency.  The results show that KMA is able to generate
multicurrency sovereign debt portfolio solutions that closely approximate the benchmark
solutions  in  all  scenarios.   Under  the  general  constraint  scenario,  the  optimal  portfolio
tends to be concentrated in the USD 30Y instrument.  In contrast,  under the specified
weight-constraint  scenario,   the  portfolio  composition  becomes  more  diversified  and
remains within the predetermined minimum and maximum weight limits.  Nevertheless,
thefminconmethod requires shorter computational time than KMA. Therefore,  KMA
can be considered a feasible alternative method for multicurrency sovereign debt portfolio
optimization, particularly for future developments involving more complex optimization
models.
Keywords:Portfolio   optimization,    Multicurrency   sovereign   debt,    Mean-Variance
## Optimization,fmincon, Komodo Mlipir Algorithm.
vii



## KATA PENGANTAR
Dengan  memanjatkan  puji  syukur  ke  hadirat  Allah  SWT  atas  rahmat,  taufik,  dan
hidayah-Nya sehingga penulis dapat menyelesaikan tugas akhir dengan judul:
## “OPTIMASI PORTOFOLIO UTANG NEGARA MULTIVALUTA MENGGUNAKAN
## ALGORITMA KOMODO MLIPIR”
sebagai   salah   satu   persyaratan   akademis   dalam   menyelesaikan   Program   Sarjana
Departemen Matematika, Fakultas Sains dan Analitika Data, Institut Teknologi Sepuluh
Nopember Surabaya. Penulis menyadari bahwa Tugas Akhir ini dapat diselesaikan dengan
baik berkat dukungan, bantuan, dan nasihat dari berbagai pihak.  Pada kesempatan ini,
penulis ingin mengucapkan terima kasih dan penghargaan kepada:
-  Ibu Prof.  Dr.  Dra.  Mardlijah, MT selaku dosen pembimbing pertama dan dosen
wali yang telah memberikan bimbingan, arahan, dan motivasi kepada penulis selama
pengerjaan Tugas Akhir ini.
-  Ibu Sena Safarina, S.Si., M.Sc., D.Sc.  selaku dosen pembimbing kedua yang telah
memberikan  masukan  dan  arahan  yang  sangat  bermanfaat  dalam  penyelesaian
Tugas Akhir ini.
-  Bapak Dr.  Didik Khusnul Arif, S.Si, M.Si selaku Kepala Departemen Matematika
Institut  Teknologi  Sepuluh  Nopember  yang  telah  memberikan  dukungan  selama
masa perkuliahan.
-  Bapak/Ibu dosen penguji yang telah memberikan kritik dan saran yang membangun
untuk perbaikan Laporan Tugas Akhir ini.
-  Bapak/Ibu  dosen  pengajar  yang  telah  memberikan  ilmu  dan  pengalaman  yang
bermanfaat,  serta  seluruh  karyawan,  Tendik,  dan  keluarga  besar  Departemen
Matematika Institut Teknologi Sepuluh Nopember atas dukungan dan bantuannya.
-  Keluarga tercinta yang senantiasa memberikan doa, dukungan moral, dan semangat
kepada penulis selama menempuh pendidikan.
-  Seluruh  teman-teman  dan  rekan-rekan  yang  telah  memberikan  dukungan  dan
semangat dalam penyelesaian Tugas Akhir ini.
Penulis menyadari bahwa Tugas Akhir ini masih jauh dari sempurna.  Oleh karena
itu, penulis mengharapkan saran dan kritik yang membangun dari pembaca.  Akhir kata,
semoga Tugas Akhir ini bermanfaat bagi semua pihak yang membacanya.
## Surabaya, Desember 2025
## R. Irfan Auliya Fauzan
ix



## DAFTAR ISI
LEMBAR PENGESAHANi
PERNYATAAN ORISINALITASiii
ABSTRAKv
ABSTRACTvii
KATA PENGANTARix
DAFTAR ISIxi
DAFTAR GAMBARxiii
DAFTAR TABELxv
DAFTAR SIMBOLxvii
## BAB IPENDAHULUAN1
1.1   Latar Belakang  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
1.2   Rumusan Masalah . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .2
1.3   Batasan Masalah . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
1.4   Tujuan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
1.5   Manfaat  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .4
## BAB IITINJAUAN PUSTAKA5
2.1   Penelitian Terdahulu  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
2.2   Optimasi Portofolio dan Teori Portofolio Modern . . . . . . . . . . . . . . . . . . . .6
2.2.1   PerubahanCost. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6
2.2.2   Risiko . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
2.3   Model Optimasi PortofolioMean-Variance. . . . . . . . . . . . . . . . . . . . . . . . . .8
2.4Quadratic ProgrammingsebagaiBenchmarkdalam Optimasi Portofolio8
2.5   Metaheuristik dalam Optimasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.6Komodo Mlipir Algorithm(KMA) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    10
2.6.1   MekanismeKomodo Mlipir Algorithm(KMA)  . . . . . . . . . . . . . . . . .    11
2.7   Kriterian Pemberhentian dalam iterasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
## BAB IIIMETODOLOGI17
3.1   Studi Literatur  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.2   Pengumpulan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.3   Pengolahan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.4   Pembentukan Model Optimasi Portofolio . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.5   Penyelesaian Model Optimasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.6   Analisis Hasil . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.7   Penarikan Kesimpulan dan Saran . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    20
xi

## BAB IVHASIL DAN PEMBAHASAN21
4.1   Deskripsi Data Penelitian  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
4.1.1   Data Suku Bunga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
4.1.2   Data Nilai Tukar Valuta Asing  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    22
4.1.3   Data Komposisi Utang  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
4.2   Pengolahan Data Penelitian  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    24
4.2.1   Penyesuaian Nilai Instrumen Berdasarkan Nilai Tukar  . . . . . . . . . .    24
4.2.2   Perhitungan PerubahanCostHistoris  . . . . . . . . . . . . . . . . . . . . . . . .    24
4.2.3   Perhitungan Matriks Kovarians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    25
4.3   Model Optimasi Portofolio  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    26
4.3.1   Model SkalarisasiCost-Risiko  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    26
4.3.2   Model MinimumCostdengan Kendala Risiko  . . . . . . . . . . . . . . . . .    28
4.4   Hasil dan Analisis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
4.4.1   Visualisasi Hasil Optimasi  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
4.4.2   Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Umum   31
4.4.3   Hasil   Model   SkalarisasiCost-Risiko   pada   Skenario   Batasan
Ditentukan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
4.4.4   Hasil Model MinimumCostpada Skenario Batasan Umum . . . . . .    33
4.4.5   Hasil Model MinimumCostpada Skenario Batasan Ditentukan . .    33
4.4.6   Konvergensi Iterasi KMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    34
4.4.7   Perbandingan Efisiensi Komputasi  . . . . . . . . . . . . . . . . . . . . . . . . . . .    36
4.4.8   Evaluasi Keseluruhan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    37
## BAB VKESIMPULAN DAN SARAN39
5.1   Kesimpulan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    39
5.2   Saran . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    39
## DAFTAR PUSTAKA41
## DAFTAR LAMPIRAN43
Lampiran 1   Repositori Kode ImplementasiKomodo Mlipir Algorithmpada
MATLAB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    43
Lampiran 2    Data Suku Bunga (Yield) Instrumen Utang . . . . . . . . . . . . . . . . .    44
Lampiran 3    Data Nilai Tukar Valuta Asing  . . . . . . . . . . . . . . . . . . . . . . . . . . . .    45
Lampiran 4   Hasil Perhitungan PerubahanCost, Rata-Rata PerubahanCost,
dan Matriks Kovarians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    46
## BIODATA PENULIS47
xii

## DAFTAR GAMBAR
Gambar 2.1   KonsepKomodo  Mlipir  Algorithm(KMA).  Sumber:   Suyanto,
Ariyanto, dkk.  (2022) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    11
Gambar 3.1   Diagram Alir Metodologi.  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
Gambar 4.1   Pergerakan Suku Bunga atauYieldUSD, JPY, dan EUR . . . . . . . .    22
Gambar 4.2   Pergerakan Nilai Tukar Valuta Asing . . . . . . . . . . . . . . . . . . . . . . . . . .    23
Gambar 4.3   Grafik   Risiko   danCostModel   SkalarisasiCost-Risiko   pada
Skenario Batasan Umum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    29
Gambar 4.4   Grafik   Risiko   danCostModel   SkalarisasiCost-Risiko   pada
Skenario Batasan Ditentukan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
Gambar 4.5   Grafik  Risiko  danCostModel  MinimumCostpada  Skenario
Batasan Umum  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    30
Gambar 4.6   Grafik  Risiko  danCostModel  MinimumCostpada  Skenario
Batasan Ditentukan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    31
Gambar 4.7   Perubahan  Nilai  Fungsi  Objektif  KMA  pada  Model  Skalarisasi
Cost-Risiko . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    35
Gambar 4.8   Perubahan NilaiCostKMA pada Model MinimumCost. . . . . . . . .    35
xiii



## DAFTAR TABEL
Tabel 4.1   Data Komposisi Utang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
Tabel 4.2   Bobot Optimal Model SkalarisasiCost-Risiko pada Skenario Batasan
Umum . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    31
Tabel 4.3   Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Umum . .    31
Tabel 4.4   Bobot Optimal Model SkalarisasiCost-Risiko pada Skenario Batasan
Ditentukan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
Tabel 4.5   Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Ditentukan  32
Tabel 4.6   Bobot Optimal Model MinimumCostpada Skenario Batasan Umum   33
Tabel 4.7   Hasil Model MinimumCostpada Skenario Batasan Umum  . . . . . . . .    33
Tabel 4.8   Bobot   Optimal   Model   MinimumCostpada   Skenario   Batasan
Ditentukan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    34
Tabel 4.9   Hasil Model MinimumCostpada Skenario Batasan Ditentukan . . . . .    34
Tabel 4.10  Nilai fungsi objektif terbaik KMA pada  Gambar 4.7b . . . . . . . . . . . . .    35
Tabel 4.11  Perbandingan Efisiensi Komputasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    36
xv



## DAFTAR SIMBOL
wVektor bobot portofolio
w
i
Bobot instrumen utang ke-idalam portofolio
## ∆c
i,t
Perubahancostlogaritmik instrumen ke-ipada periode
ke-t
## ̄
## ∆c
i
Rata-rata perubahancostinstrumen ke-i
## C
i,t
Nilaicostinstrumen  ke-isetelah  penyesuaian  pada
waktu ke-t
ΣMatriks kovarians perubahancostinstrumen
## Cov(∆c
i
## ,∆c
j
)    Kovarians perubahancostinstrumen ke-idan ke-j
σ
## 2
i
Variansi perubahancostinstrumen ke-i
σ
## 2
p
Variansi perubahancostportofolio
nJumlah instrumen dalam portofolio
TJumlah periode pengamatan
μVektorcostekspektasi instrumen
λParameter skalarisasicost-risiko
f(·)Fungsi objektif optimasi
k
i
Posisi solusi (individu) ke-idalam KMA
k
## ′
i
Posisi solusi hasil pembaruan
k
best
Solusi terbaik global
r
## 1
## ,r
## 2
,rBilangan acak pada interval [0,1]
qJumlah individubig males
dParametermlipir rate
n
## ′
Ukuran populasi setelah adaptasi
aParameter perubahan ukuran populasi
δf
## 1
## ,δf
## 2
Perubahan nilaifitnessantariterasi
x
## (k)
Vektor solusi pada iterasi ke-k
εToleransi konvergensi
kIndeks iterasi
k
max
Jumlah iterasi maksimum (maximum iteration)
xvii



## BAB I
## PENDAHULUAN
## 1.1    Latar Belakang
Pengelolaan utang negara (sovereign  debt  management) merupakan komponen vital
dalam  kebijakan  fiskal  suatu  negara.Tujuan  utama  dari  manajemen  utang  adalah
memastikan kebutuhan pembiayaan pemerintah terpenuhi dengan biaya minimal dalam
jangka panjang, sekaligus menjaga risiko tetap pada tingkat yang dapat ditoleransi (IMF,
2014).  Dalam era globalisasi keuangan, negara sering menerbitkan utang dalam berbagai
mata  uang  asing  untuk  mendiversifikasi  sumber  pendanaan  dan  memanfaatkan  suku
bunga internasional yang lebih rendah (Panzer dkk.  2015; Eichengreen dkk.  1999).
Keputusan  penerbitan  dan  komposisi  utang  dalam  berbagai  mata  uang  tersebut
secara alami menimbulkan permasalahan pemilihan kombinasi yang optimal, karena setiap
instrumen memiliki karakteristik biaya dan risiko yang berbeda, terutama risiko nilai tukar
dan risiko suku bunga.  Oleh karena itu,  diperlukan suatu pendekatan kuantitatif yang
mampu  mengevaluasi  hubungan  antara  biaya  pembiayaan  dan  risiko  secara  sistematis
dalam kerangka portofolio.
Optimasi  portofolio  merupakan  pendekatan  kuantitatif  untuk  menyusun  kombinasi
aset  ataupun  kewajiban  sehingga  tujuan  tertentu,  seperti  memaksimalkancostatau
meminimalkan biaya,  dapat dicapai pada tingkat risiko yang masih dapat diterima (H.
Markowitz, 1952).  Pendekatan ini didasarkan pada prinsip bahwa risiko dapat dikelola
dan dikurangi melalui diversifikasi, yaitu dengan mengombinasikan beberapa instrumen
sehingga pergerakan yang merugikan pada satu instrumen dapat diimbangi oleh instrumen
lain dalam portofolio (Elton dkk.  2009).
Dalam  pengelolaan  portofolio  utang  multivaluta,  penerapan  prinsip  diversifikasi
dihadapkan pada risiko pasar yang signifikan, terutama risiko nilai tukar (currency risk)
dan  risiko  suku  bunga  (interest  rate  risk).   Fluktuasi  nilai  tukar  mata  uang  domestik
terhadap EUR, JPY, dan USD dapat menyebabkan lonjakan biaya pembayaran bunga dan
pokok utang secara tak terduga, sehingga berpotensi membebani Anggaran Pendapatan
dan  Belanja  Negara  (APBN)  (IMF,  2014).    Risiko  nilai  tukar  muncul  karena  utang
berdenominasi valuta asing meningkatkan volatilitas biaya layanan utang ketika terjadi
depresiasi  mata  uang  domestik,  sementara  risiko  suku  bunga  timbul  akibat  perubahan
tingkat  suku  bunga  global  (Eichengreen  dkk.    1999).    Kondisi  ini  menuntut  adanya
strategi optimalisasi komposisi mata uang untuk memperoleh struktur portofolio utang
yang mampu mempertimbangkan hubungan antara biaya pinjaman (cost  of  borrowing)
dan risiko volatilitas pasar secara sistematis (Panzer dkk.  2015).
Dalam konteks tersebut, pendekatan kuantitatif berbasis optimasi portofolio menjadi
relevan  untuk  mendukung  pengambilan  keputusan  dalam  pengelolaan  utang  negara
multivaluta.  KerangkaMean-Variance Optimization(MVO) yang diperkenalkan oleh H.
Markowitz memungkinkan perumusan strategi alokasi portofolio dengan meminimalkan
## 1

risiko yang diukur melalui variansi, dengan tetap memperhatikan tingkat biaya ataucost
yang  diharapkan  (H.  Markowitz,  1952).   Pendekatan  ini  memberikan  dasar  matematis
yang  kuat  untuk  menganalisis  hubungan  antara  risiko  dan  biaya  dalam  pembentukan
portofolio  utang,  sehingga  komposisi  mata  uang  yang  optimal  dapat  ditentukan  secara
sistematis.
Model  MVO  dapat  dirumuskan  untuk  merepresentasikan  hubungan  antara  risiko
dancostportofolio.    Dalam  penelitian  ini,  model  disusun  dalam  dua  bentuk,  yaitu
model  skalarisasicost-risiko  dan  model  minimumcostdengan  kendala  risiko.   Kedua
bentuk  model  tersebut  melibatkan  kendala  anggaran  dan  batasan  bobot  instrumen
sehingga diperlukan metode optimasi berkendala yang mampu menangani fungsi objektif
halus  serta  kendala  linier  maupun  nonlinear.   Salah  satu  fungsi  yang  dapat  digunakan
adalahfminconpadaOptimization   Toolboxdi  perangkat  lunak  MATLAB.  Fungsi
fminconbanyak   digunakan   untuk   menyelesaikan   permasalahan   optimasi   nonlinear
berkendala  secara  numerik  dan  deterministik  (Nocedal  dkk.   2006).   Oleh  karena  itu,
hasil penyelesaian menggunakanfmincondigunakan sebagai acuan (benchmark) dalam
mengevaluasi kualitas solusi yang dihasilkan oleh metode optimasi lainnya.
Perkembangan   metode   optimasi   modern   mendorong   pemanfaatan   algoritma
metaheuristik   sebagai   pendekatan   alternatif   dalam   penyelesaian   masalah   optimasi
portofolio,   khususnya  ketika  permasalahan  melibatkan  ruang  solusi  yang  kompleks
atau  kendala  tambahan  yang  sulit  ditangani  secara  deterministik.   Berbagai  algoritma
metaheuristik   telah   banyak   diterapkan   dalam   optimasi   portofolio   danquadratic
programming, antara lainGenetic Algorithm(GA),Particle Swarm Optimization(PSO),
Simulated Annealing(SA), danAnt Colony Optimization(ACO), yang terbukti mampu
menjelajahi ruang solusi secara global (Talbi, 2009).
Meskipun demikian,  algoritma-algoritma metaheuristik tersebut memiliki beberapa
keterbatasan,   seperti   sensitivitas   terhadap   parameter,   kecenderungan   konvergensi
prematur,   serta   ketidakseimbangan   antara   proses   eksplorasi   dan   eksploitasi   pada
permasalahan   tertentu.Keterbatasan   ini   mendorong   pengembangan   algoritma
metaheuristik baru yang dirancang untuk meningkatkan efisiensi pencarian solusi serta
stabilitas kinerja pada berbagai karakteristik permasalahan optimasi.
Salah satu algoritma metaheuristik yang dikembangkan untuk menjawab tantangan
tersebut adalahKomodo Mlipir Algorithm(KMA), yang terinspirasi dari perilaku sosial
komodo dalam berburu dan berkompetisi.  KMA mengombinasikan mekanisme eksplorasi
dan eksploitasi melalui pembagian populasi solusi ke dalam beberapa kelompok dengan
peran  yang  berbeda,  sehingga  mampu  menjaga  keseimbangan  antara  pencarian  solusi
global dan penyempurnaan solusi lokal (Suyanto dkk.  2022).
Berdasarkan  uraian  tersebut,   penelitian  ini  menggunakan  model  MVO  sebagai
kerangka  matematis  dalam  optimasi  portofolio  utang  negara  multivaluta.Proses
penyelesaian model dilakukan menggunakanfminconsebagai solusi acuan (benchmark)
sertaKomodo   Mlipir   Algorithmsebagai   metode   optimasi   alternatif.Pendekatan
ini  diharapkan  mampu  memberikan  gambaran  mengenai  kemampuan  KMA  dalam
menghasilkan  solusi  portofolio  yang  mendekati  hasil  metode  pembanding,   sekaligus
memberikan kontribusi terhadap pengembangan metode optimasi berbasis metaheuristik
dalam pengelolaan risiko utang negara.
## 1.2    Rumusan Masalah
Berdasarkan latar belakang yang telah dibahas sebelumnya, didapat rumusan masalah
pada topik ini adalah sebagai berikut:
## 2

-  Bagaimana    memodelkan    permasalahan    optimasi    portofolio    utang    negara
multivaluta    (EUR,    JPY,    USD)    menggunakan    pendekatanMean-Variance
Optimization(MVO)  ke  dalam  model  skalarisasicost-risiko  dan  model  minimum
costdengan kendala risiko?
-  Bagaimana   mengimplementasikanKomodo   Mlipir   Algorithm(KMA)   untuk
menyelesaikan model optimasi portofolio utang negara multivaluta dengan kendala
anggaran dan batasan bobot?
-  Bagaimana perbandingan hasil optimasi portofolio utang negara multivaluta yang
diperoleh menggunakan KMA terhadap hasilfminconberdasarkan komposisi bobot,
nilaicost, risiko, pemenuhan kendala, dan efisiensi komputasi?
## 1.3    Batasan Masalah
Agar  penelitian  ini  dapat  difokuskan  dan  terarah,  maka  perlu  ditetapkan  batasan
masalah sebagai berikut:
-  Penelitian ini difokuskan pada optimasi portofolio utang negara dalam tiga mata
uang  asing,  yaitu  Euro  (EUR),  Yen  Jepang  (JPY),  dan  Dolar  Amerika  Serikat
(USD),  dengan  instrumen  USD
## 5Y,  USD10Y,  USD30Y,  EUR7Y,  EUR10Y,
JPY5Y, dan JPY10Y.
-  Data yang digunakan meliputi data historisyield, nilai tukar EUR terhadap USD
dan  JPY  terhadap  USD,  komposisi  portofolio  utang  eksisting  tahun  2024,  serta
batas minimum dan maksimum bobot setiap instrumen.  Periode pengamatan data
historis adalah 1 Oktober 2021 sampai dengan 24 November 2025.
-  Risiko portofolio dihitung berdasarkan matriks kovarians perubahancosthistoris,
sedangkancostekspektasi dihitung dari rata-rata perubahancosthistoris setelah
penyesuaian nilai instrumen ke dalam mata uang USD.
-  Penyelesaian model dibatasi pada dua pendekatan, yaitufminconsebagai metode
pembanding danKomodo Mlipir Algorithm(KMA) sebagai metode metaheuristik.
-  Faktor-faktor  eksternal  di  luar  model,  seperti  perubahan  kebijakan  fiskal,  kondisi
makroekonomi,  biaya  transaksi,  dan  risiko  likuiditas,  tidak  dimasukkan  secara
eksplisit.
## 1.4    Tujuan
Adapun tujuan dari penelitian ini adalah sebagai berikut:
-  Memodelkan  permasalahan  optimasi  portofolio  utang  negara  multivaluta  (EUR,
JPY,  USD)  menggunakan  pendekatanMean-Variance  Optimization(MVO)  ke
dalam model skalarisasicost-risiko dan model minimumcostdengan kendala risiko.
-  MengimplementasikanKomodo   Mlipir   Algorithm(KMA)  untuk  menyelesaikan
model optimasi portofolio utang negara multivaluta dengan kendala anggaran dan
batasan bobot.
-  Menganalisis   dan   membandingkan   hasil   optimasi   portofolio   utang   negara
multivaluta  menggunakan  KMA  terhadap  hasilfminconberdasarkan  komposisi
bobot, nilaicost, risiko, pemenuhan kendala, dan efisiensi komputasi.
## 3

## 1.5    Manfaat
Adapun manfaat yang diharapkan dari penelitian ini adalah sebagai berikut:
-  Memberikan  kontribusi  dalam  pengembangan  model  optimasi  portofolio  utang
negara multivaluta yang mempertimbangkan keseimbangan antaracostdan risiko.
-  Memberikan gambaran mengenai kelayakan KMA sebagai metode alternatif dalam
penyelesaian   optimasi   portofolio   utang   negara   dibandingkan   dengan   metode
optimasi numerik.
-  Menjadi referensi bagi peneliti selanjutnya yang tertarik pada optimasi portofolio,
manajemen utang negara, dan penerapan algoritma metaheuristik.
## 4

## BAB II
## TINJAUAN PUSTAKA
## 2.1    Penelitian Terdahulu
Dalam  pengerjaan  tugas  akhir  ini,  penelitian  terdahulu  yang  relevan  akan  dibahas
untuk memberikan dasar teoritis dan metodologis yang mendukung pengembangan model
optimasi  portofolio  utang  negara  multivaluta  menggunakan  pendekatan  metaheuristik.
Penelitian dasar yang menjadi fondasi utama dalam optimasi portofolio adalah penelitian
oleh H. Markowitz (1952) yang berjudul ”Portfolio Selection”.  Dalam penelitian tersebut
diperkenalkan  modelMean-Variance  Optimization(MVO)  sebagai  kerangka  matematis
dasar dalam penyusunan portofolio optimal.  Model ini memformulasikan permasalahan
optimasi dengan menggunakan variansi portofolio sebagai ukuran risiko dan biaya atau
rata-rata  perubahancostsebagai  komponen  yang  dikendalikan  dalam  kendala  model.
Pendekatan  MVO  ini  menjadi  landasan  bagi  pengembangan  berbagai  metode  optimasi
portofolio  selanjutnya,   termasuk  penerapannya  dalam  pengelolaan  portofolio  utang
negara multivaluta.
Sebagai  upaya  untuk  menyelesaikan  model  MVO  dengan  pendekatan  yang  lebih
fleksibel,  berbagai  algoritma  metaheuristik  mulai  diterapkan.Salah  satunya  adalah
metodeAnt  Colony  Optimization(ACO)  yang  dilakukan  oleh  Abolmaali  dkk.   (2018).
Peneliti  tersebut  menerapkanAnt  Colony  Optimization(ACO)  untuk  menyelesaikan
masalah  optimasi  portofolioMean-Variancedengan  kendala  jumlah  aset.   Model  yang
diusulkan menggunakan rasio Sharpe sebagai fungsi objektif dan membandingkanefficient
frontieryang dihasilkan ACO dengan model Markowitz sebagaibenchmark.  Hasil empiris
pada  data  Tehran  Stock  Exchange  menunjukkan  bahwa  ACO  mampu  menghasilkan
portofolio  yang  sangat  mendekatiefficient  frontierMarkowitz,  sekaligus  lebih  fleksibel
dalam  menangani  kendala  kardinalitas,  sehingga  membuktikan  efektivitas  pendekatan
metaheuristik dalam optimasi portofolio terbatas.  Meskipun menunjukkan kinerja yang
baik, penelitian ini masih memiliki beberapa keterbatasan, antara lain penggunaan rasio
Sharpe sebagai satu-satunya fungsi objektif, keterbatasan benchmark hanya pada model
Markowitz  tanpa  perbandingan  dengan  metaheuristik  lain,  serta  cakupan  data  yang
terbatas pada Tehran Stock Exchange.  Selain itu, model belum mempertimbangkan risiko
non-variansi dan risiko pasar lain seperti risiko nilai tukar, serta belum dilengkapi analisis
sensitivitas parameter algoritma secara mendalam.
Penelitian   selanjutnya   oleh   Uthayakumar   dkk.(2020)   menunjukkan   bahwa
pendekatanAnt  Colony  Optimization(ACO)  mampu  menghasilkan  kinerja  klasifikasi
yang  lebih  baik  dibandingkan  beberapa  algoritma  metaheuristik  lain,  sepertiGenetic
Algorithm(GA),Particle  Swarm  Optimization(PSO),  danGrey  Wolf  Optimization
(GWO). Namun demikian, pendekatan ACO yang digunakan dalam penelitian tersebut
masih memiliki keterbatasan.  Mekanisme pencarian solusi ACO yang sangat bergantung
pada  akumulasi  pheromone  berpotensi  menimbulkan  bias  eksploitasi  berlebih  terhadap
jalur  solusi  tertentu,  sehingga  meningkatkan  risiko  konvergensi  prematur.   Kondisi  ini
menyebabkan  ACO  belum  sepenuhnya  mampu  menjamin  diperolehnya  solusi  optimal
global,  khususnya  ketika  diterapkan  pada  ruang  solusi  yang  kompleks  dan  berdimensi
besar.  Selain itu, dibandingkan dengan PSO yang memiliki mekanisme eksplorasi global
## 5

berbasis kecepatan partikel atau GWO yang menjaga keberagaman solusi melalui struktur
hierarki kepemimpinan, ACO cenderung memerlukan pengaturan parameter yang lebih
sensitif dan berpotensi menimbulkan beban komputasi yang lebih tinggi.
Lebih lanjut,  penelitian terkait Komodo Mlipir Algorithm (KMA) yang dikaji oleh
Kusuma  dkk.(2022)  menunjukkan  bahwa  KMA  memiliki  kinerja  yang  kompetitif
dibandingkan  algoritma  metaheuristik  mapan  pada  permasalahan  optimasi  numerik
umum.  Namun, penerapan KMA pada permasalahan optimasi portofolio yang memiliki
karakteristik spesifik, seperti portofolio utang negara multivaluta yang melibatkan risiko
nilai  tukar  dan  risiko  suku  bunga  secara  simultan,  masih  belum  banyak  dikaji  dalam
literatur.
2.2    Optimasi Portofolio dan Teori Portofolio Modern
Optimasi   portofolio   merupakan   pendekatan   matematis   yang   digunakan   untuk
menentukan  komposisi  aset  yang  paling  optimal  dengan  mempertimbangkan  preferensi
pengambil  keputusan,  berbagai  kendala  yang  berlaku,  serta  ketidakpastian  terhadap
risiko  dan  hasil  di  masa  depan.Tujuan  utama  dari  optimasi  portofolio  adalah
memperoleh portofolio dengan kinerja terbaik berdasarkan kriteria tertentu,  khususnya
dalam menghadapitrade-offantaracostdan risiko (Salo dkk.  2024).
Landasan  teoritis  dari  optimasi  portofolio  berasal  dari  Teori  Portofolio  Modern
(Modern  Portfolio  Theory–MPT)  yang  diperkenalkan  oleh  H.  Markowitz  pada  tahun
-  Teori ini menekankan pentingnya diversifikasi aset sebagai strategi utama dalam
pengelolaan risiko, di mana penggabungan beberapa aset dengan karakteristikcostdan
risiko  yang  berbeda  dapat  menurunkan  risiko  portofolio  secara  keseluruhan.MPT
memperkenalkan konsep portofolio efisien, yaitu portofolio yang mampu memberikancost
maksimum pada tingkat risiko tertentu atau risiko minimum pada tingkatcosttertentu.
Hubungan optimal antaracostdan risiko tersebut direpresentasikan melalui kurva efisiensi
(efficient frontier), yang menggambarkan himpunan portofolio terbaik yang dapat dicapai
oleh investor rasional (Elton dkk.  2009).
2.2.1    PerubahanCost
Dalam penelitian ini, instrumen yang dianalisis bukan dipandang sebagai aset yang
memberikancost,  melainkan  sebagai  instrumen  utang  yang  menimbulkan  biaya.   Oleh
karena itu,  besaran yang digunakan adalah perubahan relatifcostdari satu periode ke
periode berikutnya.  Perubahancostinstrumen ke-ipada waktu ke-tdidefinisikan dalam
bentuk logaritmik sebagai berikut:
## ∆c
i,t
= ln
## 
## C
i,t
## C
i,t−1
## 
## (2.1)
dengan  ∆c
i,t
menyatakan  perubahancostlogaritmik  instrumen  ke-ipada  waktut,C
i,t
merupakan nilaicostinstrumen ke-isetelah penyesuaian nilai tukar dan suku bunga pada
waktut, sertaC
i,t−1
adalah nilaicostinstrumen ke-ipada waktut−1.
Setelah  perubahancosthistoris  dihitung  menggunakan  persamaan  (2.1),  rata-rata
perubahancostinstrumen ke-iselama periode pengamatan dihitung sebagai berikut:
## ̄
## ∆c
i
## =
## 1
## T
## T
## X
t=1
## ∆c
i,t
## (2.2)
## 6

dengan
## ̄
## ∆c
i
menyatakan  rata-rata  perubahancostinstrumen  ke-idanTmerupakan
jumlah periode pengamatan.
Nilai  rata-rata  perubahancosttersebut  digunakan  untuk  membentuk  vektorμ.
Dengan  demikian,μdalam  penelitian  ini  tidak  dimaknai  sebagai  rata-rata  perubahan
cost, tetapi sebagai vektorcostekspektasi atau rata-rata perubahancostmasing-masing
instrumen.
## 2.2.2    Risiko
Risiko portofolio diukur menggunakan variansi atau standar deviasi dari perubahan
costportofolio.   Variansi  yang  lebih  besar  menunjukkan  bahwa  perubahancostlebih
fluktuatif,  sehingga  tingkat  risiko  portofolio  menjadi  lebih  tinggi.   Variansi  perubahan
costinstrumen ke-idapat dihitung sebagai:
σ
## 2
i
## =
## 1
## T−1
## T
## X
t=1
##  
## ∆c
i,t
## −
## ̄
## ∆c
i
## 
## 2
## (2.3)
di  manaσ
## 2
i
menyatakan  variansi  perubahancostinstrumen  ke-i,   ∆c
i,t
merupakan
perubahancostinstrumen ke-ipada periode ke-t,
## ̄
## ∆c
i
adalah rata-rata perubahancost
instrumen ke-i, danTmenyatakan jumlah periode pengamatan.
Dalam  pengukuran  risiko  portofolio,  diperlukan  kovarians  antar  perubahancost
instrumen  untuk  memperhitungkan  hubungan  pergerakan  antar  instrumen.Secara
matematis, kovarians antara perubahancostinstrumen ke-idan ke-jdirumuskan sebagai
berikut:
## Cov(∆c
i
## ,∆c
j
## ) =
## 1
## T−1
## T
## X
t=1
##  
## ∆c
i,t
## −
## ̄
## ∆c
i
##  
## ∆c
j,t
## −
## ̄
## ∆c
j
## 
## (2.4)
Nilai  kovarians  digunakan  dalam  perhitungan  variansi  perubahancostportofolio
sebagai ukuran risiko keseluruhan dari kombinasi instrumen yang membentuk portofolio.
Secara matematis, variansi portofolio dirumuskan sebagai:
σ
## 2
p
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
## Cov(∆c
i
## ,∆c
j
## )(2.5)
atau dalam bentuk matriks:
σ
## 2
p
## =w
## ⊤
## Σw(2.6)
di mana:
w=
## 
## 
## 
## 
## 
w
## 1
w
## 2
## .
## .
## .
w
n
## 
## 
## 
## 
## 
## ,Σ=
## 
## 
## 
## 
## 
## Cov(∆c
## 1
## ,∆c
## 1
## )   Cov(∆c
## 1
## ,∆c
## 2
)···Cov(∆c
## 1
## ,∆c
n
## )
## Cov(∆c
## 2
## ,∆c
## 1
## )   Cov(∆c
## 2
## ,∆c
## 2
)···Cov(∆c
## 2
## ,∆c
n
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
## Cov(∆c
n
## ,∆c
## 1
## )   Cov(∆c
n
## ,∆c
## 2
)···Cov(∆c
n
## ,∆c
n
## )
## 
## 
## 
## 
## 
dengan Cov(∆c
i
## ,∆c
j
) menyatakan kovarians antara perubahancostinstrumen ke-idan
ke-j,σ
## 2
p
adalah variansi perubahancostportofolio,wmenyatakan vektor bobot portofolio,
Σmerupakan matriks kovarians perubahancostinstrumen, sertanmenyatakan jumlah
instrumen dalam portofolio.
Dengan  demikian,  risiko  portofolio  tidak  hanya  ditentukan  oleh  besarnya  variansi
perubahancostmasing-masing  instrumen  secara  individual,  tetapi  juga  oleh  kovarians
## 7

antar perubahancostyang mencerminkan hubungan pergerakan antar instrumen dalam
portofolio.  Pendekatan ini digunakan untuk menentukan kombinasi instrumen utang yang
mampu menekan biaya dengan tetap mempertimbangkan risiko perubahancost.
2.3    Model Optimasi PortofolioMean-Variance
Model    optimasi    portofolioMean-Variance    Optimization(MVO)    merupakan
pendekatan  klasik  dalam  teori  portofolio  modern  yang  diperkenalkan  oleh  H.   M.
Markowitz.   Dalam  penelitian  ini,  kerangka  MVO  diadaptasi  untuk  konteks  portofolio
utang.   Oleh  karena  itu,  komponenμ
## ⊤
wtidak  diperlakukan  sebagaicost,  melainkan
sebagaicostekspektasi portofolio atau rata-rata perubahancosttertimbang.
## Karenatujuanpenelitianadalahmeminimumkanbiayadengantetap
mempertimbangkan risiko, bentuk skalarisasi yang digunakan dinyatakan sebagai:
minf(w) =μ
## ⊤
w+
## 1
## 2
λw
## ⊤
## Σw(2.7)
dengan kendala:
n
## X
i=1
w
i
= 1,  w
i
≥0,  i= 1,2,...,n.
Pada persamaan tersebut,μmerupakan vektorcostekspektasi instrumen,Σmerupakan
matriks  kovarians  perubahancost,λmerupakan  parameter  pengendali  keseimbangan
antaracostdan risiko,wmerupakan vektor bobot portofolio, dannmerupakan jumlah
instrumen dalam portofolio.
Kendala dalam model MVO dirumuskan untuk menjamin kelayakan alokasi portofolio.
Total bobot instrumen dibatasi agar bernilai satu,
n
## X
i=1
w
i
## = 1,
yang memastikan seluruh proporsi portofolio dialokasikan secara penuh.  Selain itu, bobot
masing-masing instrumen dibatasi agar tidak bernilai negatif,
w
i
≥0,  i= 1,2,...,n.
Dengan   demikian,   model   MVO   dalam   penelitian   ini   digunakan   sebagai   kerangka
matematis  untuk  menentukan  komposisi  portofolio  utang  yang  mempertimbangkan
hubungan antaracostdan risiko perubahancost.
2.4Quadratic ProgrammingsebagaiBenchmarkdalam Optimasi Portofolio
Model optimasiMean-Variance(MVO) dapat dirumuskan sebagai masalahquadratic
programming(QP).  Hal  ini  disebabkan  oleh  struktur  matematis  model  MVO  yang
melibatkan fungsi kuadratik pada fungsi objektif, yaitu variansi perubahancostportofolio
yang  merupakan  fungsi  dari  bobot  instrumen  dan  matriks  kovarians  perubahancost,
sementara komponencostekspektasi dan kendala-kendala portofolio bersifat linier (Ho,
1992).  Kendala tersebut mencakup kendala anggaran yang mengharuskan jumlah bobot
instrumen bernilai satu, serta kendala non-negativitas bobot instrumen.
Struktur  ini  menjadikan  permasalahan  optimasi  portofolio  MVO  sebagai  masalah
optimasi  kuadratik  konveks  dengan  matriks  Hessian  yang  bersifat  definit  positif.   Sifat
konveks tersebut menjamin bahwa solusi optimal yang diperoleh merupakan solusi global,
## 8

sehingga metode QP sangat sesuai digunakan untuk menyelesaikan model MVO secara
deterministik dan stabil secara numerik (Ho, 1992).
Dalam  praktiknya,  penyelesaian  masalah  QP  pada  optimasi  portofolio  umumnya
dilakukan menggunakan algoritma deterministik yang telah teruji keandalannya.  Salah
satu  algoritma  QP  yang  paling  banyak  digunakan  dan  diakui  dalam  literatur  adalah
metode  dual  untukstrictly  convex  quadratic  programmingyang  dikembangkan  oleh
Goldfarb dan Idnani.  Algoritma ini dirancang khusus untuk menyelesaikan masalah QP
dengan matriks Hessian definit positif secara efisien, serta menunjukkan stabilitas numerik
yang tinggi dan performa komputasi yang unggul dibandingkan metode primal (Goldfarb
dkk.  1983).
Oleh   karena   itu,   dalam   banyak   penelitian   optimasi   portofolio,   metode   QP
berbasis  algoritma  Goldfarb-Idnani  digunakan  sebagai  solusi  acuan  (benchmark)  untuk
mengevaluasi  kinerja  pendekatan  optimasi  alternatif,  seperti  metode  heuristik  maupun
metaheuristik.  Solusi yang dihasilkan oleh metode ini merepresentasikan solusi optimal
global dari model MVO, sehingga dapat dijadikan dasar pembanding yang objektif dan
andal dalam analisis performa metode optimasi lainnya (Goldfarb dkk.  1983).
2.5    Metaheuristik dalam Optimasi
Metaheuristik  merupakan  pendekatan  optimasi  berbasis  pencarian  yang  dirancang
untuk  menyelesaikan  permasalahan  kompleks  dan  berdimensi  besar,  khususnya  ketika
fungsi  objektif  bersifat  non-linear,  non-konveks,  dan  multimodal.   Pada  permasalahan
semacam ini, struktur matematis sering kali tidak diketahui secara eksplisit, tidak dapat
dipisahkan,  serta  hanya  dapat  dievaluasi  melalui  simulasi  numerik.   Kondisi  tersebut
menyebabkan  metode  optimasi  deterministik  berbasis  gradien  menjadi  kurang  efektif
atau  bahkan  tidak  dapat  diterapkan.    Oleh  karena  itu,  metaheuristik  dikembangkan
sebagai metodederivative-freeyang memperlakukan fungsi objektif sebagai black box, di
mana kualitas solusi dinilai semata-mata berdasarkan nilai fungsi objektif hasil evaluasi
(M ́arov ́a, 2016).
Secara  konseptual,   metaheuristik  tidak  berdiri  sebagai  satu  algoritma  tunggal,
melainkan  mencakup  berbagai  keluarga  metode  optimasi  dengan  mekanisme  pencarian
yang berbeda-beda.  Berdasarkan sumber inspirasinya, metode metaheuristik umumnya
dapat diklasifikasikan ke dalam tiga kelompok utama,  yaitu kelompok berbasis evolusi,
berbasisswarm  intelligence,  dan  berbasis  optimisasi  lokal.   Kelompok  pertama  adalah
metaheuristik  berbasis  evolusi,  yang  meniru  prinsip  seleksi  alam  dan  genetika,  seperti
Genetic  Algorithm  (GA),  Differential  Evolution  (DE),  dan  Evolution  Strategies  (ES).
Metode-metode  ini  memanfaatkan  populasi  solusi  dan  operator  evolusioner  seperti
seleksi, crossover, dan mutasi untuk memperbaiki kualitas solusi secara bertahap (Nassef
dkk.    2024).Kelompok  kedua  adalah  metaheuristik  berbasisswarm  intelligence,  yang
terinspirasi  dari  perilaku  kolektif  makhluk  hidup  dalam  kelompok.   Contoh  algoritma
dalam  kelompok  ini  antara  lainParticle   Swarm   Optimization(PSO),Ant   Colony
Optimization(ACO),  danArtificial  Bee  Colony(ABC).  Algoritma-algoritma  tersebut
mengandalkan  interaksi  antarindividu  dalam  populasi  untuk  menyeimbangkan  proses
eksplorasi  dan  eksploitasi  ruang  solusi  melalui  mekanisme  berbagi  informasi  secara
implisit  maupun  eksplisit  (Nassef  dkk.   2024).   Selain  itu,  terdapat  pula  metaheuristik
berbasistrajectoryataulocal-search-based, yang bekerja dengan menelusuri lintasan solusi
tunggal secara iteratif, sepertiSimulated Annealing(SA),Tabu Search(TS), danVariable
Neighborhood  Search(VNS).  Meskipun  berangkat  dari  satu  solusi  awal,  metode  dalam
kelompok ini dilengkapi dengan mekanisme probabilistik atau memori untuk menghindari
## 9

konvergensi prematur pada solusi optimal lokal (Nassef dkk.  2024).
Di  antara  berbagai  kelompok  metaheuristik  tersebut,  pendekatan  berbasisswarm
intelligencemerupakan salah satu yang banyak dikaji dalam literatur optimasi modern
karena  kemampuannya  memanfaatkan  interaksi  antarindividu  untuk  menjelajahi  ruang
solusi secara global.  Salah satu algoritma metaheuristik terbaru yang termasuk dalam
pendekatan  ini  adalahKomodo  Mlipir  Algorithm(KMA),  yang  meniru  perilaku  sosial
komodo  dalam  lingkungan  alaminya.   Algoritma  ini  mengadopsi  pendekatan  berbasis
populasi  dengan  pembagian  peran  individu,   serta  mengintegrasikan  elemenswarm
intelligencedan algoritma evolusioner guna mendukung keseimbangan antara eksplorasi
dan eksploitasi ruang solusi (Kusuma dkk.  2022).
2.6Komodo Mlipir Algorithm(KMA)
Komodo   Mlipir   Algorithm(KMA)   merupakan   algoritma   metaheuristik   yang
terinspirasi  dari  perilaku  berburu  (foraging)  dan  reproduksi  komodo  di  alam  liar.
Algoritma  ini  mengadopsi  mekanisme  interaksi  antarindividu  yang  menyerupai  strategi
alami komodo dalam memperoleh dan mempertahankan sumber daya, sehingga mampu
menjelajahi  ruang  solusi  secara  efektif  tanpa  memerlukan  informasi  turunan  fungsi
objektif (Suyanto dkk.  2022).
KMA membagi populasi solusi ke dalam tiga kelompok utama berdasarkan peringkat
kualitas  (fitness  value),  yaitubig  males,female,  dansmall  males,  di  mana  setiap
kelompok memiliki peran yang berbeda dalam mengatur keseimbangan antara eksplorasi
dan  eksploitasi  ruang  solusi.Big  malesmerupakan  individu  dengan  kualitas  terbaik
yang berfokus pada eksploitasi wilayah solusi yang menjanjikan melalui pencarian lokal
intensif  di  sekitar  solusi  terbaik  saat  ini.Femalemerupakan  individu  dengan  kualitas
menengah  yang  berperan  sebagai  penyeimbang,  dengan  melakukan  eksploitasi  melalui
mekanisme reproduksi dengan individu terbaik atau eksplorasi melalui reproduksi aseksual
(parthenogenesis).    Sementara  itu,small  malesmerupakan  individu  dengan  kualitas
terendah  yang  berkontribusi  pada  eksplorasi  global  melalui  mekanisme  gerakanmlipir,
yaitu  mengikuti  solusi  terbaik  hanya  pada  sebagian  dimensi  tertentu  untuk  menjaga
keragaman  populasi  dan  menghindari  jebakan  pada  solusi  optimal  lokal  (Suyanto  dkk.
## 2022).
Untuk konsepKomodo Mlipir Algorithm(KMA), termasuk pembagian populasi dan
mekanisme pergerakan individu, dapat dilihat pada Gambar 2.1.
## 10

Gambar 2.1    KonsepKomodo Mlipir Algorithm(KMA).
Sumber:  Suyanto, Ariyanto, dkk.  (2022)
2.6.1    MekanismeKomodo Mlipir Algorithm(KMA)
Komodo  Mlipir  Algorithm(KMA) dijalankan melalui tiga mekanisme utama, yaitu
eksploitasi  solusi  olehbig  males,  eksplorasi  global  olehsmall  males,  serta  penyesuaian
ukuran populasi melalui mekanisme reproduksifemale.  Ketiga mekanisme tersebut saling
berinteraksi  untuk  menjaga  keseimbangan  antara  pencarian  intensif  di  sekitar  solusi
terbaik dan eksplorasi wilayah solusi yang lebih luas.  Uraian masing-masing mekanisme
beserta formulasi matematisnya disajikan sebagai berikut.
a.  PergerakanBig Males(Eksploitasi)
Kelompokbig malesmenerapkan strategihigh-exploitation low-exploration (HILE), di
mana proses pencarian difokuskan pada penyempurnaan solusi di sekitar individu dengan
kualitas terbaik.  Pendekatan ini bertujuan untuk mempercepat konvergensi menuju solusi
optimal dengan mempersempit ruang pencarian secara bertahap.
Pergerakan individu ke-imenuju posisi baruk
## ′
i
dirumuskan sebagai berikut:
w
ij
## =
## (
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
) ataur
## 2
## <0.5,
r
## 1
## (k
i
## −k
j
## ),lainnya.
## (2.8)
k
## ′
i
## =k
i
## +
q
## X
j=1,j̸=i
w
ij
## (2.9)
dengank
i
dank
j
masing-masing  menyatakan  posisi  individu  ke-idan  ke-j,f(k
i
)  dan
f(k
j
) adalah nilaifitnessindividu ke-idan ke-j,r
## 1
danr
## 2
merupakan bilangan acak pada
interval [0,1],qmenyatakan jumlahbig  males,  sertaw
ij
merupakan vektor pergerakan
individu ke-iterhadap individu ke-j.
## 11

b.  ReproduksiFemale(Eksploitasi dan Eksplorasi Seimbang)
Individufemaleberperan  sebagai  penyeimbang  antara  eksploitasi  dan  eksplorasi
melalui   dua   mekanisme,   yaitu   reproduksi   denganbig   maleterbaik   (mating)   dan
reproduksi  aseksual  (parthenogenesis).Mekanisme  ini  memungkinkan  pembentukan
variasi solusi baru tanpa menghilangkan fokus pada solusi yang menjanjikan.
Jikafemalemelakukan  reproduksi  denganbig  male,  maka  solusi  baru  dihasilkan
menggunakan persamaan:
k
## ′
il
## =r
l
k
il
## + (1−r
l
## )k
jl
## (2.10)
k
## ′
jl
## =r
l
k
jl
## + (1−r
l
## )k
il
## (2.11)
dengank
il
dank
jl
menyatakan komponen ke-ldari individu ke-idan ke-jyang bertindak
sebagaiwinner  big  maledan  individu  betina,  sertar
l
merupakan  bilangan  acak  pada
interval [0,1].
Sebaliknya,  jikafemalemelakukan  partenogenesis,  posisi  individu  baru  diperoleh
melalui:
k
## ′
ij
## =k
ij
## + (2r−1)α|ub
j
## −lb
j
## |(2.12)
denganα= 0.1 yang menyatakan radius mutasi sebesar 10% dari rentang ruang pencarian,
ub
j
danlb
j
merupakan batas atas dan batas bawah dimensi ke-j, sertaradalah bilangan
acak pada interval [0,1] (Suyanto dkk.  2022).
c.  PergerakanSmall Males(Eksplorasi)
Kelompoksmall malesmenerapkan strategilow-exploitation high-exploration (LIHE)
yang  bertujuan  untuk  menjelajahi  ruang  solusi  secara  lebih  luas.Mekanisme  ini
memungkinkan  algoritma  untuk  keluar  dari  jebakan  solusi  optimal  lokal  dengan  tetap
mempertahankan keterkaitan terhadap solusi terbaik yang telah ditemukan.
Formulasi pergerakansmall malesdinyatakan sebagai berikut:
w
ij
## =
## (
## P
q
j=1
r
## 1
## (k
jl
## −k
il
## ),jikar
## 2
< d,
## 0,sebaliknya.
## (2.13)
k
## ′
i
## =k
i
## +
q
## X
j=1,j̸=i
w
ij
## (2.14)
Parameterdmerupakanmlipir  rate,  yaitu  probabilitas  individu  mengikuti  dimensi
tertentu daribig  males.  Seluruh komponen pergerakan kemudian diakumulasikan untuk
menghasilkan posisi baruk
## ′
i
## .
d.  Adaptasi Populasi
Selain  mekanisme  eksploitasi  dan  eksplorasi,  KMA  juga  menerapkan  penyesuaian
ukuran populasi secara adaptif.  Apabila kualitas solusi meningkat selama dua generasi
berturut-turut, maka ukuran populasi akan dikurangi:
n
## ′
## =n−a(2.15)
sebaliknya, jika proses pencarian mengalami stagnasi, ukuran populasi akan ditambah:
n
## ′
## =n+a(2.16)
## 12

denganndann
## ′
masing-masing  menyatakan  ukuran  populasi  sebelum  dan  setelah
penyesuaian, sertaamerupakan jumlah individu yang ditambah atau dikurangi.
Penyesuaian  ukuran  populasi  dilakukan  berdasarkan  perbedaan  nilaifitness,  yang
dirumuskan sebagai berikut:
n
## ′
## =
## (
n−a,jikaδf
## 1
>0 danδf
## 2
## >0,
n+a,jikaδf
## 1
= 0 danδf
## 2
## = 0.
## (2.17)
dengan:
δf
## 1
## =
f
n−1
## −f
n
f
n−1
,  δf
## 2
## =
f
n−2
## −f
n−1
f
n−2
## (2.18)
di  manaδf
## 1
danδf
## 2
merupakan  perubahan  relatif  nilaifitnessterbaik  antar  iterasi
berturut-turut, danf
n
menyatakan nilaifitnesspada iterasi ke-n.
Melalui mekanisme adaptasi ini, KMA mampu menyesuaikan ukuran populasi secara
dinamis sehingga proses pencarian solusi dapat berlangsung secara lebih efisien dan stabil.
e.  Pseudocode Algoritma Komodo Mlipir
Berdasarkan konsep dan prosedur yang telah dijelaskan,Komodo  Mlipir  Algorithm
(KMA)  bekerja  secara  iteratif  dengan  memanfaatkan  interaksi  antarindividu  untuk
memperbarui populasi solusi hingga diperoleh individu dengan kualitas terbaik sebagai
solusi optimal globalk
best
## .
## 13

Algorithm 1Komodo Mlipir Algorithm
1:Hasil:k
best
sebagai solusi optimum global
2:Tetapkann,p, dandsebagai jumlah individu Komodo, proporsibig males, dan laju
mlipir
3:Inisialisasinindividu denganmdimensi
4:whilekriteria penghentian belum terpenuhido
## 5:forsetiap Komododo
6:Hitung nilai kualitas dan urutkan
7:end for
8:Berdasarkan peringkat dan proporsip, bagi populasi menjadi tiga kelompok:
9:qbig malesterbaik, satufemalekualitas menengah, danssmall maleskualitas
rendah
10:forsetiapbig maledo
11:Perbarui posisi menggunakan persamaan 2.9
12:Simpanqposisi terbaik untuk generasi berikutnya
13:end for
14:Perbarui posisifemaledengan:
## 15:ifkawinthen
16:gunakan persamaan 2.10 dan 2.11
## 17:else
18:gunakan persamaan 2.12
19:end if
20:forsetiapsmall maledo
21:Perbarui posisi menggunakan persamaan 2.14
22:end for
23:Perbarui ukuran populasinmenggunakan persamaan 2.17
24:Pilih individu dengan kualitas terbaik dari seluruh kelompok sebagaik
best
25:end while
Algoritma 1 merangkum secara sistematis tahapan iteratifKomodo Mlipir Algorithm
(KMA) dalam memperbarui populasi solusi hingga diperoleh solusi optimal globalk
best
yang memenuhi kriteria penghentian.
2.7    Kriterian Pemberhentian dalam iterasi
Pada penyelesaian permasalahan optimasi, khususnya yang diselesaikan menggunakan
algoritma iteratif, proses pencarian solusi dilakukan secara bertahap melalui pembaruan
solusi pada setiap iterasi.  Oleh karena itu, diperlukan suatu kriteria pemberhentian iterasi
(stopping criteria) untuk menentukan kapan proses iterasi dapat dihentikan secara tepat,
baik  ketika  solusi  telah  mencapai  kondisi  konvergen  maupun  untuk  menjaga  efisiensi
komputasi.
Secara   umum,   kriteria   pemberhentian   iterasi   dapat   didasarkan   pada   tingkat
perubahan  solusi  antar  iterasi  serta  pembatasan  jumlah  iterasi.    Dalam  konteks  ini,
digunakan kriteria gabungan yang mengombinasikan kriteria konvergensi solusi dan batas
maksimum iterasi.  Secara matematis, proses iterasi dihentikan apabila memenuhi kondisi
berikut:


x
## (k)
## −x
## (k−1)


## ≤ε∨k≥k
max
## (2.19)
denganx
## (k)
menyatakan vektor solusi pada iterasi ke-k,x
## (k−1)
menyatakan vektor solusi
## 14

pada iterasi sebelumnya,εmerupakan nilai toleransi konvergensi yang ditetapkan kecil,
kmenyatakan indeks iterasi, sertak
max
menyatakan jumlah iterasi maksimum.
Kriteria  konvergensi  solusi  pada  persamaan  2.19  digunakan  untuk  memastikan
bahwa  solusi  yang  diperoleh  telah  mencapai  tingkat  kestabilan  tertentu,  yang  ditandai
dengan  perubahan  solusi  antar  iterasi  yang  sangat  kecil.   Secara  teoretis,  kondisi  ini
berkaitan  dengan  sifat  konvergensi  barisan  solusi  iteratif,  di  mana  norma  selisih  antar
iterasi  cenderung  menuju  nol  seiring  bertambahnya  jumlah  iterasi  (Scherzer,  1995).
Kondisi tersebut mengindikasikan bahwa perbaikan solusi pada iterasi selanjutnya tidak
lagi  signifikan.Sementara  itu,  batas  maksimum  iterasi  digunakan  sebagai  kriteria
pemberhentian  apabila  proses  iterasi  belum  memenuhi  kriteria  konvergensi,   tetapi
jumlah  iterasi  telah  mencapai  nilai  maksimum  yang  ditetapkan.   Kriteria  ini  berfungsi
sebagai  mekanisme  pengaman  untuk  mencegah  proses  optimasi  berjalan  tanpa  batas
dan merupakan salah satu kriteria pemberhentian yang paling umum digunakan dalam
algoritma metaheuristik (Brezoˇcnik dkk.  2018).
Dengan mengombinasikan kedua kriteria tersebut, proses iterasi diharapkan mampu
menghasilkan  solusi  yang  stabil  dan  representatif,  sekaligus  mencapai  keseimbangan
antara kualitas solusi dan efisiensi komputasi. Pendekatan ini secara luas digunakan dalam
berbagai metode optimasi iteratif sebagai dasar penghentian proses pencarian solusi.
## 15



## BAB III
## METODOLOGI
Pada  bab  ini  dijelaskan  tahapan  penelitian  yang  dilakukan  dalam  penyusunan
Tugas Akhir.  Tahapan tersebut meliputi studi literatur, pengumpulan dan pengolahan
data, pembentukan model optimasi, penyelesaian model menggunakan metode optimasi
numerik danKomodo Mlipir Algorithm(KMA), analisis hasil, serta penarikan kesimpulan.
Alur penelitian secara umum ditunjukkan pada Gambar 3.1.
## Mulai
## Studi Literatur
## Pengumpulan Data
## Pengolahan Data
## Pembentukan Model
## Optimasi Portofolio Utang
## Penyelesaian Model
## Menggunakanfmincon
## Penyelesaian Model
Menggunakan KMA
## Analisis Hasil
## Penarikan Kesimpulan, Saran,
dan Penulisan Tugas Akhir
## Selesai
## Gambar 3.1    Diagram Alir Metodologi.
## 17

Berdasarkan Gambar 3.1, penelitian diawali dengan studi literatur untuk memperoleh
landasan  teori  mengenai  optimasi  portofolio,   pengelolaan  risiko  utang  multivaluta,
modelMean-Variance Optimization(MVO), metode optimasi numerik, dan KMA. Data
yang  diperoleh  kemudian  diolah  untuk  membentuk  vektorcostekspektasi  dan  matriks
kovarians.   Hasil  pengolahan  data  digunakan  sebagai  input  dalam  pembentukan  model
optimasi portofolio utang. Selanjutnya, model diselesaikan menggunakanfminconsebagai
metode pembanding dan KMA sebagai metode metaheuristik.  Hasil dari kedua metode
dianalisis berdasarkan komposisi bobot, nilaicost, risiko, pemenuhan kendala, serta waktu
komputasi.
## 3.1    Studi Literatur
Studi  literatur  dilakukan  untuk  membangun  landasan  teoritis  dan  metodologis
penelitian.Kajian  difokuskan  pada  teori  portofolio  modern,  modelMean-Variance
Optimization(MVO), pengukuran perubahancostdan risiko, serta penerapan optimasi
portofolio dalam pengelolaan utang negara multivaluta.  Selain itu,  dikaji pula metode
penyelesaian optimasi berkendala menggunakanfmincondan pendekatan metaheuristik,
khususnyaKomodo Mlipir Algorithm(KMA). Melalui studi literatur ini diperoleh dasar
untuk  merumuskan  model,  menentukan  fungsi  objektif  dan  kendala,  serta  menetapkan
kriteria pembandingan antara hasilfmincondan KMA.
## 3.2    Pengumpulan Data
Data  yang  digunakan  dalam  penelitian  ini  diperoleh  dari  Direktorat  Jenderal
Pengelolaan Pembiayaan dan Risiko (DJPPR). Data tersebut meliputi data historisyield
instrumen  utang  berdenominasi  USD,  EUR,  dan  JPY,  data  nilai  tukar  EUR  terhadap
USD dan JPY terhadap USD, serta data komposisi portofolio utang eksisting tahun 2024
beserta  batas  minimum  dan  maksimum  bobot  setiap  instrumen.   Periode  pengamatan
data historis adalah 1 Oktober 2021 sampai dengan 24 November 2025.
Instrumen yang digunakan terdiri atas tujuh instrumen,  yaitu USD
## 5Y, USD10Y,
## USD
30Y,  EUR7Y,  EUR10Y,  JPY5Y,  dan  JPY10Y.  Datayielddan  nilai  tukar
digunakan  untuk  menghitung  perubahancosthistoris,costekspektasi,  dan  matriks
kovarians.   Sementara  itu,  data  komposisi  utang  eksisting  dan  batas  bobot  digunakan
sebagai dasar dalam penentuan kendala model optimasi.
## 3.3    Pengolahan Data
Tahap pengolahan data dilakukan agar seluruh instrumen utang dapat dibandingkan
dalam  satu  satuan  mata  uang  yang  sama.   Instrumen  berdenominasi  EUR  dan  JPY
disesuaikan ke dalam mata uang USD menggunakan data nilai tukar, sedangkan instrumen
USD digunakan langsung sebagai mata uang dasar.  Setelah penyesuaian nilai dilakukan,
dihitung perubahancosthistoris setiap instrumen menggunakan pendekatan perubahan
costlogaritmik.
Dari perubahancosthistoris tersebut dihitung vektorcostekspektasiμsebagai rata-
rata perubahancosthistoris setiap instrumen.  Selanjutnya, dihitung matriks kovarians
Σuntuk merepresentasikan hubungan risiko antar instrumen.  Vektorμdan matriksΣ
kemudian digunakan sebagai input utama dalam pembentukan model optimasi portofolio
utang.
## 3.4    Pembentukan Model Optimasi Portofolio
Pada tahap ini disusun model optimasi portofolio utang negara multivaluta dengan
variabel keputusan berupa vektor bobot portofoliow= [w
## 1
## ,w
## 2
## ,...,w
n
## ]
## ⊤
.  Setiap bobot
## 18

menyatakan proporsi alokasi utang pada instrumen ke-i. Model dilengkapi dengan kendala
anggaran
n
## X
i=1
w
i
## = 1
agar total bobot portofolio bernilai satu.
Penelitian  ini  menggunakan  dua  bentuk  model.Model  pertama  adalah  model
skalarisasicost-risiko, yaitu
min
w
## 
## 1
## 2
λw
## ⊤
## Σw+μ
## ⊤
w
## 
## ,
denganλsebagai parameter pengendali skalarisasi antaracostdan risiko.  Model kedua
adalah model minimumcostdengan kendala risiko, yaitu
min
w
μ
## ⊤
w
dengan kendala
## √
w
## ⊤
## Σw≤σ.
Parameterσmenyatakan batas maksimum risiko portofolio yang diperbolehkan.
Pada kedua model tersebut digunakan dua skenario batasan bobot.  Skenario pertama
adalah  batasan  umum  0≤w
i
≤1,  sedangkan  skenario  kedua  adalah  batasan  yang
ditentukan berdasarkan batas minimum dan maksimum masing-masing instrumen, yaitu
lb
i
## ≤w
i
## ≤ub
i
.  Penggunaan dua skenario ini bertujuan untuk melihat pengaruh batasan
bobot terhadap komposisi portofolio, nilaicost, dan risiko yang dihasilkan.
## 3.5    Penyelesaian Model Optimasi
Penyelesaian model optimasi dilakukan menggunakan dua pendekatan, yaitufmincon
dan  KMA.  Metodefmincondigunakan  sebagai  metode  pembanding  karena  mampu
menyelesaikan  masalah  optimasi  berkendala  dengan  fungsi  objektif  halus  dan  kendala
linier maupun nonlinear.  Pada model skalarisasicost-risiko,fmincondigunakan untuk
menyelesaikan  fungsi  objektif  kuadratik  dengan  kendala  anggaran  dan  batasan  bobot.
Pada model minimumcost,fmincondigunakan untuk menyelesaikan fungsi objektif linier
dengan kendala risiko nonlinear.
Pendekatan   kedua   menggunakanKomodo   Mlipir   Algorithm(KMA).   Dalam
implementasinya, setiap individu dalam populasi KMA merepresentasikan kandidat solusi
berupa  vektor  bobot  portofolio.   Setiap  kandidat  solusi  dievaluasi  berdasarkan  fungsi
objektif model yang sedang diselesaikan.  Kandidat solusi juga diperiksa terhadap kendala
anggaran, batasan bobot, dan khusus untuk model minimumcost, kendala risiko.  Solusi
yang tidak memenuhi kendala diperbaiki melalui proses penyesuaian bobot atau dikenai
penalti agar tidak terpilih sebagai solusi terbaik.
Penyelesaian  dilakukan  pada  dua  model  dan  dua  skenario  batasan  bobot.   Dengan
demikian,  diperoleh  hasil  optimasi  untuk  model  skalarisasicost-risiko  pada  skenario
batasan umum dan batasan yang ditentukan, serta model minimumcostdengan kendala
risiko pada skenario batasan umum dan batasan yang ditentukan.
## 3.6    Analisis Hasil
Analisis hasil dilakukan dengan membandingkan solusi yang diperoleh darifmincon
dan KMA. Aspek yang dianalisis meliputi komposisi bobot portofolio,  nilaicost,  risiko
portofolio, nilai fungsi objektif, pemenuhan kendala, pola konvergensi KMA, dan waktu
## 19

komputasi.  Hasilfmincondigunakan sebagai acuan pembanding, sedangkan hasil KMA
dianalisis berdasarkan kedekatannya terhadap hasil tersebut.
Pada model skalarisasicost-risiko, evaluasi difokuskan pada perubahan nilaicostdan
risiko akibat variasi parameterλ.  Pada model minimumcost, evaluasi difokuskan pada
kemampuan  kedua  metode  menghasilkancostminimum  dengan  tetap  memenuhi  batas
risikoσ.   Selain  itu,  dianalisis  pula  pengaruh  penggunaan  batasan  umum  dan  batasan
yang ditentukan terhadap realisme komposisi portofolio yang dihasilkan.
3.7    Penarikan Kesimpulan dan Saran
Tahap akhir penelitian adalah penarikan kesimpulan berdasarkan hasil pembentukan
model,  penyelesaian  optimasi,  dan  analisis  perbandingan  antarafmincondan  KMA.
Kesimpulan diarahkan untuk menjawab rumusan masalah penelitian, khususnya mengenai
formulasi  model  optimasi  portofolio  utang  negara  multivaluta  serta  kemampuan  KMA
dalam  menghasilkan  solusi  yang  mendekati  metode  pembanding.    Selanjutnya,  saran
disusun  untuk  memberikan  arahan  pengembangan  penelitian,  baik  dari  sisi  perluasan
model, penambahan kendala, penggunaan metode metaheuristik lain, maupun pengujian
sensitivitas parameter KMA.
## 20

## BAB IV
## HASIL DAN PEMBAHASAN
Pada  bab  ini  akan  dibahas  hasil  implementasi  modelMean-Variance  Optimization
(MVO) dalam pembentukan portofolio utang negara multivaluta berdasarkan instrumen
utang  berdenominasi  USD,  JPY,  dan  EUR  dengan  mempertimbangkan  batasan  bobot
minimum dan maksimum pada setiap instrumen. Sebelum proses implementasi dilakukan,
terlebih dahulu dilakukan pengolahan data nilai tukar valuta asing dan suku bunga atau
yield, yang meliputi analisis pergerakan nilai tukar, pergerakan suku bunga, perhitungan
perubahan cost historis, rata-rata perubahan cost, serta pembentukan matriks kovarians.
Selanjutnya, model optimasi diselesaikan dengan dua pendekatan, yaitu metodequadratic
programmingmenggunakan  fungsifminconsebagai  solusi  acuan  dan  Komodo  Mlipir
Algorithm (KMA) sebagai metode metaheuristik.  Seluruh eksperimen dilakukan untuk
memperoleh  komposisi  portofolio  utang  negara  multivaluta  yang  optimal  dengan  biaya
minimum dan risiko yang tetap dipertimbangkan sesuai parameter yang ditentukan.
## 4.1    Deskripsi Data Penelitian
Data yang digunakan dalam penelitian ini merupakan data historis yang berkaitan
dengan portofolio utang negara multivaluta berdenominasi USD, JPY, dan EUR. Data
yang  digunakan  meliputi  data  suku  bunga  atauyield,  data  nilai  tukar  valuta  asing,
serta data komposisi utang eksisting yang diperoleh dari Direktorat Jenderal Pengelolaan
Pembiayaan dan Risiko(DJPPR). Data tersebut digunakan sebagai dasar dalam proses
perhitungan  perubahan  cost  historis,  rata-rata  perubahan  cost,  dan  matriks  kovarians
yang selanjutnya menjadi input pada modelMean-Variance Optimization(MVO).
Pembahasan  pada  bagian  ini  difokuskan  pada  karakteristik  awal  data,  khususnya
pergerakan nilai tukar valuta asing serta pergerakan suku bunga USD dan JPY selama
periode pengamatan.  Analisis awal terhadap data ini dilakukan untuk melihat adanya
pola kenaikan, penurunan, dan fluktuasi yang dapat memengaruhi biaya dan risiko dalam
pembentukan portofolio utang negara multivaluta.
## 4.1.1    Data Suku Bunga
Untuk  memberikan  gambaran  umum  terhadap  dinamika  pergerakan  suku  bunga,
berikut  ditampilkan  grafik  suku  bunga  atauyielddari  masing-masing  mata  uang  dan
tenor selama periode 1 Oktober 2021 hingga 24 November 2025.
## 21

Gambar 4.1    Pergerakan Suku Bunga atauYieldUSD, JPY, dan EUR
Berdasarkan  grafik  pergerakan  suku  bunga  atauyieldpada  Gambar  4.1,  dapat
dilihat  bahwayielddari  masing-masing  mata  uang  dan  tenor  yang  digunakan  dalam
penelitian ini bervariasi selama periode observasi.  Setiap instrumen menunjukkan pola
pergerakan yang berbeda-beda, dengan adanya kenaikan dan penurunanyieldpada waktu
tertentu.  Beberapa yield, khususnya pada instrumen berbasis USD dan EUR, cenderung
memiliki  tingkat  yang  lebih  tinggi  dan  mengalami  fluktuasi  yang  cukup  signifikan.
Sementara  itu,yieldJPY  berada  pada  tingkat  yang  relatif  lebih  rendah,  meskipun
tetap menunjukkan perubahan selama periode pengamatan.  Perbedaan pola pergerakan
tersebut  mencerminkan  adanya  dinamika  pasar  suku  bunga  yang  dapat  memengaruhi
biaya  dan  risiko  dalam  pembentukan  portofolio  utang.    Oleh  karena  itu,  visualisasi
ini  menjadi  penting  sebagai  gambaran  awal  sebelum  dilakukan  proses  optimasi  bobot
portofolio dengan mempertimbangkan biaya minimum dan risiko.
## 4.1.2    Data Nilai Tukar Valuta Asing
Data nilai tukar valuta asing digunakan dalam penelitian ini sebagai data pendukung
untuk  menyesuaikan  instrumen  utang  yang  memiliki  denominasi  mata  uang  berbeda
ke  dalam  satu  mata  uang  dasar.   Penyesuaian  ini  diperlukan  agar  seluruh  instrumen
dapat dibandingkan dan dihitung secara konsisten dalam proses pembentukan portofolio.
Data nilai tukar yang digunakan mencakup kurs valuta asing selama periode observasi 1
Oktober 2021 sampai dengan 24 November 2025.  Perubahan nilai tukar selama periode
tersebut  dapat  memengaruhi  nilai  instrumen  utang,  biaya  portofolio,  serta  risiko  yang
dipertimbangkan dalam proses optimasi.
Untuk memberikan gambaran umum mengenai pergerakan nilai tukar selama periode
observasi, data kurs JPY terhadap USD dan EUR terhadap USD disajikan dalam bentuk
grafik.  Visualisasi ini bertujuan untuk menunjukkan dinamika perubahan masing-masing
nilai tukar dari waktu ke waktu, sehingga dapat terlihat pola pergerakan, kecenderungan
naik atau turun, serta fluktuasi yang terjadi selama periode pengamatan.
Grafik  pergerakan  nilai  tukar  JPY  terhadap  USD  dan  EUR  terhadap  USD  selama
periode observasi ditunjukkan pada Gambar 4.2.
## 22

(a) Pergerakan Nilai Tukar EUR terhadap
## USD
(b) Pergerakan Nilai Tukar JPY terhadap
## USD
## Gambar 4.2    Pergerakan Nilai Tukar Valuta Asing
Berdasarkan    Gambar  4.2a  dan    Gambar  4.2b,  nilai  tukar  EUR  terhadap  USD
dan  JPY  terhadap  USD  menunjukkan  pergerakan  yang  berfluktuasi  selama  periode
observasi.  Kurs EUR terhadap USD cenderung mengalami kenaikan pada awal periode,
kemudian  menurun  dan  bergerak  tidak  stabil  hingga  akhir  periode.    Sementara  itu,
kurs  JPY  terhadap  USD  juga  menunjukkan  perubahan  yang  cukup  dinamis  dengan
kecenderungan meningkat pada beberapa periode tertentu.  Fluktuasi kedua kurs tersebut
perlu diperhatikan karena dapat memengaruhi nilai instrumen utang berdenominasi EUR
dan JPY dalam proses pembentukan portofolio.
## 4.1.3    Data Komposisi Utang
Data   komposisi   utang   digunakan   untuk   menunjukkan   proporsi   awal   masing-
masing   instrumen   utang   yang   dimiliki   pada   tahun   2024.Data   ini   terdiri   atas
jenis  instrumen,  mata  uang,  tenor,  komposisi  eksisting,  serta  batas  minimum  dan
maksimum yang diperbolehkan dalam proses pembentukan portofolio.  Nilai pada kolom
Existingmenunjukkan komposisi awal instrumen utang, sedangkan kolomMindanMax
menunjukkan  batas  bawah  dan  batas  atas  bobot  masing-masing  instrumen.   Batasan
tersebut  digunakan  agar  hasil  optimasi  portofolio  tetap  berada  dalam  rentang  alokasi
yang sesuai dengan ketentuan yang telah ditetapkan.
## Tabel 4.1    Data Komposisi Utang
Instrumen   Mata Uang   Tenor (years)   Existing (2024)MinMax
## USD5YUSD545.95%42.50%49.00%
## USD
## 10YUSD1011.36%10.00%12.50%
## USD30YUSD3014.78%13.00%16.50%
## EUR7YEUR814.39%13.00%15.50%
## EUR10YEUR102.44%1.50%3.00%
## JPY5YJPY56.67%5.00%8.50%
## JPY10YJPY104.41%3.00%5.50%
## Total100.00%88.00%   110.50%
Berdasarkan Tabel 4.1, instrumen dengan komposisi terbesar adalah USD 5Y dengan
bobot sebesar 45,95%, sedangkan instrumen dengan komposisi terkecil adalah EUR 10Y
dengan bobot sebesar 2,44%.  Secara keseluruhan, komposisi eksisting instrumen utang
berjumlah 100%, yang menunjukkan bahwa seluruh alokasi utang telah terbagi ke dalam
instrumen-instrumen  yang  digunakan  dalam  penelitian.   Adanya  batas  minimum  dan
## 23

maksimum  pada  setiap  instrumen  menjadi  kendala  dalam  proses  optimasi  agar  bobot
portofolio  yang  dihasilkan  tidak  menyimpang  terlalu  jauh  dari  komposisi  yang  telah
ditentukan.
## 4.2    Pengolahan Data Penelitian
Pada   bagian   ini   dilakukan   pengolahan   terhadap   data   yang   telah   dijelaskan
sebelumnya.   Tahap  awal  pengolahan  data  dilakukan  dengan  menyesuaikan  instrumen
utang berdenominasi EUR dan JPY ke dalam mata uang USD menggunakan data nilai
tukar.  Penyesuaian ini diperlukan karena perhitungan biaya dan risiko portofolio harus
dilakukan dalam satu satuan mata uang yang sama. Setelah seluruh instrumen dinyatakan
dalam mata uang USD, selanjutnya dilakukan perhitungan biaya dan risiko dari masing-
masing instrumen utang.  Hasil pengolahan data tersebut kemudian digunakan sebagai
input dalam penyelesaian model optimasi portofolio utang menggunakan metodefmincon
dan Komodo Mlipir Algorithm (KMA).
## 4.2.1    Penyesuaian Nilai Instrumen Berdasarkan Nilai Tukar
Tahap awal pengolahan data dilakukan dengan menyesuaikan nilai instrumen utang
berdasarkan nilai tukar dan tingkat suku bunga masing-masing instrumen.  Penyesuaian
ini  dilakukan  agar  instrumen  yang  memiliki  denominasi  mata  uang  berbeda  dapat
dinyatakan  dalam  satu  mata  uang  yang  sama.Dalam  penelitian  ini,  penyesuaian
dilakukan  untuk  satu  periode  pengamatan,  sehingga  nilai  instrumen  dapat  dinyatakan
sebagai:
## FV
i
## =FX
i
## (1 +IR
i
## )(4.1)
denganFV
i
merupakan  nilai  instrumen  ke-isetelah  penyesuaian,FX
i
merupakan
nilai  tukar  instrumen  ke-iterhadap  mata  uang  USD,  danIR
i
merupakan  tingkat
suku  bunga  atauyieldinstrumen  ke-i.Rumus  tersebut  menunjukkan  bahwa  nilai
instrumen disesuaikan berdasarkan nilai tukar dan tingkat suku bunga pada satu periode
pengamatan.  Untuk memperjelas proses penyesuaian nilai instrumen, berikut diberikan
contoh perhitungan pada salah satu instrumen utang, yaitu EUR
10Y pada tanggal 10
Oktober 2021.  Data yang digunakan dalam contoh perhitungan ini meliputi nilai tukar
EUR terhadap USD dan tingkat suku bunga instrumen pada periode pengamatan.
## FV
## EUR10Y
## = 0,8627(1 + 0,01477) = 0,8754(4.2)
Berdasarkan perhitungan 4.2, nilai instrumen EUR
10Y setelah penyesuaian nilai tukar
dan suku bunga adalah sebesar 0,8754.  Perhitungan yang sama dilakukan pada seluruh
instrumen utang yang digunakan dalam penelitian. Hasil penyesuaian nilai masing-masing
instrumen selanjutnya digunakan sebagai dasar dalam perhitungan biaya portofolio.
4.2.2    Perhitungan PerubahanCostHistoris
Setelah seluruh nilai instrumen disesuaikan berdasarkan nilai tukar dan suku bunga,
langkah  selanjutnya  adalah  menghitung  perubahancosthistoris  dari  masing-masing
instrumen utang.  Perubahancosthistoris dihitung menggunakan pendekatan perubahan
costlogaritmik sebagaimana didefinisikan pada persamaan (2.1).
Untuk memberikan gambaran mengenai proses perhitungan, berikut disajikan contoh
perhitungan  perubahancosthistoris  pada  instrumen  EUR
10Y  untuk  periode  ke-1.
Misalkan  nilai  instrumen  EUR10Y  pada  periode  0  adalah  0,8754  dan  pada  periode  1
## 24

adalah 0,8735, maka:
## ∆c
## EUR10Y,1
= ln
## 
## 0,8735
## 0,8754
## 
= ln(0,99783)≈−0,00217
Perhitungan   yang   sama   dilakukan   untuk   seluruh   instrumen   dan   seluruh   periode
pengamatan, sehingga diperoleh matriks perubahancosthistoris berukuranT×n, dengan
Tmenyatakan  jumlah  periode  pengamatan  dann=  7  menyatakan  jumlah  instrumen
utang.  Selanjutnya, rata-rata perubahancostmasing-masing instrumen dihitung sebagai
rata-rata dari perubahancosthistoris selama periode pengamatan sesuai persamaan (2.2).
Sebagai ilustrasi, berikut disajikan perhitungan rata-rata perubahancostuntuk salah
satu instrumen, yaitu EUR
10Y. Berdasarkan hasil perhitungan perubahancosthistoris,
diperoleh  jumlah  seluruh  perubahancosthistoris  instrumen  EUR10Y  selama  periode
pengamatan sebesar 0,03014, dengan jumlah data perubahancosthistoris sebanyakT=
-  Dengan mengacu pada persamaan (2.2), maka rata-rata perubahancostinstrumen
## EUR
10Y dihitung sebagai berikut:
## ̄
## ∆c
## EUR10Y
## =
## 1
## 1081
## ×0,03014≈0,0000279
Dengan demikian,  rata-rata perubahancostuntuk instrumen EUR10Y adalah sebesar
0,0000279.   Perhitungan  yang  sama  dilakukan  untuk  seluruh  instrumen  utang  lainnya
menggunakan  bantuan  MATLAB.  Hasil  perhitungan  tersebut  membentuk  vektor  rata-
rata perubahancostyang selanjutnya digunakan dalam proses optimasi portofolio utang.
## 4.2.3    Perhitungan Matriks Kovarians
Setelah  diperoleh  nilai  perubahancosthistoris  dan  rata-rata  perubahancost,
tahap selanjutnya adalah menghitung matriks kovarians antar instrumen.  Perhitungan
kovarians dilakukan menggunakan persamaan (2.4).
Sebagai  ilustrasi,  berikut  disajikan  contoh  perhitungan  kovarians  untuk  pasangan
instrumen EUR
10Y dan JPY10Y. Berdasarkan hasil pengolahan data, diperoleh jumlah
hasil perkalian deviasi perubahancostkedua instrumen sebagai berikut:
## 1081
## X
t=1
##  
## ∆c
## EUR
10Y,t
## −
## ̄
## ∆c
## EUR10Y
##  
## ∆c
JPY10Y,t
## −
## ̄
## ∆c
## JPY10Y
## 
## = 0,01711152.
Dengan  demikian,  kovarians  antara  instrumen  EUR10Y  dan  JPY10Y  diperoleh
sebagai berikut:
## Cov(∆c
## EUR10Y
## ,∆c
## JPY10Y
## ) =
## 0,01711152
## 1081−1
## = 0,000015844.
Perhitungan   yang   sama   dilakukan   untuk   seluruh   pasangan   instrumen   utang
menggunakan bantuan MATLAB. Hasil perhitungan tersebut kemudian disusun ke dalam
matriks kovarians berukuran 7×7.
Matriks  kovarians  yang  diperoleh  disusun  berdasarkan  urutan  instrumen  USD
## 5Y,
USD10Y, USD30Y, EUR7Y, EUR10Y, JPY5Y, dan JPY10Y, sebagaimana disajikan
berikut:
## 25

## Σ =
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 2,1402×10
## −7
## 2,2302×10
## −7
## 1,9793×10
## −7
## 2,9272×10
## −7
## 2,8311×10
## −7
## 3,2578×10
## −7
## 3,3198×10
## −7
## 2,2302×10
## −7
## 3,1884×10
## −7
## 2,6213×10
## −7
## 3,5617×10
## −7
## 3,4749×10
## −7
## 4,2978×10
## −7
## 4,4237×10
## −7
## 1,9793×10
## −7
## 2,6213×10
## −7
## 2,6869×10
## −7
## 3,4696×10
## −7
## 3,4120×10
## −7
## 4,0310×10
## −7
## 4,1515×10
## −7
## 2,9272×10
## −7
## 3,5617×10
## −7
## 3,4696×10
## −7
## 2,4936×10
## −5
## 2,4915×10
## −5
## 1,5888×10
## −5
## 1,5858×10
## −5
## 2,8311×10
## −7
## 3,4749×10
## −7
## 3,4120×10
## −7
## 2,4915×10
## −5
## 2,4931×10
## −5
## 1,5875×10
## −5
## 1,5844×10
## −5
## 3,2578×10
## −7
## 4,2978×10
## −7
## 4,0310×10
## −7
## 1,5888×10
## −5
## 1,5875×10
## −5
## 4,1692×10
## −5
## 4,1503×10
## −5
## 3,3198×10
## −7
## 4,4237×10
## −7
## 4,1515×10
## −7
## 1,5858×10
## −5
## 1,5844×10
## −5
## 4,1503×10
## −5
## 4,1444×10
## −5
## 
## 
## 
## 
## 
## 
## 
## 
## 
## 
Elemen diagonal pada matriks kovarians merepresentasikan variansi masing-masing
instrumen,   sedangkan   elemen   di   luar   diagonal   merepresentasikan   kovarians   antar
instrumen.  Nilai kovarians ini menunjukkan hubungan pergerakan perubahancostantar
instrumen dalam portofolio.
## 4.3    Model Optimasi Portofolio
Setelah model optimasi portofolio dibentuk, tahap selanjutnya adalah menyelesaikan
model tersebut untuk memperoleh bobot portofolio optimal.  Perhitungan dilakukan pada
masing-masing model dengan menggunakan metodequadratic programmingdanKomodo
Mlipir Algorithm(KMA).
Hasil  dari  proses  perhitungan  ini  digunakan  untuk  membandingkan  kinerja  kedua
metode penyelesaian serta melihat karakteristik portofolio yang dihasilkan, baik dari sisi
cost, risiko, komposisi bobot, maupun waktu komputasi.
4.3.1    Model SkalarisasiCost-Risiko
Model skalarisasicost-risiko digunakan untuk memperoleh komposisi bobot portofolio
dengan  mempertimbangkan  dua  komponen  utama,   yaitu  risiko  portofolio  dancost
ekspektasi.  Pada model ini, risiko dimasukkan secara langsung ke dalam fungsi objektif
melalui parameterλ, sehingga perubahan nilaiλakan memengaruhi keseimbangan antara
risiko dancostyang dihasilkan.
Model  skalarisasi  yang  digunakan  dapat  dituliskan  sebagai  permasalahanquadratic
programming,  karena  fungsi  objektifnya  berbentuk  kuadratik  terhadap  vektor  bobot
portofolio dan kendala yang digunakan berupa kendala linier serta batasan bobot.  Bentuk
umumquadratic programmingadalah sebagai berikut:
min
w
## 
## 1
## 2
w
## T
## Hw+c
## T
w
## 
dengan kendala
## A
eq
w=b
eq
## ,
w
min
i
## ≤w
i
## ≤w
max
i
,  i= 1,2,...,n.
Pada penelitian ini, fungsi objektif model skalarisasi dituliskan sebagai
min
w
## 
## 1
## 2
λw
## T
## Σw+μ
## T
w
## 
## .
Dengan   membandingkan   model   tersebut   terhadap   bentuk   umumquadratic
programming, diperoleh
## 26

H=λΣ,
c=μ,
## A
eq
## =1
## T
## ,
dan
b
eq
## = 1.
KendalaA
eq
w=b
eq
menunjukkan bahwa jumlah seluruh bobot portofolio harus sama
dengan satu. Adapun batasan bobot digunakan untuk mengatur rentang proporsi masing-
masing instrumen dalam portofolio.  Dalam penelitian ini, perhitungan model skalarisasi
cost-risiko dilakukan dengan dua skenario batasan bobot. Skenario pertama menggunakan
batasan umum, yaitu
## 0≤w
i
≤1,  i= 1,2,...,n.
Skenario  ini  digunakan  sebagai  pembanding  dasar  karena  hanya  membatasi  bobot
agar tidak bernilai negatif dan tidak melebihi satu.  Skenario kedua menggunakan batasan
bobot yang telah ditentukan, yaitu
lb
i
## ≤w
i
## ≤ub
i
,  i= 1,2,...,n.
Skenario kedua digunakan untuk merepresentasikan ketentuan proporsi minimum dan
maksimum pada masing-masing instrumen.  Dengan adanya dua skenario tersebut, dapat
dilihat pengaruh batasan bobot terhadap komposisi portofolio, nilaicost, dan risiko yang
dihasilkan.
a.  Penyelesaian menggunakanfmincon
Pada  pendekatan  pertama,  model  skalarisasicost-risiko  diselesaikan  menggunakan
fungsifminconpada  MATLAB.  Fungsi  ini  digunakan  untuk  menyelesaikan  masalah
optimasi   berkendala   dengan   fungsi   objektif   yang   halus,   termasuk   fungsi   objektif
kuadratik seperti pada model skalarisasi.  Dalam implementasinya,fmincondijalankan
menggunakan algoritmainterior-point.
Penyelesaian dilakukan untuk setiap nilai parameterλpada dua jenis batasan bobot,
yaitu  batasan  umum  dan  batasan  yang  ditentukan.Pada  setiap  nilaiλ,fmincon
menghasilkan  bobot  portofolio  optimal  yang  memenuhi  kendala  jumlah  bobot  sama
dengan  satu  serta  batasan  bobot  yang  digunakan.    Selanjutnya,  dari  bobot  optimal
tersebut dihitung nilaicostdan risiko portofolio.
Hasil penyelesaian menggunakanfminconkemudian digunakan sebagai pembanding
terhadap hasil yang diperoleh menggunakanKomodo Mlipir Algorithm(KMA).
b.  Penyelesaian menggunakanKomodo Mlipir Algorithm(KMA)
Pada  pendekatan  kedua,  model  skalarisasicost-risiko  diselesaikan  menggunakan
KMA. Dalam implementasinya, setiap individu dalam populasi KMA merepresentasikan
satu  kandidat  solusi  berupa  vektor  bobot  portofolio.   Setiap  kandidat  solusi  dievaluasi
berdasarkan fungsi objektif yang memuat komponen risiko dancost.
Penyelesaian menggunakan KMA dilakukan untuk setiap nilai parameterλpada dua
## 27

jenis batasan bobot, yaitu batasan umum dan batasan yang ditentukan.  Pada setiap nilai
λ,  KMA mencari bobot portofolio terbaik yang memenuhi kendala jumlah bobot sama
dengan satu serta batasan bobot yang digunakan.  Kandidat solusi dengan nilai fungsi
objektif terkecil dipilih sebagai solusi terbaik.
Hasil penyelesaian menggunakan KMA berupa bobot portofolio, nilai fungsi objektif,
nilaicost, dan risiko portofolio.  Hasil tersebut kemudian dibandingkan dengan hasil yang
diperoleh  menggunakanfminconuntuk  melihat  kesesuaian  solusi  yang  dihasilkan  oleh
metode metaheuristik terhadap metode optimasi numerik.
4.3.2    Model MinimumCostdengan Kendala Risiko
Model minimumcostdengan kendala risiko digunakan untuk memperoleh komposisi
bobot portofolio dengancostminimum, namun tetap memenuhi batas risiko yang telah
ditentukan.   Berbeda  dengan  model  skalarisasicost-risiko,  pada  model  ini  risiko  tidak
dimasukkan  secara  langsung  ke  dalam  fungsi  objektif,  melainkan  diberikan  sebagai
kendala.   Dengan  demikian,  model  ini  diarahkan  untuk  mencari  portofolio  dengancost
terendah pada tingkat risiko yang masih dapat diterima.
Model optimasi yang digunakan dituliskan sebagai berikut:
min
w
μ
## T
w
dengan kendala
## √
w
## T
## Σw≤σ,
n
## X
i=1
w
i
## = 1,
w
min
i
## ≤w
i
## ≤w
max
i
,  i= 1,2,...,n.
Parameterσmenyatakan  batas  maksimum  risiko  portofolio  yang  diperbolehkan.
Sama  seperti  model  sebelumnya,  penyelesaian  model  ini  dilakukan  menggunakan  dua
pendekatan, yaitufmincondanKomodo Mlipir Algorithm(KMA).
a.  Penyelesaian menggunakanfmincon
Pada pendekatan pertama, model minimumcostdengan kendala risiko diselesaikan
menggunakan fungsifminconpada MATLAB. Fungsi objektif yang diminimumkan adalah
nilaicostportofolio,  sedangkan  kendala  risiko  dimasukkan  sebagai  kendala  nonlinear.
Selain  itu,  model  juga  tetap  memperhatikan  kendala  jumlah  bobot  sama  dengan  satu
serta batasan bobot yang digunakan.
Penyelesaian menggunakanfmincondilakukan untuk memperoleh bobot portofolio
optimal  yang  menghasilkancostminimum  dan  tetap  memenuhi  batas  risikoσ.   Hasil
yang  diperoleh  kemudian  digunakan  sebagai  pembanding  terhadap  hasil  penyelesaian
menggunakan KMA.
b.  Penyelesaian menggunakanKomodo Mlipir Algorithm(KMA)
Pada  pendekatan  kedua,  model  minimumcostdengan  kendala  risiko  diselesaikan
menggunakan  KMA.  Dalam  implementasinya,  setiap  individu  dalam  populasi  KMA
merepresentasikan  kandidat  solusi  berupa  vektor  bobot  portofolio.Kandidat  solusi
dievaluasi berdasarkan nilaicostportofolio dan pemenuhan terhadap kendala risiko.
## 28

Apabila  kandidat  solusi  memenuhi  batas  risiko  yang  telah  ditentukan,  maka  solusi
tersebut dapat dipertimbangkan sebagai solusi layak.  Sebaliknya, apabila kandidat solusi
melanggar  batas  risiko,  maka  solusi  tersebut  tidak  dipilih  sebagai  solusi  terbaik  atau
diberikan  penalti  pada  nilai  fungsi  objektif.   Dengan  demikian,  KMA  diarahkan  untuk
mencari bobot portofolio dengancostminimum yang tetap memenuhi kendala risiko.
4.4    Hasil dan Analisis
Pada   bagian   ini   dibahas   hasil   penyelesaian   model   optimasi   portofolio   utang
menggunakan  dua  pendekatan,  yaitufmincondanKomodo  Mlipir  Algorithm(KMA).
Analisis dilakukan pada dua jenis model, yaitu model skalarisasicost-risiko serta model
minimumcostdengan  kendala  risiko.   Selain  itu,  pengujian  juga  dilakukan  pada  dua
skenario batasan, yaitu skenario batasan umum dan skenario batasan ditentukan.
Hasil  yang  diperoleh  darifmincondigunakan  sebagai  pembanding  karena  metode
ini  merupakan  salah  satu  metode  optimasi  numerik  yang  umum  digunakan  untuk
menyelesaikan masalah optimasi berkendala.  Sementara itu, hasil dari KMA digunakan
untuk   melihat   kemampuan   metode   metaheuristik   dalam   memperoleh   solusi   yang
mendekati solusi pembanding.
## 4.4.1    Visualisasi Hasil Optimasi
Untuk  memperjelas  hubungan  antara  risiko  dancostportofolio,   hasil  optimasi
divisualisasikan   dalam   bentuk   grafik   risiko-cost.Visualisasi   ini   digunakan   untuk
menunjukkan posisi solusi yang dihasilkan olehfmincondan KMA pada masing-masing
model  serta  skenario  batasan.Dalam  konteks  penelitian  ini,  portofolio  yang  lebih
efisien adalah portofolio yang mampu menghasilkancostlebih rendah pada tingkat risiko
tertentu,  atau  risiko  lebih  rendah  pada  tingkatcosttertentu.   Oleh  karena  itu,  grafik
risiko-costmenjadi alat bantu untuk melihat hubungan skalarisasi antara biaya pinjaman
dan risiko pasar dalam pembentukan portofolio utang negara multivaluta.
(a)fmincon(b) KMA
Gambar  4.3    Grafik  Risiko  danCostModel  SkalarisasiCost-Risiko  pada  Skenario
## Batasan Umum
## 29

(a)fmincon(b) KMA
Gambar  4.4    Grafik  Risiko  danCostModel  SkalarisasiCost-Risiko  pada  Skenario
## Batasan Ditentukan
Berdasarkan Gambar 4.3 dan Gambar 4.4, solusi yang dihasilkan olehfmincondan
KMA  menunjukkan  pola  risiko-costyang  searah.    Pada  model  skalarisasicost-risiko,
perubahan komposisi bobot portofolio dipengaruhi oleh parameter yang menyeimbangkan
komponen  risiko  dancost.Kedekatan  pola  grafik  KMA  terhadap  grafikfmincon
menunjukkan bahwa KMA mampu menghasilkan solusi yang mendekati metode acuan.
Pada  skenario  batasan  umum,  ruang  solusi  yang  lebih  longgar  membuat  portofolio
terkonsentrasi hampir seluruhnya pada instrumen USD
30Y. Sementara itu, pada skenario
batasan  yang  ditentukan,  batas  minimum  dan  maksimum  bobot  membuat  komposisi
portofolio lebih terkendali dan tetap berada dalam rentang alokasi yang telah ditentukan.
(a)fmincon(b) KMA
Gambar  4.5    Grafik  Risiko  danCostModel  MinimumCostpada  Skenario  Batasan
## Umum
## 30

(a)fmincon(b) KMA
Gambar  4.6    Grafik  Risiko  danCostModel  MinimumCostpada  Skenario  Batasan
## Ditentukan
Berdasarkan  Gambar  4.5  dan  Gambar  4.6,  model  minimumcostdengan  kendala
risiko menghasilkan solusi yang lebih terkendali karena risiko portofolio dibatasi secara
eksplisit.   Dengan  adanya  kendala  risiko,  penurunancosttidak  dapat  dilakukan  secara
bebas, melainkan harus tetap berada pada batas risiko yang telah ditentukan.  Pola grafik
KMA  yang  mendekati  hasilfminconmenunjukkan  bahwa  KMA  mampu  menemukan
kandidat solusi yang layak dan kompetitif,  baik pada skenario batasan umum maupun
skenario batasan yang ditentukan.
4.4.2    Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Umum
Pada skenario batasan umum, bobot setiap instrumen hanya dibatasi oleh 0≤w
i
## ≤1
dan jumlah seluruh bobot harus sama dengan satu.  Hasil penyelesaian model skalarisasi
cost-risiko pada skenario batasan umum disajikan pada Tabel 4.2.
Tabel 4.2    Bobot Optimal Model SkalarisasiCost-Risiko pada Skenario Batasan Umum
InstrumenfminconKMA
## USD5Y0,00012320438%0,0000%
## USD10Y0,00017149927%0,0000%
## USD30Y99,99952644337%100,0000%
## EUR
## 7Y0,00009064786%0,0000%
## EUR10Y0,00008310910%0,0000%
## JPY5Y0,00000256283%0,0000%
## JPY10Y0,00000253319%0,0000%
## Total100,0000%100,0000%
Tabel 4.3    Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Umum
MetodeCostRisikoNilai Objektif
fmincon1,64073×10
## −5
## 5,18353×10
## −4
## 1,77534×10
## −5
## KMA1,64072×10
## −5
## 5,18353×10
## −4
## 1,77533×10
## −5
Berdasarkan  Tabel  4.2,  solusi  optimal  pada  skenario  batasan  umum  terkonsentrasi
hampir  seluruhnya  pada  instrumen  USD
30Y.fminconmenghasilkan  bobot  USD30Y
## 31

sebesar 99,99952644337%, sedangkan KMA menghasilkan bobot sebesar 100,0000% pada
instrumen  yang  sama.   Kondisi  ini  terjadi  karena  pada  skenario  batasan  umum  model
hanya menggunakan kendala 0≤w
i
≤1, sehingga ruang solusi masih sangat longgar dan
memungkinkan seluruh bobot dialokasikan pada satu instrumen yang memberikan nilai
objektif terbaik.
Berdasarkan  Tabel  4.3,  nilaicostyang  diperolehfminconsebesar  1,64073×10
## −5
dengan risiko 5,18353×10
## −4
, sedangkan KMA menghasilkancost1,64072×10
## −5
dengan
risiko  yang  sama,  yaitu  5,18353×10
## −4
.Nilai  objektif  kedua  metode  juga  sangat
berdekatan, yaitu 1,77534×10
## −5
untukfmincondan 1,77533×10
## −5
untuk KMA. Hal
ini menunjukkan bahwa pada skenario batasan umum, KMA mampu menghasilkan solusi
yang sangat dekat dengan solusi acuan.
Hasil   ini   menunjukkan   bahwa   batasan   umum   belum   cukup   merepresentasikan
kebijakan  pembentukan  portofolio  utang  yang  realistis.    Tanpa  batas  minimum  dan
maksimum  yang  lebih  ketat,  model  cenderung  menghasilkan  portofolio  yang  sangat
terkonsentrasi.Dalam  konteks  pengelolaan  utang  negara,   kondisi  tersebut  kurang
diinginkan  karena  meningkatkan  eksposur  terhadap  satu  sumber  risiko  nilai  tukar  dan
suku bunga.
4.4.3    Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Ditentukan
Pada skenario batasan yang ditentukan, setiap instrumen memiliki batas bawah dan
batas atas bobot sesuai dengan data komposisi utang pada Tabel 4.1.  Hasil penyelesaian
model skalarisasicost-risiko pada skenario ini disajikan pada Tabel 4.4.
Tabel  4.4    Bobot  Optimal  Model  SkalarisasiCost-Risiko  pada  Skenario  Batasan
## Ditentukan
InstrumenfminconKMAMinMax
## USD5Y48,50015452250%    48,50002376089%    42,50%    49,00%
## USD
## 10Y12,49980794021%    12,49997695354%    10,00%    12,50%
## USD30Y16,49997560612%    16,49999927176%    13,00%    16,50%
## EUR
## 7Y13,00002765862%    13,00000000399%    13,00%    15,50%
## EUR10Y1,50003321570%1,50000000032%1,50%3,00%
## JPY5Y5,00000053145%5,00000000000%5,00%8,50%
## JPY
## 10Y3,00000052540%3,00000000944%3,00%5,50%
## Total100,0000%100,0000%
Tabel 4.5    Hasil Model SkalarisasiCost-Risiko pada Skenario Batasan Ditentukan
MetodeCostRisikoNilai Objektif
fmincon4,80554×10
## −5
## 1,18579×10
## −3
## 5,50890×10
## −5
## KMA4,80534×10
## −5
## 1,18579×10
## −3
## 7,90497×10
## −5
Berbeda dengan skenario batasan umum, hasil pada Tabel 4.4 menunjukkan bahwa
komposisi portofolio menjadi lebih tersebar karena setiap instrumen dibatasi oleh rentang
bobot minimum dan maksimum.  Pada hasilfmincon, instrumen USD5Y, USD10Y, dan
USD30Y berada sangat dekat dengan batas atas masing-masing, yaitu 48,50015452250%,
12,49980794021%, dan 16,49997560612%.  Sementara itu, instrumen EUR7Y, EUR10Y,
## JPY
5Y, dan JPY10Y berada sangat dekat dengan batas bawahnya.  Pola yang sama
## 32

juga terlihat pada hasil KMA, sehingga komposisi portofolio yang diperoleh KMA dapat
dikatakan mendekati hasilfmincon.
Berdasarkan  Tabel  4.5,  risiko  portofolio  pada  skenario  batasan  yang  ditentukan
adalah  1,18579×10
## −3
untuk  kedua  metode.    Nilaicostyang  dihasilkan  juga  sangat
berdekatan, yaitu 4,80554×10
## −5
padafmincondan 4,80534×10
## −5
pada KMA. Dengan
demikian, batasan bobot mampu menghasilkan komposisi portofolio yang lebih realistis
dibandingkan skenario batasan umum, sementara KMA tetap mampu mendekati solusi
acuan.
4.4.4    Hasil Model MinimumCostpada Skenario Batasan Umum
Pada model minimumcost, batas risiko tidak ditentukan secara tunggal, melainkan
diperoleh  melalui  beberapa  kandidat  nilai  batas  risiko  yang  dibentuk  menggunakan
fungsilinspace.  Setiap kandidat batas risiko digunakan dalam proses optimasi untuk
memperoleh  portofolio  dengancostminimum.   Solusi  yang  dipilih  sebagai  hasil  akhir
adalah  solusi  yang  memenuhi  kendala  portofolio,  mencapai  kondisi  konvergen,  dan
menghasilkan nilaicostterendah.
Tabel 4.6    Bobot Optimal Model MinimumCostpada Skenario Batasan Umum
InstrumenfminconKMA
## USD5Y0,00002848178%0,0000%
## USD10Y0,00002690188%0,0000%
## USD
## 30Y99,99992011979%100,0000%
## EUR7Y0,00001220334%0,0000%
## EUR
## 10Y0,00001148507%0,0000%
## JPY5Y0,00000040655%0,0000%
## JPY10Y0,00000040159%0,0000%
## Total100,0000%100,0000%
Tabel 4.7    Hasil Model MinimumCostpada Skenario Batasan Umum
MetodeCostRisiko
fmincon1,64072×10
## −5
## 5,18353×10
## −4
## KMA1,64072×10
## −5
## 5,18353×10
## −4
Berdasarkan   Tabel   4.6,   model   minimumcostpada   skenario   batasan   umum
juga  menghasilkan  portofolio  yang  terkonsentrasi  hampir  seluruhnya  pada  instrumen
USD30Y. Bobot USD30Y yang diperolehfminconadalah 99,99992011979%, sedangkan
KMA  menghasilkan  bobot  100,0000%.Hal  ini  menunjukkan  bahwa  ketika  hanya
digunakan batasan umum, model minimumcosttetap cenderung memilih satu instrumen
yang memberikan nilaicostpaling rendah dalam ruang solusi yang tersedia.
Berdasarkan Tabel 4.7, kedua metode menghasilkan nilaicostsebesar 1,64072×10
## −5
dan risiko sebesar 5,18353×10
## −4
.  Kesamaan nilai tersebut menunjukkan bahwa KMA
mampu  mencapai  solusi  yang  sama  denganfminconpada  model  minimumcostuntuk
skenario batasan umum.
4.4.5    Hasil Model MinimumCostpada Skenario Batasan Ditentukan
Hasil  penyelesaian  model  minimumcostpada  skenario  batasan  yang  ditentukan
disajikan  pada  Tabel  4.8.   Batas  risiko  yang  digunakan  dipilih  dari  beberapa  kandidat
## 33

nilai risiko yang diuji sebelumnya.  Pemilihan batas risiko tersebut didasarkan pada solusi
yang memenuhi kendala portofolio, mencapai kondisi konvergen, dan menghasilkan nilai
costyang rendah.
Tabel 4.8    Bobot Optimal Model MinimumCostpada Skenario Batasan Ditentukan
InstrumenfminconKMAMinMax
## USD5Y48,50439744760%    48,60351190162%    42,50%    49,00%
## USD10Y12,49594368506%    12,39649464684%    10,00%    12,50%
## USD
## 30Y16,49958987877%    16,49999310603%    13,00%    16,50%
## EUR7Y13,00002729733%    13,00000026372%    13,00%    15,50%
## EUR10Y1,50002716699%1,50000008086%1,50%3,00%
## JPY
## 5Y5,00000729049%5,00000000000%5,00%8,50%
## JPY10Y3,00000723376%3,00000000093%3,00%5,50%
## Total100,0000%100,0000%
Tabel 4.9    Hasil Model MinimumCostpada Skenario Batasan Ditentukan
MetodeCostRisiko
fmincon4,80535×10
## −5
## 1,18579×10
## −3
## KMA4,80553×10
## −5
## 1,18575×10
## −3
Berdasarkan Tabel 4.8, model minimumcostpada skenario batasan yang ditentukan
menghasilkan  komposisi  portofolio  yang  berada  dalam  rentang  batas  minimum  dan
maksimum  setiap  instrumen.Pada  hasilfmincon,  bobot  USD5Y,  USD10Y,  dan
## USD
30Y  berada  sangat  dekat  dengan  batas  atas,   sedangkan  EUR7Y,  EUR10Y,
JPY5Y, dan JPY10Y berada sangat dekat dengan batas bawah.  KMA menghasilkan
pola  yang  serupa,  meskipun  terdapat  perbedaan  kecil  pada  USD5Y  dan  USD10Y.
Perbedaan tersebut masih tetap memenuhi batasan bobot yang telah ditentukan.
Berdasarkan  Tabel  4.9,  nilaicostfminconadalah  4,80535×10
## −5
dengan  risiko
## 1,18579×10
## −3
,   sedangkan  KMA  menghasilkancost4,80553×10
## −5
dengan  risiko
## 1,18575×10
## −3
. Selisih yang kecil antara kedua metode menunjukkan bahwa KMA mampu
menghasilkan solusi yang mendekatifminconpada model minimumcostdengan batasan
bobot yang ditentukan.
4.4.6    Konvergensi Iterasi KMA
Selain  membandingkan  hasil  akhir  optimasi,  kinerja  KMA  juga  dianalisis  melalui
perubahan nilaicostatau fungsi objektif selama proses iterasi.  Visualisasi ini digunakan
untuk  melihat  kemampuan  KMA  dalam  memperbaiki  kualitas  solusi  dari  satu  iterasi
ke iterasi berikutnya hingga mencapai kondisi konvergen.  Pada algoritma metaheuristik
berbasis populasi, pola penurunan nilaicostatau fungsi objektif menjadi indikator bahwa
mekanisme pembaruan posisi individu mampu mengarahkan pencarian menuju solusi yang
lebih baik.
## 34

(a) Skenario batasan umum(b) Skenario batasan yang ditentukan
Gambar 4.7    Perubahan Nilai Fungsi Objektif KMA pada Model SkalarisasiCost-Risiko
(a) Skenario batasan umum(b) Skenario batasan yang ditentukan
Gambar 4.8    Perubahan NilaiCostKMA pada Model MinimumCost
Tabel 4.10    Nilai fungsi objektif terbaik KMA pada  Gambar 4.7b
Iterasi Fase 1NilaiIterasi Fase 2Nilai
## 17,9050×10
## −5
## 217,9050×10
## −5
## 27,9050×10
## −5
## 227,9050×10
## −5
## 37,9050×10
## −5
## 237,9050×10
## −5
## 47,9050×10
## −5
## 247,9050×10
## −5
## 57,9050×10
## −5
## 257,9050×10
## −5
## 67,9050×10
## −5
## 267,9050×10
## −5
## 77,9050×10
## −5
## 277,9050×10
## −5
## 87,9050×10
## −5
## 287,9050×10
## −5
## 97,9050×10
## −5
## 297,9050×10
## −5
## 107,9050×10
## −5
## 307,9050×10
## −5
## 117,9050×10
## −5
## 317,9050×10
## −5
## 127,9050×10
## −5
## 327,9050×10
## −5
## 137,9050×10
## −5
## 337,9050×10
## −5
## 147,9050×10
## −5
## 347,9050×10
## −5
## 157,9050×10
## −5
## 357,9050×10
## −5
## 167,9050×10
## −5
## 367,9050×10
## −5
## 177,9050×10
## −5
## 377,9050×10
## −5
## 187,9050×10
## −5
## 387,9050×10
## −5
## 197,9050×10
## −5
## 397,9050×10
## −5
## 207,9050×10
## −5
## 407,9050×10
## −5
Berdasarkan Gambar 4.7 dan Gambar 4.8, nilai fungsi objektif maupuncostKMA
mengalami perbaikan selama proses iterasi.  Penurunan pada iterasi awal menunjukkan
bahwa  proses  eksplorasi  dan  eksploitasi  dalam  KMA  mampu  menghasilkan  kandidat
## 35

solusi yang semakin baik.  Setelah beberapa iterasi, perubahan nilai mulai mengecil dan
cenderung  stabil.   Kondisi  ini  menunjukkan  bahwa  algoritma  telah  mendekati  kondisi
konvergen, yaitu ketika perbaikan solusi pada iterasi berikutnya tidak lagi signifikan.
Pada model skalarisasicost-risiko, grafik konvergensi menunjukkan perubahan nilai
fungsi objektif yang memuat komponen risiko dancostsecara simultan.  Sebagai contoh,
pada skenario batasan yang ditentukan di  Gambar 4.7b, nilai fungsi objektif terbaik pada
iterasi ke-1 hingga iterasi ke-40 dapat dilihat pada  Tabel 4.10.  Seluruh nilai pada fase 1
(iterasi 1–20) dan fase 2 (iterasi 21–40) tercatat tetap sebesar 7,9050×10
## −5
## .  Pembagian
ini digunakan karena pemeriksaan kestabilan konvergensi dilakukan dengan mengamati
20 iterasi yang telah mencapai nilai konvergen pada fase 1, kemudian dikonfirmasi kembali
melalui 20 iterasi berikutnya pada fase 2.  Karena tidak terdapat perubahan nilai pada
kedua fase tersebut, dapat disimpulkan bahwa KMA telah mencapai kondisi stabil dan
tidak lagi menunjukkan perbaikan fungsi objektif yang signifikan.  Sementara itu,  pada
model minimumcost, grafik menunjukkan perubahan nilaicostterbaik yang tetap harus
memenuhi  kendala  risiko.   Dengan  demikian,  grafik  konvergensi  ini  memperkuat  hasil
numerik bahwa KMA dapat digunakan sebagai pendekatan alternatif dalam penyelesaian
model optimasi portofolio utang negara multivaluta.
## 4.4.7    Perbandingan Efisiensi Komputasi
Perbandingan   efisiensi   komputasi   dilakukan   untuk   melihat   kebutuhan   waktu
penyelesaian  model  menggunakanfmincondan  KMA.  Karenafminconmerupakan
metode  optimasi  numerik  deterministik,  waktu  komputasinya  cenderung  lebih  singkat
dibandingkan KMA yang mengevaluasi populasi solusi secara iteratif.
## Tabel 4.11    Perbandingan Efisiensi Komputasi
Model dan Skenariofmincon(detik)   KMA (detik)
Skalarisasicost-risiko batasan umum1,062310,9751
Skalarisasicost-risiko batasan yang ditentukan1,140927,1108
Minimumcostbatasan umum40,4415670,1964
Minimumcostbatasan yang ditentukan34,2250638,5397
Berdasarkan  Tabel  4.11,fminconmembutuhkan  waktu  komputasi  yang  lebih  kecil
pada seluruh skenario.  Hal ini wajar karena model yang diselesaikan memiliki dimensi
relatif  kecil  dan  struktur  matematis  yang  dapat  dimanfaatkan  langsung  oleh  metode
optimasi  numerik.Sebaliknya,  KMA  memerlukan  waktu  lebih  lama  karena  proses
pencariannya dilakukan melalui pembaruan populasi solusi.
Pada  model  skalarisasicost-risiko,  waktu  komputasi  KMA  masing-masing  sebesar
10,9751 detik untuk skenario batasan umum dan 27,1108 detik untuk skenario batasan
yang ditentukan.  Pada model minimumcost, waktu komputasi KMA meningkat menjadi
670,1964 detik untuk skenario batasan umum dan 638,5397 detik untuk skenario batasan
yang  ditentukan.   Dengan  demikian,fminconlebih  unggul  dari  sisi  efisiensi  komputasi
pada  seluruh  skenario.   Namun,  KMA  tetap  relevan  sebagai  metode  alternatif  karena
mampu  menghasilkan  solusi  yang  mendekati  metode  acuan,  khususnya  ketika  model
dikembangkan menjadi lebih kompleks dan tidak selalu mudah diselesaikan dengan metode
deterministik.
## 36

## 4.4.8    Evaluasi Keseluruhan
Secara   keseluruhan,   hasil   optimasi   menunjukkan   bahwa   bentuk   kendala   yang
digunakan  memiliki  pengaruh  besar  terhadap  komposisi  portofolio.Pada  skenario
batasan umum, baik model skalarisasicost-risiko maupun model minimumcostcenderung
menghasilkan portofolio yang terkonsentrasi hampir seluruhnya pada USD30Y. Hal ini
terjadi karena batasan umum memberikan ruang alokasi yang sangat longgar.  Sebaliknya,
ketika  batasan  bobot  yang  ditentukan  diterapkan,  komposisi  portofolio  menjadi  lebih
tersebar dan tetap berada dalam rentang alokasi yang sesuai dengan ketentuan minimum
dan maksimum setiap instrumen.
Model minimumcostdengan kendala risiko memberikan hasil yang terkendali karena
risiko  portofolio  dibatasi  secara  eksplisit.    Pada  skenario  batasan  umum,  risiko  yang
dihasilkan adalah 5,18353×10
## −4
, sedangkan pada skenario batasan yang ditentukan risiko
berada di sekitar 1,18579×10
## −3
.  Nilai tersebut menunjukkan bahwa perubahan batasan
bobot berpengaruh terhadap tingkat risiko dan komposisi portofolio yang dihasilkan.
Dari  sisi  metode  penyelesaian,  KMA  mampu  menghasilkan  solusi  yang  mendekati
fminconpada seluruh skenario.  Pada beberapa skenario, seperti model skalarisasicost-
risiko batasan umum dan model minimumcostbatasan umum, hasil KMA sangat dekat
bahkan sama setelah pembulatan.  Namun,fmincontetap lebih unggul dari sisi efisiensi
komputasi. Keunggulan KMA terletak pada fleksibilitasnya sebagai metode metaheuristik
yang dapat dikembangkan untuk model yang lebih kompleks, misalnya dengan tambahan
kendala kardinalitas, kendala diskret, atau bentuk fungsi objektif yang tidak sepenuhnya
konveks.
Dengan demikian, hasil penelitian ini menunjukkan bahwa penerapan model optimasi
portofolio  mampu  memberikan  komposisi  utang  yang  lebih  terukur  dari  sisicostdan
risiko.   Selain  itu,  KMA  dapat  digunakan  sebagai  metode  alternatif  yang  layak  karena
mampu menghasilkan solusi yang mendekati solusi acuan, meskipun membutuhkan waktu
komputasi yang lebih besar dibandingkanfmincon.
## 37



## BAB V
## KESIMPULAN DAN SARAN
## 5.1    Kesimpulan
Berdasarkan  hasil  penelitian  yang  telah  dilakukan  mengenai  optimasi  portofolio
utang negara multivaluta menggunakanKomodo Mlipir Algorithm(KMA), dapat ditarik
kesimpulan sebagai berikut:
-  Model  optimasi  portofolio  utang  negara  multivaluta  yang  terdiri  atas  instrumen
berdenominasi USD, JPY, dan EUR berhasil dirumuskan menggunakan kerangka
Mean-Variance   Optimization(MVO).   Formulasi   model   dilakukan   dalam   dua
bentuk,  yaitu  model  skalarisasicost-risiko  serta  model  minimumcostdengan
kendala  risiko.   Kedua  model  tersebut  dilengkapi  dengan  kendala  anggaran  dan
batasan bobot, baik berupa skenario batasan umum maupun skenario batasan yang
ditentukan berdasarkan komposisi utang.  Dengan demikian, model yang dibentuk
mampu  merepresentasikan  hubungan  antara  biaya  dan  risiko  dalam  pengelolaan
portofolio utang negara multivaluta.
-  Hasil  optimasi  menunjukkan  bahwa  bentuk  batasan  bobot  berpengaruh  terhadap
komposisi   portofolio   yang   dihasilkan.Pada   skenario   batasan   umum,   baik
model skalarisasicost-risiko maupun model minimumcostmenghasilkan portofolio
yang  terkonsentrasi  hampir  seluruhnya  pada  instrumen  USD
30Y.  Pada  skenario
batasan  yang  ditentukan,  komposisi  portofolio  menjadi  lebih  tersebar  dan  tetap
berada  dalam  rentang  bobot  minimum  dan  maksimum  yang  telah  ditetapkan.
Hal   ini   menunjukkan   bahwa   batasan   bobot   yang   ditentukan   lebih   mampu
merepresentasikan komposisi portofolio yang realistis dibandingkan batasan umum.
3.Komodo Mlipir Algorithm(KMA) berhasil diimplementasikan untuk menyelesaikan
model   optimasi   portofolio   utang   negara   multivaluta.Implementasi   KMA
dilakukan dengan merepresentasikan setiap individu sebagai vektor bobot portofolio,
mengevaluasi kualitas solusi berdasarkan fungsi objektif, serta menjaga kelayakan
solusi   terhadap   kendala   anggaran   dan   batasan   bobot.Berdasarkan   hasil
perbandingan, KMA mampu menghasilkan nilaicost, risiko, dan bobot portofolio
yang mendekati hasilfminconpada seluruh skenario.  Namun,fmincontetap lebih
unggul  dari  sisi  waktu  komputasi,  terutama  pada  model  minimumcost.   Dengan
demikian, KMA dapat digunakan sebagai metode alternatif yang layak, khususnya
untuk pengembangan model optimasi yang lebih kompleks.
## 5.2    Saran
Berdasarkan hasil penelitian dan keterbatasan yang ditemukan, beberapa saran untuk
pengembangan penelitian selanjutnya adalah sebagai berikut:
-  Penelitian  selanjutnya  dapat  mengembangkan  model  optimasi  portofolio  utang
negara  multivaluta  dengan  pendekatan  optimasi  multiobjektif.   Berbeda  dengan
pendekatan skalarisasi yang menggabungkancostdan risiko ke dalam satu fungsi
objektif melalui parameter pembobot, pendekatan ini memperlakukan kedua aspek
## 39

tersebut  sebagai  fungsi  objektif  yang  terpisah.   Dengan  demikian,  hasil  optimasi
dapat  digunakan  sebagai  pembanding  terhadap  pendekatan  skalarisasi  dalam
mengevaluasi  keseimbangan  antara  biaya  pembiayaan  dan  risiko  portofolio  utang
negara.
-  Pengembangan  model  dapat  dilakukan  dengan  menambahkan  kendala  yang  lebih
realistis, seperti batasan kardinalitas yang membatasi jumlah instrumen aktif dalam
portofolio, kendala likuiditas, atau kendala regulasi yang berlaku dalam pengelolaan
utang negara Indonesia, sehingga model yang dihasilkan lebih sesuai dengan kondisi
praktis di lapangan.
-  Perbandingan   kinerja   KMA   dapat   diperluas   dengan   melibatkan   algoritma
metaheuristik lain yang lebih beragam, sepertiParticle Swarm Optimization(PSO),
Genetic  Algorithm(GA),  atauDifferential  Evolution(DE),  untuk  memberikan
gambaran yang lebih komprehensif mengenai posisi KMA di antara berbagai metode
optimasi metaheuristik dalam konteks optimasi portofolio utang negara.
-  Analisis sensitivitas terhadap parameter KMA, khususnya ukuran populasi, proporsi
big   males,mlipir   rate,   jumlah  iterasi  maksimum,   dan  toleransi  konvergensi,
perlu dilakukan secara lebih mendalam untuk memahami pengaruh masing-masing
parameter terhadap kualitas solusi dan efisiensi komputasi.  Hal ini penting karena
hasil  penelitian  menunjukkan  bahwa  waktu  komputasi  KMA  masih  lebih  besar
dibandingkanfmincon.
-  Penelitian ini dapat dikembangkan dengan menggunakan data yang lebih panjang
dan mencakup lebih banyak instrumen utang, termasuk instrumen berdenominasi
mata uang lain yang relevan, serta mempertimbangkan faktor-faktor makroekonomi
yang  dapat  memengaruhi  risiko  dan  biaya  portofolio  utang  negara  secara  lebih
komprehensif.
## 40

## DAFTAR PUSTAKA
Abolmaali, Saina dan Fraydoon Rahnamay Roodposhti (2018). “Portfolio optimization
using  ant  colony  method  a  case  study  on  Tehran  stock  exchange”.  In:Journal  of
Accounting8.1, pp. 96–108.
Brezoˇcnik,   Lucija,   Iztok   Fister,   dan   Vili   Podgorelec   (2018).   “Swarm   Intelligence
Algorithms for Feature Selection: A Review”. In:Applied Sciences8.
Eichengreen, Barry dan Ricardo Hausmann (1999).Exchange rates and financial fragility.
Elton, Edwin J. dkk. (2009).Modern Portfolio Theory and Investment Analysis. 8th ed.
New Jersey, USA: John Wiley & Sons, p. 752.isbn: 9780470388327.
Goldfarb, Donald dan Ashok Idnani (1983). “A numerically stable dual method for solving
strictly convex quadratic programs”. In:Mathematical Programming27.1, pp. 1–33.
Ho,  Diem  (1992).  “Quadratic  Programming  for  Portfolio  Optimization”.  In:Applied
Stochastic Models and Data Analysis8.3, pp. 189–194.
IMF,  IMF  (2014).  “Revised  guidelines  for  public  debt  management”.  In:IMF  Policy
Paper, International Monetary Fund, Washington, p. 43.
Kusuma,  Purba  Daru  dan  Meta  Kallista  (2022).  “Stochastic  Komodo  Algorithm.”  In:
International Journal of Intelligent Engineering & Systems15.4.
Markowitz, Harry (1952). “Portfolio Selection”. In:The Journal of Finance7.1, pp. 77–
## 91.
Markowitz, Harry M (2008).Portfolio  selection:  efficient  diversification  of  investments.
Yale university press.
M ́arov ́a,   Kateˇrina   (2016).   “Optimization   using   derivative-free   and   metaheuristic
methods”. In.
Nassef, Ahmed M dkk. (2024). “Hybrid metaheuristic algorithms: a recent comprehensive
review with bibliometric analysis.” In:International Journal of Electrical & Computer
## Engineering (2088-8708)14.6.
Nocedal, Jorge dan Stephen J. Wright (2006).Numerical Optimization. Springer.
Panzer,   J   dkk.   (2015).   “Debt   management   performance   assessment   (DeMPA)
methodology”. In:World Bank.
Salo, Ahti dkk. (2024). “Fifty years of portfolio optimization”. In:European  Journal  of
Operational Research318.1, pp. 1–18.
Scherzer, Otmar (1995). “Convergence criteria of iterative methods based on Landweber
iteration for solving nonlinear problems”. In:Journal  of  Mathematical  Analysis  and
Applications194.3, pp. 911–933.
Suyanto, Suyanto, Alifya Aisyah Ariyanto, dan Alifya Fatimah Ariyanto (2022). “Komodo
mlipir algorithm”. In:Applied Soft Computing114, p. 108043.
Talbi, El-Ghazali (2009).Metaheuristics: From Design to Implementation. Wiley.
Uthayakumar,  J  dkk.  (2020).  “Financial  crisis  prediction  model  using  ant  colony
optimization”.  In:International  Journal  of  Information  Management50,  pp.  538–
## 556.
## 41



## DAFTAR LAMPIRAN
## Lampiran 1
Repositori Kode ImplementasiKomodo Mlipir Algorithmpada
## MATLAB
Repositori   kode   lengkap   yang   digunakan   pada   penelitian   ini   dapat   diakses
melaluihttps://github.com/irfan2808-qql/code-final-project.   Tautan  tersebut
disertakan sebagai lampiran kode untuk memudahkan penelusuran implementasi secara
lengkap  tanpa  menambah  panjang  naskah  utama  maupun  lampiran  secara  berlebihan.
Dengan demikian, pembaca tetap dapat mengakses keseluruhan kode program, termasuk
proses  pengolahan  data,  implementasitwo-phaseKMA,  dan  pembentukan  grafik  hasil
optimasi, langsung melalui repositori tersebut.
## 43

## Lampiran 2
Data Suku Bunga (Yield) Instrumen Utang
Data   suku   bunga   (yield)   harian   yang   digunakan   dalam   penelitian   ini   dapat
diakses  melalui  repositori  data  penelitian  padahttps://github.com/irfan2808-qql/
Data-Penelitian-.   Repositori  tersebut  memuat  data  lengkap  tujuh  instrumen  utang
yang digunakan dalam penelitian ini selama periode pengamatan, sehingga lampiran ini
cukup disajikan dalam bentuk rujukan repositori untuk menghemat ruang.
## 44

## Lampiran 3
## Data Nilai Tukar Valuta Asing
Data nilai tukar harian EUR terhadap USD dan JPY terhadap USD yang digunakan
dalam penelitian ini juga dapat diakses melalui repositori data penelitian padahttps://
github.com/irfan2808-qql/Data-Penelitian-.  Repositori tersebut menyediakan data
lengkap periode pengamatan yang digunakan dalam proses pengolahan dan pembentukan
model optimasi, sehingga lampiran ini tidak lagi menampilkan tabel sampel data secara
terpisah.
## 45

## Lampiran 4
Hasil Perhitungan PerubahanCost, Rata-Rata Perubahan
Cost, dan Matriks Kovarians
Lampiran ini menyajikan hasil perhitungan numerik yang diperoleh dari pengolahan
data  suku  bunga  dan  nilai  tukar  menggunakan  skrip  Python.    Seluruh  perhitungan
dilakukan berdasarkanT= 1.081 observasi perubahancostharian yang diturunkan dari
1.082 data harga instrumen.
## A. Nilai Instrumen Setelah Penyesuaian
Data  nilai  instrumen  setelah  penyesuaian  dapat  diakses  melalui  repositori  data
penelitian  padahttps://github.com/irfan2808-qql/Data-Penelitian-.   Repositori
tersebut memuat data hasil penyesuaian nilai instrumen berdasarkan suku bunga (yield)
dan  nilai  tukar  selama  periode  pengamatan,  sehingga  subbagian  ini  disajikan  dalam
bentuk rujukan repositori untuk menghemat ruang lampiran.
B. PerubahanCostHistoris dan Rata-Rata PerubahanCost
Rata-Rata PerubahanCostμper Instrumen
## Instrumen
## ̄
## ∆c
i
## (harian)
## ̄
## ∆c
i
## (tahunan, %)
USDFixed5Y2,4744×10
## −5
## 0,6235
USDFixed10Y2,2914×10
## −5
## 0,5774
USDFixed30Y1,6407×10
## −5
## 0,4135
EURFixed7Y1,6597×10
## −5
## 0,4183
## EUR
Fixed10Y1,7399×10
## −5
## 0,4385
JPYFixed5Y−3,0466×10
## −4
## −7,6776
## JPY
Fixed10Y−3,0101×10
## −4
## −7,5855
C. Variansi PerubahanCostper Instrumen
Variansi dan Standar Deviasi PerubahanCostper Instrumen
## Instrumenσ
## 2
i
## (harian)σ
i
## (harian)
USDFixed5Y2,1402×10
## −7
## 4,6263×10
## −4
USDFixed10Y3,1884×10
## −7
## 5,6466×10
## −4
## USD
Fixed30Y2,6869×10
## −7
## 5,1835×10
## −4
EURFixed7Y2,4555×10
## −5
## 4,9553×10
## −3
EURFixed10Y    2,4541×10
## −5
## 4,9539×10
## −3
## JPY
Fixed5Y4,1809×10
## −5
## 6,4660×10
## −3
JPYFixed10Y4,2138×10
## −5
## 6,4914×10
## −3
## 46

## BIODATA PENULIS
R. Irfan Auliya Fauzan merupakan penulis Tugas Akhir berjudul
## Optimasi   Portofolio   Utang   Negara   Multivaluta   Menggunakan
AlgoritmaKomodoMLIPIR.Penulisterdaftarsebagai
mahasiswa Program Sarjana Departemen Matematika, Fakultas
Sains dan Analitika Data, Institut Teknologi Sepuluh Nopember,
dengan NRP 5002221129 dan bidang studi Matematika Terapan
dan Industri .
Selama  menempuh  perkuliahan,  penulis  memiliki  minat  pada
bidang    optimasi,pemodelan    matematika,simulasi,dan
komputasi  numerik.    Melalui  penelitian  ini,  penulis  mengkaji
penerapan  metode  optimasi  deterministik  dan  metaheuristik
dalam pembentukan portofolio utang negara multivaluta dengan
mempertimbangkan aspek biaya dan risiko.
## 47