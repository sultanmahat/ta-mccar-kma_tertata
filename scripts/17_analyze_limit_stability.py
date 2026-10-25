"""Tahap 17: Studi stabilitas batas risiko (eta, tau) antar bank latih independen.

Menjalankan B bank latih independen (seed terpisah dari 42 dan 2026), optimasi PSO dan GA
pada 4 konfigurasi, lalu evaluasi pada bank validasi dengan batas bank sendiri dan batas
"benar" (dari bank validasi). Semua parameter dibaca dari blok `sensitivity_limits` dan blok
`experiments` di configs/params.yaml.

Keluaran hanya ke results/sensitivity/limits/ (tidak menyentuh results/runs atau results/tables).

Contoh:
    python scripts/17_analyze_limit_stability.py --smoke
    python scripts/17_analyze_limit_stability.py
    python scripts/17_analyze_limit_stability.py --resume --workers 6
"""

import argparse
import logging
from pathlib import Path
import sys
import time

BASE_DIR = Path(__file__).resolve().parent.parent

from mccar_kma.analysis import limit_stability as ls  # noqa: E402
from mccar_kma.viz.limit_figures import make_all_figures  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("limit_stability")

SMOKE_N_BANKS = 2
SMOKE_BUDGET = 500


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--params", default="configs/params.yaml", help="Path params.yaml")
    p.add_argument("--smoke", action="store_true",
                   help=f"Uji cepat: {SMOKE_N_BANKS} bank, anggaran {SMOKE_BUDGET}, keluaran ke subfolder smoke/")
    p.add_argument("--n-banks", type=int, default=None, help="Menimpa sensitivity_limits.n_banks")
    p.add_argument("--workers", type=int, default=None, help="Menimpa sensitivity_limits.n_workers")
    p.add_argument("--no-resume", action="store_true", help="Jalankan ulang semua run (abaikan JSON yang ada)")
    p.add_argument("--skip-figures", action="store_true", help="Lewati pembuatan grafik")
    return p.parse_args()


def preflight_bank_check(cfg: dict) -> None:
    """Memastikan jalur kode studi menghasilkan bank seed 42 yang identik dengan bank utama."""
    df_params, df_corr, s0 = ls.load_market_inputs(BASE_DIR, cfg)
    bank = ls.build_limit_bank(
        int(cfg["scenarios"]["train_seed"]), int(cfg["scenarios"]["n_scenarios"]),
        df_params, df_corr, s0, cfg["scenarios"]["simulation_path_mode"],
    )
    stored = BASE_DIR / "data" / "processed" / (
        f"bank_train_seed{int(cfg['scenarios']['train_seed'])}_N{int(cfg['scenarios']['n_scenarios'])}.npz"
    )
    if not ls.bank_matches_stored(bank, stored):
        raise SystemExit("Preflight GAGAL: bank seed 42 dari studi tidak identik dengan bank utama.")
    logger.info("Preflight OK: bank seed 42 identik bit-by-bit dengan %s", stored.name)


def print_summary(result: dict) -> None:
    t = result["tables"]
    print("\n" + "=" * 90)
    print("RINGKASAN BATAS RISIKO ANTAR BANK")
    print("=" * 90)
    cols = ["cost_definition", "metric", "n_banks", "mean", "sd", "cv_percent",
            "bank42_value", "bank42_z", "valid_bank_value"]
    print(t["limits_summary"][cols].round(6).to_string(index=False))
    print("\nPENGHEMATAN (rata-rata antar bank, %)")
    s = t["summary_savings"]
    view = s[["config_id", "algo", "n_banks", "savings_in_mean", "savings_val_mean",
              "optimism_gap_mean"]].copy()
    for c in ("savings_in_mean", "savings_val_mean", "optimism_gap_mean"):
        view[c] = (view[c] * 100.0).round(3)
    if "savings_ref_bank42_median" in s.columns:
        view["ref_bank42_median"] = (s["savings_ref_bank42_median"] * 100.0).round(3)
    print(view.to_string(index=False))
    print("\nKELAYAKAN VALIDASI (k dari n)")
    print(t["summary_feasibility"][["config_id", "algo", "n", "k_in", "k_own", "k_true"]].to_string(index=False))
    print("\nSTABILITAS PERINGKAT PSO vs GA")
    print(t["rank_stability"].round(6).to_string(index=False))
    print("=" * 90)


def main() -> int:
    args = parse_args()
    cfg = ls.load_config(BASE_DIR / args.params)
    sl = cfg["sensitivity_limits"]

    out_dir = BASE_DIR / sl["output_dir"]
    n_banks = args.n_banks
    budget = None
    configurations = None
    if args.smoke:
        n_banks = SMOKE_N_BANKS
        budget = SMOKE_BUDGET
        out_dir = out_dir / "smoke"
    ls.assert_safe_output_dir(out_dir, BASE_DIR)

    logger.info("Keluaran: %s", out_dir)
    preflight_bank_check(cfg)

    t0 = time.perf_counter()
    result = ls.run_study(
        cfg=cfg,
        base_dir=BASE_DIR,
        out_dir=out_dir,
        n_banks=n_banks,
        budget=budget,
        configurations=configurations,
        workers=args.workers,
        resume=not args.no_resume,
        show_progress=True,
    )
    logger.info("Studi selesai dalam %.1f detik", time.perf_counter() - t0)

    if not args.skip_figures:
        make_all_figures(result, out_dir)
        logger.info("Grafik tersimpan di %s", out_dir)

    print_summary(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
