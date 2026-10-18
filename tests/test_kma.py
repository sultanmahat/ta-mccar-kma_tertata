"""Pengujian Unit dan Validasi Komodo Mlipir Algorithm (KMA).

Menguji:
1. Pembagian kelompok komodo (Persamaan 2.25)
2. Batas anggaran evaluasi yang ketat (tidak pernah melebihi dan tepat sesuai anggaran)
3. Reproduksibilitas berbasis seed acak (seed identik menghasilkan solusi identik)
4. Kelayakan solusi akhir (sum(w) = 1, lb <= w <= ub, v_J <= 1e-8, v_R <= 1e-8)
5. Masalah optimasi linear sintetis dengan solusi optimum analitis yang diketahui
6. Smoke test 3 replikasi pada evaluator riil portofolio (gross_djppr, N=5.000)
"""

from pathlib import Path
import time
import numpy as np
import pytest

from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer, compute_group_sizes
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, W0
from mccar_kma.risk.evaluator import PortfolioEvaluator


class MockLinearEvaluator:
    """Evaluator linear deterministik untuk pengujian analitis.

    Fungsi objektif: f(w) = c^T w
    Tanpa penalti risiko (v_J = 0, v_R = 0, ccar = 0, j_mccar = 0).
    """

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


def test_compute_group_sizes() -> None:
    """Menguji kebenaran rumus Persamaan 2.25 pembagian kelompok Komodo."""
    # Fase 1: n_pop = 5, p_bm = 0.5
    # n* = floor(0.5 * 4) = 2 -> n_bm = min(max(2, 2), 2) = 2, female = 1, small_males = 2
    n_bm, n_f, n_sm = compute_group_sizes(5, p_bm=0.5)
    assert n_bm == 2
    assert n_f == 1
    assert n_sm == 2
    assert n_bm + n_f + n_sm == 5

    # Fase 2: n_pop = 200, p_bm = 0.5
    # n* = floor(0.5 * 199) = 99 -> n_bm = min(max(99, 2), 197) = 99, female = 1, small_males = 100
    n_bm, n_f, n_sm = compute_group_sizes(200, p_bm=0.5)
    assert n_bm == 99
    assert n_f == 1
    assert n_sm == 100
    assert n_bm + n_f + n_sm == 200

    # Batas minimum Fase 2: n_pop = 20, p_bm = 0.5
    n_bm, n_f, n_sm = compute_group_sizes(20, p_bm=0.5)
    assert n_bm + n_f + n_sm == 20
    assert n_f == 1
    assert n_bm >= 2
    assert n_sm >= 1


def test_kma_budget_strictness() -> None:
    """Menguji bahwa anggaran evaluasi tidak pernah terlampaui dan tepat sesuai target."""
    c = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    evaluator = MockLinearEvaluator(c)
    lb = np.full(7, 0.05)
    ub = np.full(7, 0.40)

    # 1. Uji pada anggaran kecil (500)
    opt_small = KomodoMlipirOptimizer(
        phase_1_budget=100,
        phase_2_budget=400,
        phase_2_n_pop_init=20,
        phase_2_n_pop_max=25,
        check_interval=50,
    )
    res_small = opt_small.run(evaluator=evaluator, lb=lb, ub=ub, budget=500, rng=123)
    assert res_small.evaluations_used <= 500
    assert res_small.evaluations_used == 500
    assert opt_small.budget.evaluations == 500
    assert opt_small.budget.remaining == 0

    # 2. Uji pada anggaran penuh (5.000)
    opt_mid = KomodoMlipirOptimizer(
        phase_1_budget=1000,
        phase_2_budget=4000,
        phase_2_n_pop_init=50,
        check_interval=250,
    )
    res_mid = opt_mid.run(evaluator=evaluator, lb=lb, ub=ub, budget=5000, rng=456)
    assert res_mid.evaluations_used == 5000
    assert opt_mid.budget.evaluations == 5000
    assert opt_mid.budget.remaining == 0


