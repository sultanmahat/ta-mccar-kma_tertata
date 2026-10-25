"""Studi stabilitas batas risiko eta (J_MCCaR) dan tau (CCaR) antar bank latih independen.

Konteks (spesifikasi §6, Persamaan 2.22):
    tau = CCaR_alpha(w0),  eta = J_MCCaR(w0)
dihitung SEKALI dari portofolio eksisting 2024 pada satu bank latih (seed 42, N = 5.000)
lalu dipakai sebagai kendala pada optimasi di bank yang sama. Modul ini mengukur seberapa
besar galat Monte Carlo batas tersebut dan dampaknya pada penghematan, bobot, kelayakan
validasi, serta peringkat PSO vs GA.

Alur:
1. Bangkitkan B bank latih independen (seed terpisah dari 42 dan 2026).
2. Pada tiap bank: hitung eta_b dan tau_b dari w0 (m = 250) untuk biaya bruto dan bunga.
3. Optimasi PSO dan GA (satu replikasi per bank) untuk 4 konfigurasi.
4. Evaluasi tiap solusi pada bank validasi (N = 20.000) dengan (A) batas bank sendiri dan
   (B) batas "benar" = batas w0 pada bank validasi.

Semua keacakan memakai numpy.random.Generator ber-seed eksplisit; semua parameter dibaca
dari blok `sensitivity_limits` di configs/params.yaml. Tidak ada keluaran yang boleh
ditulis ke results/runs atau results/tables.
"""

from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd
from scipy import stats
import yaml

from mccar_kma.analysis.validation import validate_single_portfolio
from mccar_kma.data.cleaning import ALL_MARKET_COLS
from mccar_kma.experiments.runner import get_bounds_for_constraint
from mccar_kma.model.constraints import W0
from mccar_kma.optimizers.ga import GeneticAlgorithmOptimizer
from mccar_kma.optimizers.pso import ParticleSwarmOptimizer
from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.scenarios.cost import build_scenario_bank
from mccar_kma.scenarios.estimation import INSTRUMENTS
from mccar_kma.scenarios.gbm import generate_market_scenarios

ALGORITHM_CLASSES = {
    "pso": ParticleSwarmOptimizer,
    "ga": GeneticAlgorithmOptimizer,
}
COST_DEFINITIONS = ("gross", "interest")
N_INSTRUMENTS = 7
WEIGHT_COLUMNS = [f"w_{i}" for i in range(1, N_INSTRUMENTS + 1)]

# Seed yang sudah dipakai proyek dan tidak boleh dipakai ulang oleh studi ini.
RESERVED_SEEDS = (42, 2026, 1042, 2042, 3042)


# ==============================================================================
# 1. Utilitas konfigurasi, berkas, dan penjaga tulis
# ==============================================================================

def load_config(config_path: Path) -> Dict[str, Any]:
    """Membaca configs/params.yaml."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def file_sha256(path: Path) -> str:
    """Hash SHA-256 sebuah berkas (dipakai untuk metadata config dan bank validasi)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_safe_output_dir(output_dir: Path, base_dir: Path) -> Path:
    """Menolak direktori keluaran di dalam results/runs atau results/tables.

    Hasil 360 run utama tidak boleh tertimpa oleh studi ini.
    """
    out = Path(output_dir).resolve()
    for forbidden in ("runs", "tables"):
        protected = (Path(base_dir) / "results" / forbidden).resolve()
        if out == protected or protected in out.parents:
            raise ValueError(
                f"output_dir '{out}' berada di folder terlindungi results/{forbidden}."
            )
    return out


def validate_study_seeds(bank_seed_base: int, n_banks: int, optimizer_seed_base: int) -> None:
    """Memastikan seed bank tidak beririsan dengan seed proyek yang sudah ada."""
    bank_seeds = {bank_seed_base + b for b in range(n_banks)}
    clash = bank_seeds.intersection(RESERVED_SEEDS)
    if clash:
        raise ValueError(f"Seed bank studi beririsan dengan seed terpakai: {sorted(clash)}")
    opt_seeds = {optimizer_seed_base + b for b in range(n_banks)}
    clash = opt_seeds.intersection(bank_seeds)
    if clash:
        raise ValueError(f"Seed optimizer beririsan dengan seed bank: {sorted(clash)}")


