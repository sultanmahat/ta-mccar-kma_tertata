"""Skrip Diagnosis Komprehensif KMA vs GA & PSO (Tahap Diagnosis Metodologis).

Modul:
1. Uji Fidelitas Benchmark Standar (Sphere, Rastrigin, Rosenbrock; D=7 & D=30).
2. Studi Ablasi KMA pada Portofolio (1-fase vs 2-fase, mlipir_rate d2, interaksi q).
3. Analisis Distribusi Slack Kendala (J & tau) dari 360 run eksperimen.
4. Visualisasi Kurva Konvergensi Berpadu Skala Waktu Riil (Evaluasi & Detik).

Luaran:
- results/sensitivity/kma/benchmark_fidelity.csv
- results/sensitivity/kma/ablation_phase_and_mlipir.csv
- results/sensitivity/kma/slack_distribution_analysis.csv
- results/sensitivity/kma/fig_convergence_dual_scale_<config_id>.{pdf,png}
- results/sensitivity/kma/fig_slack_boundary_comparison.{pdf,png}
- results/sensitivity/kma/fig_benchmark_fidelity.{pdf,png}
"""

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import glob
import json
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from mccar_kma.optimizers.base import BaseOptimizer, OptimizationResult
from mccar_kma.optimizers.kma import KomodoMlipirOptimizer
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.viz.style import apply_thesis_style, save_figure

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("diagnosis_kma")


# ==============================================================================
# 1. Definisi Fungsi Benchmark Standar (Unconstrained / Box-Constrained)
# ==============================================================================

def func_sphere(x: np.ndarray) -> float:
    """Sphere: f(x) = sum(x_i^2), optimum f(0) = 0."""
    return float(np.sum(x ** 2))


def func_rastrigin(x: np.ndarray) -> float:
    """Rastrigin: f(x) = 10*D + sum(x_i^2 - 10*cos(2*pi*x_i)), optimum f(0) = 0."""
    D = len(x)
    return float(10.0 * D + np.sum(x ** 2 - 10.0 * np.cos(2.0 * np.pi * x)))


def func_rosenbrock(x: np.ndarray) -> float:
    """Rosenbrock: f(x) = sum(100*(x_{i+1} - x_i^2)^2 + (x_i - 1)^2), optimum f(1) = 0."""
    return float(np.sum(100.0 * (x[1:] - x[:-1] ** 2) ** 2 + (1.0 - x[:-1]) ** 2))


BENCHMARK_SPECS = {
    "sphere": {
        "func": func_sphere,
        "lb_val": -100.0,
        "ub_val": 100.0,
        "optimum": 0.0,
        "type": "Unimodal",
    },
    "rastrigin": {
        "func": func_rastrigin,
        "lb_val": -5.12,
        "ub_val": 5.12,
        "optimum": 0.0,
        "type": "Multimodal",
    },
    "rosenbrock": {
        "func": func_rosenbrock,
        "lb_val": -30.0,
        "ub_val": 30.0,
        "optimum": 0.0,
        "type": "Valley",
    },
}


# ==============================================================================
# 2. Wrapper Box-Constrained untuk Benchmark Standar
# ==============================================================================

class BoxEvaluatorWrapper:
    """Evaluator untuk fungsi benchmark yang hanya memotong ke kotak [lb, ub]."""

    def __init__(self, func, lb: np.ndarray, ub: np.ndarray):
        self.func = func
        self.lb = lb
        self.ub = ub

    def evaluate(self, x: np.ndarray, apply_penalty: bool = False) -> Dict[str, Any]:
        x_clipped = np.clip(x, self.lb, self.ub)
        val = self.func(x_clipped)
        return {
            "w": x_clipped,
            "mean_cost": val,
            "f_val": val,
            "ccar": 0.0,
            "j_mccar": 0.0,
            "v_J": 0.0,
            "v_R": 0.0,
            "is_feasible": True,
        }

    def __call__(self, x: np.ndarray) -> Dict[str, Any]:
        return self.evaluate(x)


