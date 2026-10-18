"""Modul manajemen gaya, tipografi, dan palet warna visualisasi skripsi (Tahap 14).

Menyediakan:
1. Konfigurasi global rcParams (font keluarga serif, ukuran teks proporsional, grid halus).
2. Palet warna dan pola garis konsisten untuk KMA, GA, PSO, Eksisting, dan DJPPR.
3. Pola arsir (hatching) dan palet kontras untuk keterbacaan cetak hitam-putih.
4. Fungsi utilitas penyimpanan gambar ganda (PDF vektor + PNG 300 dpi).
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Palet warna konsisten untuk algoritma dan benchmark
ALGO_COLORS: Dict[str, str] = {
    "kma": "#1f77b4",       # Biru Navy
    "ga": "#ff7f0e",        # Oranye Amber
    "pso": "#2ca02c",       # Hijau Emerald
    "existing": "#d62728",  # Merah Crimson
    "djppr": "#9467bd",     # Ungu Violet
}

# Gaya garis untuk pencetakan hitam-putih
ALGO_STYLES: Dict[str, str] = {
    "kma": "-",             # Garis lurus utuh
    "ga": "--",             # Garis putus-putus
    "pso": "-.",            # Garis titik-garis
    "existing": ":",        # Garis titik-titik
    "djppr": "--",          # Garis putus-putus rapat
}

# Marker untuk penandaan data diskret
ALGO_MARKERS: Dict[str, str] = {
    "kma": "o",             # Lingkaran
    "ga": "s",              # Persegi
    "pso": "^",             # Segitiga atas
    "existing": "D",        # Belah ketupat
    "djppr": "v",           # Segitiga bawah
}

# Label tampilan resmi Bahasa Indonesia
ALGO_LABELS: Dict[str, str] = {
    "kma": "Komodo Mlipir Algorithm (KMA)",
    "ga": "Genetic Algorithm (GA)",
    "pso": "Particle Swarm Optimization (PSO)",
    "existing": "Portofolio Eksisting 2024",
    "djppr": "Baseline Acak DJPPR",
}

# Palet 7 instrumen utang untuk diagram batang bertumpuk (komposisi)
INSTRUMENT_NAMES: List[str] = [
    "USD_Fixed_5Y",
    "USD_Fixed_10Y",
    "USD_Fixed_30Y",
    "EUR_Fixed_7Y",
    "EUR_Fixed_10Y",
    "JPY_Fixed_5Y",
    "JPY_Fixed_10Y",
]

INSTRUMENT_DISPLAY_NAMES: List[str] = [
    "USD 5Y",
    "USD 10Y",
    "USD 30Y",
    "EUR 7Y",
    "EUR 10Y",
    "JPY 5Y",
    "JPY 10Y",
]

INSTRUMENT_COLORS: List[str] = [
    "#2b5c8f",  # USD 5Y: Biru Tua
    "#4682b4",  # USD 10Y: Steel Blue
    "#6baed6",  # USD 30Y: Biru Terang
    "#e6550d",  # EUR 7Y: Oranye Bata
    "#fdae6b",  # EUR 10Y: Oranye Muda
    "#31a354",  # JPY 5Y: Hijau Hutan
    "#a1d99b",  # JPY 10Y: Hijau Muda
]

# Pola arsir untuk diagram batang agar tetap terbaca jelas saat dicetak monokrom
INSTRUMENT_HATCHES: List[str] = [
    "//",       # USD 5Y
    "\\\\",     # USD 10Y
    "xx",       # USD 30Y
    "..",       # EUR 7Y
    "++",       # EUR 10Y
    "**",       # JPY 5Y
    "OO",       # JPY 10Y
]


def apply_thesis_style() -> None:
    """Mengatur konfigurasi visual global Matplotlib agar sesuai dengan standar skripsi ITS."""
    # Prioritas font keluarga serif (kompatibel dengan LaTeX)
    serif_fonts = ["DejaVu Serif", "Times New Roman", "Liberation Serif", "serif"]

    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": serif_fonts,
        "mathtext.fontset": "cm",           # Computer Modern untuk formula matematika
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.05,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.labelsize": 10.5,
        "axes.labelweight": "normal",
        "axes.grid": True,
        "axes.grid.which": "major",
        "axes.grid.axis": "both",
        "grid.color": "#d3d3d3",
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
        "grid.alpha": 0.7,
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.8,
        "xtick.labelsize": 9.5,
        "ytick.labelsize": 9.5,
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.size": 3.5,
        "ytick.major.size": 3.5,
        "legend.fontsize": 9.0,
        "legend.frameon": True,
        "legend.framealpha": 0.9,
        "legend.edgecolor": "#cccccc",
        "legend.fancybox": False,
        "lines.linewidth": 1.6,
        "lines.markersize": 5.5,
    })


def save_figure(
    fig: plt.Figure,
    base_path: Union[str, Path],
    dpi: int = 300,
) -> Tuple[Path, Path]:
    """Menyimpan figur ke dalam dua format sekaligus: PDF vektor dan PNG 300 dpi.

    Parameters
    ----------
    fig : plt.Figure
        Objek figur matplotlib yang akan disimpan.
    base_path : Union[str, Path]
        Path dasar tanpa ekstensi atau dengan ekstensi (.pdf / .png).
    dpi : int
        Resolusi raster untuk berkas PNG (default: 300).

    Returns
    -------
    Tuple[Path, Path]
        Pasangan (path_pdf, path_png) berkas yang berhasil disimpan.
    """
    path_obj = Path(base_path)
    parent_dir = path_obj.parent
    parent_dir.mkdir(parents=True, exist_ok=True)

    stem = path_obj.stem
    pdf_path = parent_dir / f"{stem}.pdf"
    png_path = parent_dir / f"{stem}.png"

    # 1. Simpan format PDF vektor
    fig.savefig(pdf_path, format="pdf", bbox_inches="tight")

    # 2. Simpan format PNG 300 dpi
    fig.savefig(png_path, format="png", dpi=dpi, bbox_inches="tight")

    plt.close(fig)
    return pdf_path, png_path
