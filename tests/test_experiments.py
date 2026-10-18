"""Pengujian Unit & Integrasi untuk Subpaket Eksperimen (Tahap 10).

Menguji:
1. Pembangkitan seed replikasi deterministik & adil antar algoritma.
2. Dimensi matriks eksperimen penuh (360 run) dan pilot.
3. Integritas penyimpanan atomic dan deteksi file JSON hasil yang korup/lengkap.
4. Fitur resumability (melewati run yang sudah valid).
5. Eksekusi single run pilot dan agregasi CSV ringkasan runs.
"""

from pathlib import Path
import json
import pytest
import numpy as np

from mccar_kma.experiments.seeds import (
    get_replication_seeds,
    generate_experiment_matrix,
    compute_spec_hash,
    ExperimentSpec,
)
from mccar_kma.experiments.io import (
    get_run_result_path,
    is_run_completed,
    save_run_result,
    load_run_result,
    build_runs_summary,
)
from mccar_kma.experiments.runner import execute_single_run, get_bounds_for_constraint
from mccar_kma.model.constraints import LB_DJPPR, UB_DJPPR, LB_FREE, UB_FREE


def test_replication_seeds_determinism():
    """Uji bahwa seed replikasi deterministik dan identik antar algoritma."""
    seeds_30 = get_replication_seeds(base_seed=42, replications=30)
    assert len(seeds_30) == 30
    assert seeds_30[0] == 43
    assert seeds_30[-1] == 72
    assert len(set(seeds_30)) == 30, "Semua seed harus unik"

    # Periksa kesamaan seed antar algoritma pada matriks eksperimen
    matrix = generate_experiment_matrix(base_seed=42, replications=30)
    assert len(matrix) == 4 * 3 * 30  # 360 runs

    # Untuk setiap konfigurasi dan replikasi k, KMA, GA, dan PSO harus memiliki seed yang persis sama
    for cfg in ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]:
        for rep in range(1, 31):
            specs = [s for s in matrix if s.config_id == cfg and s.rep == rep]
            assert len(specs) == 3
            seeds = [s.seed for s in specs]
            assert seeds[0] == seeds[1] == seeds[2] == 42 + rep


def test_experiment_spec_hash():
    """Uji konsistensi hash spesifikasi eksperimen."""
    spec1 = ExperimentSpec("gross_djppr", "gross", "djppr", "kma", 1, 43, 25000)
    spec2 = ExperimentSpec("gross_djppr", "gross", "djppr", "kma", 1, 43, 25000)
    spec3 = ExperimentSpec("gross_djppr", "gross", "djppr", "ga", 1, 43, 25000)

    hash1 = compute_spec_hash(spec1)
    hash2 = compute_spec_hash(spec2)
    hash3 = compute_spec_hash(spec3)

    assert hash1 == hash2
    assert hash1 != hash3


def test_bounds_selector():
    """Uji pemilih batas proporsi djppr vs free."""
    lb_d, ub_d = get_bounds_for_constraint("djppr")
    np.testing.assert_allclose(lb_d, LB_DJPPR)
    np.testing.assert_allclose(ub_d, UB_DJPPR)

    lb_f, ub_f = get_bounds_for_constraint("free")
    np.testing.assert_allclose(lb_f, LB_FREE)
    np.testing.assert_allclose(ub_f, UB_FREE)

    with pytest.raises(ValueError):
        get_bounds_for_constraint("invalid_constraint")


def test_io_atomic_and_resumability(tmp_path: Path):
    """Uji atomic write, deteksi file korup, dan resumability."""
    target_file = tmp_path / "test_run.json"
    assert not is_run_completed(target_file)

    # 1. Tulis file kosong
    target_file.touch()
    assert not is_run_completed(target_file), "File 0 bytes harus dianggap belum lengkap"

    # 2. Tulis JSON tidak lengkap
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump({"config_id": "gross_djppr"}, f)
    assert not is_run_completed(target_file), "JSON tanpa field esensial harus dianggap belum lengkap"

    # 3. Tulis payload valid
    valid_payload = {
        "run_id": "gross_djppr_kma_rep01_seed43",
        "config_id": "gross_djppr",
        "algo": "kma",
        "rep": 1,
        "seed": 43,
        "is_feasible": True,
        "best_cost": 1.0419,
        "best_w": [0.45, 0.11, 0.15, 0.14, 0.02, 0.07, 0.06],
        "evaluations": 25000,
    }
    save_run_result(target_file, valid_payload)
    assert is_run_completed(target_file)

    loaded = load_run_result(target_file)
    assert loaded["run_id"] == "gross_djppr_kma_rep01_seed43"
    assert loaded["best_cost"] == 1.0419