# ==============================================================================
# 3. Eksekusi Uji Fidelitas Benchmark Standar
# ==============================================================================

def _run_single_benchmark(args: Tuple) -> Dict[str, Any]:
    fn_name, dim, algo_name, rep, seed, budget = args
    spec = BENCHMARK_SPECS[fn_name]
    lb = np.full(dim, spec["lb_val"])
    ub = np.full(dim, spec["ub_val"])
    evaluator = BoxEvaluatorWrapper(spec["func"], lb, ub)

    # Patch project_weights agar murni box-clipping untuk benchmark unconstrained
    import mccar_kma.optimizers.base as b
    import mccar_kma.optimizers.kma as k
    import mccar_kma.optimizers.pso as p
    import mccar_kma.optimizers.ga as g

    def box_clip(w, _lb, _ub, **kw):
        return np.clip(w, _lb, _ub)

    def box_clip_batch(W, _lb, _ub, **kw):
        return np.clip(W, _lb, _ub)

    b.project_weights = box_clip
    b.project_weights_batch = box_clip_batch
    k.project_weights = box_clip
    p.project_weights = box_clip
    g.project_weights = box_clip

    if algo_name == "kma":
        opt = KomodoMlipirOptimizer(
            phase_1_budget=int(budget * 0.2),
            phase_2_budget=int(budget * 0.8),
            check_interval=250,
        )
    elif algo_name == "ga":
        opt = GeneticAlgorithmOptimizer(check_interval=250)
    elif algo_name == "pso":
        opt = ParticleSwarmOptimizer(check_interval=250)
    else:
        raise ValueError(f"Algoritma tidak dikenal: {algo_name}")

    t0 = time.perf_counter()
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=budget, rng=seed)
    t_elapsed = time.perf_counter() - t0

    return {
        "function": fn_name,
        "dim": dim,
        "algo": algo_name,
        "rep": rep,
        "seed": seed,
        "best_fitness": float(res.best_fitness),
        "time_seconds": round(t_elapsed, 4),
        "evaluations_used": res.evaluations_used,
    }


def run_benchmark_fidelity_study(
    replications: int = 30,
    budget: int = 25000,
    n_workers: int = 4,
) -> pd.DataFrame:
    """Menjalankan uji fidelitas fungsi benchmark standar."""
    logger.info("Menjalankan Uji Fidelitas Benchmark (Sphere, Rastrigin, Rosenbrock)...")
    tasks = []
    base_seed = 100
    for fn_name in ["sphere", "rastrigin", "rosenbrock"]:
        for dim in [7, 30]:
            for algo in ["kma", "ga", "pso"]:
                for r in range(1, replications + 1):
                    seed = base_seed + r
                    tasks.append((fn_name, dim, algo, r, seed, budget))

    logger.info("Total tugas benchmark: %d (workers=%d)", len(tasks), n_workers)
    if n_workers > 1:
        results = []
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            future_to_task = {executor.submit(_run_single_benchmark, t): t for t in tasks}
            done_count = 0
            for future in as_completed(future_to_task):
                res = future.result()
                results.append(res)
                done_count += 1
                if done_count % 30 == 0 or done_count == len(tasks):
                    logger.info("Benchmark progress: %d/%d (%.1f%%) selesai", done_count, len(tasks), done_count / len(tasks) * 100)
    else:
        results = [_run_single_benchmark(t) for t in tasks]

    df = pd.DataFrame(results)
    return df


# ==============================================================================
# 4. Kelas Ablasi & Eksekusi Studi Portofolio
# ==============================================================================