def test_kma_seed_reproducibility() -> None:
    """Menguji reproduksibilitas: seed yang sama menghasilkan solusi yang identik bit-per-bit."""
    c = np.array([2.5, 1.2, 3.8, 0.9, 4.1, 1.7, 2.0])
    evaluator = MockLinearEvaluator(c)
    lb = np.array([0.05, 0.05, 0.10, 0.10, 0.05, 0.05, 0.05])
    ub = np.array([0.30, 0.25, 0.35, 0.25, 0.20, 0.20, 0.20])

    opt1 = KomodoMlipirOptimizer(
        phase_1_budget=200,
        phase_2_budget=800,
        phase_2_n_pop_init=30,
        check_interval=100,
    )
    res1 = opt1.run(evaluator=evaluator, lb=lb, ub=ub, budget=1000, rng=999)

    opt2 = KomodoMlipirOptimizer(
        phase_1_budget=200,
        phase_2_budget=800,
        phase_2_n_pop_init=30,
        check_interval=100,
    )
    res2 = opt2.run(evaluator=evaluator, lb=lb, ub=ub, budget=1000, rng=999)

    # Verifikasi identitas hasil
    assert np.allclose(res1.best_w, res2.best_w, atol=1e-14)
    assert res1.best_cost == pytest.approx(res2.best_cost, abs=1e-12)
    assert res1.evaluations_used == res2.evaluations_used
    assert len(res1.convergence_history) == len(res2.convergence_history)
    for h1, h2 in zip(res1.convergence_history, res2.convergence_history):
        assert h1["evaluation"] == h2["evaluation"]
        assert h1["best_cost"] == pytest.approx(h2["best_cost"], abs=1e-12)


def test_kma_solution_feasibility() -> None:
    """Menguji bahwa bobot solusi keluaran selalu memenuhi batas proporsi dan sum(w)=1 dalam 1e-8."""
    c = np.array([1.5, 2.3, 0.8, 3.1, 1.1, 2.7, 0.5])
    evaluator = MockLinearEvaluator(c)
    lb = LB_DJPPR
    ub = UB_DJPPR

    opt = KomodoMlipirOptimizer(
        phase_1_budget=300,
        phase_2_budget=1200,
        phase_2_n_pop_init=40,
        check_interval=150,
    )
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=1500, rng=777)

    # Kendala anggaran: sum(w) = 1 dalam toleransi 1e-8
    assert abs(np.sum(res.best_w) - 1.0) <= 1e-8

    # Batas box: lb <= w <= ub dalam toleransi 1e-8
    assert np.all(res.best_w >= lb - 1e-8)
    assert np.all(res.best_w <= ub + 1e-8)

    # Status kelayakan
    assert res.is_feasible is True
    assert res.v_J <= 1e-8
    assert res.v_R <= 1e-8


def test_kma_known_linear_optimum() -> None:
    """Menguji KMA pada masalah linear sintetis dengan solusi analitis yang dapat dihitung tangan.

    Setup analitis:
    dim = 7
    lb = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05] (sum = 0.35)
    ub = [0.40, 0.30, 0.20, 0.20, 0.20, 0.20, 0.20] (sum = 1.70)
    c = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]

    Solusi optimal analitis:
    Untuk meminimasi c^T w subject to sum(w)=1 dan lb <= w <= ub:
    Alokasikan bobot maksimum ke koefisien terendah:
    w[0]* = ub[0] = 0.40 (c[0] = 1.0)
    w[1]* = ub[1] = 0.30 (c[1] = 2.0)
    w[3..6]* = lb[3..6] = 0.05 (4 x 0.05 = 0.20)
    Sisa bobot untuk w[2]*: 1.0 - (0.40 + 0.30 + 0.20) = 0.10 (lb[2] <= 0.10 <= ub[2]).

    Vektor optimal:
    w* = [0.40, 0.30, 0.10, 0.05, 0.05, 0.05, 0.05]
    Cost optimal:
    c^T w* = 1(0.40) + 2(0.30) + 3(0.10) + 4(0.05) + 5(0.05) + 6(0.05) + 7(0.05)
           = 0.40 + 0.60 + 0.30 + 0.20 + 0.25 + 0.30 + 0.35 = 2.40.
    """
    c = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
    lb = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
    ub = np.array([0.40, 0.30, 0.20, 0.20, 0.20, 0.20, 0.20])
    w_star = np.array([0.40, 0.30, 0.10, 0.05, 0.05, 0.05, 0.05])
    optimum_cost = 2.40

    evaluator = MockLinearEvaluator(c)
    opt = KomodoMlipirOptimizer(
        phase_1_budget=1000,
        phase_2_budget=4000,
        phase_2_n_pop_init=50,
        check_interval=250,
    )
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=5000, rng=42)

    # KMA harus mendekati optimum global analitis (selisih biaya < 1% atau <= 2.42)
    assert res.best_cost >= optimum_cost - 1e-8  # Tidak mungkin lebih rendah dari batas teoritis
    assert res.best_cost <= optimum_cost + 0.03  # Toleransi 1.25% terhadap optimum
    assert np.allclose(res.best_w, w_star, atol=0.03)


