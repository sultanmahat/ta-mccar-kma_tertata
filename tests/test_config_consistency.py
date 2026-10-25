"""Tes kesetaraan default kode vs configs/params.yaml (celah S1, audit_ulang_2026-10-25.md).

Sebelum refactor ini, tidak ada tes yang membandingkan default kelas optimizer atau
konstanta kode (LB/UB/W0) dengan params.yaml, dan runner.py membangun optimizer/evaluator
tanpa argumen dari config sama sekali -- yaml bisa diubah tanpa mempengaruhi hasil.
Tes di sini membuktikan: (1) default kelas == yaml (dokumentasi tidak menyimpang),
dan (2) jalur config -> konstruktor benar-benar hidup (bukan kebetulan default sama).
"""

from pathlib import Path
import numpy as np
import pytest

from mccar_kma.utils.config import load_config
from mccar_kma.model import constraints as cns
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.experiments.runner import build_optimizer

REPO_ROOT = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="module")
def cfg():
    return load_config(REPO_ROOT / "configs" / "params.yaml")


# ------------------------------------------------------------------------------
# 1. Default kelas == params.yaml
# ------------------------------------------------------------------------------

def test_kma_defaults_match_config(cfg):
    kcfg = cfg["algorithms"]["kma"]
    opt = KomodoMlipirOptimizer()
    assert opt.phase_1_n_pop == kcfg["phase_1"]["n_pop"]
    assert opt.phase_1_budget == kcfg["phase_1"]["budget"]
    assert opt.phase_2_n_pop_init == kcfg["phase_2"]["n_pop_init"]
    assert opt.phase_2_n_pop_min == kcfg["phase_2"]["n_pop_min"]
    assert opt.phase_2_n_pop_max == kcfg["phase_2"]["n_pop_max"]
    assert opt.phase_2_budget == kcfg["phase_2"]["budget"]
    assert opt.p_bm == kcfg["p_bm"]
    assert opt.gamma == kcfg["gamma"]
    assert opt.q_interactions == kcfg["q_interactions"]
    assert opt.p_mating == kcfg["p_mating"]
    assert opt.stagnation_patience == kcfg["stagnation_patience"]
    assert opt.stagnation_tol == kcfg["stagnation_tol"]
    assert opt.delta_n == kcfg["delta_n"]
    assert opt.phase_2_mlipir_rate == kcfg["phase_2"]["mlipir_rate"]
    assert opt.population_adapt_floor == kcfg["phase_2"]["population_adapt_floor"]


def test_ga_defaults_match_config(cfg):
    gcfg = cfg["algorithms"]["ga"]
    opt = GeneticAlgorithmOptimizer()
    assert opt.n_pop == gcfg["n_pop"]
    assert opt.tournament_size == gcfg["tournament_size"]
    assert opt.p_crossover == gcfg["p_crossover"]
    # Default kelas p_mutation=None berarti "hitung 1/D saat run()" (dim=7);
    # params.yaml mencatat nilai itu eksplisit (1/7) -- dua representasi perilaku yang sama.
    assert opt.p_mutation is None
    assert gcfg["p_mutation"] == pytest.approx(1.0 / 7.0)
    assert opt.sigma_m_factor == gcfg["sigma_m_factor"]
    assert opt.elitism_count == gcfg["elitism_count"]


def test_pso_defaults_match_config(cfg):
    pcfg = cfg["algorithms"]["pso"]
    opt = ParticleSwarmOptimizer()
    assert opt.n_pop == pcfg["n_pop"]
    assert opt.w_start == pcfg["w_start"]
    assert opt.w_end == pcfg["w_end"]
    assert opt.c1 == pcfg["c1"]
    assert opt.c2 == pcfg["c2"]
    assert opt.v_max_factor == pcfg["v_max_factor"]
    assert opt.velocity_clamp_strategy == pcfg["velocity_clamp_strategy"]


