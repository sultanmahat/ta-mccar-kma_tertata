"""Estimasi parameter GBM dan statistik biaya historis.

Menyediakan fungsi untuk:
1. Menghitung parameter Geometric Brownian Motion (GBM) per variabel pasar (Pers. 2.11–2.12):
   - Rata-rata dan standar deviasi harian
   - Anualisasi (252 hari kerja): sigma = s * sqrt(252), mu = 252*m + sigma^2 / 2
2. Menghitung matriks korelasi Pearson 9x9 dan memverifikasi definit positif (Cholesky).
3. Menghitung biaya historis dan statistik perubahan biaya Delta c_{i,t} (Pers. 2.7–2.10).
"""

from typing import Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

from mccar_kma.data.cleaning import ALL_MARKET_COLS, compute_log_returns

# Definisi instrumen utang (Tabel 2.1 spesifikasi)
INSTRUMENTS: List[Dict[str, Union[str, int]]] = [
    {"name": "USD_Fixed_5Y", "currency": "USD", "tenor": 5, "yield_col": "IR_USD_5Y"},
    {"name": "USD_Fixed_10Y", "currency": "USD", "tenor": 10, "yield_col": "IR_USD_10Y"},
    {"name": "USD_Fixed_30Y", "currency": "USD", "tenor": 30, "yield_col": "IR_USD_30Y"},
    {"name": "EUR_Fixed_7Y", "currency": "EUR", "tenor": 8, "yield_col": "IR_EUR_7Y"},
    {"name": "EUR_Fixed_10Y", "currency": "EUR", "tenor": 10, "yield_col": "IR_EUR_10Y"},
    {"name": "JPY_Fixed_5Y", "currency": "JPY", "tenor": 5, "yield_col": "IR_JPY_5Y"},
    {"name": "JPY_Fixed_10Y", "currency": "JPY", "tenor": 10, "yield_col": "IR_JPY_10Y"},
]

INSTRUMENT_NAMES = [inst["name"] for inst in INSTRUMENTS]


def estimate_gbm_params(
    log_returns: pd.DataFrame,
    cols: Optional[List[str]] = None,
    days_per_year: int = 252,
) -> pd.DataFrame:
    """Mengestimasi parameter drift (mu) dan volatilitas (sigma) GBM.

    Sesuai keputusan D2a (Opsi A) dan spesifikasi model §4:
        sigma_annual = sigma_daily * sqrt(days_per_year)
        mu_annual = days_per_year * mu_daily + 0.5 * (sigma_annual ** 2)

    Parameters
    ----------
    log_returns : pd.DataFrame
        DataFrame log-return harian r_t = ln(S_t / S_{t-1}).
    cols : Optional[List[str]]
        Daftar nama kolom yang diestimasi. Default: 9 kolom variabel pasar.
    days_per_year : int
        Faktor konversi hari kerja per tahun (default: 252).

    Returns
    -------
    pd.DataFrame
        DataFrame dengan kolom:
        ['variable', 'mu_daily', 'sigma_daily', 'mu_annual', 'sigma_annual', 'n_obs']
    """
    if cols is None:
        cols = [c for c in ALL_MARKET_COLS if c in log_returns.columns]

    records = []
    for col in cols:
        series = log_returns[col].to_numpy(dtype=float)
        series = series[~np.isnan(series)]
        n_obs = len(series)
        if n_obs < 2:
            raise ValueError(f"Observasi tidak cukup untuk variabel {col}: {n_obs}")

        m_daily = float(np.mean(series))
        s_daily = float(np.std(series, ddof=1))

        sigma_ann = float(s_daily * np.sqrt(days_per_year))
        # Kalibrasi drift Opsi A: mu = 252*m + sigma^2 / 2
        mu_ann = float(days_per_year * m_daily + 0.5 * (sigma_ann ** 2))

        records.append(
            {
                "variable": col,
                "mu_daily": m_daily,
                "sigma_daily": s_daily,
                "mu_annual": mu_ann,
                "sigma_annual": sigma_ann,
                "n_obs": n_obs,
            }
        )

    return pd.DataFrame(records)


