"""Skrip Pelari Eksperimen Penuh Optimasi Portofolio Utang Negara (Tahap 10).

Menjalankan matriks eksperimen komparasi KMA vs GA vs PSO:
- 4 Konfigurasi: gross_free, gross_djppr, interest_free, interest_djppr
- 3 Algoritma: kma, ga, pso
- 30 Replikasi per kombinasi (total 360 run)
- Anggaran: 25.000 evaluasi per run
- Mendukung fitur:
  * --dry-run: Menampilkan daftar run tanpa mengeksekusi
  * --pilot: Uji coba kecil (2 replikasi, 2.000 evaluasi)
  * --config: Filter konfigurasi tertentu
  * --algo: Filter algoritma tertentu
  * --workers: Menentukan jumlah proses paralel
  * --no-resume: Memaksa jalankan ulang run yang sudah ada
  * --summary-only: Hanya membuat file ringkasan CSV dari hasil yang ada
"""

import argparse
from datetime import datetime, timezone
import logging
import os
from pathlib import Path
import sys
import multiprocessing as mp

from mccar_kma.experiments.seeds import generate_experiment_matrix, ExperimentSpec
from mccar_kma.experiments.io import (
    build_runs_summary,
    get_run_result_path,
    is_run_completed,
)
from mccar_kma.experiments.runner import run_experiment_batch


def setup_logger(log_dir: Path) -> logging.Logger:
    """Mengatur logging console dan file ke folder logs/."""
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"run_experiments_{timestamp}.log"

    logger = logging.getLogger("mccar_kma.experiments")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(processName)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console Handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File Handler
    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.info("Logging diaktifkan ke: %s", log_file)
    return logger


def parse_arguments() -> argparse.Namespace:
    """Menguraikan argumen baris perintah (CLI)."""
    parser = argparse.ArgumentParser(
        description="Pelari Eksperimen Optimasi Portofolio Utang Multivaluta (MCCaR + KMA)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Hanya tampilkan matriks dan status kelengkapan run tanpa komputasi",
    )
    parser.add_argument(
        "--pilot",
        action="store_true",
        help="Jalankan mode pilot kecil: 2 replikasi dengan anggaran 2.000 evaluasi",
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        choices=["gross_free", "gross_djppr", "interest_free", "interest_djppr"],
        help="Filter hanya untuk konfigurasi tertentu",
    )
    parser.add_argument(
        "--algo",
        type=str,
        default=None,
        choices=["kma", "ga", "pso"],
        help="Filter hanya untuk algoritma tertentu",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Jumlah proses paralel (default: jumlah core - 1)",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Jalankan ulang run meskipun file hasil JSON yang valid sudah ada",
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Hanya buat file results/tables/runs_summary.csv dari data yang sudah ada",
    )
    parser.add_argument(
        "--reps",
        type=int,
        default=None,
        help="Jumlah replikasi per konfigurasi (default: 30 untuk eksperimen, 2 untuk pilot)",
    )
    parser.add_argument(
        "--budget",
        type=int,
        default=None,
        help="Anggaran evaluasi fungsi per run (default: 25.000 untuk eksperimen, 2.000 untuk pilot)",
    )
    parser.add_argument(
        "--bank",
        type=str,
        default="data/processed/bank_train_seed42_N5000.npz",
        help="Path ke bank skenario latih",
    )
    parser.add_argument(
        "--limits",
        type=str,
        default="data/processed/risk_limits_bank_train_seed42_N5000.json",
        help="Path ke file batas risiko JSON",
    )
    parser.add_argument(
        "--runs-dir",
        type=str,
        default="results/runs",
        help="Direktori penyimpanan file JSON hasil replikasi",
    )
    parser.add_argument(
        "--summary-csv",
        type=str,
        default="results/tables/runs_summary.csv",
        help="Lokasi file output ringkasan CSV",
    )
    return parser.parse_args()


