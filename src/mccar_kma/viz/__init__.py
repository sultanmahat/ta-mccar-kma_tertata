"""Subpaket visualisasi grafik dan tabel tugas akhir (Tahap 14)."""

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
from mccar_kma.viz.figures import (
    plot_convergence_single,
    plot_convergence_grid_all,
    plot_objective_boxplots,
    plot_portfolio_composition_single,
    plot_portfolio_composition_all,
    plot_theta_ratios_single,
    plot_theta_ratios_all,
    plot_computation_times,
    plot_market_timeseries,
)

__all__ = [
    "ALGO_COLORS",
    "ALGO_STYLES",
    "ALGO_MARKERS",
    "ALGO_LABELS",
    "INSTRUMENT_NAMES",
    "INSTRUMENT_DISPLAY_NAMES",
    "INSTRUMENT_COLORS",
    "INSTRUMENT_HATCHES",
    "apply_thesis_style",
    "save_figure",
    "plot_convergence_single",
    "plot_convergence_grid_all",
    "plot_objective_boxplots",
    "plot_portfolio_composition_single",
    "plot_portfolio_composition_all",
    "plot_theta_ratios_single",
    "plot_theta_ratios_all",
    "plot_computation_times",
    "plot_market_timeseries",
]
