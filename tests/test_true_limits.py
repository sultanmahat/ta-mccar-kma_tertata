"""Tes modul kelayakan terhadap batas benar (Tahap 21, Persamaan 2.22-2.23)."""

import numpy as np
import pandas as pd
import pytest

from mccar_kma.analysis.true_limits import (
    add_true_limit_columns,
    summarize_true_limit_feasibility,
)

EPS = 1e-8
LIMITS = {"gross": {"eta": 0.05, "tau": 1.10}}


def _frame(rows):
    base = {"config_id": "gross_free", "cost_definition": "gross", "algo": "kma",
            "val_weight_feasible": True, "val_is_feasible": True}
    return pd.DataFrame([{**base, **r} for r in rows])


def test_solution_on_the_limit_is_feasible():
    df = add_true_limit_columns(_frame([{"val_j_mccar": 0.05, "val_ccar": 1.10}]), LIMITS, EPS)
    assert df.loc[0, "v_J_true"] == 0.0
    assert df.loc[0, "v_R_true"] == 0.0
    assert bool(df.loc[0, "feasible_true"])


def test_relative_violation_matches_equation_2_23():
    # J 10% di atas eta, CCaR 2% di atas tau -> v_J = 0,10 dan v_R = 0,02
    df = add_true_limit_columns(_frame([{"val_j_mccar": 0.055, "val_ccar": 1.122}]), LIMITS, EPS)
    assert df.loc[0, "v_J_true"] == pytest.approx(0.10, rel=1e-12)
    assert df.loc[0, "v_R_true"] == pytest.approx(0.02, rel=1e-12)
    assert not bool(df.loc[0, "feasible_true"])


def test_weight_infeasible_solution_is_never_feasible():
    df = add_true_limit_columns(
        _frame([{"val_j_mccar": 0.01, "val_ccar": 1.0, "val_weight_feasible": False}]), LIMITS, EPS
    )
    assert df.loc[0, "v_J_true"] == 0.0
    assert not bool(df.loc[0, "feasible_true"])


def test_violation_below_tolerance_counts_as_feasible():
    j = 0.05 * (1.0 + 0.5 * EPS)
    df = add_true_limit_columns(_frame([{"val_j_mccar": j, "val_ccar": 1.0}]), LIMITS, EPS)
    assert bool(df.loc[0, "feasible_true"])


def test_summary_counts_and_clopper_pearson_edges():
    rows = [{"val_j_mccar": 0.06, "val_ccar": 1.0}] * 4  # semua melanggar J
    rows += [{"val_j_mccar": 0.04, "val_ccar": 1.0, "algo": "ga"}] * 4  # semua layak
    df = add_true_limit_columns(_frame(rows), LIMITS, EPS)
    s = summarize_true_limit_feasibility(df, ["config_id", "algo"], level=0.95, eps_tol=EPS)
    kma = s[s["algo"] == "kma"].iloc[0]
    ga = s[s["algo"] == "ga"].iloc[0]
    assert (kma["n"], kma["k_true_limits"], kma["k_train_limits"]) == (4, 0, 4)
    assert kma["n_violate_J_true"] == 4 and kma["n_violate_R_true"] == 0
    assert kma["cp_lo_true"] == 0.0 and 0.0 < kma["cp_hi_true"] < 1.0
    assert ga["k_true_limits"] == 4 and ga["cp_hi_true"] == 1.0
    assert kma["max_v_J_true"] == pytest.approx(0.2, rel=1e-12)
    assert np.isclose(kma["eta_true"], 0.05)
