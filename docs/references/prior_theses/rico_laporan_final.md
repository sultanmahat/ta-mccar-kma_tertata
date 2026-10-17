TUGAS AKHIR - SM234801
OPTIMASI PORTOFOLIO UTANG VALAS
PEMERINTAH INDONESIA MENGGUNAKAN
METODE CVAR BERDASARKAN HASIL
PERAMALAN MODEL ARIMA-GARCH
BAGUS RICO PAMBUDI
NRP 5002221144
Dosen Pembimbing
Sena Safarina, S.Si., M.Sc., D.Sc.
NIP 1990202012052
Dra. Laksmi Prita Wardhani, M.Si
NIP 19611208 198803 2 001
Program Studi Sarjana
Departemen Matematika
Fakultas Sains dan Analitika Data
Institut Teknologi Sepuluh Nopember
Surabaya
2026
2
PROPOSAL TUGAS AKHIR - SM234801
OPTIMASI PORTOFOLIO UTANG VALAS
PEMERINTAH INDONESIA MENGGUNAKAN
METODE CVAR BERDASARKAN HASIL
PERAMALAN MODEL ARIMA-GARCH
BAGUS RICO PAMBUDI
NRP 5002221144
Dosen Pembimbing
Sena Safarina, S.Si., M.Sc., D.Sc.
NIP 1990202012052
Dra. Laksmi Prita Wardhani, M.Si
NIP 19611208 198803 2 001
Program Sarjana
Departemen Matematika
Fakultas Sains dan Analitika Data
Institut Teknologi Sepuluh Nopember
Surabaya
2026
FINAL PROJECT PROPOSAL - SM234801
OPTIMIZATION OF INDONESIA’S SOVEREIGN
FOREIGN CURRENCY DEBT PORTFOLIO USING
THE CVAR METHOD BASED ON ARIMA-GARCH
FORECASTING RESULTS
BAGUS RICO PAMBUDI
NRP 5002221144
Supervisor
Sena Safarina, S.Si., M.Sc., D.Sc.
NIP 1990202012052
Dra. Laksmi Prita Wardhani, M.Si
NIP 19611208 198803 2 001
Bachelor Program
Department of Mathematics
Faculty of Scientics
Institut Teknologi Sepuluh Nopember
Surabaya
2026
LEMBAR PENGESAHAN
Optimasi Portofolio Utang Valas Pemerintah Indonesia Menggunakan
Metode CVaR Berdasarkan Hasil Peramalan Model ARIMA-GARCH
TUGAS AKHIR
Diajukan untuk memenuhi salah satu syarat
memperoleh gelar Sarjana Matematika pada
Program Studi S-1 Matematika
Departemen Matematika
Fakultas Sains dan Analitika Data
Institut Teknologi Sepuluh Nopember
```
Oleh: BAGUS RICO PAMBUDI
```
NRP. 5002221144
Surabaya, Desember 2026
Disetujui oleh Tim Penguji Tugas Akhir:
Pembimbing
1. Sena Safarina, S.Si., M.Sc., D.Sc. (. . . . . . . . . . . . . . . . . . )
NIP. 1990202012052
2. Dra. Laksmi Prita Wardhani, M.Si (. . . . . . . . . . . . . . . . . . )
NIP. 19611208 198803 2 001
Penguji
1. Prof. Dr. Mahmud Yunus, M.Si (. . . . . . . . . . . . . . . . . . )
NIP. 19620407 198703 1 005
2. Dr. Valeriana Lukitosari, S.Si, MT (. . . . . . . . . . . . . . . . . . )
NIP. 19710928 199802 2 001
3. Endah Rokhmati Merdika Putri, S.Si., M.T., Ph.D (. . . . . . . . . . . . . . . . . . )
NIP. 19761213 200212 2 001
Mengetahui
Kepala Departemen Matematika
Fakultas Sains dan Analitika Data
Dr. Didik Khusnul Arif, S.Si, M.Si
NIP. 19730930 199702 1 001
i
PERNYATAAN ORISINALITAS
Yang bertanda tangan disini:
Nama Mahasiswa / NRP : Bagus Rico Pambudi / 5002221144
```
Departemen : Matematika
```
Dosen Pembimbing / NIP : 1. Sena Safarina, S.Si., M.Sc., D.Sc. / 1990202012052
2. Dra. Laksmi Prita Wardhani, M.Si / 19611208 198803 2 001
dengan ini menyatakan bahwa Tugas Akhir dengan judul “Optimasi Portofolio Utang
Valas Pemerintah Indonesia Menggunakan Metode CVaR Berdasarkan Hasil Peramalan
Model ARIMA-GARCH” adalah hasil karya sendiri, bersifat orisinal, dan ditulis dengan
mengikuti kaidah penulisan ilmiah.
Bilamana di kemudian hari ditemukan ketidaksesuaian dengan pernyataan ini, maka saya
bersedia menerima sanksi sesuai dengan ketentuan yang berlaku di Institut Teknologi
Sepuluh Nopember.
Surabaya, 18 Juni 2026
Mengetahui
Dosen Pembimbing 1 Dosen Pembimbing 2
Sena Safarina, S.Si., M.Sc., D.Sc. Dra. Laksmi Prita Wardhani, M.Si
NIP. 1990202012052 NIP. 19611208 198803 2 001
Mahasiswa
Bagus Rico Pambudi
NRP. 5002221144
iii
ABSTRAK
Optimasi Portofolio Utang Valas Pemerintah Indonesia Menggunakan Metode CVaR
Berdasarkan Hasil Peramalan Model ARIMA-GARCH
Nama Mahasiswa / NRP : Bagus Rico Pambudi / 5002221144
```
Departemen : Matematika FSAD -ITS
```
Dosen Pembimbing : 1. Sena Safarina, S.Si., M.Sc., D.Sc.
2. Dra. Laksmi Prita Wardhani, M.Si
Abstrak
Utang valas memiliki peran penting sebagai salah satu sumber pembiayaan untuk
menutup defisit APBN, tetapi memiliki risiko akibat perubahan suku bunga global dan
nilai tukar mata uang. Oleh karena itu, diperlukan optimasi portofolio agar diperoleh
komposisi utang valas dengan ekspektasi perubahan biaya pembayaran utang dan risiko
yang minimum dengan mempertimbangkan potensi perubahan suku bunga serta nilai
tukar mata uang pada periode mendatang. Model ARIMA-GARCH dipilih karena
mampu memodelkan rata-rata dan volatilitas suku bunga serta nilai tukar mata uang,
sedangkan ukuran risiko CVaR dipilih karena mampu menangkap risiko pada kondisi
ekstrem. Penelitian ini bertujuan untuk menghasilkan peramalan tingkat suku bunga
dan nilai tukar mata uang menggunakan model ARIMA-GARCH, memformulasikan
model optimasi portofolio utang valas Pemerintah Indonesia menggunakan model Mean-
```
Variance Optimization (MVO) dan model optimasi dengan kendala risiko Conditional
```
```
Value at Risk (CVaR), serta menentukan komposisi portofolio utang valas optimal
```
dan membandingkan kinerja kedua model tersebut. Data yang digunakan merupakan
data sekunder deret waktu harian periode 3 Juli 2017 sampai 24 November 2025, yang
meliputi tingkat suku bunga utang, nilai tukar mata uang, dan data portofolio utang
valas Pemerintah Indonesia. Data harian diubah menjadi data bulanan, lalu suku bunga
dan nilai tukar diramalkan selama 12 bulan ke depan menggunakan model ARIMA-
GARCH dengan bantuan perangkat lunak RStudio. Hasil peramalan digabungkan
dengan data historis sebagai input optimasi MVO dan CVaR dengan bantuan perangkat
lunak MATLAB. Hasil penelitian menunjukkan bahwa model MVO mampu menurunkan
ekspektasi persentase perubahan biaya pembayaran utang valas sekitar 19% dan
menekan risiko sekitar 13% dari portofolio yang digunakan Pemerintah Indonesia saat
ini, sedangkan model CVaR-90% mampu menurunkan ekspektasi persentase perubahan
biaya pembayaran utang valas sekitar 18% dan menekan risiko CVaR sekitar 0,3%.
Model ARIMA-GARCH mampu menghasilkan peramalan tingkat suku bunga dan nilai
tukar mata uang dengan akurasi yang baik sehingga dapat digunakan sebagai dasar
optimasi portofolio utang valas, sedangkan model MVO dan CVaR-90% sama-sama
mampu mengoptimalkan kinerja portofolio, dengan MVO lebih unggul dari sisi standar
deviasi dan CVaR-90% lebih sesuai untuk pengendalian risiko ekstrem.
Kata kunci: ARIMA-GARCH, CVaR, MVO, optimasi portofolio, utang valas
vvi
ABSTRACT
Optimization of Indonesia’s Sovereign Foreign Currency Debt Portfolio Using the CVaR
Method Based on ARIMA-GARCH Forecasting Results
Student Name / NRP : Bagus Rico Pambudi / 5002221144
```
Departement : Mathematics SCIENTICS - ITS
```
```
Supervisors : 1. Sena Safarina, S.Si., M.Sc., D.Sc.
```
2. Dra. Laksmi Prita Wardhani, M.Si
Abstract
Foreign-currency debt plays an important role as one source of financing to cover the
state budget deficit, but it carries risks arising from changes in global interest rates and
exchange rates. Therefore, portfolio optimization is required to obtain a foreign-currency
debt composition with minimum expected changes in debt payment costs and risk while
considering possible changes in interest rates and exchange rates in the future period.
The ARIMA-GARCH model is used because it can model the mean and volatility of
interest rates and exchange rates, while the CVaR risk measure is used because it can
capture risk under extreme conditions. This study aims to forecast interest rates and
exchange rates using the ARIMA-GARCH model, formulate the foreign-currency debt
portfolio optimization model of the Government of Indonesia using the Mean-Variance
```
Optimization (MVO) model and the optimization model with Conditional Value at
```
```
Risk (CVaR) constraints, and determine the optimal foreign-currency debt portfolio
```
composition by comparing the performance of both models. The data used in this
study are secondary daily time series data from 3 July 2017 to 24 November 2025,
consisting of debt interest rates, exchange rates, and the foreign-currency debt portfolio
data of the Government of Indonesia. The daily data are converted into monthly data,
and the interest rates and exchange rates are then forecasted for the next 12 months
using the ARIMA-GARCH model using RStudio. The forecasting results are combined
with historical data as the input for MVO and CVaR portfolio optimization using
MATLAB. The results show that the MVO model can reduce the expected percentage
change in foreign-currency debt payment costs by approximately 19% and reduce risk
by approximately 13% compared with the current portfolio used by the Government of
Indonesia. Meanwhile, the CVaR-90% model can reduce the expected percentage change
in foreign-currency debt payment costs by approximately 18% and reduce CVaR risk
by approximately 0.3%. The ARIMA-GARCH model provides accurate forecasts of
interest rates and exchange rates, so the forecasting results can be used as the basis for
foreign-currency debt portfolio optimization. Both the MVO and CVaR-90% models can
improve portfolio performance, with MVO being superior in terms of standard deviation
and CVaR-90% being more suitable for controlling extreme risk.
```
Keywords: ARIMA-GARCH, CVaR, MVO, portfolio optimization, foreign-currency
```
debt
vii
KATA PENGANTAR
Dengan memanjatkan puji syukur kehadirat Allah SWT atas rahmat, taufik, dan
hidayah-nya sehingga penulis dapat menyelesaikan tugas akhir dengan judul:
”OPTIMASI PORTOFOLIO UTANG VALAS PEMERINTAH INDONESIA
MENGGUNAKAN METODE CVAR BERDASARKAN HASIL PERAMALAN
MODEL ARIMA-GARCH”
sebagai salah satu persyaratan akademis dalam menyelesaikan Program Sarjana
Departemen Matematika, Fakultas Sains dan Analitika Data, Institut Teknologi Sepuluh
Nopember Surabaya. Penulis menyadari tugas Akhir ini dapat diselesaikan dengan baik
dukungan, bantuan, dan nasihat dari berbagai pihak. Pada kesempatan ini, penulis ingin
mengucapkan terima kasih dan penghargaan kepada:
1. Orang tua penulis, Rustamaji dan Siti Romelah, adik penulis, Erica Kirana Larasati,
serta keluarga besar yang telah memberikan dukungan, doa, dan motivasi selama
masa perkuliahan.
2. Kepala Departemen Matematika Institut Teknologi Sepuluh Nopember yang telah
memberikan arahan selama masa perkuliahan.
3. Ibu Sena Safarina, S.Si., M.Sc., D.Sc. dan Ibu Dra. Laksmi Prita Wardhani, M.Si.,
selaku dosen pembimbing yang telah memberikan bimbingan, arahan, dan motivasi
kepada penulis.
4. Bapak Prof. Dr. Mahmud Yunus, M.Si., selaku dosen wali yang telah memberikan
arahan kepada penulis selama masa perkuliahan.
5. Bapak Prof. Dr. Mahmud Yunus, M.Si., Ibu Dr. Valeriana Lukitosari, S.Si., M.T.,
dan Ibu Endah Rokhmati Merdika Putri, S.Si., M.T., Ph.D., selaku dosen penguji
yang telah memberikan kritik dan saran untuk perbaikan Tugas Akhir ini.
6. Bapak/Ibu dosen pengajar, seluruh karyawan, tenaga kependidikan, keluarga
besar Departemen Matematika Institut Teknologi Sepuluh Nopember, serta teman-
teman Matematika Angkatan 2022, AXXIIOM, atas ilmu, pengalaman, dukungan,
bantuan, cerita, dan motivasi yang telah diberikan selama masa perkuliahan.
Penulis menyadari bahwa Tugas Akhir ini masih memiliki kekurangan. Oleh karena
itu, penulis mengharapkan kritik dan saran yang membangun dari para pembaca untuk
perbaikan di masa mendatang. Akhir kata, semoga Tugas Akhir ini bermanfaat bagi
semua pihak yang membacanya.
Surabaya, 18 Juni 2026
Bagus Rico Pambudi
ix
DAFTAR ISI
LEMBAR PENGESAHAN i
PERNYATAAN ORISINALITAS iv
ABSTRAK v
ABSTRACT vii
KATA PENGANTAR ix
DAFTAR ISI xi
DAFTAR GAMBAR xv
DAFTAR TABEL xvii
DAFTAR SIMBOL xix
BAB I PENDAHULUAN 1
1.1 Latar Belakang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Rumusan Masalah . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3 Batasan Masalah . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 Tujuan Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.5 Manfaat Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
BAB II TINJAUAN PUSTAKA 5
2.1 Penelitian Terdahulu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.2 Portofolio Utang Valas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 Interpolasi Cubic Spline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
```
2.4 Autoregressive Integrated Moving Average (ARIMA) . . . . . . . . . . . . . . . . . 11
```
2.5 Identifikasi Model ARIMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5.1 Stasioneritas Data terhadap Varians . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5.2 Stasioneritas Data terhadap Mean . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.5.3 Plot ACF & PACF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
2.5.4 Orde Model ARIMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.6 Estimasi dan Uji Signifikansi Parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.7 Uji Diagnostik Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.7.1 Uji Normalitas Residual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
2.7.2 Uji Residual White Noise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.7.3 Uji Heteroskedastisitas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
```
2.8 Generalized Autoregressive Conditional Heteroskedasticity (GARCH) . . . 22
```
```
2.9 Mean Absolute Percentage Error (MAPE) . . . . . . . . . . . . . . . . . . . . . . . . . . 24
```
```
2.10 Mean-Variance Optimization (MVO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
```
2.11 Ukuran Risiko . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
```
2.12 Conditional Value-at-Risk (CVaR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
```
xi
BAB III METODOLOGI 31
3.1 Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.2 Variabel Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
3.3 Tahapan Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3.1 Studi Literatur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3.2 Pembentukan Model Biaya Utang . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.3.3 Preprocessing Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.4 Pembentukan Model ARIMA-GARCH . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.5 Input Optimasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.3.6 Proses Optimasi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.3.7 Portofolio Optimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.3.8 Analisis Hasil dan Pembahasan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.3.9 Penyusunan Tugas Akhir . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
3.4 Diagram Alir Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
BAB IV HASIL DAN PEMBAHASAN 37
4.1 Preprocessing Data dan Deskripsi Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
4.2 Identifikasi Model ARIMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
4.2.1 Stasioneritas Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.2.2 Penentuan Calon Model ARIMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.3 Pemodelan ARIMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
4.3.1 Estimasi dan Uji Signifikansi Parameter . . . . . . . . . . . . . . . . . . . . . . 53
4.3.2 Uji Diagnostik Residual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
4.3.3 Pemilihan Model Terbaik . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
4.4 Hasil Peramalan Tingkat Suku Bunga dan Nilai Tukar Mata Uang . . . . . 64
4.5 Pembentukan Model Biaya Utang dan Model Optimasi . . . . . . . . . . . . . . . 66
4.5.1 Pembentukan Model Biaya Utang . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.5.2 Pembentukan Batasan Model Optimasi Portofolio . . . . . . . . . . . . . . 69
4.5.3 Pembentukan Model Optimasi Portofolio dengan Mean-Variance
```
Optimization (MVO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
```
4.5.4 Pembentukan Model Optimasi Portofolio dengan Kendala Risiko
```
Conditional Value at Risk (CVaR) . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
```
4.6 Implementasi Optimasi Portofolio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.6.1 Perhitungan Parameter Input . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
4.6.2 Portofolio Aktual Pemerintah Indonesia . . . . . . . . . . . . . . . . . . . . . . . 79
```
4.6.3 Hasil Optimasi Menggunakan Mean-Variance Optimization (MVO) 80
```
```
4.6.4 Hasil Optimasi Menggunakan Conditional Value at Risk (CVaR) . 82
```
4.7 Analisis Hasil dan Pembahasan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
BAB V KESIMPULAN DAN SARAN 91
5.1 Kesimpulan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
5.2 Saran . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
DAFTAR PUSTAKA 95
DAFTAR LAMPIRAN 99
Lampiran 1 Listing Program MATLAB Model Cubic Spline . . . . . . . . . . . . . 99
Lampiran 2 Listing Program R pada RStudio untuk Uji ADF . . . . . . . . . . . 102
Lampiran 3 Listing Program R pada RStudio untuk Estimasi dan Uji
Signifikansi Parameter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
xii
Lampiran 4 Listing Program R pada RStudio untuk Uji Diagnostik Residual107
Lampiran 5 Listing Program R pada RStudio untuk Perhitungan MAPE . 110
Lampiran 6 Listing Program R pada RStudio untuk Plot Data Training
dan Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
Lampiran 7 Listing Program R pada RStudio untuk Hasil Peramalan . . . . 115
Lampiran 8 Listing Program MATLAB untuk Perhitungan Matriks
Varians-Kovarians . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
Lampiran 9 Listing Program MATLAB untuk Perhitungan Nilai Rmax pada
Model CVaR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
Lampiran 10 Listing Program MATLAB untuk Perhitungan CVaR
Portofolio Aktual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
Lampiran 11 Listing Program MATLAB untuk Model Mean-Variance
```
Optimization (MVO) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
```
Lampiran 12 Listing Program MATLAB untuk Model Conditional Value
```
at Risk (CVaR) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
```
Lampiran 13 Listing Program MATLAB untuk Efficient Frontier Model
MVO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
Lampiran 14 Listing Program MATLAB untuk Efficient Frontier Model
CVaR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
Lampiran 15 Data Deret Waktu Suku Bunga dan Nilai Tukar Mata Uang . . 134
Lampiran 16 Data Deret Waktu Hasil Transformasi Box-Cox . . . . . . . . . . . . . 136
Lampiran 17 Data Deret Waktu Hasil Differencing . . . . . . . . . . . . . . . . . . . . . 138
Lampiran 18 Gabungan Data Historis dan Data Hasil Peramalan . . . . . . . . . 140
Lampiran 19 Data Biaya Utang Valas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
Lampiran 20 Data Persentase Perubahan Biaya Utang Valas . . . . . . . . . . . . . 145
Lampiran 21 Output Minitab Plot Box-Cox . . . . . . . . . . . . . . . . . . . . . . . . . . . 147
Lampiran 22 Plot ACF dan PACF pada Data yang Telah Stasioner . . . . . . . 150
Lampiran 23 Plot Perbandingan Data Training dan Data Hasil Peramalan . 153
Lampiran 24 Matriks Varians-Kovarians Portofolio Utang Valas . . . . . . . . . . 155
Lampiran 25 Plot Efficient Frontier Model MVO dan CVaR . . . . . . . . . . . . . 156
UCAPAN TERIMA KASIH 157
BIODATA PENULIS 159
xiii
DAFTAR GAMBAR
Gambar 3.1 Diagram alir penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
Gambar 4.1 Hasil Interpolasi Cubic Spline Pada Variabel IR5 . . . . . . . . . . . . . . . 39
Gambar 4.2 Plot Time Series Suku Bunga . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
Gambar 4.3 Plot Time Series Nilai Tukar USD Terhadap EUR dan JPY . . . . . 41
Gambar 4.4 Plot Time Series Data Training Suku Bunga . . . . . . . . . . . . . . . . . . 43
Gambar 4.5 Plot Time Series Data Training Nilai Tukar USD Terhadap EUR
dan JPY . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
Gambar 4.6 Plot Box-Cox variabel IR1 sebelum transformasi . . . . . . . . . . . . . . . 44
Gambar 4.7 Plot Box-Cox data hasil transformasi pertama variabel IR1 . . . . . . 45
Gambar 4.8 Plot Data Training yang Telah Stasioner . . . . . . . . . . . . . . . . . . . . . . 48
Gambar 4.9 Plot ACF ∆Z1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Gambar 4.10 Plot PACF ∆Z1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
```
Gambar 4.11 Plot Data Training dan Hasil Model ARIMA(0, 1, 1) pada Suku
```
Bunga USD Tenor 5 Tahun . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
Gambar 4.12 Efficient Frontier MVO Berdasarkan Gabungan Data Historis dan
Hasil Peramalan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
Gambar 4.13 Efficient Frontier Model CVaR dengan Batasan Kementerian
Keuangan dan β = 90% . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
xv
DAFTAR TABEL
Tabel 2.1 Ringkasan Penelitian Terdahulu . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Tabel 2.5 Pola Teoretis ACF dan PACF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
Tabel 3.1 Variabel Penelitian . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
Tabel 4.1 Struktur Data IR5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
Tabel 4.2 Lebar Interval Data IR5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
Tabel 4.3 Koefisien Fungsi Interpolasi Cubic Spline Pada Interval i = 43 . . . . . . 38
Tabel 4.4 Hasil Interpolasi Cubic Spline Pada Variabel IR5 . . . . . . . . . . . . . . . . . 39
Tabel 4.5 Statistik Deskriptif Data Suku Bunga . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
Tabel 4.6 Statistik Deskriptif Data Nilai Tukar . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
Tabel 4.7 Hasil Transformasi Box-Cox . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
Tabel 4.8 Hasil Uji ADF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
Tabel 4.9 Rata-Rata Data Training yang Telah Stasioner . . . . . . . . . . . . . . . . . . . 49
Tabel 4.10 Calon Model ARIMA Berdasarkan Plot ACF dan PACF . . . . . . . . . . 52
Tabel 4.11 Hasil Estimasi dan Uji Signifikansi Parameter Model ARIMA . . . . . . 54
Tabel 4.12 Hasil Uji Normalitas Residual Model ARIMA . . . . . . . . . . . . . . . . . . . . 57
Tabel 4.13 Hasil Uji White Noise Residual Model ARIMA . . . . . . . . . . . . . . . . . . . 59
Tabel 4.14 Hasil Uji Heteroskedastisitas Residual Model ARIMA . . . . . . . . . . . . . 61
Tabel 4.15 Ringkasan Uji Diagnostik Residual Model ARIMA . . . . . . . . . . . . . . . . 62
```
Tabel 4.16 Perhitungan MAPE Model (0, 1, 1) pada ∆Z1 . . . . . . . . . . . . . . . . . . . . 63
```
Tabel 4.17 Hasil Perhitungan MAPE Model ARIMA . . . . . . . . . . . . . . . . . . . . . . . . 64
Tabel 4.18 Hasil Peramalan Tingkat Suku Bunga . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
Tabel 4.19 Hasil Peramalan Nilai Tukar Mata Uang . . . . . . . . . . . . . . . . . . . . . . . . 66
Tabel 4.20 Keterangan Indeks Model Biaya Utang Valas . . . . . . . . . . . . . . . . . . . . 67
Tabel 4.21 Kinerja Portofolio Aktual Pemerintah Indonesia . . . . . . . . . . . . . . . . . . 79
Tabel 4.22 Portofolio Hasil Optimasi MVO . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
Tabel 4.23 Portofolio Hasil Optimasi CVaR dengan Batasan Kementerian
Keuangan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82
Tabel 4.24 Portofolio Hasil Optimasi CVaR dengan Batasan Diperlebar 5% . . . . 84
Tabel 4.25 Portofolio Hasil Optimasi CVaR Tanpa Batasan . . . . . . . . . . . . . . . . . . 85
Tabel 4.26 Perbandingan Kinerja Portofolio Terbaik Hasil Optimasi CVaR . . . . . 86
Tabel 4.27 Perbandingan Portofolio Aktual, Model MVO, dan Model CVaR . . . . 88
Tabel 4.28 Perubahan Bobot Portofolio terhadap Portofolio Aktual . . . . . . . . . . . 89
Tabel 5.1 Komposisi Portofolio Optimal Model MVO dan CVaR . . . . . . . . . . . . 92
xvii
DAFTAR SIMBOL
```
Y : Nilai asli deret waktu sebelum transformasi
```
```
Yt : Nilai deret waktu pada periode ke-t
```
```
Y (λ) : Nilai deret waktu setelah transformasi Box–Cox
```
∇dYt : Hasil differencing orde-d
```
B : Operator backshift (BYt = Yt−1)
```
```
p, d, q : Orde ARIMA (AR, differencing, MA)
```
εt : Residual pada waktu ke-t
˜εt : Residual terstandarisasi
σ2t : Varians bersyarat pada waktu ke-t
ϕi, θj : Parameter AR/MA
α0, αi, βj : Parameter GARCH
```
P, Q : Orde GARCH (ARCH, GARCH)
```
```
x : Vektor bobot portofolio
```
μ : Vektor pengembalian yang diharapkan
Σ : Matriks varians-kovarians
```
f (x, y) : Fungsi kerugian portofolio
```
```
Ψ(x, α) : Probabilitas kumulatif kerugian
```
```
αβ (x) : β-Value-at-Risk (VaR)
```
```
ϕβ (x) : β-Conditional Value-at-Risk (CVaR)
```
xix
BAB I
PENDAHULUAN
1.1 Latar Belakang
Indonesia merupakan kekuatan ekonomi di kawasan pasar berkembang, sebagaimana
```
ditunjukkan oleh World Bank (2025) dalam laporannya mengenai prospek ekonomi
```
```
Indonesia. Hal tersebut juga diperkuat oleh data Badan Pusat Statistik (2025) yang
```
mencatat pertumbuhan ekonomi sebesar 5,04% dibandingkan dengan periode yang sama
pada tahun sebelumnya pada Triwulan III-2025, dengan nilai Produk Domestik Bruto
```
(PDB) atas dasar harga berlaku mencapai Rp6.060,0 triliun, meningkat dari Rp5.947,0
```
triliun pada triwulan sebelumnya. Meskipun fundamental perekonomian menunjukkan
kinerja yang baik, pemerintah tetap menghadapi tantangan yang berat dalam mengelola
```
Anggaran Pendapatan dan Belanja Negara (APBN). Kebutuhan belanja yang terus
```
meningkat untuk mendukung pembangunan nasional sering kali melampaui kapasitas
penerimaan negara sehingga menciptakan defisit anggaran. Tekanan pada neraca
pembayaran akibat pertumbuhan impor yang tinggi semakin menambah beban tersebut
```
dan menuntut pengelolaan fiskal yang baik (Badan Pusat Statistik, 2025). Fiskal
```
adalah segala aspek yang berkaitan dengan urusan keuangan negara, khususnya yang
mencakup pengelolaan pendapatan melalui perpajakan dan alokasi belanja pemerintah
```
dalam kerangka Anggaran Pendapatan dan Belanja Negara (APBN) untuk memengaruhi
```
stabilitas ekonomi makro. Merespon situasi tersebut, sejumlah kajian dari International
```
Monetary Fund (2025) dan Bank Indonesia (2025) menekankan pentingnya menjaga
```
keseimbangan ekonomi Indonesia terhadap gejolak eksternal. Langkah yang diambil oleh
pemerintah Indonesia adalah mempertimbangkan instrumen utang untuk menutup defisit
tersebut, namun penggunaannya harus tetap dikelola dengan strategi yang tepat agar
tidak membebani keuangan negara.
Utang pemerintah memegang peranan yang sangat penting dalam pendanaan
APBN, sebagaimana ditunjukkan oleh kontribusinya yang pernah mencapai 100,1%
```
selama periode 2004 hingga 2011 (Nasir, 2013). Dalam praktiknya, pemerintah
```
mengelola berbagai instrumen utang dengan karakteristik mata uang dan jatuh tempo
yang beragam, di mana keseluruhan kombinasi instrumen tersebut membentuk apa
```
yang disebut sebagai portofolio utang (Direktorat Jenderal Pengelolaan Utang, 2019).
```
Seiring berjalannya waktu, komposisi portofolio ini mengalami perubahan strategi yang
```
signifikan, terutama dalam porsi utang berdenominasi valuta asing atau valas (CNBC
```
```
Indonesia, 2025). Utang valuta asing (valas) merupakan utang yang dicatat dan
```
dibayarkan dalam mata uang selain rupiah, dan dalam beberapa tahun terakhir tren
penurunannya terlihat dari porsinya yang turun dari 33,5% pada 2020 menjadi 28,7%
pada 2024 dan 28,3% pada 2025. Sebaliknya, utang pemerintah saat ini didominasi
oleh denominasi rupiah yang porsinya meningkat dari 71,39% pada tahun 2024 menjadi
71,73% pada tahun 2025. Meskipun demikian, pemerintah menilai struktur utang valas
saat ini tetap stabil karena tingkat keterpaparannya terhadap perubahan kurs hanya
berada di kisaran 28%. Utang valas ini tetap dipertahankan karena perannya sebagai
pelengkap ketika kapasitas pendanaan domestik belum sepenuhnya mencukupi kebutuhan
pembiayaan negara. Pengelolaan komposisi antara utang domestik dan valas ini menjadi
1
kunci utama dalam menjaga keberlanjutan fiskal jangka panjang.
```
Menurut Avdjiev dkk. (2021), utang valas memiliki peran penting bagi negara
```
berkembang karena dapat memenuhi kebutuhan pendanaan yang tidak sepenuhnya dapat
dipenuhi oleh pasar domestik serta memberikan akses terhadap sumber dana yang lebih
beragam dan berbiaya relatif lebih murah dibandingkan dengan utang berdenominasi
rupiah. Selain itu, utang valas memungkinkan pemerintah memperoleh fleksibilitas
dalam mengatur pembiayaan dan dapat menjaga kestabilan pasar lokal ketika kapasitas
pendanaan lokal masih terbatas. Namun, komposisi utang valas yang tidak optimal
menghadirkan risiko pasar yang signifikan bagi ketahanan fiskal negara. Volatilitas suku
bunga global yang berubah setiap hari berpotensi memengaruhi biaya utang pemerintah
secara langsung dan tidak terduga. Risiko lainnya muncul dari fluktuasi nilai tukar mata
uang asing yang dapat meningkatkan beban pembayaran pokok dan bunga ketika terjadi
```
pelemahan nilai tukar rupiah (Direktorat Jenderal Pengelolaan Pembiayaan dan Risiko,
```
```
2025a), oleh karena itu pemerintah perlu melakukan optimasi portofolio instrumen utang
```
```
untuk menyeimbangkan biaya pembayaran dan risiko (Zenios dkk., 2019).
```
Di tengah dinamika ekonomi global yang penuh ketidakpastian, proyeksi suku bunga
dan nilai tukar menjadi hal yang penting dalam pengelolaan utang valas pemerintah.
Kedua variabel tersebut bersifat dinamis dan dapat memengaruhi biaya pembayaran
utang pada periode mendatang. Dalam peramalan nilai tukar, Babu dan Reddy
```
(2015) menunjukkan bahwa model ARIMA mampu menghasilkan akurasi yang lebih
```
baik dibandingkan beberapa metode machine learning pada peramalan nilai tukar INR
terhadap USD, GBP, EUR, dan JPY. Hasil tersebut menunjukkan bahwa model ARIMA
masih relevan digunakan untuk memodelkan pola rata-rata deret waktu keuangan.
Namun, data suku bunga dan nilai tukar juga sering memiliki volatilitas yang berubah-
ubah dari waktu ke waktu. Oleh karena itu, penambahan model GARCH diperlukan
untuk menangkap dinamika volatilitas tersebut. Hal ini sejalan dengan penelitian
```
Hassani dkk. (2020) dan Kim dkk. (2021) yang menegaskan pentingnya penggunaan
```
model GARCH dalam peramalan dan pemodelan volatilitas pada data suku bunga dan
pasar obligasi. Berdasarkan pertimbangan tersebut, penelitian ini menggunakan model
ARIMA-GARCH untuk meramalkan suku bunga dan nilai tukar sebagai dasar dalam
pembentukan portofolio optimal utang valas pemerintah.
Hasil peramalan suku bunga dan nilai tukar selanjutnya digunakan sebagai
dasar dalam pembentukan portofolio utang valas yang optimal. Salah satu
```
pendekatan yang dapat digunakan adalah Mean-Variance Optimization (MVO). Model
```
ini mempertimbangkan hubungan antara ekspektasi perubahan biaya pembayaran utang
dan risiko berdasarkan varians portofolio. Namun, varians memiliki keterbatasan karena
tidak secara khusus menggambarkan risiko pada kondisi ekstrem. Padahal, data keuangan
sering kali memiliki kemungkinan kejadian ekstrem yang lebih besar dibandingkan asumsi
```
distribusi normal (Alexander dan Baptista, 2004). Oleh karena itu, penelitian ini juga
```
```
menggunakan model optimasi dengan kendala risiko Conditional Value-at-Risk (CVaR).
```
CVaR digunakan karena mampu mengukur rata-rata kerugian atau beban biaya yang
terjadi pada kondisi terburuk pada tingkat kepercayaan tertentu. Dengan menggunakan
MVO dan CVaR, pembentukan portofolio utang valas dapat dianalisis dari dua sisi, yaitu
risiko berdasarkan varians dan risiko ekstrem yang mungkin terjadi akibat perubahan
suku bunga serta nilai tukar.
Berdasarkan permasalahan tersebut, penelitian ini berfokus pada optimasi portofolio
utang valas pemerintah Indonesia dengan mempertimbangkan potensi perubahan
2
suku bunga dan nilai tukar pada periode mendatang. Kebaruan penelitian ini
terletak pada penggabungan model peramalan ARIMA-GARCH dengan model optimasi
```
portofolio berbasis Mean-Variance Optimization (MVO) dan Conditional Value-at-Risk
```
```
(CVaR). Hasil peramalan suku bunga dan nilai tukar digunakan sebagai input dalam
```
pembentukan portofolio optimal, sehingga komposisi utang valas yang diperoleh tidak
hanya didasarkan pada data historis, tetapi juga mempertimbangkan kemungkinan
perubahan biaya pembayaran utang pada periode mendatang. Penelitian ini bertujuan
untuk menentukan komposisi portofolio optimal utang valas pemerintah Indonesia serta
menganalisis perbandingan kinerja model MVO dan model optimasi dengan kendala
risiko CVaR. Hasil penelitian ini diharapkan dapat memberikan dasar kuantitatif dalam
pengelolaan komposisi utang valas pemerintah yang lebih optimal dan tangguh terhadap
ketidakpastian pasar global.
1.2 Rumusan Masalah
Berdasarkan latar belakang yang telah diuraikan, permasalahan yang akan dibahas
dalam penelitian ini dirumuskan sebagai berikut.
1. Bagaimana hasil peramalan tingkat suku bunga dan nilai tukar mata uang asing
menggunakan model gabungan ARIMA-GARCH?
2. Bagaimana formulasi permasalahan optimasi portofolio utang valas Pemerintah
```
Indonesia ke dalam model Mean-Variance Optimization (MVO) dan model optimasi
```
```
portofolio dengan kendala risiko Conditional Value at Risk (CVaR)?
```
3. Bagaimana komposisi portofolio optimal serta perbandingan kinerja antara model
MVO dan model CVaR dengan mempertimbangkan potensi perubahan biaya utang
pada periode mendatang?
1.3 Batasan Masalah
Agar penelitian ini lebih terarah dan fokus pada permasalahan yang telah
dirumuskan, penulis menetapkan batasan-batasan masalah sebagai berikut.
1. Data yang digunakan adalah data sekunder harian pada periode 03 Juli 2017 hingga
24 November 2025, yang mencakup tingkat suku bunga utang untuk mata uang USD
```
(jangka waktu 5, 10, 15 tahun), EUR (jangka waktu 7, 10 tahun), dan JPY (jangka
```
```
waktu 5, 10 tahun), serta nilai tukar mata uang USD ke EUR dan USD ke JPY.
```
2. Objek analisis dibatasi pada portofolio utang pemerintah yang berdenominasi mata
```
uang asing (Valas), yaitu Dolar Amerika Serikat (USD), Euro (EUR), dan Yen
```
```
Jepang (JPY).
```
3. Nilai tukar yang digunakan dalam penelitian ini dinyatakan terhadap Dolar Amerika
```
Serikat (USD), bukan terhadap Rupiah. Hal ini karena pihak pengelola utang
```
negara berasumsi bahwa dana yang tersedia untuk pembayaran utang valas berada
dalam bentuk USD.
4. Peramalan dilakukan dalam rata-rata bulanan untuk proyeksi jangka menengah.
5. Faktor-faktor eksternal lain yang dapat memengaruhi tingkat suku bunga dan nilai
tukar diabaikan.
3
1.4 Tujuan Penelitian
Berdasarkan rumusan masalah yang telah ditetapkan, tujuan dari penelitian ini
adalah sebagai berikut.
1. Menghasilkan peramalan tingkat suku bunga dan nilai tukar mata uang asing
menggunakan model gabungan ARIMA-GARCH.
2. Memformulasikan permasalahan optimasi portofolio utang valas Pemerintah
```
Indonesia ke dalam model Mean-Variance Optimization (MVO) dan model optimasi
```
```
portofolio dengan kendala risiko Conditional Value at Risk (CVaR).
```
3. Menentukan komposisi portofolio optimal serta menganalisis perbandingan kinerja
antara model MVO dan model CVaR dengan mempertimbangkan potensi
perubahan biaya utang pada periode mendatang.
1.5 Manfaat Penelitian
Penelitian ini diharapkan dapat memberikan manfaat bagi pengelola utang negara
sebagai berikut.
1. Memberikan kontribusi sebagai kajian akademis mengenai penerapan metode
peramalan dan optimasi pada pengelolaan portofolio utang pemerintah, khususnya
karena pembahasan mengenai pengelolaan utang negara menggunakan pendekatan
optimasi masih relatif sedikit.
2. Memberikan gambaran mengenai perbedaan hasil optimasi portofolio utang valas
```
Pemerintah Indonesia menggunakan model Mean-Variance Optimization (MVO)
```
dan model optimasi portofolio dengan kendala risiko Conditional Value at Risk
```
(CVaR).
```
3. Memberikan rekomendasi strategi pengelolaan komposisi utang valas pemerintah
yang optimal dan tangguh dalam menghadapi ketidakpastian pasar global.
4
BAB II
TINJAUAN PUSTAKA
2.1 Penelitian Terdahulu
Pengelolaan utang valuta asing pemerintah merupakan persoalan yang tidak
hanya berkaitan dengan pemilihan instrumen pembiayaan, tetapi juga dengan upaya
mengendalikan biaya dan risiko yang muncul akibat perubahan suku bunga serta
nilai tukar mata uang. Oleh karena itu, komposisi portofolio utang valas perlu
ditentukan secara optimal agar beban pembayaran utang dapat diminimalkan dengan
tetap memperhatikan risiko yang mungkin terjadi. Sejumlah penelitian terdahulu
telah membahas persoalan tersebut melalui pendekatan kuantitatif, baik dalam bentuk
optimasi komposisi utang negara, pengukuran risiko ekstrem, maupun peramalan variabel
keuangan. Berikut merupakan penelitian terdahulu yang relevan sebagai state of the art
dari penelitian ini.
Penelitian mengenai optimasi komposisi utang negara dilakukan oleh Yavuz dan
```
G¨olba¸sı (2019) dengan objek utang negara Republik Turki. Penelitian tersebut membahas
```
persoalan penentuan strategi pinjaman dan komposisi utang yang optimal bagi pengelola
utang publik. Instrumen yang digunakan meliputi 24-months TL zero-coupon, 5-
years TL fixed-rate, 10-years CPI-indexed TL, 7-years floating-rate TL, dan 10-years
USD fixed-rate. Keberadaan instrumen 10-years USD fixed-rate menunjukkan bahwa
penelitian tersebut telah memasukkan unsur utang dalam valuta asing. Metode yang
```
digunakan adalah Turkish Treasury Debt Simulation Model (TDSM), adaptasi Modern
```
```
Portfolio Theory, serta ukuran risiko Conditional Cost-at-Risk (CCaR) dan Marginal
```
```
Conditional Cost-at-Risk (MCCaR). TDSM digunakan sebagai program simulasi untuk
```
memperkirakan pergerakan ekonomi pada masa mendatang, sehingga total beban utang
dan batas risiko terburuk pada akhir tahun kelima dapat dihitung. Selanjutnya, adaptasi
Modern Portfolio Theory digunakan sebagai dasar perhitungan untuk menentukan porsi
setiap jenis utang dalam portofolio. Pendekatan ini berfungsi mencari kombinasi
persentase utang yang menghasilkan biaya dan risiko terendah bagi negara. CCaR
digunakan sebagai ukuran risiko total portofolio untuk memperkirakan beban utang
paling besar yang harus ditanggung negara ketika kondisi ekonomi berada pada skenario
yang sangat buruk. Sementara itu, MCCaR digunakan sebagai ukuran risiko tambahan
untuk setiap jenis utang, yaitu untuk melihat perubahan risiko total apabila porsi suatu
jenis utang ditambah atau dikurangi. Hasil penelitian menunjukkan bahwa komposisi
optimal terdiri atas 60% zero-coupon, 25% fixed-rate, 5% floating-rate, 5% CPI-indexed
TL, dan 5% obligasi valas USD. Komposisi tersebut mampu menurunkan risiko sebesar
13% dan biaya sebesar 9% dibandingkan portofolio berbobot sama. Perbedaan penelitian
```
yang dilakukan oleh Yavuz dan G¨olba¸sı (2019) dengan penelitian yang dilakukan dalam
```
tugas akhir ini terletak pada cakupan instrumen, sumber data, dan kerangka analisis
```
yang digunakan. Penelitian Yavuz dan G¨olba¸sı (2019) menggunakan instrumen utang
```
valas yang masih terbatas pada satu mata uang, yaitu USD. Sementara itu, penelitian ini
menggunakan portofolio utang valas pemerintah Indonesia yang terdiri atas instrumen
berdenominasi USD, EUR, dan JPY.
```
Selanjutnya, Yang dkk. (2022) membahas optimasi portofolio utang pemerintah
```
5
dengan mempertimbangkan risiko ekstrem pada pemerintah daerah di Tiongkok.
Penelitian tersebut berangkat dari meningkatnya tekanan pembayaran utang akibat
akumulasi penerbitan obligasi jangka panjang yang berpotensi menimbulkan risiko
likuiditas pada masa mendatang. Tujuan penelitian tersebut adalah menentukan
komposisi portofolio penerbitan obligasi yang optimal dengan meminimalkan ekspektasi
biaya serta tetap memperhatikan batasan risiko likuiditas dan risiko deviasi biaya. Metode
yang digunakan adalah multi-period stochastic programming. Risiko likuiditas diukur
```
dengan Conditional Payment-at-Risk (CPaR), sedangkan risiko deviasi biaya ekstrem
```
```
diukur dengan Conditional Value-at-Risk (CVaR). Hasil penelitian menunjukkan bahwa
```
pengendalian CPaR dan CVaR mampu menekan risiko likuiditas tanpa menurunkan
```
efisiensi biaya secara drastis. Perbedaan penelitian yang dilakukan oleh Yang dkk. (2022)
```
dengan penelitian yang dilakukan dalam tugas akhir ini terletak pada objek penelitian,
```
jenis risiko, dan model optimasi yang digunakan. Penelitian Yang dkk. (2022) berfokus
```
pada penerbitan obligasi pemerintah daerah di Tiongkok dengan mempertimbangkan
risiko likuiditas dan risiko deviasi biaya. Berbeda dengan penelitian tersebut, penelitian
ini berfokus pada portofolio utang valas pemerintah Indonesia yang memiliki risiko
```
perubahan suku bunga dan nilai tukar. Selain itu, penelitian Yang dkk. (2022)
```
menggunakan CVaR sebagai ukuran risiko dalam model pemrograman stokastik multi-
periode. Berbeda dengan penelitian tersebut, penelitian ini menggunakan CVaR sebagai
kendala risiko dalam optimasi portofolio utang valas dan membandingkannya dengan
pendekatan Mean-Variance Optimization.
Selain aspek optimasi, pembentukan portofolio utang valas juga membutuhkan
estimasi terhadap variabel pasar yang memengaruhi biaya pembayaran utang, terutama
nilai tukar. Penelitian mengenai peramalan nilai tukar menggunakan model ARIMA-
```
GARCH dilakukan oleh Zhu (2025) dengan menggunakan data historis harian nilai tukar
```
USD/JPY periode Desember 1974 hingga Desember 2024. Penelitian tersebut bertujuan
mengembangkan dan mengevaluasi kemampuan model hibrida ARIMA-GARCH dalam
memproyeksikan pergerakan nilai tukar. Model ARIMA digunakan untuk memodelkan
rata-rata kondisional, sedangkan model GARCH digunakan untuk memodelkan varians
kondisional dan menangkap perubahan volatilitas dari waktu ke waktu. Hasil penelitian
menunjukkan bahwa model ARIMA-GARCH mampu memproyeksikan tren umum nilai
tukar dan menangkap karakteristik volatilitas seperti volatility clustering. Perbedaan
```
penelitian yang dilakukan oleh Zhu (2025) dengan penelitian yang dilakukan dalam tugas
```
akhir ini terletak pada objek penelitian dan pemanfaatan hasil peramalan. Penelitian Zhu
```
(2025) berfokus pada peramalan nilai tukar USD/JPY secara univariat. Berbeda dengan
```
penelitian tersebut, penelitian ini menggunakan beberapa variabel suku bunga dan nilai
tukar mata uang yang digunakan sebagai input dalam pembentukan portofolio optimal
utang valas menggunakan pendekatan Mean-Variance Optimization dan model optimasi
dengan kendala risiko CVaR.
Berdasarkan uraian penelitian terdahulu, dapat diketahui bahwa setiap penelitian
telah memberikan kontribusi pada aspek yang berbeda. Penelitian Yavuz dan G¨olba¸sı
```
(2019) telah membahas optimasi komposisi utang negara dengan mempertimbangkan
```
```
biaya dan risiko. Penelitian Yang dkk. (2022) telah menggunakan CVaR untuk
```
mengendalikan risiko ekstrem dalam optimasi portofolio utang pemerintah. Penelitian
```
Zhu (2025) telah menggunakan model ARIMA-GARCH untuk memodelkan rata-rata
```
dan volatilitas nilai tukar. Namun, ketiga penelitian tersebut masih menyisakan celah
karena aspek peramalan dan optimasi portofolio utang belum dibahas secara terintegrasi.
6
Penelitian ini mengisi celah tersebut dengan menggabungkan hasil peramalan suku
bunga dan nilai tukar sebagai input dalam pembentukan portofolio optimal utang
valas pemerintah Indonesia. Selain itu, penelitian ini juga membandingkan pendekatan
Mean-Variance Optimization dan model optimasi dengan kendala risiko CVaR. Dengan
demikian, penelitian ini tidak hanya menerapkan metode optimasi secara numerik,
tetapi juga membangun kerangka analisis yang menghubungkan peramalan variabel pasar
dengan pengambilan keputusan portofolio utang valas pemerintah. Ringkasan penelitian
terdahulu disajikan pada Tabel 2.1.
Tabel 2.1 Ringkasan Penelitian Terdahulu
No. Judul Penelitian Metode Fokus Penelitian
1
Optimal Composition
of Sovereign Debt: An
Adaptation from Modern
```
Portfolio Theory (Yavuz
```
```
dan G¨olba¸sı, 2019)
```
Turkish Treasury
Debt Simulation Model
```
(TDSM) digunakan sebagai
```
program simulasi untuk
memperkirakan pergerakan
ekonomi pada masa
mendatang dan menghitung
beban utang pada akhir
periode perencanaan.
Adaptasi Modern Portfolio
Theory digunakan sebagai
dasar pembentukan efficient
frontier untuk memperoleh
kombinasi instrumen utang
yang efisien. Conditional
```
Cost-at-Risk (CCaR)
```
digunakan untuk mengukur
risiko total portofolio
pada kondisi ekonomi
terburuk, sedangkan
Marginal Conditional
```
Cost-at-Risk (MCCaR)
```
digunakan untuk melihat
perubahan risiko akibat
perubahan porsi setiap
instrumen utang.
Menentukan komposisi
utang negara Republik
Turki yang optimal dari
sudut pandang pemerintah
sebagai pengelola utang.
Fokus penelitian diarahkan
pada pencarian kombinasi
instrumen utang yang
mampu menurunkan
biaya dan risiko secara
bersamaan. Instrumen yang
dikaji mencakup obligasi
dalam mata uang lokal
dan obligasi valuta asing
berdenominasi USD.
```
(Tabel dilanjutkan pada halaman berikutnya)
```
7
```
Tabel 2.1 Ringkasan Penelitian Terdahulu (Lanjutan)
```
No. Judul Penelitian Metode Fokus Penelitian
2
Optimal Bond Issuance
with Cost and Liquidity
Constraints for Chinese
Local Governments: A
Multi-Period Stochastic
Programming Approach
```
(Yang dkk., 2022)
```
Multi-period stochastic
programming digunakan
sebagai model optimasi
untuk menentukan
keputusan penerbitan
obligasi pada beberapa
periode. Simulasi suku
bunga digunakan untuk
membentuk skenario biaya
pembayaran obligasi.
Conditional Payment-at-
```
Risk (CPaR) digunakan
```
untuk mengukur dan
membatasi risiko likuiditas,
sedangkan Conditional
```
Value-at-Risk (CVaR)
```
digunakan untuk mengukur
risiko deviasi biaya ekstrem
pada portofolio obligasi.
Menentukan komposisi
penerbitan obligasi
pemerintah daerah di
Tiongkok yang mampu
meminimalkan ekspektasi
biaya dengan tetap menjaga
risiko likuiditas dan risiko
deviasi biaya. Fokus
penelitian terletak pada
pengelolaan struktur
jatuh tempo obligasi
agar pembayaran utang
pada masa mendatang
tetap terkendali dan tidak
menimbulkan tekanan
likuiditas yang berlebihan.
3
Implementation of the
ARIMA-GARCH Model on
Exchange Rate Forecasting
```
(Zhu, 2025)
```
Model ARIMA
digunakan untuk
memodelkan rata-rata
kondisional dan pola
pergerakan nilai tukar.
Model GARCH digunakan
untuk memodelkan
varians kondisional serta
menangkap perubahan
volatilitas dari waktu ke
waktu. Uji diagnostik
residual digunakan untuk
mengevaluasi kelayakan
model, terutama dalam
melihat stasioneritas,
sifat white noise, dan
kemampuan model
menangkap dinamika
volatilitas.
Meramalkan nilai
tukar USD/JPY dengan
mempertimbangkan pola
rata-rata dan volatilitas
data. Fokus penelitian
diarahkan pada kemampuan
model ARIMA-GARCH
dalam menangkap dinamika
nilai tukar, khususnya
pada data keuangan
yang memiliki volatilitas
berubah-ubah dan gejala
volatility clustering.
Berdasarkan Tabel 2.1, kebaruan penelitian ini terletak pada pengembangan kerangka
analisis yang mengintegrasikan hasil peramalan suku bunga dan nilai tukar dengan
pembentukan portofolio optimal utang valas pemerintah Indonesia. Peramalan dilakukan
menggunakan model ARIMA-GARCH untuk memperoleh gambaran pergerakan variabel
pasar yang memengaruhi biaya pembayaran utang. Hasil peramalan tersebut kemudian
digunakan sebagai input dalam model optimasi portofolio. Pembentukan portofolio
dilakukan dengan pendekatan Mean-Variance Optimization dan model optimasi dengan
kendala risiko CVaR. Kontribusi penelitian ini adalah memberikan dasar kuantitatif dalam
8
menentukan komposisi utang valas pemerintah yang mempertimbangkan ekspektasi
perubahan biaya pembayaran utang dan risiko secara bersamaan. Dengan demikian,
penelitian ini tidak hanya melakukan eksperimen numerik, tetapi juga menyusun kerangka
pengambilan keputusan untuk mendukung pengelolaan portofolio utang valas pemerintah
Indonesia.
2.2 Portofolio Utang Valas
```
Utang valuta asing (valas) adalah kewajiban negara kepada pihak luar negeri yang
```
```
pembayarannya menggunakan mata uang asing (Fadillah dkk., 2025; Nasir, 2013). Utang
```
ini sangat bergantung pada arah nilai tukar dan suku bunga dunia. Melemahnya
mata uang dalam negeri atau naiknya suku bunga dapat memperbesar beban pinjaman
```
secara tiba-tiba sehingga mengancam keuangan negara (Direktorat Jenderal Pengelolaan
```
```
Pembiayaan dan Risiko, 2025b; Fadillah dkk., 2025). Pada periode Maret 2005–September
```
2014, guncangan penurunan nilai tukar rupiah terbukti mendorong kenaikan rasio utang
pemerintah sehingga menunjukkan adanya pembengkakan beban utang. Namun, pada
periode Oktober 2014–Maret 2019 terlihat pola yang berbeda karena pelemahan rupiah
justru diikuti oleh penurunan rasio utang. Kondisi ini terjadi karena pemerintah
berhasil menekan porsi utang valuta asing terhadap total utang dari 54,3% pada tahun
```
2005 menjadi 41,6% pada tahun 2018 (Direktorat Jenderal Pengelolaan Utang, 2019).
```
Meskipun porsi utang valas menurun, perubahan komposisi instrumen dari pinjaman ke
```
Surat Berharga Negara (SBN) valas membuat portofolio utang menjadi lebih sensitif
```
terhadap perubahan kondisi pasar, oleh karena itu, penyusunan komposisi utang valas
yang optimal menjadi langkah penting untuk mengurangi dampak perubahan nilai tukar
```
dan suku bunga terhadap beban pembayaran utang (Direktorat Jenderal Pengelolaan
```
```
Utang, 2019; Fadillah dkk., 2025).
```
```
Penyusunan komposisi porsi pembayaran utang valuta asing (valas) dikenal sebagai
```
```
portofolio utang valas. Tujuan utamanya adalah melakukan lindung nilai (hedging)
```
dengan membagi pembayaran jenis mata uang untuk mengurangi dampak pasar yang
tidak stabil. Sebagai contoh, Pemerintah Indonesia memiliki total kewajiban utang
valas sebesar Rp105 triliun yang terdiri dari utang valas berdenominasi Dolar Amerika
```
Serikat (USD) sebesar Rp70 triliun, Euro (EUR) sebesar Rp20 triliun, dan Yen Jepang
```
```
(JPY) sebesar Rp15 triliun. Apabila alokasi anggaran pembayaran ditetapkan sebesar
```
Rp50 triliun portofolio komposisi pembayarannya 40% untuk USD, 35% untuk EUR, dan
25% untuk JPY. Berdasarkan komposisi tersebut, alokasi pembayaran didistribusikan
sesuai pembagian porsi menjadi Rp20 triliun untuk USD, Rp17,5 triliun untuk EUR,
dan Rp12,5 triliun untuk JPY. Setelah pembayaran, sisa kewajiban utang menjadi Rp50
```
triliun (USD), Rp2,5 triliun (EUR), dan Rp2,5 triliun (JPY). Sehingga total sisa utang
```
valas Pemerintah Indonesiamenjadi Rp55 triliun. Melalui pembagian ini, risiko pelemahan
Rupiah terhadap fluktuasi satu mata uang tunggal dapat diperkecil, oleh karena itu
penentuan porsi mata uang yang tepat sangat penting untuk menjaga kestabilan beban
```
utang (Direktorat Jenderal Pengelolaan Utang, 2019; Fadillah dkk., 2025).
```
2.3 Interpolasi Cubic Spline
Pada tahap pengecekan data, ditemukan adanya data bulanan yang tidak lengkap
di tengah periode pengamatan pada variabel tingkat suku bunga EUR tenor 10 tahun.
Oleh karena itu, diperlukan metode interpolasi untuk memperkirakan nilai yang hilang
berdasarkan pola data sebelum dan sesudah periode tersebut. Dalam menangani
permasalahan tersebut, penelitian ini menggunakan interpolasi Cubic Spline karena
9
metode ini mampu menghasilkan kurva yang lebih mulus dan menjaga kesinambungan
```
pola perubahan data. Menurut Imron dkk. (2022), metode interpolasi kubik bagian
```
```
demi bagian (piecewise cubic spline) merupakan metode yang paling banyak diterapkan
```
dibandingkan metode linear atau kuadratik, karena memiliki representasi yang sederhana
namun menghasilkan tampilan kurva yang paling mulus.
Tujuan utama dari metode ini adalah menurunkan polinomial orde ketiga untuk
masing-masing interval di antara titik-titik data. Jika diketahui n titik data, maka
```
terdapat n − 1 interval. Menurut Imron dkk. (2022), persamaan polinomial kubik untuk
```
interval ke-i didefinisikan sebagai berikut:
```
fi(x) = ai + bi(x − xi) + ci(x − xi)2 + di(x − xi)3, (2.1)
```
dengan keterangan
```
fi(x) : fungsi cubic spline pada interval ke-i,
```
```
i : indeks interval, dengan i = 1, 2, . . . , n − 1,
```
```
n : banyaknya titik data yang diketahui,
```
```
x : variabel bebas yang berada pada interval [xi, xi+1],
```
```
xi : titik data ke-i sekaligus batas bawah interval ke-i,
```
```
xi+1 : titik data ke-(i + 1) sekaligus batas atas interval ke-i,
```
ai, bi, ci, di : koefisien cubic spline pada interval ke-i.
Pada penelitian ini, digunakan asumsi tambahan berupa natural spline. Menurut
```
Imron dkk. (2022), kondisi natural spline mengasumsikan turunan kedua pada titik data
```
awal dan akhir sama dengan nol, sehingga secara matematis ditulis sebagai c1 = 0 dan
```
cn = 0. Koefisien spline (ai, bi, ci, di) ditentukan dengan menyelesaikan sistem persamaan
```
```
linear. Berdasarkan penurunan rumus yang dilakukan oleh Imron dkk. (2022), nilai ci
```
```
untuk i = 2, . . . , n − 1 diperoleh dengan menyelesaikan sistem Persamaan (2.2) berikut:
```
```
hi−1ci−1 + 2(hi−1 + hi)ci + hici+1 = 3
```
```
(
```
fi+1 − fi
hi
−
fi − fi−1
hi−1
```
)
```
```
, (2.2)
```
```
dimana hi = xi+1 − xi. Sistem Persamaan (2.2) dapat dituliskan dalam bentuk matriks
```
sebagai berikut:





1 0 0 · · · 0
```
h1 2(h1 + h2) h2 · · · 0
```
... . . . . . . . . . ...
```
0 · · · hn−2 2(hn−2 + hn−1) hn−1
```
0 0 0 · · · 1










c1
c2
...
cn−1
cn





=






0
3
```
( f3−f2
```
h2 −
f2−f1
h1
```
)
```
...
3
```
( fn−fn−1
```
hn−1 −
fn−1−fn−2
hn−2
```
)
```
0






.
```
Setelah nilai ci diketahui, koefisien lainnya (ai, bi, di) dapat dihitung menggunakan
```
```
persamaan (2.3) berikut:
```
```
ai = fi,
```
```
bi =
```
fi+1 − fi
hi
−
hi
3
```
(2ci + ci+1),
```
```
di =
```
ci+1 − ci
3hi
.
```
(2.3)
```
10
Setelah diperoleh seluruh koefisien tersebut, kurva interpolasi yang terbentuk akan
menghubungkan titik-titik data suku bunga dan nilai tukar yang hilang dengan pola
yang mulus dan kontinu.
```
2.4 Autoregressive Integrated Moving Average (ARIMA)
```
```
Autoregressive Integrated Moving Average (ARIMA) pertama kali diperkenalkan
```
oleh Box dan Jenkins pada tahun 1970, dan model ini kemudian dikenal luas sebagai
model Box–Jenkins. Model ARIMA merupakan gabungan komponen autoregressive
```
(AR), differencing (I), dan moving average (MA) yang dinotasikan secara umum sebagai
```
```
ARIMA(p, d, q) (Box dkk., 2015). Notasi tersebut merepresentasikan orde spesifik
```
dari masing-masing bagian, dimana p adalah orde untuk bagian autoregressive, d
menunjukkan tingkat differencing yang diperlukan, dan q adalah orde untuk moving
average. Berdasarkan susunan komponen tersebut, model ARIMA memiliki bentuk
```
khusus sebagai berikut (Box dkk., 2015).
```
1. Model ARIMA(p, 0, 0)
```
Model ARIMA(p, 0, 0) lebih sering dikenal sebagai model AR(p) yang mengasumsikan
```
bahwa nilai saat ini bergantung secara linear pada beberapa nilai masa lalu. Model
```
AR(p) dirumuskan sebagai berikut:
```
```
Yt = c + ϕ1Yt−1 + ϕ2Yt−2 + · · · + ϕpYt−p + εt. (2.4)
```
Pada model tersebut, Yt adalah nilai observasi deret waktu pada periode ke-t, c
adalah konstanta, ϕi adalah parameter autoregressive ke-i yang menunjukkan bobot
pengaruh data masa lalu, dan εt adalah residual pada periode ke-t. Konstanta c dapat
dihilangkan jika data yang sudah stasioner berfluktuasi di sekitar nol.
2. Model ARIMA(0, 0, q)
```
Model ARIMA(0, 0, q) disebut sebagai MA(q) yang hanya memperhitungkan pengaruh
```
```
residual dari beberapa periode sebelumnya. Bentuk model MA(q) dirumuskan sebagai
```
```
berikut:
```
```
Yt = c + εt − θ1εt−1 − θ2εt−2 − · · · − θqεt−q. (2.5)
```
```
Pada persamaan (2.5), c merepresentasikan konstanta yang menunjukkan rata-rata
```
proses data, dan θj adalah parameter moving average ke-j yang menunjukkan bobot
```
pengaruh residual masa lalu. Sama halnya dengan model AR(p), konstanta c dapat
```
dihilangkan jika data yang sudah stasioner memiliki rata-rata di sekitar nol.
3. Model ARIMA(p, 0, q)
```
Model ARIMA(p, 0, q), atau lebih umum ditulis sebagai ARMA(p, q), dibentuk dengan
```
```
menggabungkan komponen AR pada persamaan (2.4) dan komponen MA pada
```
```
persamaan (2.5). Bentuk model ARMA(p, q) dirumuskan sebagai berikut:
```
```
Yt = c + ϕ1Yt−1 + · · · + ϕpYt−p + εt − θ1εt−1 − · · · − θqεt−q. (2.6)
```
```
Pada persamaan (2.6), c adalah konstanta, ϕi adalah parameter autoregressive ke-i,
```
θj adalah parameter moving average ke-j, dan εt adalah residual pada periode ke-t.
Konstanta c dapat dihilangkan jika data yang sudah stasioner memiliki rata-rata di
sekitar nol.
11
4. Model ARIMA(p, d, q)
```
Terakhir, model ARIMA(p, d, q) digunakan untuk data yang tidak stasioner, sehingga
```
perlu didiferensiasi sebanyak d kali agar menjadi stasioner. Proses diferensiasi ini
```
melibatkan operator ∆, dimana ∆Yt = Yt − Yt−1. Bentuk model ARIMA(p, d, q)
```
dirumuskan sebagai berikut:
```
∆dYt = c + ϕ1∆dYt−1 + · · · + ϕp∆dYt−p + εt − θ1εt−1 − · · · − θqεt−q, (2.7)
```
dimana
```
∆dYt = (1 − B)dYt,
```
```
BdYt = Yt−d.
```
```
Pada persamaan (2.7), ∆dYt merepresentasikan operasi differencing orde d yang
```
diterapkan pada data Yt untuk mencapai kondisi stasioner. Sama halnya dengan model
```
ARMA(p, q), konstanta c dapat dihilangkan jika data yang sudah stasioner memiliki
```
rata-rata di sekitar nol.
```
Keempat model umum tersebut diasumsikan mempunyai residual (εt) yang berdistribusi
```
Normal White Noise yang dinotasikan sebagai berikut:
```
εt ∼ N (0, σ2), (2.8)
```
dimana untuk setiap t pada εt saling bebas dan mempunyai distribusi probabilitas yang
```
sama sesuai dengan persamaan (2.8).
```
2.5 Identifikasi Model ARIMA
Identifikasi model ARIMA dilakukan untuk menentukan orde model yang sesuai
berdasarkan karakteristik data deret waktu. Tahapan ini diawali dengan pemeriksaan
kestasioneran data, baik terhadap varians maupun rata-rata. Apabila data belum
stasioner terhadap varians, maka dilakukan transformasi. Selanjutnya, apabila data
belum stasioner terhadap rata-rata, maka dilakukan proses differencing. Setelah data
stasioner, identifikasi orde model ARIMA dilakukan melalui analisis plot Autocorrelation
```
Function (ACF) dan Partial Autocorrelation Function (PACF).
```
2.5.1 Stasioneritas Data terhadap Varians
Stasioneritas adalah kondisi ketika sifat statistik data tidak berubah seiring waktu
```
(Wei, 2006). Salah satu bentuk stasioneritas yang perlu dipenuhi dalam pemodelan deret
```
waktu adalah stasioneritas terhadap varians. Suatu data dikatakan stasioner terhadap
varians apabila sebaran data relatif konstan sepanjang waktu. Dengan kata lain, data
dikatakan stasioner terhadap varians apabila
```
V ar(Yt) = konstan.
```
```
Menurut Box dkk. (2015), data yang tidak stasioner terhadap varians dapat
```
ditransformasikan menggunakan transformasi Box–Cox berikut:
```
Y (λ) =
```



Y λ − 1
λ
, λ̸ = 0,
```
ln(Y ), λ = 0.
```
```
(2.9)
```
12
```
Pada Persamaan (2.9), Y (λ) adalah nilai deret waktu setelah transformasi, Y adalah
```
nilai asli deret waktu, dan λ adalah parameter transformasi Box–Cox yang menentukan
jenis transformasi yang diterapkan. Berdasarkan sifat operator varians, penjabaran
transformasi untuk λ̸ = 0 adalah sebagai berikut:
V ar
```
(
```
Y λ − 1
λ
```
)
```
= V ar
```
(
```
Y λ
λ
−
1
λ
```
)
```
= V ar
```
(
```
Y λ
λ
```
)
```
=
1
λ2
```
V ar(Y λ).
```
Karena λ adalah konstanta, maka 1λ2 juga merupakan konstanta. Sehingga berlaku
hubungan berikut:
1
λ2
```
V ar(Y λ) = konstan
```
```
V ar(Y λ) = konstan.
```
Dengan demikian, rumus transformasi Box–Cox dapat direduksi menjadi bentuk berikut:
```
Y (λ) =
```



Y λ, λ̸ = 0,
```
ln(Y ), λ = 0.
```
```
(2.10)
```
Nilai λ pada transformasi Box–Cox digunakan untuk menentukan bentuk
transformasi yang paling sesuai agar varians data menjadi lebih stabil. Dalam prosesnya,
beberapa kemungkinan nilai λ dicoba, kemudian setiap nilai tersebut digunakan untuk
```
mentransformasi data menjadi Y (λ)i . Selanjutnya, dihitung simpangan baku dari data
```
hasil transformasi dengan rumus berikut:
sλ =
√√
√√ 1
n − 1
n∑
```
i=1
```
```
(
```
```
Y (λ)i − ¯Y (λ)
```
```
)2
```
,
```
dengan sλ adalah simpangan baku data hasil transformasi untuk nilai λ tertentu, Y (λ)i
```
```
adalah data ke-i setelah transformasi, ¯Y (λ) adalah rata-rata data hasil transformasi, dan
```
n adalah banyaknya data. Nilai λ yang dipilih adalah nilai yang menghasilkan simpangan
```
baku terkecil. Menurut Wei (2006), data dianggap stasioner terhadap varians jika nilai λ
```
yang terpilih nilainya 1.
2.5.2 Stasioneritas Data terhadap Mean
Selain stasioner terhadap varians, data deret waktu juga perlu stasioner terhadap
mean. Stasioner terhadap mean berarti rata-rata data bersifat konstan sepanjang waktu.
Model ARIMA memerlukan asumsi bahwa data stasioner terhadap varians dan mean.
Data yang tidak stasioner terhadap varians dan mean dapat menyebabkan kesulitan dalam
```
peramalan karena pola dan trennya sulit untuk diprediksi (Thakkar dan Chaudhari, 2021).
```
Salah satu metode statistik yang umum digunakan untuk menguji stasioneritas data
```
terhadap mean adalah uji Augmented Dickey–Fuller (ADF). Uji ADF bertujuan untuk
```
13
```
mendeteksi keberadaan akar unit (unit root) sebagai indikasi ketidakstasioneran data.
```
```
Menurut Gujarati dan Porter (2009), prosedur pengujian ini didasarkan pada model
```
regresi yang dirumuskan sebagai berikut:
∆Yt = β1 + β2t + δYt−1 +
m∑
```
i=1
```
```
αi∆Yt−i + et, (2.11)
```
dengan keterangan
∆Yt : perubahan nilai data pada waktu ke-t, dengan ∆Yt = Yt − Yt−1,
```
Yt : nilai data pada waktu ke-t,
```
```
Yt−1 : nilai data pada waktu ke-(t − 1),
```
β1 : konstanta atau intersep,
β2 : koefisien tren waktu,
```
t : indeks waktu,
```
δ : koefisien uji akar unit yang menjadi fokus pengujian,
αi : koefisien komponen augmented yang menangkap autokorelasi,
```
m : banyaknya lag yang digunakan,
```
```
et : residual pada waktu ke-t.
```
```
Langkah-langkah uji Augmented Dickey–Fuller (ADF) adalah sebagai berikut:
```
```
(1) Hipotesis:
```
```
H0 : δ = 0, sehingga data tidak stasioner atau terdapat akar unit,
```
```
H1 : δ < 0, sehingga data stasioner atau tidak terdapat akar unit.
```
```
(2) Statistik Uji:
```
Statistik uji ADF dirumuskan sebagai rasio antara estimasi koefisien δ terhadap
galat bakunya, yang dinyatakan sebagai
```
ADFhitung =
```
ˆδ
```
SE(ˆδ)
```
```
. (2.12)
```
```
Pada Persamaan (2.12), ˆδ adalah nilai estimasi koefisien uji akar unit yang diperoleh
```
```
dari regresi pada Persamaan (2.11), dan SE(ˆδ) adalah galat baku atau standard
```
error dari estimasi tersebut.
```
(3) Daerah Kritis:
```
```
Nilai kritis uji (ADFtabel) ditentukan berdasarkan tabel MacKinnon (MacKinnon,
```
```
2010) pada tingkat signifikansi α. Kriteria pengujian adalah sebagai berikut:
```
ADFhitung < ADFtabel maka H0 ditolak atau data stasioner,
ADFhitung ≥ ADFtabel maka H0 gagal ditolak atau data tidak stasioner.
```
(4) Keputusan:
```
Keputusan pengujian ditentukan berdasarkan perbandingan antara nilai ADFhitung
dan ADFtabel sesuai dengan daerah kritis yang telah ditetapkan.
14
Jika data tidak stasioner terhadap mean, maka penanganan dapat dilakukan melalui
```
proses differencing. Proses differencing dinyatakan dalam Persamaan (2.13).
```
```
∆dYt = (1 − B)dYt. (2.13)
```
```
Pada persamaan (2.13), ∆dYt menunjukkan hasil differencing orde-d, dengan B sebagai
```
operator backshift yang didefinisikan sebagai BYt = Yt−1.
2.5.3 Plot ACF & PACF
Identifikasi struktur model deret waktu dilakukan dengan menganalisis pola visual
```
pada plot Autocorrelation Function (ACF) dan Partial Autocorrelation Function (PACF).
```
Fungsi utama ACF adalah mengukur seberapa kuat hubungan antara suatu data deret
waktu dengan nilai masa lalunya untuk mengidentifikasi orde model Moving Average
```
(MA). Berdasarkan Wei (2006), ACF pada lag k (ˆρk) dihitung menggunakan estimator
```
koefisien autokorelasi sampel yang dirumuskan sebagai
ˆρk =
```
Cov(Yt, Yt+k)
```
```
Var(Yt)
```
ˆρk =
∑n−k
```
t=1 (Yt − ¯Y )(Yt+k − ¯Y )∑
```
```
nt=1(Yt − ¯Y )2 , (2.14)
```
dengan keterangan
ˆρk : nilai autokorelasi sampel pada lag ke-k,
```
Yt : nilai data deret waktu pada waktu ke-t,
```
```
Yt+k : nilai data deret waktu pada waktu ke-(t + k),
```
¯Y : rata-rata dari seluruh data deret waktu,
```
k : lag atau selisih waktu pengamatan,
```
```
n : banyaknya data pengamatan,
```
```
Cov(Yt, Yt+k) : kovarians antara Yt dan Yt+k,
```
```
Var(Yt) : varians dari Yt.
```
Signifikansi autokorelasi sampel dievaluasi melalui uji-t dengan membandingkan ˆρk
```
terhadap galat bakunya (SE(ˆρk)) sebagai berikut:
```
```
tk =
```
ˆρk
```
SE(ˆρk)
```
```
, (2.15)
```
```
SE(ˆρk) =
```
√
1 + 2 ∑k−1m=1 ˆρ2m
n
.
Batas signifikansi visual pada plot ACF ditentukan menggunakan persentil distribusi-t
berderajat bebas n − 1, yang didefinisikan sebagai berikut:
```
Batas Atas = tn−1;1− α2 × SE(ˆρk), (2.16)
```
```
Batas Bawah = tn−1; α2 × SE(ˆρk), (2.17)
```
dengan ˆρk merupakan autokorelasi sampel pada lag k, n − 1 adalah derajat bebas dari
distribusi-t, dan α adalah taraf signifikansi yang digunakan.
```
Sementara itu, fungsi Partial Autocorrelation Function (PACF) adalah mengukur
```
15
mengukur seberapa kuat hubungan secara parsial antara suatu variabel deret waktu
dengan lag tertentu setelah menghilangkan pengaruh linier dari lag di antaranya, serta
```
digunakan untuk mengidentifikasi orde model Autoregressive (AR). PACF pada lag k (ˆρkk)
```
dihitung menggunakan estimator koefisien autokorelasi parsial sampel yang dirumuskan
sebagai berikut:
```
ˆρkk = Corr(Yt, Yt−k | Yt−1, . . . , Yt−k+1)
```
ˆρkk =
ˆρk − ∑k−1j=1 ˆρk−1,j ˆρk−j
1 − ∑k−1j=1 ˆρk−1,j ˆρj
```
, (2.18)
```
ˆρkj = ˆρk−1,j − ˆρkk ˆρk−1,k−j , untuk j = 1, 2, . . . , k − 1.
```
Signifikansi nilai PACF sampel dievaluasi menggunakan statistik uji-t (tˆρkk ) dengan galat
```
baku sˆρkk =
√
1/n, yang divisualisasikan melalui batas signifikansi dirumuskan sebagai
```
berikut:
```
tˆρkk = ˆρkk
√
n. (2.19)
```
Batas Signifikansi = ±tn−1; α2
```
1√
n
```
, (2.20)
```
dimana ˆρkk merupakan nilai PACF sampel pada lag k, n adalah jumlah observasi deret
waktu, dan α adalah taraf signifikansi yang digunakan.
```
Pola visual yang dihasilkan dari plot ACF dan PACF berdasarkan Persamaan (2.14)
```
```
dan (2.18) dicocokkan dengan pola teoretis yang dirangkum oleh Dani dkk. (2025)
```
sebagaimana disajikan pada tabel berikut:
Tabel 2.5 Pola Teoretis ACF dan PACF
Model Pola ACF Pola PACF
```
AR(p) Menurun menuju nol (tails off ) Terputus setelah lag p (cuts off )
```
```
MA(q) Terputus setelah lag q (cuts off ) Menurun menuju nol (tails off )
```
```
ARMA(p, q) Menurun menuju nol (tails off ) Menurun menuju nol (tails off )
```
Berdasarkan Tabel 2.5, istilah cuts off merujuk pada kondisi di mana nilai autokorelasi
signifikan hingga lag tertentu dan kemudian terputus atau mendekati nol secara tiba-
tiba. Sebaliknya, pola tails off menggambarkan penurunan nilai koefisien secara perlahan
menuju nol, baik berbentuk penurunan eksponensial maupun gelombang sinusoidal.
2.5.4 Orde Model ARIMA
```
Penentuan kandidat model ARIMA(p, d, q) didasarkan pada identifikasi pola
```
```
autokorelasi dan tingkat stasioneritas data. Parameter Autoregressive (AR) atau orde p
```
diidentifikasi dengan mengamati pada lag ke berapa plot Partial Autocorrelation Function
```
(PACF) mengalami pemutusan (cuts off ). Sementara itu, parameter Moving Average
```
```
(MA) atau orde q ditentukan berdasarkan pada lag ke berapa plot Autocorrelation
```
```
Function (ACF) mengalami cuts off. Parameter d menyatakan banyaknya proses
```
differencing yang diperlukan agar data deret waktu menjadi stasioner. Proses identifikasi
ini sering kali menghasilkan lebih dari satu calon model yang layak, seleksi calon model
```
terbaik didasarkan pada prinsip parsimoni (Sober, 1981; Woodward dkk., 2017). Prinsip
```
16
ini menegaskan bahwa apabila terdapat dua atau lebih calon model dengan tingkat akurasi
yang tidak berbeda jauh, maka calon model yang paling sederhana dipilih sebagai model
```
akhir. Sebagai contoh, terdapat calon model ARIMA(1,0,0) yang didefinisikan sebagai
```
```
Yt = ϕ1Yt−1 + εt, (2.21)
```
```
dan calon model ARIMA(2,0,1) yang didefinisikan sebagai
```
```
Yt = ϕ1Yt−1 + ϕ2Yt−2 − θ1εt−1 + εt, (2.22)
```
dengan keterangan
```
Yt : nilai data deret waktu pada waktu ke-t,
```
```
Yt−1 : nilai data deret waktu pada waktu ke-(t − 1),
```
```
Yt−2 : nilai data deret waktu pada waktu ke-(t − 2),
```
```
ϕ1, ϕ2 : parameter autoregressive (AR),
```
```
θ1 : parameter moving average (MA),
```
εt : residual atau galat pada waktu ke-t,
```
εt−1 : residual atau galat pada waktu ke-(t − 1).
```
```
Model ARIMA(1,0,0) pada Persamaan (2.21) mempunyai satu parameter, yaitu ϕ1,
```
```
sedangkan model ARIMA(2,0,1) pada Persamaan (2.22) mempunyai tiga parameter, yaitu
```
ϕ1, ϕ2, dan θ1. Apabila kedua model tersebut menghasilkan tingkat akurasi yang tidak
```
berbeda jauh, maka model ARIMA(1,0,0) dipilih karena memiliki jumlah parameter yang
```
```
lebih sedikit dibandingkan dengan model ARIMA(2,0,1).
```
2.6 Estimasi dan Uji Signifikansi Parameter
```
Parameter ϕ dan θ pada calon model ARIMA(p, d, q) diestimasi menggunakan
```
```
metode Maximum Likelihood Estimation (MLE). Menurut Cryer dan Chan (2008), fungsi
```
```
kepadatan probabilitas distribusi Normal umum X ∼ N (μ, σ2) didefinisikan sebagai
```
```
f (x) =
```
1√
2πσ2
exp
```
(
```
−
```
(x − μ)2
```
2σ2
```
)
```
```
. (2.23)
```
```
Berdasarkan asumsi pada Persamaan (2.8), fungsi kepadatan probabilitas untuk residual
```
dapat dirumuskan sebagai berikut:
```
f (εt) = (2πσ2)−
```
12
exp
```
(
```
−
ε2t
2σ2
```
)
```
```
. (2.24)
```
```
Berdasarkan Wei (2006), penurunan fungsi likelihood (L) untuk sejumlah n observasi data
```
adalah sebagai berikut:
```
L(β, σ2) =
```
n∏
```
t=1
```
```
(2πσ2)−
```
12
exp
```
(
```
−
ε2t
2σ2
```
)
```
=
n∏
```
t=1
```
[
```
(2πσ2)−
```
12
exp
```
(
```
−
ε2t
2σ2
```
)]
```
```
= (2πσ2)−
```
n2
exp
```
(
```
−
1
2σ2
n∑
```
t=1
```
ε2t
```
)
```
```
, (2.25)
```
17
```
dengan β merupakan parameter yang akan diestimasi, baik parameter AR (ϕ) maupun
```
```
parameter MA (θ). Selanjutnya, fungsi log-likelihood dapat dirumuskan sebagai berikut:
```
```
ln L(β, σ2) = ln
```
[
```
(2πσ2)−
```
n2
exp
```
(
```
−
1
2σ2
n∑
```
t=1
```
ε2t
```
)]
```
= ln
```
(
```
```
(2πσ2)−
```
```
n2)
```
- ln
[
exp
```
(
```
−
1
2σ2
n∑
```
t=1
```
ε2t
```
)]
```
= −
n
2
```
ln(2πσ2) −
```
1
2σ2
n∑
```
t=1
```
ε2t
= −
n
2
```
(
```
```
ln(2π) + ln(σ2)
```
```
)
```
−
1
2σ2
n∑
```
t=1
```
ε2t
= −
n
2
```
ln(2π) −
```
n
2
```
ln(σ2) −
```
1
2σ2
n∑
```
t=1
```
```
ε2t . (2.26)
```
Selanjutnya mencari nilai estimasi parameter β dapat diperoleh dengan
```
memaksimalkan fungsi log-likelihood pada persamaan (2.26). Kondisi maksimum fungsi
```
log-likelihood diperoleh dengan menyamakan turunan parsial terhadap β dengan nol.
```
Berikut dijabarkan cara mendapatkan estimasi model AR(1) menggunakan metode
```
```
MLE. Model AR(1) didefinisikan sebagai
```
```
Zt = ϕ1Zt−1 + εt,
```
sehingga diperoleh residualnya sebagai berikut:
```
εt = Zt − ϕ1Zt−1, (2.27)
```
dengan Zt adalah data yang sudah stasioner terhadap varians maupun mean, sehingga
```
turunan parsial dari residual terhadap ϕ1 pada Persamaan (2.27) adalah
```
∂εt
∂ϕ1
```
= −Zt−1. (2.28)
```
Sedangkan, fungsi log-likelihood dan turunan parsialnya terhadap ϕ1 adalah
```
ln L(β, σ2) = −
```
n
2
```
ln(2π) −
```
n
2
```
ln(σ2) −
```
1
2σ2
n∑
```
t=1
```
```
ε2t , (2.29)
```
∂ ln L
∂ϕ1
= −
1
2σ2
n∑
```
t=1
```
2εt
∂εt
∂ϕ1
```
. (2.30)
```
```
Substitusi Persamaan (2.27) dan Persamaan(2.28) ke dalam Persamaan (2.30) diperoleh
```
∂ ln L
∂ϕ1
= −
1
σ2
n∑
```
t=1
```
```
(Zt − ϕ1Zt−1)(−Zt−1)
```
=
1
σ2
n∑
```
t=1
```
```
(Zt − ϕ1Zt−1)Zt−1. (2.31)
```
Nilai estimasi parameter ˆϕ1 diperoleh dengan menyamakan turunan parsial log-likelihood
18
```
pada Persamaan (2.31) terhadap ϕ1 dengan nol, sehingga diperoleh
```
∂ ln L
∂ϕ1
= 0
1
σ2
n∑
```
t=1
```
```
(Zt − ϕ1Zt−1)Zt−1 = 0
```
n∑
```
t=1
```
```
(Zt − ϕ1Zt−1)Zt−1 = 0
```
n∑
```
t=1
```
ZtZt−1 − ϕ1
n∑
```
t=1
```
Z2t−1 = 0
ϕ1
n∑
```
t=1
```
Z2t−1 =
n∑
```
t=1
```
ZtZt−1
ˆϕ1 =
∑n
```
t=1 ZtZt−1∑
```
```
nt=1 Z2t−1. (2.32)
```
Signifikansi parameter yang telah diestimasi diuji menggunakan uji-t untuk
memastikan kelayakannya dalam model. Langkah-langkah uji-t adalah sebagai berikut:
```
(1) Hipotesis:
```
Dalam pengujian ini, βi merepresentasikan parameter model ke-i yang akan diuji,
```
baik itu parameter AR (ϕ) maupun parameter MA (θ).
```
```
H0 : βi = 0, sehingga parameter tidak signifikan terhadap model,
```
```
H1 : βi̸ = 0, sehingga parameter signifikan terhadap model.
```
```
(2) Statistik Uji:
```
Statistik uji yang digunakan dihitung melalui rasio antara nilai estimasi parameter
terhadap galat bakunya, yang dirumuskan sebagai
```
thitung =
```
ˆβi
```
SE( ˆβi)
```
```
, (2.33)
```
```
dengan:
```
```
SE( ˆβi) =
```
√
```
Var( ˆβi) (2.34)
```
```
Var( ˆβi) =
```
```
∑(β
```
```
i − ˆβi)2
```
n − 1
```
. (2.35)
```
Dimana thitung adalah nilai statistik uji-t, ˆβi adalah estimasi parameter yang diuji
```
( ˆϕ atau ˆθ), dan n adalah jumlah observasi. Nilai SE( ˆβi) merupakan galat baku,
```
```
sedangkan Var( ˆβi) merupakan varians parameter yang dihitung berdasarkan selisih
```
kuadrat antara nilai parameter dengan estimasinya.
```
(3) Daerah Kritis:
```
```
Nilai kritis uji (ttabel) ditentukan berdasarkan distribusi t-Student dengan derajat
```
```
bebas (n − k) pada tingkat signifikansi α, dimana k adalah jumlah parameter yang
```
19
diestimasi. Kriteria pengujian adalah sebagai berikut:
|thitung| > ttabel maka H0 ditolak,
|thitung| ≤ ttabel maka H0 gagal ditolak.
```
(4) Keputusan:
```
Keputusan pengujian ditentukan berdasarkan perbandingan antara nilai statistik
uji dan nilai kritis, atau dengan membandingkan nilai p-value terhadap tingkat
signifikansi α.
2.7 Uji Diagnostik Model
Dalam model ARIMA, residual εt diasumsikan mengikuti distribusi Normal dengan
```
rata-rata nol dan varians konstan sesuai dengan Persamaan (2.8). Asumsi ini menjadi
```
dasar bagi pengujian diagnostik yang dilakukan, meliputi uji normalitas residual dan uji
residual white noise.
2.7.1 Uji Normalitas Residual
Pengujian normalitas residual dilakukan untuk memastikan bahwa residual yang
```
dihasilkan oleh model bersifat acak dan mengikuti distribusi normal (Wei, 2006). Salah
```
satu metode yang sering digunakan adalah uji Kolmogorov-Smirnov. Langkah-langkah
uji Kolmogorov-Smirnov adalah sebagai berikut:
```
(1) Hipotesis:
```
```
H0 : Residual berdistribusi normal,
```
```
H1 : Residual tidak berdistribusi normal.
```
```
(2) Statistik Uji:
```
```
Statistik uji Kolmogorov-Smirnov dirumuskan oleh Massey Jr (1951) sebagai
```
```
Dhitung = max |F0(x) − SN (x)|, (2.36)
```
```
dengan Dhitung adalah nilai statistik uji, F0(x) adalah fungsi distribusi kumulatif
```
```
teoretis populasi (normal), dan SN (x) adalah fungsi distribusi kumulatif empiris
```
dari sampel residual dengan ukuran N .
```
(3) Daerah Kritis:
```
```
Nilai kritis (Dtabel) ditentukan berdasarkan tabel uji Kolmogorov-Smirnov untuk
```
ukuran sampel N dan tingkat signifikansi α. Kriteria pengambilan keputusan
adalah sebagai berikut:
```
Dhitung > Dtabel maka H0 ditolak (residual tidak normal),
```
```
Dhitung ≤ Dtabel maka H0 gagal ditolak (residual normal).
```
```
(4) Keputusan:
```
Keputusan pengujian ditentukan berdasarkan perbandingan antara nilai statistik
Dhitung dan nilai kritis Dtabel sesuai dengan kriteria yang telah ditetapkan.
20
2.7.2 Uji Residual White Noise
Pemeriksaan independensi residual bertujuan untuk memastikan bahwa residual
```
bersifat acak (white noise) dan tidak memiliki korelasi antarwaktu. Jika residual masih
```
memuat pola autokorelasi yang signifikan, maka model belum mampu menangkap seluruh
```
informasi data secara optimal (Wei, 2006). Metode yang digunakan untuk menguji asumsi
```
ini adalah statistik Ljung-Box. Langkah-langkah pengujian Ljung-Box adalah sebagai
```
berikut:
```
```
(1) Hipotesis:
```
Hipotesis pengujian dirumuskan sebagai berikut:
```
H0 : ρ1 = · · · = ρK = 0, (residual bersifat acak/white noise),
```
```
H1 : ∃ρk̸ = 0, (residual tidak acak/mengandung autokorelasi),
```
dimana K adalah jumlah lag maksimum yang diuji. Variabel ˆρk adalah autokorelasi
sampel dari residual pada lag ke-k, yang mengukur hubungan linear antara residual
pada waktu t dan t − k.
```
(2) Statistik Uji:
```
```
Menurut Box dkk., 2015, nilai statistik Ljung-Box (Q) dihitung menggunakan rumus
```
```
berikut:
```
```
Q = n(n + 2)
```
K∑
```
k=1
```
```
(n − k)−1 ˆρ2k, (2.37)
```
dimana n merepresentasikan jumlah data observasi.
```
(3) Daerah Kritis:
```
```
Nilai kritis uji (χ2α,df ) ditentukan berdasarkan distribusi Chi-Square pada tingkat
```
```
signifikansi α dengan derajat bebas df = K − (p + q), dimana p dan q adalah orde
```
model ARIMA yang diestimasi. Kriteria pengujian adalah sebagai berikut:
Q > χ2α,df maka H0 ditolak,
Q ≤ χ2α,df maka H0 gagal ditolak.
```
(4) Keputusan:
```
Keputusan pengujian ditentukan dengan membandingkan nilai statistik hitung Q
dengan nilai kritis dari tabel distribusi Chi-Square sesuai dengan daerah kritis yang
telah ditetapkan.
2.7.3 Uji Heteroskedastisitas
Uji heteroskedastisitas bertujuan untuk memastikan apakah varians dari residual
```
bersifat konstan (homoskedastis) atau mengalami perubahan seiring waktu. Mengacu
```
```
pada Wei (2006), jika varians residual tidak stabil atau mengandung efek ARCH
```
```
(Autoregressive Conditional Heteroskedasticity), hal ini menunjukkan bahwa model perlu
```
dikembangkan lebih lanjut menggunakan model volatilitas seperti GARCH. Metode
```
yang digunakan untuk menguji asumsi ini adalah uji Lagrange Multiplier (ARCH-LM).
```
Pengujian ini berlandaskan pada regresi linear dari kuadrat residual terhadap kuadrat
residual lag-nya, yang dirumuskan sebagai
```
ε2t = α0 + α1ε2t−1 + α2ε2t−2 + · · · + αqε2t−q + vt, (2.38)
```
21
dimana εt adalah residual hasil model ARIMA, α menyatakan koefisien regresi, q mewakili
```
orde lag, dan vt adalah residual regresi. Berdasarkan Engle (1982), langkah-langkah
```
pengujian ARCH-LM adalah sebagai berikut:
```
(1) Hipotesis:
```
```
H0 : Tidak terdapat efek ARCH (homoskedastis),
```
```
H1 : Terdapat efek ARCH (heteroskedastis).
```
```
(2) Statistik Uji:
```
Statistik uji ARCH-LM dirumuskan sebagai berikut:
```
LMhitung = nR2, (2.39)
```
dengan LMhitung adalah nilai statistik uji, n adalah jumlah data observasi, dan R2
```
adalah koefisien determinasi yang diperoleh dari regresi pada Persamaan (2.38).
```
```
(3) Daerah Kritis:
```
```
Nilai statistik LM mengikuti distribusi Chi-Square (χ2) dengan derajat bebas q
```
```
(jumlah lag yang diuji) dan tingkat signifikansi α. Nilai kritis (χ2tabel) ditentukan
```
berdasarkan tabel distribusi Chi-Square. Kriteria pengambilan keputusan adalah
sebagai berikut:
```
LMhitung > χ2tabel maka H0 ditolak (terdapat efek ARCH),
```
```
LMhitung ≤ χ2tabel maka H0 gagal ditolak (tidak terdapat efek ARCH).
```
```
(4) Keputusan:
```
Keputusan pengujian ditentukan berdasarkan perbandingan antara nilai statistik
LMhitung dan nilai kritis χ2tabel sesuai dengan kriteria yang telah ditetapkan.
```
2.8 Generalized Autoregressive Conditional Heteroskedasticity (GARCH)
```
Pada model ARIMA standar, varians σ2t diasumsikan konstan sesuai dengan
```
Persamaan (2.8). Namun data keuangan umumnya menunjukkan fenomena
```
```
pengelompokan volatilitas(Engle, 1982). Kondisi ini menyebabkan varians residual
```
berubah dari waktu ke waktu, sehingga diperlukan model yang dapat menangkap
```
dinamika tersebut. Model Autoregressive Conditional Heteroskedasticity (ARCH)
```
memodelkan varians bersyarat sebagai fungsi dari kuadrat residual masa lalu. Model
ARCH dengan orde Q dinyatakan sebagai
σ2t = α0 +
Q∑
```
i=1
```
```
αiε2t−i, (2.40)
```
```
dengan α0 > 0 dan αi ≥ 0 untuk semua i. Pada Persamaan (2.40), σ2t adalah varians
```
bersyarat dari residual pada waktu ke-t, α0 adalah konstanta awal, dan αi adalah koefisien
ARCH ke-i. Adapun ε2t−i merepresentasikan kuadrat dari residual model ARIMA pada
waktu ke-t − i.
Model ARCH sering membutuhkan orde tinggi untuk menangkap pola volatilitas
```
dengan baik. Untuk mengatasinya, Bollerslev (1986) mengembangkan model Generalized
```
22
```
Autoregressive Conditional Heteroskedasticity (GARCH). Pada model ini, varians
```
bersyarat juga bergantung pada nilai varians bersyarat periode sebelumnya. Bentuk
```
umum model GARCH(P, Q) dituliskan sebagai
```
σ2t = α0 +
Q∑
```
i=1
```
αiε2t−i +
P∑
```
j=1
```
```
βj σ2t−j , (2.41)
```
dengan βj ≥ 0 untuk semua j, dimana βj adalah koefisien GARCH ke-j.
Estimasi parameter Ψ dilakukan menggunakan metode Maximum Likelihood
```
Estimation (MLE). Proses ini didasarkan pada asumsi bahwa residual terdistribusi normal
```
```
bersyarat, yaitu εt | Ft−1 ∼ N (0, σ2t ), dimana Ft−1 adalah himpunan informasi yang
```
```
tersedia hingga waktu ke-t − 1. Bollerslev (1986) menyatakan bahwa fungsi likelihood
```
untuk model GARCH dirumuskan sebagai berikut:
```
L(Ψ) =
```
T∏
```
t=1
```
1√
2πσ2t
exp
```
(
```
−
1
2
˜ε2t
```
)
```
```
. (2.42)
```
Fungsi log-likelihood yang digunakan untuk mengestimasi parameter model GARCH
dirumuskan sebagai berikut:
```
ln L(Ψ) = −
```
T
2
```
ln(2π) −
```
1
2
T∑
```
t=1
```
```
(
```
ln σ2t + ˜ε2t
```
)
```
```
, (2.43)
```
dengan definisi residual terstandarisasi sebagai berikut:
˜εt =
εt
σt
,
dengan asumsi sebagai berikut:
```
˜εt ∼ N (0, 1). (2.44)
```
```
Pada Persamaan (2.43), ln L(Ψ) adalah fungsi log-likelihood dengan vektor parameter
```
```
Ψ = (α0, αi, βj ), T adalah jumlah data observasi, dan ˜εt adalah residual terstandarisasi.
```
```
Persamaan (2.43) memerlukan penyelesaian secara numerik (Bollerslev, 1986).
```
Tahap pemilihan model diawali dengan menguji beberapa kandidat, seperti
```
GARCH(1,1), GARCH(1,2), GARCH(2,1), dan GARCH(2,2). Model terbaik ditetapkan
```
```
berdasarkan nilai Akaike Information Criterion (AIC) terkecil. Berdasarkan Cryer dan
```
```
Chan (2008), AIC dirumuskan sebagai berikut:
```
```
AIC = −2 ln(L) + 2k, (2.45)
```
```
dimana L adalah nilai maksimum fungsi likelihood pada Persamaan (2.42) dan k
```
merupakan jumlah parameter model yang dihitung. Meskipun terdapat berbagai pilihan
```
orde, Bollerslev (1986) menyatakan bahwa model GARCH(1,1) umumnya sudah memadai
```
untuk menangkap pola pergerakan data keuangan. Setelah model terbaik terpilih, tahap
selanjutnya adalah menguji kelayakan model. Pengujian kelayakan model dilakukan
```
dengan menghitung galat baku (˜εt) guna menghilangkan sisa efek ketidakstabilan varians.
```
Selanjutnya, dilakukan serangkaian uji diagnostik yang meliputi uji normalitas pada galat
baku, uji white noise pada galat baku, uji white noise pada kuadrat galat baku, serta uji
23
ARCH-LM untuk mendeteksi sisa efek ARCH.
```
2.9 Mean Absolute Percentage Error (MAPE)
```
```
Mean Absolute Percentage Error (MAPE) merupakan ukuran statistik yang
```
digunakan untuk mengevaluasi kinerja model peramalan dengan cara menghitung rata-
rata persentase kesalahan absolut antara nilai aktual dan nilai prediksi. Tujuan
utama penggunaan metode ini adalah untuk mengukur tingkat akurasi model secara
relatif, di mana nilai MAPE yang semakin kecil mengindikasikan bahwa hasil dugaan
```
semakin mendekati data sebenarnya (Wei, 2006). Rumus untuk menghitung nilai MAPE
```
dirumuskan sebagai
```
MAPE =
```
1
n
n∑
```
t=1
```
∣∣
∣∣
∣
Yt − ˆYt
Yt
∣∣
∣∣
```
∣ × 100% (2.46)
```
dengan n menyatakan jumlah data observasi, Yt adalah nilai data aktual pada periode
ke-t, dan ˆYt merupakan nilai hasil prediksi pada periode ke-t.
```
2.10 Mean-Variance Optimization (MVO)
```
Optimisasi portofolio merupakan proses memilih susunan aset yang paling sesuai
untuk mencapai tujuan investasi tertentu, seperti meningkatkan keuntungan atau
mengurangi risiko. Salah satu model dasar yang banyak digunakan adalah Mean-
```
Variance Optimization (MVO) yang diperkenalkan oleh Harry Markowitz pada tahun
```
1950-an. Model ini menjadi landasan teori portofolio modern karena menekankan
pentingnya menyeimbangkan dua ukuran statistik, yaitu nilai rata-rata sebagai gambaran
```
pengembalian yang diharapkan (expected return) dan varians sebagai ukuran risiko
```
```
(Cornu´ejols dkk., 2018). Prinsip penting dalam model ini adalah menyebarkan investasi
```
pada berbagai aset sehingga risiko tidak bertumpu hanya pada satu aset saja.
Dalam teori portfolio modern, pengembalian aset didefinisikan sebagai tingkat
perubahan nilai investasi antarwaktu yang dihitung dari data harga historis. Terdapat
dua pendekatan untuk menghitung nilai ini, yaitu Linear Return dan Log Return. Linear
Return dirumuskan sebagai
```
rt =
```
Xt+1 − Xt
Xt
```
. (2.47)
```
```
Pada Persamaan (2.47), Xt merupakan harga aset pada waktu ke-t, sedangkan Xt+1
```
```
merupakan harga aset pada waktu ke-(t + 1). Nilai rt menunjukkan tingkat perubahan
```
```
harga aset dari waktu ke-t ke waktu ke-(t + 1). Penelitian ini menggunakan linear return
```
karena ukuran tersebut dapat menunjukkan secara langsung seberapa besar harga aset
mengalami kenaikan atau penurunan dari satu periode ke periode berikutnya. Misalkan
terdapat n aset dalam suatu portofolio dan N periode pengamatan. Vektor pengembalian
aset pada periode ke-t didefinisikan sebagai
rn×1,t =




r1,t
r2,t
...
rn,t




```
, (2.48)
```
dengan ri,t menyatakan pengembalian aset ke-i pada periode ke-t. Menurut Markowitz
```
(2008), harapan pengembalian (expected return) dalam model MVO didefinisikan sebagai
```
estimasi pengembalian rata-rata di masa depan. Vektor harapan pengembalian μ
24
dirumuskan sebagai
μn×1 =
1
N
N∑
```
t=1
```
```
rn×1,t. (2.49)
```
Selanjutnya, risiko dalam model MVO didefinisikan sebagai volatilitas atau ketidakpastian
pengembalian yang diestimasi melalui matriks varians-kovarians sampel. Matriks varians-
kovarians Σ didefinisikan sebagai
Σn×n =
1
N − 1
N∑
```
t=1
```
```
(
```
rn×1,t − μn×1
```
) (
```
rn×1,t − μn×1
```
)T
```
```
. (2.50)
```
Tujuan utama dari penggunaan parameter-parameter tersebut adalah untuk
mengakomodasi preferensi investor rasional di dunia nyata, yaitu menginginkan
tingkat pengembalian yang setinggi mungkin dengan tingkat risiko yang serendah
```
mungkin (Markowitz, 2008).
```
```
Menurut Markowitz (2008), kinerja sebuah portofolio dievaluasi melalui dua ukuran
```
```
utama, yaitu perkiraan tingkat pengembalian (expected return) dan tingkat risiko.
```
Pengembalian portofolio didefinisikan sebagai
```
E(Rp) = μT x (2.51)
```
Sementara itu, tingkat risiko portofolio didefinisikan sebagai
```
σ2p = xT Σx (2.52)
```
```
Berdasarkan kedua ukuran tersebut, model Mean-Variance Optimization (MVO)
```
dapat diformulasikan melalui dua pendekatan utama. Pendekatan pertama adalah
```
meminimalkan risiko portofolio pada persamaan (2.52) dengan tetap memastikan bahwa
```
tingkat pengembalian minimum tertentu dapat dicapai, dirumuskan sebagai
minx xT Σx
dengan kendala μT x ≥ μmin,
n∑
```
i=1
```
```
xi = 1,
```
xi ≥ 0, i = 1, . . . , n.
```
(2.53)
```
```
Pada Persamaan (2.53), μmin adalah target minimum harapan pengembalian portofolio
```
yang diinginkan. Pendekatan kedua adalah memaksimalkan pengembalian portofolio
```
pada persamaan (2.51) dengan tetap menjaga agar risiko tidak melampaui batas tertentu
```
yang dapat diterima, dirumuskan sebagai
maxx μT x
dengan kendala xT Σx ≤ Rmax,
n∑
```
i=1
```
```
xi = 1,
```
xi ≥ 0, i = 1, . . . , n.
```
(2.54)
```
25
```
Pada Persamaan (2.54), Rmax merepresentasikan batas maksimum risiko yang dapat
```
ditoleransi. Kedua model di atas memuat batasan-batasan agar solusi yang dihasilkan
relevan dengan kondisi nyata. Persamaan ∑ni=1 xi = 1 merupakan kendala anggaran yang
mewajibkan seluruh modal dialokasikan sepenuhnya ke dalam portofolio sehingga total
bobot aset bernilai satu. Kendala xi ≥ 0 diterapkan sebagai kendala no-short selling,
yang berarti investor tidak diperbolehkan melakukan short-selling atau mengambil posisi
negatif pada aset ke-i.
```
Model pada Persamaan (2.53) dan (2.54) menghasilkan kumpulan portofolio optimal
```
yang dikenal sebagai batas efisiensi, yaitu himpunan pilihan portofolio dengan kombinasi
```
risiko dan pengembalian yang optimal. Model pada persamaan (2.53) dan (2.54)
```
juga dikembangkan lebih lanjut dengan memasukkan batasan-batasan lain seperti biaya
transaksi, serta penggunaan ukuran risiko alternatif untuk menangkap kejadian ekstrem
```
(Rockafellar, Uryasev, dkk., 2000). Pada penelitian ini, optimisasi portofolio utang
```
valas dilakukan dengan menggunakan modifikasi dari model yang memaksimalkan
pengembalian portofolio dengan batasan risiko tertentu sebagaimana dirumuskan pada
```
Persamaan (2.54).
```
2.11 Ukuran Risiko
Dalam manajemen portofolio, pemilihan ukuran risiko yang tepat sangat penting
agar estimasi risiko dapat mencerminkan kondisi pasar secara akurat dan sejalan dengan
```
prinsip diversifikasi. Artzner dkk. (1999) merumuskan dasar teoritis untuk menilai
```
kualitas suatu ukuran risiko melalui konsep Coherent Risk Measures. Suatu pemetaan
risiko ρ : G → R dikatakan koheren apabila memenuhi empat sifat berikut untuk setiap
variabel acak kerugian X dan Y di dalam G.
1. Translation Invariance
Untuk setiap risiko X dan jumlah modal bebas risiko c ∈ R, berlaku:
```
ρ(X + c · r) = ρ(X) − c. (2.55)
```
Sifat ini menyatakan bahwa penambahan aset bebas risiko sebesar c pada risiko X
akan menurunkan nilai ukuran risiko sebesar c. Dengan kata lain, modal bebas
risiko secara langsung mengimbangi potensi kerugian dalam portofolio.
2. Subadditivity
Untuk setiap risiko X dan Y , berlaku:
```
ρ(X + Y ) ≤ ρ(X) + ρ(Y ). (2.56)
```
Sifat ini menyatakan bahwa ukuran risiko portofolio gabungan tidak akan lebih
besar atau sama dengan jumlah ukuran risiko masing-masing portofolio secara
terpisah.
3. Positive Homogeneity
Untuk setiap risiko X dan konstanta λ ≥ 0, berlaku:
```
ρ(λX) = λρ(X). (2.57)
```
Sifat ini menyatakan bahwa jika ukuran posisi diperbesar dengan faktor tertentu,
maka risikonya juga meningkat mengikuti skala perbesarannya.
26
4. Monotonicity
Untuk setiap risiko X dan Y dengan X ≤ Y , berlaku:
```
ρ(Y ) ≤ ρ(X). (2.58)
```
Sifat ini menyatakan bahwa jika satu variabel acak kerugian tidak pernah melebihi
variabel kerugian lainnya dalam suatu portofolio, maka ukuran risikonya harus lebih
kecil atau sama.
```
Dalam model optimasi Mean-Variance Optimization (MVO), ukuran risiko yang
```
digunakan adalah variansnya. Ukuran risiko ini memenuhi sifat subadditivity dan positive
homogeneity, yang berarti penggabungan aset mampu menurunkan risiko total portofolio.
Namun, ukuran risiko ini tidak dikategorikan sebagai ukuran risiko yang koheren karena
```
gagal memenuhi sifat monotonicity (Artzner dkk., 1999). Kegagalan ini disebabkan oleh
```
sifat simetris varians yang menganggap semua fluktuasi sebagai risiko tanpa membedakan
arahnya. Dalam model ini, lonjakan keuntungan yang sangat tinggi diperlakukan
sama buruknya dengan kerugian yang dalam. Akibatnya, aset yang sering memberikan
keuntungan besar justru dinilai memiliki risiko tinggi hanya karena nilainya berfluktuasi.
Hal ini bertentangan dengan prinsip yang memandang potensi keuntungan besar tersebut
sebagai nilai tambah, bukan sebagai ancaman. Ukuran risiko lain yang umum digunakan
```
seperti Value-at-Risk (VaR) seringkali tidak memenuhi sifat subadditivity, terutama pada
```
```
distribusi dengan ekor yang sangat tebal (Artzner dkk., 1999). Kondisi ini dapat
```
menghasilkan penilaian risiko yang tidak konsisten, misalnya ketika diversifikasi justru
tampak meningkatkan risiko, oleh karena itu diperlukan ukuran risiko yang memenuhi
seluruh sifat-sifat ukuran risiko yang koheren, agar model optimasi portofolio memiliki
dasar yang lebih kuat.
```
2.12 Conditional Value-at-Risk (CVaR)
```
```
Sebagai ukuran risiko yang pertama kali diperkenalkan oleh Morgan dkk. (1997),
```
```
Value-at-Risk (VaR) memberikan perkiraan mengenai batas kerugian maksimum yang
```
diperkirakan tidak akan terlampaui dalam suatu periode tertentu dan pada tingkat
kepercayaan tertentu. Meskipun demikian, VaR hanya menetapkan ambang batas
kerugian tanpa memberikan gambaran mengenai seberapa besar kerugian yang mungkin
```
terjadi apabila batas tersebut dilewati (Rockafellar, Uryasev, dkk., 2000). Keterbatasan
```
```
inilah yang menjadi dasar penggunaan Conditional Value-at-Risk (CVaR), yaitu ukuran
```
risiko yang menghitung rata-rata kerugian ketika kerugian tersebut melebihi nilai VaR
pada tingkat kepercayaan tertentu. CVaR, yang juga dikenal sebagai mean excess loss,
mean shortfall, atau tail VaR, memberikan informasi yang lebih rinci mengenai potensi
```
kerugian pada kondisi ekstrem. Rockafellar, Uryasev, dkk. (2000) mendefinisikan kerugian
```
```
portofolio sebagai fungsi f (x, y), dengan x menyatakan keputusan portofolio dan y
```
merupakan variabel acak yang merepresentasikan ketidakpastian pasar dengan densitas
```
probabilitas p(y). Probabilitas bahwa kerugian f (x, y) tidak melebihi suatu nilai ambang
```
batas α dinyatakan oleh fungsi berikut:
```
Ψ(x, α) =
```
∫
```
f (x,y)≤α
```
```
p(y)dy. (2.59)
```
```
Fungsi Ψ(x, α) pada Persamaan (2.59) merepresentasikan probabilitas kumulatif bahwa
```
```
kerugian portofolio tidak melampaui ambang batas α. Dengan kata lain, Ψ(x, α)
```
27
menunjukkan proporsi skenario ketidakpastian pasar ketika kerugian tetap berada di
bawah atau sama dengan nilai α. Berdasarkan fungsi distribusi kerugian tersebut, ambang
batas kerugian terkecil sehingga probabilitas kerugian tidak melebihi ambang tersebut
mencapai tingkat kepercayaan β disebut sebagai β-Value-at-Risk. Nilai ini dinotasikan
```
dengan αβ (x) dan dirumuskan sebagai
```
```
αβ (x) = min{α ∈ R : Ψ(x, α) ≥ β}. (2.60)
```
Selanjutnya, nilai ekspektasi kerugian ketika realisasinya melampaui batas β-VaR
```
disebut sebagai β-Conditional Value-at-Risk. Besaran ini dinotasikan dengan ϕβ (x)
```
```
dan menggambarkan rata-rata kerugian pada bagian terburuk sebesar (1 − β) dari
```
seluruh kemungkinan yang dapat terjadi. Secara matematis, β-Conditional Value-at-Risk
dirumuskan sebagai
```
ϕβ (x) = (1 − β)−1
```
∫
```
f (x,y)≥αβ (x)
```
```
f (x, y)p(y)dy. (2.61)
```
```
Secara matematis, nilai CVaR (ϕβ ) selalu lebih besar atau sama dengan VaR (αβ ) karena
```
CVaR didefinisikan sebagai ekspektasi kerugian yang melampaui ambang batas VaR.
Karakteristik ini menjadikan CVaR lebih unggul dalam menangkap besaran risiko pada
bagian ekor distribusi yang tidak terukur oleh VaR. Keunggulan utama CVaR terletak
pada sifat konveksitasnya, yang memungkinkan minimisasi risiko dapat dilakukan secara
efisien melalui linear programming dan menghasilkan solusi global yang optimal, berbeda
dengan VaR yang memiliki keterbatasan dalam hal konveksitas.
Untuk menerapkan CVaR secara praktis, tantangan utama adalah bahwa nilai
CVaR secara definisi bergantung pada VaR yang harus dihitung terlebih dahulu.
```
Untuk mengatasi ketergantungan ini, Rockafellar, Uryasev, dkk. (2000) memperkenalkan
```
```
performance function Fβ (x, α) yang memungkinkan VaR dan CVaR dihitung secara
```
bersamaan tanpa memerlukan asumsi distribusi tertentu. Performance function ini
didefinisikan sebagai
```
Fβ (x, α) = α + (1 − β)−1
```
∫
y∈Rm
```
[f (x, y) − α]+p(y) dy, (2.62)
```
dengan
```
[f (x, y) − α]+ = max(f (x, y) − α, 0).
```
```
Pada persamaan (2.62), suku [f (x, y)−α]+ merepresentasikan besaran kerugian yang
```
melebihi nilai ambang batas α, yang dikenal sebagai excess loss. Performance function
Fβ membentuk ukuran risiko melalui penjumlahan antara nilai ambang batas α dan nilai
harapan dari kerugian yang melampaui batas tersebut, yang dinormalisasi dengan faktor
```
(1 − β)−1 (Rockafellar, Uryasev, dkk., 2000).
```
```
Menurut Rockafellar, Uryasev, dkk. (2000), fungsi Fβ (x, α) bersifat konveks dan
```
terdiferensiasi secara kontinu terhadap α. Hal tersebut menunjukkan bahwa nilai β-CVaR
dapat diperoleh dengan meminimalkan Fβ terhadap α sebagai
```
ϕβ (x) = minα∈R Fβ (x, α). (2.63)
```
28
```
Pada persamaan (2.63), himpunan nilai α yang menghasilkan minimum tersebut
```
dinyatakan sebagai
```
Aβ (x) = argmin
```
α∈R
```
Fβ (x, α), (2.64)
```
```
dengan Aβ (x) merupakan interval tertutup dan terbatas yang tidak kosong (mungkin
```
```
hanya terdiri dari satu titik). Adapun nilai β-VaR dari kerugian tersebut diberikan sebagai
```
```
αβ (x) = titik ujung kiri dari Aβ (x). (2.65)
```
Dengan demikian, proses penentuan VaR dan CVaR dapat dilakukan secara bersamaan.
```
Rockafellar, Uryasev, dkk. (2000) menegaskan bahwa meminimalkan β-CVaR terhadap
```
```
keputusan portofolio x ∈ X adalah setara dengan meminimalkan fungsi Fβ (x, α) secara
```
```
simultan terhadap pasangan variabel (x, α) ∈ X ×R. Ekuivalensi optimasi ini dirumuskan
```
sebagai
```
minx∈X ϕβ (x) = min(x,α)∈X×R Fβ (x, α). (2.66)
```
```
Berdasarkan persamaan (2.66), pasangan (x∗, α∗) mencapai nilai minimum pada ruas
```
kanan jika dan hanya jika x∗ meminimalkan β-CVaR dan α∗ merupakan elemen dari
```
Aβ (x∗), yang berarti α∗ merepresentasikan nilai β-VaR yang berkorespondensi. Teorema
```
```
ini juga menjamin bahwa apabila fungsi kerugian f (x, y) bersifat konveks terhadap x,
```
```
maka fungsi Fβ (x, α) juga bersifat konveks terhadap (x, α), sehingga memungkinkan
```
penggunaan metode optimasi konveks untuk menemukan solusi optimal global tanpa perlu
menghitung VaR secara terpisah terlebih dahulu.
Pada penerapannya di dunia nyata, distribusi y sering tidak diketahui secara eksplisit
sehingga biasanya digantikan oleh q skenario sampel y1, . . . , yq. Dengan cara ini, integral
pada performance function Fβ dapat didekati menggunakan bentuk diskrit sebagai
```
˜Fβ (x, α) = α + 1
```
```
q(1 − β)
```
q∑
```
k=1
```
```
[f (x, yk) − α]+. (2.67)
```
```
Menurut Rockafellar, Uryasev, dkk. (2000), persamaan (2.67) menghasilkan fungsi
```
yang tetap konveks. Untuk menyederhanakan perhitungan, Rockafellar memperkenalkan
```
variabel bantu uk yang menggantikan suku [f (x, yk) − α]+ (Rockafellar dan Uryasev,
```
```
2002). Dengan cara ini, permasalahan optimasi dapat diubah menjadi bentuk
```
pemrograman linear sebagai
minx,α,ukα +
1
```
q(1 − β)
```
q∑
```
k=1
```
uk
```
dengan kendala uk ≥ f (x, yk) − α, k = 1, . . . , q,
```
uk ≥ 0, k = 1, . . . , q.
```
(2.68)
```
```
Model pada Persamaan (2.68) merupakan formulasi pemrograman linear yang dirancang
```
untuk meminimalkan risiko CVaR melalui optimasi bersama terhadap tiga komponen
utama, yaitu keputusan portofolio x, ambang batas VaR α, dan variabel bantu kerugian
```
uk untuk setiap skenario. Fungsi objektif pada Persamaan (2.68) merepresentasikan
```
```
aproksimasi diskrit dari performance function pada Persamaan (2.67), di mana α
```
```
menangkap komponen ambang batas kerugian dan suku 1q(1−β)∑qk=1 uk mewakili rata-
```
rata kerugian yang melampaui ambang pada bagian ekor distribusi. Kendala pada model
29
```
Persamaan (2.68) merepresentasikan nilai uk = max(f (x, yk) − α, 0). Dengan demikian,
```
hanya kerugian yang melampaui ambang batas α yang dievaluasi pada fungsi objektif,
```
yang mengaproksimasi integral pada Persamaan (2.62). Menurut Rockafellar dan Uryasev
```
```
(2002), risiko pada model optimasi ini didefinisikan secara langsung sebagai nilai CVaR itu
```
sendiri. Berdasarkan hal tersebut, model optimasi yang bertujuan untuk memaksimalkan
perkiraan pengembalian portofolio dengan tetap menjaga agar risiko tidak melampaui
batas tertentu dirumuskan sebagai
maxx,α,ukμT x
dengan kendala α +
1
```
q(1 − β)
```
q∑
```
k=1
```
uk ≤ Rmax,
```
uk ≥ f (x, yk) − α, k = 1, . . . , q,
```
uk ≥ 0, k = 1, . . . , q,
n∑
```
i=1
```
```
xi = 1,
```
lbi ≤ xi ≤ ubi, i = 1, . . . , n.
```
(2.69)
```
```
Pada Persamaan (2.69), μT x menyatakan perkiraan tingkat pengembalian portofolio
```
secara keseluruhan. Sementara itu, parameter lbi dan ubi secara berturut-turut
menunjukkan batas bawah dan batas atas untuk proporsi atau bobot masing-masing
instrumen di dalam portofolio. Penggunaan batas bawah dan batas atas ini memberikan
ruang yang lebih fleksibel agar susunan portofolio dapat disesuaikan dengan berbagai
skenario aturan atau kebijakan yang sedang diterapkan.
30
BAB III
METODOLOGI
Bab ini menjelaskan tahapan pelaksanaan Tugas Akhir secara runtut dan sistematis,
mulai dari pengumpulan data, peramalan, optimasi, hingga penyusunan laporan.
3.1 Data
Penelitian ini menggunakan data sekunder berupa deret waktu harian dari 3 Juli
2017 hingga 24 November 2025. Data tersebut meliputi tingkat suku bunga utang dalam
```
Dolar Amerika Serikat (USD) dengan jangka waktu 5, 10, dan 30 tahun; Euro (EUR)
```
```
dengan jangka waktu 7 dan 10 tahun; serta Yen Jepang (JPY) dengan jangka waktu 5
```
dan 10 tahun. Penelitian ini juga menggunakan pergerakan nilai tukar USD terhadap
```
EUR dan JPY, serta data portofolio utang valuta asing (valas) Pemerintah Indonesia
```
sejak tahun 2024. Data tingkat suku bunga dan portofolio utang valas bersumber
dari lembaga pengelola utang negara Republik Indonesia, sedangkan data pergerakan
```
nilai tukar diperoleh dari Federal Reserve Economic Data (FRED). Untuk keperluan
```
peramalan, data bulanan dibagi menjadi dua bagian, yaitu 80% sebagai data training
dan 20% sebagai data testing.
3.2 Variabel Penelitian
```
Variabel pada penelitian ini terdiri atas biaya utang (C) sebagai variabel dependen,
```
```
serta tingkat suku bunga (IR) dan nilai tukar (F X) sebagai variabel independen. Rincian
```
variabel disajikan pada tabel berikut:
Tabel 3.1 Variabel Penelitian
Variabel Keterangan
C10 Biaya utang untuk mata uang USD dengan jangka waktu
pelunasan 5 tahun
C20 Biaya utang untuk mata uang USD dengan jangka waktu
pelunasan 10 tahun
C30 Biaya utang untuk mata uang USD dengan jangka waktu
pelunasan 30 tahun
C41 Biaya utang untuk mata uang EUR dengan jangka waktu
pelunasan 7 tahun
C51 Biaya utang untuk mata uang EUR dengan jangka waktu
pelunasan 10 tahun
C62 Biaya utang untuk mata uang JPY dengan jangka waktu
pelunasan 5 tahun
C72 Biaya utang untuk mata uang JPY dengan jangka waktu
pelunasan 10 tahun
```
(Tabel dilanjutkan pada halaman berikutnya)
```
31
```
Tabel 3.1 Variabel Penelitian (Lanjutan)
```
Variabel Keterangan
IR1 Suku bunga utang untuk mata uang USD dengan jangka
waktu pelunasan 5 tahun
IR2 Suku bunga utang untuk mata uang USD dengan jangka
waktu pelunasan 10 tahun
IR3 Suku bunga utang untuk mata uang USD dengan jangka
waktu pelunasan 30 tahun
IR4 Suku bunga utang untuk mata uang EUR dengan jangka
waktu pelunasan 7 tahun
IR5 Suku bunga utang untuk mata uang EUR dengan jangka
waktu pelunasan 10 tahun
IR6 Suku bunga utang untuk mata uang JPY dengan jangka
waktu pelunasan 5 tahun
IR7 Suku bunga utang untuk mata uang JPY dengan jangka
waktu pelunasan 10 tahun
F X1 Nilai tukar mata uang USD terhadap EUR
F X2 Nilai tukar mata uang USD terhadap JPY
```
Berdasarkan variabel pada Tabel 3.1, biaya utang (Cij ) ditentukan oleh tingkat suku
```
```
bunga (IRi) dan nilai tukar (F Xj ). Dalam pelunasan utang valas, pemerintah Indonesia
```
```
melakukan pembayaran menggunakan cadangan Dolar Amerika Serikat (USD), oleh
```
```
karena itu biaya utang untuk instrumen berdenominasi USD (i = 1, 2, 3) hanya
```
dipengaruhi oleh perubahan suku bunga untuk mata uang USD dan tidak dipengaruhi
oleh risiko nilai tukar. Sebaliknya, biaya utang untuk instrumen berdenominasi EUR
dan JPY dipengaruhi oleh tingkat suku bunga mata uang terkait serta pergerakan nilai
```
tukarnya (F Xj ) terhadap USD.
```
3.3 Tahapan Penelitian
Tahapan penelitian disusun mengikuti alur pada diagram alir penelitian agar proses
pengerjaan terarah dan konsisten dari awal sampai akhir.
3.3.1 Studi Literatur
Tahap awal dilakukan melalui studi literatur untuk membangun landasan teori dan
memahami penelitian terdahulu. Literatur yang digunakan meliputi buku teks, artikel,
dan laporan penelitian lainnya yang membahas optimasi portofolio, model MVO, ukuran
```
risiko CVaR, serta metode peramalan deret waktu ARIMA(p, d, q)-GARCH(P, Q).
```
3.3.2 Pembentukan Model Biaya Utang
Dalam penelitian ini, konsep return pada teori portofolio investasi didefinisikan
menjadi biaya utang. Pembentukan model biaya utang bertujuan untuk mengukur total
beban yang harus ditanggung pemerintah dari setiap instrumen utang. Biaya utang
```
(Cij,t) dimodelkan sebagai fungsi dari tingkat suku bunga (IRi,t) dan perubahan nilai
```
```
tukar (F Xj,t).
```
32
3.3.3 Preprocessing Data
Data harian terlebih dahulu diperiksa kelengkapannya untuk setiap bulannya dari
periode 3 Juli 2017 hingga 24 November 2025. Apabila terdapat data yang tidak lengkap,
maka data tersebut akan diisi menggunakan metode interpolasi Cubic Spline seperti yang
telah dijelaskan pada subbab 2.3. Setelah itu, data diubah menjadi data bulanan dengan
menghitung nilai rata-rata setiap bulannya.
3.3.4 Pembentukan Model ARIMA-GARCH
```
Pembentukan model ARIMA(p, d, q)-GARCH(P, Q) dilakukan untuk meramalkan
```
nilai tukar dan suku bunga sebagai variabel yang memengaruhi biaya utang. Tahapan
pemebntukan model ARIMA-GARCH adalah sebagai berikut:
1. Model ARIMA
Tahap pembentukan model ARIMA dilakukan sesuai dengan tahapan yang telah
dijelaskan pada subbab 2.5.1 sampai dengan subbab 2.7. Tahapan tersebut
meliputi uji stasioneritas terhadap varians menggunakan transformasi Box-Cox,
uji stasioneritas terhadap mean menggunakan proses differencing, identifikasi
orde model ARIMA melalui plot ACF dan PACF, estimasi serta uji signifikansi
parameter, dan uji diagnostik residual. Apabila model ARIMA yang diperoleh
telah memenuhi uji diagnostik residual, tahap selanjutnya adalah melakukan uji
heteroskedastisitas untuk mengetahui ada atau tidaknya efek ARCH pada residual.
Jika terdapat efek ARCH, maka varians residual dimodelkan menggunakan
GARCH, sedangkan jika tidak terdapat efek ARCH, maka model GARCH tidak
digunakan.
2. Model GARCH
Tahap pemodelan GARCH dilakukan apabila residual dari model ARIMA
menunjukkan adanya efek ARCH atau varians residual yang berubah seiring waktu.
Pemodelan ini dilakukan sesuai dengan tahapan yang telah dijelaskan pada subbab
```
2.8. Jika model GARCH diperlukan, maka model gabungan ARIMA(p, d, q)-
```
```
GARCH(P, Q) dibentuk untuk memodelkan rata-rata sekaligus volatilitas data.
```
Sebaliknya, jika tidak terdapat efek ARCH pada residual model ARIMA, maka
model GARCH tidak digunakan.
3. Pemilihan Model Terbaik
Pemilihan model terbaik dilakukan dengan membandingkan nilai Mean Absolute
```
Percentage Error (MAPE) dari seluruh kandidat model yang telah lolos uji
```
diagnostik. Model dengan nilai MAPE terkecil dan memenuhi prinsip parsimoni
```
(model paling sederhana) dipilih sebagai model terbaik.
```
4. Evaluasi Akurasi Peramalan
Akurasi model peramalan dievaluasi menggunakan data testing dengan menghitung
```
nilai Mean Absolute Percentage Error (MAPE). Semakin kecil nilai MAPE, maka
```
semakin tinggi akurasi model peramalan.
5. Hasil Peramalan
Model terbaik yang terpilih digunakan untuk memprediksi nilai tukar dan suku
bunga pada periode mendatang. Penetapan jangka waktu peramalan didasarkan
pada nilai MAPE yang dihasilkan untuk memastikan tingkat akurasi prediksi tetap
berada dalam batas yang dapat diterima.
33
3.3.5 Input Optimasi
Input optimasi dalam penelitian ini adalah gabungan data historis dan data hasil
peramalan. Data historis yang digunakan merupakan data bulanan periode Juli 2017
sampai November 2025 sebanyak 101 bulan, sedangkan data hasil peramalan merupakan
data periode Desember 2025 sampai November 2026 sebanyak 12 bulan. Data hasil
```
peramalan diperoleh dari model ARIMA(p, d, q)-GARCH(P, Q), kemudian digabungkan
```
dengan data historis untuk membentuk data input optimasi. Penggunaan data gabungan
ini bertujuan agar proses optimasi tidak hanya mempertimbangkan pola perubahan biaya
utang pada periode sebelumnya, tetapi juga potensi perubahan suku bunga dan nilai tukar
pada periode mendatang. Data input tersebut selanjutnya digunakan sebagai dasar dalam
proses optimasi portofolio utang valas menggunakan metode MVO dan CVaR.
3.3.6 Proses Optimasi
Optimasi dilakukan untuk memperoleh bobot portofolio utang valas yang optimal
berdasarkan gabungan data historis dan hasil peramalan, yaitu portofolio dengan
ekspektasi persentase perubahan biaya pembayaran utang valas paling rendah dan tetap
memenuhi batasan risiko serta batasan bobot yang telah ditentukan. Proses optimasi
dilakukan melalui beberapa tahapan sebagai berikut.
1. Perhitungan Parameter Optimasi
Perhitungan parameter dilakukan menggunakan data biaya utang yang telah
dimodelkan pada Subbagian 3.3.2. Biaya utang tersebut kemudian dinyatakan
dalam bentuk persentase perubahan biaya pembayaran utang valas antarperiode
```
yang dihitung berdasarkan Persamaan (2.47). Berdasarkan persentase perubahan
```
biaya tersebut, parameter yang dihitung meliputi rata-rata persentase perubahan
biaya pembayaran utang valas setiap instrumen utang yang dihitung berdasarkan
```
Persamaan (2.49) dan matriks varians-kovarians yang dihitung berdasarkan
```
```
Persamaan (2.50). Selanjutnya, dilakukan penentuan batasan risiko maksimum
```
yang digunakan dalam model MVO dan CVaR.
2. Pembentukan Model Optimasi Utang Berdasarkan MVO
Model optimasi permasalahan utang valas berdasarkan MVO dibentuk berdasarkan
```
Persamaan (2.54) yang telah disesuaikan untuk meminimumkan ekspektasi
```
persentase perubahan biaya pembayaran utang valas dengan batasan varians yang
telah ditentukan sebelumnya. Batasan bobot portofolio ditetapkan sesuai dengan
batasan yang ditetapkan oleh pihak pengelola utang negara Republik Indonesia,
yaitu Kementerian Keuangan.
3. Penyelesaian Model MVO
Model optimasi utang berdasarkan MVO yang telah dibentuk selanjutnya
diselesaikan menggunakan nonlinear programming dengan bantuan fungsi fmincon
pada perangkat lunak MATLAB.
4. Pembentukan Model Optimasi Utang Berdasarkan CVaR
Model optimasi permasalahan utang valas berdasarkan CVaR dibentuk berdasarkan
```
Persamaan (2.68) yang telah disesuaikan untuk meminimumkan ekspektasi
```
persentase perubahan biaya pembayaran utang valas dengan batasan risiko yang
telah ditentukan sebelumnya. Risiko pada model ini didefinisikan sebagai
```
nilai Conditional Value at Risk (CVaR). Batasan bobot portofolio ditetapkan
```
34
sesuai dengan ketentuan pihak pengelola utang negara Republik Indonesia, yaitu
Kementerian Keuangan.
5. Penyelesaian Model CVaR
Model optimasi utang berdasarkan CVaR yang telah dibentuk selanjutnya
diselesaikan menggunakan linear programming dengan bantuan fungsi linprog pada
perangkat lunak MATLAB.
3.3.7 Portofolio Optimal
Output dari proses optimasi adalah dua portofolio utang valas optimal. Portofolio
pertama diperoleh dari model MVO, sedangkan portofolio kedua diperoleh dari model
CVaR. Kedua portofolio tersebut dibentuk berdasarkan gabungan data historis dan data
hasil peramalan, sehingga hasil optimasi tidak hanya mempertimbangkan pola perubahan
biaya utang pada periode sebelumnya, tetapi juga potensi perubahan suku bunga dan nilai
tukar pada periode mendatang. Dalam penelitian ini, portofolio optimal yang dihasilkan
oleh model CVaR menjadi hasil utama karena sesuai dengan tujuan penelitian yang
menekankan pengendalian risiko kenaikan biaya pembayaran utang valas pada kondisi
buruk. Sementara itu, portofolio optimal yang dihasilkan oleh model MVO digunakan
sebagai pembanding untuk melihat perbedaan hasil optimasi ketika risiko portofolio
diukur melalui standar deviasi.
3.3.8 Analisis Hasil dan Pembahasan
Tahapan selanjutnya setelah diperoleh dua portofolio utang valas optimal adalah
melakukan analisis hasil dan pembahasan. Analisis dilakukan dengan membandingkan
hasil optimasi model MVO dan CVaR terhadap portofolio aktual Pemerintah Indonesia
yang digunakan terakhir kali pada tahun 2024. Portofolio aktual tersebut digunakan
sebagai acuan pembanding untuk menilai apakah hasil optimasi mampu menghasilkan
ekspektasi persentase perubahan biaya pembayaran utang valas dan ukuran risiko yang
lebih rendah dibandingkan kondisi aktual. Selain itu, analisis juga dilakukan dengan
membandingkan hasil optimasi antara model MVO dan CVaR. Pembahasan difokuskan
pada perubahan komposisi bobot, ekspektasi persentase perubahan biaya pembayaran
utang valas, dan ukuran risiko pada masing-masing model. Hasil analisis ini digunakan
untuk menilai perbedaan karakteristik MVO dan CVaR serta menentukan portofolio
optimal yang paling sesuai dengan tujuan penelitian.
3.3.9 Penyusunan Tugas Akhir
Seluruh tahapan penelitian didokumentasikan dalam bentuk laporan Tugas Akhir
yang disusun secara sistematis sesuai pedoman penulisan Tugas Akhir di Departemen
Matematika ITS. Selain penyusunan laporan, dilakukan pembukuan hasil penelitian
sebagai bagian dari kelengkapan administrasi Tugas Akhir. Hasil penelitian juga disajikan
dalam bentuk poster yang digunakan untuk Pameran Tugas Akhir.
3.4 Diagram Alir Penelitian
Diagram alir dari pengerjaan Tugas Akhir ini ditunjukkan pada Gambar 3.1 di
halaman berikutnya.
35
Gambar 3.1 Diagram alir penelitian
36
BAB IV
HASIL DAN PEMBAHASAN
4.1 Preprocessing Data dan Deskripsi Data
Data yang digunakan dalam penelitian ini merupakan data harian dari periode 03 Juli
2017 hingga 24 November 2025. Sebelum digunakan dalam proses analisis, data terlebih
dahulu diperiksa kelengkapannya untuk setiap variabel. Pemeriksaan ini dilakukan agar
data yang digunakan tidak memiliki bagian kosong yang dapat mengganggu proses
pengolahan pada tahap berikutnya. Setelah pemeriksaan data harian dilakukan, data
diubah menjadi data bulanan dengan menghitung rata-rata setiap bulan. Data yang
sudah diubah menjadi data bulanan dapat dilihat pada Lampiran 15. Berdasarkan hasil
pemeriksaan, ditemukan bahwa variabel IR5 yang menyatakan suku bunga EUR dengan
jangka waktu pelunasan atau tenor 10 tahun memiliki data yang tidak lengkap pada
periode Februari 2021 sampai dengan Agustus 2021. Dengan demikian, terdapat tujuh
data bulanan yang tidak tersedia pada variabel tersebut. Pengisian data yang hilang
dilakukan menggunakan metode interpolasi Cubic Spline, sebagaimana dijelaskan pada
subbab 2.3. Berikut merupakan struktur data IR5 untuk data yang diketahui.
Tabel 4.1 Struktur Data IR5
```
i xi fi(xi)
```
```
1 1 (Juli 2017) 2,73762
```
```
2 2 (Agustus 2017) 2,56187
```
... ... ...
```
43 43 (Januari 2021) 0,97938
```
- 44 (Februari 2021) -
... ... ...
- 50 (Agustus 2021) -
```
44 51 (September 2021) 1,41345
```
... ... ...
```
94 101 (November 2025) 3,97481
```
Pada Tabel 4.1, bulan Februari 2021 berada setelah bulan Januari 2021, yaitu pada
interval i = 43. Nilai tingkat suku bunga EUR tenor 10 tahun pada bulan Februari 2021
```
sampai dengan Agustus 2021 diperoleh berdasarkan persamaan (2.1) pada interval i = 43
```
sebagai
```
f43(x) = a43 + b43(x − x43) + c43(x − x43)2 + d43(x − x43)3.
```
```
Berdasarkan persamaan (2.1), jarak lebar interval xi untuk setiap i adalah sebagai
```
```
berikut:
```
37
Tabel 4.2 Lebar Interval Data IR5
i xi hi
```
1 1 (Juli 2017) 1
```
```
2 2 (Agustus 2017) 1
```
... ... ...
```
41 41 (November 2020) 1
```
```
42 42 (Desember 2020) 1
```
```
43 43 (Januari 2021) 8
```
```
44 51 (September 2021) 1
```
```
45 52 (Oktober 2021) 1
```
... ... ...
```
93 100 (Oktober 2025) 1
```
```
94 101 (November 2025) -
```
```
Nilai c43 dan c44 diperoleh dengan menyelesaikan persamaan (2.2) berdasarkan Tabel
```
4.2 yang disajikan sebagai sistem matriks berikut:




















1 0 0 · · · 0 0 0 0 · · · 0 0 0 0 0
1 4 1 · · · 0 0 0 0 · · · 0 0 0 0 0
0 1 4 · · · 0 0 0 0 · · · 0 0 0 0 0
... ... ... . . . ... ... ... ... . . . ... ... ... ... ...
0 0 0 · · · 1 18 8 0 · · · 0 0 0 0 0
0 0 0 · · · 0 8 18 1 · · · 0 0 0 0 0
... ... ... . . . ... ... ... ... . . . ... ... ... ... ...
0 0 0 · · · 0 0 0 0 · · · 1 4 1 0 0
0 0 0 · · · 0 0 0 0 · · · 0 1 4 1 0
0 0 0 · · · 0 0 0 0 · · · 0 0 0 0 1




















︸ ︷︷ ︸A
94×94




















c1
c2
c3
...
c43
c44
...
c92
c93
c94




















︸ ︷︷ ︸c94×1
=




















0
3
```
( 2,46457 − 2,56187
```
1 −
2,56187 − 2,73762
1
```
)
```
3
```
( 2,37886 − 2,46457
```
1 −
2,46457 − 2,56187
1
```
)
```
...
3
```
( 1,41345 − 0,97938
```
8 −
0,97938 − 1,09491
1
```
)
```
3
```
( 1,56376 − 1,41345
```
1 −
1,41345 − 0,97938
8
```
)
```
...
3
```
( 4,01491 − 4,01632
```
1 −
4,01632 − 3,92995
1
```
)
```
3
```
( 3,97481 − 4,01491
```
1 −
4,01491 − 4,01632
1
```
)
```
0




















︸ ︷︷ ︸
b94×1
.
Menggunakan bantuan perangkat lunak MATLAB, diperoleh nilai c43 sebesar 0,017351704
```
dan nilai c44 sebesar 0,014875022. Berdasarkan persamaan (2.3), nilai koefisien pada
```
```
f43(x) adalah sebagai berikut:
```
Tabel 4.3 Koefisien Fungsi Interpolasi Cubic Spline Pada Interval i = 43
Koefisien Nilai
a43 0,979380952
b43 -0,077949945
c43 0,017351704
d43 -0,000103195
38
Berdasarkan Tabel 4.3, diperoleh fungsi interpolasi pada interval i = 43 sebagai
```
f43(x) = 0,979380952−0,077949945(x−43)+0,017351704(x−43)2 −0,000103195(x−43)3.
```
Dengan demikian, diperoleh nilai tingkat suku bunga EUR tenor 10 tahun pada bulan
Februari 2021 sampai dengan Agustus 2021 yang disajikan sebagai berikut:.
Tabel 4.4 Hasil Interpolasi Cubic Spline Pada Variabel IR5
x Periode Nilai Interpolasi
44 Februari 2021 0,918679516
45 Maret 2021 0,892062316
46 April 2021 0,898910182
47 Mei 2021 0,938603945
48 Juni 2021 1,010524433
49 Juli 2021 1,114052476
50 Agustus 2021 1,248568903
Kode program MATLAB untuk proses interpolasi Cubic Spline pada variabel IR5
dapat dilihat pada Lampiran 1. Selanjutnya, kurva hasil interpolasi untuk variabel IR5
disajikan pada gambar berikut:
Gambar 4.1 Hasil Interpolasi Cubic Spline Pada Variabel IR5
Berdasarkan Gambar 4.1, kurva pada periode Februari 2021 sampai dengan Agustus
2021 terlihat bergerak secara bertahap dan mulus dari data sebelum periode kosong
menuju data setelah periode kosong. Hal ini sesuai dengan sifat interpolasi Cubic Spline
39
pada subbab 2.3, yaitu membentuk kurva yang kontinu dan halus di antara titik-titik
data yang tersedia. Setelah proses interpolasi dilakukan, data pada variabel IR5 menjadi
lengkap untuk seluruh periode pengamatan dan dapat digunakan dalam tahap pengolahan
berikutnya. Selanjutnya, plot suku bunga untuk keseluruhan data historis disajikan pada
gambar berikut:
Gambar 4.2 Plot Time Series Suku Bunga
Berdasarkan Gambar 4.2, terdapat tujuh variabel suku bunga, yaitu IR1 untuk USD
tenor 5 tahun, IR2 untuk USD tenor 10 tahun, IR3 untuk USD tenor 30 tahun, IR4 untuk
EUR tenor 7 tahun, IR5 untuk EUR tenor 10 tahun, IR6 untuk JPY tenor 5 tahun, dan
IR7 untuk JPY tenor 10 tahun. Suku bunga USD yang ditunjukkan oleh IR1, IR2, dan
IR3 secara umum berada pada tingkat yang lebih tinggi dibandingkan suku bunga EUR
dan JPY. Pada awal periode pengamatan, ketiga suku bunga USD bergerak pada tingkat
yang relatif tinggi, kemudian mengalami penurunan secara bertahap hingga sekitar tahun
2020 sampai 2021. Setelah itu, suku bunga USD kembali meningkat cukup tajam pada
tahun 2022 dan mencapai tingkat yang lebih tinggi pada periode 2023 sampai 2025. Suku
bunga EUR yang ditunjukkan oleh IR4 dan IR5 juga cenderung menurun hingga sekitar
tahun 2020 sampai 2021, lalu meningkat tajam pada tahun 2022. Sementara itu, suku
bunga JPY yang ditunjukkan oleh IR6 dan IR7 berada pada tingkat yang lebih rendah,
tetapi tetap menunjukkan kenaikan pada periode akhir pengamatan. Secara umum,
pergerakan suku bunga tidak menunjukkan pola musiman tertentu karena kenaikan dan
penurunan data tidak berulang secara teratur pada periode yang sama. Selain itu,
tidak terlihat adanya data yang melonjak secara tiba-tiba, melainkan perubahan nilai
masih membentuk pergerakan yang bertahap. Selanjutnya, pergerakan nilai tukar USD
terhadap EUR dan USD terhadap JPY disajikan pada gambar berikut:
40
```
(a) Nilai Tukar USD Terhadap EUR (b) Nilai Tukar USD Terhadap JPY
```
Gambar 4.3 Plot Time Series Nilai Tukar USD Terhadap EUR dan JPY
Berdasarkan Gambar 4.3, variabel F X1 yang menyatakan nilai tukar USD terhadap
EUR mengalami perubahan yang berfluktuasi selama periode pengamatan. Pada awal
periode, nilai F X1 sempat menurun hingga sekitar akhir 2017, kemudian meningkat secara
bertahap hingga tahun 2020. Setelah itu, nilai F X1 kembali menurun pada akhir 2020
hingga awal 2021, lalu meningkat cukup tajam pada tahun 2022. Nilai tertinggi terlihat
berada di sekitar akhir 2022. Setelah mencapai titik tersebut, nilai F X1 kembali menurun,
kemudian bergerak naik dan turun dalam rentang yang relatif sempit pada periode
2023 sampai 2024. Pada tahun 2025, nilai F X1 sempat meningkat, tetapi kemudian
kembali menurun menjelang akhir periode pengamatan. Sementara itu, variabel F X2
yang menyatakan nilai tukar USD terhadap JPY pada awal periode bergerak relatif
stabil di sekitar 105 sampai 113. Nilai tersebut kemudian cenderung menurun hingga
sekitar awal 2021. Setelah itu, nilai F X2 meningkat secara tajam mulai tahun 2022
dan mencapai tingkat yang jauh lebih tinggi pada periode 2023 sampai 2025. Meskipun
terdapat beberapa penurunan pada periode tertentu, secara umum arah pergerakan F X2
setelah tahun 2021 menunjukkan tren meningkat. Pola pergerakan F X1 dan F X2 tidak
menunjukkan pola musiman tertentu karena tidak terdapat kenaikan atau penurunan
yang berulang secara teratur pada periode yang sama. Selain itu, pergerakan kedua
variabel masih terjadi secara bertahap sehingga tidak menunjukkan adanya data yang
melonjak secara tiba-tiba. Secara umum, fluktuasi F X2 terlihat lebih besar dibandingkan
F X1, terutama karena rentang pergerakannya lebih lebar dari awal hingga akhir periode
pengamatan. Selanjutnya, statistik deskriptif untuk data suku bunga disajikan pada tabel
```
berikut:
```
Tabel 4.5 Statistik Deskriptif Data Suku Bunga
Variabel Rata-rata Standar Deviasi Nilai Min. Nilai Maks.
IR1 3,605 1,288 1,261 5,679
IR2 3,973 1,147 1,975 6,125
IR3 4,639 0,908 3,034 6,261
IR4 2,472 1,341 0,579 5,174
IR5 2,841 1,280 0,892 5,420
IR6 1,049 0,359 0,538 1,980
IR7 1,407 0,530 0,621 2,669
Berdasarkan Tabel 4.5, rata-rata suku bunga tertinggi terdapat pada IR3, yaitu suku
41
bunga USD tenor 30 tahun, dengan nilai sebesar 4,639. Rata-rata tertinggi berikutnya
terdapat pada IR2 sebesar 3,973 dan IR1 sebesar 3,605. Hal ini menunjukkan bahwa
suku bunga USD cenderung memiliki tingkat rata-rata yang lebih tinggi dibandingkan
suku bunga EUR dan JPY. Sementara itu, rata-rata suku bunga terendah terdapat
pada IR6, yaitu suku bunga JPY tenor 5 tahun, dengan nilai sebesar 1,049. Dari sisi
standar deviasi, nilai terbesar terdapat pada IR4, yaitu suku bunga EUR tenor 7 tahun,
sebesar 1,341. Hal ini menunjukkan bahwa IR4 memiliki penyebaran data paling besar
dibandingkan variabel suku bunga lainnya. Standar deviasi terkecil terdapat pada IR6
sebesar 0,359, sehingga pergerakan IR6 relatif lebih stabil dibandingkan variabel suku
bunga lainnya. Berdasarkan nilai minimum dan maksimum, IR3 memiliki nilai maksimum
tertinggi sebesar 6,261, sedangkan IR6 memiliki nilai minimum terendah sebesar 0,538.
Selanjutnya, statistik deskriptif untuk data nilai tukar disajikan pada tabel berikut:
Tabel 4.6 Statistik Deskriptif Data Nilai Tukar
Variabel Rata-rata Standar Deviasi Nilai Min. Nilai Maks.
F X1 0,892 0,045 0,810 1,015
F X2 124,988 18,348 103,788 157,860
Berdasarkan Tabel 4.6, rata-rata nilai tukar F X1 sebesar 0,892, sedangkan rata-
rata nilai tukar F X2 sebesar 124,988. Perbedaan nilai rata-rata ini terjadi karena kedua
variabel menggunakan mata uang pembanding yang berbeda. Dari sisi penyebaran data,
standar deviasi F X2 sebesar 18,348 jauh lebih besar dibandingkan standar deviasi F X1
sebesar 0,045. Hal ini menunjukkan bahwa perubahan nilai tukar USD terhadap JPY
lebih besar dibandingkan perubahan nilai tukar USD terhadap EUR. Hal tersebut juga
terlihat dari nilai minimum dan maksimum F X2, yaitu sebesar 103,788 dan 157,860, yang
memiliki rentang lebih lebar dibandingkan F X1, yaitu sebesar 0,810 dan 1,015.
4.2 Identifikasi Model ARIMA
Pada tahap identifikasi model ARIMA, data dibagi menjadi dua bagian, yaitu data
training dan data testing. Pembagian ini dilakukan agar model yang dibentuk tidak hanya
dapat menyesuaikan data historis, tetapi juga dapat dievaluasi kemampuan peramalannya
pada data yang tidak digunakan saat proses pembentukan model. Data training
digunakan untuk membentuk model peramalan, sedangkan data testing digunakan untuk
mengukur akurasi hasil peramalan yang diperoleh. Dalam penelitian ini, data training
ditetapkan sebesar 80% dari seluruh data bulanan, yaitu sebanyak 80 data, dengan
periode Juli 2017 sampai dengan Februari 2024. Sementara itu, data testing ditetapkan
sebesar 20% dari seluruh data bulanan, yaitu sebanyak 21 data, dengan periode Maret
2024 sampai dengan November 2025. Pembagian ini dilakukan untuk seluruh variabel
penelitian, yaitu tujuh variabel suku bunga dan dua variabel nilai tukar. Selanjutnya,
plot data training untuk seluruh variabel suku bunga disajikan pada gambar berikut:
42
Gambar 4.4 Plot Time Series Data Training Suku Bunga
Berdasarkan Gambar 4.4, data training suku bunga yang terdiri atas IR1 sampai
dengan IR7 tidak menunjukkan pola musiman. Hal ini terlihat dari tidak adanya pola
pergerakan yang berulang secara teratur pada periode tertentu. Selain itu, seluruh plot
suku bunga juga tidak menunjukkan adanya data yang melonjak secara tiba-tiba karena
perubahan nilai masih bergerak secara bertahap dari satu periode ke periode berikutnya.
Selanjutnya, plot data training untuk nilai tukar USD terhadap EUR dan USD terhadap
JPY disajikan pada gambar berikut:
```
(a) Nilai Tukar USD Terhadap EUR (b) Nilai Tukar USD Terhadap JPY
```
Gambar 4.5 Plot Time Series Data Training Nilai Tukar USD Terhadap EUR dan JPY
Berdasarkan Gambar 4.5, data training nilai tukar USD terhadap EUR dan USD
terhadap JPY tidak menunjukkan pola musiman. Pergerakan kedua data cenderung
berubah secara fluktuatif dari waktu ke waktu, tetapi tidak membentuk pola berulang
yang tetap pada periode tertentu. Selain itu, plot data training kedua nilai tukar tersebut
juga tidak menunjukkan adanya data yang melonjak secara tiba-tiba karena perubahan
nilai masih berlangsung secara bertahap antarperiode.
43
4.2.1 Stasioneritas Data
Sebelum pemodelan ARIMA dilakukan, data training harus memenuhi asumsi
```
stasioneritas, baik terhadap varians maupun rata-rata (mean). Data dikatakan stasioner
```
terhadap varians apabila keragamannya relatif stabil sepanjang periode pengamatan.
Sementara itu, stasioner terhadap rata-rata berarti nilai rata-rata data tidak mengalami
perubahan sistematis seiring berjalannya waktu, oleh karena itu pengujian stasioneritas
dilakukan secara bertahap, yang diawali dengan pengujian terhadap varians.
Pengujian stasioneritas terhadap varians dilakukan menggunakan plot Box-Cox. Pada
metode ini, nilai rounded value dari parameter λ menjadi acuan penentuan kestabilan
varians. Jika nilai rounded value menunjukkan angka 1, data diasumsikan telah
stasioner terhadap varians. Namun, jika nilainya tidak sama dengan 1, data tersebut
memerlukan transformasi matematis terlebih dahulu. Sebagai contoh, langkah pengujian
```
ini diterapkan pada variabel tingkat suku bunga USD dengan tenor lima tahun (IR1).
```
Berikut adalah plot Box-Cox untuk variabel IR1 sebelum dilakukan transformasi.
Gambar 4.6 Plot Box-Cox variabel IR1 sebelum transformasi
Berdasarkan Gambar 4.6, nilai rounded value dari parameter λ menunjukkan angka
0,5. Karena nilai tersebut belum mencapai 1, maka data IR1 belum stasioner terhadap
```
varians sehingga perlu ditransformasi menggunakan persamaan (2.10). Apabila hasil
```
transformasi variabel IR1 dinotasikan sebagai Z1,t, maka persamaan transformasinya
dirumuskan sebagai
```
Z1,t = (IR1,t)0,5.
```
Setelah proses transformasi selesai, kestabilan varians dievaluasi kembali. Berikut
adalah plot Box-Cox untuk data IR1 setelah mengalami transformasi pertama.
44
Gambar 4.7 Plot Box-Cox data hasil transformasi pertama variabel IR1
Berdasarkan Gambar 4.7, nilai rounded value telah menunjukkan angka 1. Hal ini
membuktikan bahwa varians data hasil transformasi telah stabil, sehingga transformasi
lanjutan tidak lagi diperlukan. Prosedur pengujian dan transformasi yang sama juga
diterapkan secara konsisten pada seluruh variabel lainnya. Visualisasi plot Box-Cox
untuk variabel-variabel lainnya dapat dilihat pada Lampiran 21. Berdasarkan persamaan
```
(2.10), ringkasan hasil transformasi untuk menstabilkan varians pada keseluruhan variabel
```
disajikan pada tabel berikut:
Tabel 4.7 Hasil Transformasi Box-Cox
Variabel λ1 λ2 Transformasi
```
IR1 0,5 - Z1,t = (IR1,t)0,5
```
```
IR2 0,5 0,5 Z2,t = ((IR2,t)0,5)0,5
```
```
IR3 -0,5 0,5 Z3,t = ((IR3,t)−0,5)0,5
```
```
IR4 0,5 - Z4,t = (IR4,t)0,5
```
```
IR5 0,5 - Z5,t = (IR5,t)0,5
```
```
IR6 0 0,5 Z6,t = (ln(IR6,t + 1))0,5
```
```
IR7 0 - Z7,t = ln(IR7,t) + 1
```
```
F X1 -2 - Z8,t = (F X1,t)−2
```
```
F X2 -3 - Z9,t = (F X2,t)−3
```
Berdasarkan Tabel 4.7, bentuk transformasi masing-masing variabel bervariasi
bergantung pada nilai rounded value parameter λ. Variabel IR1, IR4, dan IR5 hanya
membutuhkan satu tahap transformasi dengan pangkat 0,5. Di sisi lain, variabel IR2 dan
45
IR3 harus ditransformasi sebanyak dua kali agar variansnya benar-benar stabil. Untuk
variabel IR6, karena nilai λ awalnya bernilai 0, transformasi pertama menggunakan fungsi
logaritma natural sebelum dilanjutkan dengan transformasi pangkat 0,5. Variabel IR7
cukup ditransformasi satu kali menggunakan fungsi logaritma natural. Sementara itu,
pada variabel nilai tukar mata uang, F X1 ditransformasi menggunakan pangkat -2 dan
F X2 menggunakan pangkat -3. Seluruh deret data yang telah melalui proses transformasi
ini dapat dilihat pada Lampiran 16.
Setelah varians data dipastikan stabil, tahap selanjutnya adalah menguji stasioneritas
```
data terhadap mean menggunakan uji Augmented Dickey-Fuller (ADF) dengan bantuan
```
perangkat lunak R, sesuai dengan rumusan pada subbab 2.5.2. Contoh pengujian ADF
untuk variabel Z1 dengan kode R pada Lampiran 2 dilakukan secara bertahap, yaitu
```
dimulai dari data asli atau level (d = 0). Pada tahap ini, diperoleh persamaan regresi uji
```
```
akar unit untuk variabel Z1 sesuai persamaan (2.11) sebagai
```
∆Z1,t = 0,05721−0,03169Z1,t−1 +0,51051∆Z1,t−1 −0,26828∆Z1,t−2 +0,19843∆Z1,t−3 +e1,t.
Berdasarkan hasil program pada Lampiran 2, diperoleh nilai estimasi koefisien uji akar
```
unit sebesar ˆδ = −0,03169 dan galat baku SE(ˆδ) = 0,02615. Selanjutnya, pengujian ADF
```
pada variabel Z1 dijabarkan sebagai berikut:
```
(1) Hipotesis
```
```
H0 : δ = 0, sehingga data tidak stasioner terhadap rata-rata,
```
```
H1 : δ < 0, sehingga data stasioner terhadap rata-rata.
```
```
(2) Statistik uji
```
```
Statistik uji ADFhitung dihitung berdasarkan persamaan (2.12) dan diperoleh
```
sebagai berikut:
```
ADFhitung =
```
ˆδ
```
SE(ˆδ)
```
=
−0,03169
0,02615
= −1,21190.
Pada tingkat signifikansi 5%, nilai kritis MacKinnon yang digunakan adalah
```
ADFtabel = −2,89000.
```
```
(3) Daerah kritis
```
Berdasarkan daerah kritis pada subbab 2.5.2, kriteria pengujian dinyatakan sebagai
```
berikut:
```
ADFhitung < ADFtabel maka H0 ditolak,
ADFhitung ≥ ADFtabel maka H0 gagal ditolak.
```
(4) Keputusan
```
Karena ADFhitung = −1,21190 ≥ ADFtabel = −2,89000, maka H0 gagal ditolak.
Dengan demikian, data Z1 pada tingkat asli belum stasioner terhadap rata-rata, oleh
karena itu pengujian dilanjutkan dengan melakukan differencing tingkat pertama
```
(d = 1) sesuai dengan persamaan (2.13).
```
46
Karena variabel Z1 tidak stasioner terhadap rata-rata, pengujian dilanjutkan pada
diferensiasi tingkat pertama. Pada tahap ini, diperoleh persamaan regresi uji akar unit
```
untuk variabel ∆Z1 sesuai persamaan (2.11) sebagai
```
∆2Z1,t = 0,00241 − 0,74162∆Z1,t−1 + 0,20518∆2Z1,t−1 + e1,t.
Berdasarkan hasil program pada Lampiran 2, diperoleh nilai estimasi koefisien uji akar
```
unit sebesar ˆδ = −0,74162 dan galat baku SE(ˆδ) = 0,13587. Selanjutnya, pengujian ADF
```
pada tingkat differencing pertama dijabarkan sebagai berikut:
```
(1) Hipotesis
```
```
H0 : δ = 0, sehingga data tidak stasioner terhadap rata-rata,
```
```
H1 : δ < 0, sehingga data stasioner terhadap rata-rata.
```
```
(2) Statistik uji
```
```
Statistik uji ADFhitung dihitung berdasarkan persamaan (2.12) dan diperoleh
```
sebagai berikut:
```
ADFhitung =
```
ˆδ
```
SE(ˆδ)
```
=
−0,74162
0,13587
= −5,45838.
Pada tingkat signifikansi 5%, nilai kritis MacKinnon yang digunakan adalah
```
ADFtabel = −2,89000.
```
```
(3) Daerah kritis
```
Berdasarkan daerah kritis pada subbab 2.5.2, kriteria pengujian dinyatakan sebagai
```
berikut:
```
ADFhitung < ADFtabel maka H0 ditolak,
ADFhitung ≥ ADFtabel maka H0 gagal ditolak.
```
(4) Keputusan
```
Karena ADFhitung = −5,45838 < ADFtabel = −2,89000, maka H0 ditolak. Dengan
demikian, data Z1 telah stasioner terhadap rata-rata setelah dilakukan differencing
satu kali, sehingga deret waktu tersebut memenuhi asumsi untuk dilanjutkan ke
tahap pemodelan ARIMA.
Ringkasan hasil uji ADF untuk seluruh variabel penelitian disajikan pada tabel berikut:
Tabel 4.8 Hasil Uji ADF
```
Variabel d ˆδ SE(ˆδ) ADFhitung ADFtabel Keputusan
```
Z10 −0,03169 0,02615 −1,21190 −2,89000 Tidak stasioner1 −0,74162 0,13587 −5,45838 −2,89000 Stasioner
Z20 −0,03266 0,02852 −1,14521 −2,89000 Tidak stasioner1 −0,85573 0,15009 −5,70124 −2,89000 Stasioner
```
(Tabel dilanjutkan pada halaman berikutnya)
```
47
```
Tabel 4.8 Hasil Uji ADF (Lanjutan)
```
```
Variabel d ˆδ SE(ˆδ) ADFhitung ADFtabel Keputusan
```
Z3
0 −0,05187 0,03180 −1,63131 −2,89000 Tidak stasioner
1 −0,40299 0,28682 −1,40503 −2,89000 Tidak stasioner
2 −5,51339 1,29059 −4,27199 −2,89000 Stasioner
Z40 −0,02562 0,02970 −0,86248 −2,89000 Tidak stasioner1 −0,85378 0,14016 −6,09160 −2,89000 Stasioner
Z50 −0,04508 0,02549 −1,76815 −2,89000 Tidak stasioner1 −0,49684 0,16913 −2,93753 −2,89000 Stasioner
Z60 −0,11885 0,04323 −2,74938 −2,89000 Tidak stasioner1 −0,60884 0,15194 −4,00716 −2,89000 Stasioner
Z70 −0,08597 0,04478 −1,91998 −2,89000 Tidak stasioner1 −1,03181 0,16626 −6,20586 −2,89000 Stasioner
Z80 −0,06026 0,03625 −1,66229 −2,89000 Tidak stasioner1 −0,79047 0,15141 −5,22086 −2,89000 Stasioner
Z90 −0,00121 0,01922 −0,06320 −2,89000 Tidak stasioner1 −0,73407 0,14929 −4,91711 −2,89000 Stasioner
Berdasarkan Tabel 4.8, seluruh variabel belum mencapai stasioneritas terhadap rata-
rata pada tingkat level. Dengan demikian, proses differencing diterapkan secara spesifik
pada masing-masing deret data hingga terbukti stasioner. Notasi ∆d digunakan untuk
menyatakan banyaknya proses differencing yang dilakukan pada suatu variabel. Sebagai
contoh, ∆Z1 menyatakan bahwa variabel Z1 telah melalui proses differencing pertama,
sedangkan ∆2Z3 menyatakan bahwa variabel Z3 telah melalui proses differencing kedua.
```
Sebagian besar variabel menjadi stasioner setelah differencing pertama (d = 1), kecuali
```
```
variabel Z3 yang membutuhkan differencing kedua (d = 2). Deret data hasil differencing
```
ini dapat dilihat pada Lampiran 17. Selanjutnya, plot data training yang telah stasioner
disajikan pada gambar berikut:
Gambar 4.8 Plot Data Training yang Telah Stasioner
Berdasarkan Gambar 4.8, seluruh variabel telah stasioner terhadap varians dan rata-
rata. Hal ini ditunjukkan oleh pola data yang berfluktuasi di sekitar nilai tertentu dan
tidak menunjukkan adanya pola tren yang meningkat atau menurun secara sistematis.
48
Selanjutnya, nilai rata-rata dari masing-masing variabel setelah proses stasioneritas
disajikan pada tabel berikut:
Tabel 4.9 Rata-Rata Data Training yang Telah Stasioner
∆Z1 ∆Z2 ∆2Z3 ∆Z4 ∆Z5 ∆Z6 ∆Z7 ∆Z8 ∆Z9
0.005818026 0.001332430 -0.000082332 0.007129251 0.004168206 0.001987575 0.009292681 -0.002078498 -0.000000005
Berdasarkan Tabel 4.9, nilai rata-rata dari seluruh variabel mendekati nol. Oleh
```
karena itu, konstanta c pada model ARIMA dalam persamaan (2.7) dapat dihilangkan.
```
Dengan terpenuhinya asumsi stasioneritas terhadap varians maupun rata-rata pada
seluruh variabel, tahapan analisis dapat dilanjutkan ke proses identifikasi model ARIMA.
4.2.2 Penentuan Calon Model ARIMA
Setelah data stasioner terhadap varians dan rata-rata, langkah selanjutnya adalah
mengidentifikasi calon model ARIMA dengan melihat plot Autocorrelation Function
```
(ACF) dan Partial Autocorrelation Function (PACF) pada data yang sudah stasioner.
```
Sebagai contoh, untuk variabel suku bunga USD 5 tahun, digunakan data yang sudah
stasioner, yaitu ∆Z1. Plot ACF dari ∆Z1 disajikan pada gambar berikut:
Gambar 4.9 Plot ACF ∆Z1
Berdasarkan data ∆Z1, jumlah observasi yang digunakan adalah n = 79, dengan
rata-rata sampel ∆Z = 0,005818026. Menggunakan taraf signifikansi α = 0.05, contoh
```
perhitungan nilai ACF pada lag pertama berdasarkan persamaan (2.14) adalah sebagai
```
49
```
berikut:
```
ˆρ1 =
∑78
```
t=1(∆Zt − ∆Z)(∆Zt+1 − ∆Z)∑
```
```
79t=1(∆Zt − ∆Z)2
```
=
∑78
```
t=1(∆Zt − 0,005818026)(∆Zt+1 − 0,005818026)∑
```
```
79t=1(∆Zt − 0,005818026)2
```
=
0,213551675
0,553673096
= 0,385699931.
```
Selanjutnya, batas atas dihitung menggunakan persamaan (2.16) dan batas bawah
```
```
menggunakan persamaan (2.17). Karena perhitungan dilakukan pada lag pertama, maka∑
```
k−1m=1 ˆρ2m = 0, sehingga diperoleh nilai standar deviasi dari ACF pada lag pertama sebagai
```
berikut:
```
```
SE(ˆρ1) =
```
√
1
79
= 0,112508790.
```
Dengan t78;0,025 = 1,990847069, batas atas dan batas bawah plot ACF adalah sebagai
```
```
berikut:
```
```
Batas Atas = t78;0,975 × SE(ˆρ1)
```
= 1,990847069 × 0,112508790
= 0,223987795,
```
Batas Bawah = −t78;0,025 × SE(ˆρ1)
```
= −1,990847069 × 0,112508790
= −0,223987795.
Karena nilai ˆρ1 = 0,385699931 berada di luar batas signifikansi −0,223987795 sampai
0,223987795, maka ACF pada lag pertama signifikan.
Selain plot ACF, identifikasi calon model juga dilakukan menggunakan plot PACF.
Plot PACF dari ∆Z1 disajikan pada gambar berikut:
50
Gambar 4.10 Plot PACF ∆Z1
```
Contoh perhitungan nilai PACF pada lag pertama berdasarkan persamaan (2.18)
```
adalah sebagai berikut: Pada lag pertama, nilai PACF dihitung dengan mensubstitusikan
```
k = 1 ke dalam persamaan (2.18). Karena tidak terdapat lag antara Yt dan Yt−1,
```
maka komponen penjumlahan pada pembilang dan penyebut bernilai nol, oleh karena
itu diperoleh nilai PACF pada lag pertama sebagai berikut:
ˆρ11 =
ˆρ1 − ∑1−1j=1 ˆρ1−1,j ˆρ1−j
1 − ∑1−1j=1 ˆρ1−1,j ˆρj
=
ˆρ1 − ∑0j=1 ˆρ0,j ˆρ1−j
1 − ∑0j=1 ˆρ0,j ˆρj
=
ˆρ1 − 0
1 − 0
= ˆρ1
= 0,385699931.
Menggunakan taraf signifikansi α = 0.05, batas atas dan batas bawah signifikansi PACF
```
dihitung menggunakan persamaan (2.20) sebagai berikut:
```
```
Batas Signifikansi = ±t78;0,025
```
1√
79
= ±1,990847069 × 0,112508790
= ±0,223987795.
Karena nilai ˆρ11 = 0,385699931 berada di luar batas signifikansi, maka PACF pada
lag pertama juga signifikan. Berdasarkan pola ACF dan PACF pada ∆Z1, calon
```
model awal yang dapat dipertimbangkan adalah ARIMA(1, 1, 0), ARIMA(0, 1, 1), dan
```
```
ARIMA(1, 1, 1). Calon model tersebut selanjutnya perlu dibandingkan melalui estimasi
```
parameter dan uji diagnostik untuk memperoleh model terbaik.
51
Grafik ACF dan PACF untuk variabel lainnya dapat dilihat pada Lampiran 22.
Berdasarkan plot ACF dan PACF tersebut, diperoleh calon model ARIMA untuk masing-
masing variabel sebagaimana disajikan pada tabel berikut:
Tabel 4.10 Calon Model ARIMA Berdasarkan Plot ACF dan PACF
Variabel Calon Model Persamaan Matematis
∆Z1
```
ARIMA(1, 1, 0) ∆Z1,t = ϕ1∆Z1,t−1 + εt
```
```
ARIMA(0, 1, 1) ∆Z1,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 1) ∆Z1,t = ϕ1∆Z1,t−1 + εt − θ1εt−1
```
∆Z2
```
ARIMA(0, 1, 1) ∆Z2,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z2,t = ϕ1∆Z2,t−1 + εt
```
```
ARIMA(1, 1, 1) ∆Z2,t = ϕ1∆Z2,t−1 + εt − θ1εt−1
```
```
ARIMA([9], 1, 0) ∆Z2,t = ϕ9∆Z2,t−9 + εt
```
```
ARIMA([9], 1, 1) ∆Z2,t = ϕ9∆Z2,t−9 + εt − θ1εt−1
```
∆2Z3
```
ARIMA(4, 2, 2) ∆2Z3,t =
```
4∑
```
i=1
```
ϕi∆2Z3,t−i + εt −
2∑
```
j=1
```
θj εt−j
```
ARIMA(2, 2, 2) ∆2Z3,t =
```
2∑
```
i=1
```
ϕi∆2Z3,t−i + εt −
2∑
```
j=1
```
θj εt−j
```
ARIMA(4, 2, 0) ∆2Z3,t =
```
4∑
```
i=1
```
ϕi∆2Z3,t−i + εt
```
ARIMA(2, 2, 0) ∆2Z3,t =
```
2∑
```
i=1
```
ϕi∆2Z3,t−i + εt
```
ARIMA(0, 2, 2) ∆2Z3,t = εt −
```
2∑
```
j=1
```
θj εt−j
```
ARIMA([2], 2, 0) ∆2Z3,t = ϕ2∆2Z3,t−2 + εt
```
```
ARIMA([4], 2, 0) ∆2Z3,t = ϕ4∆2Z3,t−4 + εt
```
```
ARIMA([2], 2, 2) ∆2Z3,t = ϕ2∆2Z3,t−2 + εt −
```
2∑
```
j=1
```
θj εt−j
```
ARIMA([4], 2, 2) ∆2Z3,t = ϕ4∆2Z3,t−4 + εt −
```
2∑
```
j=1
```
θj εt−j
∆Z4
```
ARIMA(1, 1, 1) ∆Z4,t = ϕ1∆Z4,t−1 + εt − θ1εt−1
```
```
ARIMA(2, 1, 1) ∆Z4,t =
```
2∑
```
i=1
```
ϕi∆Z4,t−i + εt − θ1εt−1
```
ARIMA(0, 1, 1) ∆Z4,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z4,t = ϕ1∆Z4,t−1 + εt
```
```
ARIMA(2, 1, 0) ∆Z4,t =
```
2∑
```
i=1
```
ϕi∆Z4,t−i + εt
∆Z5
```
ARIMA(1, 1, 1) ∆Z5,t = ϕ1∆Z5,t−1 + εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z5,t = ϕ1∆Z5,t−1 + εt
```
```
ARIMA(0, 1, 1) ∆Z5,t = εt − θ1εt−1
```
∆Z6
```
ARIMA(1, 1, 1) ∆Z6,t = ϕ1∆Z6,t−1 + εt − θ1εt−1
```
```
ARIMA(0, 1, 1) ∆Z6,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z6,t = ϕ1∆Z6,t−1 + εt
```
∆Z7
```
ARIMA([14], 1, [14]) ∆Z7,t = ϕ14∆Z7,t−14 + εt − θ14εt−14
```
```
ARIMA(0, 1, [14]) ∆Z7,t = εt − θ14εt−14
```
```
ARIMA([14], 1, 0) ∆Z7,t = ϕ14∆Z7,t−14 + εt
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
52
```
Tabel 4.10 Calon Model ARIMA Berdasarkan Plot ACF dan PACF (Lanjutan)
```
Variabel Calon Model Persamaan Matematis
∆Z8
```
ARIMA(1, 1, 1) ∆Z8,t = ϕ1∆Z8,t−1 + εt − θ1εt−1
```
```
ARIMA(0, 1, 1) ∆Z8,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z8,t = ϕ1∆Z8,t−1 + εt
```
∆Z9
```
ARIMA(1, 1, 1) ∆Z9,t = ϕ1∆Z9,t−1 + εt − θ1εt−1
```
```
ARIMA([8], 1, 1) ∆Z9,t = ϕ8∆Z9,t−8 + εt − θ1εt−1
```
```
ARIMA(0, 1, 1) ∆Z9,t = εt − θ1εt−1
```
```
ARIMA(1, 1, 0) ∆Z9,t = ϕ1∆Z9,t−1 + εt
```
```
ARIMA([8], 1, 0) ∆Z9,t = ϕ8∆Z9,t−8 + εt
```
Tahap selanjutnya adalah melakukan pemodelan ARIMA untuk meperoleh model
terbaik dari masing-masing variabel penelitian.
4.3 Pemodelan ARIMA
Pemodelan ARIMA dilakukan untuk memperoleh model deret waktu terbaik dari
masing-masing variabel penelitian yang telah stasioner. Bagian ini mencakup estimasi
dan uji signifikansi parameter, serta uji diagnostik residual yang meliputi uji normalitas,
uji white noise, dan uji heteroskedastisitas.
4.3.1 Estimasi dan Uji Signifikansi Parameter
Estimasi parameter dilakukan terhadap seluruh calon model ARIMA yang telah
diperoleh berdasarkan plot ACF dan PACF. Sebagai contoh, pada variabel suku bunga
USD 5 tahun, data yang digunakan adalah ∆Z1 dengan salah satu calon model
```
ARIMA(1, 1, 0). Model ARIMA(1, 1, 0) pada data ∆Z1 dapat dituliskan sebagai
```
```
∆Z1,t = ϕ1∆Z1,t−1 + εt. (4.1)
```
```
Berdasarkan persamaan (2.32), diperoleh estimasi untuk parameter ϕ1 pada model
```
```
ARIMA(1, 1, 0) untuk data ∆Z1 sebagai berikut:
```
ˆϕ1 =
∑79
```
t=2 ∆Z1,t∆Z1,t−1∑
```
```
79t=2 (∆Z1,t−1)2
```
=
0,216304500
0,554776622
= 0,3899.
Dengan demikian, diperoleh nilai estimasi parameter ˆϕ1 = 0,3899. Sehingga, model
```
ARIMA(1, 1, 0) pada data ∆Z1 dapat dituliskan sebagai
```
∆Z1,t = 0,3899∆Z1,t−1 + εt.
Setelah nilai estimasi parameter ϕ1 diperoleh, langkah selanjutnya adalah melakukan
uji signifikansi parameter sesuai dengan Subbab 2.6. Uji signifikansi parameter ϕ1 pada
```
model ARIMA(1, 1, 0) untuk ∆Z1 dilakukan dengan langkah-langkah sebagai berikut:
```
53
1. Hipotesis
Hipotesis yang digunakan dalam uji signifikansi parameter ϕ1 adalah sebagai
```
berikut:
```
```
H0 : ϕ1 = 0, parameter tidak signifikan terhadap model,
```
```
H1 : ϕ1̸ = 0, parameter signifikan terhadap model.
```
2. Statistik Uji
Pengujian dilakukan dengan uji dua arah pada tingkat signifikansi α = 5%. Jumlah
observasi yang digunakan adalah n = 79, sedangkan jumlah parameter yang
diestimasi adalah k = 1, sehingga diperoleh derajat bebas df = n − k = 79 − 1 = 78,
oleh karena itu nilai ttabel adalah sebagai berikut:
```
ttabel = tdf ;α/2 = t78;0,05/2 = t78;0,025 = 1,9908.
```
3. Daerah Kritis
Kriteria pengujian parameter adalah sebagai berikut:
|thitung| > ttabel maka H0 ditolak,
|thitung| ≤ ttabel maka H0 gagal ditolak.
4. Keputusan
Karena
|thitung| = 3,7671 > ttabel = 1,9908,
maka H0 ditolak. Dengan demikian, parameter ϕ1 signifikan terhadap model
```
ARIMA(1, 1, 0) pada data ∆Z1.
```
Estimasi dan uji signifikansi parameter dilakukan menggunakan bahasa pemrograman
R pada perangkat lunak RStudio. Program R yang digunakan dalam proses estimasi
dan uji signifikansi parameter dapat dilihat pada Lampiran 3. Hasil estimasi dan uji
signifikansi parameter untuk seluruh calon model ARIMA disajikan pada tabel berikut:
Tabel 4.11 Hasil Estimasi dan Uji Signifikansi Parameter Model ARIMA
Variabel Model Par. Estimasi SE thitung ttabel Keputusan
```
∆Z1 (1, 1, 0) ϕ1 0,3867 0,1030 3,7527 1,9908 Signifikan
```
```
(0, 1, 1) θ1 −0,4746 0,0903 −5,2530 1,9908 Signifikan
```
```
(1, 1, 1) ϕ1 0,0345 0,1958 0,1764 1,9913
```
Tidak
Signifikan
θ1 −0,4514 0,1637 −2,7578 1,9913 Signifikan
```
∆Z2 (0, 1, 1) θ1 −0,3515 0,1194 −2,9438 1,9908 Signifikan
```
```
(1, 1, 0) ϕ1 0,2583 0,1081 2,3891 1,9908 Signifikan
```
```
(1, 1, 1) ϕ1 −0,2559 0,2470 −1,0361 1,9913
```
Tidak
Signifikan
θ1 −0,5773 0,2029 −2,8453 1,9913 Signifikan
```
([9], 1, 0) ϕ9 −0,1414 0,1134 −1,2475 1,9908 TidakSignifikan
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
54
```
Tabel 4.11 Hasil Estimasi dan Uji Signifikansi Parameter Model ARIMA (Lanjutan)
```
Variabel Model Par. Estimasi SE thitung ttabel Keputusan
```
([9], 1, 1) ϕ9 −0,1484 0,1122 −1,3222 1,9913
```
Tidak
Signifikan
θ1 −0,3578 0,1211 −2,9554 1,9913 Signifikan
∆2Z3
```
(4, 2, 2)
```
ϕ1 −0,2239 0,5707 −0,3924 1,9935 TidakSignifikan
ϕ2 −0,2984 0,2409 −1,2388 1,9935 TidakSignifikan
ϕ3 −0,1550 0,2443 −0,6345 1,9935 TidakSignifikan
ϕ4 −0,0840 0,1757 −0,4780 1,9935 TidakSignifikan
θ1 0,4422 0,5638 0,7843 1,9935 TidakSignifikan
θ2 0,2618 0,4797 0,5458 1,9935 TidakSignifikan
```
(2, 2, 2)
```
ϕ1 0,2265 0,4353 0,5205 1,9925 TidakSignifikan
ϕ2 −0,3061 0,1679 −1,8234 1,9925 TidakSignifikan
θ1 0,8939 0,4505 1,9843 1,9925 TidakSignifikan
θ2 −0,0540 0,4441 −0,1215 1,9925 TidakSignifikan
```
(4, 2, 0)
```
ϕ1 −0,5868 0,1077 −5,4458 1,9925 Signifikan
ϕ2 −0,7022 0,1158 −6,0654 1,9925 Signifikan
ϕ3 −0,4514 0,1180 −3,8267 1,9925 Signifikan
ϕ4 −0,3083 0,1110 −2,7764 1,9925 Signifikan
```
(2, 2, 0) ϕ1 −0,3688 0,1017 −3,6262 1,9917 Signifikanϕ2 −0,4418 0,1035 −4,2679 1,9917 Signifikan
```
```
(0, 2, 2) θ1 0,6216 0,1225 5,0748 1,9917 Signifikanθ2 0,3407 0,1259 2,7053 1,9917 Signifikan
```
```
([2], 2, 0) ϕ2 −0,3417 0,1083 −3,1542 1,9908 Signifikan
```
```
([4], 2, 0) ϕ4 0,0306 0,1187 0,2583 1,9908 TidakSignifikan
```
```
([2], 2, 2)
```
ϕ2 −0,2394 0,1463 −1,6361 1,9917 TidakSignifikan
θ1 0,9526 0,2698 3,5315 1,9917 Signifikan
θ2 0,2321 0,1583 1,4664 1,9917 TidakSignifikan
```
([4], 2, 2)
```
ϕ4 0,0945 0,1239 0,7624 1,9917 TidakSignifikan
θ1 0,6419 0,1575 4,0765 1,9917 Signifikan
θ2 0,3446 0,1423 2,4215 1,9917 Signifikan
```
∆Z4 (1, 1, 1) ϕ1 −0,0379 0,2046 −0,1852 1,9913 TidakSignifikan
```
θ1 −0,4574 0,1691 −2,7048 1,9913 Signifikan
```
(2, 1, 1)
```
ϕ1 0,2217 0,2869 0,7728 1,9917 TidakSignifikan
ϕ2 −0,1954 0,1460 −1,3380 1,9917 TidakSignifikan
θ1 −0,1960 0,2801 −0,6996 1,9917 TidakSignifikan
```
(0, 1, 1) θ1 −0,4308 0,0960 −4,4893 1,9908 Signifikan
```
```
(1, 1, 0) ϕ1 0,3209 0,1056 3,0386 1,9908 Signifikan
```
```
(2, 1, 0) ϕ1 0,4022 0,1083 3,7149 1,9913 Signifikanϕ2 −0,2483 0,1075 −2,3103 1,9913 Signifikan
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
55
```
Tabel 4.11 Hasil Estimasi dan Uji Signifikansi Parameter Model ARIMA (Lanjutan)
```
Variabel Model Par. Estimasi SE thitung ttabel Keputusan
```
∆Z5 (1, 1, 1) ϕ1 0,1170 0,1830 0,6397 1,9913 TidakSignifikan
```
θ1 −0,3764 0,1545 −2,4369 1,9913 Signifikan
```
(1, 1, 0) ϕ1 0,3987 0,1023 3,8980 1,9908 Signifikan
```
```
(0, 1, 1) θ1 −0,4515 0,0845 −5,3406 1,9908 Signifikan
```
```
∆Z6 (1, 1, 1) ϕ1 0,0111 0,1994 0,0557 1,9913 TidakSignifikan
```
θ1 −0,5013 0,1663 −3,0137 1,9913 Signifikan
```
(0, 1, 1) θ1 −0,5089 0,0927 −5,4883 1,9908 Signifikan
```
```
(1, 1, 0) ϕ1 0,3899 0,1027 3,7966 1,9908 Signifikan
```
```
∆Z7 ([14], 1, [14]) ϕ14 0,1092 0,4109 0,2659 1,9913 TidakSignifikan
```
θ14 0,3668 0,4049 0,9060 1,9913 TidakSignifikan
```
(0, 1, [14]) θ14 0,2609 0,1167 2,2349 1,9908 Signifikan
```
```
([14], 1, 0) ϕ14 −0,2236 0,1067 −2,0957 1,9908 Signifikan
```
```
∆Z8 (1, 1, 1) ϕ1 0,0712 0,2994 0,2378 1,9913 TidakSignifikan
```
θ1 −0,2617 0,2822 −0,9272 1,9913 TidakSignifikan
```
(0, 1, 1) θ1 −0,3230 0,1027 −3,1449 1,9908 Signifikan
```
```
(1, 1, 0) ϕ1 0,3026 0,1087 2,7844 1,9908 Signifikan
```
```
∆Z9 (1, 1, 1) ϕ1 0,0881 0,4650 0,1896 1,9913 TidakSignifikan
```
θ1 −0,2676 0,4646 −0,5761 1,9913 TidakSignifikan
```
([8], 1, 1) ϕ8 −0,1488 0,1185 −1,2548 1,9913
```
Tidak
Signifikan
θ1 −0,3817 0,1212 −3,1494 1,9913 Signifikan
```
(0, 1, 1) θ1 −0,3521 0,1124 −3,1339 1,9908 Signifikan
```
```
(1, 1, 0) ϕ1 0,3260 0,1076 3,0307 1,9908 Signifikan
```
```
([8], 1, 0) ϕ8 −0,1048 0,1169 −0,8962 1,9908 TidakSignifikan
```
Berdasarkan Tabel 4.11, model yang seluruh parameternya signifikan akan
```
dilanjutkan ke tahap uji diagnostik residual. Sebagai contoh, model (1, 1, 0) pada ∆Z1
```
```
dilanjutkan karena parameter ϕ1 signifikan. Namun, model (2, 2, 2) dan ([2], 2, 2) pada
```
∆2Z3 tetap disertakan karena model signifikan lainnya pada variabel tersebut tidak
memenuhi asumsi white noise pada tahap selanjutnya.
4.3.2 Uji Diagnostik Residual
Uji diagnostik residual dilakukan pada model ARIMA yang seluruh parameternya
signifikan dengan bantuan perangkat lunak RStudio. Program R yang digunakan dalam
proses uji diagnostik residual dapat dilihat pada Lampiran 4. Sebagai contoh, dilakukan
```
uji normalitas residual pada model (0, 1, 1) untuk data ∆Z1 sesuai dengan subsubbab
```
2.7.1. Uji normalitas residual dilakukan dengan langkah-langkah sebagai berikut:
1. Hipotesis
Hipotesis yang digunakan dalam uji normalitas residual adalah sebagai berikut:
```
H0 : residual berdistribusi normal,
```
```
H1 : residual tidak berdistribusi normal.
```
56
2. Statistik Uji
```
Statistik uji normalitas residual dihitung berdasarkan persamaan (2.36), yaitu
```
```
Dhitung = max |F0(x) − SN (x)|.
```
Berdasarkan hasil pengujian, diperoleh
```
Dhitung = 0,0975, Dtabel = 0,1519.
```
3. Daerah Kritis
Kriteria pengujian normalitas residual adalah sebagai berikut:
Dhitung > Dtabel maka H0 ditolak,
Dhitung ≤ Dtabel maka H0 gagal ditolak.
4. Keputusan
Karena
```
Dhitung = 0,0975 ≤ Dtabel = 0,1519,
```
```
maka H0 gagal ditolak. Dengan demikian, residual model (0, 1, 1) pada data ∆Z1
```
berdistribusi normal.
Berikut hasil uji normalitas residual untuk model ARIMA pada masing-masing
variabel.
Tabel 4.12 Hasil Uji Normalitas Residual Model ARIMA
Variabel Model Dhitung Dtabel Keputusan
∆Z1
```
(1, 1, 0) 0,0896 0,1519 Normal
```
```
(0, 1, 1) 0,0964 0,1519 Normal
```
∆Z2
```
(0, 1, 1) 0,0626 0,1519 Normal
```
```
(1, 1, 0) 0,0608 0,1519 Normal
```
∆2Z3
```
(4, 2, 0) 0,0619 0,1529 Normal
```
```
(2, 2, 0) 0,1015 0,1529 Normal
```
```
(0, 2, 2) 0,0831 0,1529 Normal
```
```
(2, 2, 2) 0,0519 0,1529 Normal
```
```
([2], 2, 0) 0,0785 0,1529 Normal
```
```
([2], 2, 2) 0,0632 0,1529 Normal
```
∆Z4
```
(0, 1, 1) 0,1054 0,1519 Normal
```
```
(1, 1, 0) 0,1051 0,1519 Normal
```
```
(2, 1, 0) 0,1163 0,1519 Normal
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
57
```
Tabel 4.12 Hasil Uji Normalitas Residual Model ARIMA (Lanjutan)
```
Variabel Model Dhitung Dtabel Keputusan
∆Z5
```
(1, 1, 0) 0,1220 0,1519 Normal
```
```
(0, 1, 1) 0,1459 0,1519 Normal
```
∆Z6
```
(0, 1, 1) 0,0954 0,1519 Normal
```
```
(1, 1, 0) 0,1201 0,1519 Normal
```
∆Z7
```
(0, 1, [14]) 0,1508 0,1519 Normal
```
```
([14], 1, 0) 0,1616 0,1519 Tidak Normal
```
∆Z8
```
(0, 1, 1) 0,0800 0,1519 Normal
```
```
(1, 1, 0) 0,0774 0,1519 Normal
```
∆Z9
```
(0, 1, 1) 0,0674 0,1519 Normal
```
```
(1, 1, 0) 0,0790 0,1519 Normal
```
Setelah uji normalitas residual, dilakukan uji white noise residual pada semua model
```
ARIMA. Sebagai contoh, uji white noise residual dilakukan pada model (0, 1, 1) untuk
```
data ∆Z1 dengan lag 12 sesuai dengan subsubbab 2.7.2. Uji white noise residual dilakukan
dengan langkah-langkah sebagai berikut:
1. Hipotesis
Hipotesis yang digunakan dalam uji white noise residual adalah sebagai berikut:
```
H0 : residual bersifat white noise,
```
```
H1 : residual tidak bersifat white noise.
```
2. Statistik Uji Pada pengujian digunakan lag K = 12, banyaknya data residual
```
n = 80 − 1 = 79, dan model (0, 1, 1). Karena model tersebut memiliki p + q = 1,
```
maka derajat bebas yang digunakan adalah
```
df = K − (p + q) = 12 − 1 = 11.
```
```
Berdasarkan persamaan (2.37), statistik uji white noise residual dihitung sebagai
```
berikut.
```
Q = n(n + 2)
```
K∑
```
k=1
```
ˆρ2k
n − k
```
= 79(79 + 2)
```
12∑
```
k=1
```
ˆρ2k
79 − k
= 10,0191.
Pada taraf signifikansi α = 0,05 dengan derajat bebas df = 11, diperoleh nilai kritis
```
χ2α,df = χ20,05;11 = 19,6751.
```
58
3. Daerah Kritis
Kriteria pengujian white noise residual adalah sebagai berikut:
Q > χ2α,df maka H0 ditolak,
Q ≤ χ2α,df maka H0 gagal ditolak.
4. Keputusan
Karena
```
Q = 10,0191 ≤ χ2α,df = 19,6751,
```
```
maka H0 gagal ditolak. Dengan demikian, residual model (0, 1, 1) pada data ∆Z1
```
bersifat white noise.
Berikut hasil uji white noise residual untuk model ARIMA pada masing-masing variabel.
Tabel 4.13 Hasil Uji White Noise Residual Model ARIMA
Variabel Model Lag Q χ2α,df Keputusan
```
∆Z1 (1, 1, 0) 12 17,0610 19,6751 White Noise
```
```
(0, 1, 1) 12 10,0327 19,6751 White Noise
```
```
∆Z2 (0, 1, 1) 12 13,6400 19,6751 White Noise
```
```
(1, 1, 0) 12 17,2374 19,6751 White Noise
```
```
∆2Z3 (4, 2, 0) 12 19,3849 15,5073 Bukan White
```
Noise
```
(2, 2, 0) 12 32,6422 18,3070 Bukan White
```
Noise
```
(0, 2, 2) 12 19,7000 18,3070 Bukan White
```
Noise
```
(2, 2, 2) 12 14,6185 15,5073 White Noise
```
```
([2], 2, 0) 12 35,5454 19,6751 Bukan White
```
Noise
```
([2], 2, 2) 12 15,1588 16,9190 White Noise
```
```
∆Z4 (0, 1, 1) 12 10,1735 19,6751 White Noise
```
```
(1, 1, 0) 12 17,4526 19,6751 White Noise
```
```
(2, 1, 0) 12 8,0911 18,3070 White Noise
```
```
∆Z5 (1, 1, 0) 12 19,8541 19,6751 Bukan White
```
Noise
```
(0, 1, 1) 12 14,9258 19,6751 White Noise
```
```
∆Z6 (0, 1, 1) 12 12,0385 19,6751 White Noise
```
```
(1, 1, 0) 12 18,1399 19,6751 White Noise
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
59
```
Tabel 4.13 Hasil Uji White Noise Residual Model ARIMA (Lanjutan)
```
Variabel Model Lag Q χ2α,df Keputusan
```
∆Z7 (0, 1, [14]) 12 6,1789 19,6751 White Noise
```
```
([14], 1, 0) 12 6,5613 19,6751 White Noise
```
```
∆Z8 (0, 1, 1) 12 5,0375 19,6751 White Noise
```
```
(1, 1, 0) 12 6,3862 19,6751 White Noise
```
```
∆Z9 (0, 1, 1) 12 11,7473 19,6751 White Noise
```
```
(1, 1, 0) 12 10,0952 19,6751 White Noise
```
Setelah dilakukan uji white noise residual, tahap berikutnya adalah uji
heteroskedastisitas residual pada semua model ARIMA. Sebagai contoh, uji
```
heteroskedastisitas residual dilakukan pada model (0, 1, 1) untuk data ∆Z1 dengan lag 12
```
sesuai dengan subsubbab 2.7.3. Uji heteroskedastisitas residual dilakukan menggunakan
```
regresi bantuan berdasarkan persamaan (2.38). Dengan bantuan bahasa pemrograman R
```
pada perangkat lunak RStudio, diperoleh persamaan regresi bantuan sebagai berikut:
ε2t = 0,005374 + 0,046889ε2t−1 + 0,130348ε2t−2 + 0,011777ε2t−3
− 0,089013ε2t−4 + 0,204643ε2t−5 − 0,067795ε2t−6 + 0,019748ε2t−7
− 0,065867ε2t−8 + 0,012677ε2t−9 − 0,117753ε2t−10 + 0,010692ε2t−11
- 0,045790ε2t−12 + vt.
Uji heteroskedastisitas residual dilakukan dengan langkah-langkah sebagai berikut:
1. Hipotesis
Hipotesis yang digunakan dalam uji heteroskedastisitas residual adalah sebagai
```
berikut:
```
```
H0 : residual homoskedastis,
```
```
H1 : residual heteroskedastis.
```
2. Statistik Uji
```
Statistik uji ARCH-LM dihitung berdasarkan persamaan (2.39), yaitu
```
```
LMhitung = nR2.
```
Pada pengujian ini digunakan lag q = 12. Karena jumlah residual yang digunakan
adalah 80 data, maka banyak data efektif pada regresi bantuan adalah
```
n = 80 − 12 = 68.
```
Berdasarkan hasil regresi bantuan, diperoleh nilai
```
R2 = 0,08753.
```
60
Dengan demikian, statistik uji ARCH-LM diperoleh sebagai berikut:
```
LMhitung = nR2 = 68(0,08753) = 5,9522.
```
Selain itu, nilai kritis chi-square pada taraf signifikansi 5% dengan derajat bebas 12
adalah
```
χ2tabel = χ20,05;12 = 21,0261.
```
3. Daerah Kritis
Kriteria pengujian heteroskedastisitas residual adalah sebagai berikut:
LMhitung > χ2tabel maka H0 ditolak,
LMhitung ≤ χ2tabel maka H0 gagal ditolak.
4. Keputusan
Karena
```
LMhitung = 5,9522 ≤ χ2tabel = 21,0261,
```
```
maka H0 gagal ditolak. Dengan demikian, residual model (0, 1, 1) pada data ∆Z1
```
bersifat homoskedastis.
Berikut hasil uji heteroskedastisitas residual untuk model ARIMA pada masing-masing
variabel.
Tabel 4.14 Hasil Uji Heteroskedastisitas Residual Model ARIMA
Variabel Model Lag LMhitung χ2tabel Keputusan
```
∆Z1 (1, 1, 0) 12 9,2532 21,0261 Homoskedastis
```
```
(0, 1, 1) 12 5,9522 21,0261 Homoskedastis
```
```
∆Z2 (0, 1, 1) 12 4,7658 21,0261 Homoskedastis
```
```
(1, 1, 0) 12 7,0803 21,0261 Homoskedastis
```
```
∆2Z3 (4, 2, 0) 12 7,4858 21,0261 Homoskedastis
```
```
(2, 2, 0) 12 7,0417 21,0261 Homoskedastis
```
```
(0, 2, 2) 12 4,1754 21,0261 Homoskedastis
```
```
(2, 2, 2) 12 5,5595 21,0261 Homoskedastis
```
```
([2], 2, 0) 12 6,0482 21,0261 Homoskedastis
```
```
([2], 2, 2) 12 5,6880 21,0261 Homoskedastis
```
```
∆Z4 (0, 1, 1) 12 1,1382 21,0261 Homoskedastis
```
```
(1, 1, 0) 12 2,0993 21,0261 Homoskedastis
```
```
(2, 1, 0) 12 1,2129 21,0261 Homoskedastis
```
```
∆Z5 (1, 1, 0) 12 12,0166 21,0261 Homoskedastis
```
```
(0, 1, 1) 12 11,2726 21,0261 Homoskedastis
```
```
(Tabel dilanjutkan pada halaman berikutnya)
```
61
```
Tabel 4.14 Hasil Uji Heteroskedastisitas Residual Model ARIMA (Lanjutan)
```
Variabel Model Lag LMhitung χ2tabel Keputusan
```
∆Z6 (0, 1, 1) 12 9,0365 21,0261 Homoskedastis
```
```
(1, 1, 0) 12 5,8723 21,0261 Homoskedastis
```
```
∆Z7 (0, 1, [14]) 12 2,1171 21,0261 Homoskedastis
```
```
([14], 1, 0) 12 2,1826 21,0261 Homoskedastis
```
```
∆Z8 (0, 1, 1) 12 18,5681 21,0261 Homoskedastis
```
```
(1, 1, 0) 12 14,2995 21,0261 Homoskedastis
```
```
∆Z9 (0, 1, 1) 12 7,5880 21,0261 Homoskedastis
```
```
(1, 1, 0) 12 7,4386 21,0261 Homoskedastis
```
Setelah diperoleh tiga hasil uji diagnostik residual, ringkasan hasil uji diagnostik
residual model ARIMA disajikan pada tabel berikut:
Tabel 4.15 Ringkasan Uji Diagnostik Residual Model ARIMA
Variabel Model Uji Normalitas Uji White Noise Uji Heteroskedastisitas Keputusan
```
∆Z1(1, 1, 0) Normal White Noise Homoskedastis Layak(0, 1, 1) Normal White Noise Homoskedastis Layak
```
```
∆Z2(0, 1, 1) Normal White Noise Homoskedastis Layak(1, 1, 0) Normal White Noise Homoskedastis Layak
```
∆2Z3
```
(4, 2, 0) Normal Bukan White Noise Homoskedastis Tidak Layak
```
```
(2, 2, 0) Normal Bukan White Noise Homoskedastis Tidak Layak
```
```
(0, 2, 2) Normal Bukan White Noise Homoskedastis Tidak Layak
```
```
(2, 2, 2) Normal White Noise Homoskedastis Layak
```
```
([2], 2, 0) Normal Bukan White Noise Homoskedastis Tidak Layak
```
```
([2], 2, 2) Normal White Noise Homoskedastis Layak
```
∆Z4
```
(0, 1, 1) Normal White Noise Homoskedastis Layak
```
```
(1, 1, 0) Normal White Noise Homoskedastis Layak
```
```
(2, 1, 0) Normal White Noise Homoskedastis Layak
```
```
∆Z5(1, 1, 0) Normal Bukan White Noise Homoskedastis Tidak Layak(0, 1, 1) Normal White Noise Homoskedastis Layak
```
```
∆Z6(0, 1, 1) Normal White Noise Homoskedastis Layak(1, 1, 0) Normal White Noise Homoskedastis Layak
```
```
∆Z7(0, 1, [14]) Normal White Noise Homoskedastis Layak([14], 1, 0) Tidak Normal White Noise Homoskedastis Tidak Layak
```
```
∆Z8(0, 1, 1) Normal White Noise Homoskedastis Layak(1, 1, 0) Normal White Noise Homoskedastis Layak
```
```
∆Z9(0, 1, 1) Normal White Noise Homoskedastis Layak(1, 1, 0) Normal White Noise Homoskedastis Layak
```
Berdasarkan Tabel 4.15, model yang dipilih pada masing-masing variabel adalah
model yang termasuk dalam kategori layak dan memiliki seluruh parameter yang
signifikan. Model dikatakan layak apabila residual berdistribusi normal, bersifat
white noise, dan homoskedastis. Berdasarkan hasil uji heteroskedastisitas, seluruh
residual model bersifat homoskedastis, sehingga tidak diperlukan pemodelan lanjutan
```
menggunakan GARCH. Khusus pada variabel ∆2Z3, model ([2], 2, 2) tetap dipilih
```
meskipun terdapat parameter yang tidak signifikan pada model tersebut. Hal ini
dikarenakan model lain pada variabel ∆2Z3 tidak memenuhi asumsi white noise.
62
4.3.3 Pemilihan Model Terbaik
Pemilihan model terbaik didasarkan pada nilai Mean Absolute Percentage Error
```
(MAPE) terendah dari model yang termasuk dalam kategori layak untuk masing-masing
```
```
variabel. Sebagai contoh, dilakukan perhitungan MAPE pada model (0, 1, 1) untuk data
```
∆Z1. Data testing yang digunakan dapat dilihat pada Lampiran 15, yaitu mulai dari
```
periode Maret 2024 sampai November 2025. Perhitungan MAPE untuk model (0, 1, 1)
```
pada ∆Z1 disajikan pada Tabel 4.16.
```
Tabel 4.16 Perhitungan MAPE Model (0, 1, 1) pada ∆Z1
```
```
Periode (t) Data Testing (Yt) Hasil Peramalan ( ˆYt)
```
∣∣
∣∣ Yt − ˆYt
Yt
∣∣
∣∣
Maret 2024 4,968571429 4,970374940 0,000362984
April 2024 5,243636364 4,970374940 0,052112962
Mei 2024 5,230869565 4,970374940 0,049799488
Juni 2024 5,108000000 4,970374940 0,026943042
Juli 2024 5,030869565 4,970374940 0,012024685
Agustus 2024 4,673181818 4,970374940 0,063597592
September 2024 4,401428571 4,970374940 0,129262867
Oktober 2024 4,603043478 4,970374940 0,079802327
November 2024 4,957142857 4,970374940 0,002669298
Desember 2024 5,076363636 4,970374940 0,020879330
Januari 2025 5,245043478 4,970374940 0,052367258
Februari 2025 5,012000000 4,970374940 0,008305080
Maret 2025 4,905428571 4,970374940 0,013239697
April 2025 4,932818182 4,970374940 0,007614662
Mei 2025 4,817545455 4,970374940 0,031721441
Juni 2025 4,532857143 4,970374940 0,096515924
Juli 2025 4,446913043 4,970374940 0,117711258
Agustus 2025 4,340952381 4,970374940 0,145000061
September 2025 4,307818182 4,970374940 0,153791737
Oktober 2025 4,270173913 4,970374940 0,163974831
November 2025 4,245312500 4,970374940 0,170813973
```
Berdasarkan Tabel 4.16, diperoleh nilai MAPE sesuai dengan persamaan (2.46)
```
sebagai berikut:
```
MAPE =
```
1
n
n∑
```
t=1
```
∣∣
∣∣
∣
Yt − ˆYt
Yt
∣∣
∣∣
∣ × 100%
=
1
21
```
(1,405152) × 100%
```
= 6,69120%.
```
Berdasarkan nilai MAPE tersebut, model (0, 1, 1) pada ∆Z1 termasuk dalam kategori
```
sangat baik karena nilai MAPE yang diperoleh kurang dari 10%.
Menggunakan bantuan bahasa pemrograman R pada perangkat lunak RStudio,
diperoleh nilai MAPE untuk keseluruhan model ARIMA. Program perhitungan MAPE
dapat dilihat pada Lampiran 5. Berikut adalah hasil perhitungan MAPE untuk setiap
model pada masing-masing variabel.
63
Tabel 4.17 Hasil Perhitungan MAPE Model ARIMA
```
Variabel Model MAPE(%) Keputusan
```
∆Z1
```
(0, 1, 1) 6,69120 Terpilih
```
```
(1, 1, 0) 7,36834 Tidak Terpilih
```
∆Z2
```
(1, 1, 0) 4,25461 Terpilih
```
```
(0, 1, 1) 4,47582 Tidak Terpilih
```
∆2Z3
```
([2], 2, 2) 5,11639 Terpilih
```
```
(2, 2, 2) 7,13427 Tidak Terpilih
```
∆Z4
```
(0, 1, 1) 4,21060 Terpilih
```
```
(2, 1, 0) 4,41676 Tidak Terpilih
```
```
(1, 1, 0) 4,44154 Tidak Terpilih
```
```
∆Z5 (0, 1, 1) 4,34140 Terpilih
```
∆Z6
```
(1, 1, 0) 14,84968 Terpilih
```
```
(0, 1, 1) 15,08889 Tidak Terpilih
```
```
∆Z7 (0, 1, [14]) 15,31203 Terpilih
```
∆Z8
```
(0, 1, 1) 3,75497 Terpilih
```
```
(1, 1, 0) 3,81760 Tidak Terpilih
```
∆Z9
```
(0, 1, 1) 2,64315 Terpilih
```
```
(1, 1, 0) 2,68649 Tidak Terpilih
```
Berdasarkan Tabel 4.17, model yang dipilih adalah model dengan nilai MAPE terkecil
pada setiap variabel. Model yang digunakan untuk suku bunga USD tenor 5 tahun
```
adalah ARIMA(0, 1, 1), sedangkan model yang digunakan untuk suku bunga USD tenor
```
```
10 tahun adalah ARIMA(1, 1, 0). Untuk suku bunga USD tenor 30 tahun, model yang
```
```
digunakan adalah ARIMA([2], 2, 2). Selanjutnya, model yang digunakan untuk suku
```
```
bunga EUR tenor 7 tahun adalah ARIMA(0, 1, 1), sedangkan untuk suku bunga EUR
```
```
tenor 10 tahun digunakan model ARIMA(0, 1, 1). Untuk suku bunga JPY tenor 5 tahun,
```
```
model yang digunakan adalah ARIMA(1, 1, 0), sedangkan untuk suku bunga JPY tenor
```
```
10 tahun digunakan model ARIMA(0, 1, [14]). Adapun untuk nilai tukar USD/EUR
```
```
dan USD/JPY, model yang digunakan secara berturut-turut adalah ARIMA(0, 1, 1) dan
```
```
ARIMA(0, 1, 1).
```
4.4 Hasil Peramalan Tingkat Suku Bunga dan Nilai Tukar Mata Uang
Setelah diperoleh model ARIMA terbaik untuk setiap variabel, model tersebut
digunakan untuk melakukan peramalan tingkat suku bunga dan nilai tukar mata uang.
Peramalan dilakukan untuk 12 periode ke depan, yaitu mulai dari Desember 2025
sampai November 2026. Sebelum model digunakan untuk melakukan peramalan, terlebih
dahulu dilakukan pemeriksaan terhadap kemampuan model dalam mengikuti pola data
training. Pembuatan plot data training dan hasil model dilakukan menggunakan bahasa
pemrograman R pada perangkat lunak RStudio. Program R yang digunakan untuk
membuat plot tersebut dapat dilihat pada Lampiran 6. Sebagai contoh, digunakan model
64
```
ARIMA(0, 1, 1) pada variabel suku bunga USD tenor 5 tahun. Plot data training dan
```
```
hasil model ARIMA(0, 1, 1) pada suku bunga USD tenor 5 tahun disajikan pada gambar
```
```
berikut:
```
```
Gambar 4.11 Plot Data Training dan Hasil Model ARIMA(0, 1, 1) pada Suku Bunga
```
USD Tenor 5 Tahun
```
Berdasarkan Gambar 4.11, dapat dilihat bahwa hasil model ARIMA(0, 1, 1) mampu
```
mengikuti pola data training pada suku bunga USD tenor 5 tahun. Dengan demikian,
model tersebut valid dan layak digunakan untuk meramalkan suku bunga USD tenor
5 tahun. Plot data training dan hasil model untuk model lainnya dapat dilihat pada
Lampiran 23. Berdasarkan Lampiran 23, seluruh model terpilih mampu mengikuti pola
data training, sehingga layak digunakan dalam proses peramalan.
Berikut adalah hasil peramalan tingkat suku bunga untuk 12 periode ke depan.
Tabel 4.18 Hasil Peramalan Tingkat Suku Bunga
Periode IR1 IR2 IR3 IR4 IR5 IR6 IR7
Dec-25 4,97431 4,991475 5,184656 3,705371 3,905557 1,21279847715089 1,739477
Jan-26 4,97431 4,991475 5,177821 3,705371 3,905557 1,21279847717296 1,739477
Feb-26 4,97431 4,991475 5,170997 3,705371 3,905557 1,21279847718156 1,739477
Mar-26 4,97431 4,991475 5,164184 3,705371 3,905557 1,21279847718492 1,739477
Apr-26 4,97431 4,991475 5,157382 3,705371 3,905557 1,21279847718623 1,739477
May-26 4,97431 4,991475 5,150592 3,705371 3,905557 1,21279847718674 1,739477
Jun-26 4,97431 4,991475 5,143813 3,705371 3,905557 1,21279847718694 1,739477
Jul-26 4,97431 4,991475 5,137044 3,705371 3,905557 1,21279847718702 1,739477
Aug-26 4,97431 4,991475 5,130287 3,705371 3,905557 1,21279847718705 1,739477
Sep-26 4,97431 4,991475 5,123541 3,705371 3,905557 1,21279847718706 1,739477
Oct-26 4,97431 4,991475 5,116807 3,705371 3,905557 1,21279847718706 1,739477
Nov-26 4,97431 4,991475 5,110083 3,705371 3,905557 1,21279847718706 1,739477
Berdasarkan Tabel 4.18, diperoleh hasil peramalan tingkat suku bunga untuk tujuh
variabel, yaitu IR1, IR2, IR3, IR4, IR5, IR6, dan IR7 selama periode Desember 2025
65
sampai November 2026. Hasil peramalan tersebut menunjukkan nilai tingkat suku bunga
yang akan digunakan dalam pembentukan komponen biaya utang valas. Selanjutnya,
hasil peramalan nilai tukar mata uang disajikan pada tabel berikut:
Tabel 4.19 Hasil Peramalan Nilai Tukar Mata Uang
Periode F X1 F X2
Dec-25 0,929404 150,256822
Jan-26 0,929404 150,256822
Feb-26 0,929404 150,256822
Mar-26 0,929404 150,256822
Apr-26 0,929404 150,256822
May-26 0,929404 150,256822
Jun-26 0,929404 150,256822
Jul-26 0,929404 150,256822
Aug-26 0,929404 150,256822
Sep-26 0,929404 150,256822
Oct-26 0,929404 150,256822
Nov-26 0,929404 150,256822
Berdasarkan Tabel 4.19, diperoleh hasil peramalan nilai tukar mata uang untuk
variabel F X1 dan F X2 selama periode Desember 2025 sampai November 2026. Seluruh
hasil peramalan tingkat suku bunga dan nilai tukar mata uang diperoleh menggunakan
bahasa pemrograman R pada perangkat lunak RStudio, dengan kode program R yang
disajikan pada Lampiran 7. Hasil peramalan tersebut selanjutnya digunakan sebagai
data input dalam pembentukan model biaya utang valas dan model optimasi portofolio.
Gabungan data historis dan data hasil peramalan dapat dilihat pada Lampiran 18.
4.5 Pembentukan Model Biaya Utang dan Model Optimasi
Pada bagian ini dibahas tahapan pembentukan model biaya utang valas dan
model optimasi portofolio yang digunakan dalam penelitian. Pembahasan diawali
dengan pembentukan model biaya utang valas berdasarkan komponen nilai tukar dan
tingkat suku bunga. Selanjutnya, dijelaskan pembentukan batasan model optimasi
portofolio yang meliputi batas proporsi aset, batas anggaran, dan batas risiko maksimum.
Setelah itu, model optimasi portofolio dirumuskan menggunakan metode Mean-Variance
```
Optimization (MVO) dan Conditional Value at Risk (CVaR) sebagai pendekatan untuk
```
memperoleh komposisi portofolio utang valas yang optimal.
4.5.1 Pembentukan Model Biaya Utang
Berdasarkan variabel penelitian yang telah dijelaskan pada Tabel 3.1, model biaya
utang valas dibentuk dengan menggabungkan komponen nilai tukar dan faktor bunga.
Secara umum, biaya utang valas dapat dipandang sebagai nilai pokok utang dalam satuan
nilai tukar tertentu ditambah dengan beban bunga yang melekat pada pokok utang
tersebut. Jika F Xj,t menyatakan nilai tukar untuk jenis valuta ke-j pada periode ke-
t, maka komponen pokok utang dinyatakan oleh F Xj,t. Sementara itu, komponen bunga
66
utang diperoleh dari hasil perkalian antara nilai pokok dan tingkat suku bunga, yaitu
F Xj,tIRi,t. Dengan demikian, biaya utang valas untuk instrumen ke-i dengan jenis nilai
tukar ke-j pada periode ke-t dapat dituliskan sebagai
Cij,t = F Xj,t + F Xj,tIRi,t
```
Cij,t = F Xj,t(1 + IRi,t), (4.2)
```
```
dengan i = 1, 2, . . . , 7 dan j = 0, 1, 2. Persamaan (4.2) menunjukkan bahwa biaya utang
```
valas dipengaruhi oleh perubahan nilai tukar dan tingkat suku bunga. Semakin besar
nilai tukar atau tingkat suku bunga, maka semakin besar pula biaya utang valas yang
harus ditanggung. Berikut keterangan indeks pada model biaya utang valas.
Tabel 4.20 Keterangan Indeks Model Biaya Utang Valas
i j Keterangan
1 0 Biaya utang valas USD tenor 5 tahun
2 0 Biaya utang valas USD tenor 10 tahun
3 0 Biaya utang valas USD tenor 30 tahun
4 1 Biaya utang valas EUR tenor 7 tahun
5 1 Biaya utang valas EUR tenor 10 tahun
6 2 Biaya utang valas JPY tenor 5 tahun
7 2 Biaya utang valas JPY tenor 10 tahun
Sebagai contoh, digunakan perhitungan biaya utang valas JPY tenor 5 tahun, yaitu
untuk i = 6 dan j = 2. Karena data tingkat suku bunga dinyatakan dalam persen, maka
nilai IR6,t terlebih dahulu dinyatakan dalam bentuk desimal dengan membagi nilainya
terhadap 100. Untuk periode pertama diperoleh
C62,1 = F X2,1
```
(
```
1 +
IR6,1
100
```
)
```
= 112.417000000
```
(
```
1 +
0.860142857
100
```
)
```
```
= 112.417000000(1.008601429)
```
= 113.383946796.
Nilai C62,1 = 113.383946796 menunjukkan bahwa nilai tukar F X2,1 = 112.417000000
disesuaikan dengan faktor bunga sebesar 1.008601429, sehingga biaya utang valas yang
terbentuk menjadi lebih besar daripada nilai tukarnya. Selisih antara C62,1 dan F X2,1,
yaitu sebesar 0,966946796, merepresentasikan tambahan biaya akibat faktor bunga pada
periode pertama. Selanjutnya, untuk periode kedua diperoleh
C62,2 = F X2,2
```
(
```
1 +
IR6,2
100
```
)
```
= 109.826956522
```
(
```
1 +
0.823347826
100
```
)
```
```
= 109.826956522(1.008233478)
```
= 110.731214381.
67
Nilai C62,2 = 110,731214381 menunjukkan bahwa nilai tukar F X2,2 = 109,826956522
disesuaikan dengan faktor bunga sebesar 1,008233478, sehingga biaya utang valas yang
terbentuk menjadi lebih besar daripada nilai tukarnya. Selisih antara C62,2 dan F X2,2,
yaitu sebesar 0,904257859, merepresentasikan tambahan biaya akibat faktor bunga pada
periode kedua. Untuk periode ketiga diperoleh
C62,3 = F X2,3
```
(
```
1 +
IR6,3
100
```
)
```
= 110.776000000
```
(
```
1 +
0.818380952
100
```
)
```
```
= 110.776000000(1.008183810)
```
= 111.682569683.
Nilai C62,3 = 111.682569683 menunjukkan bahwa nilai tukar F X2,3 = 110.776000000
disesuaikan dengan faktor bunga sebesar 1.008183810, sehingga biaya utang valas yang
terbentuk menjadi lebih besar daripada nilai tukarnya. Selisih antara C62,3 dan F X2,3,
yaitu sebesar 0,906569683, merepresentasikan tambahan biaya akibat faktor bunga pada
periode ketiga. Berdasarkan ketiga hasil perhitungan tersebut, biaya utang valas JPY
tenor 5 tahun mengalami penurunan dari periode pertama ke periode kedua, yaitu
dari 113.383946796 menjadi 110.731214381, kemudian mengalami kenaikan pada periode
ketiga menjadi 111.682569683. Hasil perhitungan biaya utang valas secara lengkap
disajikan pada Lampiran 19. Berdasarkan hasil perhitungan tersebut, diperoleh sebanyak
113 data biaya utang valas untuk setiap instrumen.
Selanjutnya, persentase perubahan biaya utang antarperiode dibentuk berdasarkan
```
persamaan (2.47). Persentase perubahan biaya utang untuk instrumen ke-i dan jenis nilai
```
tukar ke-j pada periode ke-t didefinisikan sebagai berikut:
rij,t =
Cij,t+1 − Cij,t
Cij,t
.
Nilai rij,t merepresentasikan persentase perubahan biaya utang dari periode ke-t ke
periode ke-t + 1. Dalam konteks biaya utang, nilai rij,t > 0 menunjukkan bahwa
biaya utang pada periode berikutnya lebih besar dibandingkan periode sebelumnya,
sehingga terjadi peningkatan biaya. Sebaliknya, nilai rij,t < 0 menunjukkan bahwa biaya
utang pada periode berikutnya lebih kecil dibandingkan periode sebelumnya, sehingga
terjadi penurunan biaya. Adapun nilai rij,t = 0 menunjukkan bahwa biaya utang tidak
mengalami perubahan. Sebagai contoh, perhitungan persentase perubahan biaya utang
valas JPY dengan jangka waktu pelunasan 5 tahun pada periode pertama diperoleh
sebagai berikut:
r62,1 =
C62,2 − C62,1
C62,1
=
110.731214381 − 113.383946796
113.383946796
= −0.023395850.
Nilai r62,1 = −0.023395850 menunjukkan bahwa biaya utang valas JPY tenor 5 tahun
mengalami penurunan dari periode pertama ke periode kedua sebesar 2.3395850%.
68
Dengan demikian, biaya utang valas pada periode kedua lebih rendah dibandingkan
periode pertama. Untuk periode kedua diperoleh
r62,2 =
C62,3 − C62,2
C62,2
=
111.682569683 − 110.731214381
110.731214381
= 0.008591581.
Nilai r62,2 = 0.008591581 menunjukkan bahwa biaya utang valas JPY tenor 5 tahun
mengalami kenaikan dari periode kedua ke periode ketiga sebesar 0.8591581%. Dengan
demikian, biaya utang valas pada periode ketiga lebih tinggi dibandingkan periode
kedua. Hasil perhitungan persentase perubahan biaya utang secara lengkap disajikan
pada Lampiran 20. Berdasarkan hasil perhitungan tersebut, diperoleh sebanyak 112 data
persentase perubahan biaya utang untuk setiap instrumen.
4.5.2 Pembentukan Batasan Model Optimasi Portofolio
Variabel keputusan pada model optimasi portofolio dinyatakan dalam bentuk vektor
bobot portofolio, yaitu
```
x =
```
[
x1 x2 x3 x4 x5 x6 x7
]T
,
dengan xi menyatakan proporsi alokasi dana pada instrumen utang ke-i, untuk i =
1, 2, . . . , 7. Pada penelitian ini, x1 menyatakan bobot alokasi pada biaya utang valas USD
tenor 5 tahun, x2 menyatakan bobot alokasi pada biaya utang valas USD tenor 10 tahun,
x3 menyatakan bobot alokasi pada biaya utang valas USD tenor 30 tahun, x4 menyatakan
bobot alokasi pada biaya utang valas EUR tenor 7 tahun, x5 menyatakan bobot alokasi
pada biaya utang valas EUR tenor 10 tahun, x6 menyatakan bobot alokasi pada biaya
utang valas JPY tenor 5 tahun, dan x7 menyatakan bobot alokasi pada biaya utang
valas JPY tenor 10 tahun. Berdasarkan proporsi yang digunakan oleh badan pengelola
utang negara pada tahun 2024, bobot portofolio awal yang digunakan dalam penelitian
ini adalah sebagai berikut:
```
x(0) =
```







0,459485835
0,113620854
0,147798763
0,143927407
0,024401992
0,066688212
0,044076937







```
. (4.3)
```
```
Vektor x(0) tersebut menunjukkan proporsi alokasi portofolio awal pada masing-masing
```
instrumen utang. Sebagai contoh, misalkan pemerintah memiliki total utang valas sebesar
100 miliar rupiah dan dana yang tersedia untuk pembayaran utang tersebut adalah sebesar
```
50 miliar rupiah. Berdasarkan bobot x(0), dana pembayaran tersebut dialokasikan ke
```
dalam tujuh instrumen utang valas. Untuk biaya utang valas USD tenor 5 tahun, alokasi
pembayarannya adalah sebesar 0,459485835 × 50 miliar rupiah atau sekitar 22,97429175
miliar rupiah. Selanjutnya, alokasi pembayaran untuk biaya utang valas USD tenor 10
tahun adalah sekitar 5,68104270 miliar rupiah, USD tenor 30 tahun sekitar 7,38993815
miliar rupiah, EUR tenor 7 tahun sekitar 7,19637035 miliar rupiah, EUR tenor 10 tahun
69
sekitar 1,22009960 miliar rupiah, JPY tenor 5 tahun sekitar 3,33441060 miliar rupiah,
dan JPY tenor 10 tahun sekitar 2,20384685 miliar rupiah. Dengan demikian, setiap nilai
xi menyatakan bagian dana pembayaran yang dialokasikan pada instrumen utang ke-i.
Dalam penerapannya, dana yang tersedia untuk membayarkan utang harus dialokasikan
seluruhnya ke dalam ketujuh instrumen utang valas. Oleh karena itu, total bobot alokasi
portofolio harus bernilai satu. Kendala tersebut dinyatakan sebagai berikut:
7∑
```
i=1
```
```
xi = 1.
```
Pada penelitian ini digunakan tiga skenario batasan proporsi portofolio. Skenario
pertama adalah batasan Kementerian Keuangan, yaitu batasan yang diberikan oleh badan
pengelola utang negara. Batasan ini digunakan agar hasil optimasi tetap berada pada
rentang proporsi yang sesuai dengan kebijakan atau komposisi portofolio yang ditetapkan
oleh badan pengelola utang negara. Batasan Kementerian Keuangan tersebut dinyatakan
sebagai berikut:
0,425 ≤ x1 ≤ 0,490,
0,100 ≤ x2 ≤ 0,125,
0,130 ≤ x3 ≤ 0,165,
0,130 ≤ x4 ≤ 0,155,
0,015 ≤ x5 ≤ 0,030,
0,050 ≤ x6 ≤ 0,085,
0,030 ≤ x7 ≤ 0,055.
Skenario kedua adalah batasan yang diperlebar sebesar 5% dari proporsi portofolio yang
digunakan oleh badan pengelola utang negara pada tahun 2024. Pelebaran batasan ini
dilakukan untuk memberikan ruang yang lebih fleksibel bagi model optimasi, sehingga
dapat diamati instrumen utang mana yang cenderung mendominasi ketika batas proporsi
dibuat lebih longgar. Besaran 5% digunakan karena merupakan batas pelebaran yang
masih diwajarkan oleh badan pengelola utang negara. Artinya, untuk setiap proporsi awal
```
x(0)i , batas bawah dan batas atas masing-masing dibentuk melalui persamaan berikut:
```
```
LBi = x(0)i − 0,05x(0)i dan U Bi = x(0)i + 0,05x(0)i .
```
```
Sebagai contoh, untuk proporsi awal biaya utang valas USD tenor 5 tahun, yaitu x(0)1 =
```
```
0,459485835, diperoleh batas bawah 0,459485835 − 0,05(0,459485835) = 0,436511543250
```
```
dan batas atas 0,459485835 + 0,05(0,459485835) = 0,482460126750. Dengan demikian,
```
batasan lengkap pada skenario kedua adalah sebagai berikut:
0,436511543250 ≤ x1 ≤ 0,482460126750,
0,107939811300 ≤ x2 ≤ 0,119301896700,
0,140408824850 ≤ x3 ≤ 0,155188701150,
0,136731036650 ≤ x4 ≤ 0,151123777350,
0,023181892400 ≤ x5 ≤ 0,025622091600,
0,063353801400 ≤ x6 ≤ 0,070022622600,
0,041873090150 ≤ x7 ≤ 0,046280783850.
70
Skenario ketiga adalah model tanpa batasan proporsi khusus. Pada skenario ini, setiap
instrumen hanya dibatasi oleh batas dasar bobot portofolio, yaitu
0 ≤ xi ≤ 1, i = 1, 2, . . . , 7.
Tujuan diadakannya skenario ketiga adalah untuk melihat instrumen utang mana yang
akan mendominasi apabila tidak terdapat kebijakan batasan pembayaran pada masing-
masing instrumen, oleh karena itu skenario ketiga memberikan ruang solusi yang paling
fleksibel karena model optimasi dapat menentukan proporsi setiap instrumen secara bebas
selama seluruh bobot portofolio tetap berjumlah satu.
4.5.3 Pembentukan Model Optimasi Portofolio dengan Mean-Variance
```
Optimization (MVO)
```
```
Model optimasi portofolio dengan metode Mean-Variance Optimization (MVO)
```
dibentuk berdasarkan model umum pada persamaan 2.54 dan disesuaikan dengan tiga
skenario batasan proporsi portofolio yang telah dijelaskan sebelumnya. Karena penelitian
ini berfokus pada minimisasi biaya utang, maka fungsi objektif yang digunakan adalah
meminimumkan nilai ekspektasi biaya portofolio, yaitu μT x. Selain itu, risiko portofolio
dibatasi oleh Rmax melalui bentuk kuadratik xT Σx. Dengan demikian, model MVO
pertama menggunakan batasan Kementerian Keuangan dan dinyatakan sebagai berikut:
minx μT x
dengan kendala xT Σx ≤ Rmax,
7∑
```
i=1
```
```
xi = 1,
```
0,425 ≤ x1 ≤ 0,490,
0,100 ≤ x2 ≤ 0,125,
0,130 ≤ x3 ≤ 0,165,
0,130 ≤ x4 ≤ 0,155,
0,015 ≤ x5 ≤ 0,030,
0,050 ≤ x6 ≤ 0,085,
0,030 ≤ x7 ≤ 0,055.
```
(4.4)
```
Model MVO kedua menggunakan batasan yang diperlebar sebesar 5% dari proporsi
portofolio yang digunakan oleh badan pengelola utang negara pada tahun 2024. Model
71
ini dinyatakan sebagai berikut:
minx μT x
dengan kendala xT Σx ≤ Rmax,
7∑
```
i=1
```
```
xi = 1,
```
0,436511543250 ≤ x1 ≤ 0,482460126750,
0,107939811300 ≤ x2 ≤ 0,119301896700,
0,140408824850 ≤ x3 ≤ 0,155188701150,
0,136731036650 ≤ x4 ≤ 0,151123777350,
0,023181892400 ≤ x5 ≤ 0,025622091600,
0,063353801400 ≤ x6 ≤ 0,070022622600,
0,041873090150 ≤ x7 ≤ 0,046280783850.
```
(4.5)
```
Model MVO ketiga merupakan model tanpa batasan proporsi khusus. Pada model ini,
setiap bobot instrumen hanya dibatasi oleh interval dasar 0 ≤ xi ≤ 1, sehingga model
memiliki ruang solusi yang lebih fleksibel. Model ketiga dinyatakan sebagai berikut:
minx μT x
dengan kendala xT Σx ≤ Rmax,
7∑
```
i=1
```
```
xi = 1,
```
0 ≤ xi ≤ 1, i = 1, 2, . . . , 7.
```
(4.6)
```
Dalam pembentukan model MVO, nilai Rmax berperan sebagai batas maksimum
risiko portofolio yang masih diperbolehkan. Pada penelitian ini, terdapat dua cara yang
digunakan untuk menentukan nilai Rmax. Cara pertama adalah menggunakan risiko dari
portofolio awal, yaitu portofolio yang berdasarkan proporsi badan pengelola utang negara
pada tahun 2024 yang dirumuskan sebagai berikut:
```
Rmax =
```
```
(
```
```
x(0)
```
```
)T
```
```
Σx(0). (4.7)
```
Cara kedua adalah menggunakan risiko dari portofolio dengan proporsi yang sama untuk
```
setiap instrumen. Misalkan vektor bobot portofolio merata dinotasikan sebagai x(s),
```
dengan
```
x(s) =
```







0,142857143
0,142857143
0,142857143
0,142857143
0,142857143
0,142857143
0,142857143







.
72
Nilai Rmax pada cara kedua dinyatakan sebagai berikut:
```
Rmax =
```
```
(
```
```
x(s)
```
```
)T
```
```
Σx(s). (4.8)
```
Kedua nilai Rmax tersebut digunakan untuk membandingkan hasil optimasi ketika batas
risiko ditentukan berdasarkan struktur portofolio awal dan ketika batas risiko ditentukan
berdasarkan alokasi portofolio yang merata.
Selanjutnya, kurva efficient frontier digunakan untuk melihat berbagai pilihan
portofolio terbaik secara keseluruhan pada setiap tingkat risiko. Langkah awal dalam
pembuatan kurva ini adalah menentukan batas bawah dan batas atas risiko. Batas
```
bawah risiko didapatkan dengan mencari nilai risiko (varians) paling kecil melalui model
```
matematika berikut:
minx xT Σx
dengan kendala
7∑
```
i=1
```
```
xi = 1,
```
lbi ≤ xi ≤ ubi, i = 1, 2, . . . , 7.
```
(4.9)
```
Sebaliknya, batas atas risiko didapatkan dari nilai risiko ketika perkiraan biaya berada
pada titik paling kecil. Model matematika untuk mencari komposisi pada batas atas ini
adalah sebagai berikut:
minx μT x
dengan kendala
7∑
```
i=1
```
```
xi = 1,
```
lbi ≤ xi ≤ ubi, i = 1, 2, . . . , 7.
```
(4.10)
```
Pada kedua model tersebut, nilai lbi dan ubi menyesuaikan dengan aturan batasan
portofolio yang sedang dihitung. Setelah batas bawah dan batas atas risiko diketahui,
jarak antara kedua batas tersebut dibagi rata menjadi 1.000 titik nilai Rmax. Pada setiap
titik tersebut, perhitungan dilakukan kembali menggunakan Rmax sebagai batas risiko
```
maksimal. Tujuannya adalah mencari komposisi bobot portofolio (x) yang menghasilkan
```
```
perkiraan perubahan biaya utang (μT x) paling kecil. Hasil dari 1.000 kali perhitungan ini
```
kemudian digambarkan pada sebuah grafik. Sumbu mendatar pada grafik menunjukkan
```
tingkat risiko atau standar deviasi (
```
√
```
xT Σx), sedangkan sumbu tegak menunjukkan
```
perkiraan perubahan biaya. Titik-titik hasil perhitungan yang saling terhubung ini akan
membentuk sebuah garis kurva. Kurva inilah yang dinamakan efficient frontier, yaitu
garis yang menunjukkan kumpulan pilihan portofolio terbaik karena selalu memberikan
biaya utang paling murah pada setiap tingkat risiko yang dipilih.
4.5.4 Pembentukan Model Optimasi Portofolio dengan Kendala Risiko
```
Conditional Value at Risk (CVaR)
```
```
Model optimasi portofolio dengan metode Conditional Value at Risk (CVaR) dibentuk
```
berdasarkan model umum pada persamaan 2.68 dan disesuaikan dengan tiga skenario
batasan proporsi portofolio yang telah dijelaskan sebelumnya. Pada persamaan 2.68,
```
fungsi kerugian dinyatakan sebagai f (x, yk). Dalam penelitian ini, fungsi kerugian
```
73
tersebut didefinisikan sebagai
```
f (x, yk) = rTk x,
```
karena rk merepresentasikan vektor persentase perubahan biaya utang pada periode
ke-k, sedangkan x merepresentasikan vektor bobot portofolio. Dengan demikian, rTk x
menyatakan persentase perubahan biaya utang portofolio pada periode ke-k. Karena
penelitian ini berfokus pada minimisasi biaya utang, maka fungsi objektif yang digunakan
adalah meminimumkan nilai ekspektasi biaya portofolio, yaitu μT x. Risiko portofolio
dibatasi oleh Rmax, dengan ukuran risiko yang digunakan berupa CVaR. Dalam model
```
ini, α menyatakan nilai Value at Risk (VaR), sedangkan uk merupakan variabel bantu
```
yang merepresentasikan kelebihan kerugian portofolio pada periode ke-k terhadap nilai
α. Karena data persentase perubahan biaya utang yang digunakan berjumlah 100, maka
indeks k digunakan untuk k = 1, 2, . . . , 100. Dengan demikian, model CVaR pertama
menggunakan batasan Kementerian Keuangan dan dinyatakan sebagai berikut:
minx,α,ukμT x
dengan kendala α +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk ≤ Rmax,
uk ≥ rTk x − α, k = 1, . . . , 100,
uk ≥ 0, k = 1, . . . , 100,
7∑
```
i=1
```
```
xi = 1,
```
0,425 ≤ x1 ≤ 0,490,
0,100 ≤ x2 ≤ 0,125,
0,130 ≤ x3 ≤ 0,165,
0,130 ≤ x4 ≤ 0,155,
0,015 ≤ x5 ≤ 0,030,
0,050 ≤ x6 ≤ 0,085,
0,030 ≤ x7 ≤ 0,055.
```
(4.11)
```
Model CVaR kedua menggunakan batasan yang diperlebar sebesar 5% dari proporsi
portofolio yang digunakan oleh badan pengelola utang negara pada tahun 2024. Model
74
ini dinyatakan sebagai berikut:
minx,α,ukμT x
dengan kendala α +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk ≤ Rmax,
uk ≥ rTk x − α, k = 1, . . . , 100,
uk ≥ 0, k = 1, . . . , 100,
7∑
```
i=1
```
```
xi = 1,
```
0,436511543250 ≤ x1 ≤ 0,482460126750,
0,107939811300 ≤ x2 ≤ 0,119301896700,
0,140408824850 ≤ x3 ≤ 0,155188701150,
0,136731036650 ≤ x4 ≤ 0,151123777350,
0,023181892400 ≤ x5 ≤ 0,025622091600,
0,063353801400 ≤ x6 ≤ 0,070022622600,
0,041873090150 ≤ x7 ≤ 0,046280783850.
```
(4.12)
```
Model CVaR ketiga merupakan model tanpa batasan proporsi khusus. Pada model ini,
setiap bobot instrumen hanya dibatasi oleh interval dasar 0 ≤ xi ≤ 1, sehingga model
memiliki ruang solusi yang lebih fleksibel. Model ketiga dinyatakan sebagai berikut:
minx,α,ukμT x
dengan kendala α +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk ≤ Rmax,
uk ≥ rTk x − α, k = 1, . . . , 100,
uk ≥ 0, k = 1, . . . , 100,
7∑
```
i=1
```
```
xi = 1,
```
0 ≤ xi ≤ 1, i = 1, 2, . . . , 7.
```
(4.13)
```
Ketiga model CVaR tersebut diterapkan pada tiga tingkat kepercayaan, yaitu β = 0,90,
β = 0,95, dan β = 0,99. Penggunaan tiga nilai β tersebut bertujuan untuk melihat
perbedaan hasil optimasi pada tingkat risiko ekstrem yang berbeda. Semakin besar nilai
β, semakin kecil bagian ekor distribusi kerugian yang diperhatikan, sehingga ukuran CVaR
merepresentasikan rata-rata kerugian pada kondisi yang semakin ekstrem.
Dalam pembentukan model CVaR, nilai Rmax berperan sebagai batas maksimum
risiko portofolio yang masih diperbolehkan berdasarkan ukuran CVaR. Pada penelitian
ini, nilai Rmax ditentukan melalui dua cara. Cara pertama adalah menggunakan nilai
CVaR dari portofolio awal, yaitu portofolio berdasarkan proporsi badan pengelola utang
```
negara pada tahun 2024. Dengan menggunakan x(0), nilai Rmax ditentukan melalui model
```
75
```
berikut:
```
minα,ukα +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk
```
dengan kendala uk ≥ rTk x(0) − α, k = 1, . . . , 100,
```
uk ≥ 0, k = 1, . . . , 100.
```
(4.14)
```
Cara kedua adalah menggunakan nilai CVaR dari portofolio dengan proporsi yang sama
untuk setiap instrumen. Misalkan vektor bobot portofolio merata dinotasikan sebagai
```
x(s), nilai Rmax ditentukan melalui model berikut:
```
minα,ukα +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk
```
dengan kendala uk ≥ rTk x(s) − α, k = 1, . . . , 100,
```
uk ≥ 0, k = 1, . . . , 100.
```
(4.15)
```
Penentuan nilai Rmax tersebut dilakukan pada tiga tingkat kepercayaan, yaitu β = 0,90,
β = 0,95, dan β = 0,99
Selanjutnya, kurva efficient frontier digunakan untuk melihat berbagai pilihan
portofolio terbaik secara keseluruhan pada setiap tingkat risiko Conditional Value at Risk
```
(CVaR). Langkah pertama untuk membuat kurva ini adalah menentukan batas bawah
```
dan batas atas risiko. Batas bawah risiko didapatkan dengan mencari nilai risiko CVaR
paling kecil melalui model matematika berikut:
minx,α,ukα +
1
```
q(1 − β)
```
q∑
```
k=1
```
uk
dengan kendala uk ≥ rTk x − α, k = 1, . . . , q,
uk ≥ 0, k = 1, . . . , q,
7∑
```
i=1
```
```
xi = 1,
```
lbi ≤ xi ≤ ubi, i = 1, 2, . . . , 7.
```
(4.16)
```
Sebaliknya, batas atas risiko didapatkan dari nilai risiko ketika perkiraan biaya berada
```
pada titik paling kecil. Untuk mendapatkan nilai ini, komposisi portofolio terbaik (x∗)
```
```
dicari terlebih dahulu menggunakan model pencarian batas atas pada persamaan (4.10).
```
Setelah komposisi terbaik tersebut didapatkan, nilai x∗ disubstitusikan ke dalam model
```
persamaan (4.17) berikut untuk dihitung nilai risiko CVaR-nya.
```
minα,ukα +
1
```
q(1 − β)
```
q∑
```
k=1
```
uk
dengan kendala uk ≥ rTk x∗ − α, k = 1, . . . , q,
uk ≥ 0, k = 1, . . . , q.
```
(4.17)
```
Setelah batas bawah dan batas atas risiko diketahui, jarak antara kedua batas tersebut
dibagi rata menjadi 1.000 titik nilai Rmax. Pada setiap titik tersebut, perhitungan
dilakukan kembali menggunakan Rmax sebagai batas risiko maksimal. Tujuannya adalah
76
```
mencari komposisi bobot portofolio (x) yang menghasilkan perkiraan perubahan biaya
```
```
utang (μT x) paling kecil. Hasil dari 1.000 kali perhitungan ini kemudian digambarkan
```
pada sebuah grafik. Sumbu mendatar pada grafik menunjukkan tingkat risiko CVaR,
sedangkan sumbu tegak menunjukkan perkiraan perubahan biaya. Titik-titik hasil
perhitungan yang saling terhubung ini akan membentuk garis kurva efficient frontier,
yaitu garis yang menunjukkan kumpulan pilihan portofolio dengan biaya paling murah
pada setiap tingkat risiko ekstrem yang dipilih.
4.6 Implementasi Optimasi Portofolio
Pada bagian ini, pembahasan implementasi optimasi portofolio dilakukan melalui tiga
tahapan utama. Tahap pertama adalah menghitung parameter input yang digunakan
dalam model optimasi, yaitu vektor ekspektasi persentase perubahan biaya pembayaran
utang valas, matriks varians-kovarians, dan batas risiko maksimum Rmax. Tahap
kedua adalah menghitung kinerja portofolio aktual Pemerintah Indonesia sebagai acuan
pembanding. Tahap ketiga adalah memperoleh model terbaik dari hasil optimasi
MVO dan CVaR, kemudian mengevaluasi kinerjanya berdasarkan ekspektasi persentase
perubahan biaya pembayaran utang valas dan risiko.
4.6.1 Perhitungan Parameter Input
Parameter input yang digunakan dalam model optimasi portofolio terdiri atas vektor
ekspektasi persentase perubahan biaya utang, matriks varians-kovarians, dan nilai batas
risiko maksimum Rmax. Parameter tersebut dihitung berdasarkan gabungan data historis
dan hasil peramalan agar proses optimasi tidak hanya mempertimbangkan pola data masa
lalu, tetapi juga memuat informasi mengenai potensi perubahan biaya utang pada periode
mendatang.
Vektor ekspektasi persentase perubahan biaya utang dihitung menggunakan
```
persamaan (2.49) dengan N = 7 berdasarkan data gabungan historis dan hasil peramalan
```
persentase perubahan biaya utang pada Lampiran 20. Vektor ekspektasi persentase
perubahan biaya utang yang digunakan dalam penelitian ini adalah sebagai berikut:
μ =







0,000163792399765913
0,000110177775619655
0,000035896173297487
0,000932492126516585
0,000869169614771198
0,002831172063030670
0,002879522027475840







```
. (4.18)
```
Selanjutnya, matriks varians-kovarians digunakan sebagai parameter risiko dalam
model optimasi portofolio. Matriks varians-kovarians yang digunakan dalam penelitian ini
dihitung berdasarkan gabungan data historis dan hasil peramalan. Perhitungan matriks
tersebut dilakukan menggunakan bantuan program MATLAB berdasarkan persamaan
```
(2.50) dengan N = 7. Program MATLAB untuk perhitungan matriks varians-kovarians
```
disajikan pada Lampiran 8, sedangkan hasil lengkap matriks varians-kovarians Σ disajikan
pada Lampiran 24.
Mengacu pada matriks varians-kovarians Σ, nilai Rmax untuk model MVO ditentukan
```
melalui dua cara. Perhitungan pertama dilakukan menggunakan persamaan (4.7),
```
sehingga diperoleh
Rmax,1 = 0,000033683544775466,
77
```
sedangkan berdasarkan persamaan (4.8), diperoleh
```
Rmax,2 = 0,000101609932479855.
Selain itu, nilai Rmax untuk model CVaR dihitung berdasarkan dua portofolio acuan,
```
yaitu portofolio awal dan portofolio dengan bobot merata. Berdasarkan persamaan (4.14)
```
dengan β = 90%, diperoleh nilai batas risiko CVaR untuk portofolio awal sebagai berikut:
Rmax,3 = 0,011305009399949160,
```
berdasarkan persamaan (4.14) dengan β = 95%, diperoleh nilai batas risiko CVaR untuk
```
portofolio awal sebagai berikut:
Rmax,4 = 0,012714094856730768,
```
dan berdasarkan persamaan (4.14) dengan β = 99%, diperoleh nilai batas risiko CVaR
```
untuk portofolio awal sebagai berikut:
Rmax,5 = 0,016989970809430918.
```
Selanjutnya, berdasarkan persamaan (4.15) dengan β = 90%, diperoleh nilai batas
```
risiko CVaR untuk portofolio dengan bobot merata sebagai berikut:
Rmax,6 = 0,018880495149667626,
```
berdasarkan persamaan (4.15) dengan β = 95%, diperoleh nilai batas risiko CVaR untuk
```
portofolio dengan bobot merata sebagai berikut:
Rmax,7 = 0,022423957171019273,
```
dan berdasarkan persamaan (4.15) dengan β = 99%, diperoleh nilai batas risiko CVaR
```
untuk portofolio dengan bobot merata sebagai berikut:
Rmax,8 = 0,028964586540561284.
Secara keseluruhan, nilai-nilai Rmax yang digunakan dalam proses optimasi dapat
dinyatakan dalam bentuk vektor sebagai berikut:
```
Rmax =
```








0,000033683544775466
0,000101609932479855
0,011305009399949160
0,012714094856730768
0,016989970809430918
0,018880495149667626
0,022423957171019273
0,028964586540561284








```
. (4.19)
```
Program MATLAB untuk menentukan nilai Rmax berdasarkan model CVaR disajikan
pada Lampiran 9.
78
4.6.2 Portofolio Aktual Pemerintah Indonesia
```
Portofolio aktual Pemerintah Indonesia dinyatakan oleh bobot x(0) pada persamaan
```
```
(4.3). Kinerja portofolio aktual dihitung menggunakan parameter input yang diperoleh
```
dari gabungan data historis dan hasil peramalan. Pengukuran kinerja tersebut meliputi
ekspektasi persentase perubahan biaya pembayaran utang valas, standar deviasi, dan
```
Conditional Value at Risk (CVaR).
```
Ekspektasi persentase perubahan biaya pembayaran utang valas portofolio aktual
```
dihitung berdasarkan persamaan (2.51) dengan x disubstitusikan oleh x(0), sehingga
```
diperoleh
```
μT x(0).
```
Nilai tersebut merepresentasikan ekspektasi persentase perubahan biaya pembayaran
utang valas portofolio aktual dari satu periode ke periode berikutnya.
Selanjutnya, risiko portofolio aktual pada model MVO dihitung menggunakan standar
```
deviasi. Varians portofolio aktual dihitung berdasarkan persamaan (2.52) dengan x
```
```
disubstitusikan oleh x(0), sehingga diperoleh
```
```
(x(0))T Σx(0).
```
Standar deviasi portofolio aktual kemudian diperoleh dengan mengambil akar dari nilai
varians tersebut, yaitu √
```
(x(0))T Σx(0).
```
Matriks Σ yang digunakan dalam perhitungan ini dapat dilihat pada Lampiran 24.
Selain itu, risiko portofolio aktual juga dihitung menggunakan Conditional Value at
```
Risk (CVaR). Perhitungan CVaR dilakukan berdasarkan model pada persamaan (4.14)
```
```
dengan bobot portofolio aktual x(0). Perhitungan dilakukan menggunakan bantuan
```
MATLAB, dan kode programnya dapat dilihat pada Lampiran 10. Berdasarkan
perhitungan tersebut, diperoleh kinerja portofolio aktual seperti disajikan pada tabel
```
berikut:
```
Tabel 4.21 Kinerja Portofolio Aktual Pemerintah Indonesia
Bobot Ekspektasi Persentase Perubahan
Biaya Pembayaran Utang Valas Standar Deviasi
CVaR
Variabel Nilai 90% 95% 99%
x1 0,459485835
0,000562311480873920 0,005803752645958170 0,011305009399949160 0,012714094856730768 0,016989970809430918
x2 0,113620854
x3 0,147798763
x4 0,143927407
x5 0,024401992
x6 0,066688212
x7 0,044076937
Berdasarkan Tabel 4.21, ekspektasi persentase perubahan biaya pembayaran
utang valas portofolio aktual adalah sebesar 0,000562311480873920, atau sekitar
0,0562311480873920% per bulan. Nilai ini menunjukkan kecenderungan perubahan
biaya pembayaran utang valas portofolio aktual antarperiode, bukan nominal biaya
utang dalam rupiah. Risiko portofolio aktual berdasarkan standar deviasi adalah
sebesar 0,005803752645958170. Sementara itu, risiko berdasarkan CVaR pada
tingkat kepercayaan 90%, 95%, dan 99% masing-masing sebesar 0,011305009399949160,
0,012714094856730768, dan 0,016989970809430918. Hasil perhitungan ini digunakan
sebagai acuan dalam menilai hasil optimasi portofolio, baik pada model MVO maupun
model CVaR.
79
```
4.6.3 Hasil Optimasi Menggunakan Mean-Variance Optimization (MVO)
```
```
Penyelesaian model Mean-Variance Optimization (MVO) dilakukan menggunakan
```
bantuan MATLAB berdasarkan parameter input yang diperoleh dari gabungan data
historis dan hasil peramalan. Model MVO diselesaikan pada tiga skenario batasan bobot,
yaitu batasan Kementerian Keuangan yang berdasarkan pada persamaan 4.4, batasan
```
5% dari portofolio aktual x(0) yang berdasarkan pada persamaan 4.5, dan tanpa batasan
```
khusus yang berdasarkan pada persamaan 4.6. Ketiga skenario batasan tersebut masing-
masing diselesaikan dengan delapan batasan risiko maksimum sebagaimana dinyatakan
pada persamaan 4.19. Kode program penyelesaian model MVO dapat dilihat pada
Lampiran 11, dan hasil optimasi MVO disajikan pada tabel berikut:
Tabel 4.22 Portofolio Hasil Optimasi MVO
Batasan Batasan Kementerian Keuangan Batasan 5% Tanpa Batasan
Rmax Rmax,1, Rmax,2, . . . , Rmax,8 Rmax,1, Rmax,2, . . . , Rmax,8 Rmax,1, Rmax,2, . . . , Rmax,8
x1 0,4850 0,460369581550 0
x2 0,1250 0,119301896700 0
x3 0,1650 0,155188701150 1
x4 0,1300 0,136731036650 0
x5 0,0150 0,023181892400 0
x6 0,0500 0,063353801400 0
x7 0,0300 0,041873090150 0
Ekspektasi Persentase Perubahan
Biaya Pembayaran Utang Valas 0,000455644978376515 0,000536353186620772 0,000001379744806410
Standar deviasi portofolio 0,005045420400454560 0,005603754941621760 0,001966331117551670
Berdasarkan Tabel 4.22, seluruh skenario nilai Rmax menghasilkan komposisi bobot
yang sama pada masing-masing skenario batasan. Pada batasan Kementerian Keuangan,
bobot portofolio optimal adalah x1 = 0,4850 atau 48,50%, x2 = 0,1250 atau 12,50%,
```
x3 = 0,1650 atau 16,50%, x4 = 0,1300 atau 13,00%, x5 = 0,0150 atau 1,50%, x6 = 0,0500
```
atau 5,00%, dan x7 = 0,0300 atau 3,00%. Ketika batasan bobot diperlebar menjadi 5%,
komposisi portofolio optimal mengalami pergeseran, yaitu bobot x1 turun dari 48,50%
menjadi 46,04%, bobot x2 turun dari 12,50% menjadi 11,93%, dan bobot x3 turun dari
16,50% menjadi 15,52%. Sebaliknya, bobot x4 naik dari 13,00% menjadi 13,67%, bobot
x5 naik dari 1,50% menjadi 2,32%, bobot x6 naik dari 5,00% menjadi 6,34%, dan bobot
x7 naik dari 3,00% menjadi 4,19%. Pergeseran tersebut menunjukkan bahwa ketika ruang
alokasi bobot diperlebar, model MVO mengurangi porsi pada instrumen x1, x2, dan x3,
serta meningkatkan porsi pada instrumen x4, x5, x6, dan x7. Dengan demikian, pelebaran
batasan membuat komposisi portofolio optimal menjadi lebih menyebar ke instrumen
berbasis EUR dan JPY, tetapi konsekuensinya nilai ekspektasi persentase perubahan
biaya pembayaran utang valas dan standar deviasi menjadi lebih tinggi dibandingkan
batasan Kementerian Keuangan. Pada skenario tanpa batasan, model MVO memilih
```
x3 = 1 atau 100%, sedangkan bobot instrumen lainnya bernilai 0. Hal ini terjadi karena
```
x3 memiliki nilai ekspektasi persentase perubahan biaya pembayaran utang valas paling
rendah berdasarkan vektor μ pada persamaan 4.18. Pemilihan x3 secara penuh membuat
nilai ekspektasi persentase perubahan biaya dan risiko menjadi paling rendah, namun
hasil tersebut tidak mungkin diterapkan secara langsung dalam kehidupan nyata karena
Pemerintah Indonesia tetap memiliki kewajiban pembayaran pada berbagai instrumen
utang valas lainnya. Dari dua skenario batasan yang masih realistis, yaitu batasan
Kementerian Keuangan dan batasan 5%, batasan Kementerian Keuangan menghasilkan
80
ekspektasi persentase perubahan biaya pembayaran utang valas yang lebih kecil, yaitu
0,000455644978376515, dibandingkan batasan 5% sebesar 0,000536353186620772. Risiko
berdasarkan standar deviasi juga lebih rendah pada batasan Kementerian Keuangan,
yaitu 0,005045420400454560, dibandingkan batasan 5% sebesar 0,005603754941621760.
Dengan demikian, pelebaran batasan sebesar 5% belum menghasilkan portofolio yang
lebih baik dibandingkan batasan Kementerian Keuangan, baik dari sisi ekspektasi
persentase perubahan biaya maupun risiko. Selanjutnya, kurva efficient frontier untuk
model MVO pada dua skenario batasan yang masih relevan, yaitu batasan Kementerian
Keuangan dan batasan 5%, disajikan pada gambar berikut:
```
(a) Batasan Kementerian Keuangan (b) Batasan 5%
```
Gambar 4.12 Efficient Frontier MVO Berdasarkan Gabungan Data Historis dan Hasil
Peramalan
Berdasarkan Gambar 4.12, titik merah menunjukkan portofolio dengan risiko
minimum yang dapat dicapai pada masing-masing skenario batasan. Pada skenario
batasan Kementerian Keuangan, hasil yang diperoleh tidak membentuk kurva efficient
frontier dengan banyak titik, melainkan hanya menghasilkan satu titik portofolio optimal.
Hal ini menunjukkan bahwa seluruh nilai Rmax memberikan komposisi bobot yang sama,
sehingga tidak terdapat alternatif portofolio optimal lain pada skenario batasan tersebut.
Pola yang sama juga terjadi pada skenario batasan 5%. Meskipun ruang alokasi bobot
diperlebar dari portofolio aktual, hasil optimasi tetap tidak membentuk kurva efficient
frontier dengan banyak pilihan portofolio optimal. Dengan demikian, pada kedua skenario
batasan tersebut, pilihan portofolio optimal yang dihasilkan oleh model MVO hanya satu
karena perubahan nilai Rmax tidak menghasilkan variasi komposisi bobot portofolio yang
berbeda.
Berdasarkan Tabel 4.22, skenario batasan Kementerian Keuangan mempunyai
kinerja yang lebih unggul dibandingkan skenario batasan 5% karena menghasilkan
ekspektasi persentase perubahan biaya pembayaran utang valas dan standar deviasi
yang lebih rendah. Ekspektasi persentase perubahan biaya pembayaran utang valas
pada batasan Kementerian Keuangan lebih kecil sebesar 15,0476% dibandingkan
skenario batasan 5%, sedangkan risiko portofolio utang valas berdasarkan standar
deviasi juga lebih kecil sebesar 9,9636%. Hal ini menunjukkan bahwa pelebaran
batasan bobot tidak selalu menghasilkan portofolio yang lebih optimal, karena pada
kasus ini batasan 5% justru memberikan nilai ekspektasi persentase perubahan biaya
dan risiko yang lebih tinggi. Dengan demikian, skenario batasan Kementerian
```
Keuangan dipilih sebagai hasil optimasi Mean-Variance Optimization (MVO) yang
```
selanjutnya dibandingkan dengan kinerja portofolio aktual pada Tabel 4.21. Jika
81
```
dibandingkan dengan portofolio aktual x(0), portofolio optimal dengan batasan
```
Kementerian Keuangan mengalami peningkatan bobot pada instrumen x1, x2, dan x3,
masing-masing sebesar 0,025514165, 0,011379146, dan 0,017201237, sedangkan bobot x4,
x5, x6, dan x7 mengalami penurunan masing-masing sebesar 0,013927407, 0,009401992,
0,016688212, dan 0,014076937. Dari sisi ekspektasi persentase perubahan biaya
pembayaran utang valas, portofolio optimal menghasilkan nilai 0,000455644978376515,
sedangkan portofolio aktual menghasilkan nilai 0,000562311480873920, sehingga hasil
optimasi MVO mampu menurunkan ekspektasi persentase perubahan biaya sebesar
0,000106666502497405 atau sekitar 18,9693%. Dari sisi risiko, standar deviasi
portofolio optimal adalah 0,005045420400454560, sedangkan standar deviasi portofolio
aktual adalah 0,005803752645958170, sehingga risiko portofolio dapat ditekan hingga
0,000758332245503610, atau sekitar 13,0662%.
```
4.6.4 Hasil Optimasi Menggunakan Conditional Value at Risk (CVaR)
```
```
Penyelesaian model Conditional Value at Risk (CVaR) dilakukan menggunakan
```
bantuan MATLAB berdasarkan parameter input yang diperoleh dari gabungan data
historis dan hasil peramalan. Model CVaR diselesaikan pada tiga skenario batasan bobot,
yaitu batasan Kementerian Keuangan yang berdasarkan pada persamaan 4.11, batasan
```
5% dari portofolio aktual x(0) yang berdasarkan pada persamaan 4.12, dan tanpa batasan
```
khusus yang berdasarkan pada persamaan 4.13. Ketiga skenario batasan tersebut masing-
masing diselesaikan dengan delapan batasan risiko maksimum sebagaimana dinyatakan
pada persamaan 4.19 dan tiga tingkat kepercayaan, yaitu β = 90%, β = 95%, dan
β = 99%. Kode program penyelesaian model CVaR dapat dilihat pada Lampiran 12. Hasil
optimasi CVaR dengan batasan Kementerian Keuangan disajikan pada tabel berikut:
Tabel 4.23 Portofolio Hasil Optimasi CVaR dengan Batasan Kementerian Keuangan
β = 90%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM 0,485000000184049000 0,485000000016516000 0,485004232161584000 0,485000007364392000 0,485000000619660000 0,485000000007600000x2 TM TM 0,124999999173210000 0,124999999556000000 0,124998212740908000 0,124999993662871000 0,124999999658185000 0,124999999951300000
x3 TM TM 0,164999998938490000 0,164999999812140000 0,164997525576130000 0,164999989337110000 0,164999997167370000 0,164999999964290000x4 TM TM 0,130000000034050000 0,130000000026360000 0,130000002751053000 0,130000000031009000 0,130000000022340000 0,130000000003190000
x5 TM TM 0,015000000001250000 0,015000000039449000 0,015000001451055000 0,015000000078149000 0,015000000016745000 0,015000000035090000x6 TM TM 0,050000000057240000 0,050000000005200000 0,050000005559895000 0,050000000004990000 0,050000000018970000 0,050000000009310000
x7 TM TM 0,030000000066980000 0,030000000007920000 0,030000000079964000 0,030000000024150000 0,030000000013359000 0,030000000008230000μT x TM TM 0,000461340189101602 0,000461340189085346 0,000461340625253796 0,000461340189583833 0,000461340189139132 0,000461340189079226
CVaR90% TM TM 0,011273912563843000 0,012652736990327900 0,016840386912994800 0,018695570545171400 0,022168137297936800 0,028572213794284700VaR
90% TM TM 0,007259433971461060 0,007214407812901410 0,007192344077889990 0,006863732719841170 0,006873904985267150 0,007268160636157800β = 95%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM TM 0,485000005658388000 0,485000044015608000 0,485000003402470000 0,485000029225110000 0,485000000190100000x2 TM TM TM 0,124999995218662000 0,124999950354560000 0,124999996565920000 0,124999975683490000 0,124999999820750000
x3 TM TM TM 0,164999990718990000 0,164999914532728000 0,164999999971080000 0,164999989408860000 0,164999999971490000x4 TM TM TM 0,130000000014853000 0,130000017233980000 0,130000000026190000 0,130000000253310000 0,130000000011960000
x5 TM TM TM 0,015000000292351000 0,015000019203401000 0,015000000023859000 0,015000000216923000 0,015000000004221000x6 TM TM TM 0,050000000049694000 0,050000005583720000 0,050000000005400000 0,050000000052137000 0,050000000000761000
x7 TM TM TM 0,030000000020647000 0,030000004472701000 0,030000000005337000 0,030000000047496000 0,030000000000724000μT x TM TM TM 0,000461340189503507 0,000461340254121313 0,000461340189102915 0,000461340189960493 0,000461340189080485
CVaR95% TM TM TM 0,012687056960659100 0,016878134130096900 0,018729212061770300 0,022208434632837800 0,028609031290012600VaR
95% TM TM TM 0,009460541190811080 0,009662792718237370 0,009747096083991480 0,009965181486494270 0,010054785253876600β = 99%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM TM TM 0,485000011985727000 0,485000000214220000 0,485000000152095000 0,485000017317847000x2 TM TM TM TM 0,124999943957183000 0,124999999855810000 0,124999986963200000 0,124999980794598000
x3 TM TM TM TM 0,164999934127378000 0,164999999871040000 0,164999999297530000 0,164999999921600000x4 TM TM TM TM 0,130000006801080000 0,130000000022580000 0,130000000184030000 0,130000000723094000
x5 TM TM TM TM 0,015000001087861000 0,015000000024933000 0,015000000211179000 0,015000000802254000x6 TM TM TM TM 0,050000001310704000 0,050000000005879000 0,050000000046045000 0,050000000190781000
x7 TM TM TM TM 0,030000000115624000 0,030000000005718000 0,030000000045218000 0,030000000184158000μT x TM TM TM TM 0,000461340202455377 0,000461340189086583 0,000461340189147142 0,000461340192240339
CVaR99% TM TM TM TM 0,016970090187221800 0,018844463138819800 0,022353979260792800 0,028828317055396100VaR
99% TM TM TM TM 0,011731518521580400 0,011775033369385200 0,013698710283200200 0,014825816384670600
Pada Tabel 4.23, keterangan TM menunjukkan bahwa model tidak menghasilkan
solusi yang memenuhi seluruh kendala pada nilai Rmax tertentu, sedangkan μT x
82
menunjukkan ekspektasi persentase perubahan biaya pembayaran utang valas dari
portofolio yang diperoleh. Nilai Rmax pada tabel disusun dari kiri ke kanan mulai
dari nilai terkecil hingga nilai terbesar, sehingga semakin ke kanan nilai batas
risiko yang digunakan semakin besar. Untuk nilai Rmax yang sama, kenaikan
tingkat kepercayaan β tidak memberikan perubahan yang berarti terhadap nilai
ekspektasi persentase perubahan biaya pembayaran utang valas karena nilai μT x
yang diperoleh relatif sama. Namun, nilai CVaR cenderung meningkat ketika β
semakin besar. Hal ini terjadi karena semakin tinggi tingkat kepercayaan yang
digunakan, semakin ekstrem risiko yang diperhitungkan dalam model CVaR. Dari seluruh
portofolio hasil optimasi CVaR dengan batasan Kementerian Keuangan, portofolio
yang menghasilkan ekspektasi persentase perubahan biaya pembayaran utang valas
```
paling rendah adalah portofolio CVaR(90%)1 , yaitu portofolio pada β = 90% dengan
```
```
Rmax = 0,028964586540561300. Portofolio CVaR(90%)1 menghasilkan ekspektasi persentase
```
perubahan biaya pembayaran utang valas sebesar 0,000461340189079226 dan nilai
CVaR90% = 0,028572213794284700. Jika dibandingkan dengan portofolio aktual
```
pada Tabel 4.21, portofolio CVaR(90%)1 mampu menurunkan ekspektasi persentase
```
perubahan biaya pembayaran utang valas sekitar 17,956463999480356%. Namun, nilai
risikonya berdasarkan CVaR90% tidak mengalami penurunan, melainkan meningkat
sekitar 152,739354474776100% dibandingkan portofolio aktual. Sementara itu, portofolio
```
yang menghasilkan nilai CVaR paling rendah adalah portofolio CVaR(90%)2 , yaitu
```
portofolio pada β = 90% dengan Rmax = 0,011305009399949200. Portofolio
```
CVaR(90%)2 menghasilkan nilai CVaR90% = 0,011273912563843000 dan ekspektasi
```
persentase perubahan biaya pembayaran utang valas sebesar 0,000461340189101602.
```
Jika dibandingkan dengan portofolio aktual pada Tabel 4.21, portofolio CVaR(90%)2
```
mampu menurunkan ekspektasi persentase perubahan biaya pembayaran utang valas
sekitar 17,956463995501199% dan menurunkan risiko berdasarkan CVaR90% sekitar
0,275071279899308%. Kedua portofolio tersebut tetap dipertimbangkan sebagai hasil
```
optimasi CVaR dengan batasan Kementerian Keuangan karena portofolio CVaR(90%)1
```
memberikan ekspektasi persentase perubahan biaya paling rendah, sedangkan portofolio
```
CVaR(90%)2 memberikan nilai CVaR paling rendah. Selanjutnya, hasil optimasi CVaR
```
```
dengan batasan bobot yang diperlebar 5% dari portofolio aktual x(0) disajikan pada
```
halaman berikutnya.
83
Tabel 4.24 Portofolio Hasil Optimasi CVaR dengan Batasan Diperlebar 5%
β = 90%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM 0,460369587708713000 0,460369581484435000 0,460369608765471000 0,460369601002636000 0,460369581680477000 0,460370160673920000x2 TM TM 0,119301891240900000 0,119301896676161000 0,119301876157329000 0,119301881574038000 0,119301896563873000 0,119301675181629000
x3 TM TM 0,155188700335302000 0,155188701133605000 0,155188676417500000 0,155188696395410000 0,155188701135988000 0,155188330080295000x4 TM TM 0,136731036742709000 0,136731036736895000 0,136731047994353000 0,136731037016572000 0,136731036666414000 0,136731037798935000
x5 TM TM 0,023181892421190600 0,023181892415272300 0,023181894131000200 0,023181892444755000 0,023181892402285700 0,023181895166742500x6 TM TM 0,063353801400608800 0,063353801401869900 0,063353801720840500 0,063353801404592900 0,063353801400466800 0,063353806661356700
x7 TM TM 0,041873090150576800 0,041873090151765700 0,041873090467026600 0,041873090157383400 0,041873090150480100 0,041873094788309900μT x TM TM 0,000541709746812927 0,000541709746417366 0,000541709761693500 0,000541709748104365 0,000541709746352506 0,000541709835049115
CVaR90% TM TM 0,011297498413000800 0,012677370320379100 0,016874535069058700 0,018717402655246400 0,022171863518571900 0,028602029005207200VaR
90% TM TM 0,008061623025570330 0,007996739736435110 0,007610589982075480 0,007446693660429770 0,007321601661479710 0,007833137747799300β = 95%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM TM 0,46036959122577000 0,460369585261284000 0,460369583358316000 0,460369585858900000 0,460369583188548000x2 TM TM TM 0,119301892807145000 0,119301888717638000 0,119301896537276000 0,119301892474472000 0,119301895812252000
x3 TM TM TM 0,155188699150772000 0,155188700968898000 0,155188698853623000 0,155188701059217000 0,155188700382539000x4 TM TM TM 0,136731036884662000 0,136731036933569000 0,136731037238362000 0,136731036652982000 0,136731036656388000
x5 TM TM TM 0,023181892474985500 0,023181892461769200 0,023181892455450400 0,023181892403626900 0,023181892407157400x6 TM TM TM 0,063353801399728000 0,063353801408800000 0,063353801403513200 0,063353801400566300 0,063353801401580300
x7 TM TM TM 0,041873090149660100 0,041873090158591800 0,041873090153473300 0,041873090150551900 0,041873090151539700μT x TM TM TM 0,000541709747241937 0,000541709746866880 0,000541709747139255 0,000541709746572661 0,000541709746490747
CVaR95% TM TM TM 0,012707812284584800 0,016908231906519800 0,018749278493058500 0,022218755501344100 0,028630544025590900VaR
95% TM TM TM 0,010421080439502000 0,010217875025790900 0,010312101278444300 0,010490326520581000 0,010699748816806200β = 99%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM TM TM 0,460369581550130000 0,460371752234393000 0,460370043752785000 0,460369581734659000x2 TM TM TM TM 0,11929996998810000 0,119299732726883000 0,119301435921293000 0,119301896627243000
x3 TM TM TM TM 0,155188701149989000 0,155188685486430000 0,155188696981365000 0,155188701008650000x4 TM TM TM TM 0,136731036650000000 0,136731037534119000 0,136731037366695000 0,136731036669540000
x5 TM TM TM TM 0,023181892400000100 0,023181896774726000 0,023181893848711700 0,023181892405621500x6 TM TM TM TM 0,063353801400000100 0,063353802074937600 0,063353801607456400 0,063353801402257200
x7 TM TM TM TM 0,041873090150000100 0,041873090827322100 0,041873090354681500 0,041873090152001500μT x TM TM TM TM 0,000541709746326647 0,000541709873556314 0,000541709774375071 0,000541709746379055
CVaR99% TM TM TM TM 0,016985634805170200 0,018859338375476100 0,022368428987645300 0,028845286675492600VaR
99% TM TM TM TM 0,013633111828331500 0,013699736813424200 0,013832790278176000 0,014130979523224300
Pada Tabel 4.24, nilai Rmax pada tabel disusun dari kiri ke kanan mulai dari nilai
terkecil hingga nilai terbesar, sehingga semakin ke kanan nilai batas risiko yang digunakan
semakin besar. Untuk nilai Rmax yang sama, kenaikan tingkat kepercayaan β tidak
memberikan perubahan yang berarti terhadap nilai ekspektasi persentase perubahan
biaya pembayaran utang valas karena nilai μT x yang diperoleh relatif sama. Namun,
nilai CVaR cenderung meningkat ketika β semakin besar karena semakin tinggi tingkat
kepercayaan yang digunakan, semakin ekstrem risiko yang diperhitungkan dalam model
CVaR. Dari seluruh portofolio hasil optimasi CVaR dengan batasan diperlebar 5%,
portofolio yang menghasilkan ekspektasi persentase perubahan biaya pembayaran utang
```
valas paling rendah adalah portofolio CVaR(99%)3 , yaitu portofolio pada β = 99%
```
```
dengan Rmax = 0,016989970809430900. Portofolio CVaR(99%)3 menghasilkan ekspektasi
```
persentase perubahan biaya pembayaran utang valas sebesar 0,000541709746326647
dan nilai CVaR99% = 0,016985634805170200. Jika dibandingkan dengan portofolio
```
aktual pada Tabel 4.21, portofolio CVaR(99%)3 mampu menurunkan ekspektasi persentase
```
perubahan biaya pembayaran utang valas sekitar 3,663758364746682% dan menurunkan
risiko berdasarkan CVaR99% sekitar 0,025520977265910%. Sementara itu, portofolio
```
yang menghasilkan nilai CVaR paling rendah adalah portofolio CVaR(90%)4 , yaitu
```
portofolio pada β = 90% dengan Rmax = 0,011305009399949200. Portofolio
```
CVaR(90%)4 menghasilkan nilai CVaR90% = 0,011297498413000800 dan ekspektasi
```
persentase perubahan biaya pembayaran utang valas sebesar 0,000541709746812927.
```
Jika dibandingkan dengan portofolio aktual pada Tabel 4.21, portofolio CVaR(90%)4
```
mampu menurunkan ekspektasi persentase perubahan biaya pembayaran utang valas
sekitar 3,663758278253133% dan menurunkan risiko berdasarkan CVaR90% sekitar
0,066439417865243%. Kedua portofolio tersebut tetap dipertimbangkan sebagai hasil
```
optimasi CVaR dengan batasan diperlebar 5% karena portofolio CVaR(99%)3 memberikan
```
```
ekspektasi persentase perubahan biaya paling rendah, sedangkan portofolio CVaR(90%)4
```
84
memberikan nilai CVaR paling rendah. Selanjutnya, hasil optimasi CVaR tanpa batasan
bobot khusus disajikan pada tabel berikut:
Tabel 4.25 Portofolio Hasil Optimasi CVaR Tanpa Batasan
β = 90%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM 0,000000081580099452 0,00000000020955014 0,000000147100174393 0,000000354004431065 0,000000001962683790 0,000000000908540417x2 TM TM 0,000000018486467894 0,000000011853513181 0,000002496297673288 0,000010050527566631 0,000000000190055494 0,000000000095063388
x3 TM TM 0,999999719798691000 0,999999988003156000 0,999996879972891000 0,999989363496386000 0,999999980318100000 0,999999980983620000x4 TM TM 0,000000000748560141 0,000000000011165897 0,000000068072818926 0,000000049898754020 0,000000003121964740 0,000000000186935910
x5 TM TM 0,000000000587285163 0,000000000012426391 0,000000076989480641 0,000000003241388464 0,000000000407704372 0,000000000232662940x6 TM TM 0,000000006388466640 0,000000000207603030 0,000000168599862818 0,000000113274336529 0,000000001743732420 0,000000000165547000
x7 TM TM 0,000000006549974838 0,000000000541242840 0,000000173262223553 0,000000115792832799 0,000000001725704080 0,000000000162452700μT x TM TM 0,000035896235070086 0,000035896174502558 0,000035897467072764 0,000035897618413202 0,000035896175162201 0,000035896173529795
CVaR90% TM TM 0,011291391268516000 0,012502641291961800 0,016675842081435900 0,018556916546025300 0,022010076743541300 0,028477396926768800VaR
90% TM TM 0,004607366060002320 0,005646343175811770 0,006213080545011720 0,006753207755766210 0,006951522677982650 0,009315449967785080β = 95%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM 0,000000066831862180 0,000000019592039543 0,000000000037459261 0,000000000143309590 0,000000000285897271 0,000000000652284598x2 TM TM 0,000000458725585160 0,000000012659452126 0,000000000058734851 0,000000000077870757 0,000000009537769561 0,000000001387817845
x3 TM TM 0,999998886386000000 0,999999941866766000 0,999999999856860000 0,999999999761304000 0,999999987537751000 0,999999997959820000x4 TM TM 0,000000010312075850 0,000000002484984495 0,000000000005037937 0,000000000006924365 0,000000000271305690 0,000000000000507501
x5 TM TM 0,000000011060919940 0,000000002811473210 0,000000000005192030 0,000000000007480986 0,000000000288186850 0,000000000004302670x6 TM TM 0,000000003049512750 0,000000006051035860 0,000000000022957050 0,000000000022817110 0,000000000071856860 0,000000000001755450
x7 TM TM 0,000000002991765970 0,000000006087001355 0,000000000022295500 0,000000000022551170 0,000000000073133610 0,000000000001817450μT x TM TM 0,000035896188813220 0,000035896602150931 0,000035896173328415 0,000035896173346884 0,000035896174461018 0,000035896173485866
CVaR95% TM TM 0,011272461635048200 0,012636129226005200 0,016746341409820700 0,018600485800242700 0,022076185304458900 0,028488733353169300VaR
95% TM TM 0,008333641244719690 0,007995103523879760 0,008262063437005550 0,008443826257580740 0,008751481764493830 0,009136245143530130β = 99%
Rmax 0,000033683544775466 0,000101609932479855 0,011305009399949200 0,012714094856730800 0,016989970809430900 0,018880495149667600 0,022423957171019300 0,028964586540561300x
1 TM TM 0,000000000045788600 0,000000000019802037 0,000000000036488276 0,000000000036724921 0,000000000029360521 0,000000000011521703x2 TM TM 0,000000000036503068 0,000000000014164689 0,000000000011423947 0,000000000011496333 0,000000000024930947 0,000000000005104787
x3 TM TM 0,999999999917427000 0,999999999928483000 0,999999999920133000 0,999999999920183000 0,999999999920268000 0,999999999920208000x4 TM TM 0,000000000003346401 0,000000000010205329 0,000000000004855453 0,000000000001830976 0,000000000013841526 0,000000000000790508
x5 TM TM 0,000000000003247212 0,000000000010029411 0,000000000004989823 0,000000000001588649 0,000000000012469108 0,000000000000856829x6 TM TM 0,000000000003164397 0,000000000009003153 0,000000000003521542 0,000000000001130983 0,000000000001619798 0,000000000000155027
x7 TM TM 0,000000000003152464 0,000000000008960392 0,000000000003235386 0,000000000001105759 0,000000000001609061 0,000000000000149015μT x TM TM 0,000035896173348747 0,000035896173369249 0,000035896180670965 0,000035896173396490 0,000035896278566194 0,000035896176112303
CVaR99% TM TM 0,011265260203986000 0,012673659465899600 0,016928657515091400 0,018802157477780600 0,022324736456026600 0,028832679457605700VaR
99% TM TM 0,008428328058222500 0,008860205054952370 0,010246800269330300 0,011012211454443600 0,012502603946788800 0,015383548691613900
Pada Tabel 4.25, nilai Rmax pada tabel disusun dari kiri ke kanan mulai dari
nilai terkecil hingga nilai terbesar, sehingga semakin ke kanan nilai batas risiko
yang digunakan semakin besar. Untuk nilai Rmax yang sama, kenaikan tingkat
kepercayaan β tidak memberikan perubahan yang berarti terhadap nilai ekspektasi
persentase perubahan biaya pembayaran utang valas karena nilai μT x yang diperoleh
relatif sama. Namun, nilai CVaR cenderung meningkat ketika β semakin besar
karena semakin tinggi tingkat kepercayaan yang digunakan, semakin ekstrem risiko
yang diperhitungkan dalam model CVaR. Dari seluruh portofolio hasil optimasi CVaR
tanpa batasan, portofolio yang menghasilkan ekspektasi persentase perubahan biaya
pembayaran utang valas paling rendah adalah portofolio pada β = 95% dengan
```
Rmax = 0,016989970809430900. Portofolio tersebut menghasilkan ekspektasi persentase
```
perubahan biaya pembayaran utang valas sebesar 0,000035896173328415 dan nilai
CVaR95% = 0,016746341409820700. Jika dibandingkan dengan portofolio aktual
pada Tabel 4.21, portofolio ini menurunkan ekspektasi persentase perubahan biaya
pembayaran utang valas sebesar 93,616318465660889% terhadap portofolio aktual,
tetapi meningkatkan risiko berdasarkan CVaR95% sebesar 31,714774640161477% terhadap
portofolio aktual. Sementara itu, portofolio yang menghasilkan nilai CVaR paling
rendah adalah portofolio pada β = 99% dengan Rmax = 0,011305009399949200.
Portofolio tersebut menghasilkan nilai CVaR99% = 0,011265260203986000 dan ekspektasi
persentase perubahan biaya pembayaran utang valas sebesar 0,000035896173348747.
Jika dibandingkan dengan portofolio aktual pada Tabel 4.21, portofolio ini
menurunkan ekspektasi persentase perubahan biaya pembayaran utang valas sebesar
93,616318462044320% terhadap portofolio aktual dan menurunkan risiko berdasarkan
85
CVaR99% sebesar 33,694655452178280% terhadap portofolio aktual. Meskipun portofolio-
portofolio tersebut memberikan penurunan ekspektasi dan/atau risiko yang signifikan,
tidak ada portofolio yang dipilih dari skenario tanpa batasan karena hampir seluruh
bobot portofolio cenderung terpusat pada x3, bahkan mendekati satu. Kondisi tersebut
tidak mungkin diterapkan secara langsung dalam pembayaran utang valas Pemerintah
Indonesia karena porsi pembayaran untuk instrumen lainnya menjadi sangat kecil,
sehingga tidak mencukupi kebutuhan minimal pembayaran utang pada instrumen selain
x3. Selanjutnya, berdasarkan Tabel 4.23 dan Tabel 4.24, diperoleh empat portofolio
hasil optimasi CVaR yang terdiri atas dua portofolio dari skenario batasan Kementerian
Keuangan dan dua portofolio dari skenario batasan yang diperlebar 5%. Keempat
portofolio tersebut dipilih berdasarkan dua kriteria, yaitu portofolio dengan ekspektasi
persentase perubahan biaya pembayaran utang valas paling rendah dan portofolio dengan
risiko CVaR paling rendah pada masing-masing skenario batasan. Kinerja keempat
portofolio tersebut kemudian dihitung berdasarkan persentase penurunan ekspektasi
persentase perubahan biaya pembayaran utang valas dan persentase penurunan risiko
terhadap portofolio aktual Pemerintah Indonesia pada Tabel 4.21. Perbandingan keempat
portofolio hasil optimasi CVaR tersebut disajikan pada tabel berikut:
Tabel 4.26 Perbandingan Kinerja Portofolio Terbaik Hasil Optimasi CVaR
Variabel/Ukuran Batasan Kementerian Keuangan Batasan Diperlebar 5%
```
CVaR(90%)1 CVaR(90%)2 CVaR(99%)3 CVaR(90%)4
```
β 90% 90% 99% 90%
Rmax 0,028964586540561300 0,011305009399949200 0,016989970809430900 0,011305009399949200
x1 0,485000000007600000 0,485000000184049000 0,460369581550130000 0,460369587708713000
x2 0,124999999951300000 0,124999999173210000 0,119299969988100000 0,119301891240900000
x3 0,164999999964290000 0,164999998938490000 0,155188701149989000 0,155188700335302000
x4 0,130000000003190000 0,130000000034050000 0,136731036650000000 0,136731036742709000
x5 0,015000000035090000 0,015000000001250000 0,023181892400000100 0,023181892421190600
x6 0,050000000009310000 0,050000000057240000 0,063353801400000100 0,063353801400608800
x7 0,030000000008230000 0,030000000066980000 0,041873090150000100 0,041873090150576800
Ekspektasi Persentase Perubahan
Biaya Pembayaran Utang Valas 0,000461340189079226 0,000461340189101602 0,000541709746326647 0,000541709746812927
Persentase Penurunan Ekspektasi
terhadap Portofolio Aktual 17,956463999480356% 17,956463995501199% 3,663758364746682% 3,663758278253133%
Risiko 0,028572213794284700 0,011273912563843000 0,016985634805170200 0,011297498413000800
Persentase Penurunan Risiko
terhadap Portofolio Aktual −152,739354474776100% 0,275071279899308% 0,025520977265910% 0,066439417865243%
Berdasarkan Tabel 4.26, dari keempat portofolio hasil optimasi CVaR, portofolio
yang menghasilkan ekspektasi persentase perubahan biaya pembayaran utang valas paling
```
rendah adalah portofolio CVaR(90%)1 , yaitu sebesar 0,000461340189079226. Portofolio
```
tersebut mampu menurunkan ekspektasi persentase perubahan biaya pembayaran
utang valas sebesar 17,956463999480356% dibandingkan portofolio aktual. Namun,
```
dari sisi risiko, portofolio CVaR(90%)1 tidak menghasilkan penurunan risiko, tetapi
```
justru meningkatkan risiko sebesar 152,739354474776100%. Sementara itu, portofolio
```
yang menghasilkan risiko paling rendah adalah portofolio CVaR(90%)2 , yaitu sebesar
```
0,011273912563843000. Portofolio tersebut mampu menurunkan ekspektasi persentase
perubahan biaya pembayaran utang valas sebesar 17,956463995501199% dan menurunkan
risiko sebesar 0,275071279899308% dibandingkan portofolio aktual. Dengan demikian,
```
portofolio utama yang dipilih sebagai hasil optimasi CVaR adalah CVaR(90%)2 , karena
```
86
mampu menurunkan ekspektasi persentase perubahan biaya pembayaran utang valas
```
dengan nilai yang hampir sama dengan CVaR(90%)1 , sekaligus menghasilkan risiko CVaR
```
```
paling rendah. Selain itu, portofolio CVaR(90%)1 dapat dipertimbangkan sebagai portofolio
```
alternatif karena menghasilkan ekspektasi persentase perubahan biaya pembayaran
utang valas paling rendah, meskipun risikonya lebih tinggi dibandingkan portofolio
aktual. Selanjutnya, kurva efficient frontier dari model optimasi CVaR dengan batasan
Kementerian Keuangan dan β = 90% disajikan pada gambar berikut:
Gambar 4.13 Efficient Frontier Model CVaR dengan Batasan Kementerian Keuangan
dan β = 90%
Berdasarkan Gambar 4.13, garis biru merepresentasikan kumpulan portofolio efisien
yang diperoleh dari model optimasi CVaR dengan batasan Kementerian Keuangan dan
β = 90%. Setiap titik pada garis tersebut menunjukkan portofolio optimal untuk tingkat
risiko CVaR tertentu. Titik merah menunjukkan portofolio dengan batas bawah risiko,
yaitu portofolio yang menghasilkan nilai risiko paling rendah pada kurva tersebut. Kurva
tersebut menunjukkan bahwa masih terdapat beberapa pilihan portofolio optimal lainnya
selain portofolio pada batas bawah risiko. Pilihan tersebut berada di sepanjang garis
biru, yaitu portofolio dengan risiko CVaR yang lebih besar, tetapi dengan nilai ekspektasi
persentase perubahan biaya pembayaran utang valas yang hampir sama. Hal ini terlihat
dari bentuk kurva yang cenderung mendatar, sehingga perubahan nilai risiko tidak diikuti
oleh perubahan nilai ekspektasi persentase perubahan biaya pembayaran utang valas yang
besar. Apabila tujuan utama adalah menekan risiko ekstrem, maka portofolio pada titik
merah lebih sesuai untuk dipilih. Namun, apabila pengambil keputusan masih dapat
menerima risiko CVaR yang lebih tinggi, maka portofolio lain pada garis biru tetap dapat
dipertimbangkan sebagai alternatif karena masih berada pada himpunan portofolio efisien.
Untuk skenario batasan yang diperlebar 5% dan tanpa batasan, kurva efficient frontier
dapat dilihat pada Lampiran 25.
4.7 Analisis Hasil dan Pembahasan
Analisis hasil dan pembahasan dilakukan untuk mengevaluasi kinerja portofolio
aktual Pemerintah Indonesia, hasil optimasi model MVO, dan hasil optimasi model
87
CVaR. Hasil optimasi model MVO yang dianalisis mengacu pada Tabel 4.22, yaitu model
MVO dengan batasan Kementerian Keuangan pada Rmax = 0,011305009399949200.
Sementara itu, hasil optimasi model CVaR yang dianalisis mengacu pada Tabel 4.26, yaitu
```
CVaR(90%)2 sebagai portofolio utama dan CVaR(90%)1 sebagai portofolio alternatif. Analisis
```
dilakukan dengan membandingkan komposisi bobot, ekspektasi persentase perubahan
biaya pembayaran utang valas, serta risiko terhadap portofolio aktual pada Tabel 4.21.
Risiko pada model MVO diukur menggunakan standar deviasi, sedangkan risiko pada
model CVaR diukur menggunakan CVaR90%. Hasil perbandingan portofolio aktual, model
MVO, dan model CVaR disajikan pada tabel berikut:
Tabel 4.27 Perbandingan Portofolio Aktual, Model MVO, dan Model CVaR
```
Variabel Portofolio Aktual Model MVO Model CVaR(90%)1 Model CVaR(90%)2
```
Rmax - 0,011305009399949200 0,028964586540561300 0,011305009399949200
x1 0,459485835 0,4850 0,485000000007600000 0,485000000184049000
x2 0,113620854 0,1250 0,124999999951300000 0,124999999173210000
x3 0,147798763 0,1650 0,164999999964290000 0,164999998938490000
x4 0,143927407 0,1300 0,130000000003190000 0,130000000034050000
x5 0,024401992 0,0150 0,015000000035090000 0,015000000001250000
x6 0,066688212 0,0500 0,050000000009310000 0,050000000057240000
x7 0,044076937 0,0300 0,030000000008230000 0,030000000066980000
Ekspektasi Persentase Perubahan
Biaya Pembayaran Utang Valas 0,000562311480873920 0,000455644978376515 0,000461340189079226 0,000461340189101602
Persentase Penurunan Ekspektasi
terhadap Portofolio Aktual - 18,969292817290196% 17,956463999480356% 17,956463995501199%
```
Risiko (Standar Deviasi) 0,005803752645958170 0,005045420400454560 - -
```
```
Risiko (CVaR90%) 0,011305009399949160 - 0,028572213794284700 0,011273912563843000
```
Persentase Penurunan Risiko
terhadap Portofolio Aktual - 13,066236967732298% −152,739354474776100% 0,275071279899308%
Berdasarkan Tabel 4.27, analisis kinerja model dibagi menjadi dua bagian utama,
yaitu analisis ekspektasi persentase perubahan biaya pembayaran utang valas dan
analisis risiko. Dari sisi ekspektasi, portofolio aktual dibandingkan dengan model MVO,
```
CVaR(90%)2 , dan CVaR(90%)1 . Model MVO digunakan untuk memperoleh portofolio dengan
```
ekspektasi persentase perubahan biaya pembayaran utang valas yang minimum dengan
```
risiko yang diukur menggunakan standar deviasi, sedangkan CVaR(90%)2 dan CVaR(90%)1
```
digunakan untuk memperoleh portofolio optimal berdasarkan pendekatan risiko CVaR.
Dari sisi risiko, ukuran risiko pada model MVO dijelaskan melalui standar deviasi,
sedangkan ukuran risiko pada model CVaR dijelaskan melalui CVaR90%. Standar deviasi
pada model MVO menggambarkan besar penyimpangan persentase perubahan biaya
pembayaran utang valas portofolio terhadap nilai ekspektasinya, sehingga persentase
perubahan biaya tersebut tidak selalu tepat pada nilai ekspektasinya, tetapi dapat
berfluktuasi di sekitar nilai tersebut. Kelemahan model MVO dari sisi risiko terletak pada
penggunaan standar deviasi yang hanya menggambarkan penyimpangan secara umum dan
belum secara khusus menekankan risiko ekstrem. Model CVaR lebih direkomendasikan
untuk digunakan karena dapat menangkap risiko kenaikan biaya pembayaran utang valas
pada kondisi buruk, yaitu ketika persentase kenaikan biaya pembayaran utang valas
```
portofolio berada pada kelompok nilai terbesar. Model CVaR(90%)2 menjadi portofolio
```
CVaR utama karena menghasilkan risiko CVaR yang rendah dan masih mampu menjaga
ekspektasi persentase perubahan biaya pembayaran utang valas pada nilai yang tidak
terlalu berbeda jauh dibandingkan model MVO. Selanjutnya, perubahan bobot portofolio
88
hasil optimasi terhadap portofolio aktual disajikan pada tabel berikut:
Tabel 4.28 Perubahan Bobot Portofolio terhadap Portofolio Aktual
```
Variabel Model MVO Model CVaR(90%)1 Model CVaR(90%)2
```
x1 +0,025514165000000000 +0,025514165007600000 +0,025514165184048976
x2 +0,011379146000000000 +0,011379145951300000 +0,011379145173210009
x3 +0,017201237000000000 +0,017201236964290000 +0,017201235938489989
x4 −0,013927407000000000 −0,013927406996810000 −0,013927406965950018
x5 −0,009401992000000000 −0,009401991964910000 −0,009401991998750001
x6 −0,016688212000000000 −0,016688211990690000 −0,016688211942759996
x7 −0,014076937000000000 −0,014076936991770000 −0,014076936933019996
Berdasarkan Tabel 4.28, perubahan bobot model MVO terhadap portofolio aktual
menunjukkan bahwa bobot x1, x2, dan x3 mengalami kenaikan, sedangkan bobot x4, x5,
x6, dan x7 mengalami penurunan. Perubahan bobot terbesar pada model MVO terjadi
pada x1, yaitu sebesar 0,025514165000000000, sedangkan perubahan bobot terkecil terjadi
pada x5, yaitu sebesar 0,009401992000000000. Pola perubahan yang sama juga terjadi
```
pada model CVaR(90%)2 . Pada model tersebut, perubahan bobot terbesar terjadi pada
```
x1, yaitu sebesar 0,025514165184048976, sedangkan perubahan bobot terkecil terjadi
pada x5, yaitu sebesar 0,009401991998750001. Hal ini menunjukkan bahwa komposisi
```
bobot model MVO dan CVaR(90%)2 hampir sama, karena keduanya menggunakan batasan
```
Kementerian Keuangan dengan nilai Rmax = 0,011305009399949200. Selanjutnya,
```
pada model CVaR(90%)1 , perubahan bobot terbesar juga terjadi pada x1, yaitu sebesar
```
0,025514165007600000, sedangkan perubahan bobot terkecil terjadi pada x5, yaitu sebesar
0,009401991964910000. Dengan demikian, ketiga model menghasilkan pola perubahan
bobot yang relatif sama, yaitu meningkatkan porsi x1, x2, dan x3, serta menurunkan
porsi x4, x5, x6, dan x7. Perubahan terbesar secara umum terjadi pada x1, sedangkan
perubahan terkecil secara umum terjadi pada x5.
89
BAB V
KESIMPULAN DAN SARAN
5.1 Kesimpulan
Berdasarkan hasil analisis yang telah dilakukan, berikut adalah kesimpulan yang
menjawab tujuan dari penelitian ini.
1. Hasil peramalan tingkat suku bunga dan nilai tukar mata uang asing menunjukkan
tingkat akurasi yang baik berdasarkan nilai MAPE. Nilai MAPE pada hasil
peramalan menunjukkan bahwa model yang digunakan mampu menghasilkan
peramalan yang akurat untuk variabel suku bunga maupun nilai tukar. MAPE
paling besar terdapat pada variabel suku bunga JPY tenor 10 tahun, yaitu sebesar
15,31203%, sedangkan MAPE paling kecil terdapat pada variabel nilai tukar
USD/JPY, yaitu sebesar 2,64315%. Hasil peramalan tingkat suku bunga dan
nilai tukar mata uang masing-masing disajikan pada Tabel 4.18 dan Tabel 4.19.
Model GARCH tidak digunakan karena seluruh residual model ARIMA bersifat
homoskedastis sehingga tidak terdapat indikasi efek ARCH.
2. Model optimasi portofolio utang valas Pemerintah Indonesia menggunakan metode
```
Mean-Variance Optimization (MVO) adalah sebagai berikut.
```
minx μT x
dengan kendala xT Σx ≤ Rmax,
7∑
```
i=1
```
```
xi = 1,
```
0,436511543250 ≤ x1 ≤ 0,482460126750,
0,107939811300 ≤ x2 ≤ 0,119301896700,
0,140408824850 ≤ x3 ≤ 0,155188701150,
0,136731036650 ≤ x4 ≤ 0,151123777350,
0,023181892400 ≤ x5 ≤ 0,025622091600,
0,063353801400 ≤ x6 ≤ 0,070022622600,
0,041873090150 ≤ x7 ≤ 0,046280783850.
Sementara itu, model optimasi portofolio utang valas Pemerintah Indonesia
```
menggunakan metode Conditional Value at Risk (CVaR) adalah sebagai berikut:
```
91
minx,α,ukμT x
dengan kendala α +
1
```
100(1 − β)
```
100∑
```
k=1
```
uk ≤ Rmax,
uk ≥ rTk x − α, k = 1, . . . , 100,
uk ≥ 0, k = 1, . . . , 100,
7∑
```
i=1
```
```
xi = 1,
```
0 ≤ xi ≤ 1, i = 1, 2, . . . , 7.
3. Berikut komposisi bobot portofolio optimal hasil model MVO dan CVaR.
Tabel 5.1 Komposisi Portofolio Optimal Model MVO dan CVaR
```
Variabel Model MVO Model CVaR(90%)2
```
x1 0,4850 0,485000000184049000
x2 0,1250 0,124999999173210000
x3 0,1650 0,164999998938490000
x4 0,1300 0,130000000034050000
x5 0,0150 0,015000000001250000
x6 0,0500 0,050000000057240000
x7 0,0300 0,030000000066980000
Berdasarkan Tabel 5.1, komposisi bobot portofolio optimal model MVO dan
```
CVaR(90%)2 memiliki nilai yang hampir sama. Model MVO menghasilkan ekspektasi
```
persentase perubahan biaya pembayaran utang valas sebesar 0,000455644978376515
dan standar deviasi sebesar 0,005045420400454560. Nilai tersebut menunjukkan
bahwa model MVO mampu menurunkan ekspektasi persentase perubahan biaya
pembayaran utang valas sebesar 18,969292817290196% dan menurunkan risiko
berdasarkan standar deviasi sebesar 13,066236967732298% terhadap portofolio
```
aktual. Sementara itu, portofolio CVaR(90%)2 menghasilkan ekspektasi persentase
```
perubahan biaya pembayaran utang valas sebesar 0,000461340189101602 dan risiko
CVaR90% sebesar 0,011273912563843000. Portofolio tersebut mampu menurunkan
ekspektasi persentase perubahan biaya pembayaran utang valas sebesar
17,956463995501199% dan menurunkan risiko CVaR sebesar 0,275071279899308%
terhadap portofolio aktual. Model MVO lebih unggul dari sisi penurunan ekspektasi
persentase perubahan biaya pembayaran utang valas dan standar deviasi, sedangkan
```
model CVaR(90%)2 lebih sesuai digunakan apabila perhatian utama diarahkan pada
```
pengendalian risiko ekstrem.
5.2 Saran
Berdasarkan hasil yang telah diperoleh, saran untuk penelitian selanjutnya adalah
sebagai berikut:
92
1. Penelitian selanjutnya dapat menggunakan metode peramalan lain yang mampu
memodelkan hubungan antarvariabel, seperti VAR, VAR-GARCH, atau metode
berbasis machine learning. Penggunaan metode tersebut diharapkan dapat
menangkap keterkaitan antara tingkat suku bunga dan nilai tukar mata uang,
sehingga hasil peramalan yang diperoleh dapat menjadi lebih akurat.
2. Penelitian selanjutnya dapat menambahkan faktor ekonomi makro lain yang
berpengaruh terhadap biaya pembayaran utang valas, seperti inflasi, suku bunga
acuan, cadangan devisa, indeks dolar AS, atau indikator risiko global. Penambahan
variabel tersebut diharapkan dapat memberikan gambaran yang lebih menyeluruh
terhadap pergerakan biaya pembayaran utang valas.
3. Penelitian selanjutnya dapat menggunakan skenario batasan portofolio yang lebih
beragam dan disesuaikan dengan kebijakan pengelolaan utang pemerintah. Selain
itu, penelitian berikutnya juga dapat mencoba nilai β lain pada model CVaR
serta menambah skenario batasan agar hasil optimasi dapat dianalisis dari berbagai
kondisi risiko dan kebijakan portofolio.
4. Penelitian selanjutnya dapat menggunakan bentuk fungsi objektif yang berbeda
dan ukuran risiko lain dalam model optimasi portofolio. Sebagai contoh, fungsi
objektif dapat diarahkan pada minimisasi risiko dengan batas ekspektasi tertentu,
sedangkan ukuran risiko lain yang dapat dipertimbangkan meliputi Value at Risk
```
(VaR), Expected Shortfall, atau downside risk. Selain itu, penelitian selanjutnya
```
juga dapat menambahkan kendala terkait batas waktu pembayaran utang agar
model optimasi lebih sesuai dengan karakteristik kewajiban pembayaran utang valas
pemerintah.
5. Penelitian selanjutnya dapat menambahkan lebih banyak instrumen utang dalam
portofolio agar perbedaan efektivitas antara model MVO dan model optimasi
portofolio dengan kendala risiko CVaR terlihat lebih jelas.
93
DAFTAR PUSTAKA
```
Alexander, G. J., & Baptista, A. M. (2004). A comparison of var and cvar constraints
```
```
on portfolio selection with the mean-variance model. Management Science, 50 (9),
```
1261–1273.
```
Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999). Coherent measures of risk.
```
```
Mathematical finance, 9 (3), 203–228.
```
```
Avdjiev, S., Binder, S., & Sousa, R. (2021). External debt composition and domestic credit
```
cycles. Journal of International Money and Finance, 115, 102377.
```
Babu, A. S., & Reddy, S. K. (2015). Exchange rate forecasting using arima, neural network
```
```
and fuzzy neuron. Journal of Stock & Forex Trading, 4 (03).
```
```
Badan Pusat Statistik. (2025). Indonesia’s economic growth in q3-2025 was 5.04
```
```
percent (year-on-year) (Press Release No. 2478). Badan Pusat Statistik. Retrieved
```
November 30, 2025, from https://www.bps.go.id/en/pressrelease/2025/11/05/
2478/indonesia-s-economic-growth-in-q3-2025-was-5-04-percent--y-on-y-.html
```
Bank Indonesia. (2025, November 21). Maintaining stability, strengthening economic
```
```
growth: Bank indonesia policy measures [Monetary Policy Decision and Economic
```
Statement]. Bank Indonesia. Retrieved November 30, 2025, from https://www.bi.
go.id/en/publikasi/ruang-media/news-release/Pages/sp 2727425.aspx
```
Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal
```
```
of econometrics, 31 (3), 307–327.
```
```
Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis:
```
Forecasting and control. John Wiley & Sons.
```
CNBC Indonesia. (2025). Utang RI tembus Rp9.138 T, Masih Aman? Retrieved November
```
16, 2025, from https://www.cnbcindonesia.com/news/20251020073417-4-677312/
utang-ri-tembus-rp9138-t-masih-aman
```
Cornu´ejols, G., Pe˜na, J., & T¨ut¨unc¨u, R. (2018). Optimization methods in finance (2nd)
```
[Comprehensive treatment of Markowitz portfolio optimization and quadratic
programming]. Cambridge University Press.
```
Cryer, J. D., & Chan, K.-S. (2008). Time series analysis: With applications in r. Springer.
```
```
Dani, A. T. R., dkk. (2025). Navigating samarinda’s climate: A comparative analysis of
```
rainfall forecasting models. MethodsX, 14, 103080.
```
Direktorat Jenderal Pengelolaan Pembiayaan dan Risiko. (2025a). Mitigasi risiko
```
```
pembiayaan pemerintah: Upaya mencapai kesinambungan fiskal (tech. rep.).
```
Kementerian Keuangan Republik Indonesia. Retrieved November 16, 2025, from
```
https://djpb.kemenkeu.go.id
```
```
Direktorat Jenderal Pengelolaan Pembiayaan dan Risiko. (2025b). Optimalisasi komposisi
```
```
utang valuta asing dengan model marginal conditional cost at risk (mccar) (Kajian)
```
```
(Kajian Strategis Pengelolaan Utang). Kementerian Keuangan Republik Indonesia.
```
Jakarta.
```
Direktorat Jenderal Pengelolaan Utang. (2019). Dinamika utang pemerintah indonesia
```
```
(tech. rep.) (Official explanation of foreign currency debt composition and risk).
```
Kementerian Keuangan Republik Indonesia. Retrieved November 18, 2025, from
```
https://fiskal.kemenkeu.go.id/
```
95
```
Engle, R. F. (1982). Autoregressive conditional heteroscedasticity with estimates of the
```
variance of united kingdom inflation. Econometrica: Journal of the econometric
society, 987–1007.
```
Fadillah, F., Syahkilah, A., Rosyada, A. A., Hasmidyani, D., & Budiman, M. A. (2025).
```
Valuta asing: Peran dan fungsinya dalam sistem pembayaran internasional. Jurnal
```
Penelitian Ekonomi Manajemen dan Bisnis, 4 (2), 136–142.
```
```
Gujarati, D. N., & Porter, D. C. (2009). Basic econometrics. McGraw-hill.
```
```
Hassani, H., Yeganegi, M. R., Cu˜nado, J., & Gupta, R. (2020). Forecasting interest rate
```
volatility of the united kingdom: Evidence from over 150 years of data. Journal of
```
Applied Statistics, 47 (6), 1128–1143.
```
```
Imron, C., Mardlijah, & Asfihani, T. (2022). Metode numerik. Departemen Matematika
```
ITS.
```
International Monetary Fund. (2025). Imf staff completes 2025 article iv mission to
```
```
indonesia (Article IV Consultation No. PR/25/375). International Monetary Fund.
```
Retrieved November 30, 2025, from https://www.imf.org/en/news/articles/2025/
11/14/pr-25375-indonesia-imf-staff-completes-2025-article-iv-mission
```
Kim, J.-M., Kim, D. H., & Jung, H. (2021). Estimating yield spreads volatility using
```
garch-type models. The North American Journal of Economics and Finance, 57,
101396.
```
MacKinnon, J. G. (2010). Critical values for cointegration tests (tech. rep.). Queen’s
```
Economics Department Working Paper.
```
Markowitz, H. M. (2008). Portfolio selection: Efficient diversification of investments. Yale
```
university press.
```
Massey Jr, F. J. (1951). The kolmogorov-smirnov test for goodness of fit. Journal of the
```
```
American statistical Association, 46 (253), 68–78.
```
```
Morgan, J., dkk. (1997). Creditmetrics-technical document. JP Morgan, New York, 1,
```
102–127.
```
Nasir, M. (2013). Utang pemerintah: Peran dan ancamannya terhadap APBN (tech. rep.).
```
Pusat Pengelolaan Risiko Fiskal, Badan Kebijakan Fiskal, Kementerian Keuangan
Republik Indonesia. Retrieved November 16, 2025, from https://fiskal.kemenkeu.
go . id / files / berita - kajian / file / Utang Pemerintah Peran dan % 20Ancamannya
TerhadapAPBN.pdf
```
Rockafellar, R. T., Uryasev, S., dkk. (2000). Optimization of conditional value-at-risk.
```
Journal of risk, 2, 21–42.
```
Rockafellar, R. T., & Uryasev, S. (2002). Conditional value-at-risk for general loss
```
```
distributions. Journal of banking & finance, 26 (7), 1443–1471.
```
```
Sober, E. (1981). The principle of parsimony. The British Journal for the Philosophy of
```
```
Science, 32 (2), 145–156.
```
```
Thakkar, A., & Chaudhari, K. (2021). Fusion in stock market prediction: A decade survey
```
on the necessity, recent developments, and potential future directions. Information
Fusion, 65, 95–107.
```
Wei, W. W. S. (2006). Time series analysis: Univariate and multivariate methods
```
```
(2nd ed.). Pearson Addison Wesley.
```
```
Woodward, W. A., Gray, H. L., & Elliott, A. C. (2017). Applied time series analysis with
```
r. CRC press.
```
World Bank. (2025). Indonesia economic prospects, december 2025: Digital foundations
```
for growth. https://openknowledge.worldbank.org/en/publication
96
```
Yang, R., Li, L., Jiang, Q., & Qi, J. (2022). Optimal bond issuance with cost and liquidity
```
constraints for chinese local governments: A multi-period stochastic programming
```
approach. Empirical Economics, 63 (5), 2605–2632.
```
```
Yavuz, H. H., & G¨olba¸sı, U. (2019). Optimal composition of sovereign debt: An adaptation
```
from modern portfolio theory. Debt Management in Uncertain Times, 107.
Zenios, S. A., Consiglio, A., Athanasopoulou, M., Moshammer, E., Gavilan, A., & Erce,
A. (2019). Risk management for sovereign debt financing with sustainability
```
conditions. Globalization Institute Working Paper, (367).
```
```
Zhu, E. (2025). Implementation of the arima-garch model on usd/jpy exchange rate
```
forecasting. 2025 International Conference on Financial Risk and Investment
```
Management (ICFRIM 2025), 829–839.
```
97
DAFTAR LAMPIRAN
Lampiran 1
Listing Program MATLAB Model Cubic Spline
```
1 clc; clear; close all;
```
```
2 format long g;
```
3
4 %% SETUP DATA
```
5 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
6 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
7 sheet_name = ’cleaned’;
```
```
8 nama_kolom = ’IR_EUR_10Y’;
```
9
```
10 full_path = fullfile(folder_path, nama_file);
```
```
11 if ˜isfile(full_path), error(’File tidak ditemukan!’); end
```
12
```
13 raw_table = readtable(full_path, ’Sheet’, sheet_name, ’VariableNamingRule’, ’preserve’);
```
14
15 try
```
16 f_vals = raw_table.(nama_kolom);
```
17 catch
```
18 error([’Kolom "’ nama_kolom ’" tidak ditemukan.’]);
```
19 end
20
```
21 tgl_awal = datetime(2017, 7, 1);
```
```
22 jml_data = height(raw_table);
```
```
23 dates_full = tgl_awal + calmonths(0:jml_data-1)’;
```
```
24 x_axis = (1:jml_data)’;
```
25
26 %% FUNGSI ALGORITMA CUBIC SPLINE
```
27 function [f_interp, S] = myNaturalCubicSpline(x, f, x_query)
```
```
28 n = length(x);
```
```
29 h = diff(x);
```
30
```
31 A = zeros(n, n);
```
```
32 B = zeros(n, 1);
```
33
```
34 A(1, 1) = 1;
```
```
35 A(n, n) = 1;
```
36
37 for i = 2:n-1
```
38 A(i, i-1) = h(i-1);
```
```
39 A(i, i) = 2 * (h(i-1) + h(i));
```
```
40 A(i, i+1) = h(i);
```
```
41 B(i) = 3 * ((f(i+1) - f(i)) / h(i) - (f(i) - f(i-1)) / h(i-1));
```
42 end
43
```
44 c = A \ B;
```
45
```
46 S.a = f(1:end-1);
```
```
47 S.c = c(1:end-1);
```
```
48 S.c_full = c;
```
```
49 S.b = zeros(n-1,1);
```
```
50 S.d = zeros(n-1,1);
```
51
52 for i = 1:n-1
```
53 S.d(i) = (c(i+1) - c(i)) / (3 * h(i));
```
```
54 S.b(i) = (f(i+1) - f(i)) / h(i) - (h(i)/3) * (2*c(i) + c(i+1));
```
55 end
56
```
57 f_interp = zeros(size(x_query));
```
58
```
59 for k = 1:length(x_query)
```
```
60 xq = x_query(k);
```
```
61 if xq < x(1), i = 1;
```
```
62 elseif xq >= x(end), i = n-1;
```
63 else
99
```
64 idx = find(x <= xq, 1, ’last’);
```
```
65 i = min(max(idx, 1), n-1);
```
66 end
67
```
68 dx = xq - x(i);
```
```
69 f_interp(k) = S.a(i) + S.b(i)*dx + S.c(i)*dxˆ2 + S.d(i)*dxˆ3;
```
70 end
71 end
72
73 %% PROSES CUBIC SPLINE
```
74 idx_target = (dates_full >= datetime(2021, 2, 1)) & (dates_full <= datetime(2021, 8, 1));
```
```
75 f_vals(idx_target) = NaN;
```
76
```
77 idx_missing = isnan(f_vals);
```
```
78 idx_known = ˜isnan(f_vals);
```
79
```
80 x_known = x_axis(idx_known);
```
```
81 f_known = f_vals(idx_known);
```
```
82 x_query = x_axis(idx_missing);
```
83
```
84 [f_filled, S] = myNaturalCubicSpline(x_known, f_known, x_query);
```
85
```
86 f_final = f_vals;
```
```
87 f_final(idx_missing) = f_filled;
```
88
89 %% KOEFISIEN & MODEL MATEMATIKA
```
90 idx_anchor = 43;
```
```
91 idx_in_struct = find(x_known == idx_anchor);
```
```
92 if isempty(idx_in_struct)
```
```
93 error(’Titik jangkar (Jan 2021) tidak ditemukan.’);
```
94 end
95
```
96 xi = x_known(idx_in_struct);
```
```
97 ai = S.a(idx_in_struct);
```
```
98 bi = S.b(idx_in_struct);
```
```
99 ci = S.c(idx_in_struct);
```
```
100 di = S.d(idx_in_struct);
```
```
101 ci_next = S.c_full(idx_in_struct + 1);
```
102
```
103 fprintf(’\n------------------------------------------------------------\n’);
```
```
104 fprintf(’ NILAI KOEFISIEN\n’);
```
```
105 fprintf(’------------------------------------------------------------\n’);
```
```
106 fprintf(’i (titik awal) = %d (Januari 2021)\n’, xi);
```
```
107 fprintf(’c_%d = %.9f\n’, xi, ci);
```
```
108 fprintf(’c_%d = %.9f\n’, xi+1, ci_next);
```
```
109 fprintf(’a_%d = %.9f\n’, xi, ai);
```
```
110 fprintf(’b_%d = %.9f\n’, xi, bi);
```
```
111 fprintf(’d_%d = %.9f\n’, xi, di);
```
112
```
113 fprintf(’\n------------------------------------------------------------\n’);
```
```
114 fprintf(’ MODEL MATEMATIKA f_%d(x)\n’, xi);
```
```
115 fprintf(’------------------------------------------------------------\n’);
```
```
116 fprintf(’Rumus Umum: f_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)ˆ2 + d_i(x - x_i)ˆ3\n\n’);
```
117
```
118 fprintf(’Model Matematika:\n’);
```
```
119 fprintf(’f_%d(x) = %.9f + %.9f(x - %d) + %.9f(x - %d)ˆ2 + %.9f(x - %d)ˆ3\n’, ...
```
```
120 xi, ai, bi, xi, ci, xi, di, xi);
```
```
121 fprintf(’\n(Model ini hanya berlaku untuk x = 44 s.d. x = 50)\n’);
```
122
123 %% HASIL INTERPOLASI
```
124 fprintf(’\n------------------------------------------------------------\n’);
```
```
125 fprintf(’ HASIL INTERPOLASI (Feb 2021 - Agu 2021)\n’);
```
```
126 fprintf(’------------------------------------------------------------\n’);
```
127
```
128 dates_show = dates_full(idx_target);
```
```
129 vals_show = f_final(idx_target);
```
```
130 x_show = x_axis(idx_target);
```
131
```
132 fprintf(’%-20s %-10s %-20s\n’, ’Bulan’, ’x (Ke-)’, sprintf(’Nilai Spline f_%d(x)’, xi));
```
```
133 fprintf(’%s\n’, repmat(’-’, 1, 55));
```
```
134 for i = 1:length(vals_show)
```
```
135 fprintf(’%-20s %-10d %.9f\n’, ...
```
100
```
136 string(datestr(dates_show(i), ’mmmm yyyy’)), x_show(i), vals_show(i));
```
137 end
138
139 %% PLOT VISUALISASI
```
140 figure(’Name’, ’Hasil Interpolasi Cubic Spline’, ’Color’, ’w’);
```
```
141 plot(dates_full, f_final, ’b-’, ’LineWidth’, 1.5); hold on;
```
```
142 plot(dates_full(idx_known), f_vals(idx_known), ’ro’, ’MarkerSize’, 6);
```
```
143 plot(dates_full(idx_target), f_final(idx_target), ’go’, ’MarkerSize’, 6, ’LineWidth’, 1.5);
```
```
144 title([’Interpolasi Cubic Spline: ’ nama_kolom], ’Interpreter’, ’none’);
```
```
145 xlabel(’Tahun’); ylabel(sprintf(’Interest Rate f_%d(x)’, xi)); grid on;
```
```
146 legend(’Spline’, ’Data Asli’, ’Tebakan’, ’Location’, ’best’);
```
101
Lampiran 2
Listing Program R pada RStudio untuk Uji ADF
```
1 library(readxl)
```
```
2 library(urca)
```
3
4 # =========================================================================
5 # 1. SETUP PATH DAN IMPOR DATA
6 # =========================================================================
7 file_path <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
8 data_z <- suppressMessages(read_excel(file_path, sheet = "Data Training", range = "M3:U82", col_names =
```
```
FALSE))
```
9
10 # Mengubah nama kolom menjadi Z1, Z2, ..., Z9
```
11 colnames(data_z) <- paste0("Z", 1:ncol(data_z))
```
12
13 # =========================================================================
14 # 2. FUNGSI UJI ADF BERDASARKAN VARIABEL
15 # =========================================================================
```
16 uji_adf_per_variabel <- function(y, nama_var) {
```
```
17 cat(sprintf("\n====================================================================\n"))
```
```
18 cat(sprintf("%s :\n", nama_var))
```
```
19 cat(sprintf("====================================================================\n"))
```
20
21 # Z3 menggunakan differencing hingga level 2, sisanya level 1
```
22 max_diff <- ifelse(nama_var == "Z3", 2, 1)
```
23
```
24 for (diff_level in 0:max_diff) {
```
25
26 # a. Proses Differencing
```
27 if (diff_level > 0) {
```
```
28 y_test <- diff(y, differences = diff_level)
```
```
29 } else {
```
30 y_test <- y
```
31 }
```
```
32 y_clean <- na.omit(as.numeric(y_test))
```
33
34 # b. Setup Model ADF
```
35 if (nama_var == "Z5" && diff_level == 0) {
```
```
36 adf_model <- ur.df(y_clean, type = "drift", lags = 4, selectlags = "Fixed")
```
```
37 } else if (nama_var == "Z5" && diff_level == 1) {
```
```
38 adf_model <- ur.df(y_clean, type = "drift", lags = 3, selectlags = "Fixed")
```
```
39 } else {
```
```
40 adf_model <- ur.df(y_clean, type = "drift", lags = 11, selectlags = "AIC")
```
```
41 }
```
42
43 # c. Ekstraksi Nilai Parameter
44 matriks_koef <- adf_model@testreg$coefficients
45 delta_hat <- matriks_koef["z.lag.1", "Estimate"]
46 se_delta <- matriks_koef["z.lag.1", "Std. Error"]
47 adf_hitung <- matriks_koef["z.lag.1", "t value"]
48 adf_tabel_5 <- adf_model@cval["tau2", "5pct"]
49
50 # d. Mengatur Notasi Dinamis berdasarkan Tingkat Differencing
```
51 if (diff_level == 0) {
```
52 lhs_term <- "dZ_t"
```
53 lag_term <- "Z_{t-1}"
```
54 diff_term <- "dZ"
```
55 } else if (diff_level == 1) {
```
56 lhs_term <- "dˆ2 Z_t"
```
57 lag_term <- "dZ_{t-1}"
```
58 diff_term <- "dˆ2 Z"
```
59 } else {
```
```
60 lhs_term <- sprintf("dˆ%d Z_t", diff_level + 1)
```
```
61 lag_term <- sprintf("dˆ%d Z_{t-1}", diff_level)
```
```
62 diff_term <- sprintf("dˆ%d Z", diff_level + 1)
```
```
63 }
```
64
65 # e. Menyusun String Persamaan Regresi
```
66 persamaan <- paste(lhs_term, "=")
```
102
```
67 for (j in 1:nrow(matriks_koef)) {
```
```
68 nama_koef <- rownames(matriks_koef)[j]
```
```
69 nilai_koef <- round(matriks_koef[j, "Estimate"], 5)
```
```
70 abs_koef <- abs(nilai_koef)
```
71
```
72 if (nama_koef == "(Intercept)") {
```
```
73 persamaan <- paste(persamaan, nilai_koef)
```
```
74 } else if (nama_koef == "z.lag.1") {
```
```
75 tanda <- ifelse(nilai_koef < 0, "-", "+")
```
```
76 persamaan <- paste(persamaan, tanda, sprintf("%.5f %s", abs_koef, lag_term))
```
```
77 } else if (grepl("z\\.diff\\.lag", nama_koef)) {
```
```
78 tanda <- ifelse(nilai_koef < 0, "-", "+")
```
79 # Ekstraksi angka lag secara aman
```
80 lag_num <- gsub("[ˆ0-9]", "", nama_koef)
```
```
81 persamaan <- paste(persamaan, tanda, sprintf("%.5f %s_{t-%s}", abs_koef, diff_term, lag_num))
```
```
82 }
```
```
83 }
```
84
```
85 # Menambahkan error term (epsilon) di akhir persamaan
```
```
86 persamaan <- paste(persamaan, "+ e_t")
```
87
88 # f. Penentuan Keputusan
```
89 kesimpulan <- ifelse(adf_hitung < adf_tabel_5, "STASIONER", "TDK STASIONER")
```
90
91 # g. Format Cetak Hasil
```
92 cat(sprintf("\n--- Tingkat Differencing (d) = %d ---\n", diff_level))
```
```
93 cat("Model Regresi:\n")
```
```
94 cat(persamaan, "\n\n")
```
95
96 # Mencetak Tabel
```
97 df_hasil <- data.frame(
```
```
98 ‘Estimasi (Delta)‘ = round(delta_hat, 5),
```
```
99 ‘Std.Error‘ = round(se_delta, 5),
```
```
100 ‘ADF Hitung‘ = round(adf_hitung, 5),
```
```
101 ‘ADF Tabel 5%‘ = round(adf_tabel_5, 5),
```
102 Kesimpulan = kesimpulan,
103 check.names = FALSE
```
104 )
```
```
105 rownames(df_hasil) <- NULL
```
```
106 print(df_hasil)
```
```
107 }
```
```
108 cat("\n") # Memberi jarak antar variabel
```
```
109 }
```
110
111 # =========================================================================
112 # 3. EKSEKUSI UTAMA LOOPING
113 # =========================================================================
```
114 for (i in 1:ncol(data_z)) {
```
```
115 var_name <- colnames(data_z)[i]
```
```
116 uji_adf_per_variabel(data_z[[i]], var_name)
```
```
117 }
```
103
Lampiran 3
Listing Program R pada RStudio untuk Estimasi dan Uji
Signifikansi Parameter
```
1 library(readxl)
```
```
2 library(tseries)
```
```
3 library(forecast)
```
4
5 # =========================================================================
6 # 1. IMPORT DATA
7 # =========================================================================
8 file_path <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
9 data_mentah <- suppressMessages(read_excel(file_path, sheet = "Data Awal"))
```
10
11 # =========================================================================
```
12 # 2. EKSTRAKSI DAN TRANSFORMASI (Y_raw -> Y_trans -> Z)
```
13 # =========================================================================
14 # Z1: IR_USD_5Y
15 Y1_raw <- data_mentah$‘IR_USD_5Y‘[1:80]
16 Y1_trans <- Y1_raw ˆ 0.5
17 Z1 <- Y1_trans
18
19 # Z2: IR_USD_10Y
20 Y2_raw <- data_mentah$‘IR_USD_10Y‘[1:80]
```
21 Y2_trans <- (Y2_raw ˆ 0.5) ˆ 0.5
```
22 Z2 <- Y2_trans
23
24 # Z3: IR_USD_30Y
25 Y3_raw <- data_mentah$‘IR_USD_30Y‘[1:80]
```
26 Y3_trans <- (Y3_raw ˆ -0.5) ˆ 0.5
```
27 Z3 <- Y3_trans
28
29 # Z4: IR_EUR_7Y
30 Y4_raw <- data_mentah$‘IR_EUR_7Y‘[1:80]
31 Y4_trans <- Y4_raw ˆ 0.5
32 Z4 <- Y4_trans
33
34 # Z5: IR_EUR_10Y
35 Y5_raw <- data_mentah$‘IR_EUR_10Y‘[1:80]
36 Y5_trans <- Y5_raw ˆ 0.5
37 Z5 <- Y5_trans
38
39 # Z6: IR_JPY_5Y
40 Y6_raw <- data_mentah$‘IR_JPY_5Y‘[1:80]
```
41 Y6_trans <- (log(Y6_raw) + 1) ˆ 0.5
```
42 Z6 <- Y6_trans
43
44 # Z7: IR_JPY_10Y
45 Y7_raw <- data_mentah$‘IR_JPY_10Y‘[1:80]
```
46 Y7_trans <- log(Y7_raw)
```
47 Z7 <- Y7_trans
48
49 # Z8: FX_USD_EUR
50 Y8_raw <- data_mentah$‘FX_USD_EUR‘[1:80]
```
51 Y8_trans <- Y8_raw ˆ (-2)
```
52 Z8 <- Y8_trans
53
54 # Z9: FX_USD_JPY
55 Y9_raw <- data_mentah$‘FX_USD_JPY‘[1:80]
```
56 Y9_trans <- Y9_raw ˆ (-3)
```
57 Z9 <- Y9_trans
58
59
60 # =========================================================================
61 # 3. FUNGSI ESTIMASI & UJI SIGNIFIKANSI PARAMETER
62 # =========================================================================
```
63 uji_parameter_model <- function(data_z, nama_z, diff_val, daftar_model) {
```
```
64 cat(sprintf("\n====================================================================\n"))
```
```
65 cat(sprintf("%s :\n", nama_z))
```
104
```
66 cat(sprintf("====================================================================\n"))
```
67
```
68 for (m in daftar_model) {
```
```
69 cat(sprintf("\nARIMA%s\n", m$nama))
```
70
71 # a. Fitting Model
```
72 fit <- tryCatch({
```
```
73 Arima(data_z, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "ML")
```
```
74 }, error = function(e) {
```
```
75 cat(" Error dalam mengestimasi model.\n")
```
```
76 return(NULL)
```
```
77 })
```
78
```
79 if (is.null(fit)) next
```
80
81 # b. Ekstraksi Koefisien & Standar Error
82 estimasi <- fit$coef[fit$mask]
```
83 se <- suppressWarnings(sqrt(diag(fit$var.coef)))
```
84
```
85 # c. Inversi Tanda MA (Konvensi Adanya Perbedaan Model MA)
```
```
86 idx_ma <- grep("ˆma", names(estimasi))
```
```
87 if (length(idx_ma) > 0) estimasi[idx_ma] <- -estimasi[idx_ma]
```
88
```
89 # d. Uji Signifikansi (t-test)
```
90 t_hit <- estimasi / se
```
91 n_eff <- length(na.omit(data_z)) - diff_val
```
```
92 num_params <- sum(fit$mask)
```
```
93 t_tab <- qt(0.975, df = n_eff - num_params)
```
94
```
95 kesimpulan <- ifelse(is.na(t_hit), "NaN",
```
```
96 ifelse(abs(t_hit) > t_tab, "Signifikan", "Tdk Signifikan"))
```
97
98 # e. Format Tabel Output
```
99 df_param <- data.frame(
```
```
100 Parameter = names(estimasi),
```
```
101 Estimasi = round(estimasi, 4),
```
```
102 ‘Std.Error‘ = round(se, 4),
```
```
103 ‘t_hitung‘ = round(t_hit, 4),
```
```
104 ‘t_tabel‘ = round(t_tab, 4),
```
105 Kesimpulan = kesimpulan,
106 check.names = FALSE
```
107 )
```
```
108 rownames(df_param) <- NULL
```
```
109 print(df_param)
```
```
110 }
```
```
111 cat("\n")
```
```
112 }
```
113
114 # =========================================================================
```
115 # 4. EKSEKUSI MODEL BERDASARKAN VARIABEL (Z1 - Z9)
```
116 # =========================================================================
117
118 # --- Z1 ---
```
119 uji_parameter_model(Z1, "Z1", diff_val = 1, list(
```
```
120 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
121 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
122 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL)
```
```
123 ))
```
124
125 # --- Z2 ---
```
126 uji_parameter_model(Z2, "Z2", diff_val = 1, list(
```
```
127 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
128 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
129 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
130 list(nama="([9],1,0)", order=c(9,1,0), fixed=c(rep(0,8), NA)),
```
```
131 list(nama="([9],1,1)", order=c(9,1,1), fixed=c(rep(0,8), NA, NA))
```
```
132 ))
```
133
134 # --- Z3 ---
```
135 uji_parameter_model(Z3, "Z3", diff_val = 2, list(
```
```
136 list(nama="(4,2,2)", order=c(4,2,2), fixed=NULL),
```
```
137 list(nama="(2,2,2)", order=c(2,2,2), fixed=NULL),
```
105
```
138 list(nama="(4,2,0)", order=c(4,2,0), fixed=NULL),
```
```
139 list(nama="(2,2,0)", order=c(2,2,0), fixed=NULL),
```
```
140 list(nama="(0,2,2)", order=c(0,2,2), fixed=NULL),
```
```
141 list(nama="([2],2,0)", order=c(2,2,0), fixed=c(0, NA)),
```
```
142 list(nama="([4],2,0)", order=c(4,2,0), fixed=c(0, 0, 0, NA)),
```
```
143 list(nama="([2],2,2)", order=c(2,2,2), fixed=c(0, NA, NA, NA)),
```
```
144 list(nama="([4],2,2)", order=c(4,2,2), fixed=c(0, 0, 0, NA, NA, NA))
```
```
145 ))
```
146
147 # --- Z4 ---
```
148 uji_parameter_model(Z4, "Z4", diff_val = 1, list(
```
```
149 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
150 list(nama="(2,1,1)", order=c(2,1,1), fixed=NULL),
```
```
151 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
152 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
153 list(nama="(2,1,0)", order=c(2,1,0), fixed=NULL)
```
```
154 ))
```
155
156 # --- Z5 ---
```
157 uji_parameter_model(Z5, "Z5", diff_val = 1, list(
```
```
158 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
159 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
160 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL)
```
```
161 ))
```
162
163 # --- Z6 ---
```
164 uji_parameter_model(Z6, "Z6", diff_val = 1, list(
```
```
165 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
166 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
167 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
168 ))
```
169
170 # --- Z7 ---
```
171 uji_parameter_model(Z7, "Z7", diff_val = 1, list(
```
```
172 list(nama="([14],1,[14])", order=c(14,1,14), fixed=c(rep(0,13), NA, rep(0,13), NA)),
```
```
173 list(nama="(0,1,[14])", order=c(0,1,14), fixed=c(rep(0,13), NA)),
```
```
174 list(nama="([14],1,0)", order=c(14,1,0), fixed=c(rep(0,13), NA))
```
```
175 ))
```
176
177 # --- Z8 ---
```
178 uji_parameter_model(Z8, "Z8", diff_val = 1, list(
```
```
179 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
180 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
181 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
182 ))
```
183
184 # --- Z9 ---
```
185 uji_parameter_model(Z9, "Z9", diff_val = 1, list(
```
```
186 list(nama="(1,1,1)", order=c(1,1,1), fixed=NULL),
```
```
187 list(nama="([8],1,1)", order=c(8,1,1), fixed=c(rep(0,7), NA, NA)),
```
```
188 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
189 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
190 list(nama="([8],1,0)", order=c(8,1,0), fixed=c(rep(0,7), NA))
```
```
191 ))
```
106
Lampiran 4
Listing Program R pada RStudio untuk Uji Diagnostik Residual
```
1 library(readxl)
```
```
2 library(tseries)
```
```
3 library(forecast)
```
```
4 library(FinTS)
```
5
6 # =========================================================================
7 # 1. IMPORT DATA
8 # =========================================================================
9 file_path <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
10 data_mentah <- suppressMessages(read_excel(file_path, sheet = "Data Awal"))
```
11
12 # =========================================================================
```
13 # 2. EKSTRAKSI DAN TRANSFORMASI (Y_raw -> Y_trans -> Z)
```
14 # =========================================================================
15 # Z1: IR_USD_5Y
16 Y1_raw <- data_mentah$‘IR_USD_5Y‘[1:80]
17 Z1 <- Y1_raw ˆ 0.5
18
19 # Z2: IR_USD_10Y
20 Y2_raw <- data_mentah$‘IR_USD_10Y‘[1:80]
```
21 Z2 <- (Y2_raw ˆ 0.5) ˆ 0.5
```
22
23 # Z3: IR_USD_30Y
24 Y3_raw <- data_mentah$‘IR_USD_30Y‘[1:80]
```
25 Z3 <- (Y3_raw ˆ -0.5) ˆ 0.5
```
26
27 # Z4: IR_EUR_7Y
28 Y4_raw <- data_mentah$‘IR_EUR_7Y‘[1:80]
29 Z4 <- Y4_raw ˆ 0.5
30
31 # Z5: IR_EUR_10Y
32 Y5_raw <- data_mentah$‘IR_EUR_10Y‘[1:80]
33 Z5 <- Y5_raw ˆ 0.5
34
35 # Z6: IR_JPY_5Y
36 Y6_raw <- data_mentah$‘IR_JPY_5Y‘[1:80]
```
37 Z6 <- (log(Y6_raw) + 1) ˆ 0.5
```
38
39 # Z7: IR_JPY_10Y
40 Y7_raw <- data_mentah$‘IR_JPY_10Y‘[1:80]
```
41 Z7 <- log(Y7_raw)
```
42
43 # Z8: FX_USD_EUR
44 Y8_raw <- data_mentah$‘FX_USD_EUR‘[1:80]
```
45 Z8 <- Y8_raw ˆ (-2)
```
46
47 # Z9: FX_USD_JPY
48 Y9_raw <- data_mentah$‘FX_USD_JPY‘[1:80]
```
49 Z9 <- Y9_raw ˆ (-3)
```
50
51 # =========================================================================
52 # 3. FUNGSI UJI RESIDUAL DIAGNOSTIK
53 # =========================================================================
```
54 uji_residual_model <- function(data_z, nama_z, diff_val, daftar_model) {
```
```
55 cat(sprintf("\n====================================================================\n"))
```
```
56 cat(sprintf("UJI RESIDUAL VARIABEL : %s\n", nama_z))
```
```
57 cat(sprintf("====================================================================\n"))
```
58
```
59 hasil_ringkasan <- list()
```
60
```
61 for (m in daftar_model) {
```
```
62 cat(sprintf("\n--- ARIMA %s ---\n", m$nama))
```
63
64 # a. Fitting Model
```
65 fit <- Arima(data_z, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "ML")
```
```
66 resids <- na.omit(as.numeric(residuals(fit)))
```
67
107
```
68 n_eff <- length(resids) - diff_val
```
```
69 num_params <- sum(fit$mask)
```
70
```
71 # b. Uji Normalitas (Kolmogorov-Smirnov)
```
```
72 ks <- suppressWarnings(ks.test(resids, "pnorm", mean(resids), sd(resids)))
```
```
73 D_hit <- as.numeric(ks$statistic)
```
```
74 D_tab <- 1.35 / sqrt(n_eff)
```
```
75 norm_status <- ifelse(D_hit <= D_tab, "Normal", "Tdk Normal")
```
76
```
77 cat(sprintf("1. Normalitas (KS) : D_hitung = %.4f | D_tabel = %.4f -> %s\n", D_hit, D_tab, norm_status)
```
```
)
```
78
```
79 # c. Uji White Noise (Ljung-Box) lag = 12
```
80 lag_lb <- 12
81 df_lb <- lag_lb - num_params
```
82 lb <- Box.test(resids, lag = lag_lb, type = "Ljung-Box", fitdf = num_params)
```
```
83 Q_hit <- as.numeric(lb$statistic)
```
```
84 chi_tab_lb <- qchisq(0.95, df = df_lb)
```
```
85 wn_status <- ifelse(Q_hit <= chi_tab_lb, "White Noise", "Bukan WN")
```
86
```
87 cat(sprintf("2. White Noise (LB): Q_hitung = %.4f | Chi_tabel = %.4f -> %s\n", Q_hit, chi_tab_lb, wn_
```
```
status))
```
88
```
89 # d. Uji Heteroskedastisitas (ARCH-LM) lag = 12
```
90 lag_arch <- 12
```
91 arch <- ArchTest(resids, lags = lag_arch)
```
```
92 LM_hit <- as.numeric(arch$statistic)
```
```
93 chi_tab_arch <- qchisq(0.95, df = lag_arch)
```
```
94 arch_status <- ifelse(LM_hit <= chi_tab_arch, "Homoskedastis", "Heteroskedastis")
```
95
```
96 cat(sprintf("3. ARCH-LM : LM_hitung = %.4f | Chi_tabel = %.4f -> %s\n", LM_hit, chi_tab_arch,
```
```
arch_status))
```
97
98 # --- PROSES PEMBENTUKAN MODEL REGRESI BANTU ARCH ---
99 resids_sq <- residsˆ2
```
100 matriks_lag <- embed(resids_sq, lag_arch + 1)
```
101 Y_arch <- matriks_lag[, 1]
102 X_arch <- matriks_lag[, -1]
103
104 # Menjalankan Regresi OLS
```
105 reg_arch <- lm(Y_arch ˜ X_arch)
```
```
106 koef_arch <- coef(reg_arch)
```
```
107 r_squared <- summary(reg_arch)$r.squared # Menarik nilai R-Squared
```
108
```
109 # Menyusun string persamaan (e_t sebagai epsilon)
```
```
110 eq_arch <- sprintf("e_tˆ2 = %.5f", koef_arch[1]) # alpha_0
```
```
111 for(k in 1:lag_arch) {
```
112 val <- koef_arch[k+1]
```
113 if(!is.na(val)) {
```
```
114 tanda <- ifelse(val < 0, "-", "+")
```
```
115 eq_arch <- paste(eq_arch, tanda, sprintf("%.5f e_{t-%d}ˆ2", abs(val), k))
```
```
116 }
```
```
117 }
```
```
118 eq_arch <- paste(eq_arch, "+ v_t")
```
```
119 cat(sprintf(" Model Regresi : %s\n", eq_arch))
```
```
120 cat(sprintf(" R-Squared (Rˆ2) : %.5f\n", r_squared)) # Mencetak nilai R-Squared
```
121
122 # e. Simpan untuk tabel ringkasan
```
123 hasil_ringkasan[[length(hasil_ringkasan) + 1]] <- data.frame(
```
124 Model = m$nama,
125 Normalitas = norm_status,
126 ‘White Noise‘ = wn_status,
127 ‘ARCH-LM‘ = arch_status,
128 check.names = FALSE
```
129 )
```
```
130 }
```
131
```
132 cat("\n--- RINGKASAN UJI RESIDUAL ---\n")
```
```
133 df_summary <- do.call(rbind, hasil_ringkasan)
```
```
134 print(df_summary, row.names = FALSE)
```
```
135 cat("\n")
```
```
136 }
```
108
137
138 # =========================================================================
139 # 4. EKSEKUSI MODEL BERDASARKAN VARIABEL
140 # =========================================================================
141
142 # --- Z1 ---
```
143 uji_residual_model(Z1, "Z1", diff_val = 1, list(
```
```
144 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
145 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL)
```
```
146 ))
```
147
148 # --- Z2 ---
```
149 uji_residual_model(Z2, "Z2", diff_val = 1, list(
```
```
150 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
151 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
152 ))
```
153
```
154 # --- Z3 (Differencing = 2) ---
```
```
155 uji_residual_model(Z3, "Z3", diff_val = 2, list(
```
```
156 list(nama="(2,2,2)", order=c(2,2,2), fixed=NULL),
```
```
157 list(nama="(4,2,0)", order=c(4,2,0), fixed=NULL),
```
```
158 list(nama="(2,2,0)", order=c(2,2,0), fixed=NULL),
```
```
159 list(nama="(0,2,2)", order=c(0,2,2), fixed=NULL),
```
```
160 list(nama="([2],2,0)", order=c(2,2,0), fixed=c(0, NA)),
```
```
161 list(nama="([2],2,2)", order=c(2,2,2), fixed=c(0, NA, NA, NA))
```
```
162 ))
```
163
164 # --- Z4 ---
```
165 uji_residual_model(Z4, "Z4", diff_val = 1, list(
```
```
166 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
167 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
168 list(nama="(2,1,0)", order=c(2,1,0), fixed=NULL)
```
```
169 ))
```
170
171 # --- Z5 ---
```
172 uji_residual_model(Z5, "Z5", diff_val = 1, list(
```
```
173 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
174 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL)
```
```
175 ))
```
176
177 # --- Z6 ---
```
178 uji_residual_model(Z6, "Z6", diff_val = 1, list(
```
```
179 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
180 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
181 ))
```
182
183 # --- Z7 ---
```
184 uji_residual_model(Z7, "Z7", diff_val = 1, list(
```
```
185 list(nama="(0,1,[14])", order=c(0,1,14), fixed=c(rep(0,13), NA)),
```
```
186 list(nama="([14],1,0)", order=c(14,1,0), fixed=c(rep(0,13), NA))
```
```
187 ))
```
188
189 # --- Z8 ---
```
190 uji_residual_model(Z8, "Z8", diff_val = 1, list(
```
```
191 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
192 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
193 ))
```
194
195 # --- Z9 ---
```
196 uji_residual_model(Z9, "Z9", diff_val = 1, list(
```
```
197 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
198 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
199 ))
```
109
Lampiran 5
Listing Program R pada RStudio untuk Perhitungan MAPE
```
1 library(readxl)
```
```
2 library(tseries)
```
```
3 library(forecast)
```
4
5 # =========================================================================
6 # 1. IMPORT DATA & SETUP
7 # =========================================================================
8 file_path <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
9 data_mentah <- suppressMessages(read_excel(file_path, sheet = "Data Awal"))
```
10
11 # =========================================================================
```
12 # 2. FUNGSI EVALUASI MAPE (TESTING)
```
13 # =========================================================================
```
14 evaluasi_mape <- function(data_all, nama_kolom, nama_z, trans_func, back_trans_func, daftar_model) {
```
15
```
16 # Ekstraksi Data Training (1-80) dan Testing (81-101)
```
17 train_raw <- data_all[[nama_kolom]][1:80]
18 test_raw <- data_all[[nama_kolom]][81:101]
19
20 # Transformasi data training
```
21 y_train <- trans_func(train_raw)
```
```
22 h_len <- length(test_raw)
```
23
```
24 cat(sprintf("\n======================================================\n"))
```
```
25 cat(sprintf(" EVALUASI MAPE (TESTING) : %s (%s)\n", nama_z, nama_kolom))
```
```
26 cat(sprintf("======================================================\n"))
```
27
```
28 hasil <- data.frame(Model = character(), ‘MAPE (%)‘ = numeric(), stringsAsFactors = FALSE)
```
29
```
30 for (m in daftar_model) {
```
```
31 # Fitting Model (Mengabaikan peringatan jika ML kesulitan mencari titik optimum pada model tertentu)
```
```
32 fit <- suppressWarnings(Arima(y_train, order = m$order, fixed = m$fixed, include.mean = FALSE, method =
```
```
"ML"))
```
33
34 # Forecast
```
35 fc <- suppressWarnings(forecast(fit, h = h_len))
```
36
```
37 # Back-Transformasi hasil rata-rata (mean) forecast
```
```
38 fc_mean_asli <- back_trans_func(as.numeric(fc$mean))
```
39
40 # Menghitung MAPE
```
41 mape_val <- mean(abs((test_raw - fc_mean_asli) / test_raw)) * 100
```
42
43 # Simpan ke tabel
```
44 hasil <- rbind(hasil, data.frame(Model = m$nama, ‘MAPE (%)‘ = round(mape_val, 5), check.names = FALSE))
```
```
45 }
```
46
```
47 # Urutkan berdasarkan MAPE terkecil (Akurasi terbaik)
```
```
48 hasil_urut <- hasil[order(hasil$‘MAPE (%)‘), ]
```
```
49 rownames(hasil_urut) <- NULL
```
```
50 print(hasil_urut)
```
```
51 }
```
52
53 # =========================================================================
54 # 3. EKSEKUSI MODEL YANG "LAYAK" PER VARIABEL
55 # =========================================================================
56
57 # --- Z1 : IR_USD_5Y ---
58 # Transformasi: ˆ0.5 | Back-Transform: ˆ2
```
59 evaluasi_mape(data_mentah, "IR_USD_5Y", "Z1",
```
```
60 trans_func = function(x) xˆ0.5,
```
```
61 back_trans_func = function(x) xˆ2,
```
```
62 list(
```
```
63 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
64 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL)
```
```
65 ))
```
66
110
67 # --- Z2 : IR_USD_10Y ---
68 # Transformasi: ˆ0.25 | Back-Transform: ˆ4
```
69 evaluasi_mape(data_mentah, "IR_USD_10Y", "Z2",
```
```
70 trans_func = function(x) xˆ0.25,
```
```
71 back_trans_func = function(x) xˆ4,
```
```
72 list(
```
```
73 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
74 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
75 ))
```
76
77 # --- Z3 : IR_USD_30Y ---
78 # Transformasi: ˆ-0.25 | Back-Transform: ˆ-4
```
79 evaluasi_mape(data_mentah, "IR_USD_30Y", "Z3",
```
```
80 trans_func = function(x) xˆ(-0.25),
```
```
81 back_trans_func = function(x) xˆ(-4),
```
```
82 list(
```
```
83 list(nama="(2,2,2)", order=c(2,2,2), fixed=NULL),
```
```
84 list(nama="([2],2,2)", order=c(2,2,2), fixed=c(0, NA, NA, NA))
```
```
85 ))
```
86
87 # --- Z4 : IR_EUR_7Y ---
88 # Transformasi: ˆ0.5 | Back-Transform: ˆ2
```
89 evaluasi_mape(data_mentah, "IR_EUR_7Y", "Z4",
```
```
90 trans_func = function(x) xˆ0.5,
```
```
91 back_trans_func = function(x) xˆ2,
```
```
92 list(
```
```
93 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
94 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL),
```
```
95 list(nama="(2,1,0)", order=c(2,1,0), fixed=NULL)
```
```
96 ))
```
97
98 # --- Z5 : IR_EUR_10Y ---
99 # Transformasi: ˆ0.5 | Back-Transform: ˆ2
```
100 evaluasi_mape(data_mentah, "IR_EUR_10Y", "Z5",
```
```
101 trans_func = function(x) xˆ0.5,
```
```
102 back_trans_func = function(x) xˆ2,
```
```
103 list(
```
```
104 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL)
```
```
105 ))
```
106
107 # --- Z6 : IR_JPY_5Y ---
```
108 # Transformasi: (ln(x) + 1)ˆ0.5 | Back-Transform: exp(xˆ2 - 1)
```
```
109 evaluasi_mape(data_mentah, "IR_JPY_5Y", "Z6",
```
```
110 trans_func = function(x) (log(x) + 1)ˆ0.5,
```
```
111 back_trans_func = function(x) exp((xˆ2) - 1),
```
```
112 list(
```
```
113 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
114 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
115 ))
```
116
117 # --- Z7 : IR_JPY_10Y ---
```
118 # Transformasi: ln(x) | Back-Transform: exp(x)
```
```
119 evaluasi_mape(data_mentah, "IR_JPY_10Y", "Z7",
```
```
120 trans_func = function(x) log(x),
```
```
121 back_trans_func = function(x) exp(x),
```
```
122 list(
```
```
123 list(nama="(0,1,[14])", order=c(0,1,14), fixed=c(rep(0,13), NA))
```
```
124 ))
```
125
126 # --- Z8 : FX_USD_EUR ---
127 # Transformasi: ˆ-2 | Back-Transform: ˆ-0.5
```
128 evaluasi_mape(data_mentah, "FX_USD_EUR", "Z8",
```
```
129 trans_func = function(x) xˆ(-2),
```
```
130 back_trans_func = function(x) xˆ(-0.5),
```
```
131 list(
```
```
132 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
133 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
134 ))
```
135
136 # --- Z9 : FX_USD_JPY ---
```
137 # Transformasi: ˆ-3 | Back-Transform: ˆ-(1/3)
```
```
138 evaluasi_mape(data_mentah, "FX_USD_JPY", "Z9",
```
111
```
139 trans_func = function(x) xˆ(-3),
```
```
140 back_trans_func = function(x) xˆ(-1/3),
```
```
141 list(
```
```
142 list(nama="(0,1,1)", order=c(0,1,1), fixed=NULL),
```
```
143 list(nama="(1,1,0)", order=c(1,1,0), fixed=NULL)
```
```
144 ))
```
112
Lampiran 6
Listing Program R pada RStudio untuk Plot Data Training
dan Model
```
1 library(readxl)
```
```
2 library(forecast)
```
3
4 # =========================================================================
5 # 1. IMPORT DATA & TRANSFORMASI
6 # =========================================================================
7 file_path <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
8 data_mentah <- suppressMessages(read_excel(file_path, sheet = "Data Awal"))
```
9
10 # Z1: IR_USD_5Y
11 Y1_raw <- data_mentah$‘IR_USD_5Y‘[1:80]
12 Z1 <- Y1_raw ˆ 0.5
13
14 # Z2: IR_USD_10Y
15 Y2_raw <- data_mentah$‘IR_USD_10Y‘[1:80]
```
16 Z2 <- (Y2_raw ˆ 0.5) ˆ 0.5
```
17
18 # Z3: IR_USD_30Y
19 Y3_raw <- data_mentah$‘IR_USD_30Y‘[1:80]
```
20 Z3 <- (Y3_raw ˆ -0.5) ˆ 0.5
```
21
22 # Z4: IR_EUR_7Y
23 Y4_raw <- data_mentah$‘IR_EUR_7Y‘[1:80]
24 Z4 <- Y4_raw ˆ 0.5
25
26 # Z5: IR_EUR_10Y
27 Y5_raw <- data_mentah$‘IR_EUR_10Y‘[1:80]
28 Z5 <- Y5_raw ˆ 0.5
29
30 # Z6: IR_JPY_5Y
31 Y6_raw <- data_mentah$‘IR_JPY_5Y‘[1:80]
```
32 Z6 <- (log(Y6_raw) + 1) ˆ 0.5
```
33
34 # Z7: IR_JPY_10Y
35 Y7_raw <- data_mentah$‘IR_JPY_10Y‘[1:80]
```
36 Z7 <- log(Y7_raw)
```
37
38 # Z8: FX_USD_EUR
39 Y8_raw <- data_mentah$‘FX_USD_EUR‘[1:80]
```
40 Z8 <- Y8_raw ˆ (-2)
```
41
42 # Z9: FX_USD_JPY
43 Y9_raw <- data_mentah$‘FX_USD_JPY‘[1:80]
```
44 Z9 <- Y9_raw ˆ (-3)
```
45
46 # =========================================================================
47 # 2. DEFINISI DAFTAR MODEL & FUNGSI BACK-TRANSFORM
48 # =========================================================================
```
49 daftar_model <- list(
```
```
50 list(var="IR_USD_5Y", nama="ARIMA(0,1,1)", raw=Y1_raw, trans=Z1, order=c(0,1,1), fixed=NULL, back_
```
```
trans=function(x) xˆ2),
```
```
51 list(var="IR_USD_10Y", nama="ARIMA(1,1,0)", raw=Y2_raw, trans=Z2, order=c(1,1,0), fixed=NULL, back_
```
```
trans=function(x) xˆ4),
```
```
52 list(var="IR_USD_30Y", nama="ARIMA([2],2,2)", raw=Y3_raw, trans=Z3, order=c(2,2,2), fixed=c(0, NA, NA,
```
```
NA), back_trans=function(x) xˆ(-4)),
```
```
53 list(var="IR_EUR_7Y", nama="ARIMA(0,1,1)", raw=Y4_raw, trans=Z4, order=c(0,1,1), fixed=NULL, back_
```
```
trans=function(x) xˆ2),
```
```
54 list(var="IR_EUR_10Y", nama="ARIMA(0,1,1)", raw=Y5_raw, trans=Z5, order=c(0,1,1), fixed=NULL, back_
```
```
trans=function(x) xˆ2),
```
```
55 list(var="IR_JPY_5Y", nama="ARIMA(1,1,0)", raw=Y6_raw, trans=Z6, order=c(1,1,0), fixed=NULL, back_
```
```
trans=function(x) exp(xˆ2 - 1)),
```
```
56 list(var="IR_JPY_10Y", nama="ARIMA(0,1,[14])", raw=Y7_raw, trans=Z7, order=c(0,1,14), fixed=c(rep(0,13),
```
```
NA), back_trans=function(x) exp(x)),
```
```
57 list(var="FX_USD_EUR", nama="ARIMA(0,1,1)", raw=Y8_raw, trans=Z8, order=c(0,1,1), fixed=NULL, back_
```
```
trans=function(x) xˆ(-0.5)),
```
113
```
58 list(var="FX_USD_JPY", nama="ARIMA(0,1,1)", raw=Y9_raw, trans=Z9, order=c(0,1,1), fixed=NULL, back_
```
```
trans=function(x) xˆ(-1/3))
```
```
59 )
```
60
```
61 tgl_seq <- seq(as.Date("2017-07-01"), by = "month", length.out = 80)
```
```
62 label_waktu <- format(tgl_seq, "%B-%y")
```
63
64 # =========================================================================
65 # 3. PROSES FITTING & VISUALISASI SATU PER SATU
66 # =========================================================================
```
67 par(mar = c(7, 5, 4, 2))
```
68
```
69 for (m in daftar_model) {
```
```
70 n_train <- length(m$raw)
```
71
```
72 fit <- tryCatch({
```
```
73 Arima(m$trans, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "ML")
```
```
74 }, error = function(e) {
```
```
75 Arima(m$trans, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "CSS")
```
```
76 })
```
77
```
78 fitted_z <- as.numeric(fitted(fit))
```
```
79 fitted_y <- m$back_trans(fitted_z)
```
80
81 d_order <- m$order[2]
82 start_idx <- d_order + 1
```
83 if (start_idx <= 2 && m$var == "IR_USD_30Y") { start_idx <- 3 }
```
84
85 y_raw_plot <- m$raw[start_idx:n_train]
86 y_fit_plot <- fitted_y[start_idx:n_train]
87
```
88 y_max <- max(c(y_raw_plot, y_fit_plot), na.rm = TRUE)
```
```
89 y_min <- min(c(y_raw_plot, y_fit_plot), na.rm = TRUE)
```
90 t_plot <- start_idx:n_train
91
```
92 plot(t_plot, y_raw_plot, type = "l", col = "black", lwd = 2,
```
```
93 xlim = c(start_idx, n_train), ylim = c(y_min, y_max),
```
```
94 main = paste("2. Data Training vs Model -", m$nama),
```
```
95 xlab = "", ylab = m$var, xaxt = "n", cex.main = 1.3, cex.lab = 1.1)
```
96
```
97 idx_ticks_fit <- seq(start_idx, n_train, by = 6)
```
```
98 axis(1, at = idx_ticks_fit, labels = label_waktu[idx_ticks_fit], las = 2, cex.axis = 1.1)
```
99
```
100 mtext("Periode", side = 1, line = 5.5, cex = 1.1)
```
101
```
102 lines(t_plot, y_fit_plot, col = "red", lwd = 2, lty = 2)
```
103
```
104 legend("topleft", legend = c("Data Training", "Model Fitted"),
```
```
105 col = c("black", "red"), lty = c(1, 2), lwd = 2, cex = 1, bty = "n")
```
```
106 }
```
107
```
108 par(mar = c(5, 4, 4, 2) + 0.1)
```
114
Lampiran 7
Listing Program R pada RStudio untuk Hasil Peramalan
```
1 library(readxl)
```
```
2 library(forecast)
```
3
4 file_path_read <- "E:/KULIAH/Kebutuhan TA/Source Code/Tugas_Akhir_ARIMA_GARCH/Data_Tugas_Akhir.xlsx"
```
5 data_mentah <- suppressMessages(read_excel(file_path_read, sheet = "Data Awal"))
```
6
7 Y1_raw <- data_mentah$‘IR_USD_5Y‘
8 Z1 <- Y1_raw ˆ 0.5
9
10 Y2_raw <- data_mentah$‘IR_USD_10Y‘
```
11 Z2 <- (Y2_raw ˆ 0.5) ˆ 0.5
```
12
13 Y3_raw <- data_mentah$‘IR_USD_30Y‘
```
14 Z3 <- (Y3_raw ˆ -0.5) ˆ 0.5
```
15
16 Y4_raw <- data_mentah$‘IR_EUR_7Y‘
17 Z4 <- Y4_raw ˆ 0.5
18
19 Y5_raw <- data_mentah$‘IR_EUR_10Y‘
20 Z5 <- Y5_raw ˆ 0.5
21
22 Y6_raw <- data_mentah$‘IR_JPY_5Y‘
```
23 Z6 <- (log(Y6_raw) + 1) ˆ 0.5
```
24
25 Y7_raw <- data_mentah$‘IR_JPY_10Y‘
```
26 Z7 <- log(Y7_raw)
```
27
28 Y8_raw <- data_mentah$‘FX_USD_EUR‘
```
29 Z8 <- Y8_raw ˆ (-2)
```
30
31 Y9_raw <- data_mentah$‘FX_USD_JPY‘
```
32 Z9 <- Y9_raw ˆ (-3)
```
33
```
34 daftar_model <- list(
```
```
35 list(var = "IR_USD_5Y", max_lag = 1, trans = Z1, order = c(0, 1, 1), fixed = NULL, back_trans =
```
```
function(x) xˆ2),
```
```
36 list(var = "IR_USD_10Y", max_lag = 2, trans = Z2, order = c(1, 1, 0), fixed = NULL, back_trans =
```
```
function(x) xˆ4),
```
```
37 list(var = "IR_USD_30Y", max_lag = 4, trans = Z3, order = c(2, 2, 2), fixed = c(0, NA, NA, NA), back_
```
```
trans = function(x) xˆ(-4)),
```
```
38 list(var = "IR_EUR_7Y", max_lag = 1, trans = Z4, order = c(0, 1, 1), fixed = NULL, back_trans =
```
```
function(x) xˆ2),
```
```
39 list(var = "IR_EUR_10Y", max_lag = 1, trans = Z5, order = c(0, 1, 1), fixed = NULL, back_trans =
```
```
function(x) xˆ2),
```
```
40 list(var = "IR_JPY_5Y", max_lag = 2, trans = Z6, order = c(1, 1, 0), fixed = NULL, back_trans =
```
```
function(x) exp(xˆ2 - 1)),
```
```
41 list(var = "IR_JPY_10Y", max_lag = 14, trans = Z7, order = c(0, 1, 14), fixed = c(rep(0, 13), NA), back_
```
```
trans = function(x) exp(x)),
```
```
42 list(var = "FX_USD_EUR", max_lag = 1, trans = Z8, order = c(0, 1, 1), fixed = NULL, back_trans =
```
```
function(x) xˆ(-0.5)),
```
```
43 list(var = "FX_USD_JPY", max_lag = 1, trans = Z9, order = c(0, 1, 1), fixed = NULL, back_trans =
```
```
function(x) xˆ(-1/3))
```
```
44 )
```
45
46 n_train <- 80
```
47 n_total <- length(Z1)
```
48 h_future <- 12
```
49 h_forecast <- (n_total - n_train) + h_future
```
50
```
51 df_hasil <- data.frame(Periode = 1:(n_train + h_forecast))
```
52
```
53 for (m in daftar_model) {
```
54 trans_train <- m$trans[1:n_train]
55
```
56 fit <- tryCatch({
```
```
57 Arima(trans_train, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "ML")
```
```
58 }, error = function(e) {
```
115
```
59 Arima(trans_train, order = m$order, fixed = m$fixed, include.mean = FALSE, method = "CSS")
```
```
60 })
```
61
```
62 fitted_z <- as.numeric(fitted(fit))
```
63
```
64 if (m$max_lag > 0) {
```
65 fitted_z[1:m$max_lag] <- NA
```
66 }
```
67
```
68 fc_z <- as.numeric(suppressWarnings(forecast(fit, h = h_forecast)$mean))
```
```
69 combined_z <- c(fitted_z, fc_z)
```
```
70 combined_y <- m$back_trans(combined_z)
```
71
72 df_hasil[[m$var]] <- combined_y
```
73 }
```
74
```
75 cat("\n======================================================================\n")
```
```
76 cat(" HASIL PERAMALAN 12 PERIODE KEDEPAN")
```
```
77 cat("\n======================================================================\n\n")
```
78
79 df_cetak <- df_hasil[102:113, ]
80
```
81 df_cetak$IR_JPY_5Y <- sprintf("%.14f", df_cetak$IR_JPY_5Y)
```
```
82 df_cetak$FX_USD_EUR <- sprintf("%.6f", df_cetak$FX_USD_EUR)
```
```
83 df_cetak$FX_USD_JPY <- sprintf("%.6f", df_cetak$FX_USD_JPY)
```
84
```
85 print(df_cetak, row.names = FALSE)
```
116
Lampiran 8
Listing Program MATLAB untuk Perhitungan Matriks
Varians-Kovarians
```
1 clc; clear; close all;
```
2
3 %% MATRIKS VARIANS-KOVARIANS
4 % Lokasi file & path
```
5 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
6 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
7 full_path = fullfile(folder_path, nama_file);
```
8
9 %% DATA FORECAST
```
10 sheet_name = ’Perhitungan Forecast’;
```
```
11 nama_tabel = ’Table47’;
```
```
12 range_export = ’I126:O132’;
```
13
14 %% PROSES PERHITUNGAN & EKSPOR
15 % Kolom berurutan:
16 % C_USD_5Y, C_USD_10Y, C_USD_30Y, C_EUR_7Y, C_EUR_10Y, C_JPY_5Y, C_JPY_10Y
17
18 % Impor data tabel
```
19 T_ret = readtable(full_path, ...
```
20 ’Sheet’, sheet_name, ...
21 ’Range’, nama_tabel, ...
```
22 ’VariableNamingRule’, ’preserve’);
```
23
24 % Ambil data numerik dan hapus missing value
```
25 ret_data = rmmissing(T_ret{:, vartype(’numeric’)});
```
26
27 % Matriks Varians-Kovarians
```
28 cov_matrix = cov(ret_data);
```
29
30 % Ekspor hasil ke Excel
```
31 writematrix(cov_matrix, full_path, ...
```
32 ’Sheet’, sheet_name, ...
```
33 ’Range’, range_export);
```
34
35 % Tampilkan output matriks di terminal
```
36 fprintf(’\nMenampilkan Matriks Varians-Kovarians dari Sheet: %s\n’, sheet_name);
```
```
37 fprintf(’Diekspor ke Range: %s\n\n’, range_export);
```
38
```
39 for i = 1:size(cov_matrix, 1)
```
```
40 for j = 1:size(cov_matrix, 2)
```
```
41 fprintf(’%.18f ’, cov_matrix(i, j));
```
42 end
```
43 fprintf(’\n’);
```
44 end
117
Lampiran 9
Listing Program MATLAB untuk Perhitungan Nilai Rmax pada
Model CVaR
```
1 clc; clear; close all;
```
```
2 format long g;
```
3 %% 1. Impor Data Excel
```
4 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
5 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
6 full_path = fullfile(folder_path, nama_file);
```
```
7 T_ret = readtable(full_path, ’Sheet’, ’Perhitungan Forecast’, ’Range’, ’Table47’, ’VariableNamingRule’, ’
```
```
preserve’);
```
```
8 ret_data = rmmissing(T_ret{:, vartype(’numeric’)});
```
```
9 q = size(ret_data, 1);
```
10 %% 2. Definisi Bobot Portofolio
```
11 x_eksisting = [0.459485835; 0.113620854; 0.147798763; 0.143927407; 0.024401992; 0.066688212; 0.044076937];
```
```
12 x_merata = ones(7, 1) / 7;
```
```
13 portfolios = {x_eksisting, x_merata};
```
```
14 port_names = {’PORTOFOLIO EKSISTING (2024)’, ’PORTOFOLIO MERATA’};
```
15 %% 3. Evaluasi Risiko untuk Setiap Portofolio
```
16 beta_cases = [0.90, 0.95, 0.99];
```
```
17 options = optimoptions(’linprog’, ’Display’, ’off’);
```
```
18 for p_idx = 1:length(portfolios)
```
```
19 x_current = portfolios{p_idx};
```
```
20 name_current = port_names{p_idx};
```
21
```
22 R_port = ret_data * x_current;
```
23
```
24 fprintf(’\n====================================================================\n’);
```
```
25 fprintf(’ %s \n’, name_current);
```
```
26 fprintf(’====================================================================\n’);
```
```
27 fprintf(’Ekspektasi Perubahan Biaya Utang : %.18f\n’, mean(R_port));
```
```
28 fprintf(’--------------------------------------------------------------------\n’);
```
```
29 Aineq = [-ones(q, 1), -eye(q)];
```
```
30 bineq = -R_port;
```
```
31 LB = [-Inf; zeros(q, 1)];
```
```
32 for b_idx = 1:length(beta_cases)
```
```
33 beta_conf = beta_cases(b_idx);
```
```
34 f_obj = [1; (1 / (q * (1 - beta_conf))) * ones(q, 1)];
```
35
```
36 [v_opt, fval, exitflag] = linprog(f_obj, Aineq, bineq, [], [], LB, [], options);
```
37
38 if exitflag > 0
```
39 alpha_opt = v_opt(1);
```
```
40 cvar_opt = fval;
```
41
```
42 fprintf(’>> KASUS BETA = %g%% (%.2f) <<\n’, beta_conf * 100, beta_conf);
```
```
43 fprintf(’Value-at-Risk (VaR) / Alpha : %.18f\n’, alpha_opt);
```
```
44 fprintf(’Conditional VaR (CVaR) : %.18f\n’, cvar_opt);
```
```
45 fprintf(’--------------------------------------------------------------------\n’);
```
46 end
47 end
48 end
```
49 fprintf(’====================================================================\n’);
```
118
Lampiran 10
Listing Program MATLAB untuk Perhitungan CVaR
Portofolio Aktual
```
1 clc; clear; close all;
```
```
2 format long g;
```
3
4 %% ===== CONFIGURATION & PATH =====
```
5 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
6 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
7 full_path = fullfile(folder_path, nama_file);
```
8
```
9 x_eksisting = [0.459485835; 0.113620854; 0.147798763; 0.143927407; 0.024401992; 0.066688212; 0.044076937];
```
```
10 beta_cases = [0.90, 0.95, 0.99];
```
```
11 options = optimoptions(’linprog’, ’Display’, ’off’);
```
12
13 %% ===== DEFINISI SKENARIO DATA =====
```
14 scenarios = {
```
```
15 struct(’name’, ’DATA HISTORIS’, ’sheet’, ’Perhitungan Forecast’, ’range’, ’Table47’), ...
```
```
16 struct(’name’, ’GABUNGAN HISTORIS & FORECAST’, ’sheet’, ’Perhitungan Forecast’, ’range’, ’Table47’)
```
```
17 };
```
18
19 %% ===== PERHITUNGAN CVaR =====
```
20 for s_idx = 1:length(scenarios)
```
```
21 scen = scenarios{s_idx};
```
22
23 % Impor data berdasarkan skenario aktif
```
24 T_ret = readtable(full_path, ’Sheet’, scen.sheet, ’Range’, scen.range, ’VariableNamingRule’, ’preserve’
```
```
);
```
```
25 ret_data = rmmissing(T_ret{:, vartype(’numeric’)});
```
```
26 q = size(ret_data, 1);
```
27
28 % Return Portofolio Eksisting
```
29 R_port = ret_data * x_eksisting;
```
30
```
31 fprintf(’====================================================================\n’);
```
```
32 fprintf(’ SKENARIO: %s \n’, scen.name);
```
```
33 fprintf(’====================================================================\n’);
```
34
```
35 % Setup Linear Programming (CVaR)
```
```
36 Aineq = [-ones(q, 1), -eye(q)];
```
```
37 bineq = -R_port;
```
```
38 LB = [-Inf; zeros(q, 1)];
```
39
```
40 for b_idx = 1:length(beta_cases)
```
```
41 beta_conf = beta_cases(b_idx);
```
```
42 f_obj = [1; (1 / (q * (1 - beta_conf))) * ones(q, 1)];
```
43
```
44 [˜, cvar_opt, exitflag] = linprog(f_obj, Aineq, bineq, [], [], LB, [], options);
```
45
46 if exitflag > 0
```
47 fprintf(’CVaR (%g%%) : %.18f\n’, beta_conf * 100, cvar_opt);
```
48 else
```
49 fprintf(’CVaR (%g%%) : Gagal menghitung\n’, beta_conf * 100);
```
50 end
51 end
```
52 fprintf(’====================================================================\n\n’);
```
53 end
119
Lampiran 11
Listing Program MATLAB untuk Model Mean-Variance
```
Optimization (MVO)
```
```
1 clc; clear; close all;
```
```
2 format long g;
```
3
4 %% SETUP PATH EXCEL
```
5 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
6 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
7 full_path = fullfile(folder_path, nama_file);
```
8
```
9 asset_names = {’C_USD_5Y’, ’C_USD_10Y’, ’C_USD_30Y’, ...
```
```
10 ’C_EUR_7Y’, ’C_EUR_10Y’, ’C_JPY_5Y’, ’C_JPY_10Y’};
```
11
12 %% DATA GABUNGAN HISTORIS & FORECAST
```
13 nama_data = ’DATA GABUNGAN (HISTORIS + FORECAST)’;
```
```
14 sheet_export = ’Hasil Optimasi (2)’;
```
15
16 mu = [
```
17 0.000163792399765913;
```
```
18 0.000110177775619655;
```
```
19 0.000001379744806410;
```
```
20 0.000932492126516585;
```
```
21 0.000869169614771198;
```
```
22 0.002831172063030670;
```
23 0.002879522027475840
```
24 ];
```
25
26 Sigma = [
27 0.000006970413652417 0.000005595142001835 0.000004216836210849 0.000028588488162929
```
0.000027359207509166 0.000024097269845969 0.000023648643875350;
```
28 0.000005595142001835 0.000005618087029497 0.000004380873912749 0.000022069277343700
```
0.000021235456997016 0.000026485546617807 0.000026328836563041;
```
29 0.000004216836210849 0.000004380873912749 0.000003866458063852 0.000015076121824917
```
0.000014570856579239 0.000022179341644473 0.000022162889117657;
```
30 0.000028588488162929 0.000022069277343700 0.000015076121824917 0.000316361639308664
```
0.000311314788182334 0.000187060213839477 0.000184639820086248;
```
31 0.000027359207509166 0.000021235456997016 0.000014570856579239 0.000311314788182334
```
0.000307235262199714 0.000185555752488117 0.000183393357615938;
```
32 0.000024097269845969 0.000026485546617807 0.000022179341644473 0.000187060213839477
```
0.000185555752488117 0.000415252197984462 0.000414466028812572;
```
33 0.000023648643875350 0.000026328836563041 0.000022162889117657 0.000184639820086248
0.000183393357615938 0.000414466028812572 0.000414733134811496
```
34 ];
```
35
36 %% PILIH SKENARIO BATASAN
37
38 % --- [BATASAN 1] KEMENKEU ---
```
39 % nama_batasan = ’BATASAN KEMENKEU’;
```
```
40 % lb = [0.425; 0.100; 0.130; 0.130; 0.015; 0.050; 0.030];
```
```
41 % ub = [0.490; 0.125; 0.165; 0.155; 0.030; 0.085; 0.055];
```
```
42 % range_export = ’C3’;
```
43
44 % --- [BATASAN 2] DIPERLEBAR 5% ---
```
45 % nama_batasan = ’BATASAN DIPERLEBAR 5%’;
```
```
46 % lb = [0.436511543250; 0.107939811300; 0.140408824850; 0.136731036650; 0.023181892400; 0.063353801400;
```
```
0.041873090150];
```
```
47 % ub = [0.482460126750; 0.119301896700; 0.155188701150; 0.151123777350; 0.025622091600; 0.070022622600;
```
```
0.046280783850];
```
```
48 % range_export = ’C17’;
```
49
50 % --- [BATASAN 3] TANPA BATASAN ---
```
51 nama_batasan = ’TANPA BATASAN (0 s.d 1)’;
```
```
52 lb = zeros(7, 1);
```
```
53 ub = ones(7, 1);
```
```
54 range_export = ’C31’;
```
55
56 %% SETUP MVO
120
```
57 Aeq = ones(1, 7);
```
```
58 beq = 1;
```
59
```
60 x0 = lb + (ub - lb)/2;
```
61
```
62 options = optimoptions(’fmincon’, ...
```
63 ’Display’, ’off’, ...
64 ’Algorithm’, ’sqp’, ...
```
65 ’ConstraintTolerance’, 1e-10);
```
66
67 %% PARAMETER ITERASI Rmax
68 Rmax_vector = [
```
69 0.000033683544775466;
```
```
70 0.000101609932479855;
```
```
71 0.011305009399949160;
```
```
72 0.012714094856730768;
```
```
73 0.016989970809430918;
```
```
74 0.018880495149667626;
```
```
75 0.022423957171019273;
```
76 0.028964586540561284
```
77 ];
```
78
```
79 num_scenarios = length(Rmax_vector);
```
```
80 export_data = cell(12, num_scenarios);
```
81
```
82 fprintf(’\n====================================================================\n’);
```
```
83 fprintf(’ MVO | DATA: %s | %s \n’, nama_data, nama_batasan);
```
```
84 fprintf(’====================================================================\n’);
```
85
86 %% PROSES OPTIMASI
87 for iter = 1:num_scenarios
```
88 Rmax_current = Rmax_vector(iter);
```
```
89 export_data{1, iter} = Rmax_current;
```
90
```
91 objFun = @(x) mu’ * x;
```
```
92 nonlcon = @(x) deal(x’ * Sigma * x - Rmax_current, []);
```
93
```
94 [x_opt, fval, exitflag] = fmincon(objFun, x0, [], [], Aeq, beq, lb, ub, nonlcon, options);
```
95
96 if exitflag > 0
```
97 risiko_varians = x_opt’ * Sigma * x_opt;
```
```
98 risiko_std = sqrt(risiko_varians);
```
```
99 expected_cost = mu’ * x_opt;
```
100
101 for j = 1:7
```
102 export_data{1+j, iter} = x_opt(j);
```
103 end
104
```
105 export_data{9, iter} = exitflag;
```
```
106 export_data{10, iter} = expected_cost;
```
```
107 export_data{11, iter} = risiko_varians;
```
```
108 export_data{12, iter} = risiko_std;
```
109
```
110 fprintf(’>> SKENARIO RMAX = %.18f <<\n\n’, Rmax_current);
```
```
111 fprintf(’ %-13s %-20s %-20s %-20s\n’, ’Aset’, ’Bobot’, ’LB’, ’UB’);
```
```
112 fprintf(’ _____________ ____________________ ____________________ ____________________\n\n’);
```
113
114 for j = 1:7
```
115 fprintf(’ %-13s %.18f %.18f %.18f\n’, asset_names{j}, x_opt(j), lb(j), ub(j));
```
116 end
117
```
118 fprintf(’\n--------------------------------------------------------------------\n’);
```
```
119 fprintf(’ExitFlag = %d\n’, exitflag);
```
```
120 fprintf(’EKSP. PERUBAHAN BIAYA= %.18f\n’, expected_cost);
```
```
121 fprintf(’RISIKO (Varians) = %.18f\n’, risiko_varians);
```
```
122 fprintf(’RISIKO (Std Dev) = %.18f\n’, risiko_std);
```
```
123 fprintf(’====================================================================\n’);
```
124 else
125 for j = 1:7
```
126 export_data{1+j, iter} = ’TM’;
```
127 end
128
121
```
129 export_data{9, iter} = exitflag;
```
```
130 export_data{10, iter} = ’TM’;
```
```
131 export_data{11, iter} = ’TM’;
```
```
132 export_data{12, iter} = ’TM’;
```
133
```
134 fprintf(’>> SKENARIO RMAX = %.18f <<\n\n’, Rmax_current);
```
```
135 fprintf(’TIDAK ADA SOLUSI YANG MEMENUHI (ExitFlag: %d)\n’, exitflag);
```
```
136 fprintf(’====================================================================\n’);
```
137 end
138 end
139
140 %% EKSPOR KE EXCEL
```
141 writecell(export_data, full_path, ’Sheet’, sheet_export, ’Range’, range_export);
```
142
```
143 fprintf(’\n>>> Data berhasil diekspor ke Excel! <<<\n’);
```
```
144 fprintf(’Sheet: %s | Range Sel: %s\n\n’, sheet_export, range_export);
```
122
Lampiran 12
Listing Program MATLAB untuk Model Conditional Value at
```
Risk (CVaR)
```
```
1 clc; clear; close all;
```
```
2 format long g;
```
3
4 %% SETUP PATH EXCEL
```
5 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
6 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
7 full_path = fullfile(folder_path, nama_file);
```
8
```
9 asset_names = {’C_USD_5Y’, ’C_USD_10Y’, ’C_USD_30Y’, ...
```
```
10 ’C_EUR_7Y’, ’C_EUR_10Y’, ’C_JPY_5Y’, ’C_JPY_10Y’};
```
11
12 %% DATA GABUNGAN HISTORIS & FORECAST
```
13 nama_data = ’DATA GABUNGAN (HISTORIS + FORECAST)’;
```
```
14 sheet_read = ’Perhitungan Forecast’;
```
```
15 table_read = ’Table47’;
```
```
16 sheet_export = ’Hasil Optimasi (2)’;
```
17
18 %% BACA DATA
```
19 T_ret = readtable(full_path, ...
```
20 ’Sheet’, sheet_read, ...
21 ’Range’, table_read, ...
```
22 ’VariableNamingRule’, ’preserve’);
```
23
```
24 ret_data = rmmissing(T_ret{:, vartype(’numeric’)});
```
25
```
26 mu = mean(ret_data)’;
```
```
27 q = size(ret_data, 1);
```
```
28 n_assets = 7;
```
29
30 %% PILIH SKENARIO BATASAN
31
32 % --- [BATASAN 1] KEMENKEU ---
```
33 % nama_batasan = ’BATASAN KEMENKEU’;
```
```
34 % lb_x = [0.425; 0.100; 0.130; 0.130; 0.015; 0.050; 0.030];
```
```
35 % ub_x = [0.490; 0.125; 0.165; 0.155; 0.030; 0.085; 0.055];
```
```
36 % target_cells = {’N4’, ’N17’, ’N30’};
```
37
38 % --- [BATASAN 2] DIPERLEBAR 5% ---
```
39 % nama_batasan = ’BATASAN DIPERLEBAR 5%’;
```
```
40 % lb_x = [0.436511543250; 0.107939811300; 0.140408824850; 0.136731036650; 0.023181892400; 0.063353801400;
```
```
0.041873090150];
```
```
41 % ub_x = [0.482460126750; 0.119301896700; 0.155188701150; 0.151123777350; 0.025622091600; 0.070022622600;
```
```
0.046280783850];
```
```
42 % target_cells = {’X4’, ’X17’, ’X30’};
```
43
44 % --- [BATASAN 3] TANPA BATASAN ---
```
45 nama_batasan = ’TANPA BATASAN (0 s.d 1)’;
```
```
46 lb_x = zeros(7, 1);
```
```
47 ub_x = ones(7, 1);
```
```
48 target_cells = {’AH4’, ’AH17’, ’AH30’};
```
49
50 %% SETUP LINEAR PROGRAMMING
```
51 f_cost = [mu; 0; zeros(q, 1)];
```
52
```
53 Aeq = [ones(1, n_assets), 0, zeros(1, q)];
```
```
54 beq = 1;
```
55
```
56 Aineq_u = [ret_data, -ones(q, 1), -eye(q)];
```
```
57 bineq_u = zeros(q, 1);
```
58
```
59 LB = [lb_x; -Inf; zeros(q, 1)];
```
```
60 UB = [ub_x; Inf; inf(q, 1)];
```
61
```
62 options = optimoptions(’linprog’, ’Display’, ’off’);
```
63
123
64 %% PARAMETER ITERASI Rmax
65 Rmax_vector = [
```
66 0.000033683544775466;
```
```
67 0.000101609932479855;
```
```
68 0.011305009399949160;
```
```
69 0.012714094856730768;
```
```
70 0.016989970809430918;
```
```
71 0.018880495149667626;
```
```
72 0.022423957171019273;
```
73 0.028964586540561284
```
74 ];
```
75
```
76 beta_cases = [0.90, 0.95, 0.99];
```
77
78 %% PROSES OPTIMASI
```
79 for b_idx = 1:length(beta_cases)
```
```
80 beta_conf = beta_cases(b_idx);
```
81
```
82 f_cvar = [zeros(n_assets, 1); ...
```
```
83 1; ...
```
```
84 (1/(q*(1-beta_conf))) * ones(q, 1)];
```
85
```
86 fprintf(’\n====================================================================\n’);
```
```
87 fprintf(’ CVaR | BETA %g%% | %s | %s \n’, beta_conf * 100, nama_data, nama_batasan);
```
```
88 fprintf(’====================================================================\n’);
```
89
```
90 excel_output = cell(12, length(Rmax_vector));
```
91
```
92 for iter = 1:length(Rmax_vector)
```
```
93 Rmax_current = Rmax_vector(iter);
```
```
94 excel_output{1, iter} = Rmax_current;
```
95
```
96 Aineq_limit = [zeros(1, n_assets), ...
```
97 1, ...
```
98 (1/(q*(1-beta_conf))) * ones(1, q)];
```
```
99 bineq_limit = Rmax_current;
```
100
```
101 Aineq_total = [Aineq_u; Aineq_limit];
```
```
102 bineq_total = [bineq_u; bineq_limit];
```
103
```
104 [v_opt, ˜, exitflag] = linprog(f_cost, ...
```
105 Aineq_total, bineq_total, ...
106 Aeq, beq, ...
107 LB, UB, ...
```
108 options);
```
109
110 if exitflag > 0
```
111 x_opt = v_opt(1:7);
```
```
112 alpha_opt = v_opt(8);
```
```
113 cvar_aktual = f_cvar’ * v_opt;
```
```
114 expected_cost = mu’ * x_opt;
```
115
```
116 fprintf(’>> R_max = %.18f <<\n\n’, Rmax_current);
```
```
117 fprintf(’ %-13s %-20s %-20s %-20s\n’, ’Aset’, ’Bobot’, ’LB’, ’UB’);
```
```
118 fprintf(’ _____________ ____________________ ____________________ ____________________\n\n’
```
```
);
```
119
120 for j = 1:7
```
121 fprintf(’ %-13s %.18f %.18f %.18f\n’, ...
```
```
122 asset_names{j}, x_opt(j), lb_x(j), ub_x(j));
```
```
123 excel_output{1+j, iter} = x_opt(j);
```
124 end
125
```
126 fprintf(’\n--------------------------------------------------------------------\n’);
```
```
127 fprintf(’ExitFlag = %d\n’, exitflag);
```
```
128 fprintf(’EKSP. PERUBAHAN BIAYA= %.18f\n’, expected_cost);
```
```
129 fprintf(’RISIKO (CVaR) = %.18f\n’, cvar_aktual);
```
```
130 fprintf(’VaR (Alpha) = %.18f\n’, alpha_opt);
```
```
131 fprintf(’====================================================================\n’);
```
132
```
133 excel_output{9, iter} = exitflag;
```
```
134 excel_output{10, iter} = expected_cost;
```
124
```
135 excel_output{11, iter} = cvar_aktual;
```
```
136 excel_output{12, iter} = alpha_opt;
```
137 else
```
138 fprintf(’>> R_max = %.18f <<\n’, Rmax_current);
```
```
139 fprintf(’TIDAK ADA SOLUSI YANG MEMENUHI (ExitFlag: %d)\n’, exitflag);
```
```
140 fprintf(’====================================================================\n’);
```
141
142 for j = 1:7
```
143 excel_output{1+j, iter} = ’TM’;
```
144 end
145
```
146 excel_output{9, iter} = exitflag;
```
```
147 excel_output{10, iter} = ’TM’;
```
```
148 excel_output{11, iter} = ’TM’;
```
```
149 excel_output{12, iter} = ’TM’;
```
150 end
151 end
152
153 %% EKSPOR KE EXCEL
```
154 sel_target = target_cells{b_idx};
```
155
```
156 writecell(excel_output, ...
```
157 full_path, ...
158 ’Sheet’, sheet_export, ...
```
159 ’Range’, sel_target);
```
160
```
161 fprintf(’\n>>> Data BETA %g%% berhasil diekspor ke %s (Range: %s) <<<\n\n’, ...
```
```
162 beta_conf * 100, sheet_export, sel_target);
```
163 end
125
Lampiran 13
Listing Program MATLAB untuk Efficient Frontier Model
MVO
```
1 clc; clear; close all;
```
2
3 %% ===== DATA HISTORIS & FORECAST =====
```
4 nama_data = ’Historis & Forecast’;
```
5
6 mu = [
```
7 0.000163792399765913;
```
```
8 0.000110177775619655;
```
```
9 0.000001379744806410;
```
```
10 0.000932492126516585;
```
```
11 0.000869169614771198;
```
```
12 0.002831172063030670;
```
13 0.002879522027475840
```
14 ];
```
15
16 Sigma = [
17 0.000006970413652417 0.000005595142001835 0.000004216836210849 0.000028588488162929
```
0.000027359207509166 0.000024097269845969 0.000023648643875350;
```
18 0.000005595142001835 0.000005618087029497 0.000004380873912749 0.000022069277343700
```
0.000021235456997016 0.000026485546617807 0.000026328836563041;
```
19 0.000004216836210849 0.000004380873912749 0.000003866458063852 0.000015076121824917
```
0.000014570856579239 0.000022179341644473 0.000022162889117657;
```
20 0.000028588488162929 0.000022069277343700 0.000015076121824917 0.000316361639308664
```
0.000311314788182334 0.000187060213839477 0.000184639820086248;
```
21 0.000027359207509166 0.000021235456997016 0.000014570856579239 0.000311314788182334
```
0.000307235262199714 0.000185555752488117 0.000183393357615938;
```
22 0.000024097269845969 0.000026485546617807 0.000022179341644473 0.000187060213839477
```
0.000185555752488117 0.000415252197984462 0.000414466028812572;
```
23 0.000023648643875350 0.000026328836563041 0.000022162889117657 0.000184639820086248
0.000183393357615938 0.000414466028812572 0.000414733134811496
```
24 ];
```
25
```
26 assetNames = {’USD_5Y’,’USD_10Y’,’USD_30Y’,’EUR_7Y’,’EUR_10Y’,’JPY_5Y’,’JPY_10Y’};
```
```
27 n = length(mu);
```
28
29 %% ===== BATAS =====
30 % --- [BATASAN 1] KEMENKEU ---
```
31 nama_batasan = ’Kemenkeu’;
```
```
32 lb = [0.425; 0.100; 0.130; 0.130; 0.015; 0.050; 0.030];
```
```
33 ub = [0.490; 0.125; 0.165; 0.155; 0.030; 0.085; 0.055];
```
34
35 % --- [BATASAN 2] DIPERLEBAR 5% ---
```
36 % nama_batasan = ’Diperlebar 5%’;
```
```
37 % lb = [0.436511543250; 0.107939811300; 0.140408824850; 0.136731036650; 0.023181892400; 0.063353801400;
```
```
0.041873090150];
```
```
38 % ub = [0.482460126750; 0.119301896700; 0.155188701150; 0.151123777350; 0.025622091600; 0.070022622600;
```
```
0.046280783850];
```
39
40 % --- [BATASAN 3] TANPA BATASAN ---
```
41 % nama_batasan = ’Tanpa Batasan’;
```
```
42 % lb = zeros(n, 1);
```
```
43 % ub = ones(n, 1);
```
44
45 %% ===== TITIK AWAL =====
```
46 capacity = ub - lb;
```
```
47 remaining = 1 - sum(lb);
```
```
48 x0 = lb + capacity * (remaining / sum(capacity));
```
```
49 x0 = x0 / sum(x0);
```
50
51 %% ===== FUNGSI MODEL MVO =====
```
52 cost_fun = @(x) mu’ * x;
```
```
53 r_fun = @(x) x’ * Sigma * x;
```
54
55 %% ===== OPTIONS =====
```
56 options = optimoptions(’fmincon’, ...
```
126
57 ’Display’, ’none’, ...
58 ’Algorithm’, ’sqp’, ...
59 ’OptimalityTolerance’, 1e-15, ...
60 ’ConstraintTolerance’, 1e-15, ...
```
61 ’MaxIterations’, 2000000);
```
62
```
63 Aeq = ones(1, n);
```
```
64 beq = 1;
```
65
66 %% ===== TENTUKAN RANGE VARIANS =====
67 % Titik A: Portofolio Risiko Minimum
```
68 [wA, ˜, efA] = fmincon(r_fun, x0, [], [], Aeq, beq, lb, ub, [], options);
```
69
70 % Titik B: Portofolio Biaya Minimum
```
71 [wB, ˜, efB] = fmincon(cost_fun, x0, [], [], Aeq, beq, lb, ub, [], options);
```
72
73 if efA <= 0 || efB <= 0
```
74 error(’Titik ekstrem tidak feasible. Periksa lb/ub.’);
```
75 end
76
```
77 Rmax_min = r_fun(wA);
```
```
78 Rmax_max = r_fun(wB);
```
79
```
80 fprintf(’=== Parameter Model MVO (%s - %s) ===\n’, nama_data, nama_batasan);
```
```
81 fprintf(’Batas Bawah Risiko : %.18f\n’, Rmax_min);
```
```
82 fprintf(’Batas Atas Risiko : %.18f\n\n’, Rmax_max);
```
83
84 %% ===== LOOP EFFICIENT FRONTIER =====
```
85 nFront = 1000;
```
```
86 TargetRisiko = linspace(Rmax_min, Rmax_max, nFront);
```
```
87 risiko_frontier = zeros(nFront, 1);
```
```
88 biaya_frontier = zeros(nFront, 1);
```
```
89 bobot_frontier = zeros(n, nFront);
```
```
90 exitflags = zeros(nFront, 1);
```
91
```
92 w_prev = wA;
```
93
94 for i = 1:nFront
```
95 Rmax = TargetRisiko(i);
```
96
```
97 % Kendala: varians(x) <= Rmax
```
```
98 nonlcon = @(x) deal(r_fun(x) - Rmax, []);
```
99
```
100 [x_opt, ˜, ef] = fmincon(cost_fun, w_prev, [], [], Aeq, beq, lb, ub, nonlcon, options);
```
```
101 exitflags(i) = ef;
```
102
103 if ef > 0
```
104 bobot_frontier(:, i) = x_opt;
```
```
105 biaya_frontier(i) = cost_fun(x_opt);
```
```
106 risiko_frontier(i) = r_fun(x_opt);
```
```
107 w_prev = x_opt;
```
108 else
```
109 bobot_frontier(:, i) = NaN(n, 1);
```
```
110 biaya_frontier(i) = NaN;
```
```
111 risiko_frontier(i) = NaN;
```
112 end
113 end
114
```
115 valid = exitflags > 0;
```
```
116 fprintf(’Titik valid: %d / %d\n\n’, sum(valid), nFront);
```
117
118 %% ===== KONVERSI UNTUK PLOT =====
```
119 ret_frontier = biaya_frontier;
```
120
121 %% ===== GRAFIK EFFICIENT FRONTIER =====
```
122 judul_plot = sprintf(’MVO - %s - %s’, nama_data, nama_batasan);
```
123
```
124 figure(’Name’, judul_plot, ’NumberTitle’, ’off’, ’Color’, ’w’);
```
125
```
126 plot(sqrt(risiko_frontier(valid)), biaya_frontier(valid), ’b-’, ’LineWidth’, 2);
```
```
127 hold on;
```
128
127
```
129 rsk_v = sqrt(risiko_frontier(valid));
```
```
130 cost_v = biaya_frontier(valid);
```
131
132 % Titik Min Risiko
```
133 [˜, idx_minV] = min(rsk_v);
```
```
134 plot(rsk_v(idx_minV), cost_v(idx_minV), ’ro’, ...
```
135 ’MarkerSize’, 10, ...
```
136 ’MarkerFaceColor’, ’r’);
```
137
```
138 xlabel(’Risk (Standard Deviation)’);
```
```
139 ylabel(’Ekspektasi Perubahan Biaya Utang’);
```
```
140 title(judul_plot);
```
```
141 legend(’Frontier’, ’Batas Bawah Risiko’, ’Location’, ’best’);
```
```
142 grid on;
```
143
144 %% ===== TABEL KOMPOSISI SEMUA TITIK =====
```
145 fprintf(’=== Komposisi Bobot Seluruh Titik Frontier ===\n\n’);
```
146
```
147 fprintf(’%-6s’, ’Titik’);
```
148 for j = 1:n
```
149 fprintf(’ %-20s’, assetNames{j});
```
150 end
```
151 fprintf(’ %-22s %-22s %-22s\n’, ...
```
```
152 ’Variance’, ’Std Dev’, ’Eksp.Perubahan Biaya Utang’);
```
153
```
154 fprintf(’%s\n’, repmat(’-’, 1, 6 + n*22 + 70));
```
155
156 for i = 1:nFront
```
157 if exitflags(i) > 0
```
```
158 fprintf(’%-6d’, i);
```
159 for j = 1:n
```
160 fprintf(’ %-20.18f’, bobot_frontier(j, i));
```
161 end
```
162 fprintf(’ %-22.18f %-22.18f %-22.18f\n’, ...
```
```
163 risiko_frontier(i), ...
```
```
164 sqrt(risiko_frontier(i)), ...
```
```
165 ret_frontier(i));
```
166 end
167 end
168
169 %% ===== TITIK KUNCI =====
```
170 idx_valid = find(valid);
```
```
171 nv = length(idx_valid);
```
```
172 idx_key = idx_valid(round(linspace(1, nv, 5)));
```
```
173 key_labels = {’MinVar’,’Q25’,’Q50’,’Q75’,’MaxReturn’};
```
174
```
175 fprintf(’\n=== Ringkasan Titik Kunci ===\n’);
```
176
```
177 fprintf(’%-12s’, ’Metric’);
```
178 for k = 1:5
```
179 fprintf(’ %-20s’, key_labels{k});
```
180 end
181
```
182 fprintf(’\n%s\n’, repmat(’-’, 1, 12 + 5*22));
```
183
184 for j = 1:n
```
185 fprintf(’%-12s’, assetNames{j});
```
186 for k = 1:5
```
187 fprintf(’ %-20.18f’, bobot_frontier(j, idx_key(k)));
```
188 end
```
189 fprintf(’\n’);
```
190 end
191
```
192 fprintf(’%-12s’, ’Variance’);
```
193 for k = 1:5
```
194 fprintf(’ %-20.18f’, risiko_frontier(idx_key(k)));
```
195 end
196
```
197 fprintf(’\n%-12s’, ’Std Dev’);
```
198 for k = 1:5
```
199 fprintf(’ %-20.18f’, sqrt(risiko_frontier(idx_key(k))));
```
200 end
128
201
```
202 fprintf(’\n%-12s’, ’Exp.Return’);
```
203 for k = 1:5
```
204 fprintf(’ %-20.18f’, ret_frontier(idx_key(k)));
```
205 end
206
```
207 fprintf(’\n’);
```
129
Lampiran 14
Listing Program MATLAB untuk Efficient Frontier Model
CVaR
```
1 clc; clear; close all;
```
```
2 format long g;
```
3
4 %% ===== DATA HISTORIS & FORECAST =====
```
5 nama_data = ’Historis & Forecast’;
```
```
6 sheet_data = ’Perhitungan Forecast’;
```
```
7 table_data = ’Table47’;
```
8
9 %% ===== IMPORT DATA =====
```
10 folder_path = ’E:\KULIAH\Kebutuhan TA\Data Set’;
```
```
11 nama_file = ’Data Optimum Utang Valas 2014 - 2025.xlsx’;
```
```
12 full_path = fullfile(folder_path, nama_file);
```
13
```
14 T_ret = readtable(full_path, ...
```
15 ’Sheet’, sheet_data, ...
16 ’Range’, table_data, ...
```
17 ’VariableNamingRule’, ’preserve’);
```
18
```
19 ret_data = rmmissing(T_ret{:, vartype(’numeric’)});
```
20
```
21 q = size(ret_data, 1);
```
22
```
23 assetNames = {’USD_5Y’,’USD_10Y’,’USD_30Y’,’EUR_7Y’,’EUR_10Y’,’JPY_5Y’,’JPY_10Y’};
```
24
```
25 mu = mean(ret_data)’;
```
```
26 n = length(mu);
```
27
```
28 %% ===== PILIH PARAMETER CVaR (BETA) =====
```
29 % Aktifkan salah satu nilai beta, comment yang lainnya
```
30 beta_conf = 0.90;
```
```
31 % beta_conf = 0.95;
```
```
32 % beta_conf = 0.99;
```
33
34 %% ===== PILIH SKENARIO BATASAN =====
35
36 % --- [BATASAN 1] KEMENKEU ---
```
37 nama_batasan = ’Kemenkeu’;
```
```
38 lb = [0.425; 0.100; 0.130; 0.130; 0.015; 0.050; 0.030];
```
```
39 ub = [0.490; 0.125; 0.165; 0.155; 0.030; 0.085; 0.055];
```
40
41 % --- [BATASAN 2] DIPERLEBAR 5% ---
```
42 % nama_batasan = ’Diperlebar 5%’;
```
```
43 % lb = [0.436511543250; 0.107939811300; 0.140408824850; 0.136731036650; 0.023181892400; 0.063353801400;
```
```
0.041873090150];
```
```
44 % ub = [0.482460126750; 0.119301896700; 0.155188701150; 0.151123777350; 0.025622091600; 0.070022622600;
```
```
0.046280783850];
```
45
46 % --- [BATASAN 3] TANPA BATASAN ---
```
47 % nama_batasan = ’Tanpa Batasan’;
```
```
48 % lb = zeros(n, 1);
```
```
49 % ub = ones(n, 1);
```
50
```
51 %% ===== SETUP LINEAR PROGRAMMING (CVaR) =====
```
52 % Vektor variabel: [x1...xn, alpha, u1...uq]
53 % Total variabel = n + 1 + q
54
55 % Fungsi Objektif: Expected Cost
```
56 f_cost = [mu; 0; zeros(q, 1)];
```
57
58 % Fungsi Objektif: CVaR
```
59 f_cvar = [zeros(n, 1); 1; (1 / (q * (1 - beta_conf))) * ones(q, 1)];
```
60
61 % Kendala Persamaan: Total Bobot = 1
```
62 Aeq = [ones(1, n), 0, zeros(1, q)];
```
```
63 beq = 1;
```
130
64
65 % Kendala Pertidaksamaan:
66 % -R*x - alpha - u <= 0
67 % u >= -R*x - alpha
```
68 Aineq_base = [-ret_data, -ones(q, 1), -eye(q)];
```
```
69 bineq_base = zeros(q, 1);
```
70
71 % Batas bawah dan atas
```
72 LB = [lb; -Inf; zeros(q, 1)];
```
```
73 UB = [ub; Inf; inf(q, 1)];
```
74
```
75 options = optimoptions(’linprog’, ’Display’, ’none’);
```
76
77 %% ===== TENTUKAN RANGE CVaR =====
78 % Titik A: Portofolio Risiko Minimum
```
79 [vA, ˜, exitA] = linprog(f_cvar, Aineq_base, bineq_base, Aeq, beq, LB, UB, options);
```
80
81 % Titik B: Portofolio Biaya Minimum
```
82 [vB, ˜, exitB] = linprog(f_cost, Aineq_base, bineq_base, Aeq, beq, LB, UB, options);
```
83
84 if exitA <= 0 || exitB <= 0
```
85 error(’Titik ekstrem tidak feasible. Periksa lb/ub.’);
```
86 end
87
```
88 CVaR_min = f_cvar’ * vA;
```
```
89 CVaR_max = f_cvar’ * vB;
```
90
```
91 fprintf(’=== Parameter Model CVaR (%g%% - %s - %s) ===\n’, beta_conf*100, nama_data, nama_batasan);
```
```
92 fprintf(’Batas Bawah Risiko : %.18f\n’, CVaR_min);
```
```
93 fprintf(’Batas Atas Risiko : %.18f\n\n’, CVaR_max);
```
94
95 %% ===== LOOP EFFICIENT FRONTIER =====
```
96 nFront = 1000;
```
```
97 TargetRisiko = linspace(CVaR_min, CVaR_max, nFront);
```
```
98 risiko_frontier = zeros(nFront, 1);
```
```
99 VaR_frontier = zeros(nFront, 1);
```
```
100 biaya_frontier = zeros(nFront, 1);
```
```
101 bobot_frontier = zeros(n, nFront);
```
```
102 exitflags = zeros(nFront, 1);
```
103
104 for i = 1:nFront
```
105 Cmax = TargetRisiko(i);
```
106
107 % Kendala: CVaR <= Cmax
```
108 A_cvar_limit = [zeros(1, n), 1, (1 / (q * (1 - beta_conf))) * ones(1, q)];
```
```
109 b_cvar_limit = Cmax;
```
110
```
111 Aineq_total = [Aineq_base; A_cvar_limit];
```
```
112 bineq_total = [bineq_base; b_cvar_limit];
```
113
```
114 [v_opt, fval, ef] = linprog(f_cost, Aineq_total, bineq_total, Aeq, beq, LB, UB, options);
```
```
115 exitflags(i) = ef;
```
116
117 if ef > 0
```
118 x_opt = v_opt(1:n);
```
```
119 alpha_opt = v_opt(n+1);
```
120
```
121 bobot_frontier(:, i) = x_opt;
```
```
122 biaya_frontier(i) = fval;
```
```
123 risiko_frontier(i) = f_cvar’ * v_opt;
```
```
124 VaR_frontier(i) = alpha_opt;
```
125 else
```
126 bobot_frontier(:, i) = NaN(n, 1);
```
```
127 biaya_frontier(i) = NaN;
```
```
128 risiko_frontier(i) = NaN;
```
```
129 VaR_frontier(i) = NaN;
```
130 end
131 end
132
```
133 valid = exitflags > 0;
```
```
134 fprintf(’Titik valid: %d / %d\n\n’, sum(valid), nFront);
```
135
131
136 %% ===== KONVERSI UNTUK PLOT =====
```
137 ret_frontier = biaya_frontier;
```
138
```
139 rsk_v = risiko_frontier(valid);
```
```
140 cost_v = biaya_frontier(valid);
```
141
142 % Urutkan data berdasarkan risiko
```
143 [rsk_sorted, sort_idx] = sort(rsk_v);
```
```
144 cost_sorted = cost_v(sort_idx);
```
145
146 % Filter monotonitas
```
147 for k = 2:length(cost_sorted)
```
```
148 if cost_sorted(k) > cost_sorted(k-1)
```
```
149 cost_sorted(k) = cost_sorted(k-1);
```
150 end
151 end
152
153 %% ===== GRAFIK EFFICIENT FRONTIER =====
```
154 judul_plot = sprintf(’CVaR (%g%%) - %s - %s’, beta_conf*100, nama_data, nama_batasan);
```
155
```
156 figure(’Name’, judul_plot, ’NumberTitle’, ’off’, ’Color’, ’w’);
```
157
```
158 plot(rsk_sorted, cost_sorted, ’b-’, ’LineWidth’, 2);
```
```
159 hold on;
```
160
161 % Titik Min Risiko
```
162 plot(rsk_sorted(1), cost_sorted(1), ’ro’, ...
```
163 ’MarkerSize’, 10, ...
```
164 ’MarkerFaceColor’, ’r’);
```
165
```
166 xlabel(sprintf(’Risk (CVaR %g%%)’, beta_conf*100));
```
```
167 ylabel(’Ekspektasi Perubahan Biaya Utang’);
```
```
168 title(judul_plot);
```
```
169 legend(’Frontier’, ’Batas Bawah Risiko’, ’Location’, ’best’);
```
```
170 grid on;
```
171
```
172 ax = gca;
```
```
173 ax.YAxis.ExponentMode = ’auto’;
```
```
174 ax.XAxis.ExponentMode = ’auto’;
```
```
175 ytickformat(’%.18f’);
```
176
177 %% ===== TABEL KOMPOSISI SEMUA TITIK =====
```
178 fprintf(’=== Komposisi Bobot Seluruh Titik Frontier ===\n\n’);
```
179
```
180 fprintf(’%-6s’, ’Titik’);
```
181 for j = 1:n
```
182 fprintf(’ %-20s’, assetNames{j});
```
183 end
```
184 fprintf(’ %-22s %-22s %-22s\n’, ...
```
```
185 ’CVaR’, ’VaR (Alpha)’, ’Eksp.Perubahan Biaya Utang’);
```
186
```
187 fprintf(’%s\n’, repmat(’-’, 1, 6 + n*22 + 70));
```
188
189 for i = 1:nFront
```
190 if exitflags(i) > 0
```
```
191 fprintf(’%-6d’, i);
```
192 for j = 1:n
```
193 fprintf(’ %-20.18f’, bobot_frontier(j, i));
```
194 end
```
195 fprintf(’ %-22.18f %-22.18f %-22.18f\n’, ...
```
```
196 risiko_frontier(i), ...
```
```
197 VaR_frontier(i), ...
```
```
198 ret_frontier(i));
```
199 end
200 end
201
202 %% ===== TITIK KUNCI =====
```
203 idx_valid = find(valid);
```
```
204 nv = length(idx_valid);
```
```
205 idx_key = idx_valid(round(linspace(1, nv, 5)));
```
```
206 key_labels = {’MinRisk’,’Q25’,’Q50’,’Q75’,’MinCost’};
```
207
132
```
208 fprintf(’\n=== Ringkasan Titik Kunci ===\n’);
```
209
```
210 fprintf(’%-12s’, ’Metric’);
```
211 for k = 1:5
```
212 fprintf(’ %-20s’, key_labels{k});
```
213 end
214
```
215 fprintf(’\n%s\n’, repmat(’-’, 1, 12 + 5*22));
```
216
217 for j = 1:n
```
218 fprintf(’%-12s’, assetNames{j});
```
219 for k = 1:5
```
220 fprintf(’ %-20.18f’, bobot_frontier(j, idx_key(k)));
```
221 end
```
222 fprintf(’\n’);
```
223 end
224
```
225 fprintf(’%-12s’, ’CVaR’);
```
226 for k = 1:5
```
227 fprintf(’ %-20.18f’, risiko_frontier(idx_key(k)));
```
228 end
229
```
230 fprintf(’\n%-12s’, ’VaR (Alpha)’);
```
231 for k = 1:5
```
232 fprintf(’ %-20.18f’, VaR_frontier(idx_key(k)));
```
233 end
234
```
235 fprintf(’\n%-12s’, ’Exp.Cost’);
```
236 for k = 1:5
```
237 fprintf(’ %-20.18f’, ret_frontier(idx_key(k)));
```
238 end
239
```
240 fprintf(’\n’);
```
133
Lampiran 15
Data Deret Waktu Suku Bunga dan Nilai Tukar Mata Uangt
Periode

IR
1,t

IR
2,t

IR
3,t

IR
4,t

IR
5,t

IR
6,t

IR
7,t

F X
1,t

F X
2,t
1
Jul-17

3.105857143
3.736238095
4.710809524
1.865047619
2.737619048
0.860142857
0.836238095
0.867418361
112.417000000
2
Aug-17
2.934695652
3.556304348
4.598478261
1.792913043
2.561869565
0.823347826
0.785347826
0.846571253
109.826956522
3
Sep-17
2.808571429
3.379476190
4.453571429
1.648095238
2.464571429
0.818380952
0.769333333
0.839435109
110.776000000
4
Oct-17
2.832909091
3.485318182
4.484636364
1.593772727
2.378863636
0.819909091
0.806272727
0.850697783
112.914761905
5
Nov-17
3.079545455
3.524045455
4.469045455
1.497363636
2.252500000
0.783454545
0.788500000
0.851653312
112.819000000
6
Dec-17
3.170000000
3.530000000
4.390714286
1.375857143
2.131142857
0.780190476
0.791380952
0.844899181
112.940500000
7
Jan-18
3.231608696
3.579434783
4.428956522
1.210608696
1.988000000
0.793869565
0.812652174
0.820065058
110.870952381
8
Feb-18
3.615700000
3.987200000
4.759500000
1.424550000
2.090100000
0.784700000
0.819300000
0.810431859
107.970000000
9
Mar-18
3.841409091
4.115545455
4.869045455
1.591954545
2.242863636
0.756954545
0.786545455
0.810784994
106.046818182
10
Apr-18
3.875761905
4.136238095
4.838619048
1.518714286
2.203619048
0.633571429
0.716619048
0.815069892
107.656190476
11
May-18
4.147782609
4.473913043
5.118130435
1.729304348
2.237695652
0.594739130
0.742521739
0.845926414
109.688181818
12
Jun-18
4.183000000
4.469619048
5.147761905
1.939333333
2.432523810
0.676142857
0.738666667
0.856266655
110.063809524
13
Jul-18

4.107227273
4.334318182
4.944181818
1.975409091
2.406000000
0.903545455
0.730454545
0.855835153
111.520952381
14
Aug-18
4.036000000
4.352913043
4.879000000
1.923478261
2.331521739
0.932304348
0.773782609
0.866141088
110.996521739
15
Sep-18
4.150200000
4.533500000
5.116850000
2.141350000
2.609950000
0.924350000
0.754150000
0.857148565
112.097368421
16
Oct-18
4.344913043
4.728347826
5.288478261
2.179434783
2.718608696
0.923521739
0.758565217
0.870545297
112.721818182
17
Nov-18
4.500272727
4.840045455
5.479181818
2.362363636
2.827136364
0.881863636
0.702136364
0.879998191
113.338000000
18
Dec-18
4.332571429
4.622952381
5.245523810
2.292666667
2.765380952
0.839761905
0.621047619
0.878716784
112.199444444
19
Jan-19
4.043478261
4.376826087
4.978086957
1.935608696
2.491000000
0.819478261
1.156608696
0.875835350
108.960500000
20
Feb-19
3.811350000
4.174050000
4.902550000
1.601150000
2.147800000
0.800100000
1.131700000
0.881120005
110.440000000
21
Mar-19
3.654523810
4.075476190
4.831523810
1.496761905
1.955666667
0.776666667
1.110952381
0.885273509
111.144285714
22
Apr-19
3.481454545
3.909318182
4.654272727
1.368090909
1.820590909
0.785681818
1.103090909
0.890170697
111.641363636
23
May-19
3.401608696
3.886478261
4.628652174
1.338782609
1.822217391
0.763086957
1.084000000
0.893908707
109.971363636
24
Jun-19
3.164150000
3.498300000
4.306800000
1.181150000
1.624700000
0.692300000
1.003050000
0.885364433
108.068500000
25
Jul-19

2.906000000
3.263956522
4.149000000
0.867652174
1.184260870
0.797173913
0.983217391
0.891966144
108.286363636
26
Aug-19
2.713181818
2.966500000
3.864045455
0.738863636
0.965136364
0.784409091
0.896500000
0.898607333
106.188636364
27
Sep-19
2.562904762
2.833714286
3.717476190
0.722190476
0.899285714
0.702619048
0.911761905
0.908183868
107.540000000
28
Oct-19
2.611521739
2.905521739
3.750043478
0.762260870
0.948956522
0.716608696
0.942652174
0.904347504
108.136818182
29
Nov-19
2.587238095
2.973761905
3.766333333
0.981095238
1.486571429
0.785285714
1.012476190
0.904944785
108.857894737
30
Dec-19
2.507863636
2.916454545
3.539590909
0.924136364
1.447954545
0.845500000
1.064272727
0.899807885
109.100952381
31
Jan-20
2.425608696
2.859000000
3.511347826
0.838434783
1.395043478
0.844347826
1.135304348
0.901112861
109.266666667
32
Feb-20
2.308200000
2.636900000
3.327100000
0.744250000
1.249150000
0.752250000
1.047350000
0.916577616
110.029473684
33
Mar-20
3.205772727
3.118181818
3.603090909
1.913136364
2.049136364
0.820227273
0.949818182
0.905625612
107.667272727
34
Apr-20
3.437272727
3.407363636
3.729909091
2.757681818
2.741545455
1.293909091
1.222000000
0.919890440
107.738636364
35
May-20
2.757095238
2.923095238
3.469761905
2.350619048
2.564142857
1.401142857
1.678000000
0.916874959
107.200000000
36
Jun-20
2.194227273
2.584545455
3.365090909
1.738272727
2.028000000
1.395227273
1.685090909
0.888204522
107.578181818
37
Jul-20

1.954347826
2.495956522
3.298608696
1.534434783
1.844130435
1.289130435
1.599347826
0.870682656
106.681818182
38
Aug-20
1.406714286
2.168000000
3.131380952
1.223380952
1.610476190
1.287666667
1.602619048
0.845247047
106.012857143
39
Sep-20
1.363454545
2.182545455
3.214545455
1.156045455
1.575409091
1.282954545
1.595954545
0.848573949
105.589047619
40
Oct-20
1.266500000
2.138409091
3.136727273
1.122727273
1.540045455
1.274636364
1.604727273
0.849796909
105.209523810
41
Nov-20
1.260714286
1.974952381
3.033571429
0.859666667
1.322476190
1.083761905
1.589333333
0.845604879
104.406111111
42
Dec-20
1.296173913
2.026521739
3.079521739
0.623695652
1.094913043
0.876347826
1.586000000
0.821849988
103.795238095
43
Jan-21
1.338238095
2.071190476
3.141285714
0.578714286
0.979380952
0.807571429
1.209714286
0.821196749
103.788333333
44
Feb-21
1.361900000
2.214350000
3.262700000
0.668050000
0.918679516
0.716350000
1.218150000
0.826879626
105.377368421
45
Mar-21
1.756913043
2.563391304
3.518043478
0.869826087
0.892062316
0.702260870
1.224434783
0.840279735
108.699130435
46
Apr-21
1.724409091
2.219818182
3.427090909
0.690318182
0.898910182
0.632590909
1.201272727
0.835803979
109.044545455
47
May-21
1.567952381
2.316285714
3.466523810
0.679428571
0.938603945
0.611333333
1.112952381
0.823324687
109.112000000
48
Jun-21
1.452318182
2.151045455
3.354181818
0.685090909
1.010524433
0.554772727
0.961045455
0.830092296
110.107272727
49
Jul-21

1.447090909
2.137090909
3.256818182
0.647363636
1.114052476
0.537500000
0.804363636
0.845931046
110.214285714
134
Lanjutan dari halaman sebelumnya
t
Periode

IR
1,t

IR
2,t

IR
3,t

IR
4,t

IR
5,t

IR
6,t

IR
7,t

F X
1,t

F X
2,t
50
Aug-21
1.366045455
2.186545455
3.293818182
0.911045455
1.248568903
0.548181818
0.818363636
0.849853773
109.852727273
51
Sep-21
1.333954545
2.186136364
3.312727273
0.947636364
1.413454545
0.579863636
0.867409091
0.850024463
110.160952381
52
Oct-21
1.639904762
2.463476190
3.539333333
1.213285714
1.563761905
0.600476190
0.914428571
0.862088418
113.121500000
53
Nov-21
1.662045455
2.333090909
3.422454545
1.212318182
1.570818182
0.591318182
0.889090909
0.876095871
113.965000000
54
Dec-21
1.946173913
2.227869565
3.342000000
1.205695652
1.584130435
0.587173913
0.874913043
0.884896566
113.832857143
55
Jan-22
2.290000000
2.516666667
3.640476190
1.380761905
1.721619048
0.636142857
0.969047619
0.883687895
114.825500000
56
Feb-22
2.662000000
2.834000000
3.842500000
1.941000000
2.174650000
0.705200000
1.061300000
0.881181085
115.276315789
57
Mar-22
2.970434783
3.144782609
4.032608696
2.333739130
2.528608696
0.776869565
1.107304348
0.907605412
118.577391304
58
Apr-22
3.429047619
3.605238095
4.304285714
2.592000000
2.800571429
0.818285714
1.198476190
0.925828752
126.374285714
59
May-22
3.996363636
4.133181818
4.740909091
3.193909091
3.428454545
0.810545455
1.213909091
0.946414641
128.848571429
60
Jun-22
4.190909091
4.355909091
4.808181818
3.892590909
4.142454545
0.938863636
1.271954545
0.946421775
133.961904762
61
Jul-22

4.218571429
4.390476190
4.860952381
4.207523810
4.485047619
1.191142857
1.555238095
0.983517686
136.709000000
62
Aug-22
3.857826087
4.009130435
4.678695652
3.439608696
3.927130435
1.246260870
1.555000000
0.987425376
135.283478261
63
Sep-22
4.641818182
4.806363636
5.437727273
4.277727273
4.694272727
1.351500000
1.555000000
1.010434829
143.284285714
64
Oct-22
5.499523810
5.564285714
6.123809524
5.173904762
5.419714286
1.417666667
1.664666667
1.015011424
147.051500000
65
Nov-22
5.157272727
5.231818182
5.785454545
4.847227273
5.008409091
1.464000000
1.900863636
0.981583044
142.445000000
66
Dec-22
4.575000000
4.670454545
5.243181818
4.281409091
4.369954545
1.632590909
2.086545455
0.944259335
134.914761905
67
Jan-23
4.604545455
4.792272727
5.306363636
4.305772727
4.390909091
1.708272727
2.293272727
0.928006303
130.447500000
68
Feb-23
4.798500000
4.943000000
5.427500000
4.176750000
4.276550000
1.653400000
2.265200000
0.934460361
133.046315789
69
Mar-23
4.843478261
4.963913043
5.448260870
4.393652174
4.490608696
1.526521739
2.059652174
0.933687110
133.664347826
70
Apr-23
4.485500000
4.679000000
5.303000000
4.224050000
4.374400000
1.483150000
2.003050000
0.912265880
133.474500000
71
May-23
4.490434783
4.653478261
5.345217391
4.110434783
4.419391304
1.254695652
1.877521739
0.920314478
137.053181818
72
Jun-23
4.787272727
4.804090909
5.342272727
4.104363636
4.458363636
0.927681818
1.471681818
0.922551268
141.358095238
73
Jul-23

4.951428571
4.891904762
5.341904762
4.194142857
4.479809524
0.953571429
1.507952381
0.903689370
140.936000000
74
Aug-23
5.134782609
5.204347826
5.556086957
4.252869565
4.560739130
1.051347826
1.757304348
0.916623805
144.780434783
75
Sep-23
5.399047619
5.645714286
5.752857143
4.384904762
4.730047619
1.089666667
1.776571429
0.937092609
147.845000000
76
Oct-23
5.678636364
6.125000000
6.261363636
4.613318182
4.898909091
1.176818182
1.921363636
0.946578930
149.593333333
77
Nov-23
5.382272727
5.780000000
5.918181818
4.315863636
4.632818182
1.264772727
1.883909091
0.924399786
149.679000000
78
Dec-23
4.765714286
5.045714286
5.233809524
3.705809524
4.014142857
1.183666667
1.726857143
0.916744667
143.981500000
79
Jan-24
4.763478261
5.035652174
5.310434783
3.683608696
3.941173913
1.125217391
1.679434783
0.917543019
146.294285714
80
Feb-24
4.937142857
5.002857143
5.385714286
3.720571429
3.935714286
1.177523810
1.742428571
0.926540508
149.615000000
81
Mar-24
4.968571429
5.029047619
5.336666667
3.710238095
3.930952381
1.137476190
1.688142857
0.919963737
149.818571429
82
Apr-24
5.243636364
5.326818182
5.601363636
3.781000000
3.997000000
1.206863636
1.758636364
0.932542516
153.890000000
83
May-24
5.230869565
5.274347826
5.569130435
3.840217391
4.005521739
1.257782609
1.842478261
0.925080337
155.869090909
84
Jun-24
5.108000000
5.141500000
5.448000000
3.821650000
3.998300000
1.239850000
1.866750000
0.929126006
157.860000000
85
Jul-24

5.030869565
5.101304348
5.472608696
3.764652174
3.974043478
1.239652174
1.869652174
0.921969304
157.518181818
86
Aug-24
4.673181818
4.776818182
5.161818182
3.520363636
3.767272727
1.163454545
1.706818182
0.907506748
146.264090909
87
Sep-24
4.401428571
4.619047619
5.037619048
3.387476190
3.664571429
1.176619048
1.701761905
0.900573837
142.954000000
88
Oct-24
4.603043478
4.860434783
5.216086957
3.609260870
3.592521739
1.211478261
1.750043478
0.917948948
149.890909091
89
Nov-24
4.957142857
5.123333333
5.433809524
3.656000000
3.693047619
1.245000000
1.846476190
0.941678142
153.712631579
90
Dec-24
5.076363636
5.244545455
5.509545455
3.609409091
3.669454545
1.279500000
1.874954545
0.954936052
153.814285714
91
Jan-25
5.245043478
5.494347826
5.777086957
3.778913043
3.864260870
1.365608696
2.008695652
0.965694376
156.481904762
92
Feb-25
5.012000000
5.337550000
5.652350000
3.644700000
4.038650000
1.506450000
2.149300000
0.960375741
151.571578947
93
Mar-25
4.905428571
5.221523810
5.655285714
3.926000000
4.321666667
1.559476190
2.241619048
0.924895075
149.057619048
94
Apr-25
4.932818182
5.333318182
5.894545455
4.048863636
4.471500000
1.357818182
2.049363636
0.887862480
143.765128205
95
May-25
4.817545455
5.455863636
5.828272727
3.774363636
4.303727273
1.439636364
2.259000000
0.887201711
144.861860465
96
Jun-25
4.532857143
5.258952381
5.694238095
3.570095238
4.087761905
1.464142857
2.303809524
0.867415990
144.547560976
97
Jul-25

4.446913043
5.188043478
5.603043478
3.525739130
3.999347826
1.883304348
2.348608696
0.856937421
147.178888889
98
Aug-25
4.340952381
5.099238095
5.528666667
3.409857143
3.929952381
1.922142857
2.410666667
0.858652869
147.504523810
99
Sep-25
4.307818182
4.991545455
5.475090909
3.469954545
4.016318182
1.979772727
2.498954545
0.852102086
147.893255814
100
Oct-25
4.270173913
4.903782609
5.359652174
3.494739130
4.014913043
1.943130435
2.592739130
0.859338382
151.411333333
101
Nov-25
4.245312500
4.915062500
5.333250000
3.464687500
3.974812500
1.945500000
2.668812500
0.865568356
154.943870968
135
Lampiran 16
Data Deret Waktu Hasil Transformasi
Box-Cox
t
Periode

Z1
,t
Z2
,t
Z3
,t
Z4
,t
Z5
,t
Z6
,t
Z7
,t
Z8
,t
Z9
,t
1
Jul-17

1.762344218
1.390300363
0.678775431
1.365667463
1.654575186
0.921598182
0.821158096
1.329054464
0.000000704
2
Aug-17
1.713095342
1.373250387
0.682883258
1.338997029
1.600584133
0.897565298
0.758371431
1.395317259
0.000000755
3
Sep-17
1.675879300
1.355852193
0.688371521
1.283781616
1.569895356
0.894188269
0.737769060
1.419141634
0.000000736
4
Oct-17
1.683124800
1.366345743
0.687176330
1.262447119
1.542356521
0.895230803
0.784666778
1.381813395
0.000000695
5
Nov-17
1.754863372
1.370125582
0.687774876
1.223668107
1.500833102
0.869458318
0.762377127
1.378714427
0.000000696
6
Dec-17
1.780449381
1.370703988
0.690822073
1.172969370
1.459843436
0.867054099
0.766024181
1.400845443
0.000000694
7
Jan-18
1.797667571
1.375477889
0.689325978
1.100276645
1.409964539
0.877019893
0.792547909
1.486974033
0.000000734
8
Feb-18
1.901499408
1.413080831
0.677032734
1.193545139
1.445717815
0.870371300
0.800695038
1.522533963
0.000000794
9
Mar-18
1.959951298
1.424317632
0.673192150
1.261726811
1.497619323
0.849439772
0.759895235
1.521207983
0.000000839
10
Apr-18
1.968695483
1.426104606
0.674247962
1.232361264
1.484459177
0.737304189
0.666789106
1.505255761
0.000000801
11
May-18
2.036610569
1.454359877
0.664847688
1.315030170
1.495892928
0.693085561
0.702296870
1.397445335
0.000000758
12
Jun-18
2.045238372
1.454010783
0.663888869
1.392599488
1.559655029
0.780159664
0.697091480
1.363898136
0.000000750
13
Jul-18

2.026629535
1.442879946
0.670619831
1.405492473
1.551128621
0.947929923
0.685911726
1.365273807
0.000000721
14
Aug-18
2.008979841
1.444425004
0.672848511
1.386895187
1.526932133
0.964315320
0.743535688
1.332977190
0.000000731
15
Sep-18
2.037203966
1.459178443
0.664889276
1.463335232
1.615533967
0.959862234
0.717836008
1.361092983
0.000000710
16
Oct-18
2.084445500
1.474610609
0.659427902
1.476290887
1.648820395
0.959395153
0.723673498
1.319523875
0.000000698
17
Nov-18
2.121384625
1.483243180
0.653613588
1.536998255
1.681409041
0.935030565
0.646372356
1.291327623
0.000000687
18
Dec-18
2.081482988
1.466323703
0.660773754
1.514155430
1.662943460
0.908494979
0.523652481
1.295096580
0.000000708
19
Jan-19
2.010840188
1.446404694
0.669475025
1.391261548
1.578290214
0.894937200
1.145492185
1.303632143
0.000000773
20
Feb-19
1.952267912
1.429352718
0.672039023
1.265365560
1.465537444
0.881465507
1.123720927
1.288041562
0.000000742
21
Mar-19
1.911680886
1.420838086
0.674495364
1.223422210
1.398451525
0.864439691
1.105217648
1.275983514
0.000000728
22
Apr-19
1.865865629
1.406129290
0.680827427
1.169654184
1.349292744
0.871089330
1.098116157
1.261982732
0.000000719
23
May-19
1.844345059
1.404070972
0.681767608
1.157057738
1.349895326
0.854176043
1.080657903
1.251450467
0.000000752
24
Jun-19
1.778805779
1.367616282
0.694162780
1.086807251
1.274637203
0.795150369
1.003045358
1.275721449
0.000000792
25
Jul-19

1.704699387
1.344113959
0.700670997
0.931478488
1.088237506
0.879384777
0.983074968
1.256907330
0.000000788
26
Aug-19
1.647173888
1.312384487
0.713246162
0.859571775
0.982413540
0.870158264
0.890743014
1.238397548
0.000000835
27
Sep-19
1.600907481
1.297445174
0.720174850
0.849817908
0.948306762
0.804400131
0.907623608
1.212418162
0.000000804
28
Oct-19
1.616020340
1.305587647
0.718606141
0.873075523
0.974143994
0.816562711
0.940942085
1.222726462
0.000000791
29
Nov-19
1.608489383
1.313186920
0.717827863
0.990502518
1.219250355
0.870799828
1.012399004
1.221112950
0.000000775
30
Dec-19
1.583623578
1.306814074
0.729057416
0.961320115
1.203309829
0.912235106
1.062291681
1.235095136
0.000000770
31
Jan-20
1.557436578
1.300329870
0.730519035
0.915660845
1.181119587
0.911487382
1.126900763
1.231520439
0.000000767
32
Feb-20
1.519276143
1.274305082
0.740429198
0.862699252
1.117653793
0.845762045
1.046263164
1.190313902
0.000000751
33
Mar-20
1.790467181
1.328848158
0.725823784
1.383161727
1.431480480
0.895447477
0.948515300
1.219277633
0.000000801
34
Apr-20
1.853988330
1.358640702
0.719573959
1.660626935
1.655761292
1.121457953
1.200488861
1.181755927
0.000000800
35
May-20
1.660450312
1.307557335
0.732698127
1.533172869
1.601294119
1.156411791
1.517602608
1.189541989
0.000000812
36
Jun-20
1.481292433
1.267932236
0.738330484
1.318435712
1.424078650
1.154581016
1.521819514
1.267576096
0.000000803
37
Jul-20

1.397979909
1.256924681
0.742022886
1.238723045
1.357987642
1.119807086
1.469595937
1.319107573
0.000000824
38
Aug-20
1.186049866
1.213430256
0.751737168
1.106065528
1.269045386
1.119299690
1.471639196
1.399692630
0.000000839
39
Sep-20
1.167670564
1.215460429
0.746827166
1.075195542
1.255153015
1.117660797
1.467472018
1.388738931
0.000000849
40
Oct-20
1.125388822
1.209268383
0.751416643
1.059588256
1.240985679
1.114747026
1.472953819
1.384744680
0.000000859
41
Nov-20
1.122815339
1.185466149
0.757724699
0.927182111
1.149989648
1.039441309
1.463314641
1.398508273
0.000000879
42
Dec-20
1.138496339
1.193130140
0.754882194
0.789744042
1.046380927
0.931669359
1.461215123
1.480522098
0.000000894
43
Jan-21
1.156822413
1.199651248
0.751143892
0.760732729
0.989636778
0.886722182
1.190384204
1.482878463
0.000000894
44
Feb-21
1.167004713
1.219864426
0.744056156
0.817343257
0.958477708
0.816341592
1.197333314
1.462565811
0.000000855
45
Mar-21
1.325485965
1.265329772
0.730171200
0.932644673
0.944490506
0.804083121
1.202479336
1.416290104
0.000000779
46
Apr-21
1.313167579
1.220616822
0.734968276
0.830853887
0.948108740
0.736253123
1.183381601
1.431499271
0.000000771
47
May-21
1.252179053
1.233667240
0.732869171
0.824274573
0.968815744
0.712661971
1.107016287
1.475223168
0.000000770
48
Jun-21
1.205121646
1.211050900
0.738930087
0.827702186
1.005248443
0.640939350
0.960266428
1.451266712
0.000000749
49
Jul-21

1.202950917
1.209081982
0.744391870
0.804589110
1.055486843
0.615770640
0.782296172
1.397430030
0.000000747
136
Lanjutan dari halaman sebelumnya
t
Periode

Z1
,t
Z2
,t
Z3
,t
Z4
,t
Z5
,t
Z6
,t
Z7
,t
Z8
,t
Z9
,t
50
Aug-21
1.168779472
1.216016947
0.742292537
0.954487011
1.117393799
0.631547099
0.799551502
1.384559379
0.000000754
51
Sep-21
1.154969500
1.215960065
0.741231009
0.973466159
1.188887945
0.674564813
0.857755433
1.384003381
0.000000748
52
Oct-21
1.280587663
1.252815426
0.729070680
1.101492494
1.250504660
0.699976937
0.910544079
1.345539275
0.000000691
53
Nov-21
1.289203419
1.235898814
0.735217063
1.101053215
1.253322856
0.688911440
0.882444211
1.302856947
0.000000676
54
Dec-21
1.395053373
1.221722129
0.739602531
1.098041735
1.258622435
0.683787812
0.866369224
1.277070816
0.000000678
55
Jan-22
1.513274595
1.259523933
0.723953132
1.175058256
1.312104816
0.740045862
0.968558474
1.280566652
0.000000661
56
Feb-22
1.631563667
1.297477877
0.714243885
1.393197761
1.474669454
0.806676002
1.059494572
1.287863003
0.000000653
57
Mar-22
1.723494933
1.331673193
0.705672965
1.527658054
1.590159959
0.864590763
1.101928546
1.213964107
0.000000600
58
Apr-22
1.851768781
1.377950091
0.694264129
1.609968944
1.673490791
0.894123191
1.181050909
1.166644861
0.000000495
59
May-22
1.999090702
1.425841095
0.677695486
1.787151110
1.851608637
0.888792520
1.193845806
1.116444399
0.000000467
60
Jun-22
2.047170997
1.444673485
0.675312486
1.972965005
2.035302077
0.967943680
1.240554730
1.116427569
0.000000416
61
Jul-22

2.053916120
1.447531111
0.673472177
2.051224953
2.117793101
1.083934145
1.441628650
1.033797916
0.000000391
62
Aug-22
1.964134946
1.415019897
0.679937198
1.854618208
1.981698876
1.104602989
1.441475546
1.025631691
0.000000404
63
Sep-22
2.154487916
1.480655950
0.654855749
2.068266732
2.166627039
1.140708151
1.441475546
0.979452513
0.000000340
64
Oct-22
2.345106354
1.535862567
0.635688832
2.274621894
2.328027982
1.161469900
1.509624903
0.970639899
0.000000314
65
Nov-22
2.270962952
1.512387784
0.644786044
2.201641949
2.237947517
1.175232920
1.642308328
1.037877041
0.000000346
66
Dec-22
2.138924964
1.470076000
0.660847529
2.069156613
2.090443624
1.220724485
1.735509806
1.121546865
0.000000407
67
Jan-23
2.145820462
1.479569538
0.658871539
2.075035597
2.095449615
1.239145980
1.829979936
1.161176259
0.000000450
68
Feb-23
2.190547877
1.491068696
0.655164024
2.043709862
2.067982108
1.225901209
1.817663055
1.145191809
0.000000425
69
Mar-23
2.200790372
1.492643318
0.654538997
2.096104047
2.119105636
1.192892189
1.722537121
1.147089420
0.000000419
70
Apr-23
2.117899903
1.470747982
0.658975993
2.055249377
2.091506634
1.180749001
1.694671019
1.201592297
0.000000421
71
May-23
2.119064601
1.468738308
0.657670947
2.027420722
2.102234836
1.107652037
1.629952683
1.180667181
0.000000388
72
Jun-23
2.187983713
1.480480884
0.657761555
2.025922910
2.111483752
0.961734645
1.386405841
1.174948901
0.000000354
73
Jul-23

2.225180571
1.487200416
0.657772882
2.047960658
2.116556053
0.975940088
1.410752691
1.224508073
0.000000357
74
Aug-23
2.266005871
1.510398615
0.651339987
2.062248667
2.135588708
1.024730689
1.563781014
1.190193944
0.000000330
75
Sep-23
2.323585079
1.541451001
0.645697497
2.094016419
2.174867265
1.042051745
1.574685343
1.138767267
0.000000309
76
Oct-23
2.382988956
1.573173142
0.632168378
2.147863632
2.213347937
1.078338695
1.653035161
1.116056891
0.000000299
77
Nov-23
2.319972570
1.550536377
0.641140076
2.077465676
2.152398240
1.111257146
1.633348922
1.170254521
0.000000298
78
Dec-23
2.183051599
1.498755065
0.661143179
1.925047928
2.003532594
1.081025886
1.546303076
1.189880139
0.000000335
79
Jan-24
2.182539406
1.498007305
0.658745225
1.919272960
1.985239007
1.057343962
1.518457298
1.187810417
0.000000319
80
Feb-24
2.221968239
1.495562357
0.656431136
1.928878282
1.983863475
1.078616599
1.555279871
1.164853149
0.000000299
137
Lampiran 17
Data Deret Waktu Hasil
Differencing
t
Periode

∆Z
1,t

∆Z
2,t

∆2
Z3
,t
∆Z
4,t

∆Z
5,t

∆Z
6,t

∆Z
7,t

∆Z
8,t

∆Z
9,t
1
Jul-17

–
–
–
–
–
–
–
–
–
2
Aug-17
-0.049248876
-0.017049975

–
-0.026670434
-0.053991054
-0.024032884
-0.062786665
0.066262795
0.000000051
3
Sep-17
-0.037216042
-0.017398195
0.001380435
-0.055215413
-0.030688777
-0.003377029
-0.020602371
0.023824374
-0.000000019
4
Oct-17

0.007245499
0.010493550
-0.006683454
-0.021334498
-0.027538835
0.001042533
0.046897718
-0.037328239
-0.000000041
5
Nov-17

0.071738572
0.003779840
0.001793737
-0.038779011
-0.041523419
-0.025772485
-0.022289650
-0.003098967
0.000000002
6
Dec-17

0.025586009
0.000578406
0.002448651
-0.050698737
-0.040989666
-0.002404218
0.003647054
0.022131016
-0.000000002
7
Jan-18

0.017218189
0.004773901
-0.004543292
-0.072692725
-0.049878897
0.009965794
0.026523727
0.086128590
0.000000040
8
Feb-18

0.103831837
0.037602942
-0.010797149
0.093268494
0.035753276
-0.006648593
0.008147130
0.035559930
0.000000061
9
Mar-18

0.058451890
0.011236801
0.008452659
0.068181671
0.051901508
-0.020931528
-0.040799803
-0.001325980
0.000000044
10
Apr-18

0.008744185
0.001786974
0.004896397
-0.029365547
-0.013160146
-0.112135584
-0.093106129
-0.015952222
-0.000000037
11
May-18

0.067915086
0.028255271
-0.010456087
0.082668906
0.011433751
-0.044218628
0.035507763
-0.107810426
-0.000000044
12
Jun-18

0.008627804
-0.000349094
0.008441455
0.077569318
0.063762101
0.087074104
-0.005205389
-0.033547199
-0.000000008
13
Jul-18

-0.018608837
-0.011130837
0.007689781
0.012892985
-0.008526408
0.167770259
-0.011179754
0.001375672
-0.000000029
14
Aug-18
-0.017649695
0.001545058
-0.004502282
-0.018597285
-0.024196488
0.016385397
0.057623961
-0.032296617
0.000000010
15
Sep-18

0.028224126
0.014753439
-0.010187914
0.076440044
0.088601834
-0.004453085
-0.025699680
0.028115792
-0.000000021
16
Oct-18

0.047241534
0.015432166
0.002497860
0.012955655
0.033286428
-0.000467081
0.005837490
-0.041569107
-0.000000012
17
Nov-18

0.036939125
0.008632571
-0.000352940
0.060707368
0.032588646
-0.024364588
-0.077301142
-0.028196252
-0.000000011
18
Dec-18
-0.039901637
-0.016919477
0.012974480
-0.022842825
-0.018465581
-0.026535587
-0.122719875
0.003768957
0.000000021
19
Jan-19
-0.070642800
-0.019919009
0.001541105
-0.122893882
-0.084653246
-0.013557779
0.621839704
0.008535563
0.000000065
20
Feb-19
-0.058572276
-0.017051976
-0.006137273
-0.125895988
-0.112752770
-0.013471692
-0.021771258
-0.015590581
-0.000000031
21
Mar-19
-0.040587026
-0.008514631
-0.000107658
-0.041943349
-0.067085919
-0.017025817
-0.018503279
-0.012058048
-0.000000014
22
Apr-19
-0.045815257
-0.014708796
0.003875723
-0.053768027
-0.049158781
0.006649639
-0.007101492
-0.014000782
-0.000000010
23
May-19
-0.021520570
-0.002058318
-0.005391882
-0.012596446
0.000602582
-0.016913287
-0.017458254
-0.010532264
0.000000033
24
Jun-19
-0.065539280
-0.036454690
0.011454991
-0.070250487
-0.075258123
-0.059025674
-0.077612545
0.024270982
0.000000040
25
Jul-19

-0.074106392
-0.023502323
-0.005886955
-0.155328762
-0.186399697
0.084234408
-0.019970391
-0.018814119
-0.000000005
26
Aug-19
-0.057525499
-0.031729472
0.006066947
-0.071906713
-0.105823966
-0.009226512
-0.092331954
-0.018509782
0.000000048
27
Sep-19
-0.046266408
-0.014939313
-0.005646476
-0.009753867
-0.034106778
-0.065758133
0.016880594
-0.025979386
-0.000000031
28
Oct-19

0.015112859
0.008142473
-0.008497398
0.023257616
0.025837233
0.012162580
0.033318477
0.010308300
-0.000000013
29
Nov-19
-0.007530957
0.007599273
0.000790431
0.117426995
0.245106361
0.054237117
0.071456919
-0.001613513
-0.000000016
30
Dec-19
-0.024865805
-0.006372846
0.012007832
-0.029182403
-0.015940526
0.041435279
0.049892677
0.013982186
-0.000000005
31
Jan-20
-0.026186999
-0.006484204
-0.009767935
-0.045659270
-0.022190243
-0.000747725
0.064609082
-0.003574697
-0.000000003
32
Feb-20
-0.038160435
-0.026024788
0.008448544
-0.052961592
-0.063465794
-0.065725337
-0.080637598
-0.041206536
-0.000000016
33
Mar-20

0.271191038
0.054543076
-0.024515577
0.520462475
0.313826687
0.049685433
-0.097747865
0.028963730
0.000000051
34
Apr-20

0.063521149
0.029792544
0.008355590
0.277465208
0.224280812
0.226010475
0.251973561
-0.037521706
-0.000000002
35
May-20
-0.193538018
-0.051083367
0.019373992
-0.127454066
-0.054467172
0.034953838
0.317113747
0.007786062
0.000000012
36
Jun-20
-0.179157879
-0.039625099
-0.007491811
-0.214737157
-0.177215470
-0.001830775
0.004216906
0.078034107
-0.000000009
37
Jul-20

-0.083312524
-0.011007556
-0.001939955
-0.079712667
-0.066091008
-0.034773930
-0.052223577
0.051531477
0.000000020
38
Aug-20
-0.211930043
-0.043494425
0.006021881
-0.132657517
-0.088942256
-0.000507396
0.002043258
0.080585057
0.000000016
39
Sep-20
-0.018379303
0.002030173
-0.014624285
-0.030869986
-0.013892371
-0.001638893
-0.004167177
-0.010953699
0.000000010
40
Oct-20
-0.042281742
-0.006192046
0.009499479
-0.015607286
-0.014167336
-0.002913770
0.005481800
-0.003994251
0.000000009
41
Nov-20
-0.002573483
-0.023802234
0.001718579
-0.132406145
-0.090996031
-0.075305718
-0.009639178
0.013763593
0.000000020
42
Dec-20

0.015681000
0.007663991
-0.009150560
-0.137438069
-0.103608721
-0.107771949
-0.002099518
0.082013824
0.000000016
43
Jan-21

0.018326074
0.006521108
-0.000895797
-0.029011313
-0.056744149
-0.044947177
-0.270830919
0.002356365
0.000000000
44
Feb-21

0.010182300
0.020213179
-0.003349434
0.056610528
-0.031159070
-0.070380590
0.006949110
-0.020312652
-0.000000040
45
Mar-21

0.158481252
0.045465346
-0.006797220
0.115301416
-0.013987202
-0.012258472
0.005146021
-0.046275707
-0.000000076
46
Apr-21
-0.012318386
-0.044712950
0.018682031
-0.101790786
0.003618234
-0.067829998
-0.019097735
0.015209168
-0.000000007
47
May-21
-0.060988526
0.013050417
-0.006896181
-0.006579314
0.020707004
-0.023591152
-0.076365314
0.043723897
-0.000000001
48
Jun-21
-0.047057407
-0.022616339
0.008160020
0.003427613
0.036432700
-0.071722621
-0.146749859
-0.023956456
-0.000000021
49
Jul-21

-0.002170729
-0.001968919
-0.000599132
-0.023113076
0.050238400
-0.025168710
-0.177970256
-0.053836682
-0.000000002
138
Lanjutan dari halaman sebelumnya
t
Periode

∆Z
1,t

∆Z
2,t

∆2
Z3
,t
∆Z
4,t

∆Z
5,t

∆Z
6,t

∆Z
7,t

∆Z
8,t

∆Z
9,t
50
Aug-21
-0.034171445
0.006934965
-0.007561117
0.149897901
0.061906956
0.015776459
0.017255330
-0.012870651
0.000000007
51
Sep-21
-0.013809972
-0.000056882
0.001037804
0.018979148
0.071494145
0.043017714
0.058203931
-0.000555998
-0.000000006
52
Oct-21

0.125618163
0.036855361
-0.011098799
0.128026335
0.061616715
0.025412124
0.052788646
-0.038464106
-0.000000057
53
Nov-21

0.008615756
-0.016916612
0.018306711
-0.000439279
0.002818196
-0.011065497
-0.028099868
-0.042682328
-0.000000015
54
Dec-21

0.105849954
-0.014176685
-0.001760915
-0.003011480
0.005299579
-0.005123628
-0.016074988
-0.025786131
0.000000002
55
Jan-22

0.118221222
0.037801804
-0.020034867
0.077016521
0.053482380
0.056258050
0.102189251
0.003495836
-0.000000017
56
Feb-22

0.118289072
0.037953944
0.005940152
0.218139505
0.162564639
0.066630140
0.090936098
0.007296351
-0.000000008
57
Mar-22

0.091931265
0.034195316
0.001138326
0.134460294
0.115490505
0.057914761
0.042433974
-0.073898895
-0.000000053
58
Apr-22

0.128273849
0.046276898
-0.002837915
0.082310890
0.083330832
0.029532428
0.079122362
-0.047319246
-0.000000104
59
May-22

0.147321921
0.047891004
-0.005159808
0.177182166
0.178117846
-0.005330671
0.012794897
-0.050200462
-0.000000028
60
Jun-22

0.048080295
0.018832390
0.014185643
0.185813894
0.183693440
0.079151160
0.046708924
-0.000016830
-0.000000052
61
Jul-22

0.006745123
0.002857627
0.000542691
0.078259949
0.082491024
0.115990465
0.201073920
-0.082629653
-0.000000025
62
Aug-22
-0.089781174
-0.032511215
0.008305330
-0.196606746
-0.136094225
0.020668844
-0.000153104
-0.008166225
0.000000013
63
Sep-22

0.190352970
0.065636054
-0.031546470
0.213648524
0.184928163
0.036105162
0.000000000
-0.046179179
-0.000000064
64
Oct-22

0.190618437
0.055206616
0.005914532
0.206355163
0.161400943
0.020761748
0.068149358
-0.008812614
-0.000000025
65
Nov-22
-0.074143402
-0.023474783
0.028264129
-0.072979945
-0.090080465
0.013763020
0.132683425
0.067237142
0.000000032
66
Dec-22
-0.132037988
-0.042311784
0.006964274
-0.132485336
-0.147503893
0.045491565
0.093201478
0.083669824
0.000000061
67
Jan-23

0.006895498
0.009493539
-0.018037476
0.005878983
0.005005991
0.018421495
0.094470130
0.039629394
0.000000043
68
Feb-23

0.044727415
0.011499158
-0.001731525
-0.031325735
-0.027467507
-0.013244771
-0.012316881
-0.015984451
-0.000000026
69
Mar-23

0.010242495
0.001574622
0.003082487
0.052394185
0.051123528
-0.033009020
-0.095125934
0.001897611
-0.000000006
70
Apr-23
-0.082890469
-0.021895336
0.005062024
-0.040854670
-0.027599002
-0.012143187
-0.027866102
0.054502878
0.000000002
71
May-23

0.001164698
-0.002009675
-0.005742043
-0.027828655
0.010728202
-0.073096964
-0.064718336
-0.020925116
-0.000000032
72
Jun-23

0.068919112
0.011742577
0.001395655
-0.001497812
0.009248917
-0.145917392
-0.243546843
-0.005718279
-0.000000034
73
Jul-23

0.037196858
0.006719532
-0.000079282
0.022037748
0.005072300
0.014205443
0.024346851
0.049559172
0.000000003
74
Aug-23

0.040825301
0.023198198
-0.006444221
0.014288009
0.019032656
0.048790601
0.153028323
-0.034314129
-0.000000028
75
Sep-23

0.057579208
0.031052386
0.000790403
0.031767752
0.039278557
0.017321056
0.010904329
-0.051426677
-0.000000020
76
Oct-23

0.059403877
0.031722141
-0.007886627
0.053847213
0.038480672
0.036286950
0.078349818
-0.022710376
-0.000000011
77
Nov-23
-0.063016385
-0.022636765
0.022500815
-0.070397956
-0.060949698
0.032918451
-0.019686239
0.054197631
-0.000000001
78
Dec-23
-0.136920971
-0.051781312
0.011031406
-0.152417749
-0.148865645
-0.030231260
-0.087045846
0.019625617
0.000000037
79
Jan-24
-0.000512193
-0.000747760
-0.022401058
-0.005774967
-0.018293588
-0.023681924
-0.027845778
-0.002069721
-0.000000016
80
Feb-24

0.039428833
-0.002444948
0.000083865
0.009605322
-0.001375532
0.021272637
0.036822573
-0.022957268
-0.000000021
139
Lampiran 18
Gabungan Data Historis dan Data Hasil Peramalan
t
Periode

IR
1,t

IR
2,t

IR
3,t

IR
4,t

IR
5,t

IR
6,t

IR
7,t

F X
1,t

F X
2,t
1
Jul-17

3.105857143
3.736238095
4.710809524
1.865047619
2.737619048
0.860142857
0.836238095
0.867418361
112.417000000
2
Aug-17
2.934695652
3.556304348
4.598478261
1.792913043
2.561869565
0.823347826
0.785347826
0.846571253
109.826956522
3
Sep-17
2.808571429
3.379476190
4.453571429
1.648095238
2.464571429
0.818380952
0.769333333
0.839435109
110.776000000
4
Oct-17
2.832909091
3.485318182
4.484636364
1.593772727
2.378863636
0.819909091
0.806272727
0.850697783
112.914761905
5
Nov-17
3.079545455
3.524045455
4.469045455
1.497363636
2.252500000
0.783454545
0.788500000
0.851653312
112.819000000
6
Dec-17
3.170000000
3.530000000
4.390714286
1.375857143
2.131142857
0.780190476
0.791380952
0.844899181
112.940500000
7
Jan-18
3.231608696
3.579434783
4.428956522
1.210608696
1.988000000
0.793869565
0.812652174
0.820065058
110.870952381
8
Feb-18
3.615700000
3.987200000
4.759500000
1.424550000
2.090100000
0.784700000
0.819300000
0.810431859
107.970000000
9
Mar-18
3.841409091
4.115545455
4.869045455
1.591954545
2.242863636
0.756954545
0.786545455
0.810784994
106.046818182
10
Apr-18
3.875761905
4.136238095
4.838619048
1.518714286
2.203619048
0.633571429
0.716619048
0.815069892
107.656190476
11
May-18
4.147782609
4.473913043
5.118130435
1.729304348
2.237695652
0.594739130
0.742521739
0.845926414
109.688181818
12
Jun-18
4.183000000
4.469619048
5.147761905
1.939333333
2.432523810
0.676142857
0.738666667
0.856266655
110.063809524
13
Jul-18

4.107227273
4.334318182
4.944181818
1.975409091
2.406000000
0.903545455
0.730454545
0.855835153
111.520952381
14
Aug-18
4.036000000
4.352913043
4.879000000
1.923478261
2.331521739
0.932304348
0.773782609
0.866141088
110.996521739
15
Sep-18
4.150200000
4.533500000
5.116850000
2.141350000
2.609950000
0.924350000
0.754150000
0.857148565
112.097368421
16
Oct-18
4.344913043
4.728347826
5.288478261
2.179434783
2.718608696
0.923521739
0.758565217
0.870545297
112.721818182
17
Nov-18
4.500272727
4.840045455
5.479181818
2.362363636
2.827136364
0.881863636
0.702136364
0.879998191
113.338000000
18
Dec-18
4.332571429
4.622952381
5.245523810
2.292666667
2.765380952
0.839761905
0.621047619
0.878716784
112.199444444
19
Jan-19
4.043478261
4.376826087
4.978086957
1.935608696
2.491000000
0.819478261
1.156608696
0.875835350
108.960500000
20
Feb-19
3.811350000
4.174050000
4.902550000
1.601150000
2.147800000
0.800100000
1.131700000
0.881120005
110.440000000
21
Mar-19
3.654523810
4.075476190
4.831523810
1.496761905
1.955666667
0.776666667
1.110952381
0.885273509
111.144285714
22
Apr-19
3.481454545
3.909318182
4.654272727
1.368090909
1.820590909
0.785681818
1.103090909
0.890170697
111.641363636
23
May-19
3.401608696
3.886478261
4.628652174
1.338782609
1.822217391
0.763086957
1.084000000
0.893908707
109.971363636
24
Jun-19
3.164150000
3.498300000
4.306800000
1.181150000
1.624700000
0.692300000
1.003050000
0.885364433
108.068500000
25
Jul-19

2.906000000
3.263956522
4.149000000
0.867652174
1.184260870
0.797173913
0.983217391
0.891966144
108.286363636
26
Aug-19
2.713181818
2.966500000
3.864045455
0.738863636
0.965136364
0.784409091
0.896500000
0.898607333
106.188636364
27
Sep-19
2.562904762
2.833714286
3.717476190
0.722190476
0.899285714
0.702619048
0.911761905
0.908183868
107.540000000
28
Oct-19
2.611521739
2.905521739
3.750043478
0.762260870
0.948956522
0.716608696
0.942652174
0.904347504
108.136818182
29
Nov-19
2.587238095
2.973761905
3.766333333
0.981095238
1.486571429
0.785285714
1.012476190
0.904944785
108.857894737
30
Dec-19
2.507863636
2.916454545
3.539590909
0.924136364
1.447954545
0.845500000
1.064272727
0.899807885
109.100952381
31
Jan-20
2.425608696
2.859000000
3.511347826
0.838434783
1.395043478
0.844347826
1.135304348
0.901112861
109.266666667
32
Feb-20
2.308200000
2.636900000
3.327100000
0.744250000
1.249150000
0.752250000
1.047350000
0.916577616
110.029473684
33
Mar-20
3.205772727
3.118181818
3.603090909
1.913136364
2.049136364
0.820227273
0.949818182
0.905625612
107.667272727
34
Apr-20
3.437272727
3.407363636
3.729909091
2.757681818
2.741545455
1.293909091
1.222000000
0.919890440
107.738636364
35
May-20
2.757095238
2.923095238
3.469761905
2.350619048
2.564142857
1.401142857
1.678000000
0.916874959
107.200000000
36
Jun-20
2.194227273
2.584545455
3.365090909
1.738272727
2.028000000
1.395227273
1.685090909
0.888204522
107.578181818
37
Jul-20

1.954347826
2.495956522
3.298608696
1.534434783
1.844130435
1.289130435
1.599347826
0.870682656
106.681818182
38
Aug-20
1.406714286
2.168000000
3.131380952
1.223380952
1.610476190
1.287666667
1.602619048
0.845247047
106.012857143
39
Sep-20
1.363454545
2.182545455
3.214545455
1.156045455
1.575409091
1.282954545
1.595954545
0.848573949
105.589047619
40
Oct-20
1.266500000
2.138409091
3.136727273
1.122727273
1.540045455
1.274636364
1.604727273
0.849796909
105.209523810
41
Nov-20
1.260714286
1.974952381
3.033571429
0.859666667
1.322476190
1.083761905
1.589333333
0.845604879
104.406111111
42
Dec-20
1.296173913
2.026521739
3.079521739
0.623695652
1.094913043
0.876347826
1.586000000
0.821849988
103.795238095
43
Jan-21
1.338238095
2.071190476
3.141285714
0.578714286
0.979380952
0.807571429
1.209714286
0.821196749
103.788333333
44
Feb-21
1.361900000
2.214350000
3.262700000
0.668050000
0.918679516
0.716350000
1.218150000
0.826879626
105.377368421
45
Mar-21
1.756913043
2.563391304
3.518043478
0.869826087
0.892062316
0.702260870
1.224434783
0.840279735
108.699130435
46
Apr-21
1.724409091
2.219818182
3.427090909
0.690318182
0.898910182
0.632590909
1.201272727
0.835803979
109.044545455
47
May-21
1.567952381
2.316285714
3.466523810
0.679428571
0.938603945
0.611333333
1.112952381
0.823324687
109.112000000
48
Jun-21
1.452318182
2.151045455
3.354181818
0.685090909
1.010524433
0.554772727
0.961045455
0.830092296
110.107272727
49
Jul-21

1.447090909
2.137090909
3.256818182
0.647363636
1.114052476
0.537500000
0.804363636
0.845931046
110.214285714
140
Lanjutan dari halaman sebelumnya
t
Periode

IR
1,t

IR
2,t

IR
3,t

IR
4,t

IR
5,t

IR
6,t

IR
7,t

F X
1,t

F X
2,t
50
Aug-21
1.366045455
2.186545455
3.293818182
0.911045455
1.248568903
0.548181818
0.818363636
0.849853773
109.852727273
51
Sep-21
1.333954545
2.186136364
3.312727273
0.947636364
1.413454545
0.579863636
0.867409091
0.850024463
110.160952381
52
Oct-21
1.639904762
2.463476190
3.539333333
1.213285714
1.563761905
0.600476190
0.914428571
0.862088418
113.121500000
53
Nov-21
1.662045455
2.333090909
3.422454545
1.212318182
1.570818182
0.591318182
0.889090909
0.876095871
113.965000000
54
Dec-21
1.946173913
2.227869565
3.342000000
1.205695652
1.584130435
0.587173913
0.874913043
0.884896566
113.832857143
55
Jan-22
2.290000000
2.516666667
3.640476190
1.380761905
1.721619048
0.636142857
0.969047619
0.883687895
114.825500000
56
Feb-22
2.662000000
2.834000000
3.842500000
1.941000000
2.174650000
0.705200000
1.061300000
0.881181085
115.276315789
57
Mar-22
2.970434783
3.144782609
4.032608696
2.333739130
2.528608696
0.776869565
1.107304348
0.907605412
118.577391304
58
Apr-22
3.429047619
3.605238095
4.304285714
2.592000000
2.800571429
0.818285714
1.198476190
0.925828752
126.374285714
59
May-22
3.996363636
4.133181818
4.740909091
3.193909091
3.428454545
0.810545455
1.213909091
0.946414641
128.848571429
60
Jun-22
4.190909091
4.355909091
4.808181818
3.892590909
4.142454545
0.938863636
1.271954545
0.946421775
133.961904762
61
Jul-22

4.218571429
4.390476190
4.860952381
4.207523810
4.485047619
1.191142857
1.555238095
0.983517686
136.709000000
62
Aug-22
3.857826087
4.009130435
4.678695652
3.439608696
3.927130435
1.246260870
1.555000000
0.987425376
135.283478261
63
Sep-22
4.641818182
4.806363636
5.437727273
4.277727273
4.694272727
1.351500000
1.555000000
1.010434829
143.284285714
64
Oct-22
5.499523810
5.564285714
6.123809524
5.173904762
5.419714286
1.417666667
1.664666667
1.015011424
147.051500000
65
Nov-22
5.157272727
5.231818182
5.785454545
4.847227273
5.008409091
1.464000000
1.900863636
0.981583044
142.445000000
66
Dec-22
4.575000000
4.670454545
5.243181818
4.281409091
4.369954545
1.632590909
2.086545455
0.944259335
134.914761905
67
Jan-23
4.604545455
4.792272727
5.306363636
4.305772727
4.390909091
1.708272727
2.293272727
0.928006303
130.447500000
68
Feb-23
4.798500000
4.943000000
5.427500000
4.176750000
4.276550000
1.653400000
2.265200000
0.934460361
133.046315789
69
Mar-23
4.843478261
4.963913043
5.448260870
4.393652174
4.490608696
1.526521739
2.059652174
0.933687110
133.664347826
70
Apr-23
4.485500000
4.679000000
5.303000000
4.224050000
4.374400000
1.483150000
2.003050000
0.912265880
133.474500000
71
May-23
4.490434783
4.653478261
5.345217391
4.110434783
4.419391304
1.254695652
1.877521739
0.920314478
137.053181818
72
Jun-23
4.787272727
4.804090909
5.342272727
4.104363636
4.458363636
0.927681818
1.471681818
0.922551268
141.358095238
73
Jul-23

4.951428571
4.891904762
5.341904762
4.194142857
4.479809524
0.953571429
1.507952381
0.903689370
140.936000000
74
Aug-23
5.134782609
5.204347826
5.556086957
4.252869565
4.560739130
1.051347826
1.757304348
0.916623805
144.780434783
75
Sep-23
5.399047619
5.645714286
5.752857143
4.384904762
4.730047619
1.089666667
1.776571429
0.937092609
147.845000000
76
Oct-23
5.678636364
6.125000000
6.261363636
4.613318182
4.898909091
1.176818182
1.921363636
0.946578930
149.593333333
77
Nov-23
5.382272727
5.780000000
5.918181818
4.315863636
4.632818182
1.264772727
1.883909091
0.924399786
149.679000000
78
Dec-23
4.765714286
5.045714286
5.233809524
3.705809524
4.014142857
1.183666667
1.726857143
0.916744667
143.981500000
79
Jan-24
4.763478261
5.035652174
5.310434783
3.683608696
3.941173913
1.125217391
1.679434783
0.917543019
146.294285714
80
Feb-24
4.937142857
5.002857143
5.385714286
3.720571429
3.935714286
1.177523810
1.742428571
0.926540508
149.615000000
81
Mar-24
4.968571429
5.029047619
5.336666667
3.710238095
3.930952381
1.137476190
1.688142857
0.919963737
149.818571429
82
Apr-24
5.243636364
5.326818182
5.601363636
3.781000000
3.997000000
1.206863636
1.758636364
0.932542516
153.890000000
83
May-24
5.230869565
5.274347826
5.569130435
3.840217391
4.005521739
1.257782609
1.842478261
0.925080337
155.869090909
84
Jun-24
5.108000000
5.141500000
5.448000000
3.821650000
3.998300000
1.239850000
1.866750000
0.929126006
157.860000000
85
Jul-24

5.030869565
5.101304348
5.472608696
3.764652174
3.974043478
1.239652174
1.869652174
0.921969304
157.518181818
86
Aug-24
4.673181818
4.776818182
5.161818182
3.520363636
3.767272727
1.163454545
1.706818182
0.907506748
146.264090909
87
Sep-24
4.401428571
4.619047619
5.037619048
3.387476190
3.664571429
1.176619048
1.701761905
0.900573837
142.954000000
88
Oct-24
4.603043478
4.860434783
5.216086957
3.609260870
3.592521739
1.211478261
1.750043478
0.917948948
149.890909091
89
Nov-24
4.957142857
5.123333333
5.433809524
3.656000000
3.693047619
1.245000000
1.846476190
0.941678142
153.712631579
90
Dec-24
5.076363636
5.244545455
5.509545455
3.609409091
3.669454545
1.279500000
1.874954545
0.954936052
153.814285714
91
Jan-25
5.245043478
5.494347826
5.777086957
3.778913043
3.864260870
1.365608696
2.008695652
0.965694376
156.481904762
92
Feb-25
5.012000000
5.337550000
5.652350000
3.644700000
4.038650000
1.506450000
2.149300000
0.960375741
151.571578947
93
Mar-25
4.905428571
5.221523810
5.655285714
3.926000000
4.321666667
1.559476190
2.241619048
0.924895075
149.057619048
94
Apr-25
4.932818182
5.333318182
5.894545455
4.048863636
4.471500000
1.357818182
2.049363636
0.887862480
143.765128205
95
May-25
4.817545455
5.455863636
5.828272727
3.774363636
4.303727273
1.439636364
2.259000000
0.887201711
144.861860465
96
Jun-25
4.532857143
5.258952381
5.694238095
3.570095238
4.087761905
1.464142857
2.303809524
0.867415990
144.547560976
97
Jul-25

4.446913043
5.188043478
5.603043478
3.525739130
3.999347826
1.883304348
2.348608696
0.856937421
147.178888889
98
Aug-25
4.340952381
5.099238095
5.528666667
3.409857143
3.929952381
1.922142857
2.410666667
0.858652869
147.504523810
99
Sep-25
4.307818182
4.991545455
5.475090909
3.469954545
4.016318182
1.979772727
2.498954545
0.852102086
147.893255814
100
Oct-25
4.270173913
4.903782609
5.359652174
3.494739130
4.014913043
1.943130435
2.592739130
0.859338382
151.411333333
101
Nov-25
4.245312500
4.915062500
5.333250000
3.464687500
3.974812500
1.945500000
2.668812500
0.865568356
154.943870968
102
Dec-25
4.974310000
4.991475000
5.184656355
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
103
Jan-26
4.974310000
4.991475000
5.177820977
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
104
Feb-26
4.974310000
4.991475000
5.170996857
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
105
Mar-26
4.974310000
4.991475000
5.164183972
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
106
Apr-26
4.974310000
4.991475000
5.157382304
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
141
Lanjutan dari halaman sebelumnya
t
Periode

IR
1,t

IR
2,t

IR
3,t

IR
4,t

IR
5,t

IR
6,t

IR
7,t

F X
1,t

F X
2,t
107
May-26
4.974310000
4.991475000
5.150591831
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
108
Jun-26
4.974310000
4.991475000
5.143812530
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
109

Jul-26

4.974310000
4.991475000
5.137044379
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
110
Aug-26
4.974310000
4.991475000
5.130287356
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
111
Sep-26
4.974310000
4.991475000
5.123541439
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
112
Oct-26
4.974310000
4.991475000
5.116806607
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
113
Nov-26
4.974310000
4.991475000
5.110082837
3.705371000
3.905557000
1.212798477
1.739477000
0.929404000
150.256822000
142
Lampiran 19
Data Biaya Utang Valas
t Periode C10,t C20,t C30,t C41,t C51,t C62,t C72,t
1 Jul-17 1.031058571 1.037362381 1.047108095 0.883596126 0.891164971 113.383946796 113.3570737802 Aug-17 1.029346957 1.035563043 1.045984783 0.861749539 0.868259304 110.731214381 110.689480137
3 Sep-17 1.028085714 1.033794762 1.044535714 0.853269799 0.860123587 111.682569684 111.6282366934 Oct-17 1.028329091 1.034853182 1.044846364 0.864255972 0.870934723 113.840560303 113.825162835
5 Nov-17 1.030795455 1.035240455 1.044690455 0.864405659 0.870836803 113.702885584 113.7085778156 Dec-17 1.031700000 1.035300000 1.043907143 0.856523787 0.862905190 113.821651025 113.834289605
7 Jan-18 1.032316087 1.035794348 1.044289565 0.829992837 0.836367952 111.751123129 111.7719475868 Feb-18 1.036157000 1.039872000 1.047595000 0.821976866 0.827370695 108.817240590 108.854598210
9 Mar-18 1.038414091 1.041155455 1.048690455 0.823692322 0.828969795 106.849544392 106.88092461010 Apr-18 1.038757619 1.041362381 1.048386190 0.827448475 0.833030927 108.338269340 108.427675243
11 May-18 1.041477826 1.044739130 1.051181304 0.860555056 0.864855672 110.340540357 110.50264041312 Jun-18 1.041830000 1.044696190 1.051477619 0.872872520 0.877095546 110.807998110 110.876814197
13 Jul-18 1.041072273 1.043343182 1.049441818 0.872741398 0.876426547 112.528594877 112.33556224714 Aug-18 1.040360000 1.043529130 1.048790000 0.882801123 0.886335356 112.031347137 111.855393521
15 Sep-18 1.041502000 1.045335000 1.051168500 0.875503116 0.879519714 113.133540446 112.94275072516 Oct-18 1.043449130 1.047283478 1.052884783 0.889518264 0.894212017 113.762828677 113.576886687
17 Nov-18 1.045002727 1.048400455 1.054791818 0.900786948 0.904876940 114.337486608 114.13378731218 Dec-18 1.043325714 1.046229524 1.052455238 0.898862831 0.903016651 113.141652636 112.896256423
19 Jan-19 1.040434783 1.043768261 1.049780870 0.892788095 0.897652409 109.853407610 110.22074661820 Feb-19 1.038113500 1.041740500 1.049025500 0.895228058 0.900044701 111.323630440 111.689849480
21 Mar-19 1.036545238 1.040754762 1.048315238 0.898523945 0.902586508 112.007506333 112.37904580322 Apr-19 1.034814545 1.039093182 1.046542727 0.902349041 0.906377064 112.518509532 112.872869369
23 May-19 1.034016087 1.038864783 1.046286522 0.905876202 0.910197667 110.810540768 111.16345321824 Jun-19 1.031641500 1.034983000 1.043068000 0.895821915 0.899748949 108.816658226 109.152481089
25 Jul-19 1.029060000 1.032639565 1.041490000 0.899705308 0.902529350 109.149594279 109.35105399626 Aug-19 1.027131818 1.029665000 1.038640455 0.905246816 0.907280119 107.021589681 107.140617489
27 Sep-19 1.025629048 1.028337143 1.037174762 0.914742685 0.916351036 108.295596524 108.52050875228 Oct-19 1.026115217 1.029055217 1.037500435 0.911240991 0.912929369 108.911736024 109.156172249
29 Nov-19 1.025872381 1.029737619 1.037663333 0.913823155 0.918397435 109.712740233 109.96005500330 Dec-19 1.025078636 1.029164545 1.035395909 0.908123336 0.912836694 110.023400933 110.262084062
31 Jan-20 1.024256087 1.028590000 1.035113478 0.908668104 0.913683777 110.189257391 110.50717588432 Feb-20 1.023082000 1.026369000 1.033271000 0.923399245 0.928027045 110.857170400 111.181867377
33 Mar-20 1.032057727 1.031181818 1.036030909 0.922951465 0.924183116 108.550389062 108.68991606034 Apr-20 1.034372727 1.034073636 1.037299091 0.945258091 0.945109654 109.132676374 109.055202500
35 May-20 1.027570952 1.029230952 1.034697619 0.938427196 0.940384943 108.702025143 108.99881600036 Jun-20 1.021942273 1.025845455 1.033650909 0.903643939 0.906217309 109.079141950 109.390971980
37 Jul-20 1.019543478 1.024959565 1.032986087 0.884042713 0.886739180 108.057085968 108.38803152238 Aug-20 1.014067143 1.021680000 1.031313810 0.855587638 0.858859549 107.377949367 107.711839384
39 Sep-20 1.013634545 1.021825455 1.032145455 0.858383849 0.861942460 106.943707105 107.27420082440 Oct-20 1.012665000 1.021384091 1.031367273 0.859337811 0.862884168 106.550562658 106.897849732
41 Nov-20 1.012607143 1.019749524 1.030335714 0.852874262 0.856787802 105.537624770 106.06547223742 Dec-20 1.012961739 1.020265217 1.030795217 0.826975830 0.830848531 104.704845408 105.441430571
43 Jan-21 1.013382381 1.020711905 1.031412857 0.825949132 0.829239393 104.626498260 105.04387562944 Feb-21 1.013619000 1.022143500 1.032627000 0.832403596 0.834476000 106.132239200 106.661022834
45 Mar-21 1.017569130 1.025633913 1.035180435 0.847588707 0.847775554 109.462481893 110.03008039646 Apr-21 1.017244091 1.022198182 1.034270909 0.841573686 0.843317106 109.734351336 110.354467840
47 May-21 1.015679524 1.023162857 1.034665238 0.828918590 0.831052445 109.779038027 110.32636460248 Jun-21 1.014523182 1.021510455 1.033541818 0.835779182 0.838480581 110.718117847 111.165453667
49 Jul-21 1.014470909 1.021370909 1.032568182 0.851407296 0.855355162 110.806687500 111.10080935150 Aug-21 1.013660455 1.021865455 1.032938182 0.857596328 0.860464783 110.454919950 110.751722046
51 Sep-21 1.013339545 1.021861364 1.033127273 0.858079604 0.862039172 110.799735685 111.11649849752 Oct-21 1.016399048 1.024634762 1.035393333 0.872548014 0.875569428 113.800767674 114.155915316
53 Nov-21 1.016620455 1.023330909 1.034224545 0.886716940 0.889857744 114.638895766 114.97825245554 Dec-21 1.019461739 1.022278696 1.033420000 0.895565726 0.898914482 114.501253984 114.828795658
55 Jan-22 1.022900000 1.025166667 1.036404762 0.895889521 0.898901634 115.555954216 115.93821377456 Feb-22 1.026620000 1.028340000 1.038425000 0.898284810 0.900343690 116.089244368 116.499743329
57 Mar-22 1.029704348 1.031447826 1.040326087 0.928786554 0.930555201 119.498582969 119.89040391458 Apr-22 1.034290476 1.036052381 1.043042857 0.949826233 0.951757247 127.408388441 127.888851439
59 May-22 1.039963636 1.041331818 1.047409091 0.976642265 0.978862037 129.892947668 130.41267595160 Jun-22 1.041909091 1.043559091 1.048081818 0.983262103 0.985626867 135.219624372 135.665839299
61 Jul-22 1.042185714 1.043904762 1.048609524 1.024899427 1.027628922 138.337399489 138.83515044862 Aug-22 1.038578261 1.040091304 1.046786957 1.021388945 1.026202859 136.969463313 137.387136348
63 Sep-22 1.046418182 1.048063636 1.054377273 1.053658475 1.057867396 145.220772836 145.51235635764 Oct-22 1.054995238 1.055642857 1.061238095 1.067527149 1.070022143 149.136200098 149.499417303
65 Nov-22 1.051572727 1.052318182 1.057854545 1.029162605 1.030744738 144.530394800 145.15268520766 Dec-22 1.045750000 1.046704545 1.052431818 0.984686940 0.985523039 137.117368043 137.729819737
67 Jan-23 1.046045455 1.047922727 1.053063636 0.967964145 0.968754216 132.675899066 133.43901694168 Feb-23 1.047985000 1.049430000 1.054275000 0.973490434 0.974423025 135.246103575 136.060080935
69 Mar-23 1.048434783 1.049639130 1.054482609 0.974710074 0.975615344 135.704763153 136.41736847270 Apr-23 1.044855000 1.046790000 1.053030000 0.950800447 0.952172039 135.454127047 136.148060972
71 May-23 1.044904348 1.046534783 1.053452174 0.958143405 0.960986776 138.772782132 139.62638510172 Jun-23 1.047872727 1.048040909 1.053422727 0.960416127 0.963681959 142.669448586 143.438436624
73 Jul-23 1.049514286 1.048919048 1.053419048 0.941591393 0.944172932 142.279925429 143.06124776874 Aug-23 1.051347826 1.052043478 1.055560870 0.955606620 0.958428626 146.302580736 147.324667658
75 Sep-23 1.053990476 1.056457143 1.057528571 0.978183227 0.981417535 149.456017683 150.47157202976 Oct-23 1.056786364 1.061250000 1.062613636 0.990247628 0.992950972 151.353774879 152.467565242
77 Nov-23 1.053822727 1.057800000 1.059181818 0.964295620 0.967225547 151.572099170 152.49881628878 Dec-23 1.047657143 1.050457143 1.052338095 0.950717478 0.953544108 145.685761022 146.467854817
79 Jan-24 1.047634783 1.050356522 1.053104348 0.951341713 0.953704985 147.940414460 148.75120283480 Feb-24 1.049371429 1.050028571 1.053857143 0.961013109 0.963006495 151.376752248 152.221934507
81 Mar-24 1.049685714 1.050290476 1.053366667 0.954096582 0.956127074 151.522722007 152.347722941
143
Lanjutan dari halaman sebelumnya
t Periode C10,t C20,t C30,t C41,t C51,t C62,t C72,t
82 Apr-24 1.052436364 1.053268182 1.056013636 0.967801948 0.969816240 155.747242450 156.59636550083 May-24 1.052308696 1.052743478 1.055691304 0.960605433 0.962134631 157.829585227 158.740945025
84 Jun-24 1.051080000 1.051415000 1.054480000 0.964633950 0.966275251 159.817227210 160.80685155085 Jul-24 1.050308696 1.051013043 1.054726087 0.956678242 0.958608765 159.470859383 160.463223929
86 Aug-24 1.046731818 1.047768182 1.051618182 0.939454286 0.941695002 147.965807123 148.76055300687 Sep-24 1.044014286 1.046190476 1.050376190 0.931080562 0.933576009 144.636023993 145.386736713
88 Oct-24 1.046030435 1.048604348 1.052160870 0.951080121 0.950926464 151.706804870 152.51406517089 Nov-24 1.049571429 1.051233333 1.054338095 0.976105894 0.976454764 155.626353842 156.550898723
90 Dec-24 1.050763636 1.052445455 1.055095455 0.989403601 0.989976997 155.782339500 156.69823365691 Jan-25 1.052450435 1.054943478 1.057770870 1.002187126 1.003011326 158.618835260 159.625149979
92 Feb-25 1.050120000 1.053375500 1.056523500 0.995378556 0.999161956 153.854928998 154.82930689493 Mar-25 1.049054286 1.052215238 1.056552857 0.961206456 0.964865957 151.382137127 152.398923028
94 Apr-25 1.049328182 1.053333182 1.058945455 0.923810821 0.927563251 145.717197255 146.71139846495 May-25 1.048175455 1.054558636 1.058282727 0.920687929 0.925384453 146.947344485 148.134289893
96 Jun-25 1.045328571 1.052589524 1.056942381 0.898383567 0.902873891 146.663943765 147.87766145297 Jul-25 1.044469130 1.051880435 1.056030435 0.887150799 0.891209329 149.950715302 150.635545071
98 Aug-25 1.043409524 1.050992381 1.055286667 0.887931705 0.892397518 150.339771478 151.06036619799 Sep-25 1.043078182 1.049915455 1.054750909 0.881669641 0.886325217 150.821206158 151.589041053
100 Oct-25 1.042701739 1.049037826 1.053596522 0.889370017 0.893840071 154.353453033 155.337034221101 Nov-25 1.042453125 1.049150625 1.053332500 0.895557595 0.899973075 157.958303977 159.079032364
102 Dec-25 1.049740375 1.049914747 1.051846564 0.963841747 0.965702284 152.079134659 152.870504675103 Jan-26 1.049740375 1.049914747 1.051778210 0.963841747 0.965702284 152.079134659 152.870504675
104 Feb-26 1.049740375 1.049914747 1.051709969 0.963841747 0.965702284 152.079134659 152.870504675105 Mar-26 1.049740375 1.049914747 1.051641840 0.963841747 0.965702284 152.079134659 152.870504675
106 Apr-26 1.049740375 1.049914747 1.051573823 0.963841747 0.965702284 152.079134659 152.870504675107 May-26 1.049740375 1.049914747 1.051505918 0.963841747 0.965702284 152.079134659 152.870504675
108 Jun-26 1.049740375 1.049914747 1.051438125 0.963841747 0.965702284 152.079134659 152.870504675109 Jul-26 1.049740375 1.049914747 1.051370444 0.963841747 0.965702284 152.079134659 152.870504675
110 Aug-26 1.049740375 1.049914747 1.051302874 0.963841747 0.965702284 152.079134659 152.870504675111 Sep-26 1.049740375 1.049914747 1.051235414 0.963841747 0.965702284 152.079134659 152.870504675
112 Oct-26 1.049740375 1.049914747 1.051168066 0.963841747 0.965702284 152.079134659 152.870504675113 Nov-26 1.049740375 1.049914747 1.051100828 0.963841747 0.965702284 152.079134659 152.870504675
144
Lampiran 20
Data Persentase Perubahan Biaya Utang Valas
t r10,t r20,t r30,t r41,t r51,t r62,t r72,t
1 -0.001660056 -0.001734531 -0.001072776 -0.024724630 -0.025703061 -0.023396014 -0.023532661
2 -0.001225284 -0.001707556 -0.001385363 -0.009840145 -0.009370147 0.008591573 0.008480992
3 0.000236728 0.001023820 0.000297404 0.012875380 0.012569282 0.019322537 0.019680739
4 0.002398419 0.000374230 -0.000149217 0.000173198 -0.000112431 -0.001209364 -0.001024246
5 0.000877522 0.000057518 -0.000749803 -0.009118257 -0.009108037 0.001044524 0.001105561
6 0.000597157 0.000477492 0.000366338 -0.030975146 -0.030753364 -0.018190985 -0.018117054
7 0.003720675 0.003936739 0.003165247 -0.009657880 -0.010757534 -0.026253719 -0.026100908
8 0.002178329 0.001234243 0.001045685 0.002086988 0.001932749 -0.018082578 -0.018131284
9 0.000330820 0.000198747 -0.000290137 0.004560140 0.004899011 0.013932909 0.014471718
10 0.002618712 0.003242627 0.002666111 0.040010444 0.038203558 0.018481660 0.019136859
11 0.000338148 -0.000041101 0.000281887 0.014313395 0.014152504 0.004236500 0.003386107
12 -0.000727304 -0.001295122 -0.001936133 -0.000150219 -0.000762744 0.015527731 0.013156475
13 -0.000684172 0.000178224 -0.000621109 0.011526582 0.011305921 -0.004418857 -0.004274414
14 0.001097697 0.001730541 0.002267852 -0.008266876 -0.007689687 0.009838258 0.009721098
15 0.001869541 0.001863975 0.001632738 0.016008107 0.016704916 0.005562349 0.005614667
16 0.001488905 0.001066546 0.001811248 0.012668300 0.011926615 0.005051368 0.004903292
17 -0.001604793 -0.002070708 -0.002215205 -0.002136041 -0.002055848 -0.010458809 -0.010842809
18 -0.002770881 -0.002352508 -0.002541076 -0.006758246 -0.005940358 -0.029063081 -0.023698835
19 -0.002231070 -0.001942731 -0.000719550 0.002732970 0.002665054 0.013383498 0.013328733
20 -0.001510684 -0.000946242 -0.000677068 0.003681618 0.002824090 0.006143133 0.006170626
21 -0.001669674 -0.001596515 -0.001690819 0.004257088 0.004199660 0.004562223 0.004394267
22 -0.000771596 -0.000219806 -0.000244811 0.003908865 0.004215247 -0.015179447 -0.015144615
23 -0.002296470 -0.003736562 -0.003076138 -0.011098963 -0.011479615 -0.017993618 -0.018090227
24 -0.002502323 -0.002264225 -0.001512845 0.004335006 0.003090197 0.003059606 0.001819225
25 -0.001873731 -0.002880545 -0.002736028 0.006159248 0.005263838 -0.019496221 -0.020214131
26 -0.001463075 -0.001289601 -0.001411165 0.010489813 0.009997923 0.011904204 0.012879254
27 0.000474021 0.000698287 0.000314000 -0.003828065 -0.003734013 0.005689423 0.005857543
28 -0.000236656 0.000663134 0.000157011 0.002833678 0.005989584 0.007354618 0.007364519
29 -0.000773726 -0.000556524 -0.002185125 -0.006237332 -0.006054831 0.002831583 0.002746716
30 -0.000802426 -0.000558264 -0.000272776 0.000599883 0.000927968 0.001507465 0.002222811
31 -0.001146283 -0.002159267 -0.001779977 0.016211794 0.015698285 0.006061507 0.006105409
32 0.008773224 0.004689169 0.002671041 -0.000484925 -0.004142044 -0.020808589 -0.022413289
33 0.002243092 0.002804373 0.001224077 0.024168796 0.022643281 0.005364212 0.003360813
34 -0.006575748 -0.004683113 -0.002507928 -0.007226487 -0.004999115 -0.003946125 -0.000517045
35 -0.005477655 -0.003289347 -0.001011610 -0.037065483 -0.036333667 0.003469271 0.003597800
36 -0.002347290 -0.000863570 -0.000643179 -0.021691315 -0.021493884 -0.009369857 -0.009168402
37 -0.005371360 -0.003199702 -0.001618877 -0.032187444 -0.031440621 -0.006284980 -0.006238624
38 -0.000426596 0.000142368 0.000806394 0.003268176 0.003589540 -0.004044054 -0.004063050
39 -0.000956504 -0.000431936 -0.000753946 0.001111346 0.001092542 -0.003676181 -0.003508309
40 -0.000057134 -0.001600345 -0.001000185 -0.007521546 -0.007065104 -0.009506640 -0.007786663
41 0.000350181 0.000505706 0.000445974 -0.030366061 -0.030275024 -0.007890829 -0.005883551
42 0.000415259 0.000437815 0.000599188 -0.001241510 -0.001936740 -0.000748267 -0.003770386
43 0.000233494 0.001402546 0.001177165 0.007814603 0.006314952 0.014391583 0.015394969
44 0.003897056 0.003414797 0.002472756 0.018242487 0.015937611 0.031378238 0.031586586
45 -0.000319427 -0.003349861 -0.000878616 -0.007096628 -0.005258995 0.002483677 0.002948171
46 -0.001538045 0.000943726 0.000381263 -0.015037418 -0.014543356 0.000407226 -0.000254663
47 -0.001138491 -0.001614995 -0.001085781 0.008276557 0.008938228 0.008554273 0.007605517
48 -0.000051524 -0.000136607 -0.000942039 0.018698855 0.020125190 0.000799956 -0.000581514
49 -0.000798894 0.000484198 0.000358330 0.007269178 0.005973684 -0.003174606 -0.003142077
50 -0.000316584 -0.000004003 0.000183061 0.000563524 0.001829696 0.003121778 0.003293641
51 0.003019227 0.002714065 0.002193399 0.016861384 0.015695639 0.027085191 0.027353425
52 0.000217835 -0.001272505 -0.001128835 0.016238564 0.016318884 0.007364872 0.007203631
53 0.002794833 -0.001028224 -0.000777921 0.009979267 0.010177737 -0.001200655 -0.001299870
54 0.003372624 0.002825033 0.002888237 0.000361554 -0.000014292 0.009211255 0.009661497
55 0.003636719 0.003095432 0.001949275 0.002673644 0.001604242 0.004614995 0.004843352
56 0.003004371 0.003022178 0.001830741 0.033955538 0.033555532 0.029368256 0.029104447
57 0.004453830 0.004464167 0.002611460 0.022652867 0.022784297 0.066191626 0.066714660
58 0.005485074 0.005095724 0.004186054 0.028232566 0.028478680 0.019500751 0.019734515
59 0.001870695 0.002138869 0.000642277 0.006778161 0.006910912 0.041008206 0.040281079
145
Lanjutan dari halaman sebelumnya
t r10,t r20,t r30,t r41,t r51,t r62,t r72,t
60 0.000265497 0.000331242 0.000503497 0.042346108 0.042614560 0.023057120 0.023361158
61 -0.003461430 -0.003653070 -0.001738080 -0.003425196 -0.001387722 -0.009888405 -0.010429737
62 0.007548705 0.007665031 0.007251061 0.031593772 0.030856021 0.060241964 0.059141054
63 0.008196586 0.007231642 0.006506990 0.013162399 0.011489859 0.026961895 0.027400154
64 -0.003244101 -0.003149432 -0.003188304 -0.035937769 -0.036707096 -0.030883215 -0.029075244
65 -0.005537161 -0.005334543 -0.005126156 -0.043215391 -0.043872840 -0.051290435 -0.051138327
66 0.000282529 0.001163826 0.000600341 -0.016982854 -0.017015150 -0.032391732 -0.031153768
67 0.001854169 0.001438343 0.001150323 0.005709187 0.005851648 0.019372053 0.019642411
68 0.000429188 0.000199280 0.000196921 0.001252852 0.001223615 0.003391296 0.002625954
69 -0.003414407 -0.002714390 -0.001377556 -0.024529988 -0.024029250 -0.001846922 -0.001974144
70 0.000047229 -0.000243810 0.000400913 0.007722922 0.009257505 0.024500214 0.025548099
71 0.002840815 0.001439156 -0.000027953 0.002372006 0.002804599 0.028079472 0.027301799
72 0.001566563 0.000837886 -0.000003493 -0.019600602 -0.020244258 -0.002730249 -0.002629622
73 0.001747037 0.002978715 0.002033210 0.014884617 0.015098605 0.028272824 0.029801361
74 0.002513583 0.004195325 0.001864129 0.023625419 0.023986042 0.021554213 0.021360336
75 0.002652669 0.004536727 0.004808442 0.012333478 0.011751814 0.012697764 0.013264919
76 -0.002804386 -0.003250883 -0.003229601 -0.026207595 -0.025908051 0.001442477 0.000204968
77 -0.005850685 -0.006941631 -0.006461330 -0.014080891 -0.014145035 -0.038835235 -0.039547595
78 -0.000021343 -0.000095788 0.000728143 0.000656593 0.000168715 0.015476141 0.015589414
79 0.001657683 -0.000312228 0.000714834 0.010166059 0.009753026 0.023227850 0.023332461
80 0.000299499 0.000249426 -0.000465411 -0.007197120 -0.007143691 0.000964281 0.000826349
81 0.002620450 0.002835126 0.002512866 0.014364757 0.014317309 0.027880442 0.027887798
82 -0.000121307 -0.000498167 -0.000305235 -0.007435938 -0.007920685 0.013370014 0.013694951
83 -0.001167619 -0.001261920 -0.001147404 0.004193727 0.004303576 0.012593596 0.013014327
84 -0.000733821 -0.000382301 0.000233373 -0.008247385 -0.007934060 -0.002167275 -0.002136897
85 -0.003405549 -0.003087366 -0.002946647 -0.018003917 -0.017644073 -0.072145170 -0.072930548
86 -0.002596207 -0.001505777 -0.001181029 -0.008913392 -0.008621681 -0.022503734 -0.022679509
87 0.001931151 0.002307297 0.001699086 0.021479945 0.018584941 0.048886720 0.049023237
88 0.003385173 0.002507128 0.002069290 0.026313003 0.026845714 0.025836343 0.026468598
89 0.001135900 0.001153047 0.000718327 0.013623221 0.013848294 0.001002309 0.000941131
90 0.001605307 0.002373542 0.002535709 0.012920435 0.013166295 0.018208070 0.018678681
91 -0.002214294 -0.001486315 -0.001179244 -0.006793712 -0.003837813 -0.030033673 -0.030044408
92 -0.001014850 -0.001101470 0.000027787 -0.034330758 -0.034324765 -0.016072230 -0.015697182
93 0.000261089 0.001062467 0.002264532 -0.038904893 -0.038661024 -0.037421455 -0.037319979
94 -0.001098538 0.001163406 -0.000625837 -0.003380445 -0.002348949 0.008442018 0.009698575
95 -0.002716037 -0.001867239 -0.001266530 -0.024225757 -0.024325632 -0.001928587 -0.001732404
96 -0.000822173 -0.000673661 -0.000862815 -0.012503310 -0.012919370 0.022410222 0.018649765
97 -0.001014493 -0.000844254 -0.000704306 0.000880240 0.001333232 0.002594560 0.002820192
98 -0.000317557 -0.001024676 -0.000507689 -0.007052416 -0.006804479 0.003202311 0.003499759
99 -0.000360896 -0.000835904 -0.001094464 0.008733856 0.008478664 0.023420094 0.024724697
100 -0.000238433 0.000107526 -0.000250591 0.006957259 0.006861411 0.023354521 0.024089543
101 0.006990482 0.000728325 -0.001410700 0.076247640 0.073034639 -0.037219755 -0.039027945
102 0.000000000 0.000000000 -0.000064985 0.000000000 0.000000000 0.000000000 0.000000000
103 0.000000000 0.000000000 -0.000064882 0.000000000 0.000000000 0.000000000 0.000000000
104 0.000000000 0.000000000 -0.000064779 0.000000000 0.000000000 0.000000000 0.000000000
105 0.000000000 0.000000000 -0.000064677 0.000000000 0.000000000 0.000000000 0.000000000
106 0.000000000 0.000000000 -0.000064574 0.000000000 0.000000000 0.000000000 0.000000000
107 0.000000000 0.000000000 -0.000064472 0.000000000 0.000000000 0.000000000 0.000000000
108 0.000000000 0.000000000 -0.000064370 0.000000000 0.000000000 0.000000000 0.000000000
109 0.000000000 0.000000000 -0.000064269 0.000000000 0.000000000 0.000000000 0.000000000
110 0.000000000 0.000000000 -0.000064167 0.000000000 0.000000000 0.000000000 0.000000000
111 0.000000000 0.000000000 -0.000064066 0.000000000 0.000000000 0.000000000 0.000000000
112 0.000000000 0.000000000 -0.000063965 0.000000000 0.000000000 0.000000000 0.000000000
146
Lampiran 21
Output Minitab Plot Box-Cox
1. IR USD 5Y
```
(a) Data Asli (b) Transformasi Pertama
```
2. IR USD 10Y
```
(a) Data Asli (b) Transformasi Pertama (c) Transformasi Kedua
```
3. IR USD 30Y
```
(a) Data Asli (b) Transformasi Pertama (c) Transformasi Kedua
```
147
4. IR EUR 7Y
```
(a) Data Asli (b) Transformasi Pertama
```
5. IR EUR 10Y
```
(a) Data Asli (b) Transformasi Pertama
```
6. IR JPY 5Y
```
(a) Data Asli (b) Transformasi Pertama (c) Transformasi Kedua
```
148
7. IR JPY 10Y
```
(a) Data Asli (b) Transformasi Pertama
```
8. FX USD EUR
```
(a) Data Asli (b) Transformasi Pertama
```
9. FX USD JPY
```
(a) Data Asli (b) Transformasi Pertama
```
149
Lampiran 22
Plot ACF dan PACF pada Data yang Telah Stasioner
```
(a) Plot ACF Data ∆Z1 (b) Plot PACF Data ∆Z1
```
```
(a) Plot ACF Data ∆Z2 (b) Plot PACF Data ∆Z2
```
```
(a) Plot ACF Data ∆2Z3 (b) Plot PACF Data ∆2Z3
```
150
```
(a) Plot ACF Data ∆Z4 (b) Plot PACF Data ∆Z4
```
```
(a) Plot ACF Data ∆Z5 (b) Plot PACF Data ∆Z5
```
```
(a) Plot ACF Data ∆Z6 (b) Plot PACF Data ∆Z6
```
151
```
(a) Plot ACF Data ∆Z7 (b) Plot PACF Data ∆Z7
```
```
(a) Plot ACF Data ∆Z8 (b) Plot PACF Data ∆Z8
```
```
(a) Plot ACF Data ∆Z9 (b) Plot PACF Data ∆Z9
```
152
Lampiran 23
Plot Perbandingan Data Training dan Data Hasil Peramalan
```
(a) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(0, 1, 1)
```
pada Suku Bunga USD Tenor 5 Tahun
```
(b) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(1, 1, 0)
```
pada Suku Bunga USD Tenor 10 Tahun
```
(a) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA([2], 2, 2)
```
pada Suku Bunga USD Tenor 30 Tahun
```
(b) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(0, 1, 1)
```
pada Suku Bunga EUR Tenor 7 Tahun
```
(a) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(0, 1, 1)
```
pada Suku Bunga EUR Tenor 10 Tahun
```
(b) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(1, 1, 0)
```
pada Suku Bunga JPY Tenor 5 Tahun
153
```
(a) Plot Perbandingan Data Training
```
dan Data Hasil Peramalan Model
```
ARIMA(0, 1, [14]) pada Suku Bunga JPY
```
Tenor 10 Tahun
```
(b) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(0, 1, 1)
```
pada Nilai Tukar USD/EUR
```
(a) Plot Perbandingan Data Training dan
```
```
Data Hasil Peramalan Model ARIMA(0, 1, 1)
```
pada Nilai Tukar USD/JPY
154
Lampiran 24
Matriks Varians-Kovarians Portofolio Utang Valas
Matriks varians-kovarians portofolio utang valas berdasarkan gabungan data historis dan data hasil peramalan dinotasikan dengan
Σ
, yaitu sebagai berikut.
Σ
= 10
−6

6,
970413652417

5,
595142001835

4,
216836210849

28
,588488162929

27
,359207509166

24
,097269845969

23
,648643875350
5,
595142001835

5,
618087029497

4,
380873912749

22
,069277343700

21
,235456997016

26
,485546617807

26
,328836563041
4,
216836210849

4,
380873912749

3,
866458063852

15
,076121824917

14
,570856579239

22
,179341644473

22
,162889117657
28
,588488162929 22
,069277343700 15
,076121824917 316
,361639308664 311
,314788182334 187
,060213839477 184
,639820086248
27
,359207509166 21
,235456997016 14
,570856579239 311
,314788182334 307
,235262199714 185
,555752488117 183
,393357615938
24
,097269845969 26
,485546617807 22
,179341644473 187
,060213839477 185
,555752488117 415
,252197984462 414
,466028812572
23
,648643875350 26
,328836563041 22
,162889117657 184
,639820086248 183
,393357615938 414
,466028812572 414
,733134811496

.
155
Lampiran 25
Plot Efficient Frontier Model MVO dan CVaR
```
(a) Kemenkeu (b) Diperlebar 5% (c) Tanpa Batasan
```
Plot Efficient Frontier Model MVO Berdasarkan Gabungan Data Historis dan
Data Hasil Peramalan
```
(a) Kemenkeu (b) Diperlebar 5% (c) Tanpa Batasan
```
Plot Efficient Frontier Model CVaR pada Tingkat Kepercayaan 90% Berdasarkan
Gabungan Data Historis dan Data Hasil Peramalan
```
(a) Kemenkeu (b) Diperlebar 5% (c) Tanpa Batasan
```
Plot Efficient Frontier Model CVaR pada Tingkat Kepercayaan 95% Berdasarkan
Gabungan Data Historis dan Data Hasil Peramalan
```
(a) Kemenkeu (b) Diperlebar 5% (c) Tanpa Batasan
```
Plot Efficient Frontier Model CVaR pada Tingkat Kepercayaan 99% Berdasarkan
Gabungan Data Historis dan Data Hasil Peramalan
156
UCAPAN TERIMA KASIH
Segala puji dan syukur penulis panjatkan ke hadirat Allah SWT atas limpahan
rahmat, nikmat, kesehatan, dan kekuatan sehingga penulis dapat menyelesaikan Tugas
Akhir ini dengan baik. Penyelesaian Tugas Akhir ini tidak terlepas dari doa, dukungan,
bimbingan, bantuan, serta motivasi dari berbagai pihak. Oleh karena itu, dengan penuh
rasa hormat dan kerendahan hati, penulis mengucapkan terima kasih yang sebesar-
besarnya kepada:
1. Orang tua penulis, Rustamaji dan Siti Romelah, adik penulis, Erica Kirana Larasati,
serta keluarga besar penulis yang senantiasa memberikan doa, dukungan, kasih
sayang, motivasi, dan semangat selama masa perkuliahan hingga penyusunan Tugas
Akhir ini.
2. Ibu Sena Safarina, S.Si., M.Sc., D.Sc. dan Ibu Dra. Laksmi Prita Wardhani,
M.Si., selaku dosen pembimbing yang telah memberikan bimbingan, arahan,
ilmu, motivasi, serta masukan yang sangat berarti kepada penulis selama proses
penyusunan Tugas Akhir ini.
3. Bapak Jasmir, S.Pd., M.Si. dan pihak pengelola utang negara Republik Indonesia
yang telah memberikan topik, data, dan informasi yang digunakan dalam penelitian
ini.
4. Bapak Prof. Dr. Mahmud Yunus, M.Si., Ibu Dr. Valeriana Lukitosari, S.Si.,
M.T., dan Ibu Endah Rokhmati Merdika Putri, S.Si., M.T., Ph.D., selaku dosen
penguji yang telah memberikan kritik, saran, dan masukan yang membangun untuk
penyempurnaan Tugas Akhir ini.
5. Bapak Prof. Dr. Mahmud Yunus, M.Si., selaku dosen wali yang telah memberikan
arahan, nasihat, dan pendampingan akademik kepada penulis selama masa
perkuliahan.
6. Bapak/Ibu dosen pengajar, seluruh karyawan, tenaga kependidikan, dan keluarga
besar Departemen Matematika Institut Teknologi Sepuluh Nopember yang telah
memberikan ilmu, bantuan, pengalaman, dan dukungan selama penulis menempuh
masa perkuliahan.
7. Rekan-rekan seperbimbingan Ibu Sena Safarina, S.Si., M.Sc., D.Sc. yang telah
memberikan dukungan, bantuan, semangat, dan kebersamaan selama proses
penyusunan Tugas Akhir ini.
8. Rekan-rekan seperbimbingan Ibu Dra. Laksmi Prita Wardhani, M.Si. yang
telah memberikan dukungan, bantuan, semangat, dan kebersamaan selama proses
penyusunan Tugas Akhir ini.
9. Agustinus Gabriel Situmorang dan Rama Darmawan Putra, selaku sahabat penulis
di Departemen Matematika Institut Teknologi Sepuluh Nopember yang senantiasa
menemani, membantu, dan memberikan dukungan kepada penulis di saat terpuruk
selama masa perkuliahan.
157
10. Teman-teman Matematika Institut Teknologi Sepuluh Nopember Angkatan 2022,
AXXIIOM, yang telah memberikan kebersamaan, dukungan, bantuan, cerita,
motivasi, dan pengalaman berharga selama masa perkuliahan.
11. Guru-guru penulis sejak jenjang taman kanak-kanak, sekolah dasar, sekolah
menengah pertama, hingga sekolah menengah atas yang telah memberikan
ilmu, nasihat, bimbingan, serta pengalaman belajar yang berharga sehingga
turut membentuk karakter, semangat, dan kepribadian penulis dalam menempuh
pendidikan.
12. dr. Sri Purwaningsih, M.Kes., selaku wali murid les penulis yang senantiasa
mendoakan, menyemangati, dan memberikan dukungan kepada penulis.
13. Noel, Affan, Hyuga, Kevin, dan murid les penulis lainnya yang telah memberikan
semangat dan motivasi kepada penulis untuk terus menekuni dunia pendidikan.
14. Anggota Viva GeoAnalytic, yaitu Agus, Dhanar, Ferdhika, Ilyas, Louise, Teo,
Zaky, dan Tito, selaku teman sepermainan yang telah menghibur penulis serta
memberikan kebersamaan selama masa perkuliahan.
15. Alif, Nopal, Angga, Bagus, Fezar, Zaky, dan Satrio, selaku teman sepermainan
penulis semasa SMA Negeri 1 Sidoarjo yang telah memberikan kebersamaan, cerita,
dan kenangan berharga bagi penulis.
16. Alfan, Andra, Dafa, Rizky, Adam, dan Manda, selaku teman satu almamater
sekaligus teman satu kelas penulis semasa SMA yang telah memberikan
kebersamaan, dukungan, dan pengalaman berharga.
17. Abdul, Aryan, Kahil, Vickyo, Rizky, dan Salu, selaku teman penulis semasa SMP
Negeri 5 Sidoarjo yang telah memberikan kebersamaan, canda tawa, dan kenangan
berharga bagi penulis.
18. Seluruh anggota Karang Taruna RT.04 RW.01 Pepelegi yang telah memberikan
kebersamaan, pengalaman, dan dukungan dalam perkembangan penulis di luar
bidang akademik.
19. Rama, Abi, Deris, Bima, Irsyad, Rachman, Dafa, Akmal, Robi, Aji, dan teman-
teman sekitar rumah lainnya yang telah memberikan kebersamaan, canda tawa,
dukungan, dan semangat kepada penulis di luar lingkungan perkuliahan.
20. Seluruh pihak yang tidak dapat disebutkan satu per satu, yang telah memberikan
doa, dukungan, bantuan, dan motivasi kepada penulis selama masa perkuliahan
hingga penyusunan Tugas Akhir ini.
Surabaya, 18 Juni 2026
Bagus Rico Pambudi
158
BIODATA PENULIS
Penulis bernama lengkap Bagus Rico Pambudi, lahir di Sidoarjo,
Jawa Timur. Sebelum melanjutkan ke jenjang perguruan tinggi,
penulis menempuh pendidikan formal di SDN Waru 1, SMP
Negeri 5 Sidoarjo, dan SMA Negeri 1 Sidoarjo. Pada tahun
2022, penulis melanjutkan pendidikan sarjana di Program Studi
S-1 Matematika, Fakultas Sains dan Analitika Data, Institut
```
Teknologi Sepuluh Nopember (ITS), dengan NRP 5002221144.
```
Saat ini, penulis menempuh semester 8 dan memiliki minat di
bidang riset optimasi dan keuangan, khususnya dalam penerapan
metode pemodelan dan analisis kuantitatif di bawah naungan
```
Laboratorium Matematika Industri dan Keuangan (MIKE).
```
Selama menempuh studi di ITS, penulis aktif dalam berbagai
kegiatan organisasi dan kepanitiaan yang mengembangkan kemampuan berpikir analitis,
kepemimpinan, dan kerja sama tim. Salah satu kegiatan kepanitiaan yang pernah diikuti
```
penulis adalah Olimpiade Matematika ITS (OMITS) 17th. Selain itu, penulis juga
```
memperoleh pengalaman dan wawasan melalui Kerja Praktik di Komisi Pemilihan Umum
```
(KPU) Jawa Timur. Melalui kegiatan tersebut, penulis dapat menerapkan pengetahuan
```
teoritis yang telah dipelajari selama perkuliahan ke dalam konteks dunia nyata. Penulis
berpegang pada prinsip hidup “Warisan paling berharga adalah ilmu” sebagai landasan
untuk terus belajar, mengembangkan diri, dan memberikan manfaat bagi orang lain. Ke
depannya, penulis berharap dapat terus mengembangkan diri di bidang riset optimasi
dan keuangan serta berkontribusi dalam menghasilkan inovasi dan solusi matematis yang
bermanfaat bagi masyarakat luas. Penulis dengan senang hati menerima informasi, kritik,
ataupun saran terkait penulisan laporan kerja praktik ini. Adapun untuk informasi lebih
lanjut, silakan menghubungi penulis melalui e-mail bagusrikop09@gmail.com.
159