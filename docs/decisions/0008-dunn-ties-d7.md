# Keputusan D7: Penanganan Koreksi Ties pada Uji Lanjut Dunn

- **Tanggal**: 2026-10-18
- **Status**: DIPUTUSKAN
- **Diputuskan oleh**: Sultan Bakri Baihaqi Mahat (Mahasiswa)

---

## Ringkasan Keputusan

Untuk pengujian statistik komparatif non-parametrik pasca uji Kruskal–Wallis (Persamaan 2.37 dan 2.38 pada proposal skripsi), ditetapkan keputusan sebagai berikut:

| Butir Keputusan | Pilihan Terpilih | Dasar Pertimbangan / Rujukan |
|---|---|---|
| **D7: Koreksi Ties Uji Dunn** | **Menggunakan faktor koreksi ties $C_{\text{ties}}$** pada variansi standar $SE_{A,B}$ uji Dunn | Menjamin konsistensi teoretis penuh dengan koreksi ties pada uji Kruskal–Wallis (Glantz, 2012; Dinno, 2015). |

---

## Rumus Matematis yang Diimplementasikan

Sesuai Persamaan 2.38 proposal dan rujukan Glantz (2012):
$$z_{A,B} = \frac{\bar{R}_A - \bar{R}_B}{\sigma_R \sqrt{\frac{1}{n_A} + \frac{1}{n_B}}}$$

dengan variansi gabungan berperingkat yang memperhitungkan kelompok nilai kembar (*ties*):
$$\sigma_R^2 = \frac{N(N+1)}{12} \times C_{\text{ties}}$$

di mana faktor koreksi ties dihitung dari ukuran kelompok ties $t_j$:
$$C_{\text{ties}} = 1 - \frac{\sum_{j=1}^g (t_j^3 - t_j)}{N^3 - N}$$

Bila tidak ada nilai kembar ($g=0$), maka $C_{\text{ties}} = 1$ dan variansi kembali ke formula klasik tanpa koreksi:
$$\sigma_R^2 = \frac{N(N+1)}{12}$$

---

## Alasan Keputusan

1. **Konsistensi Teoretis**:
   Uji Kruskal–Wallis (Pers. 2.37) telah menggunakan koreksi ties $H = H_{\text{raw}} / C_{\text{ties}}$. Menggunakan variansi terkoeksi ties yang sama pada uji Dunn mencegah terjadinya diskrepansi di mana Kruskal–Wallis menolak $H_0$ secara signifikan namun uji post-hoc menghasilkan galat baku (*standard error*) yang terdistorsi akibat asumsi kontinuitas mutlak.
2. **Karakteristik Data Eksperimen**:
   Pada konfigurasi berbatas aktif (khususnya `interest_djppr`), algoritma metaheuristik kerap mengonvergensi ke titik batas proporsi instrumen yang identik (menghasilkan biaya $Cost$ yang sama persis hingga toleransi $10^{-8}$). Koreksi ties menjamin presisi perhitungan $z$-statistik dan nilai $p_{\text{Holm}}$.
3. **Verifikasi Silang**:
   Formula mandiri telah divalidasi terhadap pengujian analitis manual dan pustaka `scipy.stats` pada berkas pengujian `tests/test_stats.py`.
