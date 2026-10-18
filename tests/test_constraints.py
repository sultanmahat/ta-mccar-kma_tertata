"""Unit test untuk model kendala, proyeksi bobot, penalti, budget counter, dan arsip.

Menguji:
1. Konvergensi proyeksi bobot pada 10.000 titik acak untuk batas 'free' dan 'djppr'.
2. Kesamaan proyeksi batch vs looping satu-per-satu.
3. Kelayakan titik awal w0 secara analitis (v_J = 0, v_R = 0, f = Cost_bar).
4. Kepatuhan fungsi penalti kuadratik (Persamaan 2.24).
5. Kepatuhan pembatasan anggaran BudgetCounter (maksimum 25.000).
6. Integritas FeasibleArchive (hanya menyimpan solusi layak berbiaya terendah).
"""

import numpy as np
import pytest

from mccar_kma.model.constraints import (
    project_weights,
    project_weights_batch,
    check_weight_feasibility,
    compute_relative_violations,
    compute_relative_violations_batch,
)
from mccar_kma.model.penalty import (
    compute_penalized_fitness,
    compute_penalized_fitness_batch,
    BudgetCounter,
    FeasibleArchive,
)

# Batas DJPPR (Tabel 2.1 & 2.2 spesifikasi)
LB_DJPPR = np.array([0.425, 0.100, 0.130, 0.130, 0.015, 0.050, 0.030])
UB_DJPPR = np.array([0.490, 0.125, 0.165, 0.155, 0.030, 0.085, 0.055])
W0 = np.array([0.459485835, 0.113620854, 0.147798763, 0.143927407, 0.024401992, 0.066688212, 0.044076937])

# Batas Free
LB_FREE = np.zeros(7)
UB_FREE = np.ones(7)


def test_projection_10000_random_points_djppr():
    """Uji proyeksi pada 10.000 titik acak dalam rentang [-2, 2]^7 untuk batas DJPPR."""
    rng = np.random.default_rng(12345)
    n_points = 10000
    random_points = rng.uniform(-2.0, 2.0, (n_points, 7))

    for p in random_points:
        pw = project_weights(p, LB_DJPPR, UB_DJPPR, eps_tol=1e-8)
        assert abs(np.sum(pw) - 1.0) <= 1e-8, "Jumlah bobot harus 1.0 dalam toleransi 1e-8"
        assert np.all(pw >= LB_DJPPR - 1e-8), "Bobot harus >= lb"
        assert np.all(pw <= UB_DJPPR + 1e-8), "Bobot harus <= ub"


def test_projection_10000_random_points_free():
    """Uji proyeksi pada 10.000 titik acak dalam rentang [-2, 2]^7 untuk batas Free."""
    rng = np.random.default_rng(54321)
    n_points = 10000
    random_points = rng.uniform(-2.0, 2.0, (n_points, 7))

    for p in random_points:
        pw = project_weights(p, LB_FREE, UB_FREE, eps_tol=1e-8)
        assert abs(np.sum(pw) - 1.0) <= 1e-8, "Jumlah bobot harus 1.0 dalam toleransi 1e-8"
        assert np.all(pw >= LB_FREE - 1e-8), "Bobot harus >= 0"
        assert np.all(pw <= UB_FREE + 1e-8), "Bobot harus <= 1"


def test_batch_projection_equivalence():
    """Uji kesamaan identik proyeksi batch W (P, 7) vs looping satu-per-satu."""
    rng = np.random.default_rng(999)
    P = 100
    W = rng.uniform(-1.5, 1.5, (P, 7))

    batch_djppr = project_weights_batch(W, LB_DJPPR, UB_DJPPR)
    batch_free = project_weights_batch(W, LB_FREE, UB_FREE)

    for p in range(P):
        single_djppr = project_weights(W[p], LB_DJPPR, UB_DJPPR)
        single_free = project_weights(W[p], LB_FREE, UB_FREE)
        np.testing.assert_allclose(batch_djppr[p], single_djppr, atol=1e-8)
        np.testing.assert_allclose(batch_free[p], single_free, atol=1e-8)