class AblationKMA(KomodoMlipirOptimizer):
    """Subclass KMA untuk mengeksplorasi ablasi struktur fase, d2, dan normalisasi q."""

    def __init__(
        self,
        *args,
        custom_mlipir_rate_2: Optional[float] = None,
        normalize_q: bool = False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.custom_mlipir_rate_2 = custom_mlipir_rate_2
        self.normalize_q = normalize_q

    def _evolve_generation(
        self,
        pop: List[np.ndarray],
        results: List[Dict[str, Any]],
        mlipir_rate: float,
        bound_range: np.ndarray,
        evaluator: Any,
        rng: np.random.Generator,
    ) -> Tuple[List[np.ndarray], List[Dict[str, Any]]]:
        n_pop = len(pop)
        if n_pop < 3 or self.budget.is_exhausted:
            return pop, results

        eff_mlipir = self.custom_mlipir_rate_2 if (self.custom_mlipir_rate_2 is not None and abs(mlipir_rate - 0.5) < 1e-5) else mlipir_rate

        if not self.normalize_q:
            return super()._evolve_generation(
                pop=pop,
                results=results,
                mlipir_rate=eff_mlipir,
                bound_range=bound_range,
                evaluator=evaluator,
                rng=rng,
            )

        from mccar_kma.optimizers.kma import compute_group_sizes
        dim = len(self._lb)
        n_bm, n_female, n_sm = compute_group_sizes(n_pop, self.p_bm)

        # 1. Pergerakan Big Males dengan normalisasi q (w_ij_sum / (q-1))
        q = n_bm if self.q_interactions is None else min(self.q_interactions, n_bm)
        for i in range(n_bm):
            if self.budget.is_exhausted:
                break
            k_i = pop[i]
            w_ij_sum = np.zeros(dim, dtype=float)

            for j in range(q):
                if j == i:
                    continue
                k_j = pop[j]
                r1 = rng.uniform(0.0, 1.0)
                r2 = rng.uniform(0.0, 1.0)

                if results[j]["f_val"] < results[i]["f_val"] or r2 < 0.5:
                    u_ij = r1 * (k_j - k_i)
                else:
                    u_ij = r1 * (k_i - k_j)
                w_ij_sum += u_ij

            if q > 1:
                w_ij_sum /= float(q - 1)

            k_i_new = k_i + w_ij_sum
            new_res = self.evaluate_candidate(k_i_new, evaluator)

            if new_res is not None and new_res["f_val"] < results[i]["f_val"]:
                pop[i] = new_res["w"]
                results[i] = new_res

        # 2. Reproduksi Female (Persamaan 2.28-2.30)
        female_idx = n_bm
        if female_idx < n_pop and not self.budget.is_exhausted:
            k_female = pop[female_idx]
            k_winner = pop[0]
            p_choice = rng.uniform(0.0, 1.0)
            if p_choice < self.p_mating:
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_offspring1 = r_l * k_female + (1.0 - r_l) * k_winner
                k_offspring2 = r_l * k_winner + (1.0 - r_l) * k_female
                res1 = self.evaluate_candidate(k_offspring1, evaluator)
                res2 = self.evaluate_candidate(k_offspring2, evaluator)
                best_res = None
                if res1 is not None and res2 is not None:
                    best_res = res1 if res1["f_val"] < res2["f_val"] else res2
                elif res1 is not None:
                    best_res = res1
                elif res2 is not None:
                    best_res = res2
                if best_res is not None and best_res["f_val"] < results[female_idx]["f_val"]:
                    pop[female_idx] = best_res["w"]
                    results[female_idx] = best_res
            else:
                r_l = rng.uniform(0.0, 1.0, size=dim)
                k_partheno = k_female + (2.0 * r_l - 1.0) * self.gamma * bound_range
                res_partheno = self.evaluate_candidate(k_partheno, evaluator)
                if res_partheno is not None and res_partheno["f_val"] < results[female_idx]["f_val"]:
                    pop[female_idx] = res_partheno["w"]
                    results[female_idx] = res_partheno

        # 3. Small Males (Persamaan 2.31-2.32)
        start_sm = n_bm + n_female
        for i in range(start_sm, n_pop):
            if self.budget.is_exhausted:
                break
            k_i = pop[i]
            k_i_new = k_i.copy()
            for j in range(n_bm):
                k_j = pop[j]
                for l in range(dim):
                    r2 = rng.uniform(0.0, 1.0)
                    if r2 < eff_mlipir:
                        r1 = rng.uniform(0.0, 1.0)
                        u_ijl = r1 * (k_j[l] - k_i[l])
                        k_i_new[l] += u_ijl
            new_sm_res = self.evaluate_candidate(k_i_new, evaluator)
            if new_sm_res is not None:
                pop[i] = new_sm_res["w"]
                results[i] = new_sm_res

        return self._sort_population(pop, results)


def _run_single_ablation(args: Tuple) -> Dict[str, Any]:
    variant_name, config_id, rep, seed, budget, bank_path, limits_path = args

    # Pastikan fungsi proyeksi simpleks asli digunakan untuk portofolio
    from mccar_kma.model.constraints import project_weights as pw_orig, project_weights_batch as pwb_orig
    import mccar_kma.optimizers.base as b
    import mccar_kma.optimizers.kma as k
    import mccar_kma.optimizers.pso as p
    import mccar_kma.optimizers.ga as g

    b.project_weights = pw_orig
    b.project_weights_batch = pwb_orig
    k.project_weights = pw_orig
    p.project_weights = pw_orig
    g.project_weights = pw_orig

    bank = np.load(bank_path)
    with open(limits_path, "r", encoding="utf-8") as f:
        limits = json.load(f)

    cost_def = "interest" if "interest" in config_id else "gross"
    tau = float(limits[cost_def]["tau"])
    eta = float(limits[cost_def]["eta"])
    cost_matrix = bank[f"cost_{cost_def}"]
    evaluator = PortfolioEvaluator(cost_matrix=cost_matrix, tau=tau, eta=eta)

    lb = np.zeros(7)
    ub = np.ones(7)

    # Inisialisasi varian KMA
    if variant_name == "kma_2phase_default":
        opt = KomodoMlipirOptimizer(
            phase_1_budget=5000,
            phase_2_budget=20000,
            phase_1_n_pop=5,
            phase_2_n_pop_init=200,
        )
    elif variant_name == "kma_1phase_n50":
        opt = KomodoMlipirOptimizer(
            phase_1_budget=25000,
            phase_2_budget=0,
            phase_1_n_pop=50,
        )
    elif variant_name == "kma_1phase_n20":
        opt = KomodoMlipirOptimizer(
            phase_1_budget=25000,
            phase_2_budget=0,
            phase_1_n_pop=20,
        )
    elif variant_name == "kma_2phase_d2_high":
        # d2 = 6/7 = 0.857
        opt = AblationKMA(
            phase_1_budget=5000,
            phase_2_budget=20000,
            phase_1_n_pop=5,
            phase_2_n_pop_init=200,
            custom_mlipir_rate_2=(7.0 - 1.0) / 7.0,
        )
    elif variant_name == "kma_2phase_d2_low":
        # d2 = 1/7 = 0.143
        opt = AblationKMA(
            phase_1_budget=5000,
            phase_2_budget=20000,
            phase_1_n_pop=5,
            phase_2_n_pop_init=200,
            custom_mlipir_rate_2=1.0 / 7.0,
        )
    elif variant_name == "kma_2phase_norm_q":
        # normalisasi w_ij_sum / (q-1) untuk Big Males
        opt = AblationKMA(
            phase_1_budget=5000,
            phase_2_budget=20000,
            phase_1_n_pop=5,
            phase_2_n_pop_init=200,
            normalize_q=True,
        )
    else:
        raise ValueError(f"Varian ablasi tidak dikenal: {variant_name}")

    t0 = time.perf_counter()
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=budget, rng=seed)
    t_elapsed = time.perf_counter() - t0

    # Ambil metrik akhir
    final_eval = evaluator.evaluate(res.best_w)
    slack_J = eta - float(final_eval["j_mccar"])
    slack_R = tau - float(final_eval["ccar"])

    return {
        "variant": variant_name,
        "config_id": config_id,
        "rep": rep,
        "seed": seed,
        "best_cost": float(res.best_cost),
        "best_fitness": float(res.best_fitness),
        "is_feasible": bool(res.is_feasible and final_eval["is_feasible"]),
        "ccar": float(final_eval["ccar"]),
        "j_mccar": float(final_eval["j_mccar"]),
        "slack_J": slack_J,
        "slack_R": slack_R,
        "time_seconds": round(t_elapsed, 4),
    }