def compute_correlation_matrix(
    log_returns: pd.DataFrame,
    cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Menghitung matriks korelasi Pearson dan memverifikasi sifat matematisnya.

    Sifat yang diverifikasi:
    1. Simetris dalam toleransi numerik (atol=1e-12).
    2. Diagonal bernilai persis 1.0.
    3. Positif definit (faktorisasi Cholesky berhasil tanpa galat numerik).

    Parameters
    ----------
    log_returns : pd.DataFrame
        DataFrame log-return harian.
    cols : Optional[List[str]]
        Daftar variabel yang dihitung korelasinya. Default: 9 variabel pasar.

    Returns
    -------
    pd.DataFrame
        Matriks korelasi berukuran N x N.

    Raises
    ------
    ValueError
        Jika matriks korelasi tidak simetris, diagonal != 1, atau gagal Cholesky.
    """
    if cols is None:
        cols = [c for c in ALL_MARKET_COLS if c in log_returns.columns]

    df_subset = log_returns[cols].copy()
    corr_df = df_subset.corr(method="pearson")
    corr_mat = corr_df.to_numpy(dtype=float)

    # 1. Verifikasi simetris
    if not np.allclose(corr_mat, corr_mat.T, atol=1e-12):
        raise ValueError("Matriks korelasi tidak simetris.")

    # 2. Verifikasi diagonal bernilai 1.0
    if not np.allclose(np.diag(corr_mat), 1.0, atol=1e-12):
        raise ValueError("Diagonal matriks korelasi tidak bernilai 1.0.")

    # 3. Verifikasi definit positif melalui faktorisasi Cholesky
    try:
        np.linalg.cholesky(corr_mat)
    except np.linalg.LinAlgError as err:
        raise ValueError(
            "Matriks korelasi bukan matriks definit positif "
            "(faktorisasi Cholesky gagal)."
        ) from err

    return corr_df


def compute_historical_costs(
    df_market: pd.DataFrame,
    x0_eur: Optional[float] = None,
    x0_jpy: Optional[float] = None,
    cost_def: str = "gross",
) -> pd.DataFrame:
    """Menghitung biaya instrumen utang historis C_{i,t} (Persamaan 2.1–2.3).

    Persamaan:
        q_{USD,t} = 1
        q_{EUR,t} = X_{USD/EUR,0} / X_{USD/EUR,t}
        q_{JPY,t} = X_{USD/JPY,0} / X_{USD/JPY,t}
        Biaya bruto (Pers. 2.2):    C_{i,t} = q_{c(i),t} * (1 + y_{i,t} / 100)
        Biaya bunga (Pers. 2.3):    C^I_{i,t} = q_{c(i),t} * (y_{i,t} / 100)

    Parameters
    ----------
    df_market : pd.DataFrame
        DataFrame deret pasar historis (harus memiliki 7 kolom IR dan 2 kolom FX).
    x0_eur : Optional[float]
        Kurs acuan USD/EUR awal. Jika None, gunakan observasi terakhir di df_market.
    x0_jpy : Optional[float]
        Kurs acuan USD/JPY awal. Jika None, gunakan observasi terakhir di df_market.
    cost_def : str
        'gross' (Persamaan 2.2) atau 'interest' (Persamaan 2.3).

    Returns
    -------
    pd.DataFrame
        DataFrame biaya dengan kolom Tanggal (jika ada) dan 7 instrumen utang.
    """
    if cost_def not in ("gross", "interest"):
        raise ValueError(
            f"cost_def tidak valid: '{cost_def}'. Pilih 'gross' atau 'interest'."
        )

    if x0_eur is None:
        x0_eur = float(df_market["FX_USD/EUR"].iloc[-1])
    if x0_jpy is None:
        x0_jpy = float(df_market["FX_USD/JPY"].iloc[-1])

    n_rows = len(df_market)
    fx_eur = df_market["FX_USD/EUR"].to_numpy(dtype=float)
    fx_jpy = df_market["FX_USD/JPY"].to_numpy(dtype=float)

    # Hitung q_{c,t}
    q_usd = np.ones(n_rows, dtype=float)
    q_eur = x0_eur / fx_eur
    q_jpy = x0_jpy / fx_jpy

    costs_data = {}
    if "Tanggal" in df_market.columns:
        costs_data["Tanggal"] = df_market["Tanggal"].values

    for inst in INSTRUMENTS:
        name = inst["name"]
        curr = inst["currency"]
        y_col = inst["yield_col"]
        y_vals = df_market[y_col].to_numpy(dtype=float)

        if curr == "USD":
            q = q_usd
        elif curr == "EUR":
            q = q_eur
        elif curr == "JPY":
            q = q_jpy
        else:
            raise ValueError(f"Mata uang tidak dikenal: {curr}")

        if cost_def == "gross":
            # Persamaan 2.2: q * (1 + y/100)
            c = q * (1.0 + y_vals / 100.0)
        else:
            # Persamaan 2.3: q * (y/100)
            c = q * (y_vals / 100.0)

        costs_data[name] = c

    return pd.DataFrame(costs_data)


def compute_historical_cost_stats(
    df_market: pd.DataFrame,
    x0_eur: Optional[float] = None,
    x0_jpy: Optional[float] = None,
    cost_def: str = "gross",
    exclude_gap: bool = True,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Menghitung statistik perubahan biaya historis Persamaan 2.7–2.10.

    Persamaan:
        Delta c_{i,t} = ln(C_{i,t} / C_{i,t-1})                   (Pers. 2.7)
        Rata-rata: m_c,i = (1/T) sum Delta c_{i,t}               (Pers. 2.8)
        Varians: s_c,i^2 = (1/(T-1)) sum (Delta c_{i,t} - m)^2    (Pers. 2.9)
        Kovarians: Sigma_{ij} = (1/(T-1)) sum (Delta c_i - m_i)(Delta c_j - m_j) (Pers. 2.10)

    Parameters
    ----------
    df_market : pd.DataFrame
        DataFrame deret pasar historis bersih (misal 2.028 baris intersection).
    x0_eur : Optional[float]
        Kurs acuan awal X_{USD/EUR, 0}.
    x0_jpy : Optional[float]
        Kurs acuan awal X_{USD/JPY, 0}.
    cost_def : str
        'gross' atau 'interest'.
    exclude_gap : bool
        Jika True, buang perubahan biaya yang melintasi celah > 4 hari kerja.

    Returns
    -------
    Tuple[pd.DataFrame, pd.DataFrame]
        (df_stats, df_cov):
        df_stats berisi [instrument, currency, tenor, mean_delta_c, var_delta_c, std_delta_c, n_obs]
        df_cov berisi matriks kovarians 7x7 dari Delta c_{i,t}.
    """
    df_costs = compute_historical_costs(
        df_market=df_market,
        x0_eur=x0_eur,
        x0_jpy=x0_jpy,
        cost_def=cost_def,
    )

    names = INSTRUMENT_NAMES
    c_vals = df_costs[names].to_numpy(dtype=float)

    # Hitung Delta c_{i,t} = ln(C_{i,t} / C_{i,t-1})
    delta_c = np.log(c_vals[1:] / c_vals[:-1])

    if exclude_gap and "Tanggal" in df_costs.columns:
        dates_curr = pd.to_datetime(df_costs["Tanggal"].iloc[1:]).reset_index(drop=True)
        dates_prev = pd.to_datetime(df_costs["Tanggal"].iloc[:-1]).reset_index(drop=True)
        step_days = (dates_curr - dates_prev).dt.days
        valid_mask = (step_days <= 4).to_numpy()
        delta_c = delta_c[valid_mask]

    n_obs = len(delta_c)
    if n_obs < 2:
        raise ValueError(f"Observasi Delta c tidak cukup: {n_obs}")

    means = np.mean(delta_c, axis=0)
    vars_c = np.var(delta_c, axis=0, ddof=1)
    stds_c = np.sqrt(vars_c)
    cov_c = np.cov(delta_c, rowvar=False, ddof=1)

    records = []
    for idx, inst in enumerate(INSTRUMENTS):
        records.append(
            {
                "instrument": inst["name"],
                "currency": inst["currency"],
                "tenor": inst["tenor"],
                "mean_delta_c": float(means[idx]),
                "var_delta_c": float(vars_c[idx]),
                "std_delta_c": float(stds_c[idx]),
                "n_obs": n_obs,
            }
        )

    df_stats = pd.DataFrame(records)
    df_cov = pd.DataFrame(cov_c, index=names, columns=names)

    return df_stats, df_cov
