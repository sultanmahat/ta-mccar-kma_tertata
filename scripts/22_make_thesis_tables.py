"""Tahap 22: Tabel turunan untuk naskah skripsi (Bab 4).

1. results/tables/thesis_weight_change_vs_w0.csv -- perubahan bobot solusi
   (run terbaik, run median, rata-rata 30 replikasi) terhadap komposisi eksisting
   2024, per konfigurasi dan algoritma (sumber: results/tables/runs_summary.csv).
2. results/tables/thesis_scenario_example.csv -- contoh hitung beberapa skenario
   bank latih seed 42 (Persamaan 2.1-2.3), dicocokkan dengan matriks biaya bank.

Hanya membaca hasil yang ada; tidak menulis ke results/runs/ atau runs_summary.csv.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from mccar_kma.analysis.thesis_tables import scenario_example, weight_change_vs_w0
from mccar_kma.model.constraints import W0

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_IDS = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
ALGOS = ["kma", "ga", "pso"]


def file_sha256(path: Path) -> str:
    """Hash SHA-256 isi berkas (metadata reproduksibilitas)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    params_path = BASE_DIR / "configs" / "params.yaml"
    cfg = yaml.safe_load(params_path.read_text(encoding="utf-8"))
    tcfg = cfg["thesis_tables"]

    runs_path = BASE_DIR / "results" / "tables" / "runs_summary.csv"
    df_runs = pd.read_csv(runs_path, float_precision="round_trip")
    inst_names = [item["name"] for item in cfg["instruments"]["items"]]
    w0_cfg = np.array([item["w0"] for item in cfg["instruments"]["items"]], dtype=float)
    if not np.array_equal(w0_cfg, W0):
        raise RuntimeError("w0 di params.yaml berbeda dari konstanta W0 kode (audit S1)")

    df_w = weight_change_vs_w0(df_runs, W0, inst_names, CONFIG_IDS, ALGOS)
    out_w = BASE_DIR / tcfg["output_weight_change"]
    df_w.to_csv(out_w, index=False)

    bank_path = BASE_DIR / tcfg["bank_train_path"]
    bank = dict(np.load(bank_path))
    df_s = scenario_example(bank, int(tcfg["n_example_scenarios"]))
    out_s = BASE_DIR / tcfg["output_scenario_example"]
    df_s.to_csv(out_s, index=False)

    meta = {
        "stage": 22,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "config_sha256": file_sha256(params_path),
        "inputs": {
            "results/tables/runs_summary.csv": file_sha256(runs_path),
            tcfg["bank_train_path"]: file_sha256(bank_path),
        },
        "train_seed": int(cfg["scenarios"]["train_seed"]),
        "n_example_scenarios": int(tcfg["n_example_scenarios"]),
        "median_rule": "run ke-floor((n-1)/2) setelah urut best_cost naik (median bawah)",
    }
    (BASE_DIR / tcfg["output_metadata"]).write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print("Perubahan bobot terhadap w0 (run median, poin persen):")
    piv = (df_w[df_w["kind"] == "median"]
           .assign(delta_pp=lambda d: 100 * d["delta"])
           .pivot_table(index=["config_id", "algo"], columns="instrument", values="delta_pp", sort=False))
    print(piv[inst_names].round(2).to_string())
    print("\nContoh skenario 1 (biaya bruto per instrumen):")
    print(df_s[(df_s["scenario"] == 1) & (df_s["kind"].isin(["q", "cost_gross"]))].to_string(index=False))
    print(f"\nTersimpan: {out_w} ({len(df_w)} baris)\nTersimpan: {out_s} ({len(df_s)} baris)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