def test_w0_feasibility():
    """Uji bahwa bobot eksisting w0 layak by construction pada batas free dan djppr."""
    assert check_weight_feasibility(W0, LB_DJPPR, UB_DJPPR, eps_tol=1e-8)
    assert check_weight_feasibility(W0, LB_FREE, UB_FREE, eps_tol=1e-8)

    # Pada titik acuan w0, J = eta dan CCaR = tau
    tau = 1.085986
    eta = 0.068115
    v_J, v_R = compute_relative_violations(j_mccar=eta, ccar=tau, eta=eta, tau=tau)
    assert v_J == 0.0
    assert v_R == 0.0

    mean_cost_w0 = 1.042370
    f_w0 = compute_penalized_fitness(mean_cost_w0, v_J, v_R)
    assert f_w0 == mean_cost_w0  # Penalti nol


def test_penalty_function_behavior():
    """Uji penalti kuadratik Persamaan 2.24: nol untuk layak, positif kuadratik untuk melanggar."""
    mean_cost = 1.020000

    # Kasus 1: Layak (v_J = 0, v_R = 0)
    f_feas = compute_penalized_fitness(mean_cost, v_J=0.0, v_R=0.0)
    assert f_feas == mean_cost

    # Kasus 2: Melanggar kendala (v_J = 0.01, v_R = 0.02)
    # Penalti = 1e6 * (0.01^2) + 1e6 * (0.02^2) = 1e6 * 0.0001 + 1e6 * 0.0004 = 100 + 400 = 500
    f_infeas = compute_penalized_fitness(mean_cost, v_J=0.01, v_R=0.02, rho_J=1e6, rho_R=1e6)
    expected_f = mean_cost + 500.0
    assert np.isclose(f_infeas, expected_f, atol=1e-12)


def test_budget_counter():
    """Uji pelacak anggaran evaluasi fungsi BudgetCounter."""
    counter = BudgetCounter(max_evaluations=25000)

    assert counter.evaluations == 0
    assert counter.remaining == 25000
    assert not counter.is_exhausted

    # Konsumsi bertahap
    consumed = counter.consume(1000)
    assert consumed == 1000
    assert counter.evaluations == 1000
    assert counter.remaining == 24000

    # Konsumsi sampai mendekati batas
    counter.consume(23900)
    assert counter.evaluations == 24900
    assert counter.remaining == 100

    # Mencoba konsumsi melebihi sisa (minta 200 saat tersisa 100)
    consumed_last = counter.consume(200)
    assert consumed_last == 100  # Hanya mengizinkan 100
    assert counter.evaluations == 25000
    assert counter.remaining == 0
    assert counter.is_exhausted

    # Konsumsi setelah habis
    assert counter.consume(50) == 0


def test_feasible_archive():
    """Uji integritas FeasibleArchive: hanya menyimpan solusi layak berbiaya terendah."""
    archive = FeasibleArchive(eps_tol=1e-8)
    assert archive.is_empty

    w_dummy = np.ones(7) / 7.0

    # 1. Kandidat tidak layak (v_J = 0.05 > 1e-8) harus ditolak
    accepted = archive.update(w=w_dummy, mean_cost=0.90, ccar=1.20, j_mccar=0.10, v_J=0.05, v_R=0.0)
    assert not accepted
    assert archive.is_empty
    assert archive.total_feasible_count == 0

    # 2. Kandidat layak pertama (mean_cost = 1.05) diterima
    accepted = archive.update(w=w_dummy, mean_cost=1.05, ccar=1.08, j_mccar=0.06, v_J=0.0, v_R=0.0)
    assert accepted
    assert not archive.is_empty
    assert archive.best_solution.mean_cost == 1.05
    assert archive.total_feasible_count == 1

    # 3. Kandidat layak kedua yang lebih buruk (mean_cost = 1.06) ditolak dari best_solution
    accepted = archive.update(w=w_dummy, mean_cost=1.06, ccar=1.07, j_mccar=0.05, v_J=0.0, v_R=0.0)
    assert not accepted
    assert archive.best_solution.mean_cost == 1.05  # Tetap 1.05
    assert archive.total_feasible_count == 2       # Namun counter bertambah

    # 4. Kandidat layak ketiga yang lebih baik (mean_cost = 1.03) diterima
    accepted = archive.update(w=w_dummy, mean_cost=1.03, ccar=1.07, j_mccar=0.05, v_J=0.0, v_R=0.0)
    assert accepted
    assert archive.best_solution.mean_cost == 1.03
    assert archive.total_feasible_count == 3