def split_config_id(config_id: str) -> Tuple[str, str]:
    """'interest_djppr' -> ('interest', 'djppr')."""
    cost_def, constraint = config_id.split("_", 1)
    return cost_def, constraint


# ==============================================================================
# 2. Bank skenario dan batas risiko
# ==============================================================================

def load_market_inputs(base_dir: Path, cfg: Dict[str, Any]) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Memuat parameter GBM, korelasi, dan S_0 (observasi terakhir jendela).

    Mengikuti alur scripts/04_generate_scenarios.py agar bank identik dengan bank utama.
    """
    window_mode = cfg["data"]["window_mode"]
    start_date = cfg["data"]["start_date"]
    end_date = cfg["data"]["end_date"]
    proc = Path(base_dir) / "data" / "processed"
    df_market = pd.read_csv(proc / f"market_{start_date}_{end_date}_{window_mode}.csv")
    df_params = pd.read_csv(proc / f"gbm_params_{window_mode}.csv")
    df_corr = pd.read_csv(proc / f"corr_{window_mode}.csv", index_col=0)
    s0_series = df_market.iloc[-1][ALL_MARKET_COLS]
    return df_params, df_corr, s0_series


def build_limit_bank(
    seed: int,
    n_scenarios: int,
    df_params: pd.DataFrame,
    df_corr: pd.DataFrame,
    s0_series: pd.Series,
    mode: str,
) -> Dict[str, Any]:
    """Membangkitkan satu bank skenario (GBM Pers. 2.11-2.12, biaya Pers. 2.2-2.3)."""
    sim_res = generate_market_scenarios(
        df_params=df_params,
        corr_matrix=df_corr,
        s0=s0_series,
        n_scenarios=n_scenarios,
        seed=int(seed),
        mode=mode,
        var_order=ALL_MARKET_COLS,
    )
    s0_dict = {col: float(s0_series[col]) for col in ALL_MARKET_COLS}
    return build_scenario_bank(
        market_scenarios=sim_res["scenarios_market"],
        log_returns=sim_res["scenarios_log_returns"],
        market_cols=ALL_MARKET_COLS,
        s0_dict=s0_dict,
        instruments=INSTRUMENTS,
    )


def make_evaluator(
    cost_matrix: np.ndarray,
    cfg: Dict[str, Any],
    tau: Optional[float] = None,
    eta: Optional[float] = None,
) -> PortfolioEvaluator:
    """Evaluator risiko dengan parameter dari config (tanpa angka ajaib)."""
    return PortfolioEvaluator(
        cost_matrix=cost_matrix,
        alpha=float(cfg["risk"]["alpha"]),
        delta=float(cfg["risk"]["delta"]),
        tau=tau,
        eta=eta,
        rho_J=float(cfg["optimization"]["penalty_rho_J"]),
        rho_R=float(cfg["optimization"]["penalty_rho_R"]),
        eps_tol=float(cfg["optimization"]["eps_tol"]),
        zero_tol_mc=float(cfg["risk"]["zero_tolerance_mc"]),
    )


def compute_bank_limits(bank: Dict[str, Any], cfg: Dict[str, Any]) -> Dict[str, Dict[str, float]]:
    """Batas eta dan tau dari w0 untuk kedua definisi biaya (Persamaan 2.22).

    tau = CCaR_alpha(w0) (Pers. 2.13), eta = J_MCCaR(w0) (Pers. 2.20).
    """
    out: Dict[str, Dict[str, float]] = {}
    for cost_def in COST_DEFINITIONS:
        ev = make_evaluator(bank[f"cost_{cost_def}"], cfg)
        base = ev.set_baseline(W0)
        out[cost_def] = {
            "tau": float(base["tau"]),
            "eta": float(base["eta"]),
            "w0_cost": float(base["mean_cost"]),
        }
    return out


def bank_matches_stored(bank: Dict[str, Any], stored_path: Path) -> bool:
    """True bila matriks biaya bank identik bit-by-bit dengan bank tersimpan."""
    stored = np.load(stored_path)
    return bool(
        np.array_equal(bank["cost_gross"], stored["cost_gross"])
        and np.array_equal(bank["cost_interest"], stored["cost_interest"])
    )


# ==============================================================================
# 3. Optimasi per bank (worker)
# ==============================================================================

def run_json_path(out_dir: Path, config_id: str, algo: str, bank_index: int, opt_seed: int) -> Path:
    """results/sensitivity/limits/runs/<config_id>/<algo>/bank_<bb>_seed<seed>.json."""
    return Path(out_dir) / "runs" / config_id / algo / f"bank_{bank_index:02d}_seed{opt_seed}.json"


def _atomic_write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    os.replace(tmp, path)


def optimize_task(task: Dict[str, Any]) -> Dict[str, Any]:
    """Menjalankan satu optimasi (bank b, konfigurasi, algoritma) lalu menulis JSON atomik."""
    config_id = task["config_id"]
    cost_def, constraint = split_config_id(config_id)
    lb, ub = get_bounds_for_constraint(constraint)
    evaluator = make_evaluator(task["cost_matrix"], task["cfg"], tau=task["tau"], eta=task["eta"])
    optimizer = ALGORITHM_CLASSES[task["algo"]]()
    res = optimizer.run(
        evaluator=evaluator,
        lb=lb,
        ub=ub,
        budget=int(task["budget"]),
        rng=int(task["opt_seed"]),
    )
    payload = {
        "metadata": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "config_hash": task["config_hash"],
            "validation_bank_sha256": task["validation_bank_sha256"],
            "data_version": task["data_version"],
        },
        "bank_index": int(task["bank_index"]),
        "bank_seed": int(task["bank_seed"]),
        "opt_seed": int(task["opt_seed"]),
        "config_id": config_id,
        "cost_definition": cost_def,
        "constraint_type": constraint,
        "algo": task["algo"],
        "budget": int(task["budget"]),
        "tau_b": float(task["tau"]),
        "eta_b": float(task["eta"]),
        "w0_cost_in": float(task["w0_cost"]),
        "best_cost": float(res.best_cost),
        "ccar_in": float(res.ccar),
        "j_mccar_in": float(res.j_mccar),
        "v_J_in": float(res.v_J),
        "v_R_in": float(res.v_R),
        "is_feasible_in": bool(res.is_feasible),
        "evaluations": int(res.evaluations_used),
        "time_seconds": float(res.elapsed_seconds),
        "weights": [float(x) for x in res.best_w],
    }
    _atomic_write_json(Path(task["json_path"]), payload)
    return payload


# ==============================================================================
# 4. Evaluasi validasi: batas sendiri (A) vs batas benar (B)
# ==============================================================================

def load_run_records(out_dir: Path) -> pd.DataFrame:
    """Membaca seluruh JSON run menjadi satu DataFrame (tanpa kolom validasi)."""
    rows: List[Dict[str, Any]] = []
    for p in sorted((Path(out_dir) / "runs").rglob("bank_*_seed*.json")):
        with open(p, "r", encoding="utf-8") as f:
            d = json.load(f)
        row = {k: v for k, v in d.items() if k not in ("weights", "metadata")}
        for i, w in enumerate(d["weights"], start=1):
            row[f"w_{i}"] = w
        row["config_hash"] = d["metadata"]["config_hash"]
        rows.append(row)
    return pd.DataFrame(rows)


def add_validation_columns(
    df_runs: pd.DataFrame,
    cost_valid: Dict[str, np.ndarray],
    cfg: Dict[str, Any],
) -> Tuple[pd.DataFrame, Dict[str, Dict[str, float]]]:
    """Menambah metrik validasi ke tiap run.

    Batas benar (B) = batas w0 pada bank validasi (tau_v, eta_v; m = 1.000 untuk N = 20.000).
    Batas sendiri (A) = (tau_b, eta_b) dari bank tempat optimasi dijalankan.
    """
    eps_tol = float(cfg["optimization"]["eps_tol"])
    evaluators: Dict[str, PortfolioEvaluator] = {}
    true_limits: Dict[str, Dict[str, float]] = {}
    for cost_def in COST_DEFINITIONS:
        ev = make_evaluator(cost_valid[cost_def], cfg)
        base = ev.set_baseline(W0)
        true_limits[cost_def] = {
            "tau": float(base["tau"]),
            "eta": float(base["eta"]),
            "w0_cost": float(base["mean_cost"]),
        }
        evaluators[cost_def] = ev

    out_rows: List[Dict[str, Any]] = []
    for _, r in df_runs.iterrows():
        cost_def = r["cost_definition"]
        ev = evaluators[cost_def]
        tv = true_limits[cost_def]
        lb, ub = get_bounds_for_constraint(r["constraint_type"])
        w = np.array([r[c] for c in WEIGHT_COLUMNS], dtype=float)

        ev.tau, ev.eta = float(r["tau_b"]), float(r["eta_b"])
        own = validate_single_portfolio(w, ev, lb, ub, eps_tol=eps_tol)
        ev.tau, ev.eta = tv["tau"], tv["eta"]
        true = validate_single_portfolio(w, ev, lb, ub, eps_tol=eps_tol)

        savings_in = 1.0 - r["best_cost"] / r["w0_cost_in"]
        savings_val = 1.0 - own["mean_cost"] / tv["w0_cost"]
        out_rows.append({
            "savings_in": savings_in,
            "mean_cost_val": own["mean_cost"],
            "w0_cost_val": tv["w0_cost"],
            "savings_val": savings_val,
            "optimism_gap": savings_in - savings_val,
            "tau_v": tv["tau"],
            "eta_v": tv["eta"],
            "eta_error_rel": (r["eta_b"] - tv["eta"]) / tv["eta"],
            "tau_error_rel": (r["tau_b"] - tv["tau"]) / tv["tau"],
            "v_J_own": own["v_J"],
            "v_R_own": own["v_R"],
            "feasible_own": bool(own["is_feasible"]),
            "v_J_true": true["v_J"],
            "v_R_true": true["v_R"],
            "feasible_true": bool(true["is_feasible"]),
            "is_weight_feasible": bool(own["is_weight_feasible"]),
        })
    df_val = pd.DataFrame(out_rows, index=df_runs.index)
    return pd.concat([df_runs, df_val], axis=1), true_limits


# ==============================================================================
# 5. Statistik ringkasan
# ==============================================================================

def bootstrap_mean_ci(
    values: Sequence[float], resamples: int, seed: int, level: float
) -> Tuple[float, float]:
    """CI bootstrap persentil untuk rata-rata (Generator ber-seed)."""
    x = np.asarray(values, dtype=float)
    if x.size == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(int(seed))
    idx = rng.integers(0, x.size, size=(int(resamples), x.size))
    means = x[idx].mean(axis=1)
    lo = (1.0 - level) / 2.0
    return (float(np.quantile(means, lo)), float(np.quantile(means, 1.0 - lo)))


def clopper_pearson(k: int, n: int, level: float) -> Tuple[float, float]:
    """CI Clopper-Pearson (eksak) untuk proporsi k/n."""
    if n <= 0:
        return (float("nan"), float("nan"))
    alpha = 1.0 - level
    lo = 0.0 if k == 0 else float(stats.beta.ppf(alpha / 2.0, k, n - k + 1))
    hi = 1.0 if k == n else float(stats.beta.ppf(1.0 - alpha / 2.0, k + 1, n - k))
    return (lo, hi)


def win_tie_loss(
    cost_a: Sequence[float], cost_b: Sequence[float], rel_tol: float
) -> Dict[str, int]:
    """Win-Tie-Loss A terhadap B pada biaya (lebih kecil = menang).

    Seri bila |a - b| <= rel_tol * max(|a|, |b|).
    """
    a = np.asarray(cost_a, dtype=float)
    b = np.asarray(cost_b, dtype=float)
    scale = np.maximum(np.maximum(np.abs(a), np.abs(b)), np.finfo(float).tiny)
    tie = np.abs(a - b) <= rel_tol * scale
    win = (a < b) & ~tie
    loss = (a > b) & ~tie
    return {"win": int(win.sum()), "tie": int(tie.sum()), "loss": int(loss.sum())}


def wilcoxon_paired_p(a: Sequence[float], b: Sequence[float]) -> float:
    """p-value Wilcoxon signed-rank dua sisi; NaN bila semua selisih nol."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    if np.all(d == 0):
        return float("nan")
    try:
        return float(stats.wilcoxon(d, alternative="two-sided").pvalue)
    except ValueError:
        return float("nan")


