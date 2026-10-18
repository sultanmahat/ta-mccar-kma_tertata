"""Skrip Demonstrasi dan Perbandingan Komparatif Metaheuristik (Tahap 08).

Membandingkan performa 3 algoritma metaheuristik:
1. Komodo Mlipir Algorithm (KMA) - 2 fase adaptif
2. Genetic Algorithm (GA) - seleksi turnamen, crossover aritmetika, mutasi Gaussian
3. Particle Swarm Optimization (PSO) - inersia turun linear, clamping kecepatan efektif

Kriteria Keadilan Komparasi:
- Bank skenario identik
- Batas proporsi & batas risiko acuan (tau & eta) identik
- Anggaran evaluasi fungsi identik (default: 25.000 per run)
- Inisialisasi seed acak terkontrol dan seragam per replikasi
"""

import argparse
import json
from pathlib import Path
import time
import numpy as np

from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, LB_FREE, UB_FREE, W0
from mccar_kma.risk.evaluator import PortfolioEvaluator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demo Komparasi Metaheuristik: KMA vs GA vs PSO"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="gross_djppr",
        choices=["gross_djppr", "gross_free", "interest_djppr", "interest_free"],
        help="Konfigurasi biaya dan batas proporsi (default: gross_djppr)",
    )
    parser.add_argument(
        "--reps",
        type=int,
        default=3,
        help="Jumlah replikasi per algoritma (default: 3)",
    )
    parser.add_argument(
        "--budget",
        type=int,
        default=25000,
        help="Anggaran evaluasi fungsi per run (default: 25.000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Seed acuan (default: 42)",
    )
    parser.add_argument(
        "--bank",
        type=str,
        default="data/processed/bank_train_seed42_N5000.npz",
        help="Path file bank skenario latih",
    )
    parser.add_argument(
        "--limits",
        type=str,
        default="data/processed/risk_limits_bank_train_seed42_N5000.json",
        help="Path file batas risiko JSON",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cost_def, constr_type = args.config.split("_", 1)

    bank_path = Path(args.bank)
    limits_path = Path(args.limits)

    if not bank_path.exists():
        print(f"Error: Bank skenario tidak ditemukan di {bank_path}")
        return
    if not limits_path.exists():
        print(f"Error: Batas risiko tidak ditemukan di {limits_path}")
        return

    bank = np.load(bank_path)
    cost_matrix = bank[f"cost_{cost_def}"]

    with open(limits_path, "r", encoding="utf-8") as f:
        limits = json.load(f)

    tau = float(limits[cost_def]["tau"])
    eta = float(limits[cost_def]["eta"])

    lb = LB_DJPPR if constr_type == "djppr" else LB_FREE
    ub = UB_DJPPR if constr_type == "djppr" else UB_FREE

    evaluator = PortfolioEvaluator(cost_matrix=cost_matrix, tau=tau, eta=eta)
    base_eval = evaluator.evaluate(W0)

    algorithms = [
        ("KMA", KomodoMlipirOptimizer),
        ("GA", GeneticAlgorithmOptimizer),
        ("PSO", ParticleSwarmOptimizer),
    ]

    print("\n" + "=" * 90)
    print("DEMO MANDIRI TAHAP 08: KOMPARASI METAHEURISTIK (KMA vs GA vs PSO)")
    print("=" * 90)
    print(f"Konfigurasi       : {args.config} (Biaya: {cost_def.upper()}, Batas: {constr_type.upper()})")
    print(f"Anggaran Evaluasi : {args.budget:,} per run")
    print(f"Batas Risiko Acuan: tau = {tau:.8f} | eta = {eta:.8f}")
    print(f"Baseline w0       : Cost = {base_eval['mean_cost']:.8f}")
    print("-" * 90)
    print(
        f"{'Algoritma':<12}{'Rep':<6}{'Seed':<8}{'Best Cost':<16}{'CCaR':<14}"
        f"{'J_MCCaR':<12}{'Feasible':<10}{'Waktu (s)':<10}"
    )
    print("-" * 90)

    summary_data = {}

    for algo_name, algo_cls in algorithms:
        summary_data[algo_name] = []
        for k in range(1, args.reps + 1):
            run_seed = args.seed + k
            opt = algo_cls()
            t0 = time.perf_counter()
            res = opt.run(
                evaluator=evaluator,
                lb=lb,
                ub=ub,
                budget=args.budget,
                rng=run_seed,
            )
            t_elapsed = time.perf_counter() - t0

            final_eval = evaluator.evaluate(res.best_w)
            is_feasible = bool(res.is_feasible and final_eval["is_feasible"])

            print(
                f"{algo_name:<12}{k:<6}{run_seed:<8}{final_eval['mean_cost']:<16.8f}"
                f"{final_eval['ccar']:<14.8f}{final_eval['j_mccar']:<12.8f}"
                f"{str(is_feasible):<10}{t_elapsed:<10.2f}"
            )

            summary_data[algo_name].append({
                "cost": final_eval["mean_cost"],
                "feasible": is_feasible,
                "time": t_elapsed,
            })

    print("=" * 90)
    print("\nTABEL RINGKASAN KOMPARASI KINERJA:")
    print("-" * 75)
    print(
        f"{'Algoritma':<12}{'Rata-rata Biaya':<18}{'Biaya Terbaik':<18}"
        f"{'Rata-rata Waktu (s)':<22}{'Feasible (%)':<12}"
    )
    print("-" * 75)

    for algo_name in ["KMA", "GA", "PSO"]:
        runs = summary_data[algo_name]
        costs = [r["cost"] for r in runs]
        times = [r["time"] for r in runs]
        feas_pct = sum(1 for r in runs if r["feasible"]) / len(runs) * 100

        print(
            f"{algo_name:<12}{np.mean(costs):<18.8f}{np.min(costs):<18.8f}"
            f"{np.mean(times):<22.2f}{feas_pct:<12.1f}%"
        )
    print("=" * 75 + "\n")


if __name__ == "__main__":
    main()
