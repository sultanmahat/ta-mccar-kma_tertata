# Keputusan D5: Penanganan Pembagian Nol pada $\theta_i$ (Evaluator Risiko MCCaR)

- **Tanggal Usulan**: 2026-10-18
- **Tanggal Konfirmasi**: 2026-10-24
- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat
- **Pilihan yang Ditetapkan**: **Opsi A (toleransi nol 1e-12 => theta_i = 0.0 netral)**

## Ringkasan Keputusan

Pada perhitungan rasio risiko marjinal terhadap biaya marjinal $\theta_i(w) = \frac{\text{MCCaR}_{\alpha,i}(w)}{\text{MC}_i(w)}$ (Persamaan 2.18):
Jika nilai mutlak biaya marjinal instrumen ke-$i$ mendekati atau sama dengan nol ($|\text{MC}_i| \le \text{zero\_tolerance\_mc} = 10^{-12}$), maka nilai $\theta_i$ ditetapkan sama dengan $0{,}0$ (netral).

Nilai di `configs/params.yaml`:
```yaml
risk:
  zero_tolerance_mc: 1.0e-12
```

---

## Alasan Keputusan

1. **Interpretasi Finansial**:
   Jika suatu instrumen memiliki biaya marjinal nol ($\text{MC}_i = 0$), instrumen tersebut tidak menambah rata-rata beban biaya portofolio saat diterbitkan tambahan $\delta$. Dalam konteks penyeimbangan risiko MCCaR, kontribusi risiko marjinal instrumen tersebut dinilai netral ($\theta_i = 0$).
2. **Kondisi Data Riil DJPPR**:
   Dari Persamaan 2.16:
   $$\text{MC}_i = \delta \cdot \overline{C}_i$$
   Karena seluruh biaya instrumen $C_{s,i} > 0$ secara ketat pada data pasar empiris:
   - Pada definisi biaya bruto: $\overline{C}_i \approx 0{,}99 - 1{,}05 \implies \text{MC}_i \approx 0{,}01 \times 1{,}0 = 0{,}010 \gg 10^{-12}$.
   - Pada definisi biaya bunga: $\overline{C}_i \approx 0{,}023 - 0{,}055 \implies \text{MC}_i \approx 0{,}01 \times 0{,}03 = 0{,}0003 \gg 10^{-12}$.
   Oleh karena itu, kondisi $|\text{MC}_i| \le 10^{-12}$ tidak pernah terjadi pada data pasar riil kita, namun guard condition ini penting untuk melindungi kestabilan kode numerik pada kasus batas tiruan (*edge cases*) dan kasus pengujian sintetis.
3. **Mencegah Ledakan Nilai (*Numerical Explosion*)**:
   Menetapkan $\theta_i = 0{,}0$ jauh lebih stabil dibandingkan membagi dengan nilai kecil $\epsilon$, yang dapat menyebabkan nilai $\theta_i$ meledak ke $\pm 10^{12}$ dan merusak dispersi $J_{\text{MCCaR}}$.

---

## Implikasi ke Tahap Selanjutnya

1. `src/mccar_kma/risk/mccar.py` dan `evaluator.py` mengimplementasikan guard ini secara konsisten dengan toleransi $10^{-12}$.
2. Evaluator fungsi objektif terlindungi penuh dari `ZeroDivisionError` maupun `FloatingPointError` selama 9 juta evaluasi metaheuristik pada Tahap 06.
