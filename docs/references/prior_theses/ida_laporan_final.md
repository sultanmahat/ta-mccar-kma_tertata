

## TUGAS AKHIR - KM184801
## OPTIMASI KOMPOSISI UTANG VALUTA ASING
## DENGAN MODEL WORST-CASE CONDITIONAL
## VALUE-AT-RISK
## ZAKIYYAH FUROIDA
## NRP 5002221029
## Dosen Pembimbing
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
Jasmir, S.Pd., M.Si.
## NIP 19820523 200901 1 010
## Program Studi Sarjana
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
## Surabaya
## 2026



## TUGAS AKHIR - KM184801
## OPTIMASI KOMPOSISI UTANG VALUTA ASING
## DENGAN MODEL WORST-CASE CONDITIONAL
## VALUE-AT-RISK
## ZAKIYYAH FUROIDA
## NRP 5002221029
## Dosen Pembimbing
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
Jasmir, S.Pd., M.Si.
## NIP 19820523 200901 1 010
## Program Sarjana
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
## Surabaya
## 2026



## FINAL PROJECT - KM184801
## OPTIMIZATION OF INDONESIAN’S FOREIGN
## CURRENCY DEBT PORTOFOLIO USING THE
## WORST-CASE CONDITIONAL VALUE-AT-RISK
## MODEL
## ZAKIYYAH FUROIDA
## NRP 5002221029
## Supervisors
Sena Safarina, S.Si., M.Sc., D.Sc.
## NIP 1990202012052
Jasmir, S.Pd., M.Si.
## NIP 19820523 200901 1 010
## Bachelor Program
Departement of Mathematics
Faculty of Scientics
## Institut Teknologi Sepuluh Nopember
## Surabaya
## 2026



## LEMBAR PENGESAHAN
Optimasi Komposisi Utang Valuta Asing dengan Model Worst-Case
Conditional Value-at-Risk
## TUGAS AKHIR
Diajukan untuk memenuhi salah satu syarat
memperoleh gelar Sarjana Matematika pada
## Program Studi S-1 Matematika
## Departemen Matematika
Fakultas Sains dan Analitika Data
## Institut Teknologi Sepuluh Nopember
## Oleh: Zakiyyah Furoida
## NRP. 5002221029
## Surabaya, Juli 2026
Disetujui oleh Tim Penguji Tugas Akhir:
## Pembimbing
-  Sena Safarina, S.Si., M.Sc., D.Sc.(. . . . . . . . . . . . . . . . . . )
## NIP. 1990202012052
-  Jasmir, S.Pd., M.Si.(. . . . . . . . . . . . . . . . . . )
## NIP. 19820523 200901 1 010
## Penguji
-  Dr.  Valeriana Lukitosari, S.Si, MT(. . . . . . . . . . . . . . . . . . )
## NIP. 19710928 199802 2 001
-  Endah Rokhmati Merdika Putri, S.Si., M.T., Ph.D(. . . . . . . . . . . . . . . . . . )
## NIP. 19761213 200212 2 001
-  Raden Aurelius Andhika Viadinugroho, S.Si., M.Sc.(. . . . . . . . . . . . . . . . . . )
## NIP. 19990309 202406 1001
## Mengetahui
## Kepala Departemen Matematika
Fakultas Sains dan Analitika Data
Dr.  Didik Khusnul Arif, S.Si, M.Si
## NIP. 19730930 199702 1 001
i



## PERNYATAAN ORISINALITAS
Yang bertanda tangan disini:
Nama Mahasiswa / NRP:    Zakiyyah Furoida / 5002221029
## Departemen:    Matematika
Dosen Pembimbing / NIP    :    1.   Sena Safarina, S.Si., M.Sc., D.Sc. / 1990202012052
-   Jasmir, S.Pd., M.Si. / 19820523 200901 1 010
dengan  ini  menyatakan  bahwa  Tugas  Akhir  dengan  judul  “Optimasi  Komposisi  Utang
Valuta Asing dengan Model  Worst-Case  Conditional  Value-at-Risk” adalah hasil karya
sendiri, bersifat orisinal, dan ditulis dengan mengikuti kaidah penulisan ilmiah.
Bilamana di kemudian hari ditemukan ketidaksesuaian dengan pernyataan ini, maka saya
bersedia  menerima  sanksi  sesuai  dengan  ketentuan  yang  berlaku  di  Institut  Teknologi
## Sepuluh Nopember.
## Surabaya, 17 Juli 2026
## Mengetahui
Dosen Pembimbing 1Dosen Pembimbing 2
Sena Safarina, S.Si., M.Sc., D.Sc.
Jasmir, S.Pd., M.Si.
## NIP. 1990202012052NIP. 19820523 200901 1 010
## Mahasiswa
## Zakiyyah Furoida
## NRP. 5002221029
iii



## ABSTRAK
Optimasi Komposisi Utang Valuta Asing dengan Model Worst-Case Conditional
Value-at-Risk
Nama Mahasiswa / NRP    :    Zakiyyah Furoida / 5002221029
Departemen:    Matematika FSAD -ITS
Dosen Pembimbing:    1.   Sena Safarina, S.Si., M.Sc., D.Sc.
-   Jasmir, S.Pd., M.Si.
## Abstrak
Pada  akhir  November  2020,  jumlah  utang  pemerintah  meningkat  secara  signifikan
yang  tercatat  sebesar  Rp5.910  triliun  dengan  rasio  terhadap  Produk  Domestik  Bruto
(PDB)  mencapai  38, 13%.   Peningkatan  rasio  utang  tersebut  menjadi  peringatan  agar
pemerintah  Indonesia  semakin  bijaksana  dalam  mengelola  pembiayaan  utang.    Oleh
karena  itu,   pemerintah  Indonesia  senantiasa  menerapkan  pengelolaan  utang  secara
bijak  melalui  diversifikasi  komposisi  utang  valuta  asing.Dalam  kajian  akademik,
optimasi  komposisi  utang  dapat  diibaratkan  dengan  optimasi  portofolio  saham  seperti
menggunakan   model   mean-variance,   akan   tetapi   model   ini   memiliki   keterbatasan
dalam  menangkap  risiko  ekstrem.Sebagai  solusi  dari  keterbatasan  ini,  digunakan
model   Conditional   Value-at-Risk   dan   Worst-Case   Conditional   Value-at-Risk   untuk
mempertimbangkan   risiko   pada   tingkat   ketahanan   yang   lebih   ekstrem.Dengan
memanfaatkan  data  suku  bunga  dan  nilai  valuta  asing  dari  DJPPR  Kementerian
Keuangan Republik Indonesia, data ini akan dihitung pada ketiga model dengan tingkat
ukuran risiko yang berbeda dan nantinya akan dilakukan simulasi pada Matlab dengan
memanfaatkan  function  yang  sesuai.Sehingga  dihasilkan  komposisi  paling  optimal
untuk  strategi  dengan  batasan  khusus,  yaitu  terpilihnya  model  mean-CVaR  dengan
bobot tertinggi yaitu USD
5Y sebesar 47, 00% dengan expected cost sebesar 0, 000042292.
Sedangkan, untuk strategi tanpa batasan khusus, yaitu terpilihnya model mean-variance
dengan  bobot  tertinggi  yaitu  USD
30Y  sebesar  100%  dengan  expected  cost  sebesar
0.0000172.  Dari hasil berikut diharapkan dapat memberikan kontribusi akademik serta
rekomendasi kebijakan pemerintah terhadap diversifikasi komposisi utang valas.
Kata kunci:    Utang   Valuta   Asing,   Komposisi   Utang,   Mean-Variance,   Worst-Case
Conditional Value at Risk
v



## ABSTRACT
Optimization of Indonesian’s Foreign Currency Debt Portofolio Using the Worst-Case
Conditional Value-at-Risk Model
Student Name / NRP    :    Zakiyyah Furoida / 5002221029
Departement:    Mathematics SCIENTICS - ITS
Advisor:    1.   Sena Safarina, S.Si., M.Sc., D.Sc.
-   Jasmir, S.Pd., M.Si.
## Abstract
At the end of November 2020, the government’s debt increased significantly, recorded
at Rp5.910 trillion with a ratio to Gross Domestic Product (GDP) reaching 38, 13%.  This
increase in the debt ratio serves as a warning for the Indonesian government to be wiser in
managing debt financing.  Therefore, the Indonesian government consistently implements
prudent debt management through diversification of foreign currency debt composition.
In academic studies, optimization of debt composition can be likened to stock portfolio
optimization, such as using the mean-variance model however, this model has limitations
in  capturing  extreme  risks.   As  a  solution  to  these  limitations,  the  Conditional  Value-
at-Risk and Worst-Case Conditional Value-at-Risk models are employed to account for
risk  at  more  extreme  resilience  levels.   By  utilizing  interest  rate  and  foreign  exchange
rate  data  from  the  DJPPR  of  the  Ministry  of  Finance  of  the  Republic  of  Indonesia,
the  data  will  be  computed  across  three  models  with  different  risk  measure  levels  and
subsequently simulated in MATLAB using appropriate functions.  The results yield the
most  optimal  composition  for  a  strategy  with  specific  constraints,  namely  the  mean-
CVaR  model  with  the  highest  weight  of  USD
5Y  at  47, 00%  with  an  expected  cost  of
0, 000042292.  Meanwhile, for a strategy without specific constraints, the mean-variance
model is selected with the highest weight of USD
30Y at 100% with an expected cost of
0.0000172.  These results are expected to provide academic contributions as well as policy
recommendations for the government regarding the diversification of foreign currency debt
composition.
Keywords:    Foreign  Currency  Debt,  Debt  Composition,  Mean-Variance,  Worst-Case
Conditional Value at Risk
vii