def summarize_limits(
    df_limits: pd.DataFrame,
    true_limits: Dict[str, Dict[str, float]],
    ref_limits: Dict[str, Dict[str, float]],
) -> pd.DataFrame:
    """Statistik batas antar bank + posisi bank-42 (ref) dan batas benar (validasi)."""
    rows: List[Dict[str, Any]] = []
    for cost_def in COST_DEFINITIONS:
        sub = df_limits[df_limits["cost_definition"] == cost_def]
        for metric in ("eta", "tau"):
            x = sub[metric].to_numpy(dtype=float)
            mean = float(x.mean())
            sd = float(x.std(ddof=1))
            ref = float(ref_limits[cost_def][metric])
            val = float(true_limits[cost_def][metric])
            rows.append({
                "cost_definition": cost_def,
                "metric": metric,
                "n_banks": int(x.size),
                "mean": mean,
                "sd": sd,
                "cv_percent": 100.0 * sd / mean,
                "min": float(x.min()),
                "q05": float(np.quantile(x, 0.05)),
                "q25": float(np.quantile(x, 0.25)),
                "median": float(np.median(x)),
                "q75": float(np.quantile(x, 0.75)),
                "q95": float(np.quantile(x, 0.95)),
                "max": float(x.max()),
                "bank42_value": ref,
                "bank42_z": (ref - mean) / sd,
                "bank42_percentile": float(np.mean(x <= ref)),
                "valid_bank_value": val,
                "valid_bank_z": (val - mean) / sd,
            })
    return pd.DataFrame(rows)


