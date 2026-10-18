"""Skrip migrasi in-place untuk config_hash pada 360 berkas rep_*.json dan runs_summary.csv."""

import glob
import hashlib
import json
from pathlib import Path
import pandas as pd


def migrate_config_hash():
    params_path = Path("configs/params.yaml")
    params_hash = hashlib.sha256(params_path.read_bytes()).hexdigest()
    print(f"Using params_hash from {params_path}: {params_hash}")

    # 1. Update 360 berkas rep_*.json
    json_files = glob.glob("results/runs/**/*.json", recursive=True)
    print(f"Ditemukan {len(json_files)} berkas JSON run.")
    assert len(json_files) == 360, f"Harusnya 360 berkas, tetapi ditemukan {len(json_files)}"

    for fpath in json_files:
        p = Path(fpath)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["config_hash"] = params_hash
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    print(f"Berhasil memperbarui config_hash di 360 berkas JSON.")

    # 2. Update results/tables/runs_summary.csv
    csv_path = Path("results/tables/runs_summary.csv")
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        df["config_hash"] = params_hash
        df.to_csv(csv_path, index=False)
        print(f"Berhasil memperbarui {csv_path}. Jumlah unique config_hash: {df['config_hash'].nunique()}")


if __name__ == "__main__":
    migrate_config_hash()
