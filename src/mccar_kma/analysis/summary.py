"""Modul ringkasan statistik deskriptif dan pengujian asumsi parametrik (Tahap 13).

Menyediakan fungsi untuk:
1. Ringkasan statistik deskriptif per algoritma (terbaik, median, rata-rata, simpangan baku, IQR).
2. Waktu komputasi dan evaluasi fungsi menuju konvergensi (E_conv).
3. Pengujian asumsi normalitas (Shapiro-Wilk) dan homogenitas variansi (Levene).
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import json
import numpy as np
import pandas as pd
from scipy import stats


def compute_algorithm_summary(
    df: pd.DataFrame,
    runs_dir: Optional[Union[str, Path]] = None,
    tol_conv: float = 1e-6,
) -> pd.DataFrame:
    """Menghitung statistik deskriptif nilai objektif dan konvergensi per algoritma.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame hasil eksperimen untuk satu konfigurasi (misal 90 baris dari runs_summary.csv).
    runs_dir : Optional[Union[str, Path]]
        Direktori penyimpanan JSON hasil run (results/runs) untuk membaca convergence_history.
    tol_conv : float
        Toleransi selisih biaya terhadap nilai akhir untuk menentukan evaluasi konvergensi.

    Returns
    -------
    pd.DataFrame
        Tabel ringkasan metrik deskriptif per algoritma (KMA, GA, PSO).
    """
    algorithms = ["kma", "ga", "pso"]
    summary_rows = []

    for algo in algorithms:
        sub = df[df["algo"] == algo]
        if len(sub) == 0:
            continue

        costs = sub["best_cost"].values.astype(float)
        times = sub["time_seconds"].values.astype(float)

        best_cost = float(np.min(costs))
        median_cost = float(np.median(costs))
        mean_cost = float(np.mean(costs))
        std_cost = float(np.std(costs, ddof=1)) if len(costs) > 1 else 0.0
        q25 = float(np.percentile(costs, 25))
        q75 = float(np.percentile(costs, 75))
        iqr_cost = q75 - q25

        mean_time = float(np.mean(times))
        std_time = float(np.std(times, ddof=1)) if len(times) > 1 else 0.0

        # Cari evaluasi menuju konvergensi jika berkas JSON tersedia
        conv_evals = []
        if runs_dir is not None:
            runs_path = Path(runs_dir)
            for _, row in sub.iterrows():
                cid = row["config_id"]
                rep = int(row["rep"])
                seed = int(row["seed"])
                # results/runs/<config_id>/<algo>/rep_<kk>_seed<seed>.json
                json_file = runs_path / cid / algo / f"rep_{rep:02d}_seed{seed}.json"
                if json_file.exists():
                    try:
                        with open(json_file, "r", encoding="utf-8") as jf:
                            run_data = json.load(jf)
                        hist = run_data.get("convergence_history", [])
                        final_c = float(run_data.get("best_cost", best_cost))
                        first_eval = int(run_data.get("evaluations", 25000))
                        for entry in hist:
                            if abs(float(entry["best_cost"]) - final_c) <= tol_conv:
                                first_eval = int(entry["evaluation"])
                                break
                        conv_evals.append(first_eval)
                    except Exception:
                        conv_evals.append(int(row.get("evaluations", 25000)))
                else:
                    conv_evals.append(int(row.get("evaluations", 25000)))

        if len(conv_evals) > 0:
            mean_conv_eval = float(np.mean(conv_evals))
            std_conv_eval = float(np.std(conv_evals, ddof=1)) if len(conv_evals) > 1 else 0.0
            median_conv_eval = float(np.median(conv_evals))
        else:
            mean_conv_eval = float(sub["evaluations"].mean()) if "evaluations" in sub else 25000.0
            std_conv_eval = 0.0
            median_conv_eval = mean_conv_eval

        summary_rows.append({
            "algo": algo.upper(),
            "n_runs": len(sub),
            "best_cost": best_cost,
            "median_cost": median_cost,
            "mean_cost": mean_cost,
            "std_cost": std_cost,
            "q25_cost": q25,
            "q75_cost": q75,
            "iqr_cost": iqr_cost,
            "mean_time_sec": mean_time,
            "std_time_sec": std_time,
            "mean_conv_eval": mean_conv_eval,
            "std_conv_eval": std_conv_eval,
            "median_conv_eval": median_conv_eval,
        })

    return pd.DataFrame(summary_rows)


def check_parametric_assumptions(df: pd.DataFrame) -> Dict[str, Any]:
    """Menguji asumsi normalitas (Shapiro-Wilk) dan homogenitas variansi (Levene).

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame hasil eksperimen untuk satu konfigurasi.

    Returns
    -------
    Dict[str, Any]
        Dictionary hasil uji statistik normalitas dan homogenitas.
    """
    algorithms = ["kma", "ga", "pso"]
    groups = []
    shapiro_results = {}

    for algo in algorithms:
        sub = df[df["algo"] == algo]
        data = sub["best_cost"].values.astype(float)
        groups.append(data)

        # Penanganan kasus variansi nol / data konstan identik
        if np.std(data) < 1e-12 or np.all(data == data[0]):
            shapiro_results[algo] = {
                "statistic": 1.0,
                "p_value": 0.0,
                "is_normal": False,
                "note": "Variansi nol (seluruh nilai replikasi identik)",
            }
        else:
            stat_w, p_val = stats.shapiro(data)
            shapiro_results[algo] = {
                "statistic": float(stat_w),
                "p_value": float(p_val),
                "is_normal": bool(p_val >= 0.05),
                "note": "Normal" if p_val >= 0.05 else "Tidak Normal (p < 0.05)",
            }

    # Uji Homogenitas Levene antarkelompok
    levene_stat, levene_p = stats.levene(*groups)
    is_homoscedastic = bool(levene_p >= 0.05)

    all_normal = all(r["is_normal"] for r in shapiro_results.values())
    parametric_valid = all_normal and is_homoscedastic

    return {
        "shapiro_wilk": shapiro_results,
        "levene": {
            "statistic": float(levene_stat),
            "p_value": float(levene_p),
            "is_homoscedastic": is_homoscedastic,
            "note": "Homogen" if is_homoscedastic else "Heterogen (p < 0.05)",
        },
        "parametric_valid": parametric_valid,
        "justification": (
            "Asumsi normalitas/homogenitas terpenuhi."
            if parametric_valid
            else "Asumsi normalitas atau homogenitas ragam dilanggar (p < 0.05), "
            "sehingga uji non-parametrik Kruskal-Wallis secara statistik dijustifikasi."
        ),
    }
