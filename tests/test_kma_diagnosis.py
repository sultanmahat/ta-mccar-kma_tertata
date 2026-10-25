"""Tes sifat matematis modul diagnosis KMA (Tahap 18)."""

from pathlib import Path

import numpy as np
import pytest

import mccar_kma.optimizers.base as base_mod
import mccar_kma.optimizers.pso as pso_mod
from mccar_kma.analysis import kma_diagnosis as kd
from mccar_kma.model.constraints import LB_DJPPR, LB_FREE, UB_DJPPR, UB_FREE
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator

BASE_DIR = Path(__file__).resolve().parent.parent
BENCH_CFG = {"shift_seed_base": 41000, "shift_domain_fraction": 0.8}


def _small_portfolio_evaluator():
    rng = np.random.default_rng(7)
    C = 1.0 + 0.05 * rng.standard_normal((400, 7))
    ev = PortfolioEvaluator(cost_matrix=C)
    w0 = np.array([0.459485835, 0.113620854, 0.147798763, 0.143927407, 0.024401992, 0.066688212, 0.044076937])
    ev.set_baseline(w0)
    return ev


@pytest.mark.parametrize("fn", ["sphere", "rastrigin", "rosenbrock"])
@pytest.mark.parametrize("dim", [2, 7, 30])
def test_benchmark_optimum_is_zero(fn, dim):
    prob = kd.BenchmarkProblem(fn, dim)
    assert prob(prob.optimum()) == pytest.approx(0.0, abs=1e-12)
    lo, hi = {"sphere": (-100, 100), "rastrigin": (-5.12, 5.12), "rosenbrock": (-30, 30)}[fn]
    shift = kd.make_shift(fn, dim, lo, hi, BENCH_CFG)
    sp = kd.BenchmarkProblem(fn, dim, shift)
    assert sp(sp.optimum()) == pytest.approx(0.0, abs=1e-12)
    assert np.all(shift >= 0.8 * lo) and np.all(shift <= 0.8 * hi)
    # Titik lain bernilai positif (optimum unik)
    assert sp(sp.optimum() + 0.1) > 0.0


def test_shift_is_deterministic_and_function_specific():
    a = kd.make_shift("sphere", 7, -100, 100, BENCH_CFG)
    b = kd.make_shift("sphere", 7, -100, 100, BENCH_CFG)
    c = kd.make_shift("rastrigin", 7, -100, 100, BENCH_CFG)
    np.testing.assert_array_equal(a, b)
    assert not np.allclose(a, c)


@pytest.mark.parametrize("budget", [300, 2600])
def test_variant_all_flags_off_bit_identical_benchmark(budget):
    lb, ub = np.full(7, -100.0), np.full(7, 100.0)
    ev = kd.BenchmarkEvaluator(kd.BenchmarkProblem("sphere", 7))
    with kd.box_only_projection():
        r_ref = KomodoMlipirOptimizer().run(ev, lb, ub, budget=budget, rng=123)
        r_var = kd.KMAVariant().run(ev, lb, ub, budget=budget, rng=123)
        r_ins = kd.KMAVariant(instrument=True).run(ev, lb, ub, budget=budget, rng=123)
    assert r_ref.best_fitness == r_var.best_fitness == r_ins.best_fitness
    np.testing.assert_array_equal(r_ref.best_w, r_var.best_w)
    np.testing.assert_array_equal(r_ref.best_w, r_ins.best_w)
    assert [h["best_cost"] for h in r_ref.convergence_history] == [h["best_cost"] for h in r_var.convergence_history]


@pytest.mark.parametrize("lb,ub", [(LB_FREE, UB_FREE), (LB_DJPPR, UB_DJPPR)])
def test_variant_all_flags_off_bit_identical_portfolio(lb, ub):
    ev = _small_portfolio_evaluator()
    r_ref = KomodoMlipirOptimizer().run(ev, lb, ub, budget=1500, rng=5)
    r_var = kd.KMAVariant(instrument=True).run(ev, lb, ub, budget=1500, rng=5)
    assert r_ref.best_cost == r_var.best_cost
    np.testing.assert_array_equal(r_ref.best_w, r_var.best_w)


def test_box_only_projection_restores_and_does_not_normalize():
    orig_b, orig_bb, orig_p = base_mod.project_weights, base_mod.project_weights_batch, pso_mod.project_weights
    w = np.array([0.5, 0.5, 0.5])
    with kd.box_only_projection():
        out = base_mod.project_weights(w, np.zeros(3), np.ones(3))
        assert out.sum() == pytest.approx(1.5)
        assert pso_mod.project_weights(np.array([2.0, -1.0]), np.zeros(2), np.ones(2)).tolist() == [1.0, 0.0]
    assert base_mod.project_weights is orig_b
    assert base_mod.project_weights_batch is orig_bb
    assert pso_mod.project_weights is orig_p


def test_paper_q_group_sizes():
    v = kd.KMAVariant(paper_q=True)
    assert v._group_sizes(200) == (100, 1, 99)
    assert v._group_sizes(5) == (2, 1, 2)
    assert kd.KMAVariant()._group_sizes(200) == (99, 1, 100)


def test_paper_mlipir_mask_selects_between_1_and_m_minus_1():
    v = kd.KMAVariant(paper_mlipir=True)
    rng = np.random.default_rng(0)
    for rate in (0.05, 0.5, 6 / 7, 0.99):
        for _ in range(500):
            k = int(v._paper_mlipir_mask(rng, 7, rate).sum())
            assert 1 <= k <= 6