def main() -> None:
    """Fungsi eksekusi utama pelari eksperimen."""
    args = parse_arguments()
    logger = setup_logger(Path("logs"))

    runs_dir = Path(args.runs_dir)
    summary_csv = Path(args.summary_csv)
    bank_path = Path(args.bank)
    limits_path = Path(args.limits)

    if args.summary_only:
        logger.info("Mode --summary-only aktif. Memindai %s...", runs_dir)
        df_summary = build_runs_summary(runs_dir=runs_dir, output_csv=summary_csv)
        print(f"\nRingkasan selesai: {len(df_summary)} replikasi tercatat di {summary_csv}")
        return

    # Tentukan parameter eksperimen
    configs = [args.config] if args.config else None
    algos = [args.algo] if args.algo else None
    base_seed = 42

    if args.pilot:
        replications = args.reps if args.reps is not None else 2
        budget = args.budget if args.budget is not None else 2000
        logger.info("MODE PILOT DIAKTIFKAN: %d replikasi, anggaran %d evaluasi", replications, budget)
    else:
        replications = args.reps if args.reps is not None else 30
        budget = args.budget if args.budget is not None else 25000

    matrix = generate_experiment_matrix(
        configurations=configs,
        algorithms=algos,
        base_seed=base_seed,
        replications=replications,
        budget=budget,
    )

    total_runs = len(matrix)
    completed_runs = sum(
        1
        for s in matrix
        if is_run_completed(
            get_run_result_path(
                base_dir=runs_dir,
                config_id=s.config_id,
                algo=s.algo_name,
                rep=s.rep,
                seed=s.seed,
            )
        )
    )
    pending_runs = total_runs - completed_runs

    logger.info("=" * 70)
    logger.info("STATUS MATRIKS EKSPERIMEN:")
    logger.info("Total Run Terencana  : %d", total_runs)
    logger.info("Run Selesai (Valid)  : %d", completed_runs)
    logger.info("Run Tertunda (Pending): %d", pending_runs)
    logger.info("=" * 70)

    if args.dry_run:
        print("\n[DRY RUN] Daftar spesifikasi run:")
        for idx, s in enumerate(matrix, start=1):
            target_path = get_run_result_path(
                base_dir=runs_dir,
                config_id=s.config_id,
                algo=s.algo_name,
                rep=s.rep,
                seed=s.seed,
            )
            status = "SELESAI" if is_run_completed(target_path) else "PENDING"
            print(f"[{idx:03d}/{total_runs:03d}] {s.run_id:<40} Budget={s.budget} [{status}]")
        print("\nDry run selesai. Tidak ada komputasi yang dijalankan.")
        return

    # Validasi keberadaan bank dan limits
    if not bank_path.exists():
        logger.error("Bank skenario tidak ditemukan di: %s", bank_path)
        sys.exit(1)
    if not limits_path.exists():
        logger.error("Batas risiko tidak ditemukan di: %s", limits_path)
        sys.exit(1)

    # Tentukan workers
    if args.workers is not None:
        max_workers = max(1, args.workers)
    else:
        cpu_cnt = os.cpu_count() or 2
        max_workers = max(1, cpu_cnt - 1)

    logger.info("Menjalankan eksperimen dengan %d worker...", max_workers)

    resume = not args.no_resume
    run_experiment_batch(
        specs=matrix,
        bank_path=bank_path,
        limits_path=limits_path,
        output_dir=runs_dir,
        max_workers=max_workers,
        resume=resume,
    )

    # Perbarui ringkasan agregat CSV
    logger.info("Memperbarui tabel ringkasan agregat runs...")
    df_summary = build_runs_summary(runs_dir=runs_dir, output_csv=summary_csv)
    logger.info(
        "Eksperimen selesai! Total %d run tersimpan di %s dan teragregasi di %s",
        len(df_summary),
        runs_dir,
        summary_csv,
    )


if __name__ == "__main__":
    mp.freeze_support()
    main()
