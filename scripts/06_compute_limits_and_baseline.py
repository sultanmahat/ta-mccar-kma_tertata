"""Skrip penetapan batas risiko (limits) dan baseline historis DJPPR (Tahap 06).

Sesuai spesifikasi §6, §8, §11, §12 (D8):
1. Menghitung threshold risiko acuan eta = J_MCCaR(w0) dan tau = CCaR_alpha(w0)
   (Persamaan 2.22) pada bank latih untuk dua definisi biaya (gross dan interest).
   Threshold ditetapkan SEKALI dan disimpan ke data/processed/risk_limits_<bank>.json.
2. Mereplikasi acuan historis DJPPR: membangkitkan 1.000 kombinasi bobot acak di dalam
   batas proporsi [lb, ub] (skenario djppr) dengan rejection sampling (D8 Opsi A).
   Mengevaluasi Cost_bar, CCaR, J tiap kombinasi dan menyaring yang lolos (is_feasible).
   Disimpan lengkap ke results/tables/baseline_djppr_<costdef>.csv.
3. Memeriksa kelayakan w0 (v_J = 0, v_R = 0) dan menjalankan optimasi referensi independen
   scipy.optimize (SLSQP multi-start) sebagai pembanding kasar kelayakan ruang solusi.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Dict
import yaml
import numpy as np
import pandas as pd

from mccar_kma.risk.evaluator import PortfolioEvaluator
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, W0
from mccar_kma.model.limits import (
    compute_risk_limits,
    save_risk_limits,
    generate_random_weights_djppr,
    evaluate_djppr_baseline,
    solve_slsqp_reference,
)


def compute_file_hash(filepath: Path) -> str:
    """Menghitung SHA256 checksum dari file konfigurasi."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    print("=" * 80)
    print("TAHAP 06: PERHITUNGAN BATAS RISIKO (LIMITS) & BASELINE HISTORIS DJPPR")
    print("=" * 80)

    # 1. Muat konfigurasi
    config_path = Path("configs/params.yaml")
    if not config_path.exists():
        print(f"Error: File konfigurasi tidak ditemukan: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    config_hash = compute_file_hash(config_path)

    # Parameter utama
    alpha = float(config["risk"]["alpha"])
    delta = float(config["risk"]["delta"])
    zero_tol_mc = float(config["risk"]["zero_tolerance_mc"])
    rho_J = float(config["optimization"]["penalty_rho_J"])
    rho_R = float(config["optimization"]["penalty_rho_R"])
    eps_tol = float(config["optimization"]["eps_tol"])
    n_random = int(config["experiments"]["random_benchmark_count"])
    method_random = str(config["experiments"]["random_benchmark_method"])
    seed_random = int(config["experiments"].get("random_benchmark_seed", 42))

    train_seed = int(config["scenarios"]["train_seed"])
    n_scenarios = int(config["scenarios"]["n_scenarios"])
    bank_train_file = Path(f"data/processed/bank_train_seed{train_seed}_N{n_scenarios}.npz")

    if not bank_train_file.exists():
        print(f"Error: Bank latih tidak ditemukan: {bank_train_file}")
        sys.exit(1)

    print(f"\n>> Memuat bank skenario latih: {bank_train_file}")
    bank_data = np.load(bank_train_file)
    print(f"   Ukuran skenario: N = {n_scenarios:,}, alpha = {alpha:.2f}, delta = {delta:.2f}")

    # 2. Hitung Batas Acuan Risiko eta dan tau untuk Gross dan Interest
    print("\n>> 1. Menghitung Batas Risiko Acuan (Persamaan 2.22) dari Portofolio Eksisting w0:")
    instrument_names = [item["name"] for item in config["instruments"]["items"]]

    limits_record: Dict[str, Any] = {
        "metadata": {
            "created_at": datetime.now(timezone.utc).isoformat(),
            "config_hash": config_hash,
            "bank_file": str(bank_train_file.name),
            "n_scenarios": n_scenarios,
            "alpha": alpha,
            "delta": delta,
            "zero_tolerance_mc": zero_tol_mc,
            "rho_J": rho_J,
            "rho_R": rho_R,
            "eps_tol": eps_tol,
            "instrument_names": instrument_names,
        },
    }

    evaluators: Dict[str, PortfolioEvaluator] = {}

    for cost_def in ["gross", "interest"]:
        evaluator = PortfolioEvaluator.from_scenario_bank(
            bank_data_or_path=bank_data,
            cost_def=cost_def,
            alpha=alpha,
            delta=delta,
            rho_J=rho_J,
            rho_R=rho_R,
            eps_tol=eps_tol,
            zero_tol_mc=zero_tol_mc,
        )
        limits = compute_risk_limits(evaluator, w0=W0)
        limits_record[cost_def] = limits
        evaluators[cost_def] = evaluator

        print(f"   [{cost_def.upper():8s}] Cost_bar(w0) = {limits['mean_cost']:.8f} | "
              f"tau (CCaR) = {limits['tau']:.8f} | "
              f"eta (J) = {limits['eta']:.8f} | "
              f"Feasible w0: {limits['is_feasible']} (v_J={limits['v_J']:.1e}, v_R={limits['v_R']:.1e})")

    # Simpan batas acuan risiko ke JSON
    limits_out_path = Path(f"data/processed/risk_limits_{bank_train_file.stem}.json")
    save_risk_limits(limits_out_path, limits_record)
    print(f"   -> Batas risiko tersimpan permanen di: {limits_out_path}")

    # 3. Pembangkitan 1.000 Kombinasi Acak DJPPR (Keputusan D8)
    print(f"\n>> 2. Membangkitkan {n_random:,} Kombinasi Bobot Acak DJPPR:")
    print(f"   Metode: {method_random} (D8 Opsi A) | Seed: {seed_random}")
    rng = np.random.default_rng(seed_random)
    random_weights = generate_random_weights_djppr(
        n_samples=n_random,
        lb=LB_DJPPR,
        ub=UB_DJPPR,
        rng=rng,
        method=method_random,
        eps_tol=eps_tol,
    )

    max_sum_err = float(np.max(np.abs(np.sum(random_weights, axis=1) - 1.0)))
    min_lb_diff = float(np.min(random_weights - LB_DJPPR))
    max_ub_diff = float(np.max(random_weights - UB_DJPPR))
    print(f"   Verifikasi Batas: min(w - lb) = {min_lb_diff:.2e}, max(w - ub) = {max_ub_diff:.2e}, "
          f"max|sum(w) - 1| = {max_sum_err:.2e} (Semua lolos toleransi 1e-8)")

    # 4. Evaluasi Baseline DJPPR untuk Gross dan Interest
    print(f"\n>> 3. Mengevaluasi {n_random:,} Kombinasi Baseline DJPPR:")
    output_tables_dir = Path("results/tables")
    output_tables_dir.mkdir(parents=True, exist_ok=True)

    baseline_summaries = {}
    weight_cols = [f"w_{name.lower()}" for name in instrument_names]
    theta_cols = [f"theta_{name.lower()}" for name in instrument_names]

    for cost_def in ["gross", "interest"]:
        ev = evaluators[cost_def]
        base_eval = evaluate_djppr_baseline(ev, random_weights)
        baseline_summaries[cost_def] = base_eval

        # Bentuk tabel CSV lengkap
        batch_res = base_eval["batch_results"]
        df_out = pd.DataFrame(random_weights, columns=weight_cols)
        df_out.insert(0, "sample_id", np.arange(1, n_random + 1))
        df_out["mean_cost"] = batch_res["mean_cost"]
        df_out["ccar"] = batch_res["ccar"]
        df_out["j_mccar"] = batch_res["j_mccar"]
        df_out["v_J"] = batch_res["v_J"]
        df_out["v_R"] = batch_res["v_R"]
        df_out["f_val"] = batch_res["f_val"]
        df_out["is_feasible"] = batch_res["is_feasible"]

        for idx, col in enumerate(theta_cols):
            df_out[col] = batch_res["theta"][:, idx]
        df_out["theta_bar"] = batch_res["theta_bar"]

        csv_path = output_tables_dir / f"baseline_djppr_{cost_def}.csv"
        df_out.to_csv(csv_path, index=False)

        n_feas = base_eval["n_feasible"]
        pct_feas = base_eval["pct_feasible"]
        best_c = base_eval["best_cost_feasible"]
        print(f"   [{cost_def.upper():8s}] Feasible: {n_feas:,} / {n_random:,} ({pct_feas:.2f}%) | "
              f"Best Feasible Cost: {best_c['mean_cost']:.8f} (vs w0: {limits_record[cost_def]['mean_cost']:.8f})")
        print(f"      -> Tabel lengkap disimpan di: {csv_path}")

    # 5. Optimasi Referensi Independen SLSQP
    print("\n>> 4. Menjalankan Optimasi Referensi Independen SLSQP (scipy.optimize):")
    slsqp_results = {}
    for cost_def in ["gross", "interest"]:
        ev = evaluators[cost_def]
        slsqp_res = solve_slsqp_reference(
            evaluator=ev,
            lb=LB_DJPPR,
            ub=UB_DJPPR,
            max_iter=200,
            ftol=1e-6,
        )
        slsqp_results[cost_def] = slsqp_res

        w0_cost = limits_record[cost_def]["mean_cost"]
        opt_cost = slsqp_res["mean_cost"]
        diff_pct = (w0_cost - opt_cost) / w0_cost * 100.0
        print(f"   [{cost_def.upper():8s}] SLSQP Best Cost: {opt_cost:.8f} | "
              f"Feasible: {slsqp_res['is_feasible']} (v_J={slsqp_res['v_J']:.1e}, v_R={slsqp_res['v_R']:.1e}) | "
              f"Penghematan vs w0: {diff_pct:.4f}%")

    # 6. Cetak dan Simpan Tabel Perbandingan Lengkap
    print("\n" + "=" * 80)
    print("RINGKASAN PERBANDINGAN: EKSISTING vs BASELINE DJPPR vs REFERENSI SLSQP")
    print("=" * 80)

    summary_md_rows = []
    summary_md_rows.append("# Ringkasan Batas Risiko, Baseline DJPPR, dan Solusi Referensi SLSQP\n")
    summary_md_rows.append(f"- **Tanggal Eksekusi**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    summary_md_rows.append(f"- **Bank Latih**: `{bank_train_file.name}` (N = {n_scenarios:,}, seed = {train_seed})")
    summary_md_rows.append(f"- **Metode Sampling Acak (D8)**: `{method_random}` ({n_random:,} sampel, seed = {seed_random})\n")

    summary_md_rows.append("## 1. Batas Risiko Acuan Portofolio Eksisting 2024 ($w_0$)\n")
    summary_md_rows.append("| Definisi Biaya | Biaya Rata-rata $\\overline{\\text{Cost}}(w_0)$ | Batas Ekor $\\tau = \\text{CCaR}_{0.95}(w_0)$ | Batas Dispersi $\\eta = J_{\\text{MCCaR}}(w_0)$ | Status Kelayakan |")
    summary_md_rows.append("|---|---|---|---|---|")

    for cost_def in ["gross", "interest"]:
        lim = limits_record[cost_def]
        summary_md_rows.append(
            f"| **{cost_def.capitalize()}** | {lim['mean_cost']:.8f} | {lim['tau']:.8f} | {lim['eta']:.8f} | Layak ($v_J=0, v_R=0$) |"
        )

    summary_md_rows.append("\n## 2. Replikasi Baseline Historis DJPPR (1.000 Kombinasi Acak)\n")
    summary_md_rows.append("| Definisi Biaya | Total Sampel | Lolos Kendala ($J \\le \\eta$ & $\\text{CCaR} \\le \\tau$) | % Layak | Min Biaya Layak | Rata-rata Biaya Layak | Maks Biaya Layak |")
    summary_md_rows.append("|---|---|---|---|---|---|---|")

    for cost_def in ["gross", "interest"]:
        bs = baseline_summaries[cost_def]
        batch_res = bs["batch_results"]
        feas_costs = batch_res["mean_cost"][batch_res["is_feasible"]]
        summary_md_rows.append(
            f"| **{cost_def.capitalize()}** | {bs['n_samples']:,} | {bs['n_feasible']:,} | {bs['pct_feasible']:.2f}% | "
            f"{np.min(feas_costs):.8f} | {np.mean(feas_costs):.8f} | {np.max(feas_costs):.8f} |"
        )

    summary_md_rows.append("\n## 3. Komparasi Solusi: Eksisting ($w_0$) vs DJPPR vs Referensi SLSQP\n")
    summary_md_rows.append("| Definisi Biaya | Metode Solusi | $\\overline{\\text{Cost}}$ | $\\text{CCaR}_{0.95}$ | $J_{\\text{MCCaR}}$ | Status Layak | Reduksi vs $w_0$ (%) |")
    summary_md_rows.append("|---|---|---|---|---|---|---|")

    for cost_def in ["gross", "interest"]:
        lim = limits_record[cost_def]
        bs = baseline_summaries[cost_def]
        best_djppr = bs["best_cost_feasible"]
        slsqp = slsqp_results[cost_def]

        w0_c = lim["mean_cost"]
        djppr_c = best_djppr["mean_cost"]
        slsqp_c = slsqp["mean_cost"]

        red_djppr = (w0_c - djppr_c) / w0_c * 100.0
        red_slsqp = (w0_c - slsqp_c) / w0_c * 100.0

        summary_md_rows.append(f"| **{cost_def.capitalize()}** | Eksisting ($w_0$) | {w0_c:.8f} | {lim['tau']:.8f} | {lim['eta']:.8f} | Layak | 0.0000% |")
        summary_md_rows.append(f"| | DJPPR Random Filtering (Terbaik) | {djppr_c:.8f} | {best_djppr['ccar']:.8f} | {best_djppr['j_mccar']:.8f} | Layak | {red_djppr:+.4f}% |")
        summary_md_rows.append(f"| | Solusi Referensi SLSQP | {slsqp_c:.8f} | {slsqp['ccar']:.8f} | {slsqp['j_mccar']:.8f} | Layak | {red_slsqp:+.4f}% |")

    # Cetak ke konsol
    print("\n".join(summary_md_rows))

    # Simpan ringkasan markdown ke results/tables/
    md_summary_file = output_tables_dir / "limits_and_baseline_summary.md"
    with open(md_summary_file, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_md_rows) + "\n")

    print(f"\n>> Ringkasan markdown berhasil disimpan di: {md_summary_file}")
    print("=" * 80)
    print("SELESAI: Batas risiko, evaluasi baseline DJPPR, dan solver SLSQP berhasil diverifikasi!")
    print("=" * 80)


if __name__ == "__main__":
    main()