def test_kma_smoke_replications(capsys: pytest.CaptureFixture) -> None:
    """Smoke test 3 replikasi KMA pada evaluator portofolio riil (gross_djppr, N=5.000).

    Memverifikasi:
    - 3 replikasi (seed 1, 2, 3) berjalan penuh dengan anggaran 25.000 evaluasi
    - Ketiga replikasi menghasilkan solusi layak (v_J <= 1e-8, v_R <= 1e-8)
    - Ketiga replikasi mencatat 100 entri log konvergensi
    - Melaporkan tabel performa (biaya, risiko, kelayakan, waktu eksekusi)
    """
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    if not bank_path.exists():
        pytest.skip(f"Bank skenario latih tidak ditemukan: {bank_path}")

    bank = np.load(bank_path)
    cost_matrix = bank["cost_gross"]

    evaluator = PortfolioEvaluator(cost_matrix=cost_matrix)
    base_metrics = evaluator.set_baseline(W0)
    w0_cost = base_metrics["mean_cost"]

    seeds = [1, 2, 3]
    replication_results = []

    print("\n" + "=" * 78)
    print("SMOKE TEST KMA 3 REPLIKASI (Bank Latih, N=5.000, Config: gross_djppr)")
    print(f"Baseline w0 Cost: {w0_cost:.8f} | tau: {evaluator.tau:.8f} | eta: {evaluator.eta:.8f}")
    print("-" * 78)
    print(f"{'Seed':<6}{'Best Cost':<16}{'CCaR':<14}{'J_MCCaR':<12}{'Feasible':<10}{'Time (s)':<10}")
    print("-" * 78)

    for s in seeds:
        opt = KomodoMlipirOptimizer()
        t0 = time.perf_counter()
        res = opt.run(
            evaluator=evaluator,
            lb=LB_DJPPR,
            ub=UB_DJPPR,
            budget=25000,
            rng=s,
        )
        elapsed = time.perf_counter() - t0

        replication_results.append(res)
        print(
            f"{s:<6}{res.best_cost:<16.8f}{res.ccar:<14.8f}{res.j_mccar:<12.8f}"
            f"{str(res.is_feasible):<10}{elapsed:<10.2f}"
        )

        # Verifikasi per replikasi
        assert res.evaluations_used == 25000
        assert res.is_feasible is True
        assert res.v_J <= 1e-8
        assert res.v_R <= 1e-8
        assert abs(np.sum(res.best_w) - 1.0) <= 1e-8
        assert np.all(res.best_w >= LB_DJPPR - 1e-8)
        assert np.all(res.best_w <= UB_DJPPR + 1e-8)
        assert len(res.convergence_history) == 100
        assert res.best_cost <= w0_cost  # Optimasi berhasil memperbaiki atau menyamai baseline

    print("=" * 78)
