"""Unit tests untuk modul mccar_kma.model.limits.

Menguji sifat matematis:
1. Batas acuan risiko Persamaan 2.22: tau = CCaR_alpha(w0) dan eta = J_MCCaR(w0).
2. Kelayakan portofolio eksisting w0 by construction (v_J = 0, v_R = 0, is_feasible = True).
3. Serialisasi dan deserialisasi JSON batas risiko.
4. Pembangkitan kombinasi acak DJPPR: pemenuhan ketat batas proporsi [lb, ub] dan sum(w) = 1.
5. Evaluasi baseline historis DJPPR.
6. Solusi referensi independen SLSQP: konvergensi ke solusi layak dengan biaya <= biaya w0.
"""

from pathlib import Path
import json
import numpy as np
import pytest

from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, W0
from mccar_kma.model.limits import (
    compute_risk_limits,
    save_risk_limits,
    load_risk_limits,
    generate_random_weights_djppr,
    evaluate_djppr_baseline,
    solve_slsqp_reference,
)

# Bank latih yang sudah dibuat di Tahap 04
TRAIN_BANK_PATH = Path("data/processed/bank_train_seed42_N5000.npz")


@pytest.fixture(scope="module")
def train_bank_data():
    if not TRAIN_BANK_PATH.exists():
        pytest.skip(f"File bank latih {TRAIN_BANK_PATH} tidak ditemukan.")
    return np.load(TRAIN_BANK_PATH)


def test_compute_risk_limits_w0_feasibility(train_bank_data):
    """Memastikan w0 layak by construction pada batasnya sendiri untuk gross dan interest."""
    for cost_def in ["gross", "interest"]:
        evaluator = PortfolioEvaluator.from_scenario_bank(train_bank_data, cost_def=cost_def)
        limits = compute_risk_limits(evaluator, w0=W0)

        assert limits["is_feasible"] is True
        assert limits["v_J"] == pytest.approx(0.0, abs=1e-8)
        assert limits["v_R"] == pytest.approx(0.0, abs=1e-8)

        # Nilai tau dan eta harus positif
        assert limits["tau"] > 0.0
        assert limits["eta"] > 0.0
        assert limits["mean_cost"] > 0.0

        # Pada gross, biaya > 1 karena pokok + yield; pada interest, biaya < 1
        if cost_def == "gross":
            assert limits["mean_cost"] > 1.0
            assert limits["tau"] > 1.0
        else:
            assert limits["mean_cost"] < 1.0
            assert limits["tau"] < 1.0


def test_risk_limits_json_io(tmp_path):
    """Memastikan batas risiko dapat disimpan ke JSON dan dimuat kembali secara identik."""
    dummy_data = {
        "metadata": {
            "bank_file": "dummy_bank.npz",
            "seed": 42,
            "alpha": 0.95,
        },
        "gross": {
            "mean_cost": 1.0423699,
            "tau": 1.0859858,
            "eta": 0.0681147,
            "v_J": 0.0,
            "v_R": 0.0,
            "is_feasible": True,
        },
        "interest": {
            "mean_cost": 0.0445259,
            "tau": 0.0649488,
            "eta": 0.1739435,
            "v_J": 0.0,
            "v_R": 0.0,
            "is_feasible": True,
        },
    }

    test_file = tmp_path / "test_risk_limits.json"
    save_risk_limits(test_file, dummy_data)
    loaded = load_risk_limits(test_file)

    assert loaded["gross"]["tau"] == pytest.approx(dummy_data["gross"]["tau"])
    assert loaded["interest"]["eta"] == pytest.approx(dummy_data["interest"]["eta"])
    assert loaded["gross"]["is_feasible"] is True


def test_generate_random_weights_bounds_rejection():
    """Memastikan metode rejection sampling menghasilkan bobot yang valid sum=1 dan lb <= w <= ub."""
    rng = np.random.default_rng(1234)
    weights = generate_random_weights_djppr(
        n_samples=100,
        lb=LB_DJPPR,
        ub=UB_DJPPR,
        rng=rng,
        method="rejection",
    )

    assert weights.shape == (100, 7)
    # Jumlah bobot = 1
    sums = np.sum(weights, axis=1)
    np.testing.assert_allclose(sums, 1.0, atol=1e-8)

    # Batas bawah dan atas
    for i in range(100):
        assert np.all(weights[i] >= LB_DJPPR - 1e-8)
        assert np.all(weights[i] <= UB_DJPPR + 1e-8)


def test_generate_random_weights_bounds_projected():
    """Memastikan metode projected sampling menghasilkan bobot yang valid sum=1 dan lb <= w <= ub."""
    rng = np.random.default_rng(5678)
    weights = generate_random_weights_djppr(
        n_samples=100,
        lb=LB_DJPPR,
        ub=UB_DJPPR,
        rng=rng,
        method="projected",
    )

    assert weights.shape == (100, 7)
    sums = np.sum(weights, axis=1)
    np.testing.assert_allclose(sums, 1.0, atol=1e-8)

    for i in range(100):
        assert np.all(weights[i] >= LB_DJPPR - 1e-8)
        assert np.all(weights[i] <= UB_DJPPR + 1e-8)


def test_djppr_baseline_evaluation(train_bank_data):
    """Memastikan evaluasi baseline menghasilkan persentase layak dan solusi terbaik yang valid."""
    evaluator = PortfolioEvaluator.from_scenario_bank(train_bank_data, cost_def="gross")
    evaluator.set_baseline(W0)

    rng = np.random.default_rng(42)
    weights = generate_random_weights_djppr(n_samples=200, rng=rng, method="rejection")

    baseline_res = evaluate_djppr_baseline(evaluator, weights)

    assert baseline_res["n_samples"] == 200
    assert 0 <= baseline_res["n_feasible"] <= 200
    assert 0.0 <= baseline_res["pct_feasible"] <= 100.0

    if baseline_res["n_feasible"] > 0:
        best = baseline_res["best_cost_feasible"]
        assert best is not None
        assert best["v_J"] <= 1e-8
        assert best["v_R"] <= 1e-8
        assert best["mean_cost"] > 0.0


def test_slsqp_reference_optimizer(train_bank_data):
    """Memastikan SLSQP menemukan solusi layak dengan biaya <= biaya w0."""
    evaluator = PortfolioEvaluator.from_scenario_bank(train_bank_data, cost_def="interest")
    base = evaluator.set_baseline(W0)
    w0_cost = base["mean_cost"]

    # Jalankan solver referensi SLSQP
    res_slsqp = solve_slsqp_reference(
        evaluator,
        lb=LB_DJPPR,
        ub=UB_DJPPR,
        initial_points=[W0.copy()],
        max_iter=100,
    )

    assert res_slsqp["is_feasible"] is True
    assert res_slsqp["v_J"] <= 1e-8
    assert res_slsqp["v_R"] <= 1e-8
    # Biaya solusi optimal referensi harus <= biaya w0
    assert res_slsqp["mean_cost"] <= w0_cost + 1e-8
