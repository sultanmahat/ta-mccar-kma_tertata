"""Pengujian Unit dan Validasi Genetic Algorithm (GA).

Menguji:
1. Batas anggaran evaluasi yang ketat (tidak pernah melebihi dan tepat sesuai anggaran)
2. Reproduksibilitas berbasis seed acak (seed identik menghasilkan solusi identik)
3. Kelayakan solusi akhir (sum(w) = 1, lb <= w <= ub, v_J <= 1e-8, v_R <= 1e-8)
4. Masalah optimasi linear sintetis dengan solusi optimum analitis yang diketahui
"""

import numpy as np
import pytest

from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR


class MockLinearEvaluator:
    """Evaluator linear deterministik untuk pengujian analitis."""

    def __init__(self, c: np.ndarray) -> None:
        self.c = np.asarray(c, dtype=float)

    def evaluate(self, w: np.ndarray, apply_penalty: bool = True) -> dict:
        cost = float(np.dot(self.c, w))
        return {
            "mean_cost": cost,
            "f_val": cost,
            "ccar": 0.0,
            "j_mccar": 0.0,
            "v_J": 0.0,
            "v_R": 0.0,
            "is_feasible": True,
        }

    def evaluate_batch(self, W: np.ndarray, apply_penalty: bool = True) -> dict:
        costs = W @ self.c
        n = len(W)
        return {
            "mean_cost": costs,
            "f_val": costs,
            "ccar": np.zeros(n),
            "j_mccar": np.zeros(n),
            "v_J": np.zeros(n),
            "v_R": np.zeros(n),
            "is_feasible": np.ones(n, dtype=bool),
            "mccar": np.zeros((n, len(self.c))),
            "theta": np.zeros((n, len(self.c))),
            "theta_bar": np.zeros(n),
        }


def test_ga_budget_strictness() -> None:
    """Menguji bahwa GA tidak pernah melampaui anggaran dan tepat mencapai batas."""
    c = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    evaluator = MockLinearEvaluator(c)
    lb = np.full(7, 0.05)
    ub = np.full(7, 0.40)

    # 1. Anggaran kecil 500
    opt_small = GeneticAlgorithmOptimizer(n_pop=50, check_interval=50)
    res_small = opt_small.run(evaluator=evaluator, lb=lb, ub=ub, budget=500, rng=123)
    assert res_small.evaluations_used == 500
    assert opt_small.budget.evaluations == 500
    assert opt_small.budget.remaining == 0

    # 2. Anggaran menengah 2.500
    opt_mid = GeneticAlgorithmOptimizer(n_pop=50, check_interval=250)
    res_mid = opt_mid.run(evaluator=evaluator, lb=lb, ub=ub, budget=2500, rng=456)
    assert res_mid.evaluations_used == 2500
    assert opt_mid.budget.evaluations == 2500
    assert opt_mid.budget.remaining == 0


def test_ga_seed_reproducibility() -> None:
    """Menguji reproduksibilitas: seed sama menghasilkan keluaran identik bit-per-bit."""
    c = np.array([2.5, 1.2, 3.8, 0.9, 4.1, 1.7, 2.0])
    evaluator = MockLinearEvaluator(c)
    lb = np.array([0.05, 0.05, 0.10, 0.10, 0.05, 0.05, 0.05])
    ub = np.array([0.30, 0.25, 0.35, 0.25, 0.20, 0.20, 0.20])

    opt1 = GeneticAlgorithmOptimizer(n_pop=50, check_interval=100)
    res1 = opt1.run(evaluator=evaluator, lb=lb, ub=ub, budget=1000, rng=888)

    opt2 = GeneticAlgorithmOptimizer(n_pop=50, check_interval=100)
    res2 = opt2.run(evaluator=evaluator, lb=lb, ub=ub, budget=1000, rng=888)

    assert np.allclose(res1.best_w, res2.best_w, atol=1e-14)
    assert res1.best_cost == pytest.approx(res2.best_cost, abs=1e-12)
    assert res1.evaluations_used == res2.evaluations_used
    assert len(res1.convergence_history) == len(res2.convergence_history)
    for h1, h2 in zip(res1.convergence_history, res2.convergence_history):
        assert h1["evaluation"] == h2["evaluation"]
        assert h1["best_cost"] == pytest.approx(h2["best_cost"], abs=1e-12)


def test_ga_solution_feasibility() -> None:
    """Menguji bahwa bobot keluaran GA selalu memenuhi kendala proporsi dan sum(w)=1 dalam 1e-8."""
    c = np.array([1.5, 2.3, 0.8, 3.1, 1.1, 2.7, 0.5])
    evaluator = MockLinearEvaluator(c)
    lb = LB_DJPPR
    ub = UB_DJPPR

    opt = GeneticAlgorithmOptimizer(n_pop=50, check_interval=150)
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=1500, rng=555)

    assert abs(np.sum(res.best_w) - 1.0) <= 1e-8
    assert np.all(res.best_w >= lb - 1e-8)
    assert np.all(res.best_w <= ub + 1e-8)
    assert res.is_feasible is True
    assert res.v_J <= 1e-8
    assert res.v_R <= 1e-8


def test_ga_known_linear_optimum() -> None:
    """Menguji GA pada masalah linear analitis dengan optimum c^T w* = 2.40."""
    c = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    lb = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
    ub = np.array([0.40, 0.30, 0.20, 0.20, 0.20, 0.20, 0.20])
    w_star = np.array([0.40, 0.30, 0.10, 0.05, 0.05, 0.05, 0.05])
    optimum_cost = 2.40

    evaluator = MockLinearEvaluator(c)
    opt = GeneticAlgorithmOptimizer(n_pop=50, check_interval=250)
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=5000, rng=42)

    assert res.best_cost >= optimum_cost - 1e-8
    assert res.best_cost <= optimum_cost + 0.05  # Toleransi konvergensi GA
    assert np.allclose(res.best_w, w_star, atol=0.05)