def reference_from_main_runs(
    runs_summary_path: Path, ref_limits: Dict[str, Dict[str, float]]
) -> pd.DataFrame:
    """Penghematan 360 run utama (bank-42), hanya dibaca. Dipakai sebagai pembanding."""
    d = pd.read_csv(runs_summary_path)
    d = d[d["algo"].isin(["pso", "ga"])].copy()
    d["w0_cost_ref"] = d["cost_definition"].map(lambda c: ref_limits[c]["w0_cost"])
    d["savings_ref"] = 1.0 - d["best_cost"] / d["w0_cost_ref"]
    return d


def build_study_tables(
    df_runs: pd.DataFrame,
    df_limits: pd.DataFrame,
    true_limits: Dict[str, Dict[str, float]],
    ref_limits: Dict[str, Dict[str, float]],
    runs_summary_path: Optional[Path],
    cfg: Dict[str, Any],
) -> Dict[str, pd.DataFrame]:
    """Menyusun seluruh tabel ringkasan studi (analisis 1-7 pada plan)."""
    sl = cfg["sensitivity_limits"]
    level = float(sl["confidence_level"])
    resamples = int(sl["bootstrap_resamples"])
    bseed = int(sl["bootstrap_seed"])
    rel_tol = float(sl["tie_relative_tolerance"])

    tables: Dict[str, pd.DataFrame] = {}
    tables["limits_summary"] = summarize_limits(df_limits, true_limits, ref_limits)

    ref_df = None
    if runs_summary_path is not None and Path(runs_summary_path).exists():
        ref_df = reference_from_main_runs(Path(runs_summary_path), ref_limits)

    # --- Penghematan ---------------------------------------------------------
    rows: List[Dict[str, Any]] = []
    for (cid, algo), g in df_runs.groupby(["config_id", "algo"], sort=True):
        row: Dict[str, Any] = {"config_id": cid, "algo": algo, "n_banks": int(len(g))}
        for col in ("savings_in", "savings_val", "optimism_gap"):
            x = g[col].to_numpy(dtype=float)
            lo, hi = bootstrap_mean_ci(x, resamples, bseed, level)
            row.update({
                f"{col}_mean": float(x.mean()),
                f"{col}_sd": float(x.std(ddof=1)) if x.size > 1 else float("nan"),
                f"{col}_ci_lo": lo,
                f"{col}_ci_hi": hi,
                f"{col}_q05": float(np.quantile(x, 0.05)),
                f"{col}_median": float(np.median(x)),
                f"{col}_q95": float(np.quantile(x, 0.95)),
            })
        feas = g[g["feasible_true"]]
        row["savings_val_mean_feasible_true"] = (
            float(feas["savings_val"].mean()) if len(feas) else float("nan")
        )
        row["n_feasible_true"] = int(len(feas))
        if ref_df is not None:
            rg = ref_df[(ref_df["config_id"] == cid) & (ref_df["algo"] == algo)]
            rg = rg[rg["is_feasible"]]
            row["savings_ref_bank42_median"] = (
                float(rg["savings_ref"].median()) if len(rg) else float("nan")
            )
        rows.append(row)
    tables["summary_savings"] = pd.DataFrame(rows)

    # --- Bobot ----------------------------------------------------------------
    rows = []
    for (cid, algo), g in df_runs.groupby(["config_id", "algo"], sort=True):
        for i, col in enumerate(WEIGHT_COLUMNS, start=1):
            row = {
                "config_id": cid, "algo": algo, "instrument_index": i,
                "w_mean": float(g[col].mean()),
                "w_sd": float(g[col].std(ddof=1)) if len(g) > 1 else float("nan"),
                "w_min": float(g[col].min()), "w_max": float(g[col].max()),
            }
            if ref_df is not None:
                rg = ref_df[(ref_df["config_id"] == cid) & (ref_df["algo"] == algo)]
                row["w_median_bank42"] = float(rg[col].median()) if len(rg) else float("nan")
            rows.append(row)
    tables["summary_weights"] = pd.DataFrame(rows)

    # --- Kelayakan validasi ------------------------------------------------------
    rows = []
    for (cid, algo), g in df_runs.groupby(["config_id", "algo"], sort=True):
        n = int(len(g))
        row = {"config_id": cid, "algo": algo, "n": n}
        for tag, col in (("in", "is_feasible_in"), ("own", "feasible_own"), ("true", "feasible_true")):
            k = int(g[col].sum())
            lo, hi = clopper_pearson(k, n, level)
            row.update({f"k_{tag}": k, f"prop_{tag}": k / n, f"cp_lo_{tag}": lo, f"cp_hi_{tag}": hi})
        rows.append(row)
    tables["summary_feasibility"] = pd.DataFrame(rows)

    # --- Stabilitas peringkat PSO vs GA ----------------------------------------------
    rows = []
    for cid, g in df_runs.groupby("config_id", sort=True):
        p = g[g["algo"] == "pso"].set_index("bank_index").sort_index()
        a = g[g["algo"] == "ga"].set_index("bank_index").sort_index()
        common = p.index.intersection(a.index)
        if len(common) == 0:
            continue
        p, a = p.loc[common], a.loc[common]
        for space, col in (("in_sample", "best_cost"), ("validation", "mean_cost_val")):
            wtl = win_tie_loss(p[col], a[col], rel_tol)
            row = {
                "config_id": cid, "space": space, "n_banks": int(len(common)),
                "pso_win": wtl["win"], "tie": wtl["tie"], "pso_loss": wtl["loss"],
                "wilcoxon_p": wilcoxon_paired_p(p[col], a[col]),
                "mean_rel_diff_pso_minus_ga": float(np.mean((p[col] - a[col]) / a[col])),
            }
            if ref_df is not None and space == "in_sample":
                rp = ref_df[(ref_df["config_id"] == cid) & (ref_df["algo"] == "pso")]["best_cost"].median()
                ra = ref_df[(ref_df["config_id"] == cid) & (ref_df["algo"] == "ga")]["best_cost"].median()
                row["bank42_median_pso_minus_ga"] = float(rp - ra)
            rows.append(row)
    tables["rank_stability"] = pd.DataFrame(rows)

    # --- Korelasi optimisme: galat batas vs penghematan ----------------------------------
    rows = []
    for (cid, algo), g in df_runs.groupby(["config_id", "algo"], sort=True):
        row = {"config_id": cid, "algo": algo, "n": int(len(g))}
        for xcol in ("eta_error_rel", "tau_error_rel"):
            if len(g) >= 3 and g[xcol].nunique() > 1 and g["savings_in"].nunique() > 1:
                rho, pval = stats.spearmanr(g[xcol], g["savings_in"])
                row[f"spearman_{xcol}_vs_savings_in"] = float(rho)
                row[f"p_{xcol}"] = float(pval)
            else:
                row[f"spearman_{xcol}_vs_savings_in"] = float("nan")
                row[f"p_{xcol}"] = float("nan")
        rows.append(row)
    tables["optimism_correlation"] = pd.DataFrame(rows)

    # --- Dekomposisi varians: antar-bank vs antar-replikasi (bank-42) ----------------------
    rows = []
    for (cid, algo), g in df_runs.groupby(["config_id", "algo"], sort=True):
        sd_between = float(g["savings_in"].std(ddof=1)) if len(g) > 1 else float("nan")
        row = {"config_id": cid, "algo": algo, "sd_between_banks": sd_between}
        if ref_df is not None:
            rg = ref_df[(ref_df["config_id"] == cid) & (ref_df["algo"] == algo)]
            sd_within = float(rg["savings_ref"].std(ddof=1)) if len(rg) > 1 else float("nan")
            row["sd_within_reps_bank42"] = sd_within
            row["ratio_between_over_within"] = (
                sd_between / sd_within if sd_within and sd_within > 0 else float("nan")
            )
        rows.append(row)
    tables["variance_decomposition"] = pd.DataFrame(rows)
    return tables


