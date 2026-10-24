# Keputusan D1: Pemilihan Varian Jendela Data (`window_mode`)

- **Tanggal Usulan**: 2026-10-18
- **Status**: Diusulkan agen / Menunggu konfirmasi Sultan
- **Diusulkan oleh**: Agen AI (Pair Programming)
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat (Mahasiswa)

## Keputusan

Gunakan **Opsi A `intersection`**: dataset 2.028 baris dengan hanya baris yang
memiliki data lengkap dari seluruh 9 seri pasar (7 yield + 2 kurs).

Nilai di `configs/params.yaml`:
```yaml
data:
  window_mode: "intersection"
```

## Alternatif yang Dipertimbangkan

| Opsi | Deskripsi | Baris | Alasan Ditolak |
|---|---|---|---|
| **A (intersection)** ✅ | Hanya baris lengkap | 2.028 | — dipilih |
| B (spline) | Isi 163 gap EUR_10Y via natural cubic spline | 2.191 | 163 hari artifisial mengurangi volatilitas EUR; korelasi EUR_7Y–EUR_10Y turun dari 0,7598 → 0,6728 |

## Alasan Keputusan

1. **Data murni**: Seluruh 2.028 baris adalah data pasar riil, tanpa rekayasa statistik.
2. **Konsisten dengan legacy**: Identik 100% dengan `legacy/data_v0/ir_data_clean.csv`
   dan `fx_data_clean.csv` (max diff = 0.0).
3. **Spesifikasi §2 menyebutkan 2.028**: Angka ini disebutkan eksplisit di dokumen
   spesifikasi model sebagai irisan bersih jendela analisis.
4. **Korelasi antar-seri lebih murni**: Nilai korelasi log-return EUR_7Y–EUR_10Y
   lebih tinggi dan lebih tepat merefleksikan co-movement pasar aktual.
5. **Penanganan celah**: 1 baris log-return yang melintasi celah 163 hari
   (2021-01-29 → 2021-09-16) dikeluarkan, sehingga total log-return valid = **2.026**.

## Implikasi ke Tahap Selanjutnya

- Tahap 03 (Kalibrasi GBM): Gunakan 2.026 log-return dari varian intersection.
- Varian spline (`data/processed/market_..._spline.csv`) dipertahankan sebagai
  data cadangan untuk analisis sensitivitas (opsional).