def run_ablation_study(
    replications: int = 10,
    budget: int = 25000,
    n_workers: int = 4,
) -> pd.DataFrame:
    """Menjalankan studi ablasi struktur fase dan laju mlipir KMA."""
    logger.info("Menjalankan Studi Ablasi KMA pada Masalah Portofolio...")
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    limits_path = Path("data/processed/risk_limits_bank_train_seed42_N5000.json")

    variants = [
        "kma_2phase_default",
        "kma_1phase_n50",
        "kma_1phase_n20",
        "kma_2phase_d2_high",
        "kma_2phase_d2_low",
        "kma_2phase_norm_q",
    ]
    configs = ["interest_free", "gross_free"]

    tasks = []
    base_seed = 42
    for v in variants:
        for cid in configs:
            for r in range(1, replications + 1):
                seed = base_seed + r
                tasks.append((v, cid, r, seed, budget, bank_path, limits_path))

    logger.info("Total tugas ablasi: %d (workers=%d)", len(tasks), n_workers)
    if n_workers > 1:
        results = []
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            future_to_task = {executor.submit(_run_single_ablation, t): t for t in tasks}
            done_count = 0
            for future in as_completed(future_to_task):
                res = future.result()
                results.append(res)
                done_count += 1
                if done_count % 10 == 0 or done_count == len(tasks):
                    logger.info("Ablasi progress: %d/%d (%.1f%%) selesai", done_count, len(tasks), done_count / len(tasks) * 100)
    else:
        results = [_run_single_ablation(t) for t in tasks]

    df = pd.DataFrame(results)
    return df