def test_pool_selection_keeps_best_q_of_union():
    """Satu generasi dgn pool: Big Male hasil = q terbaik dari (lama ∪ baru)."""
    lb, ub = np.full(7, -100.0), np.full(7, 100.0)
    log_pool = []

    class Spy(kd.KMAVariant):
        def evaluate_candidate(self, w, evaluator):
            r = super().evaluate_candidate(w, evaluator)
            log_pool.append(r)
            return r

    ev = kd.BenchmarkEvaluator(kd.BenchmarkProblem("sphere", 7))
    opt = Spy(pool_selection=True)
    with kd.box_only_projection():
        opt._init_run(budget=10_000, lb=lb, ub=ub, rng=1)
        rng = np.random.default_rng(1)
        W = rng.uniform(lb, ub, size=(20, 7))
        res = opt.evaluate_population(W, ev)
        pop = [r["w"] for r in res]
        pop, res = opt._sort_population(pop, res)
        n_bm = opt._group_sizes(20)[0]
        old_bm_f = [r["f_val"] for r in res[:n_bm]]
        log_pool.clear()
        pop2, res2 = opt._evolve_generation(pop, res, 0.5, ub - lb, ev, rng)
    new_bm_f = [r["f_val"] for r in log_pool[:n_bm]]
    expected = sorted(old_bm_f + new_bm_f)[:n_bm]
    got = sorted(r["f_val"] for r in res2[:n_bm])
    # Big Male bertahan ada di antara n_bm teratas populasi akhir (female/small male boleh lebih baik)
    assert set(np.round(expected, 12)).issubset(set(np.round([r["f_val"] for r in res2], 12)))
    assert got[0] <= expected[0] + 1e-12


def test_deb_rules_prefers_feasible():
    v = kd.KMAVariant(deb_rules=True)
    feas = {"is_feasible": True, "mean_cost": 5.0, "f_val": 5.0, "v_J": 0.0, "v_R": 0.0}
    infeas = {"is_feasible": False, "mean_cost": 1.0, "f_val": 1.0, "v_J": 1e-9, "v_R": 0.0}
    assert v._better(feas, infeas)
    assert not kd.KMAVariant()._better(feas, infeas)


def test_recorder_counts_equal_budget_and_slack_definition():
    ev = _small_portfolio_evaluator()
    for algo in ("kma", "ga", "pso"):
        rec = kd.EvalRecorder(ev, bound_tol=1e-12)
        opt = kd.make_optimizer(algo, instrument=True)
        with kd.recording_projection(rec):
            res = opt.run(rec, LB_FREE, UB_FREE, budget=1000, rng=3)
        df = rec.to_frame()
        assert len(df) == res.evaluations_used == 1000
        assert not rec.queue and not rec.pending
        assert df["proj_dist"].notna().all()
        blocks = kd.summarize_eval_blocks(df, eta=ev.eta, eps_tol=1e-8, block_size=250, dist_tol=1e-9, near_rel=1e-3)
        assert blocks["n"].sum() == 1000
        assert ((blocks["frac_feasible"] >= 0) & (blocks["frac_feasible"] <= 1)).all()
        best = df[df["feasible"] > 0.5].nsmallest(1, "mean_cost").iloc[0]
        assert blocks["best_rel_slack_J"].iloc[-1] == pytest.approx((ev.eta - best["j_mccar"]) / ev.eta)


def test_recorder_does_not_change_optimizer_result():
    ev = _small_portfolio_evaluator()
    for algo in ("ga", "pso", "kma"):
        r_plain = kd.make_optimizer(algo).run(ev, LB_DJPPR, UB_DJPPR, budget=800, rng=11)
        rec = kd.EvalRecorder(ev, bound_tol=1e-12)
        with kd.recording_projection(rec):
            r_rec = kd.make_optimizer(algo, instrument=True).run(rec, LB_DJPPR, UB_DJPPR, budget=800, rng=11)
        np.testing.assert_array_equal(r_plain.best_w, r_rec.best_w)


def test_safe_output_dir_guard(tmp_path):
    with pytest.raises(ValueError):
        kd.assert_safe_output_dir(BASE_DIR / "results" / "runs", BASE_DIR)
    with pytest.raises(ValueError):
        kd.assert_safe_output_dir(BASE_DIR / "results" / "tables" / "x", BASE_DIR)
    kd.assert_safe_output_dir(BASE_DIR / "results" / "sensitivity" / "kma", BASE_DIR)


def test_timing_evaluator_marks_each_block():
    ev = _small_portfolio_evaluator()
    t = kd.TimingEvaluator(ev, block=250)
    kd.make_optimizer("pso").run(t, LB_FREE, UB_FREE, budget=1000, rng=0)
    assert [m[0] for m in t.marks] == [250, 500, 750, 1000]
    assert all(b[1] >= a[1] for a, b in zip(t.marks, t.marks[1:]))


def test_main_runs_slack_relative_definition():
    df, curves = kd.load_main_runs(BASE_DIR)
    if df.empty:
        pytest.skip("results/runs tidak tersedia")
    np.testing.assert_allclose(df["slack_J_rel"], (df["eta"] - df["j_mccar"]) / df["eta"])
    assert len(df) == 360
    assert all(c.shape == (30, 100) for c in curves.values())
