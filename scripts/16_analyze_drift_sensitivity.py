"""Skrip Analisis Sensitivitas Drift GBM, Jendela Data D1-B, dan Definisi Biaya.

Modul Pelaksanaan:
1. Studi Sensitivitas 4 Skenario Drift GBM:
   (a) Drift historis penuh (basis / baseline, seed 42)
   (b) Drift kurs = 0, drift yield historis (seed 1042)
   (c) Semua drift = 0 (martingale murni, seed 2042)
   (d) Drift shrinkage 50% (lambda = 0.5, seed 3042)
2. Studi Sensitivitas Jendela Data D1-B (Spline 2.191 baris vs Intersection 2.028 baris).
3. Studi Sensitivitas Definisi Biaya (Bruto / Gross vs Bunga / Interest).
4. Pembangkitan Tabel CSV dan Grafik Gaya D9 (PDF vektor + PNG 300 dpi).

Luaran:
- results/sensitivity/drift/drift_scenarios_comparison.csv
- results/sensitivity/drift/data_window_spline_vs_intersection.csv
- results/sensitivity/drift/cost_definitions_comparison.csv
- results/sensitivity/drift/fig_drift_sensitivity_weights.{pdf,png}
- results/sensitivity/drift/fig_drift_savings_comparison.{pdf,png}
- results/sensitivity/drift/fig_cost_definitions_tradeoff.{pdf,png}
- docs/reviews/sensitivitas_drift.md
"""

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import json
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mccar_kma.data.cleaning import ALL_MARKET_COLS, compute_log_returns
from mccar_kma.model.constraints import (
    LB_DJPPR,
    UB_DJPPR,
    LB_FREE,
    UB_FREE,
    W0,
)
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.scenarios.cost import build_scenario_bank
from mccar_kma.scenarios.estimation import (
    INSTRUMENTS,
    INSTRUMENT_NAMES,
    compute_correlation_matrix,
    estimate_gbm_params,
)
from mccar_kma.scenarios.gbm import generate_market_scenarios
from mccar_kma.viz.style import (
    INSTRUMENT_COLORS,
    INSTRUMENT_DISPLAY_NAMES,
    INSTRUMENT_HATCHES,
    apply_thesis_style,
    save_figure,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("drift_sensitivity")


# ==============================================================================
# 1. Pembangkitan Bank Skenario Sensitivitas Drift
# ==============================================================================

DRIFT_SCENARIOS = {
    "historical": {
        "label": "Drift Historis Penuh (Basis)",
        "desc": "mu = mu_annual_hist untuk seluruh variabel",
        "seed": 42,
    },
    "fx_zero": {
        "label": "Drift Kurs = 0",
        "desc": "mu_fx = 0, mu_yield = mu_annual_hist",
        "seed": 1042,
    },
    "martingale": {
        "label": "Martingale Murni",
        "desc": "mu = 0 untuk seluruh variabel pasar",
        "seed": 2042,
    },
    "shrinkage_half": {
        "label": "Drift Shrinkage 50%",
        "desc": "mu = 0.5 * mu_annual_hist untuk seluruh variabel",
        "seed": 3042,
    },
}


def build_drift_scenario_bank(
    scenario_key: str,
    df_params_base: pd.DataFrame,
    df_corr_base: pd.DataFrame,
    s0_series: pd.Series,
    n_scenarios: int = 5000,
) -> Dict[str, Any]:
    """Membangkitkan bank skenario berdasarkan spesifikasi drift tertentu."""
    spec = DRIFT_SCENARIOS[scenario_key]
    seed = spec["seed"]
    df_p = df_params_base.copy()

    if scenario_key == "historical":
        pass  # mu_annual tetap
    elif scenario_key == "fx_zero":
        df_p.loc[df_p["variable"].str.startswith("FX_"), "mu_annual"] = 0.0
    elif scenario_key == "martingale":
        df_p["mu_annual"] = 0.0
    elif scenario_key == "shrinkage_half":
        df_p["mu_annual"] = 0.5 * df_p["mu_annual"]
    else:
        raise ValueError(f"Skenario tidak dikenal: {scenario_key}")

    sim_res = generate_market_scenarios(
        df_params=df_p,
        corr_matrix=df_corr_base,
        s0=s0_series,
        n_scenarios=n_scenarios,
        seed=seed,
        mode="terminal_1step",
        var_order=ALL_MARKET_COLS,
    )

    s0_dict = {col: float(s0_series[col]) for col in ALL_MARKET_COLS}
    bank = build_scenario_bank(
        market_scenarios=sim_res["scenarios_market"],
        log_returns=sim_res["scenarios_log_returns"],
        market_cols=ALL_MARKET_COLS,
        s0_dict=s0_dict,
        instruments=INSTRUMENTS,
    )

    # Hitung baseline tau dan eta dari w0 untuk kedua definisi biaya
    eval_gross = PortfolioEvaluator(cost_matrix=bank["cost_gross"])
    base_gross = eval_gross.set_baseline(W0)

    eval_interest = PortfolioEvaluator(cost_matrix=bank["cost_interest"])
    base_interest = eval_interest.set_baseline(W0)

    return {
        "scenario_key": scenario_key,
        "label": spec["label"],
        "bank": bank,
        "df_params": df_p,
        "base_gross": base_gross,
        "base_interest": base_interest,
    }


# ==============================================================================
# 2. Worker Optimasi PSO
# ==============================================================================

def _run_single_drift_pso(args: Tuple) -> Dict[str, Any]:
    """Mengeksekusi satu run PSO pada bank skenario drift tertentu."""
    scenario_key, config_id, rep, seed, budget, cost_mat, tau, eta, w0_cost = args

    cost_def = "interest" if "interest" in config_id else "gross"
    is_djppr = "djppr" in config_id
    lb = LB_DJPPR if is_djppr else LB_FREE
    ub = UB_DJPPR if is_djppr else UB_FREE

    evaluator = PortfolioEvaluator(
        cost_matrix=cost_mat,
        tau=tau,
        eta=eta,
    )

    opt = ParticleSwarmOptimizer(check_interval=250)

    t0 = time.perf_counter()
    res = opt.run(evaluator=evaluator, lb=lb, ub=ub, budget=budget, rng=seed)
    t_elapsed = time.perf_counter() - t0

    final_eval = evaluator.evaluate(res.best_w)
    best_cost = float(res.best_cost)
    savings_pct = ((w0_cost - best_cost) / w0_cost) * 100.0 if w0_cost > 0 else 0.0

    slack_j = eta - float(final_eval["j_mccar"])
    slack_r = tau - float(final_eval["ccar"])

    # Cek batas aktif (|slack| <= 1e-6)
    is_j_active = abs(slack_j) <= 1e-5
    is_r_active = abs(slack_r) <= 1e-5

    record = {
        "scenario": scenario_key,
        "config_id": config_id,
        "cost_def": cost_def,
        "boundary": "djppr" if is_djppr else "free",
        "rep": rep,
        "seed": seed,
        "w0_cost": float(w0_cost),
        "best_cost": best_cost,
        "savings_pct": savings_pct,
        "ccar": float(final_eval["ccar"]),
        "j_mccar": float(final_eval["j_mccar"]),
        "tau_limit": float(tau),
        "eta_limit": float(eta),
        "slack_J": slack_j,
        "slack_R": slack_r,
        "is_j_active": is_j_active,
        "is_r_active": is_r_active,
        "time_seconds": round(t_elapsed, 4),
    }

    # Simpan bobot optimal w_1 s.d. w_7
    for idx, inst in enumerate(INSTRUMENT_NAMES):
        record[f"w_{inst}"] = float(res.best_w[idx])

    return record


def run_drift_sensitivity_experiments(
    drift_banks: Dict[str, Dict[str, Any]],
    replications: int = 10,
    budget: int = 25000,
    n_workers: int = 8,
) -> pd.DataFrame:
    """Menjalankan eksperimen sensitivitas drift untuk seluruh kombinasi."""
    logger.info("Menjalankan Optimasi PSO pada 4 Skenario Drift...")
    configs = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    tasks = []
    base_seed = 42

    for skey, sdata in drift_banks.items():
        bank = sdata["bank"]
        for cid in configs:
            cost_def = "interest" if "interest" in cid else "gross"
            cost_mat = bank["cost_interest"] if cost_def == "interest" else bank["cost_gross"]
            base_info = sdata["base_interest"] if cost_def == "interest" else sdata["base_gross"]
            tau = base_info["tau"]
            eta = base_info["eta"]
            w0_cost = base_info["mean_cost"]

            for r in range(1, replications + 1):
                seed = base_seed + r
                tasks.append((skey, cid, r, seed, budget, cost_mat, tau, eta, w0_cost))

    logger.info("Total tugas sensitivitas drift: %d (workers=%d)", len(tasks), n_workers)
    results = []
    if n_workers > 1:
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            future_to_task = {executor.submit(_run_single_drift_pso, t): t for t in tasks}
            done_count = 0
            for future in as_completed(future_to_task):
                res = future.result()
                results.append(res)
                done_count += 1
                if done_count % 20 == 0 or done_count == len(tasks):
                    logger.info("Progress sensitivitas drift: %d/%d (%.1f%%) selesai", done_count, len(tasks), done_count / len(tasks) * 100)
    else:
        for t in tasks:
            results.append(_run_single_drift_pso(t))

    df = pd.DataFrame(results)
    return df


# ==============================================================================
# 3. Studi Sensitivitas Jendela Data D1-B (Spline vs Intersection)
# ==============================================================================

def run_spline_vs_intersection_study(
    df_params_inter: pd.DataFrame,
    df_corr_inter: pd.DataFrame,
    s0_inter: pd.Series,
    spline_path: Path,
    replications: int = 10,
    budget: int = 25000,
    n_workers: int = 4,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Membandingkan parameter pasar dan optimasi portofolio antara Spline dan Intersection."""
    logger.info("Menjalankan Studi Sensitivitas Jendela Data D1-B (Spline vs Intersection)...")

    df_spline = pd.read_csv(spline_path)
    lr_spline = compute_log_returns(df_spline, exclude_gap=False)
    df_params_spline = estimate_gbm_params(lr_spline, days_per_year=252)
    df_corr_spline = compute_correlation_matrix(lr_spline)

    # Ambil S0 dari baris terakhir spline
    last_row_spline = df_spline.iloc[-1]
    s0_spline = pd.Series({c: float(last_row_spline[c]) for c in ALL_MARKET_COLS})

    # Perbandingan parameter pasar
    comp_records = []
    for var in ALL_MARKET_COLS:
        p_int = df_params_inter[df_params_inter["variable"] == var].iloc[0]
        p_spl = df_params_spline[df_params_spline["variable"] == var].iloc[0]
        comp_records.append({
            "variable": var,
            "mu_ann_intersection": p_int["mu_annual"],
            "mu_ann_spline": p_spl["mu_annual"],
            "diff_mu_pct": ((p_spl["mu_annual"] - p_int["mu_annual"]) / abs(p_int["mu_annual"])) * 100.0 if abs(p_int["mu_annual"]) > 1e-12 else 0.0,
            "sigma_ann_intersection": p_int["sigma_annual"],
            "sigma_ann_spline": p_spl["sigma_annual"],
            "diff_sigma_pct": ((p_spl["sigma_annual"] - p_int["sigma_annual"]) / p_int["sigma_annual"]) * 100.0,
            "n_obs_intersection": p_int["n_obs"],
            "n_obs_spline": p_spl["n_obs"],
        })

    # Tambahkan korelasi khusus EUR_7Y vs EUR_10Y
    r_eur_int = float(df_corr_inter.loc["IR_EUR_7Y", "IR_EUR_10Y"])
    r_eur_spl = float(df_corr_spline.loc["IR_EUR_7Y", "IR_EUR_10Y"])

    df_param_comp = pd.DataFrame(comp_records)

    # 2. Bangkitkan bank skenario Spline (N=5.000, seed 42)
    sim_spline = generate_market_scenarios(
        df_params=df_params_spline,
        corr_matrix=df_corr_spline,
        s0=s0_spline,
        n_scenarios=5000,
        seed=42,
        mode="terminal_1step",
        var_order=ALL_MARKET_COLS,
    )
    s0_spl_dict = {col: float(s0_spline[col]) for col in ALL_MARKET_COLS}
    bank_spline = build_scenario_bank(
        market_scenarios=sim_spline["scenarios_market"],
        log_returns=sim_spline["scenarios_log_returns"],
        market_cols=ALL_MARKET_COLS,
        s0_dict=s0_spl_dict,
        instruments=INSTRUMENTS,
    )

    eval_spl_gross = PortfolioEvaluator(cost_matrix=bank_spline["cost_gross"])
    base_spl_gross = eval_spl_gross.set_baseline(W0)

    eval_spl_interest = PortfolioEvaluator(cost_matrix=bank_spline["cost_interest"])
    base_spl_interest = eval_spl_interest.set_baseline(W0)

    # 3. Jalankan optimasi PSO pada bank Spline
    tasks = []
    configs = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
    for cid in configs:
        cost_def = "interest" if "interest" in cid else "gross"
        cost_mat = bank_spline["cost_interest"] if cost_def == "interest" else bank_spline["cost_gross"]
        base_info = base_spl_interest if cost_def == "interest" else base_spl_gross
        for r in range(1, replications + 1):
            seed = 42 + r
            tasks.append(("spline_d1b", cid, r, seed, budget, cost_mat, base_info["tau"], base_info["eta"], base_info["mean_cost"]))

    logger.info("Menjalankan optimasi PSO untuk varian Spline (%d tugas)...", len(tasks))
    results_spline = []
    if n_workers > 1:
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            future_to_task = {executor.submit(_run_single_drift_pso, t): t for t in tasks}
            for future in as_completed(future_to_task):
                results_spline.append(future.result())
    else:
        for t in tasks:
            results_spline.append(_run_single_drift_pso(t))

    df_opt_spline = pd.DataFrame(results_spline)
    return df_param_comp, df_opt_spline


# ==============================================================================
# 4. Pembangkitan Grafik Visualisasi Gaya D9
# ==============================================================================

def generate_sensitivity_figures(
    df_drift: pd.DataFrame,
    df_spline_opt: pd.DataFrame,
    out_dir: Path,
):
    """Membangkitkan visualisasi grafik standar tesis D9."""
    logger.info("Membangkitkan Grafik Visualisasi Sensitivitas Gaya D9...")
    apply_thesis_style()

    scenarios = ["historical", "fx_zero", "martingale", "shrinkage_half"]
    scen_labels = [
        "Basis (Historis)",
        r"$\mu_{\mathrm{kurs}} = 0$",
        "Martingale",
        r"$\mu \times 0{,}5$",
    ]

    # -------------------------------------------------------------------------
    # Grafik 1: Pergeseran Bobot 7 Instrumen Antar-Skenario Drift (interest_free & gross_free)
    # -------------------------------------------------------------------------
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    for ax, cid, title in [
        (ax1, "interest_free", "Biaya Bunga Bebas (interest_free)"),
        (ax2, "gross_free", "Biaya Bruto Bebas (gross_free)"),
    ]:
        sub = df_drift[df_drift["config_id"] == cid]
        weights_mean = []
        for skey in scenarios:
            sub_s = sub[sub["scenario"] == skey]
            w_cols = [f"w_{inst}" for inst in INSTRUMENT_NAMES]
            w_mean = sub_s[w_cols].mean().values
            weights_mean.append(w_mean)

        weights_mat = np.array(weights_mean)  # (4 scenarios, 7 instruments)
        bottom = np.zeros(len(scenarios))
        x_pos = np.arange(len(scenarios))

        for inst_idx in range(len(INSTRUMENT_NAMES)):
            vals = weights_mat[:, inst_idx]
            ax.bar(
                x_pos,
                vals,
                bottom=bottom,
                label=INSTRUMENT_DISPLAY_NAMES[inst_idx],
                color=INSTRUMENT_COLORS[inst_idx],
                hatch=INSTRUMENT_HATCHES[inst_idx],
                edgecolor="#333333",
                linewidth=0.6,
                alpha=0.9,
                width=0.55,
            )
            bottom += vals

        ax.set_xticks(x_pos)
        ax.set_xticklabels(scen_labels)
        ax.set_title(title)
        ax.set_ylabel("Proporsi Alokasi Bobot")
        ax.set_ylim(0, 1.02)
        ax.grid(axis="y", linestyle=":", alpha=0.6)

    ax2.legend(loc="upper right", bbox_to_anchor=(1.35, 1.0), title="Instrumen Utang")
    plt.tight_layout()
    save_figure(fig, out_dir / "fig_drift_sensitivity_weights")

    # -------------------------------------------------------------------------
    # Grafik 2: Perbandingan Penghematan Biaya (%) Antar-Skenario Drift
    # -------------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    configs = ["interest_free", "interest_djppr", "gross_free", "gross_djppr"]
    c_labels = ["Interest Free", "Interest DJPPR", "Gross Free", "Gross DJPPR"]
    colors = ["#1f77b4", "#aec7e8", "#2ca02c", "#98df8a"]

    # Panel A: Biaya Bunga
    ax = axes[0]
    sub_if = df_drift[df_drift["cost_def"] == "interest"]
    for idx, (cid, clbl, col) in enumerate(zip(["interest_free", "interest_djppr"], ["Interest Free", "Interest DJPPR"], ["#1f77b4", "#ff7f0e"])):
        sub_c = sub_if[sub_if["config_id"] == cid]
        means = [sub_c[sub_c["scenario"] == s]["savings_pct"].mean() for s in scenarios]
        stds = [sub_c[sub_c["scenario"] == s]["savings_pct"].std() for s in scenarios]
        x_shift = np.arange(len(scenarios)) + (idx - 0.5) * 0.35
        ax.bar(x_shift, means, width=0.32, yerr=stds, capsize=4, label=clbl, color=col, alpha=0.85, edgecolor="#333333")

    ax.set_xticks(np.arange(len(scenarios)))
    ax.set_xticklabels(scen_labels)
    ax.set_title("Penghematan Biaya Bunga (%)")
    ax.set_ylabel("Penghematan terhadap w0 (%)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()

    # Panel B: Biaya Bruto
    ax = axes[1]
    sub_gf = df_drift[df_drift["cost_def"] == "gross"]
    for idx, (cid, clbl, col) in enumerate(zip(["gross_free", "gross_djppr"], ["Gross Free", "Gross DJPPR"], ["#2ca02c", "#d62728"])):
        sub_c = sub_gf[sub_gf["config_id"] == cid]
        means = [sub_c[sub_c["scenario"] == s]["savings_pct"].mean() for s in scenarios]
        stds = [sub_c[sub_c["scenario"] == s]["savings_pct"].std() for s in scenarios]
        x_shift = np.arange(len(scenarios)) + (idx - 0.5) * 0.35
        ax.bar(x_shift, means, width=0.32, yerr=stds, capsize=4, label=clbl, color=col, alpha=0.85, edgecolor="#333333")

    ax.set_xticks(np.arange(len(scenarios)))
    ax.set_xticklabels(scen_labels)
    ax.set_title("Penghematan Biaya Bruto (%)")
    ax.set_ylabel("Penghematan terhadap w0 (%)")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()

    plt.tight_layout()
    save_figure(fig, out_dir / "fig_drift_savings_comparison")

    # -------------------------------------------------------------------------
    # Grafik 3: Trade-off dan Disparitas Biaya Bruto vs Bunga
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 4.8))

    # Scatter perbandingan penghematan Gross vs Interest untuk tiap skenario
    markers = ["o", "s", "^", "D"]
    for s_idx, (skey, slbl, m) in enumerate(zip(scenarios, scen_labels, markers)):
        sub_s = df_drift[df_drift["scenario"] == skey]
        sav_gf = sub_s[sub_s["config_id"] == "gross_free"]["savings_pct"].values
        sav_if = sub_s[sub_s["config_id"] == "interest_free"]["savings_pct"].values
        ax.scatter(sav_gf, sav_if, label=slbl, marker=m, s=60, alpha=0.8, edgecolor="#333333")

    ax.set_xlabel("Penghematan Biaya Bruto Bebas (%)")
    ax.set_ylabel("Penghematan Biaya Bunga Bebas (%)")
    ax.set_title("Disparitas Penghematan: Biaya Bruto vs Biaya Bunga")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(title="Skenario Drift")

    plt.tight_layout()
    save_figure(fig, out_dir / "fig_cost_definitions_tradeoff")


# ==============================================================================
# 5. Fungsi Utama Orkestrasi
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description="Analisis Sensitivitas Drift GBM, D1-B, dan Definisi Biaya")
    parser.add_argument("--smoke", action="store_true", help="Mode uji cepat (2 replikasi, 500 evaluasi)")
    parser.add_argument("--reps", type=int, default=10, help="Jumlah replikasi per kombinasi (default: 10)")
    parser.add_argument("--workers", type=int, default=8, help="Jumlah worker paralel (default: 8)")
    args = parser.parse_args()

    reps = 2 if args.smoke else args.reps
    budget = 500 if args.smoke else 25000
    n_scenarios = 1000 if args.smoke else 5000

    out_dir = Path("results/sensitivity/drift")
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Muat parameter dasar varian intersection
    df_params_inter = pd.read_csv("data/processed/gbm_params_intersection.csv")
    df_corr_inter = pd.read_csv("data/processed/corr_intersection.csv", index_col=0)
    df_market_inter = pd.read_csv("data/processed/market_2017-07-03_2025-11-24_intersection.csv")
    last_row_inter = df_market_inter.iloc[-1]
    s0_inter = pd.Series({c: float(last_row_inter[c]) for c in ALL_MARKET_COLS})

    # 2. Bangkitkan 4 bank skenario drift
    logger.info("Membangkitkan 4 bank skenario drift GBM...")
    drift_banks = {}
    for skey in DRIFT_SCENARIOS:
        drift_banks[skey] = build_drift_scenario_bank(
            scenario_key=skey,
            df_params_base=df_params_inter,
            df_corr_base=df_corr_inter,
            s0_series=s0_inter,
            n_scenarios=n_scenarios,
        )

    # 3. Jalankan optimasi PSO pada 4 skenario drift
    df_drift = run_drift_sensitivity_experiments(
        drift_banks=drift_banks,
        replications=reps,
        budget=budget,
        n_workers=args.workers,
    )

    # Simpan ringkasan komparasi skenario drift
    drift_csv = out_dir / "drift_scenarios_comparison.csv"
    drift_summary = df_drift.groupby(["scenario", "config_id"])[
        ["savings_pct", "best_cost", "slack_J", "slack_R", "time_seconds"] + [f"w_{i}" for i in INSTRUMENT_NAMES]
    ].agg(["mean", "median", "std"])
    drift_summary.to_csv(drift_csv)
    df_drift.to_csv(out_dir / "drift_scenarios_all_runs.csv", index=False)
    logger.info("Hasil skenario drift disimpan ke: %s", drift_csv)

    # 4. Studi sensitivitas varian Spline vs Intersection (D1-B)
    spline_file = Path("data/processed/market_2017-07-03_2025-11-24_spline.csv")
    df_param_comp, df_opt_spline = run_spline_vs_intersection_study(
        df_params_inter=df_params_inter,
        df_corr_inter=df_corr_inter,
        s0_inter=s0_inter,
        spline_path=spline_file,
        replications=reps,
        budget=budget,
        n_workers=args.workers,
    )
    df_param_comp.to_csv(out_dir / "data_window_spline_vs_intersection.csv", index=False)
    df_opt_spline.to_csv(out_dir / "data_window_spline_pso_runs.csv", index=False)
    logger.info("Hasil komparasi Spline vs Intersection disimpan!")

    # 5. Ringkasan Sensitivitas Definisi Biaya (Gross vs Interest)
    cost_comp = df_drift.groupby(["cost_def", "scenario", "boundary"])[
        ["savings_pct", "best_cost", "slack_J", "w_JPY_Fixed_5Y", "w_JPY_Fixed_10Y", "w_USD_Fixed_5Y"]
    ].agg(["mean", "median", "std"])
    cost_comp_csv = out_dir / "cost_definitions_comparison.csv"
    cost_comp.to_csv(cost_comp_csv)
    logger.info("Hasil komparasi definisi biaya disimpan ke: %s", cost_comp_csv)

    # 6. Pembangkitan Grafik Visualisasi
    generate_sensitivity_figures(df_drift, df_opt_spline, out_dir)
    logger.info("Seluruh grafik visualisasi berhasil diterbitkan di %s!", out_dir)


if __name__ == "__main__":
    main()
