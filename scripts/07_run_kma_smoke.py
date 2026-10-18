"""Skrip Demonstrasi dan Smoke Test Mandiri Algoritma Komodo Mlipir (Tahap 07).

Menjalankan Komodo Mlipir Algorithm (KMA) dua fase sesuai Algoritma 1 dan Persamaan 2.25–2.32:
- Fase 1: n_pop = 5, d = (D-1)/D = 6/7, anggaran 5.000 evaluasi
- Fase 2: n_pop adaptif (20..200), sisa anggaran 20.000 evaluasi
- Big males, Female mating/parthenogenesis, Small males mlipir
- Menampilkan tabel hasil replikasi, perbandingan bobot terhadap eksisting, dan status kelayakan.
"""

import argparse
import json
from pathlib import Path
import time
import numpy as np

from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, LB_FREE, UB_FREE, W0
from mccar_kma.risk.evaluator import PortfolioEvaluator

INSTRUMENT_NAMES = [
    "USD_Fixed_5Y",
    "USD_Fixed_10Y",
    "USD_Fixed_30Y",
    "EUR_Fixed_7Y",
    "EUR_Fixed_10Y",
    "JPY_Fixed_5Y",
    "JPY_Fixed_10Y",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Demo & Smoke Test Mandiri Komodo Mlipir Algorithm (KMA)"
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
        help="Jumlah replikasi yang dijalankan (default: 3)",
    )
    parser.add_argument(
        "--budget",
        type=int,
        default=25000,
        help="Anggaran evaluasi fungsi per replikasi (default: 25.000)",
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

    # Muat data bank dan batas
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

    print("\n" + "=" * 90)
    print(f"DEMO MANDIRI TAHAP 07: KOMODO MLIPIR ALGORITHM (KMA) DUA FASE")
    print("=" * 90)
    print(f"Konfigurasi       : {args.config} (Biaya: {cost_def.upper()}, Batas: {constr_type.upper()})")
    print(f"Anggaran Evaluasi : {args.budget:,} per replikasi")
    print(f"Batas Risiko Acuan: tau = {tau:.8f} | eta = {eta:.8f}")
    print(f"Baseline w0       : Cost = {base_eval['mean_cost']:.8f} | CCaR = {base_eval['ccar']:.8f} | J = {base_eval['j_mccar']:.8f}")
    print("-" * 90)
    print(
        f"{'Rep':<6}{'Seed':<8}{'Best Cost':<16}{'CCaR':<14}{'J_MCCaR':<12}"
        f"{'Feasible':<10}{'Evaluasi':<10}{'Waktu (s)':<10}"
    )
    print("-" * 90)

    results = []
    best_sol_overall = None
    best_cost_overall = float("inf")

    for k in range(1, args.reps + 1):
        run_seed = args.seed + k
        kma = KomodoMlipirOptimizer()
        t0 = time.perf_counter()
        res = kma.run(
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
            f"{k:<6}{run_seed:<8}{final_eval['mean_cost']:<16.8f}{final_eval['ccar']:<14.8f}"
            f"{final_eval['j_mccar']:<12.8f}{str(is_feasible):<10}{res.evaluations_used:<10}"
            f"{t_elapsed:<10.2f}"
        )

        results.append({
            "rep": k,
            "seed": run_seed,
            "cost": final_eval["mean_cost"],
            "ccar": final_eval["ccar"],
            "j": final_eval["j_mccar"],
            "feasible": is_feasible,
            "time": t_elapsed,
            "w": res.best_w,
        })

        if is_feasible and final_eval["mean_cost"] < best_cost_overall:
            best_cost_overall = final_eval["mean_cost"]
            best_sol_overall = res.best_w

    costs = [r["cost"] for r in results]
    times = [r["time"] for r in results]

    print("-" * 90)
    print("RINGKASAN REPLIKASI KMA:")
    print(f"Rata-rata Biaya  : {np.mean(costs):.8f}")
    print(f"Biaya Terbaik    : {np.min(costs):.8f} (Penghematan: {(base_eval['mean_cost'] - np.min(costs)):.8f})")
    print(f"Rata-rata Waktu  : {np.mean(times):.2f} detik")
    print("=" * 90)

    if best_sol_overall is not None:
        print("\nPERBANDINGAN BOBOT TERBAIK KMA VS EKSISTING (w0):")
        print("-" * 65)
        print(f"{'Instrumen':<18}{'w0 (Eksisting)':<18}{'w* (KMA)':<18}{'Selisih':<12}")
        print("-" * 65)
        for i, name in enumerate(INSTRUMENT_NAMES):
            diff = best_sol_overall[i] - W0[i]
            sign = "+" if diff >= 0 else ""
            print(f"{name:<18}{W0[i]:<18.6f}{best_sol_overall[i]:<18.6f}{sign}{diff:.6f}")
        print("-" * 65)
        print(f"{'TOTAL':<18}{np.sum(W0):<18.6f}{np.sum(best_sol_overall):<18.6f}")
        print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
