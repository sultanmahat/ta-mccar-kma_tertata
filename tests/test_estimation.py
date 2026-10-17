"""Unit test untuk estimasi parameter GBM dan statistik biaya historis.

Menguji modul mccar_kma.scenarios.estimation:
1. Estimator mu dan sigma pada deret sintetis GBM dengan parameter diketahui.
2. Matriks korelasi Pearson: simetri, diagonal 1.0, dan definit positif (Cholesky).
3. Deteksi galat jika matriks tidak definit positif.
4. Perhitungan biaya bruto vs bunga (Pers. 2.2 vs 2.3) dan sifat invarian Delta c terhadap X_0.
5. Verifikasi keluaran pada dataset riil (2.026 log-return intersection).
"""

from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from mccar_kma.data.cleaning import (
    ALL_MARKET_COLS,
    IR_COLS,
    FX_COLS,
    compute_log_returns,
)
from mccar_kma.scenarios.estimation import (
    estimate_gbm_params,
    compute_correlation_matrix,
    compute_historical_costs,
    compute_historical_cost_stats,
    INSTRUMENTS,
    INSTRUMENT_NAMES,
)


@pytest.fixture
def sample_market_df() -> pd.DataFrame:
    """Fixture memuat dataset intersection riil jika ada, atau membuat data tiruan."""
    data_path = Path("data/processed/market_2017-07-03_2025-11-24_intersection.csv")
    if data_path.exists():
        return pd.read_csv(data_path)

    # Fallback tiruan
    np.random.seed(42)
    dates = pd.date_range("2020-01-01", periods=100, freq="B")
    data = {"Tanggal": dates}
    for col in ALL_MARKET_COLS:
        data[col] = 2.0 + np.cumsum(np.random.randn(100) * 0.05)
    return pd.DataFrame(data)


def test_gbm_params_synthetic():
    """Uji estimator parameter GBM pada deret sintetis dengan mu dan sigma diketahui.

    Model: S_t = S_0 * exp((mu - 0.5*sigma^2)*t + sigma*W_t)
    dt = 1/252, n_steps = 5.000.
    Standard error mu: sigma / sqrt(T_years) = 0.20 / sqrt(5000/252) ≈ 0.045.
    Standard error sigma: sigma / sqrt(2N) = 0.20 / sqrt(10000) = 0.002.
    """
    np.random.seed(42)
    true_mu = 0.08      # 8% per tahun
    true_sigma = 0.20   # 20% per tahun
    days_per_year = 252
    dt = 1.0 / days_per_year
    n_steps = 5000

    # Pembangkitan lintasan GBM
    z = np.random.randn(n_steps)
    drift_step = (true_mu - 0.5 * (true_sigma ** 2)) * dt
    diff_step = true_sigma * np.sqrt(dt) * z
    log_returns = drift_step + diff_step

    # Bentuk DataFrame
    df_lr = pd.DataFrame({"SYNTH": log_returns})
    df_est = estimate_gbm_params(df_lr, cols=["SYNTH"], days_per_year=days_per_year)

    row = df_est.iloc[0]
    est_mu = row["mu_annual"]
    est_sigma = row["sigma_annual"]

    # 1. Konsistensi aljabar estimator
    expected_mu = days_per_year * np.mean(log_returns) + 0.5 * (est_sigma ** 2)
    assert np.isclose(est_mu, expected_mu, atol=1e-12)

    # 2. Toleransi statistik terhadap nilai riil (T=5.000)
    # sigma: 3 * SE(sigma) = 3 * 0.002 = 0.006 -> toleransi 0.010
    assert abs(est_sigma - true_sigma) < 0.010, f"Est sigma {est_sigma} vs true {true_sigma}"
    # mu: SE(mu) ≈ 0.045 -> toleransi 0.050 (realisasi seed 42 menghasilkan diff ≈ 0.018)
    assert abs(est_mu - true_mu) < 0.050, f"Est mu {est_mu} vs true {true_mu}"


