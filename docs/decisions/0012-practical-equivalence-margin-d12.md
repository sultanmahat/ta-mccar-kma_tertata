# Keputusan D12: Margin Ekivalensi Praktis untuk Uji TOST

- **Tanggal Usulan**: 2026-10-25
- **Tanggal Konfirmasi**: 2026-10-25
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (Margin Relatif Seragam 0,01%)**

---

## Ringkasan Keputusan

Uji Kruskal-Wallis/Dunn Tahap 13 (`results/tables/stats_summary.md`) menghasilkan $p\ll0{,}001$ dan $\epsilon^2$ besar di keempat konfigurasi, tetapi selisih median biaya absolut sangat kecil (mis. `gross_djppr`: selisih KMA-PSO 0,0051% dari biaya ~1,04; `interest_djppr`: identik sampai desimal ke-6). Uji ekivalensi (TOST) membutuhkan ambang $\delta$ ("selisih yang dianggap tidak bermakna secara praktis") yang tidak ditentukan proposal/spesifikasi.

Ditetapkan:
- **Margin $\delta$ = 0,01% dari median biaya seluruh run pada `config_id` yang sama** (gabungan 30 replikasi × 3 algoritma = 90 run per konfigurasi), diterapkan seragam untuk keempat konfigurasi (`gross_free`, `gross_djppr`, `interest_free`, `interest_djppr`) dan untuk ketiga pasangan algoritma dalam satu konfigurasi (KMA-GA, KMA-PSO, GA-PSO berbagi margin yang sama). <!-- koreksi 2026-10-25 R3: sebelumnya tertulis "median biaya grup pembanding", yang bisa dibaca sebagai median per-pasangan; `scripts/20_analyze_practical_significance.py:59` sejak awal memakai median gabungan ketiga algoritma per config_id -- teks ini disamakan dengan implementasi, bukan sebaliknya; tidak ada angka hasil yang berubah. -->
- Nilai di `configs/params.yaml`: `practical_significance.equivalence_margin_pct: 0.01`.

---

## Alasan & Justifikasi Keputusan

1. **Kesederhanaan dan keterbandingan**: satu angka untuk seluruh konfigurasi memudahkan interpretasi lintas Bab 4 ("selisih di bawah 0,01% dianggap tidak bermakna secara praktis, di manapun itu muncul").
2. **Aman secara numerik**: margin 0,01% jauh lebih besar dari toleransi kelayakan solver (`optimization.eps_tol = 1e-8`), sehingga tidak ada risiko presisi numerik solver disalahartikan sebagai ekivalensi substantif.
3. **Keterbatasan yang disadari**: margin relatif 0,01% pada `interest_free`/`interest_djppr` (biaya absolut kecil, ~0,03–0,17) secara absolut jauh lebih longgar dibanding pada `gross_*` (~1,04). Ini dicatat sebagai keterbatasan di `docs/reviews/signifikansi_praktis.md`, bukan diabaikan — opsi margin berjenjang (per definisi biaya) dipertimbangkan tapi tidak dipilih demi kesederhanaan satu angka.

---

## Implikasi ke Dokumen & Kode

1. `configs/params.yaml` blok `practical_significance.equivalence_margin_pct: 0.01` — satu-satunya sumber nilai margin, dibaca oleh `scripts/20_analyze_practical_significance.py`.
2. `docs/reviews/signifikansi_praktis.md` mencantumkan hasil TOST dan CI-vs-margin dengan margin ini, serta mencatat keterbatasannya pada konfigurasi `interest_*` di bagian Keterbatasan.
3. Tidak mengubah Tahap 13 (`stats_summary.md`, `stats_<config_id>.csv`) — ini lapisan tambahan, bukan revisi.
