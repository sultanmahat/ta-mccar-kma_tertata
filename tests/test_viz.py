"""Unit test untuk modul visualisasi skripsi dan pembangkit tabel LaTeX (Tahap 14).

Menguji:
1. Penerapan gaya tipografi tesis (serif, 300 dpi, rcParams).
2. Fungsi penyimpanan ganda save_figure (.pdf vektor dan .png raster).
3. Integritas fungsi plotting dasar pada data sintetis / smoke test.
4. Sintaksis booktabs pada tabel LaTeX yang dihasilkan.
"""

from pathlib import Path
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from mccar_kma.viz.style import (
    apply_thesis_style,
    save_figure,
    ALGO_COLORS,
    ALGO_STYLES,
    ALGO_MARKERS,
    ALGO_LABELS,
    INSTRUMENT_NAMES,
    INSTRUMENT_COLORS,
    INSTRUMENT_HATCHES,
)
from mccar_kma.viz.figures import (
    plot_convergence_single,
    plot_objective_boxplots,
    plot_computation_times,
)
import importlib.util

spec = importlib.util.spec_from_file_location(
    "make_figures_tables",
    Path(__file__).parent.parent / "scripts" / "14_make_figures_tables.py",
)
make_figures_tables = importlib.util.module_from_spec(spec)
spec.loader.exec_module(make_figures_tables)

generate_experiment_params_table = make_figures_tables.generate_experiment_params_table
generate_risk_limits_table = make_figures_tables.generate_risk_limits_table
generate_results_summary_table = make_figures_tables.generate_results_summary_table


def test_thesis_style_application():
    """Memverifikasi pengaturan global rcParams setelah apply_thesis_style()."""
    apply_thesis_style()
    assert plt.rcParams["font.family"] == ["serif"]
    assert plt.rcParams["savefig.dpi"] == 300
    assert plt.rcParams["axes.grid"] is True
    assert plt.rcParams["text.usetex"] is False  # Tidak bergantung pada instalasi latex biner lokal


def test_save_figure_dual_format(tmp_path: Path):
    """Memverifikasi save_figure menghasilkan berkas PDF dan PNG secara bersamaan."""
    apply_thesis_style()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot([0, 1, 2], [10, 20, 15], label="Data Uji")
    ax.legend()

    base_output = tmp_path / "test_figure"
    pdf_path, png_path = save_figure(fig, base_output, dpi=150)

    assert pdf_path.exists()
    assert png_path.exists()
    assert pdf_path.stat().st_size > 0
    assert png_path.stat().st_size > 0
    assert pdf_path.suffix == ".pdf"
    assert png_path.suffix == ".png"


def test_convergence_plot_smoke(tmp_path: Path):
    """Smoke test untuk fungsi plot_convergence_single."""
    apply_thesis_style()
    runs_dir = tmp_path / "runs"
    config_dir = runs_dir / "gross_djppr"
    for algo in ["kma", "ga", "pso"]:
        algo_dir = config_dir / algo
        algo_dir.mkdir(parents=True, exist_ok=True)
        dummy_data = {
            "convergence_history": [
                [0, 1000.0],
                [250, 950.0],
                [500, 900.0],
                [25000, 850.0],
            ]
        }
        with open(algo_dir / "rep_01_seed100.json", "w", encoding="utf-8") as f:
            json.dump(dummy_data, f)

    out_base = tmp_path / "fig_convergence_test"
    pdf_p, png_p = plot_convergence_single(
        runs_dir=runs_dir,
        config_id="gross_djppr",
        output_path=out_base,
        w0_cost=1050.0,
        baseline_cost=980.0,
    )

    assert pdf_p.exists()
    assert png_p.exists()
    assert pdf_p.stat().st_size > 0
    assert png_p.stat().st_size > 0


def test_boxplot_smoke(tmp_path: Path):
    """Smoke test untuk boxplot nilai objektif."""
    apply_thesis_style()
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
    rows = []
    for cid in config_ids:
        for algo in ["kma", "ga", "pso"]:
            for cost in [800.0, 810.0, 820.0]:
                rows.append({"config_id": cid, "algo": algo, "best_cost": cost, "time_seconds": 15.0})

    df_runs = pd.DataFrame(rows)

    out_base = tmp_path / "fig_boxplot_test"
    pdf_p, png_p = plot_objective_boxplots(df_runs, out_base)
    assert pdf_p.exists()
    assert png_p.exists()

    out_time_base = tmp_path / "fig_time_test"
    pdf_t, png_t = plot_computation_times(df_runs, out_time_base)
    assert pdf_t.exists()
    assert png_t.exists()


def test_latex_table_syntax(tmp_path: Path):
    """Memverifikasi sintaksis booktabs pada tabel LaTeX yang dihasilkan."""
    params_yaml = Path("configs/params.yaml")
    if not params_yaml.exists():
        pytest.skip("configs/params.yaml tidak ditemukan")

    out_tex = tmp_path / "tab_params_test.tex"
    generate_experiment_params_table(params_yaml, out_tex)

    assert out_tex.exists()
    content = out_tex.read_text(encoding="utf-8")
    assert r"\begin{table}" in content
    assert r"\toprule" in content
    assert r"\midrule" in content
    assert r"\bottomrule" in content
    assert r"\end{table}" in content