# ==============================================================================
# 5. Analisis Slack Kendala dari 360 Run Eksisting
# ==============================================================================

def analyze_constraint_slacks_360_runs() -> pd.DataFrame:
    """Mengekstrak dan menganalisis slack J dan tau dari 360 file run JSON."""
    logger.info("Menganalisis Slack Kendala J dan Tau dari 360 Berkas Run...")
    json_files = glob.glob("results/runs/**/*.json", recursive=True)
    assert len(json_files) == 360, f"Harusnya 360 run, ditemukan {len(json_files)}"

    records = []
    for fpath in json_files:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)

        cid = data["config_id"]
        algo = data["algo"]
        rep = data["rep"]
        seed = data["seed"]
        cost = data["best_cost"]
        ccar = data["ccar"]
        j_mccar = data["j_mccar"]
        tau = data["tau_limit"]
        eta = data["eta_limit"]
        t_sec = data["time_seconds"]
        is_feas = data["is_feasible"]

        slack_j = eta - j_mccar
        slack_r = tau - ccar

        records.append({
            "config_id": cid,
            "algo": algo,
            "rep": rep,
            "seed": seed,
            "best_cost": cost,
            "ccar": ccar,
            "j_mccar": j_mccar,
            "tau": tau,
            "eta": eta,
            "slack_J": slack_j,
            "slack_R": slack_r,
            "time_seconds": t_sec,
            "is_feasible": is_feas,
        })

    df = pd.DataFrame(records)
    return df


# ==============================================================================
# 6. Pembangkitan Grafik Visualisasi
# ==============================================================================

