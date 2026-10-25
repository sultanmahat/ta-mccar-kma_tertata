"""Tahap 21: Kelayakan 360 solusi terhadap batas risiko "benar" dari bank validasi.

Batas benar = (eta_v, tau_v) dari w0 pada bank validasi N = 20.000 (Persamaan 2.22
diterapkan pada bank validasi). J_MCCaR dan CCaR tiap solusi pada bank validasi
dibaca dari keluaran Tahap 12, lalu pelanggaran relatif dihitung ulang dengan
Persamaan 2.23 terhadap batas benar.

Batas benar dihitung ulang dari bank validasi dan dicocokkan dengan nilai
valid_bank_value Tahap 17 (results/sensitivity/limits/limits_summary.csv);
skrip berhenti bila selisih relatif melebihi true_limits.crosscheck_rel_tol.

Keluaran (lihat blok true_limits di configs/params.yaml): CSV per run, CSV
ringkasan per config_id x algo, dan metadata JSON. Tidak menulis ke
results/runs/ maupun keluaran Tahap 12.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yaml

from mccar_kma.analysis.true_limits import (
    add_true_limit_columns,
    summarize_true_limit_feasibility,
)
from mccar_kma.model.constraints import W0
from mccar_kma.risk.evaluator import PortfolioEvaluator

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_IDS = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
ALGOS = ["kma", "ga", "pso"]


def file_sha256(path: Path) -> str:
    """Hash SHA-256 isi berkas (metadata reproduksibilitas)."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compute_true_limits(cfg: dict) -> dict:
    """Batas benar (eta_v, tau_v) dari w0 pada bank validasi (Persamaan 2.22)."""
    tcfg = cfg["true_limits"]
    bank_path = BASE_DIR / tcfg["bank_valid_path"]
    limits = {}
    for cost_def in cfg["cost_definitions"]:
        ev = PortfolioEvaluator.from_scenario_bank(
            bank_data_or_path=bank_path,
            cost_def=cost_def,
            alpha=float(cfg["risk"]["alpha"]),
            delta=float(cfg["risk"]["delta"]),
            rho_J=float(cfg["optimization"]["penalty_rho_J"]),
            rho_R=float(cfg["optimization"]["penalty_rho_R"]),
            eps_tol=float(cfg["optimization"]["eps_tol"]),
            zero_tol_mc=float(cfg["risk"]["zero_tolerance_mc"]),
        )
        base = ev.set_baseline(W0)
        limits[cost_def] = {"eta": float(base["eta"]), "tau": float(base["tau"]),
                            "w0_cost": float(base["mean_cost"])}
    return limits


def crosscheck_limits(limits: dict, cfg: dict) -> pd.DataFrame:
    """Cocokkan batas benar dengan valid_bank_value Tahap 17; gagal keras bila tidak sama."""
    tcfg = cfg["true_limits"]
    ref = pd.read_csv(BASE_DIR / tcfg["limits_summary_path"])
    tol = float(tcfg["crosscheck_rel_tol"])
    rows = []
    for cost_def, lim in limits.items():
        for metric in ("eta", "tau"):
            r = ref[(ref["cost_definition"] == cost_def) & (ref["metric"] == metric)]
            ref_val = float(r["valid_bank_value"].iloc[0])
            rel = abs(lim[metric] - ref_val) / abs(ref_val)
            rows.append({"cost_definition": cost_def, "metric": metric,
                         "tahap21": lim[metric], "tahap17": ref_val, "rel_diff": rel})
            if rel > tol:
                raise RuntimeError(
                    f"Batas benar {cost_def}/{metric} tidak cocok dengan Tahap 17: "
                    f"{lim[metric]!r} vs {ref_val!r} (rel {rel:.3e} > {tol:.0e})"
                )
    return pd.DataFrame(rows)


def main() -> int:
    params_path = BASE_DIR / "configs" / "params.yaml"
    cfg = yaml.safe_load(params_path.read_text(encoding="utf-8"))
    tcfg = cfg["true_limits"]
    eps_tol = float(cfg["optimization"]["eps_tol"])

    limits = compute_true_limits(cfg)
    df_check = crosscheck_limits(limits, cfg)
    print("Cross-check batas benar vs Tahap 17:")
    print(df_check.to_string(index=False))

    val_path = BASE_DIR / tcfg["validation_runs_path"]
    df_val = pd.read_csv(val_path)
    if len(df_val) != len(CONFIG_IDS) * len(ALGOS) * int(cfg["experiments"]["replications"]):
        raise RuntimeError(f"Jumlah baris validasi tidak sesuai desain: {len(df_val)}")

    df_runs = add_true_limit_columns(df_val, limits, eps_tol=eps_tol)
    df_sum = summarize_true_limit_feasibility(
        df_runs, ["config_id", "algo"], level=float(tcfg["confidence_level"]), eps_tol=eps_tol
    )
    order = {(c, a): i for i, (c, a) in enumerate((c, a) for c in CONFIG_IDS for a in ALGOS)}
    df_sum["_o"] = [order[(c, a)] for c, a in zip(df_sum["config_id"], df_sum["algo"])]
    df_sum = df_sum.sort_values("_o").drop(columns="_o").reset_index(drop=True)

    keep = ["config_id", "cost_definition", "constraint_type", "algo", "rep", "seed",
            "val_cost", "val_ccar", "val_j_mccar", "val_v_J", "val_v_R", "val_is_feasible",
            "eta_true", "tau_true", "v_J_true", "v_R_true", "feasible_true"]
    out_runs = BASE_DIR / tcfg["output_runs"]
    out_sum = BASE_DIR / tcfg["output_summary"]
    out_runs.parent.mkdir(parents=True, exist_ok=True)
    df_runs[keep].to_csv(out_runs, index=False)
    df_sum.to_csv(out_sum, index=False)

    meta = {
        "stage": 21,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "config_sha256": file_sha256(params_path),
        "inputs": {
            tcfg["validation_runs_path"]: file_sha256(val_path),
            tcfg["bank_valid_path"]: file_sha256(BASE_DIR / tcfg["bank_valid_path"]),
        },
        "validation_seed": int(cfg["scenarios"]["validation_seed"]),
        "true_limits": limits,
        "crosscheck_tahap17": df_check.to_dict(orient="records"),
        "eps_tol": eps_tol,
    }
    (BASE_DIR / tcfg["output_metadata"]).write_text(json.dumps(meta, indent=2), encoding="utf-8")

    print("\nKelayakan terhadap batas bank latih vs batas benar (bank validasi):")
    cols = ["config_id", "algo", "n", "k_train_limits", "k_true_limits", "cp_lo_true",
            "cp_hi_true", "n_violate_J_true", "n_violate_R_true", "max_v_J_true"]
    print(df_sum[cols].to_string(index=False))
    print(f"\nTersimpan: {out_runs}\nTersimpan: {out_sum}\nTersimpan: {BASE_DIR / tcfg['output_metadata']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
