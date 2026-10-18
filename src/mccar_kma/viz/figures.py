"""Modul pembuatan gambar grafis ilmiah tugas akhir (Tahap 14).

Mengimplementasikan 6 topik visualisasi:
1. Kurva konvergensi (median + pita IQR 30 replikasi) per konfigurasi dan panel all.
2. Boxplot nilai objektif per algoritma di 4 konfigurasi.
3. Komposisi portofolio: eksisting vs DJPPR vs KMA/GA/PSO (batang bertumpuk 7 instrumen).
4. Profil rasio theta_i per instrumen untuk eksisting dan solusi terbaik.
5. Waktu komputasi per algoritma di 4 konfigurasi.
6. Deret waktu yield suku bunga dan kurs valas historis 2017–2025.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mccar_kma.viz.style import (
    ALGO_COLORS,
    ALGO_STYLES,
    ALGO_MARKERS,
    ALGO_LABELS,
    INSTRUMENT_NAMES,
    INSTRUMENT_DISPLAY_NAMES,
    INSTRUMENT_COLORS,
    INSTRUMENT_HATCHES,
    apply_thesis_style,
    save_figure,
)


CONFIG_TITLES: Dict[str, str] = {
    "gross_free": "Biaya Bruto — Batas Bebas (gross_free)",
    "gross_djppr": "Biaya Bruto — Batas DJPPR (gross_djppr)",
    "interest_free": "Biaya Bunga — Batas Bebas (interest_free)",
    "interest_djppr": "Biaya Bunga — Batas DJPPR (interest_djppr)",
}


def compute_convergence_envelope(
    runs_dir: Union[str, Path],
    config_id: str,
    algo: str,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Mengekstrak deret evaluasi, median, Q1, dan Q3 dari 30 replikasi run."""
    runs_path = Path(runs_dir) / config_id / algo
    json_files = sorted(list(runs_path.glob("rep_*.json")))
    if not json_files:
        return np.array([]), np.array([]), np.array([]), np.array([])

    all_histories: List[Dict[int, float]] = []
    eval_set = set()

    for jf in json_files:
        try:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)
            hist = data.get("convergence_history", [])
            run_dict = {}
            for pt in hist:
                ev = int(pt["evaluation"])
                c = float(pt["best_cost"])
                run_dict[ev] = c
                eval_set.add(ev)
            all_histories.append(run_dict)
        except Exception:
            continue

    sorted_evals = np.array(sorted(list(eval_set)))
    n_runs = len(all_histories)
    if n_runs == 0 or len(sorted_evals) == 0:
        return np.array([]), np.array([]), np.array([]), np.array([])

    mat = np.full((n_runs, len(sorted_evals)), np.nan)
    for r_idx, r_dict in enumerate(all_histories):
        for e_idx, ev in enumerate(sorted_evals):
            if ev in r_dict:
                mat[r_idx, e_idx] = r_dict[ev]

    # Forward fill jika ada titik kosong
    for r_idx in range(n_runs):
        for e_idx in range(1, len(sorted_evals)):
            if np.isnan(mat[r_idx, e_idx]):
                mat[r_idx, e_idx] = mat[r_idx, e_idx - 1]

    median_curve = np.nanmedian(mat, axis=0)
    q1_curve = np.nanpercentile(mat, 25, axis=0)
    q3_curve = np.nanpercentile(mat, 75, axis=0)

    return sorted_evals, median_curve, q1_curve, q3_curve


# ==============================================================================
# TOPIK 1: Kurva Konvergensi (Median + Pita IQR)
# ==============================================================================