## KATA PENGANTAR
Dengan  memanjatkan  puji  syukur  kehadirat  Allah  SWT  atas  rahmat,  taufik,  dan
hidayah-nya sehingga penulis dapat menyelesaikan tugas akhir dengan judul:
”Optimasi Komposisi Utang Valuta Asing dengan Metode Worst-Case Conditional
Value-at-Risk”
sebagai   salah   satu   persyaratan   akademis   dalam   menyelesaikan   Program   Sarjana
Departemen Matematika, Fakultas Sains dan Analitika Data, Institut Teknologi Sepuluh
Nopember   Surabaya.Penulis   menyadari   bahwa   Laporan   Tugas   Akhir   ini   dapat
diselesaikan dengan baik atas dukungan, bantuan, dan nasihat dari berbagai pihak.  Pada
kesempatan ini, penulis ingin mengucapkan terima kasih dan penghargaan kepada:
-  Ibu Sena Safarina, S.Si., M.Sc., D.Sc.  dan Bapak Jasmir, S.Pd., M.Si.  selaku Dosen
Pembimbing yang telah membantu dan memberikan arahan, serta motivasi kepada
penulis.
-  Ibu  Endah  Rokhmati  Merdika  Putri,  S.Si.,  M.T.,  Ph.D.  selaku  Dosen  Wali  yang
telah memberikan arahan kepada penulis selama masa perkuliahan.
-  Ibu  Dr.   Valeriana  Lukitosari,  S.Si.,  M.T.,  Ibu  Endah  Rokhmati  Merdika  Putri,
S.Si., M.T., Ph.D., dan Bapak Raden Aurelius Andhika Viadinugroho, S.Si., M.Sc.
selaku Dosen Penguji yang telah memberikan kritik dan sarannya untuk perbaikan
Laporan Tugas Akhir ini.
-  Bapak/Ibu  Dosen  Pengajar  yang  telah  memberikan  ilmu  dan  pengalaman  yang
bermanfaat,  serta  seluruh  karyawan,  tenaga  kependidikan,  dan  keluarga  besar
Departemen Matematika Institut Teknologi Sepuluh Nopember atas dukungan dan
bantuannya.
-  Teman-teman Teater Tiyang Alit yang telah menemani selama pengerjaan Laporan
Tugas Akhir ini.
Penulis mengharapkan saran dan kritik dari pembaca.  Akhir kata, semoga Laporan Tugas
Akhir ini bermanfaat bagi semua pihak yang membacanya.
## Surabaya, 18 Juni 2026
## Zakiyyah Furoida
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
1.5   Manfaat  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .3
## BAB IITINJAUAN PUSTAKA5
2.1   Penelitian Terdahulu  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
2.2   Utang Valuta Asing  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
2.3   Model Mean-Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
2.4    Return . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .7
2.4.1   Return Aset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
2.4.2   Expected Return Aset  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
2.4.3   Expected Return Portofolio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
2.5   Risiko  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.5.1   Varian Aset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.5.2   Kovarian Aset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.5.3   Risiko Portofolio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .9
2.6    Robust Risk Measurement  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    10
2.7    Conditional Value-at-Risk (CVaR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    10
2.8    Worst-Case Conditional Value-at-Risk (WCCVaR) . . . . . . . . . . . . . . . . . . .    12
2.9    Quadratic Programming . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
2.10  Interpolasi  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    14
## BAB IIIMETODOLOGI17
3.1   Studi Literatur  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.2   Pengumpulan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.3   Prapemrosesan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.4   Pengolahan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
xi

3.5   Formulasi Model Mean-Variance Komposisi Utang Valuta Asing . . . . . . .    18
3.6   Formulasi Kendala Risiko  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    18
3.7   Formulasi Parameter Kendala . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.8   Penyelesaian Optimasi Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.9   Analisis Hasil dan Pembahasan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.10  Penarikan Kesimpulan dan Saran  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
3.11  Penyusunan Laporan Tugas Akhir . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
## BAB IVHASIL DAN PEMBAHASAN21
4.1   Pengumpulan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
4.2   Prapemrosesan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    22
4.3   Pengolahan Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
4.3.1   Menghitung Total Biaya Utang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23
4.3.2   Menghitung Tingkat Perubahan Total Biaya  . . . . . . . . . . . . . . . . . .    24
4.3.3   Menghitung Mean Tingkat Perubahan Total Biaya . . . . . . . . . . . . .    24
4.3.4   Menghitung Varians Tingkat Perubahan Total Biaya  . . . . . . . . . . .    25
4.3.5   Menghitung Standar Deviasi Total Biaya . . . . . . . . . . . . . . . . . . . . . .    26
4.3.6   Menghitung Matriks Varians-Kovarians . . . . . . . . . . . . . . . . . . . . . . .    26
4.3.7   Statistik Deskriptif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    27
4.4   Formulasi Model Mean-Variance untuk Komposisi Utang Valuta Asing .    28
4.5   Formulasi Kendala Risiko Model Mean-Variance . . . . . . . . . . . . . . . . . . . . .    28
4.5.1   Kendala Risiko Conditional Value-at-Risk (CVaR)  . . . . . . . . . . . . .    28
4.5.2   Kendala Risiko Worst-case Conditional Value-at-Risk (W-CVaR) .    29
4.6   Penentuan Kendala Batas Atas dan Batas Bawah Instrumen . . . . . . . . . .    30
4.7   Penentuan Nilai Risiko Maksimal (R
max
) pada Kendala Model  . . . . . . . .    31
4.8   Penyelesaian Optimasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    32
4.8.1   Penyelesaian Optimasi dengan Model Mean-Variance  . . . . . . . . . . .    32
4.8.2   Penyelesaian Optimasi dengan Model Mean-CVaR  . . . . . . . . . . . . .    35
4.8.3   Penyelesaian Optimasi dengan Model Mean-WCCVaR . . . . . . . . . .    37
4.9   Hasil dan Pembahasan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    38
4.9.1   Hasil untuk Strategi dengan Batasan Khusus . . . . . . . . . . . . . . . . . .    38
4.9.2   Grafik Efficient Frontier  Strategi dengan Batasan Khusus . . . . . . .    40
4.9.3   Hasil untuk Strategi tanpa Batasan Khusus  . . . . . . . . . . . . . . . . . . .    40
4.9.4   Grafik Efficient Frontier  Strategi tanpa Batasan Khusus . . . . . . . .    41
## BAB VKESIMPULAN DAN SARAN43
5.1   Kesimpulan  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    43
5.2   Saran . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    43
## DAFTAR PUSTAKA45
## DAFTAR LAMPIRAN47
Lampiran 1    Hasil Interpolasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    47
Lampiran 2    Data Suku Bunga dan Data Valuta Asing . . . . . . . . . . . . . . . . . . .    48
Lampiran 3    Data Total Biaya Utang Valas . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    49
Lampiran 4    Data Tingkat Perubahan Total Biaya Utang Valas . . . . . . . . . . .    50
Lampiran 5    Hasil Optimasi tanpa Batasan Khusus . . . . . . . . . . . . . . . . . . . . . .    51
Lampiran 6    Hasil Optimasi dengan Batasan Khusus  . . . . . . . . . . . . . . . . . . . .    53
## BIODATA PENULIS59
xii

## DAFTAR GAMBAR
Gambar 2.1   State of The Art Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6
Gambar 3.1   Diagram Alir Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    17
Gambar 4.1   Grafik Pergerakan Suku Bunga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
Gambar 4.2   Grafik Pergerakan Nilai Valuta Asing USD/EUR . . . . . . . . . . . . . . .    22
Gambar 4.3   Grafik Pergerakan Nilai Valuta Asing USD/JPY  . . . . . . . . . . . . . . .    22
Gambar 4.4   Grafik Pergerakan Tingkat Perubahan Total Biaya . . . . . . . . . . . . . .    27
Gambar 4.5   Grafik Keseluruhan Bobot Optimal dengan Batasan Khusus  . . . . .    40
Gambar 4.6   Grafik Efficient Frontier  dengan Batasan Khusus . . . . . . . . . . . . . . .    40
Gambar 4.7   Grafik Keseluruhan Bobot Optimal tanpa Batasan Khusus . . . . . . .    41
Gambar 4.8   Grafik Efficient Frontier  tanpa Batasan Khusus . . . . . . . . . . . . . . . .    42
xiii



## DAFTAR TABEL
Tabel 4.1   Data Suku Bunga dan Nilai Valuta Asing . . . . . . . . . . . . . . . . . . . . . . . .    21
Tabel 4.2   Hasil Prapemrosesan Data Suku Bunga EUR 10 Tahun . . . . . . . . . . . .    23
Tabel 4.3   Data Perhitungan Total Biaya Utang  . . . . . . . . . . . . . . . . . . . . . . . . . . .    24
Tabel 4.4   Data Perhitungan Tingkat Perubahan Total Biaya Utang . . . . . . . . . .    24
Tabel 4.5    Mean Tingkat Perubahan Total Biaya . . . . . . . . . . . . . . . . . . . . . . . . . . .    25
Tabel 4.6   Varians Tingkat Perubahan Total Biaya . . . . . . . . . . . . . . . . . . . . . . . . .    25
Tabel 4.7   Varians Tingkat Perubahan Total Biaya . . . . . . . . . . . . . . . . . . . . . . . . .    26
Tabel 4.8   Hasil Analisis Statistik Deskriptif . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    27
Tabel 4.9   Proporsi Existing (2024) dan Batas Instrumen  . . . . . . . . . . . . . . . . . . .    30
Tabel 4.10  Strategi variasi batasan bobot untuk tiap instrumen  . . . . . . . . . . . . . .    31
Tabel 4.11  strategi variasi nilai risiko maksimal (R
max
## ) . . . . . . . . . . . . . . . . . . . . . .    32
Tabel 4.12  Hasil Optimasi Model Mean-Variance . . . . . . . . . . . . . . . . . . . . . . . . . . .    35
Tabel 4.13  Hasil Optimasi Model Mean-CVaR  . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    37
Tabel 4.14  Hasil Optimasi Model Mean-WCCVaR . . . . . . . . . . . . . . . . . . . . . . . . . .    38
Tabel 4.15  Hasil Optimasi untuk Strategi dengan Batasan Khusus . . . . . . . . . . . .    39
Tabel 4.16  Hasil Optimasi untuk Strategi tanpa Batasan Khusus  . . . . . . . . . . . . .    41
xv



## DAFTAR SIMBOL
i:    Indeks yang menunjukkan aset atau sekuritas tertentu
t:    Indeks yang menunjukkan periode waktu tertentu dalam rangkaian data
historis
n:    Jumlah total periode dalam data historis
m:    Jumlah total aset
1:    Vektor satuan berdimensi n
x:    Vektor bobot portofolio (x
## 1
## ,x
## 2
## ,...,x
n
## )
## ⊤
x
i
:    Bobot dana yang diinvestasikan pada aset ke-i
μ:    Vektor ekspektasi return aset (μ
## 1
## ,μ
## 2
## ,...,μ
n
## )
## ⊤
μ
i
:    Estimasi ekspektasi pengembalian untuk aset ke-i
μ
min
:    Tingkat return minimum portofolio yang disyaratkan
Σ:    Matriks varians-kovarians simetris berukuran m× m
r
i,t
:    Tingkat pengembalian (rate of return) aset ke-i pada periode waktu ke-t
## I
i,t
:    Nilai total return aset ke-i pada waktu ke-t
## I
i,t−1
:    Nilai total return aset ke-i pada periode sebelumnya (t− 1)
## ̄r
i
:    Rata-rata aritmatika tingkat pengembalian aset ke-i
σ
## 2
i
:    Varians return aset ke-i
σ
i
:    Standar deviasi return aset ke-i
σ
j
:    Standar deviasi return aset ke-j
ρ
ij
:    Koefisien korelasi antara return aset ke-i dan ke-j
cov(R
i
## ,R
j
)    :    Kovarians antara return aset ke-i dan aset ke-j
## IR
i,t
:    Suku bunga (interest rate) instrumen ke-i pada periode ke-t
## FX
j,t
:    Nilai valuta asing (foreign exchange) instrumen ke-j pada periode ke-t
## C
i,t
:    Total biaya utang pada instrumen ke-i dan periode ke-t
f (x,y):    Fungsi kerugian (loss function) portofolio
y:    Variabel acak yang memiliki distribusi probabilitas p(y)
p(y):    Fungsi densitas probabilitas dari variabel acak y
ψ(x,a):    Fungsi distribusi kumulatif dari fungsi kerugian f (x,y)
α:    Tingkat kepercayaan (confidence level) dalam pengukuran risiko CVaR
β:    Tingkat   kepercayaan   (confidence   level)   dalam   pengukuran   risiko
WCCVaR
γ:    Parameter ambang batas yang merepresentasikan nilai VaR
S:    Jumlah total skenario simulasi
s:    Indeks skenario, s = 1,...,S
y
s
:    Vektor faktor risiko pada skenario ke-s
f (x,y
s
):    Fungsi kerugian portofolio x pada skenario ke-s
z
s
:    Variabel  bantu  yang  merepresentasikan  kerugian  melebihi  ambang γ
pada skenario ke-s
## U
α
j
:    Batas atas CVaR yang dapat ditoleransi pada tingkat kepercayaan α
j
X:    Himpunan kendala kelayakan portofolio
w:    Vektor bobot portofolio pada model WCCVaR
xvii

τ:    Batas maksimum risiko yang dapat ditoleransi pada model WCCVaR
κ:    Faktor skala WCCVaR, κ =
q
β/(1− β)
Q:    Matriks simetris berukuran n× n pada quadratic programming
c:    Vektor berukuran n× 1 pada quadratic programming
A:    Matriks kendala kesamaan berukuran m× n
b:    Vektor kendala kesamaan berukuran m× 1
D:    Matriks kendala ketidaksamaan berukuran p× n
g:    Vektor kendala ketidaksamaan berukuran p× 1
x
l
:    Batas bawah interval pencarian akar pada interpolasi
x
u
:    Batas atas interval pencarian akar pada interpolasi
x
r
:    Perkiraan titik potong garis lurus dengan sumbu-x pada interpolasi
f (x
l
):    Nilai fungsi f (x) pada titik x
l
f (x
u
)    :    Nilai fungsi f (x) pada titik x
u
## R
max
:    Nilai risiko maksimal yang diizinkan pada kendala model
lb:    Batas bawah (lower bound) bobot per instrumen
ub:    Batas atas (upper bound) bobot per instrumen
xviii

## BAB I
## PENDAHULUAN
## 1.1    Latar Belakang
## Berdasarkan  Peraturan  Pemerintah  Republik  Indonesia  Nomor  02  Tahun  2006
tentang  Tata  Cara  Pengadaan  Pinjaman  dan/atau  Penerimaan  Hibah  serta  Penerusan
Pinjaman  dan  atau  Hibah  Luar  Negeri,  yang  dimaksud  dengan  utang  atau  pinjaman
adalah  setiap  penerimaan  negara  baik  dalam  bentuk  devisa  dan  atau  devisa  yang
dirupiahkan, rupiah, maupun dalam bentuk barang dan jasa yang diperoleh dari pemberi
pinjaman luar negeri yang harus dibayar kembali dengan persyaratan tertentu.  Publikasi
Statistik Utang Luar Negeri Indonesia menyatakan bahwa Pinjaman Luar Negeri adalah
setiap penerimaan negara baik dalam bentuk devisa dan/atau devisa yang dirupiahkan,
rupiah,   maupun  dalam  bentuk  barang  dan/atau  jasa  yang  diperoleh  dari  pemberi
pinjaman luar negeri yang harus dibayar kembali dengan persyaratan tertentu (Indonesia,
## 2021).
Selama masa pandemi Covid-19, beban utang pemerintah meningkat hingga mencapai
tingkat  yang  sulit  dihindari.    Sampai  akhir  November  2020,  total  utang  pemerintah
Indonesia mencapai Rp5.910 triliun, dengan rasio utang terhadap Produk Domestik Bruto
(PDB) sebesar 38,13% (Ananda, 2021).  Meskipun rasio ini masih berada di bawah batas
maksimal 60% yang ditetapkan dalam UU Nomor 17 Tahun 2003, hal ini tidak berarti
bahwa pemerintah memiliki ruang yang aman untuk terus meningkatkan utang.  Justru,
kenaikan rasio utang menjadi peringatan agar pemerintah lebih hati-hati dan bijaksana
dalam mengelola pembiayaan utang.
Mengacu pada informasi dari laman Kementerian Keuangan, pemerintah senantiasa
melakukan pengelolaan utang secara hati-hati melalui pengaturan komposisi mata uang,
tingkat bunga, serta struktur jatuh tempo yang optimal. Pemerintah juga mengutamakan
penerbitan utang berjangka menengah-panjang dan menerapkan pengelolaan portofolio
utang secara aktif.  Upaya tersebut terlihat dari menurunnya rasio utang pemerintah pada
akhir 2023 dibandingkan akhir 2022 (39,70% PDB) maupun puncak pandemi di akhir 2021
(40,74%  PDB)  (Direktorat  Jenderal  Pengelolaan  Pembiayaan  dan  Risiko,  Kementerian
## Keuangan Republik Indonesia, 2025).
Pengelolaan pinjaman luar negeri pemerintah tidak terlepas dari berbagai risiko yang
perlu dimitigasi. Salah satu risiko utama terkait dengan variasi denominasi pinjaman yang
berasal dari dalam maupun luar negeri, seperti USD, EUR, JPY, dan mata uang lainnya.
Berdasarkan  Statistik  Utang  Luar  Negeri  Indonesia  (SULNI)  tahun  2021,  komposisi
pinjaman  pemerintah  masih  didominasi  oleh  USD,  yaitu  sebesar  USD92,3  miliar  dari
total  USD200,2  miliar  pinjaman  luar  negeri.   Di  posisi  berikutnya  terdapat  pinjaman
berdenominasi  IDR  sebesar  USD62,4  miliar,  EUR  sebesar  USD21,7  miliar,  dan  JPY
sebesar  USD21,3  miliar  (Indonesia,  2021).    Dominasi  mata  uang  USD  ini  membuat
pemerintah  rentan  terhadap  volatilitas  global,  sehingga  diperlukan  upaya  diversifikasi
mata uang untuk mengurangi eksposur risiko nilai tukar.
Dalam  menentukan  portofolio  utang,  pendekatan  optimasi  portofolio  saham  dapat
diadaptasi. Salah satu pendekatan yang paling terkenal adalah model mean-variance yang
diperkenalkan  oleh  Markowitz  (1952),  yang  bertujuan  memaksimalkan  expected  return
## 1

atau meminimalkan risiko berdasarkan varians  return.  Model ini telah menjadi fondasi
teori portofolio modern dan membuka jalan bagi penggunaan metode kuantitatif dalam
pengambilan keputusan keuangan (Eduardus Tandelilin & CWM, 2017).
Namun,   seiring   perkembangan   waktu,   banyak   penelitian   memperluas   model
(Markowitz, 1952) dengan mempertimbangkan ketidakpastian parameter.  Model mean-
variance  klasik bersifat pasti karena mengandalkan estimasi tunggal dari data historis.
Padahal,  dalam  praktiknya,  return  aset  bersifat  tidak  pasti  dan  dapat  berubah  seiring
waktu.    Salah  satu  pendekatan  yang  dikembangkan  untuk  mengatasi  ketidakpastian
ini adalah  Robust  Optimization, yaitu metode optimasi yang menghasilkan solusi stabil
meskipun terjadi kesalahan estimasi atau perubahan nilai parameter input seperti return
dan kovarians aset (Georgantas, Doumpos, & Zopounidis, 2024).
Contoh model-model dari  Robust  Optimization  dengan menggunakan ukuran risiko
yaitu  Mean–variance  with  box  uncertainty,  Mean–variance  with  el lipsoidal  uncertainty,
Worst-case  Conditional  Value-at-Risk,  Worst-case  Omega  Ratio,  dan  lainnya.   Dalam
literatur  optimasi  portofolio  terdapat  beberapa  penelitian  yang  membandingkan  hasil
berbagai model robust dalam dalam satu kerangka kerja yang terpadu dan terstandar.
Sebagai contoh penelitian oleh Georgantas et al. (2024) yang membandingkan beberapa
model Robust Optimization.  Penelitian ini menyimpulkan bahwa Worst-Case Conditional
Value-at-Risk  oleh Zhu and Fukushima (2009) menunjukan model dengan kinerja yang
paling  stabil  dibanding  model  lainnya.Model  ini  dikatakan  sebagai  model  robust
counterpart  dari  model  Conditional  Value-at-Risk  yang  digunakan  untuk  mengatasi
ketidakpastian distribusi return portofolio. Karena distribusi return portofolio sebenarnya
bersifat acak dan tidak diketahui secara pasti, memperkenalkan pendekatan robust yang
mempertimbangkan kemungkinan terburuk dari berbagai distribusi yang mungkin terjadi.
Maka dalam penelitian ini akan digunakan model Worst-case Conditional Value-at-Risk
oleh Zhu and Fukushima (2009) untuk membangun portofolio saham yang optimal.
Oleh  karena  itu,   pada  tugas  akhir  ini  penulis  menggunakan  formulasi  model
mean–variance  oleh Markowitz (1952) untuk membangun komposisi utang valuta asing
yang  optimal  dengan  meminimalkan  ekspektasi  biaya  dengan  membatasi  risiko  yang
dihitung  menggunakan  ukuran  risiko  yang  berbeda-beda.   Risiko  diukur  menggunakan
model  robust  optimization  yaitu  Worst-Case  Conditional  Value-at-Risk  oleh  Zhu  and
Fukushima (2009) sebagai ukuran yang tangguh dalam menghadapi ketidakpastian dan
strategi  ekstrem.   Model  ini  dibatasi  oleh  ambang  batas  keberlanjutan  pada  arus  dan
stok utang guna mengendalikan risiko pembiayaan ulang serta menjaga dinamika utang
yang berkelanjutan.  Sebagai pembanding, risiko juga akan diukur dengan model klasik
mean-variance oleh (Markowitz, 1952) dan model robust optimization lainnya Conditional
Value-at-Risk  oleh (Rockafellar, Uryasev, et al., 2000).  Dengan fokus pada tiga sumber
utang luar negeri Indonesia, yaitu USD, EUR, dan JPY, simulasi penyelesaian dilakukan
menggunakan perangkat lunak optimasi seperti Matlab.
## 1.2    Rumusan Masalah
Berdasarkan  latar  belakang  yang  telah  dibahas  sebelumnya,   didapat  rumusan
masalah pada tugas akhir ini adalah sebagai berikut.
-  Bagaimana  formulasi  model  Mean-Variance  untuk  menentukan  komposisi  utang
valuta  asing,  serta  bagaimana  ukuran  risiko  dirumuskan  menggunakan  model
Conditional   Value-at-Risk   (CVaR)   dan   Worst-Case   Conditional   Value-at-Risk
(WCCVaR)?
## 2

## 2.  Bagaimanahasilkomposisiutangvalutaasingyangoptimaldengan
mempertimbangkan   biaya   dan   risiko   menggunakan   formulasi   model   Mean-
Variance, Mean-CVaR, dan Mean-WCCVaR?
-  Bagaimana perbandingan hasil komposisi utang valuta asing yang dihasilkan oleh
formulasi model Mean-Variance, Mean-CVaR, dan Mean-WCCVaR?
## 1.3    Batasan Masalah
-  Data  yang  digunakan  dalam  penelitian  tugas  akhir  ini  adalah  perubahan  harian
suku  bunga  dan  nilai  tukar  (foreign  exchange)  mata  uang  USD,  EUR,  dan  JPY
pada periode 1 Januari 2021 hingga 24 November 2025.
-  Objek  analisis  dalam  penelitian  tugas  akhir  ini  dibatasi  pada  utang  valuta  asing
yang  berdenominasi  dolar  Amerika  Serikat  (USD),  euro  (EUR),  dan  yen  Jepang
## (JPY).
-  Faktor makroekonomi diabaikan.
## 1.4    Tujuan
Berdasarkan latar belakang dan permasalahan yang diangkat dalam penelitian tugas
akhir ini, terdapat beberapa tujuan yang disusun sebagai berikut.
-  Formulasi model Mean-Variance untuk menentukan komposisi utang valuta asing,
serta memformulasikan ukuran risikonya dengan model  Conditional  Value-at-Risk
(CVaR) dan Worst-Case Conditional Value-at-Risk (WCCVaR).
-  Menentukan komposisi utang valuta asing yang optimal dengan mempertimbangkan
biaya dan risiko menggunakan formulasi model Mean-Variance, Mean-CVaR, Mean-
WCCVaR.
-  Mengetahui perbandingan hasil komposisi utang valuta asing yang dihasilkan oleh
formulasi model Mean-Variance, Mean-CVaR, Mean-WCCVaR.
## 1.5    Manfaat
Berdasarkan tujuan yang telah disusun, maka penelitian tugas akhir ini diharapkan
dapat memberikan manfaat sebagai berikut
-  Memberikan kontribusi pada penerapan model optimasi penentuan komposisi utang
valuta asing.
-  Memberikan kontribusi dalam pengembangan penerapan metode pengukuran risiko,
khususnya  Conditional  Value-at-Risk  (CVaR) dan  Worst-Case  Conditional  Value-
at-Risk (WCCVaR) pada permasalahan penentuan komposisi utang valuta asing.
-  Memberikan  gambaran  perbandingan  kinerja  metode  Conditional  Value-at-Risk
(CVaR)  dan  Worst-Case  Conditional  Value-at-Risk  (WCCVaR)  dalam  mengelola
risiko utang valuta asing di bawah ketidakpastian.
-  Menjadi   bahan   pertimbangan   bagi   pengambil   keputusan   dalam   menentukan
komposisi utang valuta asing yang optimal dengan memperhatikan keseimbangan
antara biaya dan risiko.
## 3



## BAB II
## TINJAUAN PUSTAKA
## 2.1    Penelitian Terdahulu
Pembentukan  portofolio  utang  yang  baik  sangat  penting  bagi  sebuah  negara,
terutama ketika mengelola utang dalam mata uang asing yang memiliki banyak risiko,
seperti  perbedaan  tingkat  bunga,  kondisi  krisis  ekonomi,  dan  perbedaan  karakteristik
pasar  di  berbagai  negara.   Banyak  penelitian  telah  membahas  permasalahan  tersebut.
Misalnya,  penelitian  (D’Erasmo,  Mendoza,  &  Zhang,  2016)  yang  berjudul  “What  is  a
Sustainable Public Debt?” menjelaskan bahwa cara konvensional mengukur keberlanjutan
utang  memiliki  kekurangan.Oleh  karena  itu,  diperlukan  pendekatan  modern  yang
lebih lengkap untuk memahami kemampuan suatu negara dalam menyesuaikan kebijakan
keuangan dan menghadapi peningkatan utang publik.
Salah satu penelitian yang membahas portofolio utang optimal dengan pendekatan
modern   adalah   studi   oleh   Bianchi,    Hatchondo,   and   Martinez   (2018)   berjudul
“International  Reserves  and  Rol lover  Risk”.   Penelitian  tersebut  menggunakan  model
matematika  dengan  mempertimbangkan  surplus  primer  yang  ada  secara  eksternal,
struktur jatuh tempo utang, dan keputusan pemerintah dalam mengelola utang.  Temuan
mereka menyatakan bahwa strategi optimal dalam mengelola utang bertujuan mengurangi
pembayaran   bunga   secara   bersih   sekaligus   menghindari   risiko   gagal   bayar   akibat
melanggar batas keberlanjutan fiskal.
Seiring perkembangan waktu, banyak sekali model-model yang membahas mengenai
optimasi  portofolio.    Model  yang  paling  awal  dan  dikenal  sebagai  awal  mula  model
optimasi  portofolio  adalah  model  oleh  Markowitz  (1952).   Namun,  model  ini  memiliki
kelemahan  karena  bersifat  statis  dan  tidak  bisa  menangani  dinamika  pasar,   biaya
transaksi,   serta  berbagai  batasan  nyata  dalam  pengelolaan  portofolio.Studi  oleh
Kolm,  T ̈ut ̈unc ̈u,  and  Fabozzi  (2014)  yang  berjudul  ”60  years  of  portfolio  optimization:
Practical  chal lenges  and  current  trends”  dalam  studi  literaturnya  menegaskan  bahwa
praktik modern lebih sering meninggalkan model statis dan beralih ke pendekatan multi-
periode  yang  lebih  realistis.Meskipun  demikian,  pendekatan  ini  masih  menantang
karena membutuhkan estimasi parameter yang tepat, tingkat komputasi yang tinggi, dan
penyesuaian terhadap berbagai batasan portofolio nyata.
Sebagai jawaban atas kelemahan dalam model Markowitz, studi oleh Rockafellar et
al.  (2000)  yang  berjudul  “Optimization  of  Conditional  Value-at-Risk”,  yang membahas
pendekatan  baru  berbasis  minimisasi  Conditional  Value-at-Risk  sebagai  ukuran  risiko
yang   lebih   konsisten   dibandingkan   VaR   (Value-at-Risk).Mereka   memasukkan
analisis  risiko  ekor  (tail  risk),  serta  dapat  diterapkan  pada  portofolio  berskala  besar
melalui  pemrograman  linear  maupun  nonsmooth,  sehingga  lebih  relevan  untuk  praktik
manajemen risiko modern.  Ukuran risiko ini digunakan pada penelitian yang berjudul
”Analisis  Investasi  Saham  Sektor  Energi  Menggunakan  Metode  Value-at-Risk  (VAR)
dan Conditional  Value-at  -Risk  (CVAR) dengan Pendekatan Single Index Model:  Studi
Kasus Indeks LQ45 Tahun 2025” oleh Aisah, Santoso, and Rauf (2026) yang menyatakan
bahwa CVaR mampu melengkapi pengukuran VaR dengan menyoroti potensi kerugian
pada kondisi pasar terburuk,  sehingga menegaskan bahwa pendekatan kuantitatif yang
## 5

terintegrasi  mampu  menghasilkan  portofolio  yang  efisien  dan  relatif  tahan  terhadap
guncangan  ekstrem.   Selain  itu,  penelitian  berjudul  ”Risk  Measurement  of  Investment
Portfolio Using VaR and CVaR from the Top 10 Traded Stocks on the IDX ” oleh Rusyn
et  al.  (2024)  juga  menyatakan  bahwa  CVaR  sebagai  alat  evaluasi  risiko  memberikan
perspektif yang lebih komprehensif daripada VaR.
Model Conditional  Value-at-Risk  kemudian diubah untuk digunakan dalam analisis
portofolio  utang  pemerintah,  salah  satunya  oleh  Zenios  et  al.  (2019)  yang  berjudul
”Risk  Management  for  Sovereign  Debt  Financing  with  Sustainability  Conditions”.  Hasil
penelitian menunjukkan bahwa strategi pembiayaan berdasarkan memberikan hasil yang
lebih  baik  dibandingkan  pendekatan  sederhana.   Kini,  pendekatan  tersebut  digunakan
dalam alat analisis European Stability Mechanism (ESM) untuk mengevaluasi kemampuan
bayar dan keberlanjutan utang negara anggota.
Namun,   berbagai  model  tersebut  masih  memiliki  kekurangan,   terutama  ketika
informasi  mengenai  distribusi  probabilitas  aset  terbatas  atau  tidak  pasti.Untuk
mengatasi  hal  ini,   studi  oleh  Zhu  and  Fukushima  (2009)  yang  berjudul  “Worst-
Case   Conditional   Value-at-Risk   with   Application   to   Robust   Portfolio   Management”
memperkenalkan  pengembangan  menuju   Robust   Optimization  dengan  menggunakan
Robust   Risk   Measurement   yang   memenuhi   sifat   konveks   dan   koheren.Mereka
memasukkan  berbagai  bentuk  ketidakpastian  distribusi,  seperti  mixture  distribution
uncertainty, box uncertainty, dan el lipsoidal uncertainty.
Berdasarkan    kajian    terhadap    berbagai    penelitian    terdahulu,Gambar    2.1
menampilkan kerangka alur tinjauan pustaka yang memperlihatkan keterkaitan antara
metodologi dan fokus penelitian yang mendasari penyusunan Tugas Akhir ini.
Gambar 2.1    State of The Art Penelitian
## 6

## 2.2    Utang Valuta Asing
Menurut  Peraturan  Pemerintah  Republik  Indonesia  Nomor  2  Tahun  2006  tentang
cara  mengadakan  pinjaman  dan/atau  menerima  bantuan  serta  mengalirkan  pinjaman
dan/atau  bantuan  dari  luar  negeri,  utang  atau  pinjaman  adalah  setiap  penerimaan
negara dalam bentuk apa pun, seperti valuta asing, valuta asing yang diubah ke rupiah,
rupiah, barang, atau jasa, yang diperoleh dari pemberi pinjaman luar negeri dan harus
dibayar kembali sesuai syarat tertentu (Pemerintah Republik Indonesia, 2006).  Definisi
ini  selaras  dengan  publikasi  Statistik  Utang  Luar  Negeri  Indonesia,  yang  menyatakan
bahwa pinjaman valuta asing mencakup semua penerimaan negara dalam bentuk tersebut
yang memiliki kewajiban untuk dibayar kembali sesuai perjanjian yang disepakati.  Utang
merupakan salah satu pilihan pembiayaan negara yang dipilih berdasarkan pertimbangan
yang masuk akal, baik yang bersifat darurat maupun untuk pengembangan (Indonesia,
## 2021).
Selain    itu,utang    valuta    asing    juga    berperan    penting    dalam    mengatasi
ketidakseimbangan antara ekspor dan impor serta menyediakan tambahan valuta asing
ketika  hasil  ekspor  belum  cukup  untuk  menunjang  kebutuhan  modal  pembangunan
nasional  (Fedihartono,  Virjannah,  &  Yasin,  2023).Dalam  konteks  tersebut,  valuta
asing  memiliki  peran  penting  dalam  menentukan  daya  saing  perdagangan  Indonesia  di
pasar internasional, terutama karena fluktuasi nilainya dapat memengaruhi biaya impor,
pendapatan dari ekspor, serta kestabilan ekonomi secara keseluruhan (Insulinde Yuliyati,
## 2023).
2.3    Model Mean-Variance
Model mean-variance diperkenalkan oleh Markowitz (1952) merupakan pendekatan
paling klasik digunakan untuk optimasi portofolio.  Dengan mengasumsikan terdapat N
aset dengan tingkat expected return μ = (μ
## 1
## ,...,μ
## N
) dan matriks kovarians pengembalian
Σ, model MV dengan fungsi objektif berupa meminimumkan risiko portofolio berdasarkan
x
## ⊤
Σ x dapat dimodelkan sebagai berikut.
## Meminimumkan
x
x
## ⊤
Σ x
dengan kendala   1
## ⊤
x = 1,
μ
## ⊤
x≥ μ
min
## ,
x≥ 0,
## (2.1)
dengan keterangan:
Σ:  matriks kovarians return aset,
x:  vektor bobot portofolio (x
## 1
## ,x
## 2
## ,...,x
n
## )
## ⊤
## ,
μ:  vektor ekspektasi return aset (μ
## 1
## ,μ
## 2
## ,...,μ
n
## )
## ⊤
## ,
μ
min
:  tingkat return minimum portofolio yang disyaratkan,
1:  vektor satuan berdimensi n.
## 2.4    Return
Pada  dunia  investasi,  penilaian  kinerja  suatu  portofolio  tidak  terlepas  dari  peran
return  sebagai  salah  satu  aspek  utamanya.   Terdapat  beberapa  komponen  return  yang
menjadi  bagian  dari  suatu  portofolio  di  antaranya  adalah  return  aset,  expected  return
aset, serta expected return portofolio.
## 7

## 2.4.1    Return Aset
Return aset adalah tingkat keuntungan yang dihasilkan oleh suatu aset selama periode
waktu tertentu (Cornuejols, Pe ̃na, & T ̈ut ̈unc ̈u, 2018). Sehingga, return dari aset portofolio
dapat diartikan sebagai hasil keuntungan investasi seorang investor pada periode tertentu.
Perhitungan linear nilai return aset dapat dirumuskan sebagai berikut:
r
i,t
= ln

## I
i,t
## I
i,t−1
## !
,  i = 1,...,m, t = 1, 2,...,n(2.2)
dengan keterangan:
r
i,t
:  tingkat pengembalian (rate of return) aset i pada periode waktu t,
## I
i,t
:  nilai total return aset i pada waktu t,
## I
i,t−1
:  nilai total return aset i pada periode sebelumnya (t− 1),
i:  indeks yang menunjukkan aset atau sekuritas tertentu,
t:  indeks yang menunjukkan periode waktu tertentu dalam rangkaian data historis.
## 2.4.2    Expected Return Aset
Expected return aset adalah nilai rata-rata dari distribusi probabilitas pengembalian
aset  di  masa  depan  (Cornuejols  et  al.,  2018).    Sehingga,  expected  return  aset  dapat
diartikan sebagai estimasi pengembalian yang diharapkan oleh investor.  Umumnya, nilai
ini diestimasi menggunakan data historis yang dirumuskan sebagai berikut:
## ̄r
i
## =
## 1
n
n
## X
t=1
r
i,t
,  i = 1,...,m, t = 1, 2,...,n(2.3)
dengan keterangan:
## ̄r
i
:  rata-rata aritmatika tingkat pengembalian aset i,
n :  jumlah total periode dalam data historis yang digunakan,
r
i,t
:  tingkat pengembalian aset i pada periode t.
## 2.4.3    Expected Return Portofolio
Expected  return  portofolio adalah rata-rata dari expected  return  masing-masing aset
pada suatu portofolio dengan keterangan bobot adalah proporsi dana yang diinvestasikan
pada tiap aset (Cornuejols et al., 2018).  Perhitungan nilai expected return suatu portofolio
dapat dirumuskan sebagai berikut:
E[x] = x
## 1
μ
## 1
+ x
## 2
μ
## 2
+··· + x
m
μ
m
## =
m
## X
i=1
x
i
μ
i
,  i = 1,...,m
dalam notasi matriks, persamaan tersebut ditulis sebagai berikut.
## E[x] =μ
## T
x(2.4)
dengan keterangan:
x
i
:  bobot dana yang diinvestasikan pada aset i,
μ
i
:  estimasi ekspektasi pengembalian untuk aset i,
n:  jumlah total aset yang menyusun portofolio,
μ:  vektor kolom yang memuat ekspektasi pengembalian tiap aset (μ
## 1
## ,...,μ
m
## ),
x:  vektor portofolio yang memuat bobot tiap aset (x
## 1
## ,...,x
m
## ).
## 8

## 2.5    Risiko
Selain  return,  terdapat  aspek  lainnya  yang  penting  dalam  penilaian  kinerja  suatu
portofolio  yaitu  risiko.   Risiko  pada  portofolio  adalah  ukuran  yang  mempresentasikan
potensi  kerugian  yang  mungkin  timbul  dari  suatu  investasi  (Elton,  Gruber,  Brown,  &
## Goetzmann, 2009).
## 2.5.1    Varian Aset
Varian  aset  merupakan  alat  ukur  volatilitas  atau  risiko  dari  tingkat  pengembalian
suatu  aset.   Nilai  ini  mencerminkan  seberapa  jauh  return  aset  menyimpang  dari  nilai
ekspektasinya (Cornuejols et al., 2018).  Umumnya, nilai ini dihitung menggunakan data
historis yang dirumuskan sebagai berikut:
σ
## 2
i
## =
## 1
n
n
## X
t=1
## (r
i,t
## −  ̄r
i
## )
## 2
,  i = 1,...,m, t = 1, 2,...,n(2.5)
dengan keterangan:
n:  jumlah total periode waktu dalam data historis yang digunakan,
r
i,t
:  tingkat pengembalian aset i pada periode waktu ke-t,
## ̄r
i
:  rata-rata aritmatika tingkat pengembalian aset i selama n periode.
## 2.5.2    Kovarian Aset
Selain varian, terdapat kovarian yang merupakan alat ukur hubungan statistik antara
pengembalian dua aset yang berbeda.  Nilai kovarian menyatakan bahwa apakah kedua
aset tersebut cenderung bergerak searah atau berlawanan arah (Cornuejols et al., 2018).
Nilai ini juga dihitung menggunakan data historis yang dirumuskan sebagai berikut:
cov(R
i
## ,R
j
## ) =
## 1
n
n
## X
t=1
## (r
i,t
## −  ̄r
i
## ) (r
j,t
## −  ̄r
j
),  i = 1,...,m, t = 1, 2,...,n(2.6)
dengan keterangan:
n:  jumlah total periode waktu dalam data historis yang digunakan,
r
i,t
:  tingkat pengembalian aset i pada periode t,
r
j,t
:  tingkat pengembalian aset j pada periode t,
## ̄r
i
:  rata-rata aritmatika tingkat pengembalian aset i selama n periode,
## ̄r
j
:  rata-rata aritmatika tingkat pengembalian aset j selama n periode.
## 2.5.3    Risiko Portofolio
Risiko portofolio mempertimbangkan hubungan antar aset melalui komponen varians
dan kovarians. Pada model mean-variance oleh (Markowitz, 1952), risiko portofolio diukur
menggunakan varians portofolio yang dirumuskan sebagai berikut:
Var[x] = x
## T
## Σx =
## X
i
## X
j
ρ
ij
σ
i
σ
j
x
i
x
j
,,  i = 1,...,m, j = 1, 2,...,m(2.7)
dengan keterangan:
x :  vektor bobot portofolio kolom yang memuat proporsi dana yang diinvestasikan pada
setiap aset (x
## 1
## ,...,x
m
## )
## T
## ,
x
## T
:  transpose dari vektor bobot portofolio x,
Σ :  matriks kovarians simetris berukuran m× m.
## 9

sedangkan Σ didefinisikan sebagai berikut:
## Σ =
## 
## 
## 
## 
## 
## 
σ
## 2
## 1
σ
## 12
··· σ
## 1m
σ
## 21
σ
## 2
## 2
··· σ
## 2m
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
m1
σ
m2
···  σ
## 2
m
## 
## 
## 
## 
## 
## 
Elemen diagonal utama dari matriks Σ berupa σ
## 2
i
yang merepresentasikan varian return
masing-masing aset, sehingga Σ dikenal sebagai matriks varian–kovarian.
## 2.6    Robust Risk Measurement
Robust  Risk  Measurement  didefinisikan  sebagai  sekumpulan  ukuran  risiko  nominal
serta suatu himpunan ketidakpastian pada ukuran probabilitas yang memengaruhi proses
acak.  Prinsip-prinsip sebagai syarat utama dalam pendefinisian ukuran risiko robust yaitu
ukuran risiko yang digunakan bersifat konveks dan koheren.  Maka, yang pertama akan
diperkenalkan definisi dari ukuran risiko konveks dengan teorema oleh Fertis, Baes, and
L ̈uthi  (2012),  yaitu  misalkan  diberikan  suatu  ruang  probabilitas  (Ω,F, P),  di  mana  Ω
merupakan ruang sampel, F  adalah σ aljabar yang memuat kejadian-kejadian acak, dan
P  adalah  ukuran  probabilitas  pada F .   Selanjutnya,  misalkan L
## 1
(Ω,F, P)  menyatakan
kelas variabel acak yang terintegralkan.  Suatu pemetaan ρ  : L
## 1
(Ω,F, P) → R disebut
sebagai ukuran risiko konveks apabila memenuhi sifat-sifat sebagai berikut:
## 1.  Monotonicity:  Jika X
## 1
## ,X
## 2
## ∈ L
## 1
(Ω,F, P) dan X
## 1
## ≤ X
## 2
hampir pasti menurut P,
maka ρ(X
## 1
)≥ ρ(X
## 2
## ).
-  Translation  invariance:  Jika X,A ∈ L
## 1
(Ω,F, P) dan A = a hampir pasti, dengan
a∈ R, maka ρ(X + A) = ρ(X)− a.
## 3.  Convexity: Jika X
## 1
## ,X
## 2
## ∈ L
## 1
(Ω,F, P) dan 0≤ λ≤ 1, maka ρ
## 
λX
## 1
+ (1−λ)X
## 2
## 
m≤
λρ(X
## 1
) + (1− λ)ρ(X
## 2
## ).
Selanjutnya, suatu pemetaan ρ : L
## 1
(Ω,F, P) → R disebut sebagai ukuran risiko koheren
apabila merupakan ukuran risiko konveks dan juga memenuhi sifat Positive homogeneity
yaitu,  Jika X ∈ L
## 1
(Ω,F, P)  dan λ ≥  0,  maka ρ(λX)  = λρ(X).   Gagasan  utama  dari
robust risk measurement adalah untuk menilai risiko terburuk yang mungkin terjadi ketika
setiap ukuran probabilitas dalam himpunan strategi dianggap mungkin terjadi (Fertis et
al., 2012).
2.7    Conditional Value-at-Risk (CVaR)
Value-at-risk   adalah  ukuran  risiko  yang  menyatakan  kerugian  maksimum  yang
mungkin  terjadi  pada  suatu  portofolio  dalam  periode  waktu  tertentu  dengan  tingkat
kepercayaan  tertentu.    Berdasarkan  definisi  pada  suatu  tingkat  probabilitas  tertentu
β,  value-at-risk  (β-VaR)  dari  suatu  portofolio  didefinisikan  sebagai  jumlah  kerugian
minimum α  sedemikian  sehingga,  dengan  probabilitas β,  kerugian  tidak  akan  melebihi
α.   Sementara  itu, β-CVaR  didefinisikan  sebagai  nilai  harapan  bersyarat  dari  kerugian
yang melampaui nilai α tersebut (Rockafellar et al., 2000).
Masalah optimasi diawali dengan memisalkan f (x, y) notasi dari fungsi kerugian dan
y ∈ R  notasi  dari  variabel  acak  yang  memiliki  distribusi  probabilitas p(y).   Sehingga,
## 10

diasumsikan nilai ekspektasi absolutnya terbatas, yaitu
E [|f (x, y)|] < +∞
probabilitas  bahwa  nilai  fungsi  kerugian f (x, y)  tidak  melebihi  suatu  ambang  batas α
dapat dinyatakan sebagai
ψ(x,α) =
## Z
f(x,y)≤α
p(y)dy.
Oleh karena itu, β-VaR dapat didefinisikan sebagai nilai ambang batas minimum α
sehingga probabilitas terjadinya kerugian yang melebihi α tidak lebih besar dari β, yaitu
VaR
β
(x) = min{α∈ R  : ψ(x,α)≥ β}.(2.8)
Conditional  Value-at-Risk  (CVaR)  didefinisikan  sebagai  nilai  ekspektasi  kerugian
yang melebihi VaR
β
(x) (Ji, Huang, Xie, Zhou, & Zhou, 2018) dan dinyatakan sebagai
CVaR
α
## (x) = F
α
(x,γ) = γ +
## 1
1− α
## Z
(f (x, y)− γ)
## +
p(y)dy(2.9)
karena   perhitungan   langsung   CVaR
α
(x)   secara   eksplisit   tidak   mudah   dilakukan,
Rockafellar  et  al.  (2000)  memperkenalkan  suatu  fungsi  bantu  yang  bersifat  konveks
dan  kontinu  untuk  merepresentasikan  Conditional  Value-at-Risk  (CVaR)  lebih  mudah
dianalisis dengan dirumuskan sebagai berikut
## F
α
(x,γ) = γ +
## 1
1− α
## Z
(f (x, y)− γ)
## +
p(y)dy.(2.10)
Sehingga,  untuk meminimalkan nilai  Conditional  Value-at-Risk  (CVaR) dari suatu
portofolio,  cukup  meminimalkan  fungsi F
α
terhadap  portofolio x  dan  variabel  ambang
batas γ seacara bersamaan yang dapat ditulis sebagai berikut:
Meminimumkan CVaR
α
## (x) = Meminimumkan
x∈X,γ
## F
α
## (x,γ)
dari penjelasan tersebut berdasarkan (Cornuejols et al., 2018), menjelaskan bahwa model
portofolio dengan memaksimumkan imbal hasil yang diharapkan (μ
## T
x) dengan batasan
bahwa  risiko  CVaR
α
j
(x)  tidak  boleh  melampaui  toleransi  risiko U
α
j
dan  total  bobot
investasi harus berjumlah satu dituliskan sebagai berikut:
## Memaksimumkan
x
μ
## T
x
dengan kendala    CVaR
α
j
## (x)≤ U
α
j
,  j = 1,...,J
e
## T
x = 1.
## (2.11)
Model   CVaR
α
j
(x)   dapat   ditulis   ulang   dengan   mempertimbangkan   distribusi
probabilitas  kontinu  yang  seringkali  tidak  diketahui,  sehingga  fungsi F
α
diaprosimasi
menggunakan S jumlah skenario yang merupakan data historis. Hal ini mengubah integral
pada persamaan 2.10 menjadi bentuk penjumlahan rata-rata dari skenario-skenario yang
terdapat.  Model ini dapat ditulis sebagai berikut:
## Meminimumkanγ +
## 1
(1− α)S
## S
## X
s=1
(f (x, y
s
)− γ)
## +
## 11

untuk   menyelesaikan   persamaan   tersebut,    diperkenalkan   variabel   bantu   untuk
menggantikan fungsi maksimum, sehingga persamaan dapat ditulis sebagai berikut:
## Meminimumkan
x,z,γ
γ +
## 1
(1− α)S
## S
## X
s=1
z
s
dengan kendala  z
s
## ≥ 0,
z
s
≥ f (x,y
s
)− γ,  s = 1,...,S
x∈ X
apabila fungsi kerugian bersifat linear terhadap x, maka persamaan menjadi bentuk linear
programming yang dapat ditulis sebagai berikut:
## Memaksimumkan
x
μ
## T
x
dengan kendala  γ +
## 1
(1− α
j
## )S
## S
## X
s=1
z
s
## ≤ U
α
j
## ,
z
s
## ≥ 0,
z
s
≥ f (x,y
s
)− γ,
x∈ X.
## (2.12)
dengan keterangan:
x:  vektor bobot portofolio,
μ
## T
x:  ekspektasi imbal hasil portofolio,
γ:  parameter ambang batas yang merepresentasikan nilai VaR,
α
j
:  tingkat kepercayaan ke-j,
S:  jumlah total skenario,
z
s
:  variabel bantu yang merepresentasikan kerugian melebihi ambang γ pada skenario s,
f (x,y
s
) :  fungsi kerugian portofolio x pada skenario s,
y
s
:  vektor faktor risiko pada skenario ke-s,
## U
α
j
:  batas atas CVaR yang dapat ditoleransi pada tingkat kepercayaan α
j
## ,
X:  himpunan kendala kelayakan portofolio.
2.8    Worst-Case Conditional Value-at-Risk (WCCVaR)
Worst-Case  Conditional  Value-at-Risk  adalah  model  Robust  Optimization  untuk
ukuran  risiko  berbasis  VaR.  Dengan  fungsi  densitas  probabilitas  dari  return  portofolio
p∈ R, Zhu and Fukushima (2009) mendefinisikan worst-case CVaR sebagai berikut:
WCCVaR
β
(w) = sup
## F∈D
CVaR
β
(w) = sup
## F∈D
min
α
## H
β
## (w).
Dengan spesifikasi tersebut, maka worst-case CVaR dinyatakan sebagai berikut:
WCCVaR
β
(w) = min
α
sup
## F∈D
## H
β
## (w)
Diketahui  bahwa
c
## H
β
(w,α)  pada  persamaan    (2.12)  bersifat  konveks  terhadap  (w,α)
apabila f (w,y)   konveks   terhadap  w.Berdasarkan   fakta   bahwa   fungsi g(t)   =
max{g
## 1
## (t),g
## 2
(t)}  bersifat  konveks  jika  kedua  fungsi g
## 1
(t)  dan g
## 2
(t)  konveks,  maka
diperoleh bahwa jika f (w,y) konveks terhadap w, maka H
β
(w,α) juga konveks terhadap
## 12

(w) (Tang & Ling, 2014).
Oleh karena itu, (Tang & Ling, 2014) menjelaskan bahwa model portofolio dengan
memaksimumkan  imbal  hasil  yang  diharapkan  (μ
## T
w)  dengan  batasan  bahwa  risiko
WCCVaR
β
(w) tidak boleh melampaui toleransi risiko τ  dan total bobot investasi harus
berjumlah satu dituliskan sebagai berikut:
## Memaksimumkan
w
μ
## T
w
dengan kendala    WCCVaR
β
(w)≤ τ
e
## T
w = 1.
## (2.13)
Berdasarkan  (Tang  &  Ling,  2014),  memformulasikan  bentuk  WCCVaR
β
(w)  pada
kasus fungsi kerugian yang bersifat linier.  Formula ini memanfaatkan informasi matriks
kovarians  Σ  dan  vektor  rata-rata  imbal  hasilμ  sehingga  pengukuran  risiko  worst-case
dapat  dilakukan  tanpa  memerlukan  asumsi  mengenai  bentuk  distribusi  probabilitas
tertentu.  Sehingga dapat ditulis sebagai berikut:
WCCVaR
β
## (w) = Meminimumkan
α∈R
## (
α +
## 1
2(1− β)
## 
q
w
## T
## Σw + (μ
## T
w + α)
## 2
## − (μ
## T
w + α)
## 
## )
nilai α optimal yang meminimumkan persamaan tersebut diperoleh sebagai berikut:
α
## ∗
## =−μ
## T
w +
## 2β− 1
2β(1− β)
## √
w
## T
## Σw
nilai α
## ∗
merupakan parameter penentu Value-at-Risk yang diperlukan untuk mencapai
bentuk  solusi  tertutup  dari  risiko  WCCVaR
β
(w).Berdasarkan  formulasi  tersebut
Diketahui  bahwa  w  merupakan  vektor  bobot  portofolio  yang  menyatakan  proporsi
dana  yang  dialokasikan  pada  setiap  aset,   sedangkanμ
## T
w  menyatakan  ekspektasi
imbal  hasil  portofolio  yang  diperoleh  dari  kombinasi  bobot  aset  dan  ekspektasi  imbal
hasilnya.  Parameter β merupakan tingkat kepercayaan (confidence level) yang digunakan
dalam  pengukuran  risiko,   dan  Σ  adalah  matriks  kovarians  imbal  hasil  aset  yang
menggambarkan hubungan risiko antar aset. Selanjutnya,
q
β
## 1−β
w
## T
Σw merepresentasikan
ukuran risiko portofolio berbasis WCCVaR, τ  menyatakan batas maksimum risiko yang
dapat  ditoleransi  investor,  serta  kendala e
## T
w  =  1  memastikan  bahwa  seluruh  dana
diinvestasikan sehingga total bobot portofolio bernilai satu.  Sehingga, persamaan  (2.13)
dapat ditulis ulang sebagai berikut:
## Memaksimumkan
w
μ
## T
w
dengan kendala −μ
## T
w +
s
β
1− β
w
## T
Σw≤ τ
e
## T
w = 1.
## (2.14)
Oleh  karena  itu,  berdasarkan  persamaan   (2.14)  bahwa  kendala −μ
## T
w +
## √
w ≤
τ  memastikan  bahwa  risiko  WCCVaR
β
(w)  tidak  melampaui  toleransi  risiko τ  yang
ditetapkan  investor,  sedangkan  kendala e
## T
w   =   1  menjamin  bahwa  seluruh  bobot
portofolio teralokasi secara penuh. Variabel w merupakan vektor keputusan yang memuat
bobot masing-masing aset, sementaraβ adalah tingkat kepercayaan dan Σ adalah matriks
kovarians imbal hasil aset.
## 13

Penelitian yang dilakukan oleh Zhu and Fukushima (2009) juga menunjukkan bahwa
pendekatan  minimisasi  worst-case  CVaR  mampu  menangani  ketidakpastian  distribusi
probabilitas secara efektif.  Hasil penelitian tersebut menunjukkan bahwa dibandingkan
dengan  CVaR,  worst-case  CVaR  memiliki  kinerja  yang  lebih  tangguh  dalam  praktik
optimasi  saham.Selain  itu,   Zhu  and  Fukushima  (2009)  juga  menyatakan  bahwa
peningkatan  tingkat  risiko  umumnya  diikuti  oleh  peningkatan  imbal  hasil,  khususnya
dalam bentuk imbal hasil pada kondisi terburuk.  Oleh karena itu, pendekatan worst-case
CVaR berfokus pada optimisasi portofolio melalui analisis strategi terburuk dari sisi risiko
dan imbal hasil.
## 2.9    Quadratic Programming
Quadratic  Programming  (QP) adalah suatu permasalahan optimasi di mana fungsi
objektifnya bersifat kuadratik dan kendalanya bersifat linear.  Permasalahan seperti ini
juga  sering  muncul  sebagai  bagian  dari  langkah  penyelesaian  dalam  berbagai  metode
optimasi  dengan  batasan,  misalnya  pada  metode  sequential  quadratic  programming,
metode augmented lagrangian, dan metode titik interior (Nocedal, 2006).
Suatu permasalahan quadratic programming umum dapat dinyatakan sebagai berikut:
Meminimumkan  f (x) =
## 1
## 2
x
## T
Qx + c
## T
x
dengan kendala  Ax = b,
Dx≤ g,
## (2.15)
dengan keterangan:
x:  vektor berukuran n× 1, dengan x = [x
## 1
x
## 2
... x
n
## ]
## T
## ,
Q:  matriks simetris berukuran n× n,
c:  vektor berukuran n× 1,
A:  matriks berukuran m× n,
b:  vektor berukuran m× 1,
D:  matriks berukuran p× n,
g:  vektor berukuran p× 1.
## 2.10    Interpolasi
Interpolasi  polinomial  merupakan  metode  yang  paling  umum  digunakan  untuk
memperkirakan  nilai-nilai  di  antara  titik  data  yang  diketahui  secara  pasti  (Chapra,
Canale, et al., 2011).  Bentuk umum dari suatu polinomial berorde ke-n adalah
f (x) = a
## 0
+ a
## 1
x + a
## 2
x
## 2
+··· + a
n
x
n
## .
Untuk n + 1 titik data, terdapat satu dan hanya satu polinomial berorde n yang melalui
seluruh  titik  tersebut.Interpolasi  polinomial  adalah  proses  menentukan  polinomial
unik  berorde n  yang  memuat n + 1  titik  data.   Polinomial  ini  selanjutnya  digunakan
sebagai suatu rumus untuk menghitung nilai-nilai antara (intermediate  values).  Bentuk
interpolasi yang paling sederhana adalah menghubungkan dua titik data dengan sebuah
garis  lurus.Teknik  ini  dikenal  sebagai   interpolasi   linier   (Chapra  et  al.,   2011).
Interpolasi  linear  adalah  metode  numerik  untuk  memperkirakan  nilai  atau  akar
suatu fungsi dengan menghubungkan dua titik yang telah diketahui menggunakan garis
lurus.    Metode  ini  digunakan  untuk  memperoleh  estimasi  yang  lebih  efisien  dengan
mempertimbangkan  besarnya  nilai  fungsi  pada  batas  interval,  sehingga  perkiraan  akar
cenderung lebih akurat dibandingkan metode biseksi (Chapra et al., 2011).  Titik potong
## 14

garis lurus dengan sumbu-x dapat diperkirakan sebagai berikut:
f (x
l
## )
x
r
− x
l
## =
f (x
u
## )
x
r
− x
u
## (2.16)
Persamaan  tersebut  kemudian  dapat  diselesaikan  untuk  memperoleh  nilai x
r
,  sehingga
diperoleh:
x
r
= x
u
## −
f (x
u
## ) (x
l
− x
u
## )
f (x
l
)− f (x
u
## )
## .(2.17)
dengan keterangan:
x
l
:  batas bawah interval pencarian akar,
x
u
:  batas atas interval pencarian akar,
x
r
:  perkiraan titik potong garis lurus dengan sumbu-x,
f (x
l
):  nilai fungsi f (x) pada titik x
l
## ,
f (x
u
):  nilai fungsi f (x) pada titik x
u
## .
## 15



## BAB III
## METODOLOGI
Pada bab ini, akan dijelaskan secara umum mengenai urutan pelaksanaan tugas akhir
dengan langkah-langkah yang dilakukan ditunjukkan pada diagram alir sebagai berikut:
## Gambar 3.1    Diagram Alir Penelitian
## 17

## 3.1    Studi Literatur
Pada tahap ini, akan dilakukan studi literatur yaitu mengumpulkan referensi-referensi
dari sumber terpercaya mengenai utang valuta asing, optimasi portofolio dengan mean-
variance, model conditional value-at-risk, dan model worst-case conditional value-at-risk.
## 3.2    Pengumpulan Data
Pada tugas akhir ini akan digunakan data berupa suku bunga dan nilai valuta asing
(foreign exchange) dari instrumen utang valuta asing.  Untuk, data suku bunga terdapat
tujuh  instrumen  yang  mendominasi  dan  tercatat  dalam  Kementerian  Keuangan,  yaitu
USD dengan waktu jatuh tempo 5 tahun, 10 tahun, dan 30 tahun, EUR dengan waktu
jatuh tempo 8 tahun dan 10 tahun, serta JPY dengan waktu jatuh tempo 5 tahun dan
10  tahun.   Sedangkan,  untuk  data  nilai  valuta  asing  (foreign  exchange)  terdapat  dua
instrumen, yaitu data nilai valuta asing USD/EUR dan USD/JPY. Data suku bunga dan
nilai valuta asing berada pada periode 1 Januari 2021 sampai dengan 24 November 2025
yang didapatkan dari pihak pertama yaitu DJPPR Kementerian Keuangan.
## 3.3    Prapemrosesan Data
Pada tahap ini, akan dilakukan prapemrosesan data sebagai langkah awal persiapan
data  sebelum  ke  langkah  pengolahan  data.   Langkah  ini  bertujuan  untuk  memastikan
kualitas data yang kurang akurat seperti, adanya data hilang (missing value), data ganda,
atau terdapat kesalahan (noise) pada data yang dapat memengaruhi hasil analisis.  Data
yang tidak sesuai kemudian diperbaiki.  Tahap ini penting dilakukan karena kualitas data
yang baik akan menghasilkan model yang lebih akurat dan reliabel.  Hasil dari tahap ini
berupa data yang bersih dan siap digunakan pada proses pengolahan selanjutnya.
## 3.4    Pengolahan Data
Pada tahap ini, akan dilakukan pengolahan data dari data awal berupa suku bunga
dan  nilai  valuta  asing  (foreign  exchange)  menjadi  data  pergerakan  total  biaya  yang
nantinya  akan  sebagai  informasi  untuk  penyelesaian  model  matematika.    Parameter-
parameter  yang  didapatkan  pada  tahap  pengolahan  data  ini  akan  digunakan  untuk
menggambarkan karakteristik imbal hasil dan risiko dari masing-masing instrumen utang.
Hasil pengolahan data ini menjadi masukan utama dalam proses formulasi model.
3.5    Formulasi Model Mean-Variance Komposisi Utang Valuta Asing
Pada tahap ini,  akan dilakukan formulasi model mean-variance untuk menentukan
komposisi utang valuta asing. Formulasi dilakukan dengan memperhatikan fungsi objektif
dan  kendala  dari  model  untuk  disesuaikan  dengan  kondisi  utang  valuta  asing.   Fungsi
objektif dirancang untuk meminimumkan biaya utang dengan mempertimbangkan tingkat
risiko  yang  dihadapi.   Selain  itu,  ditetapkan  berbagai  kendala,  seperti  batas  proporsi
alokasi dana dan total bobot portofolio.
## 3.6    Formulasi Kendala Risiko
Pada tahap ini, akan dilakukan formulasi pada kendala risiko model mean-variance.
Kendala  awal  yang  berupa  variance  diformulasi  menggunakan  model  ukuran  risiko
conditional  value-at-risk  (CVaR)  dan  worst-case  conditional  value-at-risk  (WCCVaR).
Formulasi  kendala  risiko  ini  diharapkan  mampu  memberikan  perlindungan  yang  lebih
baik  terhadap  fluktuasi  pasar  valuta  asing.   Dengan  demikian,  model  optimisasi  yang
diperoleh menjadi lebih adaptif dan realistis dalam pengelolaan utang valuta asing.
## 18

## 3.7    Formulasi Parameter Kendala
Pada  tahap  ini,  akan  dilakukan  formulasi  pada  nilai  kendala  batasan  bobot  dan
risiko.   Untuk  kendala  bobot,  tiap  instrumen  dibatasi  rentang  nilai  batas  bawah  dan
batas atas.  Rentang nilai tersebut diperoleh dari beberapa variasi aturan yang mengacu
pada ketentuan bobot yang ditetapkan oleh Kementerian Keuangan.  Sedangkan untuk
kendala risiko, nilai risiko dibatasi oleh nilai risiko maksimal.  Nilai ini didapatkan dengan
menyubtitusi asumsi bobot awal ke model risiko.
## 3.8    Penyelesaian Optimasi Model
Pada  tahap  ini,  model  yang  sudah  diformulasi  akan  diselesaikan  dengan  beberapa
variasi  rentang  nilai  bobot  per  instrumen  dan  beberapa  parameter  batasan  risiko
maksimal.   Perhitungan  dilakukan  menggunakan  aplikasi  MATLAB  dengan  hasil  yang
diharapkan  berupa  komposisi  utang  valas  optimal  dengan  expected  biaya  utang  paling
minimum
3.9    Analisis Hasil dan Pembahasan
Pada  tahap  ini,  akan  dilakukan  analisis  hasil  dari  penyelesaian  keseluruhan  model
dengan  beberapa  variasi  rentang  nilai  bobot  per  instrumen  dan  beberapa  parameter
batasan  risiko  maksimal.   Dari  keseluruhan  hasil  yang  didapat  akan  dilakukan  analisis
perbandingan,  terutama  pada  komposisi  utang  valas,  nilai  expected  total  biaya  utang,
dan nilai risikonya.
3.10    Penarikan Kesimpulan dan Saran
Pada   tahap   ini,   akan   dilakukan   penarikan   kesimpulan   terkait   perbandingan
hasil  perhitungan  menggunakan  model  batasan  risiko  Conditional  Value-at-Risk  dan
Conditional   Value-at-Risk   pada  beberapa  parameter.Selanjutnya,   akan  diberikan
saran untuk penelitian selanjutnya dan pemerintah untuk mempertimbangkan kebijakan
komposisi utang valuta asing.
## 3.11    Penyusunan Laporan Tugas Akhir
Keseluruhan rangkaian penelitian tugas akhir ini akan disusun secara sistematis pada
pembukuan  tugas  akhir  yang  mencakup  bab  pendahuluan,  tinjauan  pustaka,  metode
penelitian, pembahasan, dan kesimpulan serta saran.
## 19



## BAB IV
## HASIL DAN PEMBAHASAN
## 4.1    Pengumpulan Data
Pada tugas akhir ini akan digunakan data berupa suku bunga dan nilai valuta asing
(foreign exchange) dari instrumen utang valuta asing.  Untuk, data suku bunga terdapat
tujuh instrumen yang tercatat dalam Kementerian Keuangan, yaitu USD dengan waktu
jatuh tempo 5 tahun, 10 tahun, dan 30 tahun, EUR dengan waktu jatuh tempo 8 tahun
dan 10 tahun, serta JPY dengan waktu jatuh tempo 5 tahun dan 10 tahun.  Sedangkan,
untuk data nilai valuta asing (foreign exchange) terdapat dua instrumen, yaitu data nilai
valuta asing USD/EUR dan USD/JPY. Data suku bunga dan nilai valuta asing berada
pada  periode  1  januari  2021  sampai  dengan  24  november  2025  yang  didapatkan  dari
pihak  pertama  yaitu  DJPPR  Kementerian  Keuangan.   Berikut  merupakan  tabel  data
yang akan digunakan pada Laporan Tugas Akhir ini dengan keseluruhan data terlampir
pada Lampiran 2:
Tabel 4.1    Data Suku Bunga dan Nilai Valuta Asing
NoTanggal
Suku BungaNilai Valuta Asing
## USD5Y USD10Y USD30Y EUR7Y EUR10Y JPY5Y JPY10YUSD/EUR USD/JPY
11/1/20210,01264   0,02016   0,03064   0,00578   0,01044   0,00919  0,012510,8191103,4000
21/4/20210,01236   0,01975   0,03043   0,00564   0,01011   0,00919  0,012540,8162103,1500
31/5/20210,01234   0,01986   0,03046   0,00555   0,00993   0,00913  0,012470,8132102,7600
41/6/20210,01251   0,02023   0,03088   0,00539   0,00981   0,00914  0,012490,8114103,0700
51/7/20210,01330   0,02085   0,03179   0,00554   0,00983   0,00887  0,012390,8151103,8400
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
127611/24/20250,04231   0,04922   0,05348   0,03476   0,03991   0,01990  0,027080,8676156,6000
Untuk memperoleh gambaran yang lebih komprehensif, pergerakan keseluruhan data
suku bunga dan nilai valuta asing dapat diamati melalui grafik berikut:
## Gambar 4.1    Grafik Pergerakan Suku Bunga
## 21

Gambar 4.2    Grafik Pergerakan Nilai Valuta Asing USD/EUR
Gambar 4.3    Grafik Pergerakan Nilai Valuta Asing USD/JPY
## 4.2    Prapemrosesan Data
Setelah  didapatkan  data  suku  bunga  dan  nilai  valuta  asing,  selanjutnya  dilakukan
prapemrosesan data untuk untuk menghindari adanya data hilang (missing  value) yang
dapat memengaruhi hasil analisis.  Data hilang pada tugas akhir ini terdapat pada data
suku bunga EUR pada jatuh tempo (tenor) 10 tahun dari tanggal 1 Februari 2021 - 15
September  2021.   Prapemrosesan  data  menggunakan  persamaan  interpolasi  pada  2.17,
yaitu:
x
r
= x
u
## −
f (x
u
## ) (x
l
− x
u
## )
f (x
l
)− f (x
u
## )
sebagai contoh perhitungan prapemrosesan pada data hilang ke-2, diketahui bahwa nilai
sebelum data hilang (y
## 1
) adalah 0,967 pada periode x
## 1
= 1, sedangkan nilai setelah data
hilang (y
## 2
) adalah 1,352 pada periode x
## 2
= 165. Berdasarkan persamaan  (2.17), diperoleh
hasil sebagai berikut:
x
## 2
## = 1, 352−
## 0, 967 (1− 165)
## 1, 352− 0, 967
## ≈ 413, 088.
Hasil  dari  perhitungan  prapemrosesan  data  menggunakan  persamaan  interpolasi
linear dapat dilihat pada tabel berikut dengan keseluruhan data terlampir pada Lampiran
## 1:
## 22

Tabel 4.2    Hasil Prapemrosesan Data Suku Bunga EUR 10 Tahun
No.TanggalEUR10Y
## 11/29/20210,967
## 22/1/20210,972
## 32/2/20210,974
## 42/3/20210,975
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 1649/15/20210,1350
## 1659/16/20210,1352
## 4.3    Pengolahan Data
Setelah keseluruhan data suku bunga dan nilai valuta melalui prapemrosesan data,
selanjutnya  dilakukan  pengolahan  data  sebagai  informasi  dalam  penyelesaian  model
matematika.
## 4.3.1    Menghitung Total Biaya Utang
Berdasarkan data suku bunga dan nilai valuta asing pada instrumen ke-i dan periode
ke-t yang dinotasikan dengan IR
i,t
dan FX
j,t
,  akan dilakukan perhitungan total biaya
utang  pada  instrumen  ke-i  dan  periode  ke-t  yang  dinotasikan  dengan C
i,t
## .    Urutan
instrumen  ke-i  disesuaikan  dengan  Tabel  4.1  sehingga  instrumen  ke-1  adalah  USD
## 5Y
yaitu  USD  dengan  jatuh  tempo  (tenor)  5  tahun  dan  instrumen  ke-7  adalah  JPY
## 10Y
yaitu JPY dengan jatuh tempo (tenor) 10 tahun.
Dalam   pengelolaan   utang   valuta   asing,   pemerintah   tidak   hanya   menghadapi
kewajiban  pembayaran  bunga  yang  dipengaruhi  oleh  tingkat  suku  bunga,  tetapi  juga
risiko  yang  timbul  akibat  fluktuasi  nilai  tukar.   Faktor  (1 + IR
i,t
)  merepresentasikan
besarnya  kewajiban  pembayaran  utang  setelah  memperhitungkan  bunga  pada  periode
ke-t.  Sementara itu, FX
j,t
digunakan untuk mengonversi kewajiban tersebut ke dalam
mata uang domestik sesuai dengan nilai tukar yang berlaku.  Dengan demikian, nilai C
i,t
menggambarkan total biaya utang yang harus ditanggung pemerintah dalam mata uang
domestik untuk setiap satu unit utang valuta asing pada periode ke-t.  Sehingga,  total
biaya dihitung menggunakan persamaan, yaitu:
## C
i,t
## = (1 + IR
i,t
## )× FX
j,t
,  i = 1,...,m, j = 1, 2, 3, t = 1,...,n
sebagai  contoh  perhitungan  total  biaya  utang  pada  data  ke-1  instrumen  ke-7  yaitu
## JPY
10Y, maka didapatkan hasil sebagai berikut:
## C
## 7,1
## = (1 + 0, 01251)× 103, 4000 = 104, 693534.
Hasil dari dari perhitungan total biaya utang dapat dilihat pada tabel berikut dengan
keseluruhan data terlampir pada Lampiran 3:
## 23

## Tabel 4.3    Data Perhitungan Total Biaya Utang
No.TanggalUSD5Y   USD10Y   USD30Y   EUR7Y   EUR10Y   JPY5Y   JPY10Y
## 11/1/20211,012641,020161,030640,823830,82765104,35025    104,69353
## 21/4/20211,012361,019751,030430,820800,82738104,09795    104,44350
## 31/5/20211,012341,019861,030460,817710,82723103,69820   104,041472
## 41/6/20211,012511,020231,030880,815770,82714104,01206    104,35734
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
## .
## .
## .
## .
## .
## .
## 1.27611/24/20251,042311,049221,053480,897760,85179159,71634    160,84073
## 4.3.2    Menghitung Tingkat Perubahan Total Biaya
Berdasarkan data total biaya dari ketujuh instrumen yang telah diperoleh, selanjutnya
akan  dilakukan  perhitungan  nilai  tingkat  perubahan  total  biaya  instrumen  ke-i  pada
periode  ke-t  yang  dinotasikan  dengan r
i,t
.   Perhitungan  tingkat  perubahan  total  biaya
utang menggunakan persamaan 2.2, yaitu:
r
i,t
= ln

## C
i,t
## C
i,t−1
## !
,  i = 1,...,m, t = 1, 2,...,n
sebagai  contoh  perhitungan  total  biaya  utang  pada  data  ke-1  instrumen  ke-7  yaitu
## JPY
10Y, digunakan nilai total biaya periode sebelumnya C
## 7,0
sebesar 104,693534 dan
nilai total biaya periode saat ini C
## 7,1
sebesar 104,696636.  Berdasarkan persamaan  (2.2),
diperoleh hasil sebagai berikut:
r
## 7,1
= ln

## 104, 69664
## 104, 69353
## !
## = 0, 00003.
Hasil  dari  dari  perhitungan  tingkat  perubahan  total  biaya  utang  menggunakan
persamaan   (2.2)  dapat  dilihat  pada  tabel  berikut  dengan  keseluruhan  data  terlampir
pada Lampiran 4.
## Tabel 4.4    Data Perhitungan Tingkat Perubahan Total Biaya Utang
No.TanggalUSD5Y   USD10Y   USD30Y   EUR7Y   EUR10Y   JPY5Y   JPY10Y
## 11/4/2021-0,000277-0,000402-0,000204-0,003686-0,000327-0,002421    -0,002391
## 21/5/2021-0,0000200,0001080,000029-0,003772-0,000178-0,003848    -0,003857
## 31/6/20210,0001680,0003630,000408-0,002375-0,0001190,0030220,003032
## 41/7/20210,0007800,0006080,0008820,0046990,0000200,0071750,007344
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
## .
## .
## .
## .
## .
## .
## 1.27611/24/2025-0,000470-0,000286-0,000199-0,001478-0,0000100,0005110,000511
## 4.3.3    Menghitung Mean Tingkat Perubahan Total Biaya
Berdasarkan   perhitungan   tingkat   perubahan   total   biaya   pada   masing-masing
instrumen utang, selanjutnya akan dilakukan perhitungan mean tingkat perubahan pada
masing-masing instrumen utang menggunakan persamaan  (2.3), yaitu:
## ̄r
i
## =
## 1
n
n
## X
t=1
r
i,t
,  i = 1,...,m, t = 1, 2,...,n
## 24

sebagai  contoh  perhitungan  mean  tingkat  perubahan  total  biaya  pada  instrumen  ke-7
yaitu  JPY10Y,  digunakan  jumlah  seluruh  tingkat  perubahan  total  biayanya  sebesar
0,429377  dengan  jumlah  periode  pengamatan  sebanyak  n  =  1.276.Berdasarkan
persamaan  mean  tingkat  perubahan,  diperoleh  hasil  untuk  mean  tingkat  perubahan
instrumen ke-7 sebagai berikut:
## ̄r
## 7
## =
## 1
## 1276
## 1276
## X
t=1
r
## 7,t
## =
## 0, 429377
## 1276
## = 0, 00033650.
Keseluruhan hasil dari perhitungan mean tingkat perubahan total biaya pada semua
instrumen dapat dilihat pada Tabel 4.5 berikut:
## Tabel 4.5    Mean Tingkat Perubahan Total Biaya
Inst.USD5YUSD10YUSD30YEUR7YEUR10YJPY5YJPY10Y
μ0.000022630.000022010.000017180.000067340.000022530.000333580.00033650
Nilai  mean  Tingkat  Perubahan  yang  bernilai  positif  menunjukkan  bahwa  secara
rata-rata  terjadi  peningkatan  total  biaya  utang  selama  periode  pengamatan.   Seluruh
instrumen memiliki nilai mean positif, yang mengindikasikan bahwa rata-rata total biaya
utang  pada  masing-masing  instrumen  cenderung  mengalami  kenaikan  dari  waktu  ke
waktu.   Instrumen  dengan  nilai  mean  tertinggi  yaitu  JPY
10Y,  sedangkan  instrumen
dengan nilai mean terendah yaitu USD30Y.
## 4.3.4    Menghitung Varians Tingkat Perubahan Total Biaya
Berdasarkan   perhitungan   tingkat   perubahan   total   biaya   pada   masing-masing
instrumen  utang,  selanjutnya  akan  dilakukan  perhitungan  varians  tingkat  perubahan
pada masing-masing instrumen utang menggunakan persamaan  (2.5), yaitu:
σ
## 2
i
## =
## 1
n
n
## X
t=1
## (r
i,t
## −  ̄r
i
## )
## 2
,  i = 1,...,m, t = 1, 2,...,n
sebagai contoh perhitungan varians tingkat perubahan total biaya pada instrumen ke-7
yaitu  JPY
10Y,  digunakan  jumlah  kuadrat  selisih  antara  tingkat  perubahan  total  dan
mean  tingkat  perubahan  total  sebesar  0,046889  dengan  jumlah  periode  pengamatan
sebanyak  n  =  1.276.   Berdasarkan  persamaan  varians  return,  diperoleh  hasil  sebagai
berikut:
σ
## 2
## 7
## =
## 1
## 1.276
## 1.276
## X
t=1
## (r
## 7,t
## −  ̄r
## 7
## )
## 2
## =
## 0, 046889
## 1276
## = 0, 00003675.
Keseluruhan  hasil  dari  perhitungan  varians  tingkat  perubahan  total  biaya  dapat
dilihat pada Tabel 4.6 berikut:
## Tabel 4.6    Varians Tingkat Perubahan Total Biaya
Inst.USD5YUSD10YUSD30YEUR7YEUR10YJPY5YJPY10Y
σ
## 2
## 0.000000190.000000300.000000250.000023000.000000090.000036940.00003675
Nilai  varians  tingkat  perubahan  yang  bernilai  relatif  kecil  menunjukkan  bahwa
tingkat  penyebaran  data  tingkat  perubahan  terhadap  nilai  rata-ratanya  cenderung
## 25

rendah, sehingga fluktuasi perubahan tingkat perubahan total biaya pada masing-masing
instrumen  selama  periode  pengamatan  tidak  terlalu  besar.Instrumen  dengan  nilai
varians tertinggi yaitu JPY
5Y, sedangkan instrumen dengan nilai varians terendah yaitu
USD30Y. Semakin besar nilai varians instrumen maka semakin tinggi risiko instrumen
tersebut.
## 4.3.5    Menghitung Standar Deviasi Total Biaya
Setelah  dilakukan  perhitungan  varians,  selanjutnya  dilakukan  perhitungan  standar
deviasi total biaya pada masing-masing instrumen utang menggunakan persamaan, yaitu:
σ
i
## =
s
## P
n
t=1
## (r
t=1
− μ
i
## )
## 2
n− 1
,  i = 1,...,m, t = 1,...,n
sebagai contoh perhitungan standar deviasi tingkat perubahan total biaya pada instrumen
ke-7  yaitu  JPY10Y,  digunakan  jumlah  kuadrat  selisih  antara  tingkat  perubahan  dan
mean tingkat perubahan sebesar 7,735009 dengan jumlah periode pengamatan sebanyak
n = 1.276.  Berdasarkan persamaan standar deviasi tingkat perubahan,  diperoleh hasil
sebagai berikut:
σ
## 2
## 7
## =
## 7, 735009
## 1.276
## = 0, 00033581.
Keseluruhan  hasil  dari  perhitungan  standar  deviasi  total  biaya  dapat  dilihat  pada
Tabel 4.7 berikut:
## Tabel 4.7    Varians Tingkat Perubahan Total Biaya
Inst.USD5YUSD10YUSD30YEUR7YEUR10YJPY5YJPY10Y
σ
## 2
i
## 0.000437560.000547670.000497450.004796350.000300780.006078240.00606192
Nilai  standar  deviasi  tingkat  perubahan  yang  relatif  kecil  menunjukkan  bahwa
tingkat  penyimpangan  data  tingkat  perubahan  terhadap  nilai  rata-ratanya  cenderung
rendah, sehingga fluktuasi tingkat perubahan total biaya pada masing-masing instrumen
selama periode pengamatan tidak terlalu besar.  Instrumen dengan nilai standar deviasi
tertinggi yaitu JPY
5Y, sedangkan instrumen dengan nilai standar deviasi terendah yaitu
EUR10Y.  Semakin  besar  nilai  standar  deviasi  suatu  instrumen  maka  semakin  tinggi
tingkat  risiko  instrumen  tersebut,  karena  pergerakan  return  yang  dihasilkan  semakin
tidak stabil.
4.3.6    Menghitung Matriks Varians-Kovarians
Setelah  dilakukan  perhitungan  varians  dan  standar  deviasi,  selanjutnya  dilakukan
perhitungan  kovarians  total  biaya  pada  masing-masing  instrumen  utang  menggunakan
persamaan  (2.5.3).  Hasil dari perhitungan matriks varians-kovarians dapat dilihat pada
matriks berikut:
## Σ = 10
## −5
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
## 0.019675   0.0205650.0182170.0296250.007774   0.031354   0.032002
## 0.020565   0.0307910.0246960.0336910.009365   0.039886   0.041086
## 0.018217   0.0246960.025393 −0.001408   0.008551   0.039466   0.040643
## 0.029625   0.033691 −0.0014082.3582920.016832   1.476108   1.472924
## 0.007774   0.0093650.0085510.0168320.009324   0.020767   0.021207
## 0.031354   0.0398860.0394661.4761080.020767   3.797976   3.781733
## 0.032002   0.0410860.0406431.4729240.021207   3.781733   3.777873
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
## 26

Sebagian besar antar instrumen memiliki nilai kovarians positif, hal ini menunjukkan
bahwa perubahan total biaya antar instrumen cenderung bergerak searah,  yaitu ketika
total biaya suatu instrumen meningkat maka instrumen lain juga cenderung meningkat.
Namun,  terdapat  pasangan  instrumen  dengan  nilai  kovarians  negatif,  yaitu  USD
## 30Y
dan EUR7Y yang menunjukkan bahwa perubahan total biaya kedua instrumen tersebut
bergerak  berlawanan  arah.   Semakin  besar  nilai  kovarians  positif  maka  semakin  kuat
hubungan  searah  antar  instrumen,   sedangkan  nilai  kovarians  negatif  menunjukkan
hubungan   yang   berlawanan   arah   dan   dapat   membantu   mengurangi   risiko   dalam
pembentukan komposisi utang.
## 4.3.7    Statistik Deskriptif
Selanjutnya dilakukan proses analisis statistik deskriptif.  Proses ini dilakukan untuk
memudahkan dalam memahami pola dan kondisi data sebelum dilakukan analisis lebih
lanjut.  Analisis statistik deskriptif dilakukan pada keseluruhan data tingkat perubahan
total biaya menggunakan persamaan 2.2.  Berikut tabel hasil analisis statistik deskriptif:
## Tabel 4.8    Hasil Analisis Statistik Deskriptif
## USD5YUSD10YUSD30YEUR7YEUR10YJPY5YJPY10Y
MIN-0.00313465-0.00465272-0.00349436-0.02278202-0.00322426-0.03865068-0.03883686
## MAX0.002943750.003035770.002926320.018454150.002874660.021996720.02205614
## MEAN0.000022630.000022010.000017180.000067340.000022530.000333580.00033650
## VAR0.000000190.000000300.000000250.000023000.000000090.000036940.00003675
## SD0.000437560.000547670.000497450.004796350.000300780.006078240.00606192
Berdasarkan  Tabel  4.8,  secara  deskriptif,  nilai  minimum  terendah  terdapat  pada
instrumen  JPY
10Y  dan  nilai  maksimal  tertinggi  terdapat  pada  instrumen  JPY10Y.
Seluruh  instrumen  memiliki  nilai  rata-rata  (mean)  yang  relatif  kecil  dan  mendekati
nol,  nilai  rata-rata  tertinggi  terdapat  pada  instrumen  JPY
10Y,  sedangkan  nilai  rata-
rata  terendah  terdapat  pada  instrumen  USD30Y.  Dari  sisi  penyebaran  data,  standar
deviasi  terbesar  terdapat  pada  instrumen  JPY5Y  standar  deviasi  terendah  terdapat
pada instrumen EUR
10Y. Selain itu, seluruh instrumen juga memiliki nilai varians yang
cenderung  kecil  dan  mendekati  nol.   Dari  hasil  analisis  tersebut  menunjukkan  bahwa
data total biaya memiliki fluktuasi yang relatif stabil selama periode pengamatan.  Untuk
memperoleh gambaran yang lebih jelas, hasil pergerakan total biaya dapat diamati pada
grafik berikut:
## Gambar 4.4    Grafik Pergerakan Tingkat Perubahan Total Biaya
## 27

4.4    Formulasi Model Mean-Variance untuk Komposisi Utang Valuta Asing
Berdasarkan  persamaan  2.1,   model  mean-variance  optimization  memiliki  fungsi
objektif berupa memaksimalkan keuntungan portofolio dengan membatasi risiko.  Model
ini  dapat  diadaptasi  untuk  komposisi  utang  valas  pemerintah.   Asumsikan μ  sebagai
tingkat perubahan dari total biaya utang dengan x
i
sebagai bobot per instrumen dan Σ
sebagai matriks kovarians tingkat perubahan instrumen.  Dengan demikian model awal
2.1 menjadi meminimumkan ekspektasi total biaya dengan risiko yang dibatasi.  Model
optimasi dapat ditulis sebagai berikut:
## Meminimalkan
x
μ
## T
x(4.1)
dengan kendala   x
## T
## Σx≤ R
max
## ,(4.2)
## 7
## X
i=1
x
i
## = 1,(4.3)
lb≤ x
i
≤ ub.(4.4)
Berdasarkan formulasi model tersebut, pertidaksamaan 4.2 memastikan bahwa risiko
dari tingkat perubahan total biaya tidak boleh melebihi batas risiko maksimal.  Untuk
persamaan 4.3 memastikan bahwa total bobot untuk ke-tujuh instrumen utang adalah
satu.    Terakhir,  untuk  pertidaksamaan  4.4  memastikan  bahwa  bobot  instrumen  ke-i
berada pada batas bawah dan batas atas yang telah ditentukan.
Model   mean-variance   merupakan   model   paling   sederhana   untuk   menentukan
portofolio.  Untuk membuat hasil menjadi lebih tangguh terhadap ketidakpastian biaya
utang, Laporan Tugas Akhir ini akan memperkenalkan dua model lainnya dengan ukuran
risiko yang berbeda-beda pada kendala setiap modelnya untuk menghasilkan model yang
lebih tangguh.  Formulasi kendala model akan dijelaskan pada bab berikutnya.
4.5    Formulasi Kendala Risiko Model Mean-Variance
Ukuran  risiko  diperlukan  untuk  menggambarkan  informasi  tentang  ketidakpastian
biaya utang di masa depan.  Pada tugas akhir ini, digunakan tiga model dengan ukuran
risiko yang berbeda-beda, yaitu model dengan kendala ukuran risiko berdasarkan variance
sesuai  dengan  Model  2.1,  ukuran  risiko  CVaR  pada  persamaan    (2.12),  dan  ukuran
risiko WC-CVaR pada persamaan   (2.14).  Untuk model pertama telah dijelaskan pada
bab  sebelumnya.    Sedangkan,  untuk  kedua  model  lainnya  akan  dijelaskan  pada  bab
berikutnya.
4.5.1    Kendala Risiko Conditional Value-at-Risk (CVaR)
Untuk model kedua yang diusulkan,  nilai CVaR akan dimasukkan sebagai kendala
yang dibatasi oleh nilai risiko maksimal yaitu R
max
.  Berdasarkan persamaan CvaR 2.12,
## 28

model kedua dapat ditulis sebagai berikut:
## Meminimalkan
x,z,γ
μ
## ⊤
x(4.5)
dengan kendala  γ +
## 1
(1− α
j
## )S
## S
## X
s=1
z
s
## ≤ R
max
,  j = 1,...,J,(4.6)
z
s
≥ 0,  s = 1,...,S,(4.7)
z
s
≥ f (x,y
s
)− γ,  s = 1,...,S,(4.8)
## 7
## X
i=1
x
i
## = 1,(4.9)
lb≤ x
i
≤ ub.(4.10)
## Berdasarkanformulasimodeltersebut,padabagiankendalapertama,
pertidaksamaan  4.6  memastikan  bahwa  nilai  CVaR  dari  ekspektasi  total  biaya  utang
tidak boleh melebihi batas risiko maksimal, yaitu R
max
, dengan γ  adalah nilai ambang
batas, α adalah tingkat kepercayaan untuk strategi ke-j, s adalah jumlah strategi, dan
z
s
adalah  variabel  bantu.   Variabel  bantu  pada  kendala  pertidaksamaan  4.7  dan  4.8
memastikan bahwa nilainya non-negatif dan harus lebih besar atau sama dengan selisih
antara biaya aktual f (x,y
s
) pada strategi ke-s dan nilai ambang batas γ.  Untuk kendala
keempat dan kelima, persamaan 4.9 dan pertidaksamaan 4.10 disamakan pada model 4.3
dan 4.4.
4.5.2    Kendala Risiko Worst-case Conditional Value-at-Risk (W-CVaR)
Untuk  model  ketiga  yang  diusulkan,  nilai  WC-CVaR  akan  dimasukkan  sebagai
kendala yang dibatasi oleh nilai risiko maksimal yaitu R
max
. Berdasarkan persamaan WC-
CVaR 2.14, ukuran risiko ini merupakan pengembangan dari CVaR yang lebih tangguh.
Bentuk model ketiga dapat ditulis sebagai berikut:
## Meminimalkan
x
μ
## ⊤
x(4.11)
dengan kendala − μ
## T
x +
s
β
1− β
## √
x
## T
## Σx≤ R
max
## ,(4.12)
## 7
## X
i=1
x
i
## = 1,(4.13)
lb≤ x
i
≤ ub.(4.14)
## Berdasarkanformulasimodeltersebut,padabagiankendalapertama,
pertidaksamaan 4.12 memastikan bahwa nilai WC-CVaR dari ekspektasi total biaya tidak
boleh melebihi batas risiko maksimal, yaitu R
max
, dengan −μ
## ⊤
x adalah nilai negatif dari
ekspektasi total biaya utang,
s
β
1− β
adalah faktor skala yang bergantung pada tingkat
kepercayaan β,  dan
## √
x
## T
Σx  adalah  standar  deviasi  portofolio  yang  merepresentasikan
risiko dalam kondisi distribusi total biaya terburuk dari seluruh kemungkinan distribusi
yang memiliki rata-rata total biaya μ dan matriks kovarians Σ yang sama.  Untuk kendala
kedua dan ketiga, persamaan 4.13 dan pertidaksamaan 4.14 disamakan pada model 4.3
dan 4.4.
## 29

4.6    Penentuan Kendala Batas Atas dan Batas Bawah Instrumen
Pada  bab  sebelumnya  telah  diformulasikan  kendala  risiko  pada  ketiga  model  yang
diusulkan.   Selanjutnya,  akan  diformulasikan  untuk  kendala  batas  bawah lb  dan  batas
atas ub bobot per instrumen utang pada pertidaksamaan 4.4, pertidaksamaan 4.10, dan
pertidaksamaan  4.14.   Pada  tugas  akhir  ini  akan  menggunakan  lima  pilihan  strategi
kendala batas bawah lb dan batas atas ub bobot per instrumen aset.
Strategi pertama menggunakan batas bawah (lb) dan batas atas (ub) dari kebijakan
asli  Kementerian  Keuangan.    Strategi  ini  dihitung  dari  proporsi  existing  2024  yang
ditambah  atau  dikurangi  dengan  nilai  delta.    Nilai  delta  diperoleh  dari  selisih  data
max-min proporsi outstanding utang valuta asing pada tahun 2022 sampai dengan 2024.
Keseluruhan data proporsi existing 2024 dapat dilihat pada tabel berikut:
Tabel 4.9    Proporsi Existing (2024) dan Batas Instrumen
## Instrument
## Proporsi
## Existing (2024)
DeltaLbUb
## USD5Y45,95%3,00%42,50%49,00%
## USD10Y11,36%1,00%10,00%12,50%
## USD30Y14,78%1,50%13,00%16,50%
## EUR7Y14,39%1,00%13,00%15,50%
## EUR10Y2,44%0,50%1,50%3,00%
## JPY5Y6,67%1,50%5,00%8,50%
## JPY10Y4,41%1,00%3,00%5,50%
Dikarenakan proporsi dari Tabel 4.9 ini masih memiliki keterbatasan pada rentang
interval  dan  masih  berdenominasi  pada  instrumen  USD.  Oleh  karena  itu,  diperlukan
modifikasi batasan kebijakan asli ini menjadi berbagai strategi alokasi yang lebih beragam,
sehingga memberikan gambaran yang lebih komprehensif tentang bagaimana perubahan
komposisi dapat memengaruhi hasil perhitungan.
Strategi  kedua  memodifikasi  batas  bawah  (lb)  dan  batas  atas  (ub)  dari  kebijakan
asli Kementerian Keuangan dengan memperlebar intervalnya sebesar 0,015 ke batas atas
dan batas bawah.  Lalu, strategi ketiga memodifikasi dengan mempersempit bobot USD
sebesar  0,05  dan  memperlebar  bobot  EUR  dan  JPY  sebesar  0,05.   Terakhir,  strategi
keempat menggunakan proporsi existing 2024 sebagai nilai tengah interval batasan bobot
per instrumen dengan lebar interval sebesar 0,04.
Untuk  pertimbangan  lainnya,  ditambahkan  strategi  kelima  yaitu  batasan  bobot
menggunakan  batasan  paling  umum  pada  model  optimasi,  yaitu  bobot  per  instrumen
tidak boleh negatif dan berada pada interval [0, 1] karena total bobot dari keseluruhan
instrumen adalah 1.  Artinya, pada strategi ini tidak ada aturan khusus pada pembobotan
instrumen utang.  Keseluruhan strategi batasan bobot per instrumen dapat dilihat pada
tabel berikut:
## 30

Tabel 4.10    Strategi variasi batasan bobot untuk tiap instrumen
## Inst.
Strategi 1Strategi 2Strategi 3Strategi 4Strategi 5
lbublbublbublbublbub
## USD5Y0,430,490,410,510,380,440,440,480,001,00
## USD10Y0,100,130,090,140,050,080,090,130,001,00
## USD30Y0,130,170,120,180,080,120,130,170,001,00
## EUR7Y0,130,160,120,170,180,210,050,090,001,00
## EUR10Y0,020,030,000,050,070,080,020,060,001,00
## JPY5Y0,050,090,040,100,100,140,120,160,001,00
## JPY10Y0,030,060,020,070,080,110,000,040,001,00
4.7    Penentuan Nilai Risiko Maksimal (R
max
) pada Kendala Model
Dari kelima strategi batasan bobot pada bab sebelumnya, selanjutnya akan dihitung
strategi variasi nilai risiko maksimal (R
max
) yang didapat dengan menyubtitusi dua asumsi
bobot yaitu asumsi pertama adalah bobot per instrumen diasumsikan sama rata, sehingga
dikarenakan  jumlah  instrumen  ada  tujuh  maka  tiap  instrumen  memiliki  bobot  seperti
berikut:
x =
## 
## 1
## 7
## 1
## 7
## 1
## 7
## 1
## 7
## 1
## 7
## 1
## 7
## 1
## 7
## 
sedangkan asumsi kedua adalah bobot sesuai dengan nilai existing  2024 pada Tabel 4.9
seperti berikut:
x =
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
## 0.4595
## 0.1136
## 0.1478
## 0.1439
## 0.0244
## 0.0667
## 0.0441
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
Kedua  asumsi  tersebut  masing-masing  disubtitusi  pada  ketiga  pertidaksamaan
kendala  bobot  yaitu  pertama,  pada  persamaan  kendala  4.2  pada  model  mean-variance
yaitu:
x
## T
## Σx = R
max
kedua, pada persamaan 4.6 sampai 4.8 pada model mean-CVaR dengan diubah menjadi
persamaan nonlinear agar mempermudah perhitungan dengan α sebesar 0,95 yaitu:
μ
p
= x
## T
μ =
n
## X
i=1
x
i
μ
i
σ
p
## =
## √
x
## T
Σx− μ
p
## +
φ(z
α
## )
1− α
σ
p
## = R
max
dan ketiga, pada persamaan 4.12 pada model mean-WCCVaR dengan nilai β sebesar 0,95
yaitu:
## −μ
## T
x +
s
β
1− β
## √
x
## T
## Σx = R
max
Sehingga keseluruhan perhitungan variasi nilai risiko maksimal (R
max
) dapat dilihat
pada tabel berikut:
## 31

Tabel 4.11    strategi variasi nilai risiko maksimal (R
max
## )
ModelAsumsiNilai Risiko Maksimal
Mean-Variance
sama rata0,000087271
existing0,000107219
Mean-CVaR
sama rata0,018430507
existing0,020512618
Mean-WCCVaR
sama rata0,039906568
existing0,044316912
Hasil yang diperoleh dari perhitungan ketiga model dengan beberapa strategi tersebut
nantinya akan dilakukan perbandingan untuk menentukan komposisi utang yang paling
optimal.
## 4.8    Penyelesaian Optimasi
Setelah didapatkan ketiga model formulasi untuk penentuan komposisi utang valuta
asing optimal dan nilai-nilai parameter pada kendala model selanjutnya akan dilakukan
penyelesaian optimasi pada masing-masing model menggunakan software matlab R2024a
yang akan dijelaskan pada bab berikutnya.
4.8.1    Penyelesaian Optimasi dengan Model Mean-Variance
Berdasarkan persamaan 4.1 sampai dengan 4.4, model optimasi mean-variance akan
dikerjakan menggunakan matlab dengan penyelesaian fmincon untuk meminimalkan total
biaya  dengan  kendala  risiko  yang  dibatasi.   Adapun  langkah-langkah  dari  penyelesaian
model tersebut sebegai berikut:
## 1.  Input Parameter
Pada  bab  sebelumnya,  telah  dihitung  nilai  mean  total  biaya  utang  dan  matriks
varians-kovarians  dari  total  biaya  instrumen  utang.    Kedua  nilai  tersebut  akan
diinisialisasi sebagai inputan dengan nilai mean yang direpresentasikan oleh vektor
mu dan matriks varians-kovarians direpresentasikan oleh matriks Sigma. Selanjutnya
variabel n diinisialisasi untuk membaca jumlah elemen dalam vektor mu.  Sehingga
tahap input parameter ditulis sebagai berikut:
1 mu = [0.00002263214878;
## 2        .
## 3        .
## 4        .
## 5        0.0003365025468];
## 6 Sigma = [0.0000001967544988      ...  0.0000003200220634;
## 7            0.0000002056519467      ...  0.0000004108635933;
## 8            0.0000001821664689      ...  0.0000004064263243;
## 9            0.0000002962494759      ...  0.00001472924079;
## 10            0.00000007773555672     ...  0.0000002120672048;
## 11            0.0000003135357379      ...  0.00003781733234;
## 12            0.0000003200220634      ...  0.00003777872643];
13 n = length(mu);
## 2.  Nilai Batas Bobot
Selanjutnya, batas bawah dan batas atas untuk tiap bobot per instrumen pada tabel
## 32

Tabel  4.10  diinisiaalisasi  melalui  variabel  lb  dan  ub.   Untuk  strategi  ke-1  sampai
dengan ke-4 dapat diinput nilai batas bawah dan batas atas secara berurutan untuk
tiap instrumennya.  Sebagai contoh strategi ke-1 dapat ditulis sebagai berikut:
1      lb = [0.425  0.10  0.103  0.13  0.015  0.05  0.03];
2      ub = [0.49  0.125  0.165  0.155  0.03  0.085  0.055];
sedangkan  untuk  strategi  ke-1,  dengan  rentang  bobot  untuk  semua  instrumen
adalah [0, 1] maka lb diinisialisasi sebagai vektor nol berukuran n×1 yang berarti
setiap aset memiliki bobot minimum sebesar 0, sedangkan ub diinisialisasi sebagai
vektor satu berukuran n×1 yang berarti setiap aset diperbolehkan memiliki bobot
maksimum sebesar 1.  Sehingga inisialisasi batas bobot untuk strategi ke-5 dapat
ditulis sebagai berikut:
1      lb = zeros(n,1);
2      ub = ones(n,1);
agar  total  bobot  seluruh  instrumen  pada  komposisi  tepat  berjumlah  1,  maka
diinisialisasi  kendala  kesamaan  (equality  constraint)  melalui  variabel Aeq  yaitu
vektor satu berukuran 1× n dan variabel beq yaitu bernilai skalar 1.  Selanjutnya,
agar algoritma memiliki titik awal yang tidak melanggar batasan,  maka dihitung
titik  awal feasible  melalui  variabel x0  dengan capacity  dihitung  sebagai  sisa
alokasi bobot sebelum terdistribusi, sehingga x0 diperoleh dengan mendistribusikan
sisa alokasi tersebut pada masing-masing aset dan dinormalisasi agar total bobot
seluruh instrumen tepat berjumlah 1.  Tahap ini dapat ditulis sebagai berikut:
1 Aeq = ones(1,n);
2 beq = 1;
3 capacity   = ub - lb;
4 remaining = 1 - sum(lb);
5 x0 = lb + capacity * (remaining / sum(capacity));
6 x0 = x0 / sum(x0);
## 3.  Nilai Batas R
max
Selanjutnya, nilai risiko maksimal atau (R
max
) pada Tabel 4.11 diinisialisasi melalui
variabel Rmaxlist.  Nilai (R
max
) diinput secara berurutan sebagai berikut:
## 1 Rmax_list = [0.000004969  0.000020269  0.004474733  0.009197278
## 0.009599414  0.019547159];
## 4.  Opsi Penyelesaian
Selanjutnya,  agar  algoritma  optimasi  dapat  berjalan  sesuai  dengan  model  mean-
variance yang ingin diselesaikan, maka diinisialisasi parameter opsi optimasi melalui
function optimoptions yang disimpan melalui variabel options.  Algoritma yang
dipilih  yaitu  Sequential  Quadratic  Programming  (sqp)  karena  mampu  menangani
permasalahan optimasi nonlinier dengan kendala kesamaan maupun ketidaksamaan.
Untuk toleransi fungsi objektif dan variabel keputusan masing-masing ditetapkan
sebesar 10
## −12
melalui variabel TolFun dan TolX. Selanjutnya untuk solver yang
digunakan yaitu  solver fmincon karena sesuai dengan fungsi objektif model yaitu
meminimumkan nilai total biaya utang.  Tahap ini dapat ditulis sebagai berikut:
## 33

1 options = optimoptions(’fmincon ’,’Algorithm ’, ...
2           ’sqp’,’Display ’,’off’,’TolFun ’, 1e-12,’TolX’, 1e-12);
-  Inisiasi Loop Optimasi setiap Nilai R
max
Selanjutnya,  dilakukan  iterasi  untuk  setiap  nilai  risiko  maksimal  (R
max
## ).    Hal
ini  dilakukan  agar  setiap  nilai R
max
dapat  diuji  secara  bergantian.Iterasi
dilakukan dengan perulangan for sejumlah elemen dalam Rmax
list dengan setiap
iterasi  ke-k  nilai  variabel Rmax  diambil  dari Rmaxlist.Selanjutnya,   fungsi
objektif diinisialisasi melalui variabel objfun dan kendala risiko diinisialisasi melalui
nonlcon.   Selanjutnya  model  optimasi  sesuai  persamaan  4.1  sampai  dengan  4.4
dihitung  menggunakan  solver fmincon  untuk  menghasilkan  bobot  optimal  yang
ditulis  dengan  variabel x
opt,  nilai  fungsi  objektif  dengan  variabel fval,  dan
indikator  keberhasilan  dengan  variabel exitflag.    Inisiasi  loop  optimasi  dapat
ditulis sebagai berikut:
1 for k = 1: length(Rmax_list)
## 2      Rmax = Rmax_list(k);
3      objfun = @(x) mu’ * x;
4      nonlcon = @(x) deal(x’ * Sigma * x - Rmax , []);
5      [x_opt , fval , exitflag] = fmincon(objfun , x0, [], [], Aeq
, beq , lb, ub, nonlcon , options);
## 6.  Cetak Hasil Akhir Optimasi
Selanjutnya,  pada  setiap  iterasi  akan  dihitung  dengan  beberapa  ukuran  kinerja
komposisi dari bobot optimal melalui variabel xopt.  Selanjutnya, untuk ekspektasi
total biaya dihitung melalui variabel expReturn, variance dihitung melalui variabel
variance,  dan  risiko  portofolio  melalui  variabel expRisk.   Seluruh  perhitungan
sesuai  dengan  model  mean-variance  pada  persamaan  4.1  sampai  dengan  4.4.
Seluruh hasil optimasi ditampilkan menggunakan function fprint dan disp dengan
penulisan 10 digit desimal %.10fn sebagai berikut:
1 expReturn = mu’ * x_opt;
2 variance = x_opt ’ * Sigma * x_opt;
3 expRisk    = sqrt(variance);
4 fprintf(’\n====  HASIL  MVO (Rmax = %.8f) ====\n’, Rmax);
5 disp(table ((1:n)’, x_opt , ’VariableNames ’, {’Aset’,’Bobot ’}))
6 fprintf(’Expected  Cost       : %.10f\n’, expReturn);
7 fprintf(’Risiko (std dev)    : %.10f\n’, expRisk);
8 fprintf(’Sum  Bobot            : %.6f\n’,   sum(x_opt));
Keseluruhan  hasil  dari  penyelesaian  optimasi  dengan  model  mean-variance  dapat
dilihat pada tabel berikut:
## 34

Tabel 4.12    Hasil Optimasi Model Mean-Variance
## R
max
Strategi 1Strategi 2Strategi 3Strategi 4Strategi 5
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
0.0000049690.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
0.0000202690.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
0.0044747330.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
0.0091972780.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
0.0095994140.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
0.0195471590.000052  0.0010770.000042  0.0008850.000086  0.0017740.000064  0.0010340.000017  0.000504
4.8.2    Penyelesaian Optimasi dengan Model Mean-CVaR
Untuk  menyelesaikan  model  kedua  yaitu  mean-CVaR  pada  persamaan  4.5  sampai
dengan  4.10  dapat  menggunakan  langkah-langkah  program  yang  sama  dengan  model
mean-variance.  Namun, pada model mean-CVaR terdapat parameter tambahan.
Pada  penambahan  parameter,  terdapat  tingkat  kepercayaan  (α)  ditulis  dengan
variabel alpha  dengan  nilai  0.95,  sedangkan  jumlah  strategi  CVaR  (S)  ditulis  dengan
variabel S dengan nilai 1000.  Selanjutnya untuk fungsi kerugan (Y) diinisialisasi sebagai
matriks data tingkat perubahan simulasi berukuran S×n yang dibangkitkan berdasarkan
distribusi  normal  multivariat  dengan  vektor  mean  melalui  variabel mu  dan  matriks
kovarians  melalui  variabel Sigma  menggunakan  function mvrnd.   Sehingga  setiap  baris
pada Y  merepresentasikan satu strategi tingkat perubahan dari seluruh instrumen yang
akan  digunakan  pada  perhitungan  risiko  selanjutnya.   Tahap  ini  dapat  ditulis  sebagai
berikut:
1 alpha = 0.95;
## 2 S      = 1000;
3 rng (42);
4 Y = mvnrnd(mu’, Sigma_psd , S);
Selanjutnya,  yang  menjadi  perbedaan  dari  penyelesaian  model  mean-variance  dan
mean-CVaR  adalah  pada  solver  yang  digunakan.Pada  algoritma  optimasi  mean-
CVaR  menggunakan  algoritma  interior-point  karena  mampu  menangani  permasalahan
optimasi linier berskala besar dengan kendala kesamaan maupun ketidaksamaan secara
efisien. Sehingga, diinisialisasi parameter opsi optimasi melalui fungsi optimoptions yang
disimpan dalam variabel options dengan algoritma yang dipilih yaitu interior-point.
Jumlah iterasi maksimum ditetapkan sebesar 10.000 melalui parameter MaxIterations
agar  algoritma  memiliki  ruang  iterasi  yang  cukup  untuk  mencapai  solusi  optimal.
Selanjutnya, solver yang digunakan yaitu linprog karena sesuai dengan formulasi model
mean-CVaR  yang  memiliki  fungsi  objektif  dan  kendala  yang  bersifat  linier  terhadap
variabel keputusan.  Tahap ini dapat ditulis sebagai berikut:
1 options = optimoptions(’linprog ’,’Algorithm ’,’interior -point’,
... ’Display ’, ’off’,’MaxIterations ’, 10000);
Karena solver  berbeda, maka tahap loop optimasi juga akan berbeda.  Selanjutnya,
dilakukan iterasi untuk setiap nilai risiko maksimal (R
max
) agar setiap nilai R
max
dapat
diuji  secara  bergantian.Iterasi  dilakukan  dengan  perulangan for  sejumlah  elemen
dalam Rmax
list dengan setiap iterasi ke-k nilai variabel Rmax diambil dari Rmaxlist.
Selanjutnya,   model  mean-CVaR  sesuai  dengan  persamaan  4.5  sampai  dengan  4.10
diinisialisasi melalui variabel f yang terdiri dari vektor mu sebagai komponen bobot aset,
## 35

skalar bernilai nol sebagai inisiasi variabel ambang batas gamma, dan vektor variabel bantu
zs berukuran S yang bernilai nol sebagai inisiasi awal.  Kemudian, kendala risiko pada
model mean-CVaR diinisialisasi melalui A
cvar dan bcvar yang memastikan nilai CVaR
tidak melebihi R
max
, sedangkan kendala variabel bantu zs diinisialisasi melalui Az dan
bz untuk memastikan setiap strategi kerugian terhitung dengan benar.  Seluruh kendala
ketidaksamaan kemudian digabungkan menjadi satu matriks A
ineq dan vektor bineq.
Tahap ini dapat ditulis sebagai berikut:
1 for k = 1: length(Rmax_list)
## 2      Rmax = Rmax_list(k);
3      f = [mu; 0; zeros(S,1)];
4      A_cvar = [zeros(1,n), 1, ones(1,S)/((1- alpha)*S)];
5      b_cvar = Rmax;
6      A_z = [-Y, ones(S,1), -eye(S)];
7      b_z = zeros(S,1);
8      A_ineq = [A_cvar; A_z];
9      b_ineq = [b_cvar; b_z];
Selanjutnya,   agar   seluruh   variabel   keputusan   memiliki   batas   yang   sesuai,   maka
diinisialisasi  batas  bawah  dan  batas  atas  seluruh  variabel  keputusan  melalui lb
all
dan uball  yang  mencakup  batas  bobot  aset,  variabel  gamma  yang  tidak  dibatasi,
serta  variabel  bantu z
s
yang  dibatasi  bernilai  tidak  negatif.   Kendala  kesamaan  total
bobot bernilai satu diinisialisasi melalui Aeqfull dan beqfull yang memastikan jumlah
seluruh bobot aset tepat bernilai satu.  Agar solusi optimal dapat diperoleh berdasarkan
seluruh  fungsi  objektif  dan  kendala  yang  telah  diinisialisasi,  maka  dijalankan  proses
optimasi menggunakan solver linprog yang menghasilkan vektor solusi w
opt, nilai fungsi
objektif fval,  dan  indikator  keberhasilan exitflag.   Tahap  ini  dapat  ditulis  sebagai
berikut:
1      lb_all = [lb;   -Inf; zeros(S,1)];
2      ub_all = [ub;    Inf; ones(S,1)*Inf];
3      Aeq_full = [ones(1,n), 0, zeros(1,S)];
4      beq_full   = 1;
5      [w_opt , fval , exitflag] = linprog(f, A_ineq , b_ineq , Aeq_full
, beq_full , lb_all , ub_all , options);
Selanjutnya,  agar  bobot  optimal  setiap  aset,  nilai  ambang  batas,  dan  variabel  bantu
dapat  digunakan  secara  terpisah  pada  tahap  analisis  selanjutnya,  maka  vektor  solusi
w
opt didekomposisi menjadi tiga bagian, yaitu xopt yang diperoleh dari elemen pertama
hingga ke-n sebagai bobot optimal setiap aset, gammaopt yang diperoleh dari elemen ke-
(n+1) sebagai nilai ambang batas CVaR optimal, serta zopt yang diperoleh dari elemen
ke-(n+2) hingga akhir sebagai vektor variabel bantu optimal pada setiap strategi simulasi.
Tahap ini dapat ditulis sebagai berikut:
1      x_opt      = w_opt (1:n);
2      gamma_opt = w_opt(n+1);
3      z_opt      = w_opt(n+2: end);
Keseluruhan hasil dari penyelesaian optimasi dengan model mean-CVaR dapat dilihat
pada tabel berikut:
## 36

Tabel 4.13    Hasil Optimasi Model Mean-CVaR
## R
max
Strategi 1Strategi 2Strategi 3Strategi 4Strategi 5
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
0.000004969Tidak MemenuhiTidak MemenuhiTidak MemenuhiTidak MemenuhiTidak Memenuhi
0.000020269Tidak MemenuhiTidak MemenuhiTidak MemenuhiTidak MemenuhiTidak Memenuhi
0.0044747330.000052  0.0044560.000042  0.0044400.000086  0.0044680.000064  0.0044550.000017  0.004416
0.0091972780.000052  0.0091500.000042  0.0091290.000086  0.0091500.000064  0.0091410.000017  0.009116
0.0095994140.000052  0.0095510.000042  0.0095320.000086  0.0095520.000064  0.0095450.000017  0.009516
0.0195471590.000052  0.0194190.000042  0.0194620.000086  0.0194270.000064  0.0194080.000017  0.019406
4.8.3    Penyelesaian Optimasi dengan Model Mean-WCCVaR
Untuk menyelesaikan model kedua yaitu mean-WCCVaR pada persamaan 4.5 sampai
dengan  4.10  dapat  menggunakan  langkah-langkah  program  yang  sama  dengan  model
mean-variance.  Namun, pada model mean-WCCVaR terdapat parameter tambahan.
Pada  penambahan  parameter,  terdapat  tingkat  kepercayaan  (β)  ditulis  dengan
variabel beta dengan nilai 0, 95,  sedangkan nilai κ ditulis dengan variabel kappa yang
diperoleh  dari  perhitungan
q
β/(1− β)  sebagai  faktor  skala  yang  digunakan  dalam
formulasi model mean-WCCVaR. Tahap ini dapat ditulis sebagai berikut:
1 beta   = 0.95;
2 kappa = sqrt(beta / (1 - beta));
Selanjutnya,  dilakukan  iterasi  untuk  setiap  nilai  risiko  maksimal  (R
max
).   Hal  ini
dilakukan agar setiap nilai R
max
dapat diuji secara bergantian.  Iterasi dilakukan dengan
perulangan for sejumlah elemen dalam Rmaxlist dengan setiap iterasi ke-k nilai variabel
Rmax diambil dari Rmax
list.  Selanjutnya, fungsi objektif diinisialisasi melalui variabel
objfun,  sedangkan  kendala  risiko  diinisialisasi  melalui  variabel nonlcon.   Selanjutnya,
model  optimasi  sesuai  persamaan  4.11  sampai  dengan  4.14  dihitung  menggunakan
solver fmincon untuk menghasilkan bobot optimal yang ditulis dengan variabel xopt,
nilai  fungsi  objektif  dengan  variabel fval,  dan  indikator  keberhasilan  dengan  variabel
exitflag.  Tahap ini dapat ditulis sebagai berikut:
1 for k = 1: length(Rmax_list)
## 2      Rmax = Rmax_list(k);
3      objfun = @(x) mu’ * x;
4      nonlcon = @(x) deal(-mu ’*x + kappa * sqrt(x’*Sigma*x) - Rmax ,
## []);
5      [x_opt , fval , exitflag] = fmincon(objfun , x0, [], [], Aeq ,
beq , lb , ub , nonlcon , options);
Keseluruhan hasil dari penyelesaian optimasi dengan model mean-WCCVaR dapat
dilihat pada tabel berikut:
## 37

Tabel 4.14    Hasil Optimasi Model Mean-WCCVaR
## R
max
Strategi 1Strategi 2Strategi 3Strategi 4Strategi 5
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
## Expected
CostRisk
0.000004969Tidak MemenuhiTidak MemenuhiTidak MemenuhiTidak MemenuhiTidak Memenuhi
0.000020269Tidak MemenuhiTidak MemenuhiTidak MemenuhiTidak MemenuhiTidak Memenuhi
0.004474733Tidak Memenuhi0.000042  0.003823Tidak Memenuhi0.000064  0.0044420.000017  0.002179
0.0091972780.000052  0.0044570.000042  0.0038150.000086  0.0076460.000064  0.0044420.000017  0.002179
0.0095994140.000052  0.0046450.000042  0.0038150.000086  0.0076460.000064  0.0044420.000017  0.002179
0.0195471590.000052  0.0046450.000042  0.0038150.000086  0.0076460.000064  0.0044420.000017  0.002179
Setelah mendapatkan algoritma untuk ketiga model optimasi, perbandingan hasil dari
program ketiga model tersebut akan dibahas pada bab berikutnya.
4.9    Hasil dan Pembahasan
Pada penyelesaian optimasi dengan ketiga model yang berbeda ukuran didapatkan
hasil akhir berupa:
-  Bobot dan instrumen yang terpilih dalam komposisi utang valuta asing yang optimal
pada tiap model.
-  Nilai  expected  cost  pada  penyelesaian  optimal  sebagai  fungsi  objektif  pada  tiap
model.
-  Nilai risiko pada penyelesaian optimal sebagai kendala pada tiap model
Penyelesaian optimasi dilakukan menggunakan software Matlab R2024a dan dibahas
pada subbab berikutnya.
4.9.1    Hasil untuk Strategi dengan Batasan Khusus
Melalui penyelesaian optimasi yang dilakukan, didapatkan hasil penyelesaian dengan
strategi dengan batasan khusus, yaitu strategi ke-1 sampai dengan strategi ke-4 dengan
kendala batasan hasil modifikasi dari kebijakan bobot komposisi Kementerian Keuangan
yang disajikan pada Tabel 4.15 .
Berdasarkan  Tabel  4.15  menjelaskan  bahwa  pada  model  formulasi  mean-variance
didapatkan  hasil  komposisi  optimal  yaitu  pada  strategi  ke-3  yaitu  kendala  batasan
hasil  formulasi  memperlebar  interval  bobot  kebijakan  Kementerian  Keuangan  dengan
terpilihnya  instrumen  dengan  bobot  paling  besar  yaitu  USD
5Y  sebesar  47,83%  dan
instrumen dengan bobot paling kecil yaitu JPY
10Y sebesar 1,50%. Komposisi ini berlaku
untuk seluruh nilai kendala risiko maksimal (R
max
). Lalu, untuk nilai expected cost sebesar
0,000042296 dengan nilai risiko sebesar 0,0008849.
Sedangkan, berdasarkan Tabel 4.15 menjelaskan bahwa pada model formulasi mean-
CVaR  didapatkan  hasil  komposisi  optimal  yaitu  pada  strategi  ke-2  juga  yaitu  kendala
batasan  hasil  formulasi  memperlebar  interval  bobot  kebijakan  Kementerian  Keuangan
dengan terpilihnya instrumen dengan bobot paling besar yaitu USD
5Y sebesar 47,00%
dan instrumen dengan bobot paling kecil yaitu JPY10Y sebesar 1,50%.  Komposisi ini
berlaku untuk seluruh nilai kendala risiko maksimal (R
max
), kecuali nilai yang terlalu kecil
seperti 0,00000496 dan 0,000020268.  Lalu, untuk nilai expected cost sebesar 0,000042292
dengan nilai risiko sebesar 0,004440.
Yang  terakhir,  berdasarkan  Tabel  4.15  menjelaskan  bahwa  pada  model  formulasi
mean-WCCVaR didapatkan hasil komposisi optimal yaitu pada strategi ke-2 juga yaitu
## 38

kendala  batasan  hasil  formulasi  memperlebar  interval  bobot  kebijakan  Kementerian
Keuangan  dengan  terpilihnya  instrumen  dengan  bobot  paling  besar  yaitu  USD5Y
sebesar 47,83% dan instrumen dengan bobot paling kecil yaitu JPY
10Y sebesar 1,50%.
Komposisi ini berlaku untuk seluruh nilai kendala risiko maksimal (R
max
), kecuali nilai
yang  terlalu  kecil  seperti  0,00000496  dan  0,000020268.   Lalu,  untuk  nilai  expected  cost
sebesar 0,000042296 dengan nilai risiko sebesar 0,0038148.
Oleh karena itu,  pada strategi dengan kendala batasan khusus,  model mean-CVaR
memiliki hasil yang paling optimal dengan nilai expected cost paling kecil dibanding dua
model  lainnya.   Kesimpulan  hasil  komposisi  dengan  strategi  dengan  kendala  batasan
paling  optimal  untuk  setiap  strategi  dapat  dilihat  pada  tabel  dan  grafik  berikut  dan
keseluruhan hasil dapat dilihat pada Lampiran 6:
Tabel 4.15    Hasil Optimasi untuk Strategi dengan Batasan Khusus
Mean-Variance dengan R
max
## = 0,004474733
Strategi ke-1Strategi ke-2Strategi ke-3Strategi ke-4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## Expected Cost0,00005240,00004230,00008620,0000635
## Risk0,00107740,00088490,00177390,0010337
Mean-CVaR dengan R
max
## = 0,004474733
Strategi ke-1Strategi ke-2Strategi ke-3Strategi ke-4
## USD5Y47,00%47,00%37,50%45,90%
## USD10Y12,50%14,00%7,50%13,40%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y3,00%4,50%7,50%6,40%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## Expected Cost0,0000520,0000420,0000860,000064
## Risk0,0044560,0044400,0044680,004455
Mean-WCCVaR dengan R
max
## = 0,004474733
Strategi ke-1Strategi ke-2Strategi ke-3Strategi ke-4
## USD5Y47,42%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,58%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## Expected Cost0,00005240,00004230,00008620,0000635
## Risk0,00464530,00381480,00764620,0044422
## 39

Gambar 4.5    Grafik Keseluruhan Bobot Optimal dengan Batasan Khusus
4.9.2    Grafik Efficient Frontier Strategi dengan Batasan Khusus
Setelah   didapatkan   hasil   dari   penyelesaian   optimasi   menggunakan   Matlab,
selanjutnya dilakukan penyelesaian grafik efficient frontier untuk tiap model pada strategi
dengan  batasan  khusus.Grafik  efficient  frontier  digunakan  untuk  menggambarkan
gabungan  portofolio  optimal  yang  memberikan  expected  cost  terendah  dengan  tingkat
risiko tertentu.  Penyelesaian ini dilakukan menggunakan software Matlab R2024a.  Untuk
grafik efficient frontier pada model mean-variance, mean-CVaR, dan mean-WCCVaR pada
strategi dengan batasan khusus dapat dilihat pada Gambar 4.8 berikut:
(a) Mean-Variance(b) Mean-CVaR(c) Mean-WCCVaR
Gambar 4.6    Grafik Efficient Frontier  dengan Batasan Khusus
4.9.3    Hasil untuk Strategi tanpa Batasan Khusus
Melalui penyelesaian optimasi yang dilakukan, didapatkan hasil penyelesaian dengan
strategi  tanpa  batasan  khusus,  yaitu  strategi  ke-5  dengan  kendala  batasan  [0, 1]  untuk
tiap instrumennya disajikan pada Tabel 4.16.
Berdasarkan Tabel 4.16 menjelaskan bahwa pada ketiga model formulasi baik mean-
variance,  mean-CVaR,  dan  mean-WCCVaR  didapatkan  hasil  komposisi  optimal  yaitu
terpilihnya  instrumen  ke-3  yaitu  USD
30Y  dengan  bobot  100%  dan  untuk  instrumen
lainnya tidak dipilih.  Komposisi ini berlaku untuk seluruh nilai kendala risiko maksimal
## (R
max
).   Namun,  pada  nilai  kendala  risiko  masksimal  (R
max
)  yang  terlalu  kecil  seperti
0.00000496  dan  0.000020268,  model  mean-CVaR  dan  mean-WCCVaR  tidak  terpenuhi.
Lalu, untuk nilai expected cost pada model mean-variance sebesar 0.0000172 dengan nilai
risiko sebesar 0,0005039, model mean-CVaR sebesar 0,000017 dengan nilai risiko sebesar
## 40

0,019406, dan model mean-WCCVaR sebesar 0,000017 dan 0,002179.  Alasan dari nilai
risiko yang berbeda-beda tetapi hasil komposisi sama adalah sebenarnya hasil komposisi
tidak  benar-benar  mirip,  nyatanya  pada  instrumen  selain  USD
30Y  terdapat  angka  di
belakang nol yang nilainya sangat kecil.  Sehingga Matlab menghitung USD30Y dengan
bobot 100%.
Oleh karena itu, pada strategi tanpa kendala batasan khusus, model mean-variance
memiliki hasil yang paling optimal dengan nilai risiko paling rendah.  Kesimpulan hasil
komposisi  dengan  strategi  tanpa  kendala  batasan  paling  optimal  untuk  setiap  strategi
dapat  dilihat  pada  tabel  dan  grafik  berikut  dan  keseluruhan  hasil  dapat  dilihat  pada
## Lampiran 5:
Tabel 4.16    Hasil Optimasi untuk Strategi tanpa Batasan Khusus
Strategi ke-5 dengan R
max
## = 0,004474733
Mean-VarianceMean-CVaRMean-WCCVaR
## USD5Y0,00%0,00%0,00%
## USD10Y0,00%0,00%0,00%
## USD30Y100,00%100,00%100,00%
## EUR7Y0,00%0,00%0,00%
## EUR10Y0,00%0,00%0,00%
## JPY5Y0,00%0,00%0,00%
## JPY10Y0,00%0,00%0,00%
## Expected Cost0,000017180,000017180,00001718
## Risk0,000503910,004416050,00217932
Gambar 4.7    Grafik Keseluruhan Bobot Optimal tanpa Batasan Khusus
4.9.4    Grafik Efficient Frontier Strategi tanpa Batasan Khusus
Setelah   didapatkan   hasil   dari   penyelesaian   optimasi   menggunakan   Matlab,
selanjutnya dilakukan penyelesaian grafik efficient frontier untuk tiap model pada strategi
tanpa  batasan  khusus.Grafik  efficient  frontier   digunakan  untuk  menggambarkan
## 41

gabungan  portofolio  optimal  yang  memberikan  expected  cost  terendah  dengan  tingkat
risiko tertentu.  Penyelesaian ini dilakukan menggunakan software Matlab R2024a.  Untuk
grafik efficient frontier pada model mean-variance, mean-CVaR, dan mean-WCCVaR pada
strategi tanpa batasan khusus dapat dilihat pada Gambar 4.8 berikut:
(a) Mean-Variance(b) Mean-CVaR(c) Mean-WCCVaR
Gambar 4.8    Grafik Efficient Frontier  tanpa Batasan Khusus
## 42

## BAB V
## KESIMPULAN DAN SARAN
## 5.1    Kesimpulan
Berdasarkan  simulasi  yang  telah  dilakukan  terhadap  model  optimasi  portofolio,
diperoleh kesimpulan sebagai berikut:
-  Implementasi  formulasi  model  mean-variance,  mean-CVaR,  dan  mean-WCCVaR
untuk   menentukan   komposisi   utang   valuta   asing   berhasil   dilakukan   dengan
menggunakan bantuan software Matlab R2024a.
-  Komposisi utang paling optimal dengan strategi tanpa batasan khusus yaitu dengan
model  mean-variance  yang  menghasilkan  komposisi  dengan  instrumen  ke-3  yaitu
## USD
30Y dengan bobot sebesar 100% dan untuk instrumen lainnya tidak dipilih.
Lalu, untuk nilai expected cost sebesar 0,0000172 dan nilai risiko sebesar 0,0005039.
Sedangkan untuk komposisi utang paling optimal dengan strategi dengan batasan
khusus  yaitu  dengan  model  mean-CVaR  yang  menghasilkan  komposisi  dengan
instrumen  ke-2  yaitu  USD
30Y  dengan  masing-masing  bobot  sebesar  47,00%,
14,00%;  18,00%;  11,50%;  4,50%;  3.50%;  1.50%.   Lalu,  untuk  nilai  expected  cost
sebesar 0,000042292 dengan nilai risiko sebesar 0,004440.
-  Komposisi  paling  optimal  pada  strategi  tanpa  batasan  khusus  diperoleh  melalui
model  mean-variance,  sedangkan  pada  strategi  dengan  batasan  khusus  diperoleh
melalui model mean-CVaR. Ketiga model menghasilkan nilai fungsi objektif berupa
expected  cost  yang  sama  tetapi  menghasilkan  nilai  risiko  yang  berbeda-beda.
Hal ini membuktikan bahwa model dengan ukuran risiko yang longgar cenderung
menghasilkan nilai risiko yang lebih kecil,  sementara model dengan ukuran risiko
yang  ketat  menghasilkan  nilai  risiko  yang  lebih  besar.   Oleh  karena  itu,  model
dengan  ukuran  risiko  yang  longgar  terpilih  sebagai  solusi  dengan  hasil  optimasi
paling  optimal,  karena  mampu  menghasilkan  nilai  risiko  rendah  dengan  nilai
expected cost yang sama dengan model lainnya.  Faktor kendala batasan bobot juga
berpengaruh dalam menghasilkan komposisi optimal.
## 5.2    Saran
Beberapa  saran  yang  diberikan  untuk  pengembangan  penelitian  ini  ke  depannya
antara lain adalah memperbanyak data yang digunakan, baik dari segi jumlah maupun
rentang   periode   untuk  meningkatkan   kualitas   penyelesaian   permasalahan   optimasi
komposisi utang valuta asing.  Lalu, pertimbangan dalam penambahan jumlah instrumen
pada optimasi agar komposisi lebih diversifikasi.  Selain itu, mempertimbangkan strategi
yang  lebih  beragam,  khususnya  dalam  hal  penetapan  batasan  bobot  per  instrumen
maupun tingkat kepercayaan yang digunakan.
## 43



## DAFTAR PUSTAKA
Aisah,  A.  N.,  Santoso,  E.  K.,  &  Rauf,  N.  M.   (2026).   Analisis  investasi  saham  sektor
energi menggunakan metode value at risk (var) dan conditional value at risk (cvar)
dengan pendekatan single index model: Studi kasus indeks lq45 tahun 2025. Journal
of Economic and Business Advancement, 1 (3), 186–194.
Ananda,  C.  F.    (2021).    Fenomena  utang  dalam  pandemi.  https://feb.ub.ac.id/
fenomena-utang-dalam-pandemi/.    (Artikel  dipublikasikan  25  Januari  2021  di
Fakultas Ekonomi dan Bisnis Universitas Brawijaya)
Bianchi, J., Hatchondo, J. C., & Martinez, L.  (2018).  International reserves and rollover
risk.  American Economic Review, 108 (9), 2629–2670.
Chapra, S. C., Canale, R. P., et al. (2011).  Numerical methods for engineers (Vol. 1221).
## Mcgraw-hill New York.
Cornuejols,  G.,  Pe ̃na,  J.,  &  T ̈ut ̈unc ̈u,  R.   (2018).    Optimization  methods  in  finance.
## Cambridge University Press.
Direktorat   Jenderal   Pengelolaan   Pembiayaan   dan   Risiko,   Kementerian   Keuangan
Republik Indonesia.  (2025).  Utang  negara  bengkak  itu  hoax. https://www.djppr
.kemenkeu.go.id/utangnegarabengkak.    (Halaman  resmi  DJPPR  menjelaskan
fakta terkait utang negara dan merespon klaim utang “membengkak”)
D’Erasmo, P., Mendoza, E. G., & Zhang, J.  (2016).  What is a sustainable public debt?
In Handbook of macroeconomics (Vol. 2, pp. 2493–2597).  Elsevier.
Eduardus Tandelilin, M., & CWM, C.  (2017).  Pasar modal:  Manajemen portofolio dan
investasi.  Pt Kanisius.
Elton, E. J., Gruber, M. J., Brown, S. J., & Goetzmann, W. N. (2009).  Modern portfolio
theory and investment analysis.  John Wiley & Sons.
Fedihartono,  C.  M.,  Virjannah,  N.  A.,  &  Yasin,  M.   (2023).   Pengaruh  kurs  terhadap
pengangguran, utang luar negeri, neraca perdagangan, dan pertumbuhan ekonomi
di indonesia.  Trending:  Jurnal Manajemen dan Ekonomi, 1 (3), 01–13.
Fertis, A., Baes, M., & L ̈uthi, H.-J.  (2012).  Robust risk management.  European Journal
of Operational Research, 222 (3), 663–672.
Georgantas, A., Doumpos, M., & Zopounidis, C. (2024). Robust optimization approaches
for  portfolio  selection:   a  comparative  analysis.    Annals  of  Operations  Research,
## 339 (3), 1205–1221.
Indonesia, B.  (2021).  External debt statistics of indonesia.  Bank Indonesia, 15 .
Insulinde Yuliyati, I. (2023). Analisis determinan volatilitas nilai kurs rupiah di indonesia
tahun 2010–2022  (Unpublished doctoral dissertation).  S-2 Ekonomi Syariah.
Ji,  L.,  Huang,  G.,  Xie,  Y.,  Zhou,  Y., & Zhou,  J.  (2018).  Robust cost-risk tradeoff for
day-ahead schedule optimization in residential microgrid system under worst-case
conditional value-at-risk consideration.  Energy, 153 , 324–337.
Kolm, P. N., T ̈ut ̈unc ̈u, R., & Fabozzi, F. J.  (2014).  60 years of portfolio optimization:
Practical challenges and current trends. European Journal of Operational Research,
## 234 (2), 356–371.
Markowitz, H.  (1952).  Modern portfolio theory.  Journal of Finance, 7 (11), 77–91.
## 45

Nocedal,  J.   (2006).    Numerical  optimization  (springer  series  in  operations  research).
## Springer.
Pemerintah Republik Indonesia.  (2006).  Peraturan pemerintah republik indonesia nomor
2  tahun  2006  tentang  tata  cara  pengadaan  pinjaman  dan/atau  penerimaan  hibah
serta penerusan pinjaman dan/atau hibah luar negeri. https://peraturan.bpk.go
.id/Details/49010/pp-no-2-tahun-2006. (Ditetapkan dan diundangkan pada 30
Januari 2006, dicabut oleh PP Nomor 10 Tahun 2011)
Rockafellar, R. T., Uryasev, S., et al.  (2000).  Optimization of conditional value-at-risk.
Journal of risk, 2 , 21–42.
Rusyn, V., et al.  (2024).  Risk measurement of investment portfolio using var and cvar
from  the  top  10  traded  stocks  on  the  idx.   International  Journal  of  Quantitative
Research and Modeling, 5 (1), 12–19.
Tang, L., & Ling, A.  (2014).  A closed-form solution for robust portfolio selection with
worst-case  cvar  risk  measure.    Mathematical  Problems  in  Engineering,  2014 (1),
## 494575.
Zenios, S. A., Consiglio, A., Athanasopoulou, M., Moshammer, E., Gavilan, A., & Erce, A.
(2019). Risk management for sovereign debt financing with sustainability conditions.
## Globalization Institute Working Paper (367).
Zhu, S., & Fukushima, M.  (2009).  Worst-case conditional value-at-risk with application
to robust portfolio management.  Operations research, 57 (5), 1155–1168.
## 46

## DAFTAR LAMPIRAN
## Lampiran 1
## Hasil Interpolasi
No.TanggalEUR10Y
## 11/29/20210,96700
## 22/1/20210,97202
## 32/2/20210,97370
## 42/3/20210,97537
## 52/4/20210,97704
## 62/5/20210,97872
## 72/8/20210,98374
## 82/9/20210,98541
## 92/10/20210,98709
## 102/11/20210,98876
## 112/12/20210,99043
## 122/15/20210,99546
## 132/16/20210,99713
## 142/17/20210,99880
## 152/18/20211,00048
## 162/19/20211,00215
## 172/22/20211,00717
## 182/23/20211,00885
## 192/24/20211,01052
## 202/25/20211,01220
## 212/26/20211,01387
## 223/1/20211,01889
## 233/2/20211,02057
## 243/3/20211,02224
## 253/4/20211,02391
## .
## .
## .
## .
## .
## .
## .
## .
## .
## 1659/16/20211,35200
## 47

## Lampiran 2
Data Suku Bunga dan Data Valuta Asing
## Tanggal
## Data Suku Bunga
## Data Valuta Asing
## USD
## 5Y    USD
## 10Y    USD
## 30Y    EUR
## 7Y    EUR
## 10Y
## JPY
## 5Y    JPY
## 10Y
## USD/EUR
## USD/JPY
## 1/1/2021
## 0,012640
## 0,020160
## 0,030640    0,005780
## 0,010440    0,009190
## 0,012510
## 0,819100    103,400000
## 1/4/2021
## 0,012360
## 0,019750
## 0,030430    0,005640
## 0,010110    0,009190
## 0,012540
## 0,816200    103,150000
## 1/5/2021
## 0,012340
## 0,019860
## 0,030460    0,005550
## 0,009930    0,009130
## 0,012470
## 0,813200    102,760000
## 1/6/2021
## 0,012510
## 0,020230
## 0,030880    0,005390
## 0,009810    0,009140
## 0,012490
## 0,811400    103,070000
## 1/7/2021
## 0,013300
## 0,020850
## 0,031790    0,005540
## 0,009830    0,008870
## 0,012390
## 0,815100    103,840000
## 1/8/2021
## 0,013680
## 0,021240
## 0,032350    0,005550
## 0,009820    0,008910
## 0,012310
## 0,819200    104,010000
## 1/11/2021
## 0,013740
## 0,021210
## 0,032260    0,005470
## 0,009770    0,008910
## 0,012310
## 0,823100    104,280000
## 1/12/2021
## 0,013790
## 0,021820
## 0,032500    0,005570
## 0,009830    0,009060
## 0,012410
## 0,819200    103,770000
## 1/13/2021
## 0,013750
## 0,021510
## 0,032130    0,005660
## 0,009810    0,008110
## 0,011780
## 0,822600    103,920000
## 1/14/2021
## 0,013560
## 0,021060
## 0,031800    0,005690
## 0,009710    0,007990
## 0,011720
## 0,822900    103,810000
## 1/15/2021
## 0,013560
## 0,020930
## 0,031800    0,005690
## 0,009690    0,007980
## 0,011870
## 0,828200    103,920000
## 1/18/2021
## 0,013560
## 0,020930
## 0,031800    0,005730
## 0,009700    0,008010
## 0,012040
## 0,828200    103,700000
## 1/19/2021
## 0,013540
## 0,020580
## 0,031430    0,005810
## 0,009710    0,007970
## 0,012510
## 0,824500    103,910000
## 1/20/2021
## 0,013560
## 0,020460
## 0,031250    0,005850
## 0,009720    0,007810
## 0,011690
## 0,826100    103,560000
## 1/21/2021
## 0,013480
## 0,020410
## 0,031160    0,005840
## 0,009740    0,007100
## 0,011750
## 0,821900    103,530000
## 1/22/2021
## 0,013640
## 0,020770
## 0,031420    0,005950
## 0,009750    0,007060
## 0,011810
## 0,821700    103,840000
## 1/25/2021
## 0,013800
## 0,020710
## 0,031190    0,005970
## 0,009650    0,007000
## 0,011820
## 0,823700    103,770000
## 1/26/2021
## 0,013640
## 0,020510
## 0,030990    0,006110
## 0,009670    0,006960
## 0,011730
## 0,822400    103,630000
## 1/27/2021
## 0,013520
## 0,020540
## 0,030980    0,006250
## 0,009640    0,007040
## 0,011760
## 0,825700    104,160000
## 1/28/2021
## 0,013540
## 0,020660
## 0,031140    0,006260
## 0,009670    0,007070
## 0,012290
## 0,825000    104,270000
## 1/29/2021
## 0,013520
## 0,020760
## 0,031270    0,006230
## 0,009670    0,007090
## 0,011840
## 0,824000    104,780000
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## 11/24/2025
## 0,042310
## 0,049220
## 0,053480    0,034760
## 0,039910    0,019900
## 0,027080
## 0,867600    156,600000
## 48

## Lampiran 3
## Data Total Biaya Utang Valas
## Tanggal
## USD
## 5Y    USD
## 10Y    USD
## 30Y    EUR
## 7Y    EUR
## 10Y
## JPY
## 5Y
## JPY
## 10Y
## 1/1/2021
## 1,01264
## 1,02016
## 1,03064
## 0,82383
## 0,82765
## 104,35025    104,69353
## 1/4/2021
## 1,01236
## 1,01975
## 1,03043
## 0,82080
## 0,82738
## 104,09795    104,44350
## 1/5/2021
## 1,01234
## 1,01986
## 1,03046
## 0,81771
## 0,82723
## 103,69820    104,04142
## 1/6/2021
## 1,01251
## 1,02023
## 1,03088
## 0,81577
## 0,82714
## 104,01206    104,35734
## 1/7/2021
## 1,01330
## 1,02085
## 1,03179
## 0,81962
## 0,82715
## 104,76106    105,12658
## 1/8/2021
## 1,01368
## 1,02124
## 1,03235
## 0,82375
## 0,82714
## 104,93673    105,29036
## 1/11/2021
## 1,01374
## 1,02121
## 1,03226
## 0,82760
## 0,82710
## 105,20913    105,56369
## 1/12/2021
## 1,01379
## 1,02182
## 1,03250
## 0,82376
## 0,82715
## 104,71016    105,05779
## 1/13/2021
## 1,01375
## 1,02151
## 1,03213
## 0,82726
## 0,82714
## 104,76279    105,14418
## 1/14/2021
## 1,01356
## 1,02106
## 1,03180
## 0,82758
## 0,82705
## 104,63944    105,02665
## 1/15/2021
## 1,01356
## 1,02093
## 1,03180
## 0,83291
## 0,82704
## 104,74928    105,15353
## 1/18/2021
## 1,01356
## 1,02093
## 1,03180
## 0,83295
## 0,82705
## 104,53064    104,94855
## 1/19/2021
## 1,01354
## 1,02058
## 1,03143
## 0,82929
## 0,82705
## 104,73816    105,20991
## 1/20/2021
## 1,01356
## 1,02046
## 1,03125
## 0,83093
## 0,82706
## 104,36880    104,77062
## 1/21/2021
## 1,01348
## 1,02041
## 1,03116
## 0,82670
## 0,82708
## 104,26506    104,74648
## 1/22/2021
## 1,01364
## 1,02077
## 1,03142
## 0,82659
## 0,82709
## 104,57311    105,06635
## 1/25/2021
## 1,01380
## 1,02071
## 1,03119
## 0,82862
## 0,82700
## 104,49639    104,99656
## 1/26/2021
## 1,01364
## 1,02051
## 1,03099
## 0,82742
## 0,82702
## 104,35126    104,84558
## 1/27/2021
## 1,01352
## 1,02054
## 1,03098
## 0,83086
## 0,82700
## 104,89329    105,38492
## 1/28/2021
## 1,01354
## 1,02066
## 1,03114
## 0,83016
## 0,82702
## 105,00719    105,55148
## 1/29/2021
## 1,01352
## 1,02076
## 1,03127
## 0,82913
## 0,82702
## 105,52289    106,02060
## 2/1/2021
## 1,01358
## 1,02088
## 1,03162
## 0,83437
## 0,82706
## 105,68402    106,18669
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## 11/24/2025
## 1,04231
## 1,04922
## 1,05348
## 0,89776
## 0,85179
## 159,71634    160,84073
## 49

## Lampiran 4
## Data Tingkat Perubahan Total Biaya Utang Valas
## Tanggal
## USD
## 5Y
## USD
## 10Y    USD
## 30Y
## EUR
## 7Y
## EUR
## 10Y
## JPY
## 5Y
## JPY
## 10Y
## 1/4/2021
-0,000277    -0,000402    -0,000204    -0,003686    -0,000327    -0,002421    -0,002391
## 1/5/2021
## -0,000020
## 0,000108
## 0,000029
## -0,003772    -0,000178    -0,003848    -0,003857
## 1/6/2021
## 0,000168
## 0,000363
## 0,000408
## -0,002375    -0,000119
## 0,003022
## 0,003032
## 1/7/2021
## 0,000780
## 0,000608
## 0,000882
## 0,004699
## 0,000020
## 0,007175
## 0,007344
## 1/8/2021
## 0,000375
## 0,000382
## 0,000543
## 0,005027
## -0,000010
## 0,001675
## 0,001557
## 1/11/2021
## 0,000059
## -0,000029    -0,000087
## 0,004670
## -0,000050
## 0,002593
## 0,002593
## 1/12/2021
## 0,000049
## 0,000597
## 0,000232
## -0,004650
## 0,000059
## -0,004754    -0,004804
## 1/13/2021
## -0,000039    -0,000303    -0,000358
## 0,004231
## -0,000020
## 0,000503
## 0,000822
## 1/14/2021
## -0,000187    -0,000441    -0,000320
## 0,000394
## -0,000099    -0,001178    -0,001118
## 1/15/2021
## 0,000000
## -0,000127
## 0,000000
## 0,006420
## -0,000020
## 0,001049
## 0,001207
## 1/18/2021
## 0,000000
## 0,000000
## 0,000000
## 0,000040
## 0,000010
## -0,002089    -0,001951
## 1/19/2021
## -0,000020    -0,000343    -0,000359    -0,004398
## 0,000010
## 0,001983
## 0,002487
## 1/20/2021
## 0,000020
## -0,000118    -0,000175
## 0,001978
## 0,000010
## -0,003533    -0,004184
## 1/21/2021
## -0,000079    -0,000049    -0,000087    -0,005107
## 0,000020
## -0,000994    -0,000230
## 1/22/2021
## 0,000158
## 0,000353
## 0,000252
## -0,000134
## 0,000010
## 0,002950
## 0,003049
## 1/25/2021
## 0,000158
## -0,000059    -0,000223
## 0,002451
## -0,000099    -0,000734    -0,000664
## 1/26/2021
## -0,000158    -0,000196    -0,000194    -0,001440
## 0,000020
## -0,001390    -0,001439
## 1/27/2021
## -0,000118
## 0,000029
## -0,000010
## 0,004144
## -0,000030
## 0,005181
## 0,005131
## 1/28/2021
## 0,000020
## 0,000118
## 0,000155
## -0,000838
## 0,000030
## 0,001085
## 0,001579
## 1/29/2021
## -0,000020
## 0,000098
## 0,000126
## -0,001243
## 0,000000
## 0,004899
## 0,004435
## 2/1/2021
## 0,000059
## 0,000118
## 0,000339
## 0,006291
## 0,000050
## 0,001526
## 0,001565
## 2/2/2021
## -0,000158    -0,000137    -0,000136
## 0,001416
## 0,000017
## 0,000572
## 0,001135
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## ...
## 11/24/2025
## -0,000470    -0,000286    -0,000199    -0,001478    -0,000010
## 0,000511
## 0,000511
## 50

## Lampiran 5
Hasil Optimasi tanpa Batasan Khusus
## R
max
## = 0,000004969
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%
## Tidak Memenuhi
## USD10Y0,00%
## USD30Y100,00%
## EUR7Y0,00%
## EUR10Y0,00%
## JPY5Y0,00%
## JPY10Y0,00%
## EXPECTED COST0,0000172
## RISIKO0,0005039
## R
max
## = 0,000020269
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%
## Tidak Memenuhi
## USD10Y0,00%
## USD30Y100,00%
## EUR7Y0,00%
## EUR10Y0,00%
## JPY5Y0,00%
## JPY10Y0,00%
## EXPECTED COST0,0000172
## RISIKO0,0005039
## R
max
## = 0,004474733
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%0,00%0,00%
## USD10Y0,00%0,00%0,00%
## USD30Y100,00%100,00%100,00%
## EUR7Y0,00%0,00%0,00%
## EUR10Y0,00%0,00%0,00%
## JPY5Y0,00%0,00%0,00%
## JPY10Y0,00%0,00%0,00%
## EXPECTED COST0,00001720,00001700,0000172
## RISIKO0,00050390,00441600,0021793
## 51

## R
max
## = 0,009197278
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%0,00%0,00%
## USD10Y0,00%0,00%0,00%
## USD30Y100,00%100,00%100,00%
## EUR7Y0,00%0,00%0,00%
## EUR10Y0,00%0,00%0,00%
## JPY5Y0,00%0,00%0,00%
## JPY10Y0,00%0,00%0,00%
## EXPECTED COST0,00001720,00001700,0000172
## RISIKO0,00050390,00911600,0021793
## R
max
## = 0,009599414
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%0,00%0,00%
## USD10Y0,00%0,00%0,00%
## USD30Y100,00%100,00%100,00%
## EUR7Y0,00%0,00%0,00%
## EUR10Y0,00%0,00%0,00%
## JPY5Y0,00%0,00%0,00%
## JPY10Y0,00%0,00%0,00%
## EXPECTED COST0,00001720,00001700,0000172
## RISIKO0,00050390,00951600,0021793
## R
max
## = 0,019547159
## MV #5MCVAR #5MWCCVAR #5
## USD5Y0,00%0,00%0,00%
## USD10Y0,00%0,00%0,00%
## USD30Y100,00%100,00%100,00%
## EUR7Y0,00%0,00%0,00%
## EUR10Y0,00%0,00%0,00%
## JPY5Y0,00%0,00%0,00%
## JPY10Y0,00%0,00%0,00%
## EXPECTED COST0,00001720,00001700,0000172
## RISIKO0,00050390,01940600,0021793
## 52

## Lampiran 6
Hasil Optimasi dengan Batasan Khusus
## R
max
## = 0,000004969
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y
## Tidak Memenuhi
## USD10Y
## USD30Y
## EUR7Y
## EUR10Y
## JPY5Y
## JPY10Y
## EXPECTED COST
## RISIKO
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y
## Tidak Memenuhi
## USD10Y
## USD30Y
## EUR7Y
## EUR10Y
## JPY5Y
## JPY10Y
## EXPECTED COST
## RISIKO
## 53

## R
max
## = 0,000020269
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y
## Tidak Memenuhi
## USD10Y
## USD30Y
## EUR7Y
## EUR10Y
## JPY5Y
## JPY10Y
## EXPECTED COST
## RISIKO
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y
## Tidak Memenuhi
## USD10Y
## USD30Y
## EUR7Y
## EUR10Y
## JPY5Y
## JPY10Y
## EXPECTED COST
## RISIKO
## R
max
## = 0,004474733
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## 54

## MV #1MV #2MV #3MV #4
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y47,00%47,00%37,50%45,90%
## USD10Y12,50%14,00%7,50%13,40%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y3,00%4,50%7,50%6,40%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005200,00004200,00008600,0000640
## RISIKO0,00445600,00444000,00446800,0044550
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y48,52%
## Tidak Memenuhi
## 47,18%
## USD10Y14,00%12,73%
## USD30Y18,00%16,80%
## EUR7Y11,50%4,70%
## EUR10Y2,98%5,79%
## JPY5Y3,50%12,40%
## JPY10Y1,50%0,40%
## EXPECTED COST0,00004200,0000635
## RISIKO0,00382300,0044418
## R
max
## = 0,009197278
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## 55

## MV #1MV #2MV #3MV #4
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y47,00%47,00%37,50%45,90%
## USD10Y12,50%14,00%7,50%13,40%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y3,00%4,50%7,50%6,40%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005200,00004200,00008600,0000640
## RISIKO0,00915000,00912900,00915000,0091410
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y47,00%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,58%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004200,00008600,0000635
## RISIKO0,00464530,00381500,00764600,0044422
## R
max
## = 0,009599414
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y47,00%47,00%37,50%45,90%
## 56

## MV #1MV #2MV #3MV #4
## USD10Y12,50%14,00%7,50%13,40%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y3,00%4,50%7,50%6,40%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005200,00004200,00008600,0000640
## RISIKO0,00955100,00953200,00955200,0095450
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y47,42%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,58%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004200,00008600,0000635
## RISIKO0,00464530,00381500,00764600,0044422
## R
max
## = 0,019547159
Mean-Variance
## MV #1MV #2MV #3MV #4
## USD5Y47,08%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,92%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004230,00008620,0000635
## RISIKO0,00107740,00088490,00177390,0010337
Mean-CVaR
MCVaR #1MCVaR #2MCVaR #3MCVaR #4
## USD5Y47,00%47,00%37,50%45,90%
## USD10Y12,50%14,00%7,50%13,40%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y3,00%4,50%7,50%6,40%
## JPY5Y5,00%3,50%10,00%12,40%
## 57

## MV #1MV #2MV #3MV #4
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005200,00004200,00008600,0000640
## RISIKO0,01941900,01946200,01942700,0194080
Mean-WCCVaR
MWCVaR #1MWCVaR #2MWCVaR #3MWCVaR #4
## USD5Y47,42%47,83%39,49%47,20%
## USD10Y12,50%13,40%6,03%12,78%
## USD30Y16,50%18,00%11,50%16,80%
## EUR7Y13,00%11,50%18,00%4,70%
## EUR10Y2,58%4,27%6,98%5,72%
## JPY5Y5,00%3,50%10,00%12,40%
## JPY10Y3,00%1,50%8,00%0,40%
## EXPECTED COST0,00005240,00004200,00008600,0000635
## RISIKO0,00464530,00381500,007646000044422
## 58

## BIODATA PENULIS
Zakiyyah  Furoida  atau  biasa  dipanggil  Ida  lahir  di  Lamongan,
6  Maret  2004.Penulis  menempuh  pendidikan  formal  S1  di
## Departemen Matematika Institut Teknologi Sepuluh Nopember
dengan  NRP  5002221029.   Penulis  memiliki  pengalaman  aktif
dalam hal non-akademik, yaitu Teater Tiyang Alit dan Himatika
ITS. Selain itu, penulis juga merupakan penerima beasiswa Bank
Indonesia selama 2 tahun dan menjadi bagian dari Generasi Baru
Indonesia (GenBI), serta aktif mengikuti seluruh kegiatan yang
diadakan oleh Bank Indonesia.  Kritik dan saran kepada penulis
dapat disampaikan melalui email furoidazakiyyah@gmail.com
## 59