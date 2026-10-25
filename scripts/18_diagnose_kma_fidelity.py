"""Tahap 18: Diagnosis KMA v2 — fidelitas benchmark, instrumentasi kendala, timing, ablation.

Semua parameter dibaca dari blok `kma_diagnosis` di configs/params.yaml. Keluaran hanya ke
`kma_diagnosis.output_dir` (results/sensitivity/kma); results/runs, results/tables, results/figures,
dan results/sensitivity/limits ditolak. kma.py / ga.py / pso.py tidak diubah.

Tahap A: main360 (read-only), timing (1 worker, sekuensial), profile, benchmark D=7/30, instrument.
Tahap B: benchmark D=50 + fungsi tergeser + varian KMA, ablation portofolio.

Contoh:
    python scripts/18_diagnose_kma_fidelity.py --stage A --smoke
    python scripts/18_diagnose_kma_fidelity.py --stage A
    python scripts/18_diagnose_kma_fidelity.py --stage B --workers 10
    python scripts/18_diagnose_kma_fidelity.py --stage none   # hanya bangun ulang tabel & grafik
"""

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import argparse
import json
import logging
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

from mccar_kma.analysis import kma_diagnosis as kd  # noqa: E402
from mccar_kma.viz import kma_figures as kf  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("diagnose_kma_v2")

