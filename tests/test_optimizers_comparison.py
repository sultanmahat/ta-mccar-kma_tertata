"""Smoke Test Komparasi Awal 3 Replikasi: KMA vs GA vs PSO.

Menjalankan 3 replikasi (seed 1, 2, 3) untuk ketiga algoritma metaheuristik:
1. Komodo Mlipir Algorithm (KMA)
2. Genetic Algorithm (GA)
3. Particle Swarm Optimization (PSO)

pada konfigurasi evaluasi riil:
- Bank latih N = 5.000 skenario
- Konfigurasi: gross_djppr (biaya bruto, batas DJPPR)
- Anggaran: 25.000 evaluasi fungsi per run

Menampilkan tabel komparasi awal biaya terbaik layak dan waktu komputasi.
"""

from pathlib import Path
import time
import numpy as np
import pytest

from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, W0
from mccar_kma.risk.evaluator import PortfolioEvaluator


def test_optimizers_smoke_comparison() -> None:
    """Menjalankan 3 replikasi komparasi KMA vs GA vs PSO dan menampilkan tabel ringkasan."""
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    if not bank_path.exists():
        pytest.skip(f"Bank skenario latih tidak ditemukan: {bank_path}")

    bank = np.load(bank_path)
    cost_matrix = bank["cost_gross"]

    evaluator = PortfolioEvaluator(cost_matrix=cost_matrix)
    base_metrics = evaluator.set_baseline(W0)
    w0_cost = base_metrics["mean_cost"]

    seeds = [1, 2, 3]
    algorithms = [
        ("KMA", KomodoMlipirOptimizer),
        ("GA", GeneticAlgorithmOptimizer),
        ("PSO", ParticleSwarmOptimizer),
    ]

    print("\n" + "=" * 88)
    print("SMOKE TEST KOMPARASI AWAL METAHEURISTIK (3 Replikasi, Bank Latih, N=5.000, gross_djppr)")
    print(f"Baseline w0: Cost = {w0_cost:.8f} | tau = {evaluator.tau:.8f} | eta = {evaluator.eta:.8f}")
    print("-" * 88)
    print(
        f"{'Algoritma':<10}{'Seed':<6}{'Best Cost':<16}{'CCaR':<14}{'J_MCCaR':<12}"
        f"{'Feasible':<10}{'Time (s)':<10}"
    )
    print("-" * 88)

    all_results = {}

    for algo_name, algo_cls in algorithms:
        all_results[algo_name] = []
        for s in seeds:
            opt = algo_cls()
            t0 = time.perf_counter()
            res = opt.run(
                evaluator=evaluator,
                lb=LB_DJPPR,
                ub=UB_DJPPR,
                budget=25000,
                rng=s,
            )
            elapsed = time.perf_counter() - t0

            all_results[algo_name].append(res)
            print(
                f"{algo_name:<10}{s:<6}{res.best_cost:<16.8f}{res.ccar:<14.8f}{res.j_mccar:<12.8f}"
                f"{str(res.is_feasible):<10}{elapsed:<10.2f}"
            )

            # Verifikasi ketat per run
            assert res.evaluations_used == 25000
            assert res.is_feasible is True
            assert res.v_J <= 1e-8
            assert res.v_R <= 1e-8
            assert abs(np.sum(res.best_w) - 1.0) <= 1e-8
            assert np.all(res.best_w >= LB_DJPPR - 1e-8)
            assert np.all(res.best_w <= UB_DJPPR + 1e-8)
            assert len(res.convergence_history) == 100
            assert res.best_cost <= w0_cost + 1e-6

    print("=" * 88)

    # Ringkasan rata-rata per algoritma
    print("\nRINGKASAN RATA-RATA 3 REPLIKASI:")
    print("-" * 65)
    print(f"{'Algoritma':<12}{'Mean Cost':<16}{'Min Cost':<16}{'Mean Time (s)':<14}")
    print("-" * 65)
    for algo_name in ["KMA", "GA", "PSO"]:
        costs = [r.best_cost for r in all_results[algo_name]]
        times = [r.elapsed_seconds for r in all_results[algo_name]]
        print(
            f"{algo_name:<12}{np.mean(costs):<16.8f}{np.min(costs):<16.8f}"
            f"{np.mean(times):<14.2f}"
        )
    print("-" * 65)
