"""Grafik diagnosis KMA Tahap 18 (gaya D9: PDF + PNG 300 dpi, serif, garis/marker/arsir)."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mccar_kma.viz.style import ALGO_COLORS, ALGO_MARKERS, ALGO_STYLES, apply_thesis_style, save_figure

CONFIGS = ("gross_free", "gross_djppr", "interest_free", "interest_djppr")
MAIN_ALGOS = ("kma", "ga", "pso")
ALGO_SHORT = {"kma": "KMA", "ga": "GA", "pso": "PSO"}
HATCHES = ["", "//", "\\\\", "xx", "..", "++", "**", "OO", "--", "||", "oo", "//\\\\"]
VARIANT_GREYS = plt.cm.Greys(np.linspace(0.25, 0.85, 12))


def _color(name: str, i: int = 0):
    return ALGO_COLORS.get(name, VARIANT_GREYS[i % len(VARIANT_GREYS)])


def _boxplot(ax, data: List[np.ndarray], labels: List[str], colors: List[Any], hatches: List[str]) -> None:
    data = [np.asarray(d, dtype=float)[np.isfinite(d)] if len(d) else np.array([np.nan]) for d in data]
    bp = ax.boxplot(data, patch_artist=True, widths=0.6, showfliers=True,
                    flierprops={"marker": ".", "markersize": 3, "alpha": 0.6})
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels, rotation=30, ha="right")
    for patch, c, h in zip(bp["boxes"], colors, hatches):
        patch.set_facecolor(c)
        patch.set_alpha(0.75)
        patch.set_hatch(h)
        patch.set_edgecolor("#222222")
    for med in bp["medians"]:
        med.set_color("black")


# ------------------------------------------------------------------------------
def fig_benchmark_fidelity(df: pd.DataFrame, ref_cfg: Dict[str, Any], out_dir: Path, floor: float) -> None:
    """Median ± IQR fitness akhir per algoritma vs D; bintang = KMA Suyanto (2022) Tabel 2."""
    apply_thesis_style()
    sub = df[(~df["shifted"]) & (df["algo"].isin(MAIN_ALGOS))]
    if sub.empty:
        return
    fns = [f for f in ("sphere", "rastrigin", "rosenbrock") if f in set(sub["function"])]
    fig, axes = plt.subplots(1, len(fns), figsize=(4.3 * len(fns), 4.0))
    axes = np.atleast_1d(axes)
    dims = sorted(sub["dim"].unique())
    for ax, fn in zip(axes, fns):
        for k, algo in enumerate(MAIN_ALGOS):
            med, lo, hi = [], [], []
            for d in dims:
                x = sub[(sub["function"] == fn) & (sub["algo"] == algo) & (sub["dim"] == d)]["best_fitness"].to_numpy()
                x = np.maximum(x, floor) if len(x) else np.array([np.nan])
                med.append(np.median(x)); lo.append(np.percentile(x, 25)); hi.append(np.percentile(x, 75))
            xs = np.arange(len(dims)) + (k - 1) * 0.12
            med, lo, hi = map(np.asarray, (med, lo, hi))
            ax.errorbar(xs, med, yerr=[med - lo, hi - med], color=_color(algo), marker=ALGO_MARKERS[algo],
                        linestyle=ALGO_STYLES[algo], capsize=3, label=ALGO_SHORT[algo])
        ref_dim = int(ref_cfg["dim"])
        if ref_dim in dims:
            xr = dims.index(ref_dim)
            for algo, mk in (("kma", "*"), ("ga", "P")):
                val = max(float(ref_cfg[algo][fn]["avg"]), floor)
                ax.scatter([xr + 0.3], [val], marker=mk, s=110, color=_color(algo), edgecolor="black", zorder=5,
                           label=f"{ALGO_SHORT[algo]} Suyanto (2022), D={ref_dim}")
        ax.set_yscale("log")
        ax.set_xticks(range(len(dims)))
        ax.set_xticklabels([f"D={d}" for d in dims])
        ax.set_title(fn.capitalize())
        ax.set_ylabel(f"Fitness akhir (median, IQR; lantai {floor:g})")
    axes[0].legend(fontsize=7.5, loc="best")
    fig.suptitle("Uji fidelitas benchmark (25.000 evaluasi, 30 replikasi)", fontsize=11)
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_benchmark_fidelity")


def fig_benchmark_shift(df: pd.DataFrame, out_dir: Path, floor: float) -> None:
    """Median fitness asli vs tergeser (uji bias titik-asal, H2)."""
    apply_thesis_style()
    sh = df[df["set"] == "shifted"]
    if sh.empty:
        return
    algos = [a for a in ("kma", "kma_paper_all", "ga", "pso") if a in set(sh["algo"])]
    base = df[(~df["shifted"])]
    fns = ("sphere", "rastrigin", "rosenbrock")
    dims = sorted(sh["dim"].unique())
    fig, axes = plt.subplots(len(dims), len(fns), figsize=(4.2 * len(fns), 3.4 * len(dims)), squeeze=False)
    for r, d in enumerate(dims):
        for c, fn in enumerate(fns):
            ax = axes[r, c]
            xs = np.arange(len(algos))
            for off, (frame, hatch, lab) in enumerate(((base, "", "asli"), (sh, "//", "tergeser"))):
                vals = []
                for a in algos:
                    x = frame[(frame["function"] == fn) & (frame["dim"] == d) & (frame["algo"] == a)]["best_fitness"]
                    vals.append(max(float(np.median(x)), floor) if len(x) else np.nan)
                ax.bar(xs + (off - 0.5) * 0.38, vals, width=0.38, hatch=hatch, edgecolor="black",
                       color=[_color(a.split("_")[0] if a in MAIN_ALGOS else "kma") for a in algos],
                       alpha=0.55 if off else 0.9, label=lab)
            ax.set_yscale("log")
            ax.set_xticks(xs)
            ax.set_xticklabels([a.replace("kma_", "KMA ").replace("kma", "KMA").upper() if a in MAIN_ALGOS else a.replace("kma_", "KMA-") for a in algos], rotation=20)
            ax.set_title(f"{fn.capitalize()}, D={d}")
            if c == 0:
                ax.set_ylabel("Median fitness akhir")
    axes[0, 0].legend()
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_benchmark_shift")


def fig_benchmark_variants(df: pd.DataFrame, out_dir: Path, floor: float) -> None:
    """Distribusi fitness akhir varian KMA K1-K4 vs default (H1)."""
    apply_thesis_style()
    var = df[(df["set"].isin(["variants", "stage_a"])) & (~df["shifted"]) & (df["algo"].str.startswith("kma"))]
    if var["algo"].nunique() < 2:
        return
    algos = ["kma"] + sorted(a for a in var["algo"].unique() if a != "kma")
    dims = sorted(var[var["algo"] != "kma"]["dim"].unique())
    fns = ("sphere", "rastrigin", "rosenbrock")
    fig, axes = plt.subplots(len(dims), len(fns), figsize=(4.4 * len(fns), 3.6 * len(dims)), squeeze=False)
    for r, d in enumerate(dims):
        for c, fn in enumerate(fns):
            ax = axes[r, c]
            data = [np.maximum(var[(var["function"] == fn) & (var["dim"] == d) & (var["algo"] == a)]["best_fitness"].to_numpy(), floor) for a in algos]
            _boxplot(ax, data, [a.replace("kma_", "") if a != "kma" else "default" for a in algos],
                     [_color("kma") if a == "kma" else VARIANT_GREYS[i] for i, a in enumerate(algos)],
                     [HATCHES[i % len(HATCHES)] for i in range(len(algos))])
            ax.set_yscale("log")
            ax.set_title(f"{fn.capitalize()}, D={d}")
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_benchmark_variants")


# ------------------------------------------------------------------------------
def _time_grid(timing: pd.DataFrame, cid: str, algo: str, evals: np.ndarray) -> Optional[np.ndarray]:
    sub = timing[(timing["config_id"] == cid) & (timing["algo"] == algo)]
    if sub.empty:
        return None
    med = sub.groupby("evaluation")["seconds"].median()
    xe = med.index.to_numpy(dtype=float)
    t = np.interp(evals, xe, med.to_numpy(dtype=float))
    return np.where((evals >= xe.min()) & (evals <= xe.max()), t, np.nan)


def fig_convergence(df_main: pd.DataFrame, curves: Dict, timing: pd.DataFrame, out_dir: Path) -> None:
    """Gap biaya (%) vs evaluasi dan vs detik (1 worker, skala sama): median, rata-rata, pita IQR."""
    apply_thesis_style()
    evals = np.arange(250, 25001, 250, dtype=float)
    ref = df_main.groupby("config_id")["ref_best_cost"].first()

    def draw(ax, cid, use_time):
        for algo in MAIN_ALGOS:
            if (cid, algo) not in curves:
                continue
            gap = (curves[(cid, algo)] - ref[cid]) / ref[cid] * 100.0
            x = evals if not use_time else _time_grid(timing, cid, algo, evals)
            if x is None:
                continue
            med = np.nanmedian(gap, axis=0)
            mean = np.nanmean(gap, axis=0)
            q25, q75 = np.nanpercentile(gap, 25, axis=0), np.nanpercentile(gap, 75, axis=0)
            ax.plot(x, med, color=_color(algo), linestyle="-", label=f"{ALGO_SHORT[algo]} median")
            ax.plot(x, mean, color=_color(algo), linestyle=":", linewidth=1.1, label=f"{ALGO_SHORT[algo]} rata-rata")
            ax.fill_between(x, q25, q75, color=_color(algo), alpha=0.18)
            if not use_time:
                ax.plot(evals[[19, 39, 99]], med[[19, 39, 99]], linestyle="none", marker=ALGO_MARKERS[algo],
                        color=_color(algo))
        ax.set_yscale("symlog", linthresh=1e-4)
        ax.set_ylabel("Gap biaya ke terbaik (%)")
        if not use_time:
            for e in (5000, 10000, 25000):
                ax.axvline(e, color="#888888", linestyle="--", linewidth=0.7)
            ax.set_xlabel("Evaluasi fungsi")
        else:
            ax.set_xlabel("Waktu dinding, 1 worker (detik)")

    for cid in CONFIGS:
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.3), sharey=True)
        draw(a1, cid, False)
        draw(a2, cid, True)
        a1.set_title(f"{cid}: vs evaluasi")
        a2.set_title(f"{cid}: vs waktu (skala sama)")
        a1.legend(fontsize=7, ncol=2)
        fig.tight_layout()
        save_figure(fig, out_dir / f"fig_kma_convergence_{cid}")

    for use_time, stem in ((False, "fig_kma_convergence_all"), (True, "fig_kma_convergence_time_all")):
        fig, axes = plt.subplots(2, 2, figsize=(11.5, 8.0))
        for ax, cid in zip(axes.ravel(), CONFIGS):
            draw(ax, cid, use_time)
            ax.set_title(cid)
        axes[0, 0].legend(fontsize=7, ncol=2)
        fig.tight_layout()
        save_figure(fig, out_dir / stem)


def fig_slack_and_phase(df_main: pd.DataFrame, out_dir: Path, floor: float) -> None:
    """Slack relatif J dan perbaikan biaya 5k→25k per run (360 run)."""
    apply_thesis_style()
    fig, axes = plt.subplots(2, 4, figsize=(14, 7.0))
    for c, cid in enumerate(CONFIGS):
        g = df_main[df_main["config_id"] == cid]
        data = [np.maximum(g[g["algo"] == a]["slack_J_rel"].to_numpy(), floor) for a in MAIN_ALGOS]
        _boxplot(axes[0, c], data, [ALGO_SHORT[a] for a in MAIN_ALGOS], [_color(a) for a in MAIN_ALGOS], ["", "//", "\\\\"])
        axes[0, c].set_yscale("log")
        axes[0, c].set_title(cid)
        data = [np.maximum(g[g["algo"] == a]["improve_pct_5k_25k"].to_numpy(), floor) for a in MAIN_ALGOS]
        _boxplot(axes[1, c], data, [ALGO_SHORT[a] for a in MAIN_ALGOS], [_color(a) for a in MAIN_ALGOS], ["", "//", "\\\\"])
        axes[1, c].set_yscale("log")
    axes[0, 0].set_ylabel(r"Slack relatif $(\eta-J)/\eta$")
    axes[1, 0].set_ylabel("Perbaikan biaya 5k→25k (%)")
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_slack_phase")


def fig_acceptance(gen: pd.DataFrame, out_dir: Path) -> None:
    """Rasio penerimaan Big Male dan norma langkah relatif per generasi (H3)."""
    apply_thesis_style()
    if gen.empty:
        return
    fig, axes = plt.subplots(2, 4, figsize=(14, 6.5), sharex=True)
    bins = np.arange(0, 25001, 500)
    for c, cid in enumerate(CONFIGS):
        g = gen[gen["config_id"] == cid].copy()
        if g.empty:
            continue
        g["bin"] = np.digitize(g["eval_end"], bins)
        g["acc"] = g["bm_accepted"] / g["bm_attempts"].clip(lower=1)
        agg = g.groupby("bin").agg(e=("eval_end", "median"), acc=("acc", "mean"), step=("bm_step_norm_median", "median"))
        axes[0, c].plot(agg["e"], agg["acc"], color=_color("kma"), marker="o", markersize=2.5)
        axes[0, c].set_title(cid)
        axes[1, c].plot(agg["e"], agg["step"], color=_color("kma"), linestyle="--", marker="s", markersize=2.5)
        axes[1, c].set_yscale("log")
        axes[1, c].axhline(1.0, color="#888888", linewidth=0.7)
        for ax in axes[:, c]:
            ax.axvline(5000, color="#d62728", linestyle=":", linewidth=0.9)
        axes[1, c].set_xlabel("Evaluasi")
    axes[0, 0].set_ylabel("Penerimaan Big Male")
    axes[1, 0].set_ylabel(r"$\|\Delta\|/\|ub-lb\|$ (median)")
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_acceptance")


def fig_projection(blocks: pd.DataFrame, out_dir: Path) -> None:
    """Fraksi kandidat melanggar J dan jarak proyeksi per blok 250 eval (H5)."""
    apply_thesis_style()
    if blocks.empty:
        return
    metrics = [("frac_vJ_pos", r"Fraksi kandidat $v_J>0$", False),
               ("mean_proj_dist", "Jarak raw→proyeksi (rata-rata)", True),
               ("frac_near_boundary", r"Fraksi layak dgn slack rel. $\leq 10^{-3}$", False)]
    fig, axes = plt.subplots(len(metrics), 4, figsize=(14, 9.5), sharex=True)
    for c, cid in enumerate(CONFIGS):
        for r, (col, lab, logy) in enumerate(metrics):
            ax = axes[r, c]
            for algo in MAIN_ALGOS:
                g = blocks[(blocks["config_id"] == cid) & (blocks["algo"] == algo)]
                if g.empty:
                    continue
                m = g.groupby("eval_end")[col].median()
                ax.plot(m.index, m.to_numpy(), color=_color(algo), linestyle=ALGO_STYLES[algo], label=ALGO_SHORT[algo])
            if logy:
                ax.set_yscale("symlog", linthresh=1e-6)
            if c == 0:
                ax.set_ylabel(lab)
            if r == 0:
                ax.set_title(cid)
        axes[-1, c].set_xlabel("Evaluasi")
    axes[0, 0].legend()
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_projection")


def fig_ablation(df: pd.DataFrame, out_dir: Path) -> None:
    """Gap biaya (%) per varian KMA pada portofolio (H3-H5)."""
    apply_thesis_style()
    if df.empty:
        return
    algos = ["kma_default"] + sorted(a for a in df["algo"].unique() if a != "kma_default")
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    for ax, cid in zip(axes.ravel(), CONFIGS):
        g = df[df["config_id"] == cid]
        data = [g[g["algo"] == a]["gap_pct"].to_numpy() for a in algos]
        _boxplot(ax, data, [a.replace("kma_", "") for a in algos],
                 [_color("kma") if a == "kma_default" else VARIANT_GREYS[i] for i, a in enumerate(algos)],
                 [HATCHES[i % len(HATCHES)] for i in range(len(algos))])
        ax.set_yscale("symlog", linthresh=1e-4)
        ax.set_title(cid)
        ax.set_ylabel("Gap biaya ke terbaik 360 run (%)")
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_ablation")


def fig_time_profile(profile: pd.DataFrame, out_dir: Path) -> None:
    """Pembagian waktu 1 run (cProfile, 1 worker): evaluator / proyeksi / RNG / sisa (H6)."""
    apply_thesis_style()
    if profile.empty:
        return
    comps = [("evaluator_seconds", "Evaluator", "//"), ("projection_seconds", "Proyeksi", "\\\\"),
             ("rng_seconds", "RNG skalar/vektor", "xx"), ("other_seconds", "Sisa (loop optimizer)", "..")]
    labels = [f"{r.config_id}\n{ALGO_SHORT[r.algo]}" for r in profile.itertuples()]
    fig, ax = plt.subplots(figsize=(13, 4.8))
    bottom = np.zeros(len(profile))
    greys = plt.cm.Greys(np.linspace(0.3, 0.8, len(comps)))
    for (col, lab, h), colr in zip(comps, greys):
        v = profile[col].to_numpy()
        ax.bar(np.arange(len(profile)), v, bottom=bottom, label=lab, hatch=h, color=colr, edgecolor="black")
        bottom += v
    ax.set_xticks(np.arange(len(profile)))
    ax.set_xticklabels(labels, fontsize=7.5)
    ax.set_ylabel("Detik (cProfile, termasuk overhead profiler)")
    ax.legend()
    fig.tight_layout()
    save_figure(fig, out_dir / "fig_kma_time_profile")