def plot_convergence_single(
    runs_dir: Union[str, Path],
    config_id: str,
    output_path: Union[str, Path],
    w0_cost: float,
    baseline_cost: Optional[float] = None,
) -> Tuple[Path, Path]:
    """Menggambar kurva konvergensi tunggal untuk satu konfigurasi."""
    apply_thesis_style()
    fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)

    # Garis acuan w0
    ax.axhline(
        y=w0_cost,
        color=ALGO_COLORS["existing"],
        linestyle=ALGO_STYLES["existing"],
        linewidth=1.8,
        label=f"Eksisting 2024 ($w_0 = {w0_cost:.6f}$)",
        zorder=3,
    )

    if baseline_cost is not None and not np.isnan(baseline_cost):
        ax.axhline(
            y=baseline_cost,
            color=ALGO_COLORS["djppr"],
            linestyle=ALGO_STYLES["djppr"],
            linewidth=1.6,
            label=f"Baseline DJPPR ($Cost = {baseline_cost:.6f}$)",
            zorder=3,
        )

    for algo in ["kma", "ga", "pso"]:
        evals, med, q1, q3 = compute_convergence_envelope(runs_dir, config_id, algo)
        if len(evals) == 0:
            continue

        c_hex = ALGO_COLORS[algo]
        l_style = ALGO_STYLES[algo]
        lbl = f"{ALGO_LABELS[algo]} (Akhir: {med[-1]:.6f})"

        # Garis median
        ax.plot(evals, med, label=lbl, color=c_hex, linestyle=l_style, linewidth=2.0, zorder=5)
        # Pita IQR
        ax.fill_between(evals, q1, q3, color=c_hex, alpha=0.18, zorder=4)

    ax.set_title(f"Kurva Konvergensi Optimasi Biaya — {CONFIG_TITLES.get(config_id, config_id)}")
    ax.set_xlabel("Jumlah Evaluasi Fungsi Portofolio")
    ax.set_ylabel("Biaya Rata-Rata Portofolio ($Cost$)")
    ax.set_xlim(0, 25500)
    ax.legend(loc="upper right", framealpha=0.9)

    return save_figure(fig, output_path)


def plot_convergence_grid_all(
    runs_dir: Union[str, Path],
    limits_path: Union[str, Path],
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar panel 4-grid (2x2) kurva konvergensi untuk keempat konfigurasi."""
    apply_thesis_style()
    with open(limits_path, "r", encoding="utf-8") as f:
        limits = json.load(f)

    w0_gross = float(limits["gross"]["mean_cost"])
    w0_interest = float(limits["interest"]["mean_cost"])

    config_list = [
        ("gross_free", w0_gross, None),
        ("gross_djppr", w0_gross, 1.042709),
        ("interest_free", w0_interest, None),
        ("interest_djppr", w0_interest, 0.044148),
    ]

    fig, axes = plt.subplots(2, 2, figsize=(13.0, 9.2), dpi=300)
    axes_flat = axes.flatten()

    for idx, (cid, w0_val, base_val) in enumerate(config_list):
        ax = axes_flat[idx]
        ax.axhline(
            y=w0_val,
            color=ALGO_COLORS["existing"],
            linestyle=ALGO_STYLES["existing"],
            linewidth=1.6,
            label=f"Eksisting ($w_0 = {w0_val:.6f}$)",
            zorder=3,
        )
        if base_val is not None:
            ax.axhline(
                y=base_val,
                color=ALGO_COLORS["djppr"],
                linestyle=ALGO_STYLES["djppr"],
                linewidth=1.4,
                label=f"Baseline DJPPR ({base_val:.6f})",
                zorder=3,
            )

        for algo in ["kma", "ga", "pso"]:
            evals, med, q1, q3 = compute_convergence_envelope(runs_dir, cid, algo)
            if len(evals) == 0:
                continue
            c_hex = ALGO_COLORS[algo]
            l_style = ALGO_STYLES[algo]
            lbl = f"{algo.upper()} (Median: {med[-1]:.6f})"
            ax.plot(evals, med, label=lbl, color=c_hex, linestyle=l_style, linewidth=1.8, zorder=5)
            ax.fill_between(evals, q1, q3, color=c_hex, alpha=0.18, zorder=4)

        ax.set_title(f"({chr(97+idx)}) {CONFIG_TITLES.get(cid, cid)}", fontsize=11, fontweight="bold")
        ax.set_xlabel("Evaluasi Fungsi", fontsize=9.5)
        ax.set_ylabel("Biaya Portofolio ($Cost$)", fontsize=9.5)
        ax.set_xlim(0, 25500)
        ax.legend(loc="upper right", fontsize=8.5, framealpha=0.9)

    fig.suptitle("Perbandingan Kurva Konvergensi Metaheuristik (Median + Pita IQR 30 Replikasi)", fontsize=13.5, fontweight="bold", y=0.995)
    plt.tight_layout()
    return save_figure(fig, output_path)


# ==============================================================================
# TOPIK 2: Boxplot Nilai Objektif
# ==============================================================================

def plot_objective_boxplots(
    runs_df: pd.DataFrame,
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar panel 4-grid boxplot sebaran nilai objektif per algoritma."""
    apply_thesis_style()
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    fig, axes = plt.subplots(2, 2, figsize=(12.0, 8.5), dpi=300)
    axes_flat = axes.flatten()

    for idx, cid in enumerate(config_ids):
        ax = axes_flat[idx]
        sub = runs_df[runs_df["config_id"] == cid]

        data = [
            sub[sub["algo"] == "kma"]["best_cost"].values,
            sub[sub["algo"] == "ga"]["best_cost"].values,
            sub[sub["algo"] == "pso"]["best_cost"].values,
        ]

        bp = ax.boxplot(
            data,
            tick_labels=["KMA", "GA", "PSO"],
            patch_artist=True,
            showmeans=True,
            meanprops={"marker": "D", "markeredgecolor": "black", "markerfacecolor": "yellow", "markersize": 5},
            medianprops={"color": "black", "linewidth": 1.6},
            widths=0.55,
        )

        colors = [ALGO_COLORS["kma"], ALGO_COLORS["ga"], ALGO_COLORS["pso"]]
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.7)

        # Plot individual points jitter
        for g_idx, vals in enumerate(data):
            jitter = np.random.normal(0, 0.04, size=len(vals))
            ax.scatter(np.full_like(vals, g_idx + 1) + jitter, vals, color=colors[g_idx], s=18, alpha=0.6, edgecolors="none")

        ax.set_title(f"({chr(97+idx)}) {CONFIG_TITLES.get(cid, cid)}", fontsize=11, fontweight="bold")
        ax.set_ylabel("Biaya Rerata Portofolio ($Cost$)", fontsize=9.5)
        ax.set_xlabel("Algoritma Optimasi", fontsize=9.5)

    fig.suptitle("Sebaran Nilai Objektif Solusi Layak Terbaik (30 Replikasi per Algoritma)", fontsize=13.5, fontweight="bold", y=0.995)
    plt.tight_layout()
    return save_figure(fig, output_path)