STAGE_STEPS = {
    "A": ["main360", "timing", "profile", "benchmark", "instrument"],
    "B": ["benchmark", "ablation"],
    "none": [],
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--params", default="configs/params.yaml")
    p.add_argument("--stage", choices=["A", "B", "none"], required=True)
    p.add_argument("--steps", default=None, help="Subset langkah dipisah koma (default: semua langkah tahap)")
    p.add_argument("--smoke", action="store_true", help="Anggaran & replikasi kecil, keluaran ke subfolder smoke/")
    p.add_argument("--workers", type=int, default=None, help="Menimpa kma_diagnosis.n_workers")
    p.add_argument("--no-resume", action="store_true")
    p.add_argument("--skip-figures", action="store_true")
    return p.parse_args()


def run_parallel(func: Callable[[Dict[str, Any]], Any], tasks: List[Dict[str, Any]], workers: int, label: str) -> List[Any]:
    todo = [t for t in tasks if not (t.get("resume", True) and Path(t["out_path"]).exists())]
    logger.info("[%s] %d tugas (%d sudah ada, %d dijalankan), workers=%d",
                label, len(tasks), len(tasks) - len(todo), len(todo), workers)
    failures = []
    t0 = time.perf_counter()
    if workers <= 1:
        for i, t in enumerate(todo, 1):
            func(t)
            if i % 10 == 0 or i == len(todo):
                logger.info("[%s] %d/%d (%.0f s)", label, i, len(todo), time.perf_counter() - t0)
    else:
        with ProcessPoolExecutor(max_workers=workers) as ex:
            futs = {ex.submit(func, t): t for t in todo}
            for i, fut in enumerate(as_completed(futs), 1):
                try:
                    fut.result()
                except Exception as e:  # dicatat, tidak disembunyikan
                    failures.append((futs[fut]["out_path"], repr(e)))
                    logger.error("[%s] GAGAL %s: %r", label, futs[fut]["out_path"], e)
                if i % 25 == 0 or i == len(todo):
                    logger.info("[%s] %d/%d (%.0f s)", label, i, len(todo), time.perf_counter() - t0)
    if failures:
        logger.error("[%s] %d tugas gagal", label, len(failures))
    return failures


def benchmark_tasks(cfg, stage, out_dir, budget, reps, resume, chash) -> List[Dict[str, Any]]:
    d = cfg["kma_diagnosis"]
    b = d["benchmark"]
    tasks: List[Dict[str, Any]] = []

    def add(set_name, fn, dim, algo, shifted):
        lo, hi = b["domains"][fn]
        shift = kd.make_shift(fn, dim, lo, hi, b).tolist() if shifted else None
        tag = "shift" if shifted else "base"
        for r in range(1, reps + 1):
            seed = int(b["seed_base"]) + r
            out = out_dir / "runs_benchmark" / set_name / f"{fn}_D{dim}_{tag}_{algo}_rep{r:02d}_seed{seed}.json"
            tasks.append({"set": set_name, "function": fn, "dim": int(dim), "algo": algo, "shift": shift,
                          "domain": [float(lo), float(hi)], "rep": r, "seed": seed, "budget": budget,
                          "checkpoints": d["checkpoints"], "config_hash": chash, "out_path": str(out),
                          "resume": resume})

    if stage == "A":
        for fn in b["functions"]:
            for dim in b["dims_stage_a"]:
                for a in b["algorithms"]:
                    add("stage_a", fn, dim, a, False)
    else:
        for fn in b["functions"]:
            for dim in b["dims_stage_b"]:
                for a in b["algorithms"]:
                    add("stage_b", fn, dim, a, False)
            for dim in b["shifted_dims"]:
                for a in b["shifted_algorithms"]:
                    add("shifted", fn, dim, a, True)
            for dim in b["variant_dims"]:
                for v in b["variants"]:
                    add("variants", fn, dim, f"kma_{v}", False)
    # Tugas termahal dulu (KMA, D besar) agar beban worker seimbang
    tasks.sort(key=lambda t: (not t["algo"].startswith("kma"), -t["dim"]))
    return tasks


def portfolio_tasks(cfg, kind, out_dir, budget, reps, resume, common) -> List[Dict[str, Any]]:
    d = cfg["kma_diagnosis"]
    if kind == "instrument":
        sub, algos, configs = d["instrumentation"], d["instrumentation"]["algorithms"], d["portfolio_ablation"]["configurations"]
    elif kind == "timing":
        sub, algos, configs = d["timing"], d["timing"]["algorithms"], d["portfolio_ablation"]["configurations"]
    else:
        sub = d["portfolio_ablation"]
        algos, configs = [f"kma_{v}" for v in sub["variants"]], sub["configurations"]
    tasks = []
    for cid in configs:
        for a in algos:
            for r in range(1, reps + 1):
                seed = int(sub["seed_base"]) + r
                out = out_dir / f"runs_{kind}" / cid / a / f"rep{r:02d}_seed{seed}.json"
                tasks.append({**common, "kind": kind, "config_id": cid, "algo": a, "rep": r, "seed": seed,
                              "budget": budget, "out_path": str(out), "resume": resume})
    tasks.sort(key=lambda t: not t["algo"].startswith("kma"))
    return tasks


# ------------------------------------------------------------------------------
def build_outputs(cfg: Dict[str, Any], out_dir: Path, skip_figures: bool) -> None:
    d = cfg["kma_diagnosis"]
    floor = float(d["log_floor"])

    # 360 run utama (read-only)
    df_main, curves = kd.load_main_runs(BASE_DIR)
    s = kd.summarize_main_runs(df_main)
    df_main.to_csv(out_dir / "main_runs_360.csv", index=False)
    s["slack"].to_csv(out_dir / "slack_360.csv", index=False)
    s["checkpoints"].to_csv(out_dir / "convergence_checkpoints.csv", index=False)
    s["phase"].to_csv(out_dir / "phase_improvement_360.csv", index=False)
    ref_best = df_main.groupby("config_id")["ref_best_cost"].first().to_dict()

    # Timing 1 worker
    trecs = kd.load_json_dir(out_dir / "runs_timing")
    timing = pd.DataFrame([{"config_id": r["config_id"], "algo": r["algo"], "rep": r["rep"],
                            "evaluation": m[0], "seconds": m[1]} for r in trecs for m in r["timing_marks"]])
    if not timing.empty:
        timing.to_csv(out_dir / "timing_single_worker.csv", index=False)
        tsum = pd.DataFrame([{"config_id": r["config_id"], "algo": r["algo"], "rep": r["rep"],
                              "time_seconds": r["time_seconds"], "best_cost": r["best_cost"]} for r in trecs])
        tsum.groupby(["config_id", "algo"]).agg(
            n=("rep", "count"), seconds_median=("time_seconds", "median"), seconds_min=("time_seconds", "min"),
            seconds_max=("time_seconds", "max")).reset_index().to_csv(out_dir / "timing_summary.csv", index=False)

    # Benchmark
    brecs = kd.load_json_dir(out_dir / "runs_benchmark")
    bdf, bsum = kd.summarize_benchmark(brecs)
    if not bdf.empty:
        bdf.to_csv(out_dir / "benchmark_runs.csv", index=False)
        bsum.to_csv(out_dir / "benchmark_fidelity.csv", index=False)
        kd.compare_with_suyanto(bsum, d["reference_suyanto_2022"]).to_csv(out_dir / "benchmark_vs_suyanto.csv", index=False)

    # Instrumentasi
    irecs = kd.load_json_dir(out_dir / "runs_instrument")
    blocks_rows, gen_rows, inst_runs = [], [], []
    for r in irecs:
        bl = pd.DataFrame(r.get("blocks", {}))
        if not bl.empty:
            bl.insert(0, "rep", r["rep"]); bl.insert(0, "algo", r["algo"]); bl.insert(0, "config_id", r["config_id"])
            blocks_rows.append(bl)
        for g in r.get("gen_log", []):
            gen_rows.append({"config_id": r["config_id"], "rep": r["rep"], **g})
        inst_runs.append({k: r[k] for k in ("config_id", "algo", "rep", "best_cost", "slack_J_rel", "is_feasible")})
    blocks = pd.concat(blocks_rows, ignore_index=True) if blocks_rows else pd.DataFrame()
    gen = pd.DataFrame(gen_rows)
    if not blocks.empty:
        blocks.to_csv(out_dir / "instrumentation_blocks.csv", index=False)
        p1_end = 5000
        blocks["window"] = np.where(blocks["eval_end"] <= p1_end, "eval_1-5000", "eval_5001-25000")
        cols = ["frac_projected", "mean_proj_dist", "median_proj_dist", "mean_n_at_bound", "frac_fallback_mid",
                "frac_raw_out_box", "frac_vJ_pos", "frac_vR_pos", "frac_feasible", "frac_near_boundary"]
        blocks.groupby(["config_id", "algo", "window"])[cols].mean().reset_index().to_csv(
            out_dir / "instrumentation_summary.csv", index=False)
    if not gen.empty:
        gen.to_csv(out_dir / "kma_generation_log.csv", index=False)
        gen["acc"] = gen["bm_accepted"] / gen["bm_attempts"].clip(lower=1)
        gen.groupby(["config_id", "phase"]).agg(
            generations_per_run=("generation", lambda x: len(x) / max(1, gen["rep"].nunique())),
            bm_acceptance_mean=("acc", "mean"), bm_step_norm_median=("bm_step_norm_median", "median"),
            bm_step_norm_p90=("bm_step_norm_median", lambda x: float(np.percentile(x, 90))),
            n_pop_median=("n_pop", "median"), n_bm_median=("n_bm", "median"),
            female_acceptance=("female_accepted", "mean"),
        ).reset_index().to_csv(out_dir / "kma_phase_summary.csv", index=False)
    if inst_runs:
        pd.DataFrame(inst_runs).to_csv(out_dir / "instrumentation_runs.csv", index=False)

    # Ablation
    arecs = kd.load_json_dir(out_dir / "runs_ablation")
    adf = kd.summarize_portfolio(arecs, ref_best)
    if not adf.empty:
        adf.to_csv(out_dir / "ablation_portfolio.csv", index=False)
        adf.groupby(["config_id", "algo"]).agg(
            n=("rep", "count"), cost_median=("best_cost", "median"), gap_pct_median=("gap_pct", "median"),
            gap_pct_q25=("gap_pct", lambda x: float(np.percentile(x, 25))),
            gap_pct_q75=("gap_pct", lambda x: float(np.percentile(x, 75))),
            slack_J_rel_median=("slack_J_rel", "median"), feasible_rate=("is_feasible", "mean"),
            time_median=("time_seconds", "median"),
        ).reset_index().to_csv(out_dir / "ablation_summary.csv", index=False)
        kd.ablation_tests(adf).to_csv(out_dir / "ablation_tests.csv", index=False)

    if skip_figures:
        return
    kf.fig_convergence(df_main, curves, timing if not timing.empty else pd.DataFrame(
        columns=["config_id", "algo", "evaluation", "seconds"]), out_dir)
    kf.fig_slack_and_phase(df_main, out_dir, floor)
    if not bdf.empty:
        kf.fig_benchmark_fidelity(bdf, d["reference_suyanto_2022"], out_dir, floor)
        kf.fig_benchmark_shift(bdf, out_dir, floor)
        kf.fig_benchmark_variants(bdf, out_dir, floor)
    if not gen.empty:
        kf.fig_acceptance(gen, out_dir)
    if not blocks.empty:
        kf.fig_projection(blocks, out_dir)
    if not adf.empty:
        kf.fig_ablation(adf, out_dir)
    prof_path = out_dir / "profile_kma.csv"
    if prof_path.exists():
        kf.fig_time_profile(pd.read_csv(prof_path), out_dir)


def main() -> int:
    args = parse_args()
    cfg = kd.load_config(BASE_DIR / args.params)
    d = cfg["kma_diagnosis"]
    out_dir = BASE_DIR / d["output_dir"]
    budget, rep_scale = int(d["budget"]), None
    if args.smoke:
        out_dir = out_dir / "smoke"
        budget, rep_scale = int(d["smoke"]["budget"]), int(d["smoke"]["replications"])
    kd.assert_safe_output_dir(out_dir, BASE_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    workers = int(args.workers or d["n_workers"])
    resume = not args.no_resume
    steps = STAGE_STEPS[args.stage] if args.steps is None else [s.strip() for s in args.steps.split(",")]

    chash = kd.config_hash(cfg)
    bank_path, limits_path = kd.bank_paths(BASE_DIR, cfg)
    data_version = kd.file_sha256(bank_path)[:16]
    common = {"bank_path": str(bank_path), "limits_path": str(limits_path), "checkpoints": d["checkpoints"],
              "config_hash": chash, "data_version": data_version,
              "eps_tol": float(cfg["optimization"]["eps_tol"]),
              "block_size": int(d["instrumentation"]["block_size"]),
              "dist_tol": float(d["projection_distance_tol"]), "bound_tol": float(d["bound_tol"]),
              "near_rel": float(d["instrumentation"]["near_boundary_rel_slack"])}

    def reps(n: int) -> int:
        return rep_scale if rep_scale is not None else int(n)

    failures = []
    t_all = time.perf_counter()
    for step in steps:
        logger.info("=== Langkah %s (tahap %s) ===", step, args.stage)
        if step == "main360":
            pass  # dibangun di build_outputs (read-only)
        elif step == "timing":
            tasks = portfolio_tasks(cfg, "timing", out_dir, budget, reps(d["timing"]["replications"]), resume, common)
            failures += run_parallel(kd.run_portfolio_task, tasks, 1, "timing")
        elif step == "profile":
            prof_path = out_dir / "profile_kma.csv"
            if resume and prof_path.exists():
                logger.info("[profile] sudah ada, dilewati")
                continue
            rows = []
            for cid in d["portfolio_ablation"]["configurations"]:
                for a in d["timing"]["algorithms"]:
                    rows.append(kd.run_profile_task({**common, "config_id": cid, "algo": a,
                                                     "seed": int(d["timing"]["profile_seed"]), "budget": budget}))
                    logger.info("[profile] %s %s: %.1f s", cid, a, rows[-1]["profiled_total_seconds"])
            pd.DataFrame(rows).to_csv(prof_path, index=False)
        elif step == "benchmark":
            tasks = benchmark_tasks(cfg, args.stage, out_dir, budget, reps(d["benchmark"]["replications"]), resume, chash)
            failures += run_parallel(kd.run_benchmark_task, tasks, workers, f"benchmark-{args.stage}")
        elif step == "instrument":
            tasks = portfolio_tasks(cfg, "instrument", out_dir, budget, reps(d["instrumentation"]["replications"]), resume, common)
            failures += run_parallel(kd.run_portfolio_task, tasks, workers, "instrument")
        elif step == "ablation":
            tasks = portfolio_tasks(cfg, "ablation", out_dir, budget, reps(d["portfolio_ablation"]["replications"]), resume, common)
            failures += run_parallel(kd.run_portfolio_task, tasks, workers, "ablation")
        else:
            raise SystemExit(f"Langkah tidak dikenal: {step}")

    build_outputs(cfg, out_dir, args.skip_figures)
    meta = {"date": kd.now_iso(), "config_hash": chash, "data_version": data_version,
            "bank_path": str(bank_path.relative_to(BASE_DIR)), "stage": args.stage, "steps": steps,
            "smoke": args.smoke, "budget": budget, "workers": workers,
            "elapsed_seconds": round(time.perf_counter() - t_all, 1), "failures": failures}
    with open(out_dir / f"metadata_stage_{args.stage}.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=1)
    logger.info("Selesai tahap %s dalam %.1f s; gagal: %d", args.stage, meta["elapsed_seconds"], len(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
