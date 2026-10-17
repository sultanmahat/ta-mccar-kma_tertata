"""
Modul Simulasi Geometric Brownian Motion (GBM) untuk Proyeksi Skenario Pasar:
Sesuai Persamaan 2.8 & 2.9 (Bab 2 dan Bab 3 Proposal TA Sultan Bakri)

Model Stokastik:
S_{t + Delta t} = S_t * exp( (mu - 0.5 * sigma^2) * Delta t + sigma * sqrt(Delta t) * Z )
dengan Z ~ N(0, 1).
"""

import numpy as np

def estimate_gbm_parameters(series, dt=1.0/252.0):
    """
    Mengestimasi drift (mu) dan volatilitas (sigma) tahunan dari deret waktu historis.
    series: array 1D nilai historis (harga / kurs / indeks biaya).
    dt: fraksi waktu tahunan (default 1/252 untuk data harian).
    """
    # Log-returns: r_t = ln(S_t / S_{t-1})
    log_returns = np.diff(np.log(series))
    mean_ret = np.mean(log_returns)
    var_ret = np.var(log_returns, ddof=1)

    # Konversi ke parameter kontinu tahunan
    sigma = np.sqrt(var_ret / dt)
    mu = (mean_ret / dt) + 0.5 * (sigma ** 2)

    return mu, sigma

def simulate_gbm_paths(S0, mu, sigma, n_paths=5000, n_steps=252, dt=1.0/252.0, seed=42):
    """
    Membangkitkan n_paths skenario proyeksi Geometric Brownian Motion.
    S0: nilai awal pada t=0 (data historis terakhir).
    n_paths: jumlah skenario simulasi (default 5.000 sesuai Bab 3 Proposal).
    n_steps: jumlah langkah proyeksi (default 252 hari bursa ~ 1 tahun).
    dt: langkah waktu.
    """
    if seed is not None:
        np.random.seed(seed)

    # Matriks bilangan acak normal baku Z ~ N(0, 1)
    Z = np.random.standard_normal((n_paths, n_steps))

    # Lintasan simulasi
    drift_term = (mu - 0.5 * (sigma ** 2)) * dt
    diffusion_term = sigma * np.sqrt(dt) * Z

    # Akumulasi log returns
    cumulative_returns = np.cumsum(drift_term + diffusion_term, axis=1)

    # Nilai aset pada tiap langkah: S_t = S_0 * exp(cumsum)
    paths = np.zeros((n_paths, n_steps + 1))
    paths[:, 0] = S0
    paths[:, 1:] = S0 * np.exp(cumulative_returns)

    # Mengembalikan nilai terminal (akhir horizon) dan seluruh lintasan
    terminal_values = paths[:, -1]
    return terminal_values, paths

def generate_market_scenarios(cost_matrix, n_paths=5000, n_steps=252, dt=1.0/252.0, seed=42):
    """
    Menghasilkan skenario terminal masa depan untuk seluruh 7 instrumen
    menggunakan parameter estimasi historis dari cost_matrix (disesuaikan ke USD).
    
    Output:
    scenario_costs: matriks berukuran (n_paths, n_instruments) yang berisi biaya terminal
                    relatif atau rasio biaya untuk setiap instrumen pada 5.000 skenario.
    """
    n_instruments = cost_matrix.shape[1]
    scenario_costs = np.zeros((n_paths, n_instruments))

    for i in range(n_instruments):
        series = cost_matrix[:, i]
        S0 = series[-1]
        mu, sigma = estimate_gbm_parameters(series, dt=dt)
        term_vals, _ = simulate_gbm_paths(S0, mu, sigma, n_paths=n_paths, n_steps=n_steps, dt=dt, seed=seed + i)
        
        # Rasio perubahan biaya relatif: C_terminal / C_0
        scenario_costs[:, i] = term_vals / S0

    return scenario_costs
