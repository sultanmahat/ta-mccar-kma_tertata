"""Unit test untuk modul pembangkit skenario GBM dan biaya portofolio.

Menguji modul mccar_kma.scenarios.gbm dan cost:
1. Pembangkitan guncangan normal multivariat berkorelasi Z via Cholesky.
2. Sifat distribusi terminal GBM (mean, std log-return vs parameter target).
3. Reproduksibilitas seed (seed sama -> identik, seed beda -> beda).
4. Kepositifan nilai (yield, kurs, biaya > 0).
5. Arah faktor konversi kurs q (kurs naik -> q turun -> biaya turun).
6. Konsistensi aljabar biaya bruto vs bunga: C_gross - C_interest = q (USD = 1.0 persis).
7. Integrasi pembentukan bank skenario pada parameter riil Tahap 03.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from mccar_kma.data.cleaning import ALL_MARKET_COLS
from mccar_kma.scenarios.gbm import (
    generate_correlated_shocks,
    simulate_gbm_terminal,
    simulate_gbm_path,
    generate_market_scenarios,
)
from mccar_kma.scenarios.cost import (
    compute_q_factors,
    compute_scenario_costs,
    build_scenario_bank,
)
from mccar_kma.scenarios.estimation import INSTRUMENTS, INSTRUMENT_NAMES


@pytest.fixture
def sample_gbm_inputs():
    """Fixture memuat parameter GBM, korelasi, dan S0 riil jika ada."""
    base_dir = Path(".")
    params_file = base_dir / "data" / "processed" / "gbm_params_intersection.csv"
    corr_file = base_dir / "data" / "processed" / "corr_intersection.csv"
    data_file = (
        base_dir
        / "data"
        / "processed"
        / "market_2017-07-03_2025-11-24_intersection.csv"
    )

    if params_file.exists() and corr_file.exists() and data_file.exists():
        df_params = pd.read_csv(params_file)
        df_corr = pd.read_csv(corr_file, index_col=0)
        df_market = pd.read_csv(data_file)
        s0_series = df_market.iloc[-1][ALL_MARKET_COLS]
        return df_params, df_corr, s0_series

    # Fallback tiruan
    df_params = pd.DataFrame({
        "variable": ALL_MARKET_COLS,
        "mu_annual": [0.05] * 7 + [0.01, 0.02],
        "sigma_annual": [0.20] * 7 + [0.08, 0.09],
    })
    df_corr = pd.DataFrame(np.eye(9), index=ALL_MARKET_COLS, columns=ALL_MARKET_COLS)
    s0_series = pd.Series([4.0] * 7 + [0.85, 150.0], index=ALL_MARKET_COLS)
    return df_params, df_corr, s0_series


def test_correlated_shocks_properties():
    """Uji sifat statistik guncangan Z: mean mendekati 0 dan korelasi mendekati target."""
    target_rho = 0.70
    corr_target = np.array([[1.0, target_rho], [target_rho, 1.0]])
    n = 20000

    Z = generate_correlated_shocks(n_scenarios=n, corr_matrix=corr_target, seed=123)

    assert Z.shape == (n, 2)
    # Mean mendekati 0
    assert abs(np.mean(Z[:, 0])) < 0.03
    assert abs(np.mean(Z[:, 1])) < 0.03
    # Std dev mendekati 1.0
    assert abs(np.std(Z[:, 0]) - 1.0) < 0.03
    assert abs(np.std(Z[:, 1]) - 1.0) < 0.03

    # Korelasi sampel
    emp_corr = np.corrcoef(Z, rowvar=False)
    assert abs(emp_corr[0, 1] - target_rho) < 0.02


def test_simulate_gbm_terminal_synthetic():
    """Uji distribusi terminal GBM 1-step vs parameter teoritis mu dan sigma."""
    s0 = np.array([100.0, 5.0])
    mu = np.array([0.08, 0.04])
    sig = np.array([0.20, 0.30])
    corr = np.array([[1.0, 0.5], [0.5, 1.0]])
    n = 20000

    s_term, log_ret = simulate_gbm_terminal(
        s0=s0, mu_annual=mu, sigma_annual=sig, corr_matrix=corr, n_scenarios=n, seed=42
    )

    assert s_term.shape == (n, 2)
    assert log_ret.shape == (n, 2)
    # Semua harga terminal > 0
    assert np.all(s_term > 0)

    # Verifikasi log-return teoritis: E[ln(S_T/S_0)] = mu - 0.5*sigma^2
    target_mean = mu - 0.5 * (sig ** 2)
    emp_mean = np.mean(log_ret, axis=0)
    se_mean = sig / np.sqrt(n)

    for j in range(2):
        assert abs(emp_mean[j] - target_mean[j]) < 3 * se_mean[j]

    # Verifikasi standar deviasi teoritis: Std[ln(S_T/S_0)] = sigma
    emp_std = np.std(log_ret, axis=0, ddof=1)
    se_std = sig / np.sqrt(2 * n)
    for j in range(2):
        assert abs(emp_std[j] - sig[j]) < 3 * se_std[j]


def test_simulate_gbm_path():
    """Uji simulasi lintasan 252 langkah menghasilkan nilai terminal positif dan konsisten."""
    s0 = np.array([100.0])
    mu = np.array([0.05])
    sig = np.array([0.15])
    corr = np.array([[1.0]])
    n = 1000

    paths, log_ret = simulate_gbm_path(
        s0=s0, mu_annual=mu, sigma_annual=sig, corr_matrix=corr, n_scenarios=n, n_steps=252, seed=99
    )

    assert paths.shape == (n, 253, 1)
    assert np.all(paths > 0)
    assert np.allclose(paths[:, 0, 0], 100.0)


def test_seed_reproducibility():
    """Uji reproduksibilitas: seed sama persis bit-by-bit; seed beda menghasilkan variasi."""
    s0 = np.array([4.0, 150.0])
    mu = np.array([0.05, 0.02])
    sig = np.array([0.20, 0.10])
    corr = np.eye(2)

    s_a1, lr_a1 = simulate_gbm_terminal(s0, mu, sig, corr, n_scenarios=500, seed=42)
    s_a2, lr_a2 = simulate_gbm_terminal(s0, mu, sig, corr, n_scenarios=500, seed=42)
    s_b, lr_b = simulate_gbm_terminal(s0, mu, sig, corr, n_scenarios=500, seed=2026)

    # Identik bit-by-bit
    assert np.array_equal(s_a1, s_a2)
    assert np.array_equal(lr_a1, lr_a2)

    # Berbeda dengan seed lain
    assert not np.array_equal(s_a1, s_b)


def test_q_factor_behavior():
    """Uji faktor konversi q: USD=1, dan arah pergerakan kurs asing."""
    market_cols = ALL_MARKET_COLS
    idx_eur = market_cols.index("FX_USD/EUR")
    idx_jpy = market_cols.index("FX_USD/JPY")

    x0_dict = {"FX_USD/EUR": 0.8676, "FX_USD/JPY": 156.60}

    # Kasus 1: Kurs tidak berubah -> q = 1.0
    scen_flat = np.zeros((1, 9))
    scen_flat[0, idx_eur] = 0.8676
    scen_flat[0, idx_jpy] = 156.60
    q_flat = compute_q_factors(scen_flat, market_cols, x0_dict)
    np.testing.assert_allclose(q_flat[0], [1.0, 1.0, 1.0], atol=1e-12)

    # Kasus 2: Kurs nominal naik (mata uang asing melemah -> q turun < 1.0)
    scen_depr = np.zeros((1, 9))
    scen_depr[0, idx_eur] = 1.0000  # naik dari 0.8676
    scen_depr[0, idx_jpy] = 180.00  # naik dari 156.60
    q_depr = compute_q_factors(scen_depr, market_cols, x0_dict)
    assert q_depr[0, 0] == 1.0  # USD selalu 1.0
    assert q_depr[0, 1] < 1.0   # EUR turun
    assert q_depr[0, 2] < 1.0   # JPY turun
    assert np.isclose(q_depr[0, 1], 0.8676 / 1.0000)
    assert np.isclose(q_depr[0, 2], 156.60 / 180.00)


def test_cost_gross_vs_interest_algebra():
    """Uji hubungan aljabar C_gross - C_interest = q (khusus USD = 1.0 persis)."""
    np.random.seed(777)
    market_scen = np.ones((50, 9)) * 4.0
    market_scen[:, ALL_MARKET_COLS.index("FX_USD/EUR")] = 0.85
    market_scen[:, ALL_MARKET_COLS.index("FX_USD/JPY")] = 150.0

    x0_dict = {"FX_USD/EUR": 0.8676, "FX_USD/JPY": 156.60}

    c_gross = compute_scenario_costs(market_scen, ALL_MARKET_COLS, x0_dict, cost_def="gross")
    c_interest = compute_scenario_costs(market_scen, ALL_MARKET_COLS, x0_dict, cost_def="interest")

    assert c_gross.shape == (50, 7)
    assert c_interest.shape == (50, 7)
    assert np.all(c_gross > 0)
    assert np.all(c_interest > 0)

    # Selisih C_gross - C_interest = q * (1 + y/100) - q * (y/100) = q
    diff = c_gross - c_interest

    # Tiga instrumen pertama adalah USD -> q = 1.0 persis
    np.testing.assert_allclose(diff[:, 0], 1.0, atol=1e-12)
    np.testing.assert_allclose(diff[:, 1], 1.0, atol=1e-12)
    np.testing.assert_allclose(diff[:, 2], 1.0, atol=1e-12)

    # Instrumen EUR (indeks 3, 4) -> q_eur
    expected_q_eur = 0.8676 / 0.85
    np.testing.assert_allclose(diff[:, 3], expected_q_eur, atol=1e-12)
    np.testing.assert_allclose(diff[:, 4], expected_q_eur, atol=1e-12)

    # Instrumen JPY (indeks 5, 6) -> q_jpy
    expected_q_jpy = 156.60 / 150.0
    np.testing.assert_allclose(diff[:, 5], expected_q_jpy, atol=1e-12)
    np.testing.assert_allclose(diff[:, 6], expected_q_jpy, atol=1e-12)


def test_build_scenario_bank_integration(sample_gbm_inputs):
    """Uji pembentukan bank skenario lengkap menggunakan parameter riil Tahap 03."""
    df_params, df_corr, s0_series = sample_gbm_inputs
    n = 5000
    seed = 42

    res = generate_market_scenarios(
        df_params=df_params,
        corr_matrix=df_corr,
        s0=s0_series,
        n_scenarios=n,
        seed=seed,
        mode="terminal_1step",
    )

    s0_dict = s0_series.to_dict()
    bank = build_scenario_bank(
        market_scenarios=res["scenarios_market"],
        log_returns=res["scenarios_log_returns"],
        market_cols=ALL_MARKET_COLS,
        s0_dict=s0_dict,
    )

    # Cek kunci-kunci bank
    expected_keys = {
        "scenarios_market",
        "scenarios_log_returns",
        "cost_gross",
        "cost_interest",
        "q_factors",
        "s0",
        "variable_names",
        "instrument_names",
        "currency_names",
    }
    assert expected_keys.issubset(set(bank.keys()))

    assert bank["scenarios_market"].shape == (n, 9)
    assert bank["scenarios_log_returns"].shape == (n, 9)
    assert bank["cost_gross"].shape == (n, 7)
    assert bank["cost_interest"].shape == (n, 7)
    assert bank["q_factors"].shape == (n, 3)

    # Cek tidak ada NaN dan semua positif
    assert np.isnan(bank["scenarios_market"]).sum() == 0
    assert np.isnan(bank["cost_gross"]).sum() == 0
    assert np.all(bank["scenarios_market"] > 0)
    assert np.all(bank["cost_gross"] > 0)
    assert np.all(bank["cost_interest"] > 0)
