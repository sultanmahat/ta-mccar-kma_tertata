"""Batas risiko portofolio (limits), baseline historis DJPPR, dan optimasi referensi SLSQP.

Mengimplementasikan:
1. Perhitungan batas acuan risiko eta dan tau dari portofolio eksisting 2024 (Persamaan 2.22):
   - tau = CCaR_alpha(w0) (Persamaan 2.13 & 2.22)
   - eta = J_MCCaR(w0)    (Persamaan 2.20 & 2.22)
2. Pembangkitan 1.000 kombinasi bobot acak DJPPR di dalam rentang batas proporsi [lb, ub]
   dengan rejection sampling (Keputusan D8, Opsi A).
3. Evaluasi baseline historis DJPPR (Persamaan 2.21, Subbab 3.6.1 proposal).
4. Solusi referensi independen menggunakan scipy.optimize.minimize (SLSQP multi-start)
   sebagai pembanding kasar ruang solusi layak.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union, TYPE_CHECKING
import json
import numpy as np
from scipy.optimize import minimize

if TYPE_CHECKING:
    from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.model.constraints import (
    LB_DJPPR,
    UB_DJPPR,
    W0,
    check_weight_feasibility,
    project_weights,
)


def compute_risk_limits(
    evaluator: PortfolioEvaluator,
    w0: np.ndarray = W0,
) -> Dict[str, Any]:
    """Menghitung batas acuan risiko eta dan tau dari portofolio eksisting w0 (Persamaan 2.22).

    Persamaan 2.22:
        tau = CCaR_alpha(w0)
        eta = J_MCCaR(w0)

    Sesuai spesifikasi §6:
    Threshold dihitung SEKALI pada bank latih untuk masing-masing definisi biaya,
    dan diverifikasi bahwa w0 layak by construction (v_J = 0, v_R = 0).

    Parameters
    ----------
    evaluator : PortfolioEvaluator
        Objek evaluator risiko yang sudah diinisialisasi dengan matriks biaya C.
    w0 : np.ndarray
        Vektor bobot portofolio eksisting (default: W0).

    Returns
    -------
    Dict[str, Any]
        Dictionary hasil evaluasi batas risiko w0:
        - 'w0': list float
        - 'mean_cost': float (Cost_bar(w0))
        - 'tau': float (CCaR_alpha(w0))
        - 'eta': float (J_MCCaR(w0))
        - 'mc': list float (MC_i)
        - 'mccar': list float (MCCaR_i)
        - 'theta': list float (theta_i)
        - 'theta_bar': float
        - 'v_J': float
        - 'v_R': float
        - 'is_feasible': bool
    """
    w0_arr = np.asarray(w0, dtype=float)

    # 1. Tetapkan baseline pada evaluator
    base = evaluator.set_baseline(w0_arr)
    tau = base["tau"]
    eta = base["eta"]

    # 2. Evaluasi lengkap w0 dengan penalti
    eval_w0 = evaluator.evaluate(w0_arr, apply_penalty=True)

    # Verifikasi bahwa w0 layak by construction
    if not eval_w0["is_feasible"]:
        raise ValueError(
            f"Portofolio eksisting w0 tidak layak pada batasnya sendiri! "
            f"v_J={eval_w0['v_J']}, v_R={eval_w0['v_R']}"
        )

    return {
        "w0": w0_arr.tolist(),
        "mean_cost": float(eval_w0["mean_cost"]),
        "tau": float(tau),
        "eta": float(eta),
        "mc": eval_w0["mc"].tolist(),
        "mccar": eval_w0["mccar"].tolist(),
        "theta": eval_w0["theta"].tolist(),
        "theta_bar": float(eval_w0["theta_bar"]),
        "v_J": float(eval_w0["v_J"]),
        "v_R": float(eval_w0["v_R"]),
        "is_feasible": bool(eval_w0["is_feasible"]),
    }


def save_risk_limits(
    filepath: Union[str, Path],
    limits_data: Dict[str, Any],
) -> None:
    """Menyimpan dictionary batas risiko ke file JSON terstruktur.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path file tujuan .json.
    limits_data : Dict[str, Any]
        Data batas risiko yang dihasilkan.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    def _convert_numpy(obj: Any) -> Any:
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, (np.floating, np.float64, np.float32)):
            return float(obj)
        if isinstance(obj, (np.integer, np.int64, np.int32)):
            return int(obj)
        if isinstance(obj, (np.bool_, bool)):
            return bool(obj)
        if isinstance(obj, dict):
            return {k: _convert_numpy(v) for k, v in obj.items()}
        if isinstance(obj, (list, tuple)):
            return [_convert_numpy(x) for x in obj]
        return obj

    clean_data = _convert_numpy(limits_data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(clean_data, f, indent=2)


def load_risk_limits(
    filepath: Union[str, Path],
) -> Dict[str, Any]:
    """Membaca file JSON batas risiko.

    Parameters
    ----------
    filepath : Union[str, Path]
        Path file .json.

    Returns
    -------
    Dict[str, Any]
        Dictionary data batas risiko.
    """
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"File batas risiko tidak ditemukan: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


def generate_random_weights_djppr(
    n_samples: int = 1000,
    lb: np.ndarray = LB_DJPPR,
    ub: np.ndarray = UB_DJPPR,
    rng: Optional[np.random.Generator] = None,
    method: str = "rejection",
    max_attempts: int = 200000,
    eps_tol: float = 1e-8,
) -> np.ndarray:
    """Membangkitkan n_samples kombinasi bobot acak di dalam rentang batas [lb, ub].

    Sesuai Keputusan D8:
    - Opsi A (default: 'rejection'): sampling seragam pada hiperkubus [lb, ub],
      normalisasi w = u / sum(u), terima jika lb <= w <= ub.
    - Opsi B ('projected'): sampling seragam pada [lb, ub] lalu diproyeksikan
      menggunakan project_weights.

    Parameters
    ----------
    n_samples : int
        Jumlah kombinasi acak yang dibangkitkan (default: 1.000).
    lb : np.ndarray
        Batas bawah proporsi (default: LB_DJPPR).
    ub : np.ndarray
        Batas atas proporsi (default: UB_DJPPR).
    rng : Optional[np.random.Generator]
        Generator acak NumPy dengan seed eksplisit.
    method : str
        Metode pembangkitan: 'rejection' (D8 Opsi A) atau 'projected' (D8 Opsi B).
    max_attempts : int
        Batas maksimum percobaan untuk rejection sampling.
    eps_tol : float
        Toleransi numerik (default: 1e-8).

    Returns
    -------
    np.ndarray
        Matriks bobot berukuran (n_samples, D) yang memenuhi sum(w)=1 dan lb <= w <= ub.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    lb = np.asarray(lb, dtype=float)
    ub = np.asarray(ub, dtype=float)
    d = len(lb)

    if method == "rejection":
        weights = []
        attempts = 0
        while len(weights) < n_samples and attempts < max_attempts:
            attempts += 1
            raw = rng.uniform(lb, ub)
            norm = raw / np.sum(raw)
            if np.all(norm >= lb - eps_tol) and np.all(norm <= ub + eps_tol):
                # Proyeksi presisi numerik halus ke 1e-8
                w_clean = project_weights(norm, lb, ub, eps_tol=eps_tol)
                weights.append(w_clean)

        if len(weights) < n_samples:
            raise RuntimeError(
                f"Rejection sampling hanya mengumpulkan {len(weights)}/{n_samples} sampel "
                f"setelah {attempts} percobaan."
            )
        return np.array(weights, dtype=float)

    elif method == "projected":
        weights = np.empty((n_samples, d), dtype=float)
        for i in range(n_samples):
            raw = rng.uniform(lb, ub)
            weights[i] = project_weights(raw, lb, ub, eps_tol=eps_tol)
        return weights

    else:
        raise ValueError(f"Metode sampling tidak dikenal: {method}. Pilih 'rejection' atau 'projected'.")


def evaluate_djppr_baseline(
    evaluator: PortfolioEvaluator,
    weights: np.ndarray,
) -> Dict[str, Any]:
    """Mengevaluasi populasi kombinasi bobot acak DJPPR terhadap batas risiko acuan.

    Parameters
    ----------
    evaluator : PortfolioEvaluator
        Evaluator portofolio dengan tau dan eta yang sudah ditetapkan.
    weights : np.ndarray
        Matriks bobot kombinasi acak berukuran (n_samples, D).

    Returns
    -------
    Dict[str, Any]
        Dictionary hasil evaluasi baseline lengkap:
        - 'n_samples': int
        - 'n_feasible': int
        - 'pct_feasible': float
        - 'batch_results': Dict hasil evaluate_batch
        - 'best_cost_feasible': Dict berisi bobot dan metrik solusi layak biaya terendah
        - 'best_balance_feasible': Dict berisi bobot dan metrik solusi layak rasio paling seimbang
    """
    if evaluator.tau is None or evaluator.eta is None:
        raise ValueError("Threshold tau dan eta belum ditentukan pada evaluator.")

    weights = np.asarray(weights, dtype=float)
    n_samples, d = weights.shape

    # 1. Evaluasi batch
    batch_res = evaluator.evaluate_batch(weights, apply_penalty=True)
    is_feasible = batch_res["is_feasible"]
    n_feasible = int(np.sum(is_feasible))
    pct_feasible = (n_feasible / n_samples) * 100.0

    # 2. Ekstrak solusi layak terbaik berdasarkan biaya minimum
    feasible_idx = np.where(is_feasible)[0]
    best_cost_sol = None
    best_balance_sol = None

    if n_feasible > 0:
        costs_feas = batch_res["mean_cost"][feasible_idx]
        best_cost_pos = feasible_idx[np.argmin(costs_feas)]

        best_cost_sol = {
            "index": int(best_cost_pos),
            "w": weights[best_cost_pos].tolist(),
            "mean_cost": float(batch_res["mean_cost"][best_cost_pos]),
            "ccar": float(batch_res["ccar"][best_cost_pos]),
            "j_mccar": float(batch_res["j_mccar"][best_cost_pos]),
            "v_J": float(batch_res["v_J"][best_cost_pos]),
            "v_R": float(batch_res["v_R"][best_cost_pos]),
            "theta": batch_res["theta"][best_cost_pos].tolist(),
            "theta_bar": float(batch_res["theta_bar"][best_cost_pos]),
        }

        # Keseimbangan rasio efisiensi: jarak deviasi rata-rata theta terhadap 1
        theta_feas = batch_res["theta"][feasible_idx]
        dev_from_one = np.mean(np.abs(theta_feas - 1.0), axis=1)
        best_bal_pos = feasible_idx[np.argmin(dev_from_one)]

        best_balance_sol = {
            "index": int(best_bal_pos),
            "w": weights[best_bal_pos].tolist(),
            "mean_cost": float(batch_res["mean_cost"][best_bal_pos]),
            "ccar": float(batch_res["ccar"][best_bal_pos]),
            "j_mccar": float(batch_res["j_mccar"][best_bal_pos]),
            "v_J": float(batch_res["v_J"][best_bal_pos]),
            "v_R": float(batch_res["v_R"][best_bal_pos]),
            "theta": batch_res["theta"][best_bal_pos].tolist(),
            "theta_bar": float(batch_res["theta_bar"][best_bal_pos]),
            "mean_abs_dev_from_one": float(np.min(dev_from_one)),
        }

    return {
        "n_samples": n_samples,
        "n_feasible": n_feasible,
        "pct_feasible": float(pct_feasible),
        "batch_results": batch_res,
        "best_cost_feasible": best_cost_sol,
        "best_balance_feasible": best_balance_sol,
    }


def solve_slsqp_reference(
    evaluator: PortfolioEvaluator,
    lb: np.ndarray = LB_DJPPR,
    ub: np.ndarray = UB_DJPPR,
    initial_points: Optional[List[np.ndarray]] = None,
    max_iter: int = 200,
    ftol: float = 1e-6,
) -> Dict[str, Any]:
    """Menyelesaikan optimasi referensi portofolio dengan SLSQP (scipy.optimize).

    Bertujuan sebagai sanity check kelayakan ruang solusi dan pembanding kasar:
    min_w Cost_bar(w)
    s.t.  J_MCCaR(w) <= eta
          CCaR_alpha(w) <= tau
          sum(w) = 1
          lb <= w <= ub

    Parameters
    ----------
    evaluator : PortfolioEvaluator
        Evaluator portofolio dengan tau dan eta yang sudah ditetapkan.
    lb : np.ndarray
        Batas bawah proporsi.
    ub : np.ndarray
        Batas atas proporsi.
    initial_points : Optional[List[np.ndarray]]
        Daftar titik awal. Jika None, menggunakan w0, midpoint, dan beberapa titik acak.
    max_iter : int
        Iterasi maksimum SLSQP per start.
    ftol : float
        Toleransi fungsi SLSQP.

    Returns
    -------
    Dict[str, Any]
        Dictionary hasil solusi referensi SLSQP terbaik yang layak.
    """
    if evaluator.tau is None or evaluator.eta is None:
        raise ValueError("Threshold tau dan eta belum ditentukan pada evaluator.")

    lb = np.asarray(lb, dtype=float)
    ub = np.asarray(ub, dtype=float)

    # 1. Definisi fungsi objektif dan kendala SLSQP
    # Biaya rata-rata linier dalam w
    mean_instrument_costs = np.mean(evaluator.C, axis=0)

    def obj(w: np.ndarray) -> float:
        return float(np.dot(mean_instrument_costs, w))

    def ccar_constraint(w: np.ndarray) -> float:
        # tau - CCaR(w) >= 0
        return float(evaluator.tau - evaluator.evaluate(w, apply_penalty=False)["ccar"])

    def j_constraint(w: np.ndarray) -> float:
        # eta - J_MCCaR(w) >= 0
        return float(evaluator.eta - evaluator.evaluate(w, apply_penalty=False)["j_mccar"])

    bounds = list(zip(lb, ub))
    constraints = [
        {"type": "eq", "fun": lambda w: float(np.sum(w) - 1.0)},
        {"type": "ineq", "fun": ccar_constraint},
        {"type": "ineq", "fun": j_constraint},
    ]

    # 2. Tentukan titik awal jika belum disediakan
    if initial_points is None:
        midpoint = (lb + ub) / 2.0
        midpoint_norm = midpoint / np.sum(midpoint)
        initial_points = [W0.copy(), midpoint_norm]

        # Tambahkan 3 titik acak dengan seed terisolasi
        rng = np.random.default_rng(2026)
        for _ in range(3):
            raw = rng.uniform(lb, ub)
            norm = raw / np.sum(raw)
            if np.all(norm >= lb) and np.all(norm <= ub):
                initial_points.append(norm)

    best_w = None
    best_eval = None
    best_cost = float("inf")
    converged_runs = []

    for i, w_init in enumerate(initial_points):
        res = minimize(
            obj,
            w_init,
            method="SLSQP",
            bounds=bounds,
            constraints=constraints,
            options={"maxiter": max_iter, "ftol": ftol},
        )

        w_opt = project_weights(res.x, lb, ub, eps_tol=evaluator.eps_tol)
        eval_res = evaluator.evaluate(w_opt, apply_penalty=True)
        is_feas = eval_res["is_feasible"]
        cost = eval_res["mean_cost"]

        run_info = {
            "start_index": i,
            "success": bool(res.success),
            "status": int(res.status),
            "message": str(res.message),
            "nit": int(res.nit),
            "w": w_opt.tolist(),
            "mean_cost": float(cost),
            "ccar": float(eval_res["ccar"]),
            "j_mccar": float(eval_res["j_mccar"]),
            "v_J": float(eval_res["v_J"]),
            "v_R": float(eval_res["v_R"]),
            "is_feasible": bool(is_feas),
        }
        converged_runs.append(run_info)

        if is_feas and cost < best_cost:
            best_cost = cost
            best_w = w_opt
            best_eval = eval_res

    if best_w is None:
        raise RuntimeError("SLSQP tidak menemukan solusi yang layak dari seluruh titik awal!")

    return {
        "best_w": best_w.tolist(),
        "mean_cost": float(best_eval["mean_cost"]),
        "ccar": float(best_eval["ccar"]),
        "j_mccar": float(best_eval["j_mccar"]),
        "v_J": float(best_eval["v_J"]),
        "v_R": float(best_eval["v_R"]),
        "is_feasible": bool(best_eval["is_feasible"]),
        "theta": best_eval["theta"].tolist(),
        "theta_bar": float(best_eval["theta_bar"]),
        "converged_runs": converged_runs,
    }
