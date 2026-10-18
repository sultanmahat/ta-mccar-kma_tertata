"""Unit test untuk evaluator risiko CCaR dan MCCaR.

Menguji:
1. Kasus sintetis kecil yang dihitung tangan (N=4, D=2, alpha=0.50, delta=0.10).
2. Sifat analitik: MC_i = delta * mean(C_i) persis, CCaR >= Cost_bar, CCaR^(+i) >= CCaR.
3. Pembagi J_MCCaR adalah n (bukan n - 1).
4. Penanganan pembagian nol D5 jika MC_i mendekati nol.
5. Kesamaan identik 100% antara evaluasi batch dan loop satu-per-satu.
"""

from pathlib import Path
import numpy as np
import pytest

from mccar_kma.risk.ccar import compute_ccar, compute_ccar_batch, compute_tail_count
from mccar_kma.risk.mccar import (
    compute_marginal_cost,
    compute_mccar,
    compute_theta,
    compute_j_mccar,
)
from mccar_kma.risk.evaluator import PortfolioEvaluator


def test_tail_count_exact_for_train_and_validation():
    """Uji ketepatan m skenario ekor (Persamaan 2.13, AUDIT-01 & AUDIT-03).
    
    Memastikan tidak ada floating-point ceil artifact:
    - N = 5.000, alpha = 0.95 -> m = 250 tepat (bukan 251)
    - N = 20.000, alpha = 0.95 -> m = 1.000 tepat (bukan 1.001)
    - N = 100, alpha = 0.95 -> m = 5 tepat
    - N = 5.001, alpha = 0.95 -> m = 251 tepat (karena ceil(250.05) = 251)
    """
    assert compute_tail_count(5000, alpha=0.95) == 250
    assert compute_tail_count(20000, alpha=0.95) == 1000
    assert compute_tail_count(100, alpha=0.95) == 5
    assert compute_tail_count(5001, alpha=0.95) == 251


def test_hand_calculated_synthetic_case():
    """Uji kasus sintetis kecil yang dihitung tangan sampai presisi penuh.

    Setup:
    - N = 4 skenario, D = 2 instrumen
    - alpha = 0.50 -> m = ceil(0.50 * 4) = 2 skenario ekor
    - delta = 0.10
    - C = [[1.0, 2.0],
           [3.0, 1.0],
           [2.0, 4.0],
           [4.0, 3.0]]
    - w = [0.6, 0.4]

    Hitungan Tangan:
    1. Cost_s = [0.6*1 + 0.4*2 = 1.4,
                 0.6*3 + 0.4*1 = 2.2,
                 0.6*2 + 0.4*4 = 2.8,
                 0.6*4 + 0.4*3 = 3.6]
       Cost_bar = (1.4 + 2.2 + 2.8 + 3.6) / 4 = 2.50
    2. Dua biaya tertinggi: 3.6 dan 2.8 -> CCaR = (3.6 + 2.8) / 2 = 3.20
    3. MC_i:
       mean(C[:, 0]) = (1 + 3 + 2 + 4) / 4 = 2.50 -> MC_0 = 0.1 * 2.50 = 0.25
       mean(C[:, 1]) = (2 + 1 + 4 + 3) / 4 = 2.50 -> MC_1 = 0.1 * 2.50 = 0.25
    4. Perturbasi instrumen 0:
       delta * C[:, 0] = [0.1, 0.3, 0.2, 0.4]
       Cost^{(+0)} = [1.5, 2.5, 3.0, 4.0]
       Dua tertinggi: 4.0 dan 3.0 -> CCaR^{(+0)} = (4.0 + 3.0) / 2 = 3.50
       MCCaR_0 = 3.50 - 3.20 = 0.30
       theta_0 = 0.30 / 0.25 = 1.20
    5. Perturbasi instrumen 1:
       delta * C[:, 1] = [0.2, 0.1, 0.4, 0.3]
       Cost^{(+1)} = [1.6, 2.3, 3.2, 3.9]
       Dua tertinggi: 3.9 dan 3.2 -> CCaR^{(+1)} = (3.9 + 3.2) / 2 = 3.55
       MCCaR_1 = 3.55 - 3.20 = 0.35
       theta_1 = 0.35 / 0.25 = 1.40
    6. theta_bar = (1.20 + 1.40) / 2 = 1.30
    7. J_MCCaR = sqrt( ((1.2 - 1.3)^2 + (1.4 - 1.3)^2) / 2 )
               = sqrt( (0.01 + 0.01) / 2 ) = sqrt(0.01) = 0.10
    """
    C = np.array([
        [1.0, 2.0],
        [3.0, 1.0],
        [2.0, 4.0],
        [4.0, 3.0],
    ])
    w = np.array([0.6, 0.4])
    alpha = 0.50
    delta = 0.10

    evaluator = PortfolioEvaluator(
        cost_matrix=C,
        alpha=alpha,
        delta=delta,
    )

    res = evaluator.evaluate(w, apply_penalty=False)

    assert np.isclose(res["mean_cost"], 2.50, atol=1e-12)
    assert np.isclose(res["ccar"], 3.20, atol=1e-12)
    np.testing.assert_allclose(res["mc"], [0.25, 0.25], atol=1e-12)
    np.testing.assert_allclose(res["mccar"], [0.30, 0.35], atol=1e-12)
    np.testing.assert_allclose(res["theta"], [1.20, 1.40], atol=1e-12)
    assert np.isclose(res["theta_bar"], 1.30, atol=1e-12)
    assert np.isclose(res["j_mccar"], 0.10, atol=1e-12)


