"""Tabel turunan untuk naskah skripsi (Tahap 22).

Dua tabel, mengikuti pola laporan TA terdahulu yang menjadi rujukan format:
1. Perubahan bobot solusi terhadap komposisi eksisting 2024 (w0) per konfigurasi
   dan algoritma, untuk tiga ringkasan: run biaya terbaik, run biaya median, dan
   rata-rata bobot 30 replikasi.
2. Contoh hitung beberapa skenario dari bank latih: nilai pasar terminal, faktor
   kurs q (Persamaan 2.1), dan biaya per instrumen (Persamaan 2.2 dan 2.3), yang
   dihitung ulang dan dicocokkan dengan matriks biaya tersimpan di bank.

Modul hanya membaca hasil yang sudah ada; tidak ada optimasi yang dijalankan.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

import numpy as np
import pandas as pd

from mccar_kma.scenarios.cost import compute_q_factors, compute_scenario_costs

WEIGHT_COLUMNS = [f"w_{i}" for i in range(1, 8)]
FX_COLUMNS = ("FX_USD/EUR", "FX_USD/JPY")


def representative_runs(group: pd.DataFrame) -> Dict[str, pd.Series]:
    """Pilih run biaya terbaik dan run biaya median (median bawah bila n genap) dari satu grup."""
    ordered = group.sort_values(["best_cost", "rep"]).reset_index(drop=True)
    median_pos = (len(ordered) - 1) // 2
    return {"best": ordered.iloc[0], "median": ordered.iloc[median_pos]}


def weight_change_vs_w0(
    df_runs: pd.DataFrame,
    w0: Sequence[float],
    instrument_names: Sequence[str],
    config_ids: Sequence[str],
    algos: Sequence[str],
) -> pd.DataFrame:
    """Selisih bobot solusi terhadap w0 dalam poin proporsi (w_i - w0_i).

    Parameters
    ----------
    df_runs : pd.DataFrame
        results/tables/runs_summary.csv (kolom config_id, algo, rep, best_cost, w_1..w_7).
    w0 : Sequence[float]
        Komposisi eksisting 2024 (Tabel 2.2 proposal).
    instrument_names : Sequence[str]
        Nama 7 instrumen sesuai urutan w_1..w_7.
    config_ids, algos : Sequence[str]
        Urutan baris keluaran.

    Returns
    -------
    pd.DataFrame
        Format panjang: satu baris per (config_id, algo, kind, instrumen).
        kind = "best" | "median" | "mean30"; rep kosong untuk mean30.
    """
    w0 = np.asarray(w0, dtype=float)
    rows: List[dict] = []
    for cid in config_ids:
        for algo in algos:
            g = df_runs[(df_runs["config_id"] == cid) & (df_runs["algo"] == algo)]
            if g.empty:
                raise ValueError(f"Tidak ada run untuk {cid}/{algo}")
            reps = representative_runs(g)
            picks = [
                ("best", int(reps["best"]["rep"]), float(reps["best"]["best_cost"]),
                 reps["best"][WEIGHT_COLUMNS].to_numpy(dtype=float)),
                ("median", int(reps["median"]["rep"]), float(reps["median"]["best_cost"]),
                 reps["median"][WEIGHT_COLUMNS].to_numpy(dtype=float)),
                ("mean30", None, float(g["best_cost"].mean()),
                 g[WEIGHT_COLUMNS].to_numpy(dtype=float).mean(axis=0)),
            ]
            for kind, rep, cost, w in picks:
                for name, wi, w0i in zip(instrument_names, w, w0):
                    rows.append({
                        "config_id": cid, "algo": algo, "kind": kind, "rep": rep,
                        "cost_train": cost, "instrument": name,
                        "w0": float(w0i), "w": float(wi), "delta": float(wi - w0i),
                    })
    return pd.DataFrame(rows)


def scenario_example(
    bank: Dict[str, np.ndarray],
    n_examples: int,
    instruments: Optional[List[dict]] = None,
) -> pd.DataFrame:
    """Contoh hitung skenario 1..n_examples dari bank (Persamaan 2.1-2.3), format panjang.

    Biaya dihitung ulang dari nilai pasar terminal dan kurs awal s0, lalu dicocokkan
    dengan matriks biaya tersimpan; ValueError bila tidak identik dalam toleransi
    pembulatan mesin.
    """
    var_names = [str(v) for v in bank["variable_names"]]
    s0 = np.asarray(bank["s0"], dtype=float)
    market = np.asarray(bank["scenarios_market"], dtype=float)[:n_examples]
    x0 = {fx: float(s0[var_names.index(fx)]) for fx in FX_COLUMNS}

    q = compute_q_factors(market, var_names, x0)
    costs = {d: compute_scenario_costs(market, var_names, x0, instruments, cost_def=d)
             for d in ("gross", "interest")}
    for d in costs:
        stored = np.asarray(bank[f"cost_{d}"], dtype=float)[:n_examples]
        if not np.allclose(costs[d], stored, rtol=0.0, atol=1e-12):
            raise ValueError(f"Biaya {d} hitung ulang tidak cocok dengan bank tersimpan")
    if not np.allclose(q, np.asarray(bank["q_factors"], dtype=float)[:n_examples], rtol=0.0, atol=1e-12):
        raise ValueError("Faktor q hitung ulang tidak cocok dengan bank tersimpan")

    inst_names = [str(n) for n in bank["instrument_names"]]
    cur_names = [str(c) for c in bank["currency_names"]]
    rows: List[dict] = []
    for s in range(n_examples):
        sid = s + 1
        for j, v in enumerate(var_names):
            rows.append({"scenario": sid, "kind": "s0", "name": v, "value": float(s0[j])})
            rows.append({"scenario": sid, "kind": "market_T", "name": v, "value": float(market[s, j])})
        for j, c in enumerate(cur_names):
            rows.append({"scenario": sid, "kind": "q", "name": c, "value": float(q[s, j])})
        for d in ("gross", "interest"):
            for j, n in enumerate(inst_names):
                rows.append({"scenario": sid, "kind": f"cost_{d}", "name": n,
                             "value": float(costs[d][s, j])})
    return pd.DataFrame(rows)
