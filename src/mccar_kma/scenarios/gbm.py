"""Pembangkit skenario Geometric Brownian Motion (GBM) berkorelasi.

Menyediakan fungsi untuk:
1. Membangkitkan guncangan normal multivariat berkorelasi Z = eps @ L.T via faktorisasi Cholesky.
2. Mensimulasikan skenario harga/yield/kurs masa depan:
   - Mode terminal 1-step (D2b Opsi A): S_T = S_0 * exp((mu - 0.5*sigma^2) + sigma*Z)
   - Mode jalur 252 langkah: simulasi bertahap delta_t = 1/252
3. Verifikasi empiris terhadap parameter target (mean, std, korelasi).
"""

from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

from mccar_kma.data.cleaning import ALL_MARKET_COLS


def generate_correlated_shocks(
    n_scenarios: int,
    corr_matrix: Union[np.ndarray, pd.DataFrame],
    seed: Optional[int] = None,
) -> np.ndarray:
    """Membangkitkan guncangan acak normal standar berkorelasi Z ~ N(0, C).

    Menggunakan faktorisasi Cholesky C = L @ L.T:
        Z = eps @ L.T,  dengan eps ~ N(0, I)

    Parameters
    ----------
    n_scenarios : int
        Jumlah skenario yang dibangkitkan (N).
    corr_matrix : Union[np.ndarray, pd.DataFrame]
        Matriks korelasi target C (K x K).
    seed : Optional[int]
        Seed generator bilangan acak untuk reproduksibilitas.

    Returns
    -------
    np.ndarray
        Array berukuran (n_scenarios, K) dengan korelasi mendekati C.
    """
    if isinstance(corr_matrix, pd.DataFrame):
        corr_mat = corr_matrix.to_numpy(dtype=float)
    else:
        corr_mat = np.asarray(corr_matrix, dtype=float)

    k = corr_mat.shape[0]
    if corr_mat.shape != (k, k):
        raise ValueError(f"Matriks korelasi harus bujur sangkar, didapat: {corr_mat.shape}")

    # Faktorisasi Cholesky C = L @ L.T (L segitiga bawah)
    try:
        L = np.linalg.cholesky(corr_mat)
    except np.linalg.LinAlgError as err:
        raise ValueError(
            "Matriks korelasi bukan definit positif; faktorisasi Cholesky gagal."
        ) from err

    rng = np.random.default_rng(seed)
    eps = rng.standard_normal((n_scenarios, k))

    # Z = eps @ L.T  --> Cov(Z) = L @ Cov(eps) @ L.T = L @ I @ L.T = C
    Z = eps @ L.T
    return Z


