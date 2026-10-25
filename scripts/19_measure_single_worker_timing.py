"""Tahap 19: Pengukuran waktu komputasi bersih 1 proses (tanpa paralel).

Eksperimen utama (Tahap 10) diukur dengan beberapa worker paralel, sehingga
waktu per run terkontaminasi kontensi CPU antar proses. Skrip ini mengulang
3 algoritma x 4 konfigurasi x 5 replikasi (minimum) secara SEKUENSIAL (1
proses) pada bank dan batas risiko yang identik dengan eksperimen utama
(bank seed 42, N=5.000, batas eta/tau dari risk_limits_bank_train_seed42_N5000.json),
seed baru (tidak beririsan dengan seed proyek manapun).

Hanya untuk pengukuran waktu -- TIDAK menimpa results/tables/runs_summary.csv
atau results/runs/. Keluaran terpisah: results/tables/timing_single_worker_360.csv.
"""

from __future__ import annotations

import argparse
import json
import logging
from pathlib import Path
import platform
import subprocess
import time

import numpy as np
import pandas as pd
import yaml

from mccar_kma.experiments.runner import get_bounds_for_constraint
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("single_worker_timing")

BASE_DIR = Path(__file__).resolve().parent.parent
ALGORITHM_CLASSES = {"kma": KomodoMlipirOptimizer, "ga": GeneticAlgorithmOptimizer, "pso": ParticleSwarmOptimizer}


def detect_machine_spec() -> dict:
    """Spesifikasi mesin: nama CPU (via wmic bila Windows), jumlah core logis, OS."""
    cpu_name = platform.processor() or "unknown"
    if platform.system() == "Windows":
        try:
            out = subprocess.run(
                ["powershell", "-NoProfile", "-Command",
                 "(Get-CimInstance Win32_Processor).Name"],
                capture_output=True, text=True, timeout=10, check=False,
            ).stdout.strip()
            if out:
                cpu_name = out
        except Exception:
            pass
    return {
        "machine_cpu": cpu_name,
        "machine_cores_logical": os_cpu_count(),
        "os_version": f"{platform.system()} {platform.release()} ({platform.version()})",
    }


def os_cpu_count() -> int:
    import os
    return int(os.cpu_count() or 0)


def make_evaluator(cost_matrix: np.ndarray, cfg: dict, tau: float, eta: float) -> PortfolioEvaluator:
    return PortfolioEvaluator(
        cost_matrix=cost_matrix,
        alpha=float(cfg["risk"]["alpha"]),
        delta=float(cfg["risk"]["delta"]),
        tau=tau,
        eta=eta,
        rho_J=float(cfg["optimization"]["penalty_rho_J"]),
        rho_R=float(cfg["optimization"]["penalty_rho_R"]),
        eps_tol=float(cfg["optimization"]["eps_tol"]),
        zero_tol_mc=float(cfg["risk"]["zero_tolerance_mc"]),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--params", default="configs/params.yaml", help="Path params.yaml")
    args = parser.parse_args()

    cfg = yaml.safe_load((BASE_DIR / args.params).read_text(encoding="utf-8"))
    sw = cfg["single_worker_timing"]

    bank = np.load(BASE_DIR / "data" / "processed" / "bank_train_seed42_N5000.npz")
    limits = json.loads(
        (BASE_DIR / "data" / "processed" / "risk_limits_bank_train_seed42_N5000.json").read_text(encoding="utf-8")
    )

    machine = detect_machine_spec()
    logger.info("Spesifikasi mesin: %s", machine)

    budget = int(sw["budget"])
    seed_base = int(sw["seed_base"])
    reps = int(sw["replications"])

    rows = []
    t_all = time.perf_counter()
    for cid in sw["configurations"]:
        cost_def, constraint = cid.split("_", 1)
        lb, ub = get_bounds_for_constraint(constraint)
        cost_matrix = bank[f"cost_{cost_def}"]
        tau = float(limits[cost_def]["tau"])
        eta = float(limits[cost_def]["eta"])
        for algo in sw["algorithms"]:
            for r in range(1, reps + 1):
                seed = seed_base + r
                evaluator = make_evaluator(cost_matrix, cfg, tau, eta)
                opt = ALGORITHM_CLASSES[algo]()
                t0 = time.perf_counter()
                res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=budget, rng=seed)
                elapsed = time.perf_counter() - t0
                rows.append({
                    "config_id": cid, "algo": algo, "rep": r, "seed": seed,
                    "time_seconds": round(elapsed, 4), "best_cost": float(res.best_cost),
                    **machine,
                })
                logger.info("[%s/%s] rep %d/%d: %.2f s", cid, algo, r, reps, elapsed)

    df = pd.DataFrame(rows)
    out_path = BASE_DIR / sw["output_path"]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False)
    logger.info("Tersimpan: %s (%d baris, %.1f s total)", out_path, len(df), time.perf_counter() - t_all)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