def test_j_mccar_uses_n_denominator():
    """Uji spesifikasi §5: pembagi J_MCCaR adalah n, bukan n-1."""
    theta = np.array([1.0, 2.0, 3.0, 4.0])
    n = len(theta)  # 4
    theta_bar = np.mean(theta)  # 2.5

    # Formula proposal: pembagi n
    expected_j = np.sqrt(np.mean((theta - theta_bar) ** 2))
    computed_j = compute_j_mccar(theta)

    assert np.isclose(computed_j, expected_j, atol=1e-12)
    # Pembagi n-1 akan menghasilkan nilai lebih besar (akar 5/3 vs akar 5/4)
    sample_j = np.std(theta, ddof=1)
    assert computed_j < sample_j


def test_d5_zero_division_guard():
    """Uji keputusan D5: jika MC_i mendekati nol, theta_i di-set 0.0 tanpa error."""
    mccar = np.array([0.05, 0.10])
    mc_with_zero = np.array([0.05, 1e-14])  # instrumen kedua MC mendekati 0

    theta, theta_bar = compute_theta(mccar, mc_with_zero, zero_tol=1e-12)

    assert np.isclose(theta[0], 0.05 / 0.05, atol=1e-12)
    assert theta[1] == 0.0  # D5 guard aktif
    assert np.isclose(theta_bar, (1.0 + 0.0) / 2.0, atol=1e-12)


def test_analytical_identities_on_bank():
    """Uji sifat analitik pada bank skenario riil (bank_train_seed42_N5000.npz)."""
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    if not bank_path.exists():
        pytest.skip("Bank skenario riil belum ada.")

    evaluator = PortfolioEvaluator.from_scenario_bank(bank_path, cost_def="gross")

    # 1. Sifat MC_i = delta * mean(C_i) konstan
    # Hitung MC_i langsung dari rata-rata C
    expected_mc = 0.01 * np.mean(evaluator.C, axis=0)
    np.testing.assert_allclose(evaluator.mc, expected_mc, atol=1e-14)

    # 2. CCaR >= Cost_bar untuk berbagai portofolio
    rng = np.random.default_rng(42)
    for _ in range(20):
        w = rng.uniform(0.01, 1.0, 7)
        w = w / np.sum(w)
        res = evaluator.evaluate(w, apply_penalty=False)
        assert res["ccar"] >= res["mean_cost"] - 1e-12

    # 3. CCaR^(+i) >= CCaR karena delta * C > 0
    w0 = np.array([0.4595, 0.1136, 0.1478, 0.1439, 0.0244, 0.0667, 0.0441])
    res_w0 = evaluator.evaluate(w0, apply_penalty=False)
    # MCCaR = CCaR^(+i) - CCaR harus >= 0
    assert np.all(res_w0["mccar"] >= -1e-12)


def test_batch_vs_single_equivalence():
    """Uji kesamaan identik 100% antara evaluate_batch dan loop evaluate."""
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    if not bank_path.exists():
        # Gunakan data sintetis jika file belum ada
        rng_dummy = np.random.default_rng(99)
        C = rng_dummy.uniform(0.9, 1.2, (500, 7))
        evaluator = PortfolioEvaluator(cost_matrix=C, tau=1.05, eta=0.05)
    else:
        evaluator = PortfolioEvaluator.from_scenario_bank(
            bank_path, cost_def="gross", tau=1.085986, eta=0.068115
        )

    rng = np.random.default_rng(99)
    P = 25
    W = rng.uniform(0.05, 0.3, (P, 7))
    W = W / np.sum(W, axis=1, keepdims=True)

    # Evaluasi batch
    batch_res = evaluator.evaluate_batch(W, apply_penalty=True)

    # Evaluasi satu-per-satu
    for p in range(P):
        single_res = evaluator.evaluate(W[p], apply_penalty=True)
        assert np.isclose(batch_res["mean_cost"][p], single_res["mean_cost"], atol=1e-12)
        assert np.isclose(batch_res["ccar"][p], single_res["ccar"], atol=1e-12)
        np.testing.assert_allclose(batch_res["mccar"][p], single_res["mccar"], atol=1e-12)
        np.testing.assert_allclose(batch_res["theta"][p], single_res["theta"], atol=1e-12)
        assert np.isclose(batch_res["j_mccar"][p], single_res["j_mccar"], atol=1e-12)
        assert np.isclose(batch_res["v_J"][p], single_res["v_J"], atol=1e-12)
        assert np.isclose(batch_res["v_R"][p], single_res["v_R"], atol=1e-12)
        assert np.isclose(batch_res["f_val"][p], single_res["f_val"], atol=1e-12)
        assert batch_res["is_feasible"][p] == single_res["is_feasible"]
