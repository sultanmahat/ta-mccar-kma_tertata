"""Antarmuka bersama pengoptimal metaheuristik portofolio utang multivaluta.

Menyediakan:
1. OptimizationResult: dataclass standar hasil optimasi (bobot, biaya, metrik risiko,
   kelayakan, anggaran terpakai, riwayat konvergensi, durasi, metadata).
2. BaseOptimizer: kelas dasar abstrak yang mengelola BudgetCounter (batas 25.000 evaluasi),
   FeasibleArchive (arsip solusi layak), dan pencatatan log konvergensi tiap 250 evaluasi.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import time
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
import numpy as np

from mccar_kma.model.constraints import (
    project_weights,
    project_weights_batch,
    check_weight_feasibility,
)
from mccar_kma.model.penalty import BudgetCounter, FeasibleArchive, FeasibleSolution


@dataclass
class OptimizationResult:
    """Struktur data standar hasil optimasi portofolio.

    Attributes
    ----------
    best_w : np.ndarray
        Vektor bobot portofolio terbaik (7,). Diambil dari solusi layak terbaik
        di arsip jika ada; jika tidak ada solusi layak, diambil solusi dengan
        fitness f(w) terendah.
    best_cost : float
        Rata-rata biaya portofolio Cost_bar(w) dari solusi terbaik.
    best_fitness : float
        Nilai fitness f(w) (dengan penalti) dari solusi terbaik.
    ccar : float
        Nilai risiko ekor CCaR_alpha(w).
    j_mccar : float
        Nilai dispersi risiko J_MCCaR(w).
    v_J : float
        Pelanggaran relatif kendala dispersi risiko v_J(w).
    v_R : float
        Pelanggaran relatif kendala risiko ekor v_R(w).
    is_feasible : bool
        True jika solusi memenuhi kendala proporsi, sum(w)=1, v_J <= eps_tol,
        dan v_R <= eps_tol.
    evaluations_used : int
        Jumlah evaluasi fungsi yang digunakan (maksimum 25.000).
    convergence_history : List[Dict[str, Any]]
        Log konvergensi tiap interval evaluasi (default: tiap 250 evaluasi).
        Tiap entri memuat {'evaluation': int, 'best_cost': Optional[float],
        'best_fitness': Optional[float], 'is_feasible': bool}.
    elapsed_seconds : float
        Waktu eksekusi optimasi dalam detik.
    metadata : Dict[str, Any]
        Informasi tambahan (nama algoritma, hyperparameter, seed, dll.).
    """

    best_w: np.ndarray
    best_cost: float
    best_fitness: float
    ccar: float
    j_mccar: float
    v_J: float
    v_R: float
    is_feasible: bool
    evaluations_used: int
    convergence_history: List[Dict[str, Any]] = field(default_factory=list)
    elapsed_seconds: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseOptimizer(ABC):
    """Kelas dasar abstrak untuk algoritma optimasi (KMA, GA, PSO).

    Parameters
    ----------
    check_interval : int
        Interval evaluasi untuk pencatatan kurva konvergensi (default: 250).
    eps_tol : float
        Toleransi numerik kendala (default: 1e-8).
    """

    def __init__(
        self,
        check_interval: int = 250,
        eps_tol: float = 1e-8,
    ) -> None:
        self.check_interval = int(check_interval)
        self.eps_tol = float(eps_tol)

        # Komponen pelacak yang diinisialisasi per eksekusi
        self.budget: BudgetCounter = BudgetCounter(25000)
        self.archive: FeasibleArchive = FeasibleArchive(eps_tol=eps_tol)
        self.convergence_history: List[Dict[str, Any]] = []
        self._next_checkpoint: int = self.check_interval
        self._best_overall: Optional[Dict[str, Any]] = None
        self._lb: Optional[np.ndarray] = None
        self._ub: Optional[np.ndarray] = None

    def _init_run(
        self,
        budget: int,
        lb: np.ndarray,
        ub: np.ndarray,
        rng: Optional[Union[int, np.random.Generator]] = None,
    ) -> np.random.Generator:
        """Menginisialisasi state sebelum optimasi dimulai."""
        self.budget = BudgetCounter(budget)
        self.archive = FeasibleArchive(eps_tol=self.eps_tol)
        self.convergence_history = []
        self._next_checkpoint = self.check_interval
        self._best_overall = None
        self._lb = np.asarray(lb, dtype=float)
        self._ub = np.asarray(ub, dtype=float)

        if rng is None:
            return np.random.default_rng()
        if isinstance(rng, (int, np.integer)):
            return np.random.default_rng(int(rng))
        if isinstance(rng, np.random.Generator):
            return rng
        raise TypeError(f"Tipe rng tidak valid: {type(rng)}")

    def _process_eval_dict(
        self,
        w_proj: np.ndarray,
        raw_res: Union[Dict[str, Any], float, int, np.floating, np.integer],
    ) -> Dict[str, Any]:
        """Menstandardisasi output evaluator ke format dictionary terpadu."""
        if isinstance(raw_res, (int, float, np.floating, np.integer)):
            val = float(raw_res)
            return {
                "w": w_proj,
                "mean_cost": val,
                "f_val": val,
                "ccar": 0.0,
                "j_mccar": 0.0,
                "v_J": 0.0,
                "v_R": 0.0,
                "is_feasible": True,
            }

        res = dict(raw_res)
        res["w"] = w_proj
        if "f_val" not in res:
            res["f_val"] = float(res.get("mean_cost", 0.0))
        if "v_J" not in res:
            res["v_J"] = 0.0
        if "v_R" not in res:
            res["v_R"] = 0.0
        if "mean_cost" not in res:
            res["mean_cost"] = float(res["f_val"])
        if "ccar" not in res:
            res["ccar"] = 0.0
        if "j_mccar" not in res:
            res["j_mccar"] = 0.0
        if "is_feasible" not in res:
            res["is_feasible"] = bool(
                res["v_J"] <= self.eps_tol and res["v_R"] <= self.eps_tol
            )
        return res

    def evaluate_candidate(
        self,
        w: np.ndarray,
        evaluator: Any,
    ) -> Optional[Dict[str, Any]]:
        """Mengevaluasi satu kandidat solusi bobot dengan proyeksi dan pelacakan anggaran.

        Jika anggaran evaluasi telah habis, mengembalikan None.
        """
        if self.budget.is_exhausted:
            return None

        # 1. Proyeksikan ke ruang proporsi layak sum(w)=1 dan lb <= w <= ub
        w_proj = project_weights(w, self._lb, self._ub, eps_tol=self.eps_tol)

        # 2. Panggil evaluator
        if hasattr(evaluator, "evaluate"):
            raw_res = evaluator.evaluate(w_proj, apply_penalty=True)
        elif callable(evaluator):
            raw_res = evaluator(w_proj)
        else:
            raise TypeError("Evaluator harus memiliki metode evaluate() atau callable")

        # 3. Catat konsumsi anggaran
        self.budget.consume(1)
        current_eval = self.budget.evaluations

        # 4. Standardisasi hasil
        eval_dict = self._process_eval_dict(w_proj, raw_res)

        # 5. Perbarui FeasibleArchive jika solusi layak
        self.archive.update(
            w=w_proj,
            mean_cost=eval_dict["mean_cost"],
            ccar=eval_dict["ccar"],
            j_mccar=eval_dict["j_mccar"],
            v_J=eval_dict["v_J"],
            v_R=eval_dict["v_R"],
            evaluation_index=current_eval,
            f_val=eval_dict.get("f_val", eval_dict["mean_cost"]),
        )

        # 6. Catat solusi terbaik keseluruhan (fallback)
        if self._best_overall is None or eval_dict["f_val"] < self._best_overall["f_val"]:
            self._best_overall = eval_dict

        # 7. Rekam log konvergensi jika menyentuh kelipatan interval
        self._check_convergence_checkpoint()

        return eval_dict

    def evaluate_population(
        self,
        W: np.ndarray,
        evaluator: Any,
    ) -> List[Dict[str, Any]]:
        """Mengevaluasi populasi matriks kandidat bobot W berukuran (P, D).

        Menggunakan evaluasi batch jika evaluator mendukung evaluate_batch untuk
        kecepatan optimal, atau evaluasi individu per baris jika tidak.
        Jumlah evaluasi dipangkas secara otomatis jika melebihi sisa anggaran.
        """
        W = np.asarray(W, dtype=float)
        p = len(W)
        rem = self.budget.remaining
        if rem <= 0:
            return []

        # Pangkas jika sisa anggaran kurang dari ukuran populasi
        if p > rem:
            W = W[:rem]
            p = rem

        # 1. Proyeksi seluruh populasi
        W_proj = project_weights_batch(W, self._lb, self._ub, eps_tol=self.eps_tol)

        results: List[Dict[str, Any]] = []

        # 2. Eksekusi batch jika tersedia pada evaluator
        if hasattr(evaluator, "evaluate_batch"):
            batch_dict = evaluator.evaluate_batch(W_proj, apply_penalty=True)
            for i in range(p):
                self.budget.consume(1)
                current_eval = self.budget.evaluations
                row_dict = {
                    "w": W_proj[i],
                    "mean_cost": float(batch_dict["mean_cost"][i]),
                    "ccar": float(batch_dict["ccar"][i]),
                    "mccar": batch_dict["mccar"][i],
                    "theta": batch_dict["theta"][i],
                    "theta_bar": float(batch_dict["theta_bar"][i]),
                    "j_mccar": float(batch_dict["j_mccar"][i]),
                    "v_J": float(batch_dict["v_J"][i]),
                    "v_R": float(batch_dict["v_R"][i]),
                    "f_val": float(batch_dict["f_val"][i]),
                    "is_feasible": bool(batch_dict["is_feasible"][i]),
                }
                # Perbarui arsip
                self.archive.update(
                    w=row_dict["w"],
                    mean_cost=row_dict["mean_cost"],
                    ccar=row_dict["ccar"],
                    j_mccar=row_dict["j_mccar"],
                    v_J=row_dict["v_J"],
                    v_R=row_dict["v_R"],
                    evaluation_index=current_eval,
                    f_val=row_dict["f_val"],
                )
                # Perbarui best overall
                if self._best_overall is None or row_dict["f_val"] < self._best_overall["f_val"]:
                    self._best_overall = row_dict

                self._check_convergence_checkpoint()
                results.append(row_dict)
        else:
            # Evaluasi per individu
            for i in range(p):
                res = self.evaluate_candidate(W_proj[i], evaluator)
                if res is not None:
                    results.append(res)

        return results

    def _check_convergence_checkpoint(self) -> None:
        """Merekam status konvergensi setiap kelipatan check_interval evaluasi."""
        while self.budget.evaluations >= self._next_checkpoint:
            best_cost = (
                self.archive.best_solution.mean_cost
                if self.archive.best_solution is not None
                else (self._best_overall["mean_cost"] if self._best_overall else None)
            )
            best_fitness = (
                self._best_overall["f_val"]
                if self._best_overall is not None
                else None
            )
            has_feasible = self.archive.best_solution is not None

            self.convergence_history.append({
                "evaluation": self._next_checkpoint,
                "best_cost": best_cost,
                "best_fitness": best_fitness,
                "is_feasible": has_feasible,
            })
            self._next_checkpoint += self.check_interval

    def _build_result(
        self,
        elapsed_seconds: float,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> OptimizationResult:
        """Membangun objek OptimizationResult akhir sesuai aturan spesifikasi §6 langkah 3."""
        # Catat sisa checkpoint jika ada (misal run berhenti di batas akhir persis)
        self._check_convergence_checkpoint()

        meta = metadata or {}

        # Solusi akhir: prioritas solusi layak terbaik di arsip (v_J <= eps_tol dan v_R <= eps_tol)
        if self.archive.best_solution is not None:
            sol = self.archive.best_solution
            return OptimizationResult(
                best_w=sol.w,
                best_cost=sol.mean_cost,
                best_fitness=sol.f_val,
                ccar=sol.ccar,
                j_mccar=sol.j_mccar,
                v_J=sol.v_J,
                v_R=sol.v_R,
                is_feasible=True,
                evaluations_used=self.budget.evaluations,
                convergence_history=list(self.convergence_history),
                elapsed_seconds=float(elapsed_seconds),
                metadata=meta,
            )

        # Fallback jika tidak ada solusi layak sama sekali
        if self._best_overall is not None:
            b = self._best_overall
            return OptimizationResult(
                best_w=b["w"],
                best_cost=b["mean_cost"],
                best_fitness=b["f_val"],
                ccar=b["ccar"],
                j_mccar=b["j_mccar"],
                v_J=b["v_J"],
                v_R=b["v_R"],
                is_feasible=b["is_feasible"],
                evaluations_used=self.budget.evaluations,
                convergence_history=list(self.convergence_history),
                elapsed_seconds=float(elapsed_seconds),
                metadata=meta,
            )

        # Kasus ekstrem: tidak ada evaluasi sama sekali
        dummy_w = (self._lb + self._ub) / 2.0
        dummy_w /= np.sum(dummy_w)
        return OptimizationResult(
            best_w=dummy_w,
            best_cost=float("inf"),
            best_fitness=float("inf"),
            ccar=float("inf"),
            j_mccar=float("inf"),
            v_J=1.0,
            v_R=1.0,
            is_feasible=False,
            evaluations_used=0,
            convergence_history=[],
            elapsed_seconds=float(elapsed_seconds),
            metadata=meta,
        )

    @abstractmethod
    def run(
        self,
        evaluator: Any,
        lb: np.ndarray,
        ub: np.ndarray,
        budget: int = 25000,
        rng: Optional[Union[int, np.random.Generator]] = None,
    ) -> OptimizationResult:
        """Menjalankan proses optimasi hingga anggaran habis."""
        pass
