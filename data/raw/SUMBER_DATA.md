# Data Mentah (raw)

Folder ini berisi **data sumber asli** yang tidak boleh diubah.

## Sumber utama
`Dataset_Utama_Optimum_Utang_Valas.xlsx` — dataset utama dari Direktorat Jenderal Pengelolaan Pembiayaan dan Risiko (DJPPR), Kementerian Keuangan RI.

Sheet:
1. **Data IR** — yield (%) harian 7 instrumen + kolom `Kategori` (Sebelum Covid / Covid / Setelah Covid).
2. **Data FX** — kurs harian `FX_USD/EUR` dan `FX_USD/JPY` (unit mata uang per 1 USD).
3. **Data Awal** — `Instrument, Curr, Tenor (yr), Existing (2024), Min, Max`.
4. **Data IR_formula** — duplikat Data IR; diabaikan.

Penanda data hilang: teks `#N/A N/A` dan `#N/A` (dibaca sebagai NaN).

## Instrumen (7)
| Instrumen | Mata Uang | Tenor | Existing 2024 | Min | Max |
|-----------|-----------|-------|---------------|-----|-----|
| USD_Fixed_5Y  | USD | 5  | 45,95% | 42,5% | 49,0% |
| USD_Fixed_10Y | USD | 10 | 11,36% | 10,0% | 12,5% |
| USD_Fixed_30Y | USD | 30 | 14,78% | 13,0% | 16,5% |
| EUR_Fixed_7Y  | EUR | 8  | 14,39% | 13,0% | 15,5% |
| EUR_Fixed_10Y | EUR | 10 | 2,44%  | 1,5%  | 3,0%  |
| JPY_Fixed_5Y  | JPY | 5  | 6,67%  | 5,0%  | 8,5%  |
| JPY_Fixed_10Y | JPY | 10 | 4,41%  | 3,0%  | 5,5%  |

Presisi penuh ada di sheet `Data Awal` (dan `legacy/data_v0/portfolio_data.csv`).

## Catatan
- 3.104 baris hari kerja, 1 Jan 2014 – 24 Nov 2025. Data lengkap untuk `IR_JPY_5Y` baru mulai **2017-07-03** → awal jendela analisis (2.191 baris).
- `IR_EUR_10Y` hilang 163 hari kerja berurutan (1 Feb – 15 Sep 2021). Irisan lengkap = 2.028 baris. Pemilihan 2.028 vs isi spline 2.191 adalah keputusan D1 (`docs/context/spesifikasi_model.md` §12).
- Data olahan dibuat oleh `scripts/02_preprocess_data.py` (Tahap 2) ke `data/processed/`. Data olahan versi lama ada di `legacy/data_v0/`.