def generate_diagnostic_plots(
    df_bench: pd.DataFrame,
    df_slack: pd.DataFrame,
    df_ablation: pd.DataFrame,
    out_dir: Path,
):
    """Membangkitkan seluruh grafik visualisasi diagnosis."""
    logger.info("Membangkitkan Grafik Visualisasi Diagnosis...")
    apply_thesis_style()

    # -------------------------------------------------------------------------
    # Grafik 1: Boxplot Distribusi Slack J (Jarak ke Batas Aktif)
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), sharey=False)
    configs = ["interest_free", "gross_free"]
    algos = ["kma", "ga", "pso"]
    algo_labels = ["KMA", "GA", "PSO"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

    for idx, cid in enumerate(configs):
        ax = axes[idx]
        sub = df_slack[df_slack["config_id"] == cid]
        data_plot = [sub[sub["algo"] == a]["slack_J"].values for a in algos]

        bp = ax.boxplot(data_plot, tick_labels=algo_labels, patch_artist=True, widths=0.5)
        for patch, col in zip(bp["boxes"], colors):
            patch.set_facecolor(col)
            patch.set_alpha(0.7)

        ax.axhline(0, color="red", linestyle="--", alpha=0.7, label=r"Batas Aktif ($\eta$)")
        ax.set_title(f"Distribusi Slack Kendala J: {cid}")
        ax.set_ylabel(r"Slack J ($\eta - J$)")
        ax.grid(True, linestyle=":", alpha=0.6)
        if idx == 0:
            ax.legend(loc="upper right")

    plt.tight_layout()
    save_figure(fig, out_dir / "fig_slack_boundary_comparison")

    # -------------------------------------------------------------------------
    # Grafik 2: Kurva Konvergensi Berpadu Skala Waktu Riil (interest_free)
    # -------------------------------------------------------------------------
    json_if = glob.glob("results/runs/interest_free/**/*.json", recursive=True)
    algo_histories = {"kma": [], "ga": [], "pso": []}
    algo_times = {"kma": [], "ga": [], "pso": []}

    for fpath in json_if:
        with open(fpath, "r", encoding="utf-8") as f:
            d = json.load(f)
        a = d["algo"]
        hist = d.get("convergence_history", [])
        if hist:
            evals = [pt["evaluation"] for pt in hist]
            costs = [pt["best_cost"] for pt in hist]
            algo_histories[a].append((evals, costs))
            algo_times[a].append(d["time_seconds"])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.8))

    eval_grid = np.linspace(250, 25000, 100)
    for a, col, lbl in zip(algos, colors, algo_labels):
        curves = []
        for evals, costs in algo_histories[a]:
            # Interpolasi ke grid evaluasi
            interp_c = np.interp(eval_grid, evals, costs)
            curves.append(interp_c)

        curves = np.array(curves)
        med = np.median(curves, axis=0)
        q25 = np.percentile(curves, 25, axis=0)
        q75 = np.percentile(curves, 75, axis=0)

        # Panel 1: Konvergensi vs Evaluasi
        ax1.plot(eval_grid, med, color=col, label=lbl, linewidth=2)
        ax1.fill_between(eval_grid, q25, q75, color=col, alpha=0.2)

        # Panel 2: Konvergensi vs Waktu Riil
        avg_time = np.mean(algo_times[a])
        time_grid = (eval_grid / 25000.0) * avg_time
        ax2.plot(time_grid, med, color=col, label=f"{lbl} (~{avg_time:.1f}s)", linewidth=2)
        ax2.fill_between(time_grid, q25, q75, color=col, alpha=0.2)

    ax1.set_xlabel("Jumlah Evaluasi Fungsi")
    ax1.set_ylabel("Nilai Biaya Terbaik")
    ax1.set_title("Konvergensi vs Anggaran Evaluasi (interest_free)")
    ax1.grid(True, linestyle=":", alpha=0.6)
    ax1.legend(loc="upper right")

    ax2.set_xlabel("Waktu Komputasi Riil (detik)")
    ax2.set_ylabel("Nilai Biaya Terbaik")
    ax2.set_title("Konvergensi vs Waktu Riil (interest_free)")
    ax2.grid(True, linestyle=":", alpha=0.6)
    ax2.legend(loc="upper right")

    plt.tight_layout()
    save_figure(fig, out_dir / "fig_convergence_dual_scale_interest_free")

    # -------------------------------------------------------------------------
    # Grafik 3: Performa Benchmark Standar (D=7 vs D=30)
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2))
    fns = ["sphere", "rastrigin", "rosenbrock"]

    for idx, fn in enumerate(fns):
        ax = axes[idx]
        sub = df_bench[df_bench["function"] == fn]

        x_pos = np.arange(len(algos))
        width = 0.35

        med_7 = [sub[(sub["algo"] == a) & (sub["dim"] == 7)]["best_fitness"].median() for a in algos]
        med_30 = [sub[(sub["algo"] == a) & (sub["dim"] == 30)]["best_fitness"].median() for a in algos]

        # Log scale if values span multiple orders of magnitude
        ax.bar(x_pos - width / 2, med_7, width, label="D=7", color="#4a7bb0", alpha=0.8)
        ax.bar(x_pos + width / 2, med_30, width, label="D=30", color="#e07a5f", alpha=0.8)

        ax.set_xticks(x_pos)
        ax.set_xticklabels(algo_labels)
        ax.set_title(fn.capitalize())
        ax.set_yscale("log")
        ax.set_ylabel("Nilai Fitness Terbaik (Log Scale)")
        ax.grid(True, linestyle=":", alpha=0.6)
        if idx == 0:
            ax.legend()

    plt.tight_layout()
    save_figure(fig, out_dir / "fig_benchmark_fidelity")