# ==============================================================================
# 6. Orkestrasi studi
# ==============================================================================

def run_study(
    cfg: Dict[str, Any],
    base_dir: Path,
    out_dir: Optional[Path] = None,
    n_banks: Optional[int] = None,
    budget: Optional[int] = None,
    configurations: Optional[Sequence[str]] = None,
    algorithms: Optional[Sequence[str]] = None,
    workers: Optional[int] = None,
    resume: bool = True,
    show_progress: bool = False,
) -> Dict[str, Any]:
    """Menjalankan studi penuh dan mengembalikan DataFrame hasil.

    Fase 1 (resumable): bangkitkan bank, hitung batas, optimasi, tulis satu JSON per run.
    Fase 2: baca JSON, evaluasi validasi (A dan B), tulis tabel ringkasan.
    """
    base_dir = Path(base_dir)
    sl = cfg["sensitivity_limits"]
    out = assert_safe_output_dir(
        Path(out_dir) if out_dir is not None else base_dir / sl["output_dir"], base_dir
    )
    out.mkdir(parents=True, exist_ok=True)

    n_banks = int(n_banks if n_banks is not None else sl["n_banks"])
    budget = int(budget if budget is not None else cfg["experiments"]["budget_evaluations"])
    configurations = list(configurations if configurations is not None else cfg["experiments"]["configurations"])
    algorithms = [a.lower() for a in (algorithms if algorithms is not None else sl["algorithms"])]
    workers = int(workers if workers is not None else sl["n_workers"])
    bank_seed_base = int(sl["bank_seed_base"])
    opt_seed_base = int(sl["optimizer_seed_base"])
    validate_study_seeds(bank_seed_base, n_banks, opt_seed_base)

    config_path = base_dir / "configs" / "params.yaml"
    config_hash = file_sha256(config_path)
    valid_path = base_dir / "data" / "processed" / (
        f"bank_valid_seed{int(cfg['scenarios']['validation_seed'])}_N{int(cfg['scenarios']['validation_scenarios'])}.npz"
    )
    valid_sha = file_sha256(valid_path)
    data_version = f"market_{cfg['data']['start_date']}_{cfg['data']['end_date']}_{cfg['data']['window_mode']}"

    df_params, df_corr, s0_series = load_market_inputs(base_dir, cfg)
    n_scen = int(cfg["scenarios"]["n_scenarios"])
    mode = cfg["scenarios"]["simulation_path_mode"]

    # --- Fase 1a: bank dan batas ---------------------------------------------------
    banks: List[Dict[str, Any]] = []
    limit_rows: List[Dict[str, Any]] = []
    for b in range(n_banks):
        seed_b = bank_seed_base + b
        bank = build_limit_bank(seed_b, n_scen, df_params, df_corr, s0_series, mode)
        lims = compute_bank_limits(bank, cfg)
        banks.append({
            "bank_index": b, "bank_seed": seed_b,
            "cost_gross": bank["cost_gross"], "cost_interest": bank["cost_interest"],
            "limits": lims,
        })
        for cost_def in COST_DEFINITIONS:
            limit_rows.append({
                "bank_index": b, "bank_seed": seed_b, "cost_definition": cost_def,
                "eta": lims[cost_def]["eta"], "tau": lims[cost_def]["tau"],
                "w0_cost": lims[cost_def]["w0_cost"],
            })
    df_limits = pd.DataFrame(limit_rows)
    df_limits.to_csv(out / "limits_per_bank.csv", index=False)

    # --- Fase 1b: optimasi (resumable) ------------------------------------------------
    tasks: List[Dict[str, Any]] = []
    for bk in banks:
        for cid in configurations:
            cost_def, _ = split_config_id(cid)
            for algo in algorithms:
                opt_seed = opt_seed_base + bk["bank_index"]
                jp = run_json_path(out, cid, algo, bk["bank_index"], opt_seed)
                if resume and jp.exists():
                    continue
                tasks.append({
                    "bank_index": bk["bank_index"], "bank_seed": bk["bank_seed"],
                    "opt_seed": opt_seed, "config_id": cid, "algo": algo, "budget": budget,
                    "cost_matrix": bk[f"cost_{cost_def}"],
                    "tau": bk["limits"][cost_def]["tau"], "eta": bk["limits"][cost_def]["eta"],
                    "w0_cost": bk["limits"][cost_def]["w0_cost"],
                    "cfg": cfg, "config_hash": config_hash,
                    "validation_bank_sha256": valid_sha, "data_version": data_version,
                    "json_path": str(jp),
                })

    if tasks:
        tasks.sort(key=lambda t: (t["config_id"] != "interest_free", t["bank_index"]))
        bar = None
        if show_progress:
            from tqdm import tqdm
            bar = tqdm(total=len(tasks), desc="Optimasi per bank")
        if workers <= 1:
            for t in tasks:
                optimize_task(t)
                if bar is not None:
                    bar.update(1)
        else:
            with ProcessPoolExecutor(max_workers=workers) as ex:
                futures = [ex.submit(optimize_task, t) for t in tasks]
                for fut in as_completed(futures):
                    fut.result()
                    if bar is not None:
                        bar.update(1)
        if bar is not None:
            bar.close()

    # --- Fase 2: validasi dan ringkasan --------------------------------------------------
    df_runs = load_run_records(out)
    df_runs = df_runs[
        df_runs["bank_index"].isin(range(n_banks))
        & df_runs["config_id"].isin(configurations)
        & df_runs["algo"].isin(algorithms)
    ].reset_index(drop=True)

    valid_bank = np.load(valid_path)
    cost_valid = {"gross": valid_bank["cost_gross"], "interest": valid_bank["cost_interest"]}
    df_runs, true_limits = add_validation_columns(df_runs, cost_valid, cfg)
    df_runs.to_csv(out / "runs_all.csv", index=False)

    ref_limits = load_reference_limits(base_dir)
    runs_summary_path = base_dir / "results" / "tables" / "runs_summary.csv"
    tables = build_study_tables(df_runs, df_limits, true_limits, ref_limits, runs_summary_path, cfg)
    for name, df in tables.items():
        df.to_csv(out / f"{name}.csv", index=False)

    return {
        "df_limits": df_limits,
        "df_runs": df_runs,
        "true_limits": true_limits,
        "ref_limits": ref_limits,
        "tables": tables,
        "out_dir": out,
    }


def load_reference_limits(base_dir: Path) -> Dict[str, Dict[str, float]]:
    """Batas bank utama (seed 42) dari risk_limits_bank_train_seed42_N5000.json (hanya dibaca)."""
    p = Path(base_dir) / "data" / "processed" / "risk_limits_bank_train_seed42_N5000.json"
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    return {
        cd: {
            "tau": float(d[cd]["tau"]),
            "eta": float(d[cd]["eta"]),
            "w0_cost": float(d[cd]["mean_cost"]),
        }
        for cd in COST_DEFINITIONS
    }
