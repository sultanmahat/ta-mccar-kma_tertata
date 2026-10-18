"""Modul visualisasi kurva konvergensi cepat untuk eksperimen pilot (Tahap 11a)."""

from pathlib import Path
from typing import Dict, List, Optional
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def plot_pilot_convergence(
    runs_dir: Path,
    output_png: Path,
    config_id: str = "gross_djppr",
    rep: int = 1,
    seed: int = 43,
    baseline_cost: float = 1.04236992,
) -> Path:
    """Menggambar grafik kurva konvergensi komparatif KMA vs GA vs PSO untuk replikasi pilot.

    Parameters
    ----------
    runs_dir : Path
        Direktori induk results/runs.
    output_png : Path
        Path berkas gambar output (PNG).
    config_id : str
        ID konfigurasi (default: gross_djppr).
    rep : int
        Nomor replikasi (default: 1).
    seed : int
        Seed replikasi (default: 43).
    baseline_cost : float
        Biaya rata-rata portofolio eksisting w0 (default: 1.04236992).

    Returns
    -------
    Path
        Path berkas gambar yang dihasilkan.
    """
    runs_path = Path(runs_dir)
    out_path = Path(output_png)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    algos = [
        ("kma", "Komodo Mlipir Algorithm (KMA)", "#1f77b4", "-"),
        ("ga", "Genetic Algorithm (GA)", "#ff7f0e", "--"),
        ("pso", "Particle Swarm Optimization (PSO)", "#2ca02c", "-."),
    ]

    plt.figure(figsize=(10, 6), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    # Garis acuan baseline eksisting w0
    plt.axhline(
        y=baseline_cost,
        color="#d62728",
        linestyle=":",
        linewidth=1.8,
        label=f"Baseline Eksisting w0 (Cost = {baseline_cost:.6f})",
    )

    plotted_any = False

    for algo_key, label_name, color_hex, line_style in algos:
        json_file = runs_path / config_id / algo_key / f"rep_{rep:02d}_seed{seed}.json"
        if not json_file.exists():
            continue

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            history = data.get("convergence_history", [])
            if not history:
                continue

            evals = [pt["evaluation"] for pt in history]
            costs = [pt["best_cost"] for pt in history]

            # Filter None jika ada
            valid_pts = [(e, c) for e, c in zip(evals, costs) if c is not None]
            if not valid_pts:
                continue

            x_vals, y_vals = zip(*valid_pts)
            final_cost = data.get("best_cost", y_vals[-1])
            is_feas = data.get("is_feasible", True)

            plt.plot(
                x_vals,
                y_vals,
                label=f"{label_name} (Akhir: {final_cost:.6f})",
                color=color_hex,
                linestyle=line_style,
                linewidth=2.0,
            )

            # Titik solusi akhir
            plt.scatter(
                [x_vals[-1]],
                [final_cost],
                color=color_hex,
                s=60,
                zorder=5,
            )
            plotted_any = True
        except Exception as exc:
            print(f"Peringatan: Gagal memplot {json_file}: {exc}")

    plt.title(
        f"Kurva Konvergensi Optimasi Biaya Portofolio (Pilot: {config_id}, Seed {seed})",
        fontsize=13,
        fontweight="bold",
        pad=12,
    )
    plt.xlabel("Jumlah Evaluasi Fungsi Portofolio", fontsize=11, labelpad=8)
    plt.ylabel("Biaya Rata-Rata Portofolio (Cost)", fontsize=11, labelpad=8)
    plt.xlim(0, 25500)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(frameon=True, facecolor="white", framealpha=0.9, fontsize=10, loc="upper right")
    plt.tight_layout()

    plt.savefig(out_path, dpi=300)
    plt.close()
    return out_path
