"""
Modul pemuatan dan penyiapan data untuk Tugas Akhir:
"Optimasi Portofolio Utang Negara Multivaluta dengan MCCaR dan KMA"
Peneliti: Sultan Bakri Baihaqi Mahat (NRP 5002221016)
"""

import os
import pandas as pd
import numpy as np

# Path direktori
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "DATASET", "processed")

def load_processed_data():
    """
    Memuat data bersih dari DATASET/processed/:
    - fx_data_clean.csv: kurs FX_USD/EUR dan FX_USD/JPY harian.
    - ir_data_clean.csv: yield suku bunga 7 instrumen harian.
    - portfolio_data.csv: bobot eksisting (2024), batas bawah (Min), dan batas atas (Max).
    """
    fx_path = os.path.join(DATA_DIR, "fx_data_clean.csv")
    ir_path = os.path.join(DATA_DIR, "ir_data_clean.csv")
    port_path = os.path.join(DATA_DIR, "portfolio_data.csv")

    df_fx = pd.read_csv(fx_path, parse_dates=['Tanggal'])
    df_ir = pd.read_csv(ir_path, parse_dates=['Tanggal'])
    df_port = pd.read_csv(port_path)

    # Gabungkan berdasarkan tanggal (inner join)
    df_merged = pd.merge(df_ir, df_fx, on='Tanggal', how='inner').sort_values('Tanggal').reset_index(drop=True)

    instruments = df_port['Instrument'].tolist()
    currencies = df_port['Curr'].tolist()
    existing_weights = df_port['Existing (2024)'].to_numpy(dtype=float)
    lower_bounds = df_port['Min'].to_numpy(dtype=float)
    upper_bounds = df_port['Max'].to_numpy(dtype=float)

    return {
        'df_merged': df_merged,
        'df_port': df_port,
        'instruments': instruments,
        'currencies': currencies,
        'existing_weights': existing_weights,
        'lower_bounds': lower_bounds,
        'upper_bounds': upper_bounds
    }

def calculate_adjusted_costs(df_merged, instruments):
    """
    Menghitung Future Value / Biaya Penyesuaian ke USD (Persamaan 3.1 & 3.2):
    FV_i = FX_i * (1 + IR_i / 100)
    Catatan:
    - USD: FX = 1.0
    - EUR: Kurs harian di fx_data_clean adalah FX_USD/EUR (misal ~0.88, artinya 1 USD = 0.88 EUR -> 1 EUR = 1 / 0.88 USD)
    - JPY: Kurs harian di fx_data_clean adalah FX_USD/JPY (misal ~113.4, artinya 1 USD = 113.4 JPY -> 1 JPY = 1 / 113.4 USD)
    """
    n_samples = len(df_merged)
    cost_matrix = np.zeros((n_samples, len(instruments)))

    for i, inst in enumerate(instruments):
        ir_col = f"IR_{inst.replace('_Fixed', '')}" if f"IR_{inst.replace('_Fixed', '')}" in df_merged.columns else None
        if ir_col is None:
            # Fallback format kolom alternatif
            matching_cols = [c for c in df_merged.columns if inst.split('_')[0] in c and inst.split('_')[-1] in c]
            ir_col = matching_cols[0] if matching_cols else df_merged.columns[i+1]

        ir_values = df_merged[ir_col].to_numpy(dtype=float) / 100.0  # konversi persen ke desimal

        if "USD" in inst:
            fx_usd = 1.0
            cost_matrix[:, i] = fx_usd * (1.0 + ir_values)
        elif "EUR" in inst:
            # Konversi EUR ke USD: 1 / (USD/EUR)
            fx_usd_per_eur = 1.0 / df_merged['FX_USD/EUR'].to_numpy(dtype=float)
            cost_matrix[:, i] = fx_usd_per_eur * (1.0 + ir_values)
        elif "JPY" in inst:
            # Konversi JPY ke USD: 1 / (USD/JPY)
            fx_usd_per_jpy = 1.0 / df_merged['FX_USD/JPY'].to_numpy(dtype=float)
            cost_matrix[:, i] = fx_usd_per_jpy * (1.0 + ir_values)

    # Hitung log-return / perubahan biaya logaritmik: Delta c_{i, t} = ln(C_{i, t} / C_{i, t-1})
    log_returns = np.diff(np.log(cost_matrix), axis=0)

    # Rata-rata perubahan biaya mu dan matriks kovarians Sigma
    mu_vector = np.mean(log_returns, axis=0)
    cov_matrix = np.cov(log_returns, rowvar=False)

    return {
        'cost_matrix': cost_matrix,
        'log_returns': log_returns,
        'mu_vector': mu_vector,
        'cov_matrix': cov_matrix
    }
