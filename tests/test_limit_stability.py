"""Tes sifat matematis modul studi stabilitas batas risiko (Tahap 17)."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from mccar_kma.analysis import limit_stability as ls

BASE_DIR = Path(__file__).resolve().parent.parent
BANK42 = BASE_DIR / "data" / "processed" / "bank_train_seed42_N5000.npz"


@pytest.fixture(scope="module")
def cfg():
    return ls.load_config(BASE_DIR / "configs" / "params.yaml")


def test_safe_output_dir_guard():
    with pytest.raises(ValueError):
        ls.assert_safe_output_dir(BASE_DIR / "results" / "runs", BASE_DIR)
    with pytest.raises(ValueError):
        ls.assert_safe_output_dir(BASE_DIR / "results" / "tables" / "x", BASE_DIR)
    ls.assert_safe_output_dir(BASE_DIR / "results" / "sensitivity" / "limits", BASE_DIR)


def test_study_seeds_disjoint_from_reserved_and_each_other(cfg):
    sl = cfg["sensitivity_limits"]
    ls.validate_study_seeds(int(sl["bank_seed_base"]), int(sl["n_banks"]), int(sl["optimizer_seed_base"]))
    with pytest.raises(ValueError):
        ls.validate_study_seeds(40, 5, 20000)  # memuat 42
    with pytest.raises(ValueError):
        ls.validate_study_seeds(10000, 20, 10010)  # seed optimizer = seed bank


def test_split_config_id():
    assert ls.split_config_id("interest_djppr") == ("interest", "djppr")
    assert ls.split_config_id("gross_free") == ("gross", "free")


def test_bootstrap_ci_deterministic_and_brackets_mean():
    x = np.random.default_rng(0).normal(5.0, 1.0, size=40)
    a = ls.bootstrap_mean_ci(x, 2000, 7, 0.95)
    b = ls.bootstrap_mean_ci(x, 2000, 7, 0.95)
    assert a == b
    assert a[0] < x.mean() < a[1]
    assert ls.bootstrap_mean_ci(np.full(10, 3.0), 500, 1, 0.95) == (3.0, 3.0)
    assert all(np.isnan(v) for v in ls.bootstrap_mean_ci([], 10, 1, 0.95))


def test_clopper_pearson_known_values():
    # k = 0: batas atas tertutup 1 - (alpha/2)^(1/n)
    lo, hi = ls.clopper_pearson(0, 10, 0.95)
    assert lo == 0.0
    assert hi == pytest.approx(1.0 - 0.025 ** (1 / 10), rel=1e-10)
    lo, hi = ls.clopper_pearson(10, 10, 0.95)
    assert hi == 1.0
    assert lo == pytest.approx(0.025 ** (1 / 10), rel=1e-10)
    lo, hi = ls.clopper_pearson(5, 20, 0.95)
    assert lo < 0.25 < hi


def test_win_tie_loss_counts_and_tolerance():
    a = [1.0, 2.0, 3.0, 1.0 + 1e-12]
    b = [2.0, 1.0, 3.0, 1.0]
    assert ls.win_tie_loss(a, b, 1e-8) == {"win": 1, "tie": 2, "loss": 1}
    assert ls.win_tie_loss(a, b, 0.0) == {"win": 1, "tie": 1, "loss": 2}


def test_wilcoxon_all_zero_is_nan():
    assert np.isnan(ls.wilcoxon_paired_p([1.0, 2.0], [1.0, 2.0]))
    p = ls.wilcoxon_paired_p(np.arange(12.0), np.arange(12.0) + 1.0)
    assert 0.0 < p < 0.01


def test_summarize_limits_statistics():
    df = pd.DataFrame({
        "cost_definition": ["gross"] * 4 + ["interest"] * 4,
        "eta": [1.0, 2.0, 3.0, 4.0, 10.0, 10.0, 12.0, 8.0],
        "tau": [2.0, 2.0, 2.0, 6.0, 1.0, 2.0, 3.0, 4.0],
    })
    ref = {"gross": {"eta": 2.5, "tau": 3.0}, "interest": {"eta": 10.0, "tau": 2.5}}
    true = {"gross": {"eta": 3.0, "tau": 2.0}, "interest": {"eta": 9.0, "tau": 1.0}}
    out = ls.summarize_limits(df, true, ref).set_index(["cost_definition", "metric"])
    r = out.loc[("gross", "eta")]
    sd = np.std([1, 2, 3, 4], ddof=1)
    assert r["mean"] == pytest.approx(2.5)
    assert r["cv_percent"] == pytest.approx(100 * sd / 2.5)
    assert r["bank42_z"] == pytest.approx(0.0)
    assert r["valid_bank_z"] == pytest.approx(0.5 / sd)
    assert r["bank42_percentile"] == pytest.approx(0.5)


@pytest.mark.skipif(not BANK42.exists(), reason="bank seed 42 tidak tersedia")
def test_bank42_limits_match_stored_reference(cfg):
    d = np.load(BANK42)
    lims = ls.compute_bank_limits({"cost_gross": d["cost_gross"], "cost_interest": d["cost_interest"]}, cfg)
    ref = ls.load_reference_limits(BASE_DIR)
    for cd in ls.COST_DEFINITIONS:
        for k in ("eta", "tau", "w0_cost"):
            assert lims[cd][k] == pytest.approx(ref[cd][k], rel=1e-12)
    assert ls.bank_matches_stored({"cost_gross": d["cost_gross"], "cost_interest": d["cost_interest"]}, BANK42)
    assert not ls.bank_matches_stored({"cost_gross": d["cost_gross"] * 1.0001, "cost_interest": d["cost_interest"]}, BANK42)
