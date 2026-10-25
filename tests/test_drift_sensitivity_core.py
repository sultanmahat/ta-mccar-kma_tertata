"""Tes fungsi inti scripts/16_analyze_drift_sensitivity.py (celah R9, audit_ulang_2026-10-25.md).

Logika sensitivitas drift GBM berada di skrip, bukan di src/, dan tidak punya tes.
Skrip ini dimuat langsung via importlib (nama berawalan angka, tidak bisa diimpor
sebagai paket Python biasa) supaya fungsi intinya bisa diuji tanpa menjalankan main().
"""

import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT_PATH = REPO_ROOT / "scripts" / "16_analyze_drift_sensitivity.py"


def _load_script_module():
    spec = importlib.util.spec_from_file_location("drift_sensitivity_script_16", SCRIPT_PATH)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def script16():
    if not SCRIPT_PATH.exists():
        pytest.skip("scripts/16_analyze_drift_sensitivity.py tidak ditemukan.")
    return _load_script_module()


@pytest.fixture(scope="module")
def market_inputs():
    proc = REPO_ROOT / "data" / "processed"
    params_path = proc / "gbm_params_intersection.csv"
    corr_path = proc / "corr_intersection.csv"
    market_path = proc / "market_2017-07-03_2025-11-24_intersection.csv"
    if not (params_path.exists() and corr_path.exists() and market_path.exists()):
        pytest.skip("Data olahan intersection (Tahap 02-03) belum di-generate.")
    from mccar_kma.data.cleaning import ALL_MARKET_COLS

    df_params = pd.read_csv(params_path)
    df_corr = pd.read_csv(corr_path, index_col=0)
    df_market = pd.read_csv(market_path)
    s0 = pd.Series({c: float(df_market.iloc[-1][c]) for c in ALL_MARKET_COLS})
    return df_params, df_corr, s0


# ------------------------------------------------------------------------------
# build_drift_scenario_bank: logika penyesuaian mu per skenario drift
# ------------------------------------------------------------------------------

def test_build_drift_scenario_bank_mu_adjustment(script16, market_inputs):
    df_params_base, df_corr, s0 = market_inputs

    historical = script16.build_drift_scenario_bank(
        "historical", df_params_base, df_corr, s0, n_scenarios=20
    )
    np.testing.assert_array_equal(
        historical["df_params"]["mu_annual"].to_numpy(),
        df_params_base["mu_annual"].to_numpy(),
    )

    fx_zero = script16.build_drift_scenario_bank(
        "fx_zero", df_params_base, df_corr, s0, n_scenarios=20
    )
    is_fx = fx_zero["df_params"]["variable"].str.startswith("FX_")
    assert np.all(fx_zero["df_params"].loc[is_fx, "mu_annual"].to_numpy() == 0.0)
    np.testing.assert_array_equal(
        fx_zero["df_params"].loc[~is_fx, "mu_annual"].to_numpy(),
        df_params_base.loc[~is_fx, "mu_annual"].to_numpy(),
    )

    martingale = script16.build_drift_scenario_bank(
        "martingale", df_params_base, df_corr, s0, n_scenarios=20
    )
    assert np.all(martingale["df_params"]["mu_annual"].to_numpy() == 0.0)

    shrink = script16.build_drift_scenario_bank(
        "shrinkage_half", df_params_base, df_corr, s0, n_scenarios=20
    )
    np.testing.assert_allclose(
        shrink["df_params"]["mu_annual"].to_numpy(),
        0.5 * df_params_base["mu_annual"].to_numpy(),
    )

    # Skenario tak dikenal -> KeyError pada lookup DRIFT_SCENARIOS[scenario_key]
    # (baris pertama fungsi, sebelum percabangan if/elif/else yang punya raise ValueError).
    with pytest.raises(KeyError):
        script16.build_drift_scenario_bank(
            "skenario_tidak_dikenal", df_params_base, df_corr, s0, n_scenarios=20
        )

    # Bank harus memuat matriks biaya konsisten dengan ukuran n_scenarios
    assert historical["bank"]["cost_gross"].shape[0] == 20
    assert historical["bank"]["cost_interest"].shape[0] == 20
    assert "tau" in historical["base_gross"] and "eta" in historical["base_gross"]


# ------------------------------------------------------------------------------
# _run_single_drift_pso: savings_pct dan flag kendala aktif
# ------------------------------------------------------------------------------

def test_run_single_drift_pso_savings_and_active_flags(script16):
    from mccar_kma.scenarios.estimation import INSTRUMENT_NAMES

    rng = np.random.default_rng(0)
    cost_mat = rng.uniform(0.5, 1.5, size=(200, 7))
    tau = float(np.quantile(cost_mat.sum(axis=1), 0.99))  # longgar: mudah layak
    eta = 10.0  # longgar: mudah layak
    w0_cost = 1.0

    args = ("historical", "gross_free", 1, 123, 300, cost_mat, tau, eta, w0_cost)
    record = script16._run_single_drift_pso(args)

    assert record["scenario"] == "historical"
    assert record["config_id"] == "gross_free"
    assert record["cost_def"] == "gross"
    assert record["boundary"] == "free"

    expected_savings = ((w0_cost - record["best_cost"]) / w0_cost) * 100.0
    assert record["savings_pct"] == pytest.approx(expected_savings)

    assert isinstance(record["is_j_active"], (bool, np.bool_))
    assert isinstance(record["is_r_active"], (bool, np.bool_))
    for inst in INSTRUMENT_NAMES:
        assert f"w_{inst}" in record
    assert abs(sum(record[f"w_{inst}"] for inst in INSTRUMENT_NAMES) - 1.0) < 1e-6


def test_run_single_drift_pso_djppr_uses_bounded_box(script16):
    from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR

    rng = np.random.default_rng(1)
    cost_mat = rng.uniform(0.5, 1.5, size=(200, 7))
    tau = float(np.quantile(cost_mat.sum(axis=1), 0.99))
    eta = 10.0

    args = ("historical", "gross_djppr", 1, 321, 300, cost_mat, tau, eta, 1.0)
    record = script16._run_single_drift_pso(args)

    assert record["boundary"] == "djppr"
    from mccar_kma.scenarios.estimation import INSTRUMENT_NAMES

    w = np.array([record[f"w_{inst}"] for inst in INSTRUMENT_NAMES])
    assert np.all(w >= LB_DJPPR - 1e-6) and np.all(w <= UB_DJPPR + 1e-6)