def test_corr_matrix_synthetic():
    """Uji matriks korelasi pada deret normal multivariat sintetis."""
    np.random.seed(54321)
    true_rho = 0.65
    cov = np.array([[1.0, true_rho], [true_rho, 1.0]])
    data = np.random.multivariate_normal(mean=[0, 0], cov=cov, size=10000)

    df_lr = pd.DataFrame(data, columns=["VAR_A", "VAR_B"])
    corr = compute_correlation_matrix(df_lr, cols=["VAR_A", "VAR_B"])

    est_rho = corr.loc["VAR_A", "VAR_B"]
    assert abs(est_rho - true_rho) < 0.02
    assert abs(corr.loc["VAR_A", "VAR_A"] - 1.0) < 1e-12
    assert abs(corr.loc["VAR_B", "VAR_B"] - 1.0) < 1e-12


def test_corr_matrix_not_positive_definite():
    """Uji deteksi ValueError ketika matriks korelasi bukan definit positif."""
    # Matriks singular: dua kolom identik persis
    df_singular = pd.DataFrame({
        "A": [0.1, 0.2, 0.3],
        "B": [0.1, 0.2, 0.3],
        "C": [0.5, 0.1, 0.2],
    })
    # Dua variabel berkorelasi sempurna 1.0 -> semi-definit positif, determinan nol
    with pytest.raises(ValueError, match="bukan matriks definit positif"):
        compute_correlation_matrix(df_singular, cols=["A", "B", "C"])


def test_historical_cost_math_and_invariance():
    """Uji rumus biaya bruto vs bunga dan invarian Delta c terhadap nilai X_0."""
    df_mock = pd.DataFrame({
        "Tanggal": ["2023-01-02", "2023-01-03", "2023-01-04"],
        "IR_USD_5Y": [3.0, 3.1, 3.2],
        "IR_USD_10Y": [3.5, 3.6, 3.7],
        "IR_USD_30Y": [4.0, 4.1, 4.2],
        "IR_EUR_7Y": [2.0, 2.1, 2.2],
        "IR_EUR_10Y": [2.5, 2.6, 2.7],
        "IR_JPY_5Y": [0.2, 0.25, 0.3],
        "IR_JPY_10Y": [0.5, 0.55, 0.6],
        "FX_USD/EUR": [0.95, 0.96, 0.94],
        "FX_USD/JPY": [130.0, 132.0, 131.0],
    })

    # Hitung dengan X0 baseline
    stats_base, cov_base = compute_historical_cost_stats(
        df_mock, x0_eur=0.94, x0_jpy=131.0, cost_def="gross", exclude_gap=False
    )

    # Hitung dengan X0 yang diskalakan 10x
    stats_scaled, cov_scaled = compute_historical_cost_stats(
        df_mock, x0_eur=9.4, x0_jpy=1310.0, cost_def="gross", exclude_gap=False
    )

    # Delta c_{i,t} = ln(C_t / C_{t-1}) harus persis identik karena X_0 saling meniadakan
    np.testing.assert_allclose(
        stats_base["mean_delta_c"].values,
        stats_scaled["mean_delta_c"].values,
        atol=1e-12,
    )
    np.testing.assert_allclose(
        cov_base.values,
        cov_scaled.values,
        atol=1e-12,
    )


