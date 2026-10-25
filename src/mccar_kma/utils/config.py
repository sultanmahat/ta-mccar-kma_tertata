"""Pemuatan konfigurasi parameter proyek (configs/params.yaml).

Satu sumber loader bersama supaya tidak ada duplikasi `yaml.safe_load` di tiap modul
(akar masalah temuan S1/R9, audit_ulang_2026-10-25.md). Path default diresolusi dari
lokasi berkas ini, bukan dari direktori kerja saat ini, supaya modul `src/` bisa dipanggil
dari mana pun (termasuk dari tests/) tanpa tergantung CWD.
"""

from pathlib import Path
from typing import Any, Dict, Optional, Union
import yaml

# src/mccar_kma/utils/config.py -> parents[3] = root repositori
REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = REPO_ROOT / "configs" / "params.yaml"


def load_config(config_path: Optional[Union[str, Path]] = None) -> Dict[str, Any]:
    """Membaca configs/params.yaml (atau path lain yang diberikan).

    Parameters
    ----------
    config_path : Optional[Union[str, Path]]
        Lokasi berkas YAML konfigurasi. Jika None, memakai `configs/params.yaml`
        di root repositori.

    Returns
    -------
    Dict[str, Any]
        Isi konfigurasi terparse.
    """
    path = Path(config_path) if config_path is not None else DEFAULT_CONFIG_PATH
    if not path.exists():
        raise FileNotFoundError(f"Berkas konfigurasi tidak ditemukan: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
