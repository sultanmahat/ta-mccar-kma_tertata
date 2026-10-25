"""Grafik gaya D9 untuk studi stabilitas batas risiko (PDF vektor + PNG 300 dpi).

Label Bahasa Indonesia, font serif, warna algoritma konsisten (PSO hijau, GA oranye).
Semua fungsi menerima DataFrame hasil `analysis.limit_stability` dan menulis ke `out_dir`.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mccar_kma.viz.style import (
    ALGO_COLORS,
    INSTRUMENT_COLORS,
    INSTRUMENT_DISPLAY_NAMES,
    apply_thesis_style,
    save_figure,
)

CONFIG_ORDER = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
CONFIG_LABELS = {
    "gross_free": "Bruto, bebas",
    "gross_djppr": "Bruto, DJPPR",
    "interest_free": "Bunga, bebas",
    "interest_djppr": "Bunga, DJPPR",
}
ALGO_NAMES = {"pso": "PSO", "ga": "GA"}


def _configs_present(df: pd.DataFrame) -> List[str]:
    return [c for c in CONFIG_ORDER if c in set(df["config_id"])]


def fig_limits_distribution(
    df_limits: pd.DataFrame, limits_summary: pd.DataFrame, out_dir: Path
) -> None:
    """Sebaran eta_b dan tau_b antar bank dengan penanda bank-42 dan bank validasi."""
    apply_thesis_style()
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 6.4))
    panels = [
        ("gross", "eta", r"$\eta$ biaya bruto"),
        ("gross", "tau", r"$\tau$ biaya bruto"),
        ("interest", "eta", r"$\eta$ biaya bunga"),
        ("interest", "tau", r"$\tau$ biaya bunga"),
    ]
    for ax, (cost_def, metric, title) in zip(axes.ravel(), panels):
        x = df_limits.loc[df_limits["cost_definition"] == cost_def, metric].to_numpy(dtype=float)
        row = limits_summary[
            (limits_summary["cost_definition"] == cost_def) & (limits_summary["metric"] == metric)
        ].iloc[0]
        ax.hist(x, bins=min(10, max(3, len(x) // 2)), color="#b0b0b0", edgecolor="black")
        ax.plot(x, np.full_like(x, -0.15), "|", color="black", markersize=10, clip_on=False)
        ax.axvline(row["mean"], color="black", linestyle="-", linewidth=1.2, label="Rata-rata bank")
        ax.axvline(row["bank42_value"], color="#d62728", linestyle="--", linewidth=1.6,
                   label=f"Bank utama (seed 42), z = {row['bank42_z']:+.2f}")
        ax.axvline(row["valid_bank_value"], color="#9467bd", linestyle=":", linewidth=1.8,
                   label="Bank validasi (N = 20.000)")
        ax.set_title(f"{title} (CV = {row['cv_percent']:.1f}%)")
        ax.set_xlabel("Nilai batas")
        ax.set_ylabel("Jumlah bank")
        ax.legend(fontsize=7, loc="best")
    fig.tight_layout()
    save_figure(fig, Path(out_dir) / "fig_limits_distribution")
    plt.close(fig)


def fig_savings_distribution(df_runs: pd.DataFrame, summary_savings: pd.DataFrame, out_dir: Path) -> None:
    """Boxplot penghematan dalam sampel dan validasi per konfigurasi dan algoritma."""
    apply_thesis_style()
    configs = _configs_present(df_runs)
    fig, axes = plt.subplots(1, len(configs), figsize=(3.4 * len(configs), 4.4), sharey=False)
    axes = np.atleast_1d(axes)
    for ax, cid in zip(axes, configs):
        data, pos, colors = [], [], []
        p = 0.0
        for algo in ("pso", "ga"):
            for col in ("savings_in", "savings_val"):
                vals = df_runs[(df_runs["config_id"] == cid) & (df_runs["algo"] == algo)][col] * 100.0
                data.append(vals.to_numpy())
                pos.append(p)
                colors.append(ALGO_COLORS[algo])
                p += 1.0
            p += 0.6
        bp = ax.boxplot(data, positions=pos, widths=0.7, patch_artist=True, showfliers=True)
        for patch, c, i in zip(bp["boxes"], colors, range(len(colors))):
            patch.set_facecolor(c)
            patch.set_alpha(0.75)
            patch.set_hatch("//" if i % 2 == 1 else "")
        for algo in ("pso", "ga"):
            ref = summary_savings[(summary_savings["config_id"] == cid) & (summary_savings["algo"] == algo)]
            if "savings_ref_bank42_median" in ref.columns and len(ref):
                ax.axhline(ref["savings_ref_bank42_median"].iloc[0] * 100.0, color=ALGO_COLORS[algo],
                           linestyle="--", linewidth=1.2)
        ax.set_xticks([0.5, 3.1])
        ax.set_xticklabels(["PSO", "GA"])
        ax.set_title(CONFIG_LABELS[cid])
        ax.set_ylabel("Penghematan terhadap $w_0$ (%)")
    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor="#cccccc", edgecolor="black", label="Dalam sampel"),
        plt.Rectangle((0, 0), 1, 1, facecolor="#cccccc", edgecolor="black", hatch="//", label="Validasi"),
        plt.Line2D([0], [0], color="black", linestyle="--", label="Median 360 run (bank 42)"),
    ]
    fig.legend(handles=handles, loc="lower center", ncol=3, fontsize=8)
    fig.tight_layout(rect=(0, 0.07, 1, 1))
    save_figure(fig, Path(out_dir) / "fig_savings_distribution")
    plt.close(fig)


def fig_weights_by_config(summary_weights: pd.DataFrame, out_dir: Path) -> None:
    """Bobot rata-rata +- SD per instrumen antar bank (PSO dan GA)."""
    apply_thesis_style()
    configs = _configs_present(summary_weights)
    fig, axes = plt.subplots(len(configs), 1, figsize=(8.2, 2.5 * len(configs)), sharex=True)
    axes = np.atleast_1d(axes)
    x = np.arange(7)
    for ax, cid in zip(axes, configs):
        for off, algo in ((-0.17, "pso"), (0.17, "ga")):
            g = summary_weights[(summary_weights["config_id"] == cid) & (summary_weights["algo"] == algo)]
            g = g.sort_values("instrument_index")
            ax.errorbar(x + off, g["w_mean"], yerr=g["w_sd"], fmt="o", capsize=3,
                        color=ALGO_COLORS[algo], label=ALGO_NAMES[algo])
        for i in range(7):
            ax.axvspan(i - 0.4, i + 0.4, color=INSTRUMENT_COLORS[i], alpha=0.12)
        ax.set_ylabel("Bobot")
        ax.set_title(CONFIG_LABELS[cid], loc="left")
        ax.legend(fontsize=7, ncol=2, loc="upper right")
    axes[-1].set_xticks(x)
    axes[-1].set_xticklabels(INSTRUMENT_DISPLAY_NAMES, rotation=30, ha="right")
    fig.tight_layout()
    save_figure(fig, Path(out_dir) / "fig_weights_by_config")
    plt.close(fig)


def fig_feasibility(summary_feasibility: pd.DataFrame, out_dir: Path) -> None:
    """Proporsi solusi layak di validasi: batas sendiri vs batas benar (CI Clopper-Pearson)."""
    apply_thesis_style()
    configs = _configs_present(summary_feasibility)
    fig, ax = plt.subplots(figsize=(9.0, 4.2))
    width = 0.19
    labels: List[str] = []
    slot = 0
    for cid in configs:
        for algo in ("pso", "ga"):
            r = summary_feasibility[
                (summary_feasibility["config_id"] == cid) & (summary_feasibility["algo"] == algo)
            ]
            if r.empty:
                continue
            r = r.iloc[0]
            for k, (tag, hatch, shade) in enumerate((("own", "", 1.0), ("true", "//", 0.55))):
                p = r[f"prop_{tag}"]
                err = np.array([[p - r[f"cp_lo_{tag}"]], [r[f"cp_hi_{tag}"] - p]])
                ax.bar(slot + (k - 0.5) * width * 1.1, p, width, color=ALGO_COLORS[algo],
                       alpha=shade, hatch=hatch, edgecolor="black",
                       yerr=err, capsize=2)
            labels.append(f"{CONFIG_LABELS[cid]}\n{ALGO_NAMES[algo]}")
            slot += 1
    ax.set_xticks(range(slot))
    ax.set_xticklabels(labels, fontsize=7)
    ax.set_ylabel("Proporsi layak di validasi")
    ax.set_ylim(0, 1.08)
    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor="#999999", edgecolor="black", label="Batas bank sendiri"),
        plt.Rectangle((0, 0), 1, 1, facecolor="#999999", edgecolor="black", hatch="//",
                      alpha=0.55, label="Batas benar (bank validasi)"),
    ]
    ax.legend(handles=handles, fontsize=8, loc="lower left")
    fig.tight_layout()
    save_figure(fig, Path(out_dir) / "fig_feasibility_validation")
    plt.close(fig)


def fig_savings_vs_eta_error(df_runs: pd.DataFrame, out_dir: Path) -> None:
    """Penghematan dalam sampel vs galat relatif eta_b terhadap eta bank validasi."""
    apply_thesis_style()
    configs = _configs_present(df_runs)
    fig, axes = plt.subplots(1, len(configs), figsize=(3.4 * len(configs), 3.8))
    axes = np.atleast_1d(axes)
    for ax, cid in zip(axes, configs):
        for algo in ("pso", "ga"):
            g = df_runs[(df_runs["config_id"] == cid) & (df_runs["algo"] == algo)]
            xs = g["eta_error_rel"].to_numpy() * 100.0
            ys = g["savings_in"].to_numpy() * 100.0
            ax.scatter(xs, ys, s=22, color=ALGO_COLORS[algo], label=ALGO_NAMES[algo], alpha=0.85)
            if len(g) >= 3 and np.ptp(xs) > 0:
                coef = np.polyfit(xs, ys, 1)
                xx = np.linspace(xs.min(), xs.max(), 20)
                ax.plot(xx, np.polyval(coef, xx), color=ALGO_COLORS[algo], linewidth=1.0)
        ax.set_title(CONFIG_LABELS[cid])
        ax.set_xlabel(r"Galat batas $(\eta_b-\eta_v)/\eta_v$ (%)")
        ax.set_ylabel("Penghematan dalam sampel (%)")
        ax.legend(fontsize=7)
    fig.tight_layout()
    save_figure(fig, Path(out_dir) / "fig_savings_vs_eta_error")
    plt.close(fig)


def fig_rank_difference(df_runs: pd.DataFrame, out_dir: Path) -> None:
    """Selisih relatif biaya PSO - GA per bank (negatif = PSO lebih murah)."""
    apply_thesis_style()
    configs = _configs_present(df_runs)
    fig, axes = plt.subplots(1, len(configs), figsize=(3.4 * len(configs), 3.8), sharey=False)
    axes = np.atleast_1d(axes)
    for ax, cid in zip(axes, configs):
        g = df_runs[df_runs["config_id"] == cid]
        p = g[g["algo"] == "pso"].set_index("bank_index").sort_index()
        a = g[g["algo"] == "ga"].set_index("bank_index").sort_index()
        common = p.index.intersection(a.index)
        if len(common) == 0:
            continue
        d = ((p.loc[common, "best_cost"] - a.loc[common, "best_cost"]) / a.loc[common, "best_cost"]).to_numpy()
        ax.bar(np.arange(len(d)), d * 100.0,
               color=[ALGO_COLORS["pso"] if v <= 0 else ALGO_COLORS["ga"] for v in d], edgecolor="black")
        ax.axhline(0.0, color="black", linewidth=0.8)
        ax.set_title(CONFIG_LABELS[cid])
        ax.set_xlabel("Indeks bank")
        ax.set_ylabel("(PSO - GA) / GA pada biaya (%)")
    fig.tight_layout()
    save_figure(fig, Path(out_dir) / "fig_rank_difference")
    plt.close(fig)


def make_all_figures(result: Dict, out_dir: Path) -> None:
    """Membuat keenam grafik studi."""
    tables = result["tables"]
    fig_limits_distribution(result["df_limits"], tables["limits_summary"], out_dir)
    fig_savings_distribution(result["df_runs"], tables["summary_savings"], out_dir)
    fig_weights_by_config(tables["summary_weights"], out_dir)
    fig_feasibility(tables["summary_feasibility"], out_dir)
    fig_savings_vs_eta_error(result["df_runs"], out_dir)
    fig_rank_difference(result["df_runs"], out_dir)