# ==============================================================================
# TOPIK 3: Komposisi Portofolio (Diagram Batang Bertumpuk 7 Instrumen)
# ==============================================================================

def plot_portfolio_composition_single(
    composition_dict: Dict[str, np.ndarray],
    config_id: str,
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar diagram batang bertumpuk komposisi 7 instrumen untuk satu konfigurasi."""
    apply_thesis_style()
    fig, ax = plt.subplots(figsize=(8.0, 5.0), dpi=300)

    strategies = list(composition_dict.keys())
    n_strategies = len(strategies)
    x = np.arange(n_strategies)
    width = 0.55

    bottom = np.zeros(n_strategies)
    for inst_idx, (name_disp, color_hex, hatch_pat) in enumerate(zip(INSTRUMENT_DISPLAY_NAMES, INSTRUMENT_COLORS, INSTRUMENT_HATCHES)):
        weights = np.array([composition_dict[st][inst_idx] * 100.0 for st in strategies])
        ax.bar(
            x,
            weights,
            width,
            bottom=bottom,
            label=name_disp,
            color=color_hex,
            hatch=hatch_pat,
            edgecolor="#333333",
            linewidth=0.7,
            alpha=0.9,
        )
        bottom += weights

    ax.set_title(f"Komposisi Alokasi Portofolio Optimal — {CONFIG_TITLES.get(config_id, config_id)}")
    ax.set_xticks(x)
    ax.set_xticklabels(strategies, fontweight="bold")
    ax.set_ylabel("Proporsi Alokasi Utang (%)")
    ax.set_ylim(0, 105)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), title="Instrumen Utang", framealpha=0.9)

    plt.tight_layout()
    return save_figure(fig, output_path)


def plot_portfolio_composition_all(
    all_compositions: Dict[str, Dict[str, np.ndarray]],
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar panel 4-grid komposisi portofolio bertumpuk untuk seluruh konfigurasi."""
    apply_thesis_style()
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    fig, axes = plt.subplots(2, 2, figsize=(13.5, 9.5), dpi=300)
    axes_flat = axes.flatten()

    for idx, cid in enumerate(config_ids):
        ax = axes_flat[idx]
        comp_dict = all_compositions.get(cid, {})
        strategies = list(comp_dict.keys())
        n_strat = len(strategies)
        x = np.arange(n_strat)
        width = 0.52

        bottom = np.zeros(n_strat)
        for inst_idx, (name_disp, color_hex, hatch_pat) in enumerate(zip(INSTRUMENT_DISPLAY_NAMES, INSTRUMENT_COLORS, INSTRUMENT_HATCHES)):
            weights = np.array([comp_dict[st][inst_idx] * 100.0 for st in strategies])
            ax.bar(
                x,
                weights,
                width,
                bottom=bottom,
                label=name_disp if idx == 0 else "",
                color=color_hex,
                hatch=hatch_pat,
                edgecolor="#333333",
                linewidth=0.6,
                alpha=0.9,
            )
            bottom += weights

        ax.set_title(f"({chr(97+idx)}) {CONFIG_TITLES.get(cid, cid)}", fontsize=11, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(strategies, fontsize=9, fontweight="bold")
        ax.set_ylabel("Proporsi (%)", fontsize=9.5)
        ax.set_ylim(0, 105)

    # Legenda bersama di bawah atau samping
    fig.legend(
        labels=INSTRUMENT_DISPLAY_NAMES,
        loc="lower center",
        ncol=7,
        bbox_to_anchor=(0.5, 0.01),
        title="Instrumen Utang Multivaluta",
        fontsize=9.5,
        title_fontsize=10.5,
        frameon=True,
    )

    fig.suptitle("Perbandingan Komposisi Alokasi Portofolio Optimal (7 Instrumen)", fontsize=13.5, fontweight="bold", y=0.99)
    plt.subplots_adjust(bottom=0.10, top=0.94, hspace=0.28, wspace=0.22)
    return save_figure(fig, output_path)


# ==============================================================================
# TOPIK 4: Rasio theta_i per Instrumen
# ==============================================================================

def plot_theta_ratios_single(
    theta_dict: Dict[str, np.ndarray],
    theta_bar_dict: Dict[str, float],
    config_id: str,
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar diagram profil rasio theta_i = MCCaR_i / MC_i untuk 7 instrumen."""
    apply_thesis_style()
    fig, ax = plt.subplots(figsize=(9.0, 5.0), dpi=300)

    strategies = list(theta_dict.keys())
    n_strat = len(strategies)
    n_inst = len(INSTRUMENT_DISPLAY_NAMES)
    x = np.arange(n_inst)
    width = 0.8 / n_strat

    strat_colors = {
        "Eksisting 2024": ALGO_COLORS["existing"],
        "Baseline DJPPR": ALGO_COLORS["djppr"],
        "KMA Best": ALGO_COLORS["kma"],
        "GA Best": ALGO_COLORS["ga"],
        "PSO Best": ALGO_COLORS["pso"],
    }

    for s_idx, st in enumerate(strategies):
        offset = (s_idx - (n_strat - 1) / 2.0) * width
        c = strat_colors.get(st, "#333333")
        theta_vals = theta_dict[st]
        ax.bar(x + offset, theta_vals, width, label=st, color=c, alpha=0.85, edgecolor="#222222", linewidth=0.7)

    # Garis rata-rata theta_bar eksisting
    if "Eksisting 2024" in theta_bar_dict:
        th_bar_w0 = theta_bar_dict["Eksisting 2024"]
        ax.axhline(th_bar_w0, color=ALGO_COLORS["existing"], linestyle=":", linewidth=1.5, label=f"$\\bar{{\\theta}}$ Eksisting ({th_bar_w0:.3f})")

    ax.set_title(f"Profil Rasio Marginal Risk-Cost ($\\theta_i = \\text{{MCCaR}}_i / \\text{{MC}}_i$) — {CONFIG_TITLES.get(config_id, config_id)}")
    ax.set_xticks(x)
    ax.set_xticklabels(INSTRUMENT_DISPLAY_NAMES, fontweight="bold")
    ax.set_ylabel("Rasio $\\theta_i$ (Tanpa Satuan)")
    ax.set_xlabel("Instrumen Utang Multivaluta")
    ax.legend(loc="upper right", framealpha=0.9, fontsize=9.0)

    plt.tight_layout()
    return save_figure(fig, output_path)


def plot_theta_ratios_all(
    all_thetas: Dict[str, Dict[str, np.ndarray]],
    all_theta_bars: Dict[str, Dict[str, float]],
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar panel 4-grid profil rasio theta_i untuk keempat konfigurasi."""
    apply_thesis_style()
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    fig, axes = plt.subplots(2, 2, figsize=(13.5, 9.2), dpi=300)
    axes_flat = axes.flatten()

    strat_colors = {
        "Eksisting 2024": ALGO_COLORS["existing"],
        "Baseline DJPPR": ALGO_COLORS["djppr"],
        "KMA Best": ALGO_COLORS["kma"],
        "GA Best": ALGO_COLORS["ga"],
        "PSO Best": ALGO_COLORS["pso"],
    }

    for idx, cid in enumerate(config_ids):
        ax = axes_flat[idx]
        th_dict = all_thetas.get(cid, {})
        th_bar_dict = all_theta_bars.get(cid, {})
        strategies = list(th_dict.keys())
        n_strat = len(strategies)
        n_inst = len(INSTRUMENT_DISPLAY_NAMES)
        x = np.arange(n_inst)
        width = 0.8 / n_strat if n_strat > 0 else 0.2

        for s_idx, st in enumerate(strategies):
            offset = (s_idx - (n_strat - 1) / 2.0) * width
            c = strat_colors.get(st, "#333333")
            ax.bar(x + offset, th_dict[st], width, label=st, color=c, alpha=0.85, edgecolor="#222222", linewidth=0.6)

        if "Eksisting 2024" in th_bar_dict:
            th_bar_w0 = th_bar_dict["Eksisting 2024"]
            ax.axhline(th_bar_w0, color=ALGO_COLORS["existing"], linestyle=":", linewidth=1.3, label=f"$\\bar{{\\theta}}_{{w0}}$ ({th_bar_w0:.2f})")

        ax.set_title(f"({chr(97+idx)}) {CONFIG_TITLES.get(cid, cid)}", fontsize=11, fontweight="bold")
        ax.set_xticks(x)
        ax.set_xticklabels(INSTRUMENT_DISPLAY_NAMES, fontsize=8.5, fontweight="bold")
        ax.set_ylabel("Rasio $\\theta_i$", fontsize=9.5)
        ax.legend(loc="upper right", fontsize=8.0, framealpha=0.9)

    fig.suptitle("Profil Rasio Marginal Risk-Cost ($\\theta_i = \\text{MCCaR}_i / \\text{MC}_i$)", fontsize=13.5, fontweight="bold", y=0.99)
    plt.tight_layout()
    return save_figure(fig, output_path)


# ==============================================================================
# TOPIK 5: Waktu Komputasi per Algoritma
# ==============================================================================

def plot_computation_times(
    runs_df: pd.DataFrame,
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar grafik perbandingan waktu komputasi antar algoritma di 4 konfigurasi."""
    apply_thesis_style()
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
    algos = ["kma", "ga", "pso"]

    fig, ax = plt.subplots(figsize=(9.0, 5.2), dpi=300)

    n_cfg = len(config_ids)
    x = np.arange(n_cfg)
    width = 0.25

    for a_idx, algo in enumerate(algos):
        mean_times = []
        std_times = []
        for cid in config_ids:
            sub = runs_df[(runs_df["config_id"] == cid) & (runs_df["algo"] == algo)]
            mean_times.append(float(sub["time_seconds"].mean()))
            std_times.append(float(sub["time_seconds"].std(ddof=1)))

        offset = (a_idx - 1) * width
        c_hex = ALGO_COLORS[algo]
        lbl = ALGO_LABELS[algo]

        bars = ax.bar(
            x + offset,
            mean_times,
            width,
            yerr=std_times,
            capsize=4,
            label=lbl,
            color=c_hex,
            alpha=0.85,
            edgecolor="#222222",
            linewidth=0.7,
        )

        # Label angka di atas batang
        for b, m in zip(bars, mean_times):
            ax.text(
                b.get_x() + b.get_width() / 2.0,
                m + 3.0,
                f"{m:.1f}s",
                ha="center",
                va="bottom",
                fontsize=8.0,
                fontweight="bold",
            )

    ax.set_title("Perbandingan Waktu Komputasi per Replikasi (Rata-rata $\\pm$ 1 Simpangan Baku)")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{cid}\n({CONFIG_TITLES[cid].split('—')[0].strip()})" for cid in config_ids], fontsize=9.5)
    ax.set_ylabel("Waktu Komputasi (Detik)")
    ax.set_ylim(0, max(runs_df["time_seconds"]) * 1.15)
    ax.legend(loc="upper left", framealpha=0.9)

    plt.tight_layout()
    return save_figure(fig, output_path)


# ==============================================================================
# TOPIK 6: Deret Waktu Data Pasar (Yield dan Kurs 2017–2025)
# ==============================================================================

def plot_market_timeseries(
    market_csv_path: Union[str, Path],
    output_path: Union[str, Path],
) -> Tuple[Path, Path]:
    """Menggambar deret waktu historis yield suku bunga dan kurs valas pada jendela analisis."""
    apply_thesis_style()
    df_market = pd.read_csv(market_csv_path)
    df_market["Tanggal"] = pd.to_datetime(df_market["Tanggal"])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11.0, 7.5), dpi=300, sharex=True)

    # Panel 1: Suku Bunga Yield Obligasi (7 instrumen)
    ir_cols = [
        ("IR_USD_5Y", "USD 5Y", "#1f77b4", "-"),
        ("IR_USD_10Y", "USD 10Y", "#aec7e8", "--"),
        ("IR_USD_30Y", "USD 30Y", "#2ca02c", "-."),
        ("IR_EUR_7Y", "EUR 7Y", "#ff7f0e", "-"),
        ("IR_EUR_10Y", "EUR 10Y", "#ffbb78", "--"),
        ("IR_JPY_5Y", "JPY 5Y", "#9467bd", "-"),
        ("IR_JPY_10Y", "JPY 10Y", "#c5b0d5", "-."),
    ]

    for col, lbl, color, l_style in ir_cols:
        ax1.plot(df_market["Tanggal"], df_market[col], label=lbl, color=color, linestyle=l_style, linewidth=1.2)

    ax1.set_title("(a) Deret Waktu Suku Bunga Yield Obligasi Negara Valas ($C_{i,t}$, % per Tahun)", fontsize=11, fontweight="bold")
    ax1.set_ylabel("Yield (%)", fontsize=10)
    ax1.legend(loc="upper right", ncol=4, fontsize=8.5, framealpha=0.9)

    # Panel 2: Kurs Valuta Asing (FX_USD/EUR dan FX_USD/JPY)
    color_eur = "#d62728"
    color_jpy = "#8c564b"

    line1 = ax2.plot(df_market["Tanggal"], df_market["FX_USD/EUR"], label="Kurs USD/EUR (Kiri)", color=color_eur, linewidth=1.4)
    ax2.set_ylabel("Kurs FX USD/EUR (EUR per 1 USD)", color=color_eur, fontsize=10)
    ax2.tick_params(axis="y", labelcolor=color_eur)

    ax2_twin = ax2.twinx()
    line2 = ax2_twin.plot(df_market["Tanggal"], df_market["FX_USD/JPY"], label="Kurs USD/JPY (Kanan)", color=color_jpy, linestyle="--", linewidth=1.4)
    ax2_twin.set_ylabel("Kurs FX USD/JPY (JPY per 1 USD)", color=color_jpy, fontsize=10)
    ax2_twin.tick_params(axis="y", labelcolor=color_jpy)
    ax2_twin.grid(False)

    lines = line1 + line2
    labels = [l.get_label() for l in lines]
    ax2.legend(lines, labels, loc="upper left", fontsize=8.5, framealpha=0.9)
    ax2.set_title("(b) Deret Waktu Nilai Tukar Valuta Asing Terhadap USD", fontsize=11, fontweight="bold")
    ax2.set_xlabel("Tahun Observasi (Jendela Analisis 2017–2025)", fontsize=10)

    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

    fig.suptitle("Dinamika Pasar Historis 2017–2025 (2.028 Hari Kerja)", fontsize=13.0, fontweight="bold", y=0.995)
    plt.tight_layout()
    return save_figure(fig, output_path)
