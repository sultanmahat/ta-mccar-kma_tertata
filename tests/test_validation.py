"""Pengujian unit dan integrasi untuk modul validasi independen (Tahap 12)."""

from pathlib import Path
import json
import numpy as np
import pandas as pd
import pytest
import yaml

from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.analysis.validation import (
    validate_single_portfolio,
    validate_all_runs,
    evaluate_benchmarks_validation,
    generate_validation_comparison_tables,
)


@pytest.fixture
def paths():
    base = Path(__file__).resolve().parent.parent
    return {
        "params": base / "configs" / "params.yaml",
        "bank_valid": base / "data" / "processed" / "bank_valid_seed2026_N20000.npz",
        "limits": base / "data" / "processed" / "risk_limits_bank_train_seed42_N5000.json",
        "runs_summary": base / "results" / "tables" / "runs_summary.csv",
        "baseline_gross": base / "results" / "tables" / "baseline_djppr_gross.csv",
        "baseline_interest": base / "results" / "tables" / "baseline_djppr_interest.csv",
    }


def test_validate_single_portfolio_w0(paths):
    """Memverifikasi evaluasi portofolio eksisting w0 pada bank validasi N=20.000."""
    with open(paths["limits"], "r", encoding="utf-8") as f:
        limits = json.load(f)
    with open(paths["params"], "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    items = params["instruments"]["items"]
    lb_djppr = np.array([it["lb"] for it in items])
    ub_djppr = np.array([it["ub"] for it in items])

    # Gross
    ev_g = PortfolioEvaluator.from_scenario_bank(
        paths["bank_valid"],
        cost_def="gross",
        tau=limits["gross"]["tau"],
        eta=limits["gross"]["eta"],
    )
    w0_g = np.array(limits["gross"]["w0"])
    res_g = validate_single_portfolio(w0_g, ev_g, lb_djppr, ub_djppr, eps_tol=1e-8)

    assert res_g["is_weight_feasible"] is True
    assert res_g["max_sum_err"] < 1e-8
    assert res_g["max_bound_err"] < 1e-8
    assert res_g["ccar"] <= limits["gross"]["tau"] + 1e-8
    assert res_g["j_mccar"] <= limits["gross"]["eta"] + 1e-8
    assert res_g["is_feasible"] is True

    # Interest
    ev_i = PortfolioEvaluator.from_scenario_bank(
        paths["bank_valid"],
        cost_def="interest",
        tau=limits["interest"]["tau"],
        eta=limits["interest"]["eta"],
    )
    w0_i = np.array(limits["interest"]["w0"])
    res_i = validate_single_portfolio(w0_i, ev_i, lb_djppr, ub_djppr, eps_tol=1e-8)

    assert res_i["is_weight_feasible"] is True
    assert res_i["max_sum_err"] < 1e-8
    assert res_i["max_bound_err"] < 1e-8
    assert res_i["ccar"] <= limits["interest"]["tau"] + 1e-8
    assert res_i["j_mccar"] <= limits["interest"]["eta"] + 1e-8
    assert res_i["is_feasible"] is True


def test_runs_summary_weight_feasibility(paths):
    """Memverifikasi seluruh 360 solusi di runs_summary.csv memenuhi kendala bobot dalam toleransi 1e-8."""
    df = pd.read_csv(paths["runs_summary"])
    assert len(df) == 360

    with open(paths["params"], "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    items = params["instruments"]["items"]
    lb_djppr = np.array([it["lb"] for it in items])
    ub_djppr = np.array([it["ub"] for it in items])

    w_cols = [f"w_{i}" for i in range(1, 8)]
    W = df[w_cols].values

    # 1. Sum of weights == 1.0 within 1e-8
    sum_err = np.abs(np.sum(W, axis=1) - 1.0)
    assert np.all(sum_err <= 1e-8)

    # 2. DJPPR bounds within 1e-8
    is_djppr = (df["constraint_type"] == "djppr").values
    W_djppr = W[is_djppr]
    assert np.all(W_djppr >= lb_djppr - 1e-8)
    assert np.all(W_djppr <= ub_djppr + 1e-8)

    # 3. Free bounds within 1e-8
    W_free = W[~is_djppr]
    assert np.all(W_free >= 0.0 - 1e-8)
    assert np.all(W_free <= 1.0 + 1e-8)


def test_evaluate_benchmarks_validation(paths):
    """Memverifikasi fungsi evaluasi benchmark pada bank validasi."""
    benchmarks = evaluate_benchmarks_validation(
        bank_valid_path=paths["bank_valid"],
        limits_path=paths["limits"],
        baseline_gross_csv=paths["baseline_gross"],
        baseline_interest_csv=paths["baseline_interest"],
        params_path=paths["params"],
        eps_tol=1e-8,
    )

    assert "existing" in benchmarks
    assert "baseline_djppr" in benchmarks

    # Cek Eksisting
    assert benchmarks["existing"]["gross"]["is_feasible"] is True
    assert benchmarks["existing"]["interest"]["is_feasible"] is True

    # Cek Baseline DJPPR
    bg = benchmarks["baseline_djppr"]["gross"]
    bi = benchmarks["baseline_djppr"]["interest"]

    assert bg["total_tested"] == 398
    assert bg["feasible_count"] == 398
    assert bg["feasibility_rate"] == 1.0

    assert bi["total_tested"] == 440
    assert bi["feasible_count"] == 440
    assert bi["feasibility_rate"] == 1.0


def test_generate_validation_comparison_tables(paths):
    """Memverifikasi pembuatan tabel komparasi dan markdown ringkasan."""
    # Jalankan validasi pada subsampel untuk kecepatan tes
    df_runs = pd.read_csv(paths["runs_summary"])
    # Ambil 1 baris per algo per config (12 baris)
    sub_runs = df_runs.groupby(["config_id", "algo"]).first().reset_index()

    temp_runs_csv = paths["runs_summary"].parent / "temp_test_runs.csv"
    sub_runs.to_csv(temp_runs_csv, index=False)

    try:
        val_df = validate_all_runs(
            runs_summary_path=temp_runs_csv,
            bank_valid_path=paths["bank_valid"],
            limits_path=paths["limits"],
            params_path=paths["params"],
            eps_tol=1e-8,
        )
        assert len(val_df) == 12

        benchmarks = evaluate_benchmarks_validation(
            bank_valid_path=paths["bank_valid"],
            limits_path=paths["limits"],
            baseline_gross_csv=paths["baseline_gross"],
            baseline_interest_csv=paths["baseline_interest"],
            params_path=paths["params"],
            eps_tol=1e-8,
        )

        tables, md = generate_validation_comparison_tables(
            val_df=val_df,
            benchmarks_dict=benchmarks,
            params_path=paths["params"],
        )

        assert len(tables) == 4
        assert "gross_free" in tables
        assert "gross_djppr" in tables
        assert "interest_free" in tables
        assert "interest_djppr" in tables

        assert "Ringkasan Validasi Independen" in md
        assert "Eksisting 2024" in md
        assert "Baseline DJPPR" in md
        assert "KMA" in md
    finally:
        if temp_runs_csv.exists():
            temp_runs_csv.unlink()