def test_evaluator_defaults_match_config(cfg):
    from mccar_kma.risk.evaluator import PortfolioEvaluator

    risk_cfg = cfg["risk"]
    opt_cfg = cfg["optimization"]
    dummy = np.zeros((10, 7))
    ev = PortfolioEvaluator(cost_matrix=dummy)
    assert ev.alpha == risk_cfg["alpha"]
    assert ev.delta == risk_cfg["delta"]
    assert ev.rho_J == opt_cfg["penalty_rho_J"]
    assert ev.rho_R == opt_cfg["penalty_rho_R"]
    assert ev.eps_tol == opt_cfg["eps_tol"]
    assert ev.zero_tol_mc == risk_cfg["zero_tolerance_mc"]


def test_constraints_bounds_match_config(cfg):
    items = cfg["instruments"]["items"]
    lb_cfg = np.array([float(it["lb"]) for it in items])
    ub_cfg = np.array([float(it["ub"]) for it in items])
    w0_cfg = np.array([float(it["w0"]) for it in items])
    np.testing.assert_array_equal(cns.LB_DJPPR, lb_cfg)
    np.testing.assert_array_equal(cns.UB_DJPPR, ub_cfg)
    np.testing.assert_array_equal(cns.W0, w0_cfg)
    np.testing.assert_array_equal(cns.LB_FREE, np.zeros(7))
    np.testing.assert_array_equal(cns.UB_FREE, np.ones(7))


# ------------------------------------------------------------------------------
# 2. Jalur config -> konstruktor benar-benar hidup (bukan kebetulan default sama)
# ------------------------------------------------------------------------------

def test_build_optimizer_reflects_config_override(cfg):
    """Mengubah params.yaml (di memori, tidak menulis file) harus mengubah atribut optimizer."""
    import copy

    cfg_mod = copy.deepcopy(cfg)
    cfg_mod["algorithms"]["kma"]["phase_2"]["mlipir_rate"] = 0.3
    cfg_mod["algorithms"]["kma"]["p_bm"] = 0.7
    opt_kma = build_optimizer("kma", cfg_mod)
    assert opt_kma.phase_2_mlipir_rate == 0.3
    assert opt_kma.p_bm == 0.7
    # nilai lain yang tidak diubah tetap mengikuti config_mod (sama dengan asli)
    assert opt_kma.gamma == cfg_mod["algorithms"]["kma"]["gamma"]

    cfg_mod["algorithms"]["ga"]["n_pop"] = 7
    opt_ga = build_optimizer("ga", cfg_mod)
    assert opt_ga.n_pop == 7

    cfg_mod["algorithms"]["pso"]["c1"] = 2.0
    opt_pso = build_optimizer("pso", cfg_mod)
    assert opt_pso.c1 == 2.0


def test_build_optimizer_defaults_identical_to_unmodified_config(cfg):
    """build_optimizer(cfg asli) harus identik dengan instansiasi default (status quo tidak berubah)."""
    opt_default = KomodoMlipirOptimizer()
    opt_from_cfg = build_optimizer("kma", cfg)
    assert opt_default.phase_2_mlipir_rate == opt_from_cfg.phase_2_mlipir_rate
    assert opt_default.p_bm == opt_from_cfg.p_bm
    assert opt_default.phase_1_n_pop == opt_from_cfg.phase_1_n_pop

    opt_default_ga = GeneticAlgorithmOptimizer()
    opt_from_cfg_ga = build_optimizer("ga", cfg)
    assert opt_default_ga.n_pop == opt_from_cfg_ga.n_pop
    # opt_default_ga.p_mutation == None (dihitung 1/D saat run()); opt_from_cfg_ga pakai
    # nilai eksplisit dari params.yaml (1/7) -- keduanya resolve ke perilaku yang sama untuk D=7.
    assert opt_default_ga.p_mutation is None
    assert opt_from_cfg_ga.p_mutation == pytest.approx(1.0 / 7.0)

    opt_default_pso = ParticleSwarmOptimizer()
    opt_from_cfg_pso = build_optimizer("pso", cfg)
    assert opt_default_pso.c1 == opt_from_cfg_pso.c1


def test_build_optimizer_unknown_algo_raises(cfg):
    with pytest.raises(ValueError):
        build_optimizer("tidak_ada", cfg)
