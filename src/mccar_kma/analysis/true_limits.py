"""Kelayakan solusi 360 run terhadap batas risiko "benar" dari bank validasi (Tahap 21).

Tahap 12 mengevaluasi ulang solusi pada bank validasi N = 20.000 dengan batas
bank latih (tau, eta dari seed 42), sesuai spesifikasi §10. Modul ini menambah
pembanding kedua: batas yang dihitung ulang dari w0 pada bank validasi itu
sendiri (Persamaan 2.22 diterapkan pada bank validasi), yaitu estimasi batas
yang lebih presisi (m = 1.000 skenario ekor). Perbedaan keduanya mengukur
seberapa besar kelayakan hasil utama bergantung pada estimasi batas bank latih
(temuan T3, docs/reviews/audit_ulang_2026-10-25.md).

Tidak ada optimasi yang dijalankan ulang; J_MCCaR dan CCaR tiap solusi pada bank
validasi dibaca dari keluaran Tahap 12 (results/tables/validation_all_runs.csv).
"""

from __future__ import annotations

from typing import Dict, Sequence

import numpy as np
import pandas as pd

from mccar_kma.analysis.limit_stability import clopper_pearson
from mccar_kma.model.constraints import compute_relative_violations


def add_true_limit_columns(
    df_val: pd.DataFrame,
    true_limits: Dict[str, Dict[str, float]],
    eps_tol: float,
) -> pd.DataFrame:
    """Menambah pelanggaran relatif dan status kelayakan terhadap batas benar (Persamaan 2.23).

    Parameters
    ----------
    df_val : pd.DataFrame
        Keluaran Tahap 12; wajib memuat kolom cost_definition, val_j_mccar,
        val_ccar, dan val_weight_feasible.
    true_limits : Dict[str, Dict[str, float]]
        {cost_definition: {"eta": ..., "tau": ...}} dari w0 pada bank validasi.
    eps_tol : float
        Toleransi kelayakan relatif (sama dengan eksperimen utama).

    Returns
    -------
    pd.DataFrame
        Salinan df_val dengan kolom eta_true, tau_true, v_J_true, v_R_true,
        feasible_true.
    """
    out = df_val.copy()
    eta_col, tau_col, vj_col, vr_col = [], [], [], []
    for _, r in out.iterrows():
        lim = true_limits[r["cost_definition"]]
        v_j, v_r = compute_relative_violations(
            float(r["val_j_mccar"]), float(r["val_ccar"]),
            lim["eta"], lim["tau"], eps_tol=eps_tol,
        )
        eta_col.append(lim["eta"])
        tau_col.append(lim["tau"])
        vj_col.append(v_j)
        vr_col.append(v_r)
    out["eta_true"] = eta_col
    out["tau_true"] = tau_col
    out["v_J_true"] = vj_col
    out["v_R_true"] = vr_col
    risk_ok = (out["v_J_true"] <= eps_tol) & (out["v_R_true"] <= eps_tol)
    out["feasible_true"] = out["val_weight_feasible"].astype(bool) & risk_ok
    return out


def summarize_true_limit_feasibility(
    df: pd.DataFrame,
    group_cols: Sequence[str],
    level: float,
    eps_tol: float,
) -> pd.DataFrame:
    """Ringkasan k/n layak per grup terhadap batas bank latih dan batas benar, dengan CI Clopper-Pearson.

    Parameters
    ----------
    df : pd.DataFrame
        Keluaran add_true_limit_columns.
    group_cols : Sequence[str]
        Kolom pengelompokan, mis. ["config_id", "algo"].
    level : float
        Tingkat kepercayaan CI.
    eps_tol : float
        Ambang v > eps_tol dihitung sebagai pelanggaran.

    Returns
    -------
    pd.DataFrame
        Satu baris per grup.
    """
    rows = []
    for keys, g in df.groupby(list(group_cols), sort=False):
        keys = keys if isinstance(keys, tuple) else (keys,)
        n = int(len(g))
        k_train = int(g["val_is_feasible"].astype(bool).sum())
        k_true = int(g["feasible_true"].astype(bool).sum())
        lo, hi = clopper_pearson(k_true, n, level)
        row = dict(zip(group_cols, keys))
        row.update({
            "n": n,
            "k_train_limits": k_train,
            "k_true_limits": k_true,
            "prop_true": k_true / n if n else float("nan"),
            "cp_lo_true": lo,
            "cp_hi_true": hi,
            "n_violate_J_true": int((g["v_J_true"] > eps_tol).sum()),
            "n_violate_R_true": int((g["v_R_true"] > eps_tol).sum()),
            "max_v_J_true": float(np.max(g["v_J_true"])),
            "max_v_R_true": float(np.max(g["v_R_true"])),
            "eta_true": float(g["eta_true"].iloc[0]),
            "tau_true": float(g["tau_true"].iloc[0]),
        })
        rows.append(row)
    return pd.DataFrame(rows)
