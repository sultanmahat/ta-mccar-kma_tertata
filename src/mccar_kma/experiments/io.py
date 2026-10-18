"""Modul I/O untuk eksperimen: penyimpanan atomic, validasi resumability, dan agregasi ringkasan.

Struktur folder hasil:
results/runs/<config_id>/<algo>/rep_<kk>_seed<seed>.json
"""

from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)

ESSENTIAL_RUN_FIELDS = [
    "config_id",
    "algo",
    "rep",
    "seed",
    "is_feasible",
    "best_cost",
    "best_w",
    "evaluations",
]


def get_run_result_path(
    base_dir: Path,
    config_id: str,
    algo: str,
    rep: int,
    seed: int,
) -> Path:
    """Menentukan path file JSON hasil untuk suatu replikasi tertentu."""
    return Path(base_dir) / config_id / algo / f"rep_{rep:02d}_seed{seed}.json"


def is_run_completed(filepath: Path) -> bool:
    """Memeriksa apakah suatu run telah selesai dan file JSON hasil valid serta utuh.

    Parameters
    ----------
    filepath : Path
        Lokasi file JSON hasil replikasi.

    Returns
    -------
    bool
        True jika file ada, ukuran > 0, JSON valid, dan seluruh field esensial ada.
    """
    path = Path(filepath)
    if not path.is_file():
        return False
    if path.stat().st_size == 0:
        return False

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        for field in ESSENTIAL_RUN_FIELDS:
            if field not in data:
                return False
        return True
    except Exception as exc:
        logger.warning("File hasil %s rusak atau tidak dapat dibaca: %s", path, exc)
        return False


def save_run_result(filepath: Path, data: Dict[str, Any]) -> None:
    """Menyimpan hasil run secara atomic untuk mencegah kerusakan data jika terputus.

    Parameters
    ----------
    filepath : Path
        Lokasi target file JSON hasil.
    data : Dict[str, Any]
        Data hasil replikasi.
    """
    target = Path(filepath)
    target.parent.mkdir(parents=True, exist_ok=True)

    tmp_file = target.with_suffix(f".tmp_{os.getpid()}")
    try:
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_file, target)
    except Exception:
        if tmp_file.exists():
            try:
                tmp_file.unlink()
            except OSError:
                pass
        raise


def load_run_result(filepath: Path) -> Dict[str, Any]:
    """Membaca isi file JSON hasil replikasi.

    Parameters
    ----------
    filepath : Path
        Lokasi file JSON.

    Returns
    -------
    Dict[str, Any]
        Data hasil replikasi.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def build_runs_summary(
    runs_dir: Path,
    output_csv: Optional[Path] = None,
) -> pd.DataFrame:
    """Memindai seluruh file JSON replikasi yang tersimpan dan menyusun CSV ringkasan.

    Parameters
    ----------
    runs_dir : Path
        Direktori induk penyimpanan hasil (misal results/runs).
    output_csv : Optional[Path]
        Jika diberikan, DataFrame ringkasan akan disimpan ke file CSV ini.

    Returns
    -------
    pd.DataFrame
        DataFrame berisi 1 baris per replikasi yang selesai.
    """
    runs_path = Path(runs_dir)
    records: List[Dict[str, Any]] = []

    if runs_path.exists():
        for json_file in sorted(runs_path.rglob("rep_*_seed*.json")):
            if not is_run_completed(json_file):
                continue
            try:
                data = load_run_result(json_file)
                best_w = data.get("best_w", [])
                record = {
                    "config_id": data.get("config_id"),
                    "cost_definition": data.get("cost_definition"),
                    "constraint_type": data.get("constraint_type"),
                    "algo": data.get("algo"),
                    "rep": data.get("rep"),
                    "seed": data.get("seed"),
                    "is_feasible": data.get("is_feasible"),
                    "best_cost": data.get("best_cost"),
                    "best_fitness": data.get("best_fitness"),
                    "ccar": data.get("ccar"),
                    "j_mccar": data.get("j_mccar"),
                    "tau": data.get("tau_limit"),
                    "eta": data.get("eta_limit"),
                    "evaluations": data.get("evaluations"),
                    "time_seconds": data.get("time_seconds"),
                    "timestamp": data.get("timestamp"),
                }
                for i, w_val in enumerate(best_w, start=1):
                    record[f"w_{i}"] = w_val
                records.append(record)
            except Exception as exc:
                logger.error("Gagal mengekstrak %s: %s", json_file, exc)

    df = pd.DataFrame(records)
    if not df.empty:
        sort_cols = [c for c in ["config_id", "algo", "rep"] if c in df.columns]
        if sort_cols:
            df = df.sort_values(sort_cols).reset_index(drop=True)

    if output_csv is not None:
        out_path = Path(output_csv)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(out_path, index=False)
        logger.info("Tabel ringkasan runs (%d baris) disimpan ke %s", len(df), out_path)

    return df