def simulate_gbm_terminal(
    s0: np.ndarray,
    mu_annual: np.ndarray,
    sigma_annual: np.ndarray,
    corr_matrix: Union[np.ndarray, pd.DataFrame],
    n_scenarios: int = 5000,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulasi langsung nilai terminal T=1 tahun (1-step terminal).

    Persamaan:
        drift_comp = mu_annual - 0.5 * (sigma_annual ** 2)
        log_returns = drift_comp * T + sigma_annual * sqrt(T) * Z,   T = 1.0
        S_T = S_0 * exp(log_returns)

    Parameters
    ----------
    s0 : np.ndarray
        Nilai awal variabel pasar saat t=0 (K,).
    mu_annual : np.ndarray
        Drift tahunan terkalibrasi mu_i (K,).
    sigma_annual : np.ndarray
        Volatilitas tahunan terkalibrasi sigma_i (K,).
    corr_matrix : Union[np.ndarray, pd.DataFrame]
        Matriks korelasi Pearson 9x9 (K x K).
    n_scenarios : int
        Jumlah skenario terminal (default: 5.000).
    seed : Optional[int]
        Seed acak.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        (scenarios_sT, scenarios_log_returns):
        Masing-masing berukuran (n_scenarios, K).
    """
    s0 = np.asarray(s0, dtype=float)
    mu = np.asarray(mu_annual, dtype=float)
    sig = np.asarray(sigma_annual, dtype=float)

    if not (len(s0) == len(mu) == len(sig)):
        raise ValueError("Panjang s0, mu_annual, dan sigma_annual harus sama.")

    if np.any(s0 <= 0):
        raise ValueError("Semua elemen S_0 harus bernilai positif (> 0).")

    Z = generate_correlated_shocks(n_scenarios=n_scenarios, corr_matrix=corr_matrix, seed=seed)

    # drift_term = (mu - 0.5*sigma^2) * 1.0
    drift_term = mu - 0.5 * (sig ** 2)
    # log_returns = drift_term + sigma * Z
    log_returns = drift_term + sig * Z

    # S_T = S_0 * exp(log_returns)
    s_terminal = s0 * np.exp(log_returns)

    return s_terminal, log_returns


def simulate_gbm_path(
    s0: np.ndarray,
    mu_annual: np.ndarray,
    sigma_annual: np.ndarray,
    corr_matrix: Union[np.ndarray, pd.DataFrame],
    n_scenarios: int = 5000,
    n_steps: int = 252,
    dt: Optional[float] = None,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """Simulasi lintasan bertahap 252 langkah per skenario.

    Parameters
    ----------
    s0 : np.ndarray
        Nilai awal variabel pasar saat t=0 (K,).
    mu_annual : np.ndarray
        Drift tahunan (K,).
    sigma_annual : np.ndarray
        Volatilitas tahunan (K,).
    corr_matrix : Union[np.ndarray, pd.DataFrame]
        Matriks korelasi Pearson (K x K).
    n_scenarios : int
        Jumlah skenario lintasan.
    n_steps : int
        Jumlah langkah diskritisasi (default: 252).
    dt : Optional[float]
        Ukuran langkah waktu. Default: 1.0 / n_steps.
    seed : Optional[int]
        Seed acak.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        (paths, terminal_log_returns):
        paths berukuran (n_scenarios, n_steps + 1, K),
        terminal_log_returns berukuran (n_scenarios, K).
    """
    s0 = np.asarray(s0, dtype=float)
    mu = np.asarray(mu_annual, dtype=float)
    sig = np.asarray(sigma_annual, dtype=float)
    k = len(s0)

    if dt is None:
        dt = 1.0 / n_steps

    if isinstance(corr_matrix, pd.DataFrame):
        corr_mat = corr_matrix.to_numpy(dtype=float)
    else:
        corr_mat = np.asarray(corr_matrix, dtype=float)

    L = np.linalg.cholesky(corr_mat)
    rng = np.random.default_rng(seed)

    paths = np.zeros((n_scenarios, n_steps + 1, k), dtype=float)
    paths[:, 0, :] = s0

    drift_step = (mu - 0.5 * (sig ** 2)) * dt
    diff_coef = sig * np.sqrt(dt)

    current_s = np.copy(s0)
    # Replikasi untuk seluruh n_scenarios
    current_mat = np.tile(s0, (n_scenarios, 1))

    for step in range(1, n_steps + 1):
        eps_t = rng.standard_normal((n_scenarios, k))
        z_t = eps_t @ L.T
        step_lr = drift_step + diff_coef * z_t
        current_mat = current_mat * np.exp(step_lr)
        paths[:, step, :] = current_mat

    terminal_lr = np.log(paths[:, -1, :] / s0)
    return paths, terminal_lr


def generate_market_scenarios(
    df_params: pd.DataFrame,
    corr_matrix: Union[pd.DataFrame, np.ndarray],
    s0: Union[pd.Series, Dict[str, float], np.ndarray],
    n_scenarios: int = 5000,
    seed: Optional[int] = None,
    mode: str = "terminal_1step",
    var_order: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Fungsi pembungkus tingkat tinggi untuk pembangkitan skenario pasar finansial.

    Menyelaraskan urutan variabel, mengekstraksi mu, sigma, S0, menjalankan
    simulasi, dan menghitung statistik verifikasi kualitas.

    Parameters
    ----------
    df_params : pd.DataFrame
        DataFrame parameter GBM hasil Tahap 03.
    corr_matrix : Union[pd.DataFrame, np.ndarray]
        Matriks korelasi 9x9.
    s0 : Union[pd.Series, Dict[str, float], np.ndarray]
        Nilai observasi awal (t=0).
    n_scenarios : int
        Jumlah skenario (N).
    seed : Optional[int]
        Seed generator acak.
    mode : str
        'terminal_1step' atau 'path_252'.
    var_order : Optional[List[str]]
        Urutan variabel. Default: ALL_MARKET_COLS.

    Returns
    -------
    Dict[str, Any]
        Dictionary berisi:
        - 'scenarios_market': np.ndarray (N, 9)
        - 'scenarios_log_returns': np.ndarray (N, 9)
        - 's0': np.ndarray (9,)
        - 'variable_names': List[str]
        - 'seed': Optional[int]
        - 'mode': str
        - 'n_scenarios': int
        - 'empirical_metrics': Dict ringkasan rata-rata dan deviasi
    """
    if var_order is None:
        var_order = ALL_MARKET_COLS

    # Susun parameter sesuai var_order
    param_indexed = df_params.set_index("variable")
    mu_arr = np.array([param_indexed.loc[v, "mu_annual"] for v in var_order], dtype=float)
    sig_arr = np.array([param_indexed.loc[v, "sigma_annual"] for v in var_order], dtype=float)

    if isinstance(s0, pd.Series):
        s0_arr = np.array([float(s0[v]) for v in var_order], dtype=float)
    elif isinstance(s0, dict):
        s0_arr = np.array([float(s0[v]) for v in var_order], dtype=float)
    else:
        s0_arr = np.asarray(s0, dtype=float)

    if isinstance(corr_matrix, pd.DataFrame):
        corr_aligned = corr_matrix.loc[var_order, var_order].to_numpy(dtype=float)
    else:
        corr_aligned = np.asarray(corr_matrix, dtype=float)

    if mode == "terminal_1step":
        scen_market, scen_lr = simulate_gbm_terminal(
            s0=s0_arr,
            mu_annual=mu_arr,
            sigma_annual=sig_arr,
            corr_matrix=corr_aligned,
            n_scenarios=n_scenarios,
            seed=seed,
        )
    elif mode == "path_252":
        paths, scen_lr = simulate_gbm_path(
            s0=s0_arr,
            mu_annual=mu_arr,
            sigma_annual=sig_arr,
            corr_matrix=corr_aligned,
            n_scenarios=n_scenarios,
            n_steps=252,
            seed=seed,
        )
        scen_market = paths[:, -1, :]
    else:
        raise ValueError(f"Mode simulasi tidak dikenal: '{mode}'. Pilih 'terminal_1step' atau 'path_252'.")

    # Metrik empiris
    mean_lr_emp = np.mean(scen_lr, axis=0)
    std_lr_emp = np.std(scen_lr, axis=0, ddof=1)
    corr_emp = np.corrcoef(scen_lr, rowvar=False)

    target_drift = mu_arr - 0.5 * (sig_arr ** 2)
    max_corr_diff = float(np.max(np.abs(corr_emp - corr_aligned)))

    metrics = {
        "mean_log_returns_simulated": {v: float(m) for v, m in zip(var_order, mean_lr_emp)},
        "target_drift_term": {v: float(t) for v, t in zip(var_order, target_drift)},
        "std_log_returns_simulated": {v: float(s) for v, s in zip(var_order, std_lr_emp)},
        "target_sigma_annual": {v: float(s) for v, s in zip(var_order, sig_arr)},
        "max_correlation_difference": max_corr_diff,
        "all_positive": bool(np.all(scen_market > 0)),
        "nan_count": int(np.isnan(scen_market).sum()),
    }

    return {
        "scenarios_market": scen_market,
        "scenarios_log_returns": scen_lr,
        "s0": s0_arr,
        "variable_names": var_order,
        "seed": seed,
        "mode": mode,
        "n_scenarios": n_scenarios,
        "empirical_metrics": metrics,
    }
