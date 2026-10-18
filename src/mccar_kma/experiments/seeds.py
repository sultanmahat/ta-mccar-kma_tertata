"""Modul penanganan seed replikasi dan pembuatan spesifikasi eksperimen.

Menjamin keadilan komparasi (Fairness) sesuai spesifikasi:
1. Replikasi ke-k (k = 1..30) menggunakan seed identik untuk semua algoritma (KMA, GA, PSO).
2. Formula seed deterministik: seed_k = base_seed + k.
3. Mendukung 4 konfigurasi (gross_free, gross_djppr, interest_free, interest_djppr).
"""

from dataclasses import dataclass
from typing import List, Optional
import hashlib
import json


@dataclass(frozen=True)
class ExperimentSpec:
    """Spesifikasi tunggal untuk satu replikasi eksperimen optimasi."""

    config_id: str
    cost_definition: str
    constraint_type: str
    algo_name: str
    rep: int
    seed: int
    budget: int

    @property
    def run_id(self) -> str:
        """Pengenal unik satu run: <config_id>_<algo>_rep<kk>_seed<seed>."""
        return f"{self.config_id}_{self.algo_name}_rep{self.rep:02d}_seed{self.seed}"


def get_replication_seeds(base_seed: int = 42, replications: int = 30) -> List[int]:
    """Membangkitkan daftar seed replikasi deterministik.

    Parameters
    ----------
    base_seed : int
        Seed dasar acuan (default: 42).
    replications : int
        Jumlah replikasi (default: 30).

    Returns
    -------
    List[int]
        Daftar seed berurutan [base_seed + 1, ..., base_seed + replications].
    """
    return [base_seed + k for k in range(1, replications + 1)]


def generate_experiment_matrix(
    configurations: Optional[List[str]] = None,
    algorithms: Optional[List[str]] = None,
    base_seed: int = 42,
    replications: int = 30,
    budget: int = 25000,
) -> List[ExperimentSpec]:
    """Membangkitkan matriks lengkap spesifikasi eksperimen (default: 360 run).

    Parameters
    ----------
    configurations : Optional[List[str]]
        Daftar config_id (default: gross_free, gross_djppr, interest_free, interest_djppr).
    algorithms : Optional[List[str]]
        Daftar algoritma (default: kma, ga, pso).
    base_seed : int
        Seed dasar acuan (default: 42).
    replications : int
        Jumlah replikasi per konfigurasi per algoritma (default: 30).
    budget : int
        Anggaran evaluasi fungsi per run (default: 25.000).

    Returns
    -------
    List[ExperimentSpec]
        Daftar seluruh ExperimentSpec yang akan dieksekusi.
    """
    if configurations is None:
        configurations = [
            "gross_free",
            "gross_djppr",
            "interest_free",
            "interest_djppr",
        ]
    if algorithms is None:
        algorithms = ["kma", "ga", "pso"]

    seeds = get_replication_seeds(base_seed=base_seed, replications=replications)
    matrix: List[ExperimentSpec] = []

    for cfg in configurations:
        cost_def, constr = cfg.split("_", 1)
        for algo in algorithms:
            for rep_idx, seed in enumerate(seeds, start=1):
                spec = ExperimentSpec(
                    config_id=cfg,
                    cost_definition=cost_def,
                    constraint_type=constr,
                    algo_name=algo.lower(),
                    rep=rep_idx,
                    seed=seed,
                    budget=budget,
                )
                matrix.append(spec)

    return matrix


def compute_spec_hash(spec: ExperimentSpec) -> str:
    """Menghitung hash SHA256 dari spesifikasi run untuk verifikasi integritas."""
    payload = json.dumps(
        {
            "config_id": spec.config_id,
            "cost_definition": spec.cost_definition,
            "constraint_type": spec.constraint_type,
            "algo_name": spec.algo_name,
            "rep": spec.rep,
            "seed": spec.seed,
            "budget": spec.budget,
        },
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()
