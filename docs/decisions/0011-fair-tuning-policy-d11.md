# Keputusan D11: Kebijakan Penalaan Parameter yang Adil (Fair Tuning Policy)

- **Tanggal Usulan**: 2026-10-18
- **Tanggal Konfirmasi**: 2026-10-18
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (Default Literatur / Status Quo Proposal)**

---

## Ringkasan Keputusan

Untuk menjamin perbandingan performa yang adil (*fair comparison*) antara **Komodo Mlipir Algorithm (KMA)**, **Genetic Algorithm (GA)**, dan **Particle Swarm Optimization (PSO)** tanpa bias selektif, eksperimen komparasi menetapkan **Opsi A**:
1. Seluruh algoritma menggunakan konfigurasi parameter default dari literatur rujukan penemunya masing-masing:
   - **KMA**: Mengikuti parameter default makalah penemu (*Suyanto, Ariyanto, & Ariyanto, 2022*) dan spesifikasi dua fase proposal ($p_{\text{bm}} = 0{,}5$, $\gamma = 0{,}1$, $p_{\text{mating}} = 0{,}5$, $\Delta n = 5$, Fase 1: $n=5$, $d=(D-1)/D$, Fase 2: $n_{\text{init}}=200$, $d=0{,}5$).
   - **GA**: Mengikuti literatur klasik (*Goldberg, 1989; Holland, 1992*) dengan ukuran populasi $n=50$, turnamen biner ($k=2$), probabilitas kawin silang $p_c = 0{,}9$, probabilitas mutasi $p_m = 1/D$, dan elitisme 2 individu.
   - **PSO**: Mengikuti kanonik *Constriction / Standard PSO* (*Eberhart & Shi, 2000; Clerc & Kennedy, 2002*) dengan ukuran swarm $n=50$, bobot inersia menurun linear $\omega \in [0{,}9 \to 0{,}4]$, koefisien akselerasi kognitif dan sosial $c_1 = c_2 = 1{,}49618$, dan batas kecepatan $v_{\text{max}} = 0{,}2 \times \text{rentang}$.
2. Tidak dilakukan prosedur penalaan hiperparameter (*hyperparameter tuning*) tambahan yang bersifat selektif pada salah satu algoritma.

---

## Alasan & Justifikasi Keputusan

1. **Konsistensi terhadap Naskah Proposal**: Tabel 3.1 proposal tesis pasca-seminar proposal telah menetapkan parameter default untuk ketiga algoritma. Mempertahankan konfigurasi default menjaga fidelitas komitmen penelitian formal yang telah disetujui komisi pembimbing.
2. **Pencegahan Bias Peneliti (*Researcher Degree of Freedom / Cherry-Picking*)**: Melakukan penalaan hiperparameter secara bebas pada masalah portofolio MCCaR rentan menimbulkan bias komparasi, di mana algoritma yang di-tune lebih intensif akan tampak lebih unggul secara artifisial.
3. **Keterbukaan terhadap Hasil Empiris**: Perbedaan kinerja yang muncul dieksplorasi secara ilmiah melalui **diagnosis mekanistik** (analisis ledakan langkah interaksi, dinamika populasi Fase 2, dan interaksi tebing penalti) dan dilaporkan secara jujur dan transparan di Bab 4 dan Bab 5, bukan ditutupi dengan intervensi tuning sepihak.

---

## Implikasi ke Dokumen & Kode

1. Konfigurasi di `configs/params.yaml` tetap menggunakan parameter standar yang telah ditetapkan pada Keputusan D4 dan D6.
2. Hasil komparasi 360 run dipertahankan sebagai representasi murni kinerja *out-of-the-box* literatur.
3. Temuan sensitivitas parameter (pengaruh ukuran populasi $n$, laju mlipir $d_2$, dan skala interaksi $q$) disajikan sebagai bab diagnosis ilmiah (*Ablation Study*) pada `docs/reviews/diagnosis_kma.md` dan dilaporkan sebagai saran riset lanjutan pada Bab 5 naskah skripsi.