# ==============================================================================
# 7. Fungsi Utama Orkestrasi Diagnosis
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Diagnosis Performa KMA vs GA & PSO")
    parser.add_argument("--smoke", action="store_true", help="Jalankan mode smoke test cepat (2 rep)")
    parser.add_argument("--reps", type=int, default=30, help="Jumlah replikasi benchmark (default: 30)")
    parser.add_argument("--ablation-reps", type=int, default=10, help="Jumlah replikasi ablasi portofolio (default: 10)")
    parser.add_argument("--workers", type=int, default=4, help="Jumlah worker paralel (default: 4)")
    args = parser.parse_args()

    reps = 2 if args.smoke else args.reps
    ablation_reps = 2 if args.smoke else args.ablation_reps
    budget = 500 if args.smoke else 25000

    out_dir = Path("results/sensitivity/kma")
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Analisis Slack dari 360 Run Eksisting
    df_slack = analyze_constraint_slacks_360_runs()
    slack_summary = df_slack.groupby(["config_id", "algo"])[["slack_J", "slack_R", "best_cost", "time_seconds"]].agg(
        ["mean", "median", "std", "min", "max"]
    )
    slack_csv = out_dir / "slack_distribution_analysis.csv"
    slack_summary.to_csv(slack_csv)
    logger.info("Ringkasan slack disimpan ke: %s", slack_csv)

    # 2. Uji Fidelitas Benchmark Standar
    df_bench = run_benchmark_fidelity_study(replications=reps, budget=budget, n_workers=args.workers)
    bench_csv = out_dir / "benchmark_fidelity.csv"
    bench_summary = df_bench.groupby(["function", "dim", "algo"])[["best_fitness", "time_seconds"]].agg(
        ["median", "mean", "std", "min", "max"]
    )
    bench_summary.to_csv(bench_csv)
    logger.info("Hasil benchmark disimpan ke: %s", bench_csv)

    # 3. Studi Ablasi KMA pada Masalah Portofolio
    df_ablation = run_ablation_study(replications=ablation_reps, budget=budget, n_workers=args.workers)
    ablation_csv = out_dir / "ablation_phase_and_mlipir.csv"
    ablation_summary = df_ablation.groupby(["config_id", "variant"])[["best_cost", "slack_J", "time_seconds"]].agg(
        ["median", "mean", "std", "min", "max"]
    )
    ablation_summary.to_csv(ablation_csv)
    logger.info("Hasil ablasi disimpan ke: %s", ablation_csv)

    # 4. Pembangkitan Seluruh Grafik Diagnosis
    generate_diagnostic_plots(df_bench, df_slack, df_ablation, out_dir)
    logger.info("Seluruh grafik visualisasi diagnosis berhasil disimpan di %s!", out_dir)


if __name__ == "__main__":
    main()