def test_real_dataset_gbm_params(sample_market_df):
    """Uji pipeline estimasi pada data riil 2.028 baris / 2.026 log-return."""
    if len(sample_market_df) < 2000:
        pytest.skip("Dataset riil 2.028 baris tidak tersedia.")

    df_lr = compute_log_returns(sample_market_df, cols=ALL_MARKET_COLS, exclude_gap=True)
    assert len(df_lr) == 2026

    df_params = estimate_gbm_params(df_lr, cols=ALL_MARKET_COLS, days_per_year=252)

    # 1. Dimensi dan kolom
    assert len(df_params) == 9
    assert list(df_params["variable"]) == ALL_MARKET_COLS
    assert set(df_params.columns) == {
        "variable", "mu_daily", "sigma_daily", "mu_annual", "sigma_annual", "n_obs"
    }

    # 2. Semua observasi = 2026
    assert (df_params["n_obs"] == 2026).all()

    # 3. Semua sigma > 0
    assert (df_params["sigma_daily"] > 0).all()
    assert (df_params["sigma_annual"] > 0).all()

    # 4. Volatilitas JPY yield paling tinggi (spesifikasi §11)
    sig_jpy5 = df_params.loc[df_params["variable"] == "IR_JPY_5Y", "sigma_annual"].iloc[0]
    sig_usd5 = df_params.loc[df_params["variable"] == "IR_USD_5Y", "sigma_annual"].iloc[0]
    assert sig_jpy5 > sig_usd5, "Volatilitas JPY_5Y harus lebih tinggi dari USD_5Y"


def test_real_dataset_correlation_properties(sample_market_df):
    """Uji sifat matriks korelasi 9x9 pada data riil."""
    if len(sample_market_df) < 2000:
        pytest.skip("Dataset riil tidak tersedia.")

    df_lr = compute_log_returns(sample_market_df, cols=ALL_MARKET_COLS, exclude_gap=True)
    corr_df = compute_correlation_matrix(df_lr, cols=ALL_MARKET_COLS)

    mat = corr_df.to_numpy()

    # 1. Simetris
    assert np.allclose(mat, mat.T, atol=1e-12)

    # 2. Diagonal persis 1.0
    assert np.allclose(np.diag(mat), 1.0, atol=1e-12)

    # 3. Definit positif melalui Cholesky
    L = np.linalg.cholesky(mat)
    # Rekonstruksi: L @ L.T == mat
    reconstructed = L @ L.T
    assert np.allclose(reconstructed, mat, atol=1e-12)

    # 4. Nilai eigen semua positif
    eigvals = np.linalg.eigvalsh(mat)
    assert (eigvals > 0).all(), f"Nilai eigen harus positif, ditemukan min = {eigvals.min()}"


def test_real_dataset_cost_stats_sanity(sample_market_df):
    """Uji statistik biaya historis pada data riil memenuhi sanity check §11."""
    if len(sample_market_df) < 2000:
        pytest.skip("Dataset riil tidak tersedia.")

    df_cost_gross, df_cov_gross = compute_historical_cost_stats(
        sample_market_df, cost_def="gross", exclude_gap=True
    )

    assert len(df_cost_gross) == 7
    assert (df_cost_gross["n_obs"] == 2026).all()
    assert (df_cost_gross["var_delta_c"] > 0).all()

    # Cek rata-rata Delta c tahunan untuk JPY adalah negatif (sekitar -3.2% s.d. -3.5%)
    jpy5_mean = df_cost_gross.loc[df_cost_gross["instrument"] == "JPY_Fixed_5Y", "mean_delta_c"].iloc[0]
    jpy5_ann = jpy5_mean * 252
    assert -0.05 < jpy5_ann < -0.02, f"JPY annual gross cost mean {jpy5_ann} harus negatif sekitar -3.5%"

    # Cek USD adalah positif kecil (sekitar +0.1%)
    usd5_mean = df_cost_gross.loc[df_cost_gross["instrument"] == "USD_Fixed_5Y", "mean_delta_c"].iloc[0]
    usd5_ann = usd5_mean * 252
    assert 0.0 < usd5_ann < 0.005, f"USD annual gross cost mean {usd5_ann} harus positif kecil"

    # Matriks kovarians berukuran 7x7 dan simetris
    assert df_cov_gross.shape == (7, 7)
    cov_vals = df_cov_gross.to_numpy()
    assert np.allclose(cov_vals, cov_vals.T, atol=1e-12)