def test_runs_summary_aggregation(tmp_path: Path):
    """Uji agregasi otomatis seluruh file hasil menjadi file CSV ringkasan."""
    runs_dir = tmp_path / "runs"
    # Buat 2 dummy file run
    p1 = get_run_result_path(runs_dir, "gross_djppr", "kma", 1, 43)
    p2 = get_run_result_path(runs_dir, "gross_djppr", "ga", 1, 43)

    save_run_result(
        p1,
        {
            "config_id": "gross_djppr",
            "cost_definition": "gross",
            "constraint_type": "djppr",
            "algo": "kma",
            "rep": 1,
            "seed": 43,
            "is_feasible": True,
            "best_cost": 1.0419,
            "best_fitness": 1.0419,
            "ccar": 1.085,
            "j_mccar": 0.068,
            "tau_limit": 1.086,
            "eta_limit": 0.0682,
            "evaluations": 25000,
            "best_w": [0.45, 0.11, 0.15, 0.14, 0.02, 0.07, 0.06],
            "time_seconds": 38.5,
            "timestamp": "2026-10-18T10:00:00Z",
        },
    )

    save_run_result(
        p2,
        {
            "config_id": "gross_djppr",
            "cost_definition": "gross",
            "constraint_type": "djppr",
            "algo": "ga",
            "rep": 1,
            "seed": 43,
            "is_feasible": True,
            "best_cost": 1.0418,
            "best_fitness": 1.0418,
            "ccar": 1.085,
            "j_mccar": 0.068,
            "tau_limit": 1.086,
            "eta_limit": 0.0682,
            "evaluations": 25000,
            "best_w": [0.46, 0.11, 0.14, 0.14, 0.02, 0.07, 0.06],
            "time_seconds": 9.2,
            "timestamp": "2026-10-18T10:01:00Z",
        },
    )

    csv_out = tmp_path / "summary.csv"
    df = build_runs_summary(runs_dir=runs_dir, output_csv=csv_out)

    assert len(df) == 2
    assert csv_out.exists()
    assert "best_cost" in df.columns
    assert "w_1" in df.columns
    assert df.loc[df["algo"] == "kma", "best_cost"].iloc[0] == 1.0419


def test_execute_single_run_pilot_and_resume(tmp_path: Path):
    """Uji integrasi runner: menjalankan 1 run pilot kecil, memvalidasi JSON, dan menguji resume skip."""
    bank_path = Path("data/processed/bank_train_seed42_N5000.npz")
    limits_path = Path("data/processed/risk_limits_bank_train_seed42_N5000.json")

    if not bank_path.exists() or not limits_path.exists():
        pytest.skip("Bank skenario atau batas risiko belum di-generate.")

    spec = ExperimentSpec(
        config_id="gross_djppr",
        cost_definition="gross",
        constraint_type="djppr",
        algo_name="pso",
        rep=1,
        seed=999,
        budget=500,  # Budget kecil untuk tes cepat
    )

    out_dir = tmp_path / "runs"
    # Run pertama: harus mengeksekusi optimasi
    res1 = execute_single_run(
        spec=spec,
        bank_path=bank_path,
        limits_path=limits_path,
        output_dir=out_dir,
        resume=True,
    )
    assert res1["status"] == "completed"
    assert res1["evaluations"] <= 500
    assert len(res1["best_w"]) == 7
    assert len(res1["convergence_history"]) > 0

    target_json = get_run_result_path(out_dir, spec.config_id, spec.algo_name, spec.rep, spec.seed)
    assert target_json.exists()
    assert is_run_completed(target_json)

    # Run kedua dengan resume=True: harus di-skip dan tidak menghitung ulang
    res2 = execute_single_run(
        spec=spec,
        bank_path=bank_path,
        limits_path=limits_path,
        output_dir=out_dir,
        resume=True,
    )
    assert res2["status"] == "skipped"
    assert res2["run_id"] == res1["run_id"]
