# Keputusan D13: Laju Mlipir (d) Fase 2 KMA

- **Tanggal Usulan**: 2026-10-25
- **Tanggal Konfirmasi**: —
- **Status**: **Diusulkan agen, menunggu konfirmasi Sultan**
- **Pihak yang Mengonfirmasi**: —
- **Pilihan yang Ditetapkan**: belum ditetapkan — mencatat nilai yang **sudah dipakai** di kode (bukan usulan nilai baru)

---

## Ringkasan Keputusan

Audit ulang (`docs/reviews/audit_ulang_2026-10-25.md`, temuan **T5**) menemukan bahwa laju mlipir Fase 2 KMA (`d = 0,5`) adalah literal di `src/mccar_kma/optimizers/kma.py:187`, tidak tercatat di Tabel 3.1 proposal, `docs/context/spesifikasi_model.md`, maupun D4 (`docs/decisions/0006-kma-parameters-d4.md`).

Berkas ini **hanya mencatat** nilai yang sudah dipakai sejak 360 run utama dijalankan:

| Parameter | Simbol | Nilai | Sumber |
|---|---|---|---|
| Laju mlipir Fase 2 | $d_2$ | $0{,}5$ | `kma.py:187` (sebelum refactor ini), identik di `configs/params.yaml` sejak diteruskan ke konstruktor (Tahap ini) |
| Lantai pembagi adaptasi populasi | — | $10^{-12}$ | `kma.py:399-400` (sebelum refactor ini), lihat juga R11 |

Nilai di `configs/params.yaml`:
```yaml
algorithms:
  kma:
    phase_2:
      mlipir_rate: 0.5
      population_adapt_floor: 1.0e-12
```

**Tidak ada nilai yang diubah.** Hasil 360 run utama (`results/runs/`) tetap sah — dibuktikan lewat reproduksi bit-identik 6 run contoh di `docs/reviews/` (lihat Walkthrough tugas refactor config-flow, 2026-10-25).

---

## Mengapa ini "diusulkan agen, menunggu konfirmasi" (bukan "diputuskan")

Laju $d_2 = 0,5$ tidak ditentukan proposal maupun D4. Ablasi Tahap 18 (`results/sensitivity/kma/ablation_tests.csv`) menunjukkan `kma_d2_low` signifikan lebih baik dari default pada `gross_free` (p_Holm = 0,0031) dan `interest_free` (p_Holm = 0,047) — artinya nilai ini **mempengaruhi hasil** dan pemilihannya bukan keputusan teknis netral seperti D5/D13-floor. Karena itu, agen tidak memilih sendiri apakah nilai 0,5 ini **dipertahankan untuk 360 run yang sudah ada** (Opsi A) atau **diubah lalu seluruh eksperimen diulang** (Opsi B) — itu keputusan Sultan.

- **Opsi A (dipertahankan)**: Tidak ada pekerjaan tambahan. 360 run tetap sah seperti sekarang.
- **Opsi B (ubah ke `kma_d2_low` lalu ulang eksperimen)**: Mengikuti temuan ablasi Tahap 18, tapi mengulang 360 run + seluruh analisis turunannya (Tahap 12, 13, 17, 18, 19, 20) — biaya komputasi dan dokumentasi besar.

Rekomendasi tidak diberikan di sini (di luar cakupan tugas refactor config-flow); keputusan menunggu Sultan.

---

## Implikasi ke Tahap Selanjutnya

1. `src/mccar_kma/optimizers/kma.py`: `phase_2_mlipir_rate` dan `population_adapt_floor` adalah parameter konstruktor (default = nilai di atas, tidak berubah).
2. `src/mccar_kma/experiments/runner.py` (`build_optimizer`) membaca kedua nilai ini dari `configs/params.yaml` saat membangun optimizer KMA untuk tiap run.
3. Jika Sultan memilih Opsi B di atas pada sesi berikutnya, cukup ubah `configs/params.yaml` (`algorithms.kma.phase_2.mlipir_rate`) — tidak perlu ubah kode lagi, karena jalur ini sudah mengalir dari config (itulah tujuan refactor ini).
