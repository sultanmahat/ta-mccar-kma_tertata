"""Skrip Tahap 12 — Validasi independen dan pembanding solusi portofolio utang.

Mengevaluasi ulang seluruh solusi optimal dari eksperimen penuh (360 run) pada
bank skenario validasi independen (N=20.000, seed 2026, m=1.000).
Memeriksa kendala bobot, kepatuhan batas risiko bank latih (tau dan eta),
serta membandingkan performa terhadap Eksisting 2024 dan Baseline DJPPR.

Keluaran:
- results/tables/validation_gross_free.csv
- results/tables/validation_gross_djppr.csv
- results/tables/validation_interest_free.csv
- results/tables/validation_interest_djppr.csv
- results/tables/validation_all_runs.csv
- results/tables/validation_summary.md
"""

from pathlib import Path
import argparse
import time
import pandas as pd

from mccar_kma.analysis.validation import (
    validate_all_runs,
    evaluate_benchmarks_validation,
    generate_validation_comparison_tables,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validasi independen 360 solusi pada bank skenario N=20.000.")
    parser.add_argument("--params", type=str, default="configs/params.yaml", help="Path ke params.yaml")
    parser.add_argument(
        "--bank-valid",
        type=str,
        default="data/processed/bank_valid_seed2026_N20000.npz",
        help="Path ke bank validasi .npz",
    )
    parser.add_argument(
        "--limits",
        type=str,
        default="data/processed/risk_limits_bank_train_seed42_N5000.json",
        help="Path ke batas risiko acuan bank latih JSON",
    )
    parser.add_argument(
        "--runs-summary",
        type=str,
        default="results/tables/runs_summary.csv",
        help="Path ke runs_summary.csv",
    )
    parser.add_argument(
        "--baseline-gross",
        type=str,
        default="results/tables/baseline_djppr_gross.csv",
        help="Path ke baseline DJPPR gross CSV",
    )
    parser.add_argument(
        "--baseline-interest",
        type=str,
        default="results/tables/baseline_djppr_interest.csv",
        help="Path ke baseline DJPPR interest CSV",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="results/tables",
        help="Direktori keluaran tabel dan ringkasan",
    )
    parser.add_argument(
        "--eps-tol",
        type=float,
        default=1e-8,
        help="Toleransi numerik kendala (default: 1e-8)",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("TAHAP 12 — VALIDASI INDEPENDEN DAN PEMBANDING SOLUSI PORTOFOLIO")
    print("=" * 78)
    print(f"Bank Validasi    : {args.bank_valid}")
    print(f"Batas Risiko     : {args.limits}")
    print(f"Hasil Eksperimen : {args.runs_summary}")
    print(f"Toleransi Kendala: {args.eps_tol:.1e}")
    print("-" * 78)

    t0 = time.perf_counter()

    # 1. Validasi seluruh 360 solusi
    print("\n[1/4] Mengevaluasi 360 solusi run pada bank validasi N=20.000...")
    val_df = validate_all_runs(
        runs_summary_path=args.runs_summary,
        bank_valid_path=args.bank_valid,
        limits_path=args.limits,
        params_path=args.params,
        eps_tol=args.eps_tol,
    )
    print(f"      -> Selesai mengevaluasi {len(val_df)} solusi.")

    # 2. Periksa kendala bobot
    print("\n[2/4] Memeriksa ulang kendala bobot (sum(w)=1 dan batas proporsi)...")
    max_sum_err = val_df["val_max_sum_err"].max()
    max_bound_err = val_df["val_max_bound_err"].max()
    n_weight_feas = val_df["val_weight_feasible"].sum()
    print(f"      -> Maksimum galat penjumlahan : {max_sum_err:.3e} (<= {args.eps_tol:.1e}: {max_sum_err <= args.eps_tol})")
    print(f"      -> Maksimum pelanggaran batas : {max_bound_err:.3e} (<= {args.eps_tol:.1e}: {max_bound_err <= args.eps_tol})")
    print(f"      -> Kelayakan bobot            : {n_weight_feas} / {len(val_df)} ({(n_weight_feas/len(val_df))*100:.2f}%)")

    # 3. Evaluasi pembanding (w0 dan baseline DJPPR)
    print("\n[3/4] Mengevaluasi portofolio pembanding (Eksisting w0 & Baseline DJPPR)...")
    benchmarks = evaluate_benchmarks_validation(
        bank_valid_path=args.bank_valid,
        limits_path=args.limits,
        baseline_gross_csv=args.baseline_gross,
        baseline_interest_csv=args.baseline_interest,
        params_path=args.params,
        eps_tol=args.eps_tol,
    )
    print("      -> Portofolio eksisting w0 dan titik acak baseline DJPPR berhasil dievaluasi.")

    # 4. Susun tabel dan markdown ringkasan
    print("\n[4/4] Menyusun tabel komparasi dan ringkasan markdown...")
    config_tables, summary_md = generate_validation_comparison_tables(
        val_df=val_df,
        benchmarks_dict=benchmarks,
        params_path=args.params,
    )

    # Simpan berkas
    # a. Berkas CSV per konfigurasi
    for cid, tbl in config_tables.items():
        out_csv = output_dir / f"validation_{cid}.csv"
        # Simpan juga run individu validasi per config
        cfg_runs = val_df[val_df["config_id"] == cid]
        cfg_runs.to_csv(out_csv, index=False)
        print(f"      -> Tersimpan: {out_csv} ({len(cfg_runs)} baris)")

    # b. Berkas gabungan seluruh 360 run
    all_runs_csv = output_dir / "validation_all_runs.csv"
    val_df.to_csv(all_runs_csv, index=False)
    print(f"      -> Tersimpan: {all_runs_csv} ({len(val_df)} baris)")

    # c. Berkas ringkasan markdown
    summary_md_path = output_dir / "validation_summary.md"
    with open(summary_md_path, "w", encoding="utf-8") as f:
        f.write(summary_md)
    print(f"      -> Tersimpan: {summary_md_path}")

    elapsed = time.perf_counter() - t0
    print("-" * 78)
    print(f"VALIDASI SELESAI dalam {elapsed:.2f} detik.")
    print("=" * 78)


if __name__ == "__main__":
    main()
