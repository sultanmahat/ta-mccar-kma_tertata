"""Tes sifat matematis modul signifikansi praktis (Tahap 19-20)."""

import numpy as np
import pytest

from mccar_kma.analysis import practical_significance as ps


def test_hl_estimator_matches_known_shift():
    rng = np.random.default_rng(0)
    x = rng.normal(5.0, 1.0, size=200)
    y = x - 2.0  # selisih konstan diketahui = 2.0
    assert ps.hodges_lehmann_estimator(x, y) == pytest.approx(2.0, abs=1e-9)


def test_hl_estimator_symmetric_antisymmetric():
    rng = np.random.default_rng(1)
    x = rng.normal(0.0, 1.0, size=50)
    y = rng.normal(0.0, 1.0, size=60)
    assert ps.hodges_lehmann_estimator(x, y) == pytest.approx(-ps.hodges_lehmann_estimator(y, x))


def test_bootstrap_hl_ci_contains_point_estimate_and_is_deterministic():
    rng = np.random.default_rng(2)
    x = rng.normal(10.0, 0.5, size=30)
    y = rng.normal(9.0, 0.5, size=30)
    point = ps.hodges_lehmann_estimator(x, y)
    ci_a = ps.bootstrap_hl_ci(x, y, resamples=2000, seed=7, level=0.95)
    ci_b = ps.bootstrap_hl_ci(x, y, resamples=2000, seed=7, level=0.95)
    assert ci_a == ci_b
    assert ci_a[0] <= point <= ci_a[1]


def test_median_diff_pct_basic():
    x = [10.0, 10.0, 10.0]
    y = [8.0, 8.0, 8.0]
    r = ps.median_diff_pct(x, y)
    assert r["diff_abs"] == pytest.approx(2.0)
    assert r["diff_pct"] == pytest.approx(25.0)


def test_tost_equivalent_for_identical_distributions():
    rng = np.random.default_rng(3)
    x = rng.normal(0.0, 0.01, size=100)
    y = rng.normal(0.0, 0.01, size=100)
    res = ps.equivalence_test_tost(x, y, margin=1.0, alpha=0.05)
    assert res["is_equivalent"] is True


def test_tost_not_equivalent_for_large_separation():
    rng = np.random.default_rng(4)
    x = rng.normal(100.0, 0.1, size=50)
    y = rng.normal(0.0, 0.1, size=50)
    res = ps.equivalence_test_tost(x, y, margin=0.01, alpha=0.05)
    assert res["is_equivalent"] is False


def test_equivalence_via_ci():
    assert ps.equivalence_via_ci(0.0, (-0.5, 0.5), margin=1.0) is True
    assert ps.equivalence_via_ci(0.0, (-2.0, 2.0), margin=1.0) is False


def test_constraint_activity_flags():
    # Aktif: slack kecil relatif terhadap batas
    r = ps.constraint_activity_flags(j_mccar=0.0999, eta=0.1, ccar=5.0, tau=10.0, rel_tol=1e-2)
    assert r["j_active"] is True
    assert r["r_active"] is False
    # Tidak aktif: slack besar
    r2 = ps.constraint_activity_flags(j_mccar=0.05, eta=0.1, ccar=1.0, tau=10.0, rel_tol=1e-2)
    assert r2["j_active"] is False
    assert r2["r_active"] is False


def test_box_vertex_flags_all_at_bound_vs_interior():
    lb = np.array([0.0, 0.0, 0.0])
    ub = np.array([1.0, 1.0, 1.0])
    w_vertex = np.array([0.0, 1.0, 0.5])  # 2 dari 3 di batas (lb & ub), 1 di interior (n-1)
    w_interior = np.array([0.3, 0.3, 0.4])  # tidak ada yang di batas
    r_vertex = ps.box_vertex_flags(w_vertex, lb, ub, bound_tol=1e-6)
    r_interior = ps.box_vertex_flags(w_interior, lb, ub, bound_tol=1e-6)
    assert r_vertex["is_lp_vertex"] is True
    assert r_vertex["n_bound_active"] == 2
    assert r_interior["is_lp_vertex"] is False
    assert r_interior["n_bound_active"] == 0


def test_lp_vertex_feasible_matches_interest_djppr_example():
    # Contoh nyata: results/runs/interest_djppr/pso/rep_01_seed43.json
    lb = np.array([0.425, 0.100, 0.130, 0.130, 0.015, 0.050, 0.030])
    ub = np.array([0.490, 0.125, 0.165, 0.155, 0.030, 0.085, 0.055])
    w = np.array([0.445, 0.100, 0.130, 0.155, 0.030, 0.085, 0.055])
    r = ps.lp_vertex_feasible(
        w, lb, ub, bound_tol=1e-4,
        j_mccar=0.15992898960783142, eta=0.174187839957078,
        ccar=0.06343748027512724, tau=0.06496905837185826,
        rel_tol=1e-3,
    )
    assert r["n_bound_active"] == 6
    assert r["is_lp_vertex"] is True
    assert r["j_active"] is False
    assert r["r_active"] is False
    assert r["lp_feasible"] is True


def test_contingency_exact_matches_fisher_reference_28_30_vs_30_30():
    # Premis instruksi: interest_free PSO 28/30 vs KMA 30/30, p approx 0.49
    table = [[28, 2], [30, 0]]
    r = ps.contingency_exact_test(table)
    assert r["p_fisher"] == pytest.approx(0.4918, abs=5e-3)
    assert 0.0 <= r["p_barnard"] <= 1.0


def test_contingency_exact_identical_tables_p_is_one():
    table = [[30, 0], [30, 0]]
    r = ps.contingency_exact_test(table)
    assert r["p_fisher"] == pytest.approx(1.0)
