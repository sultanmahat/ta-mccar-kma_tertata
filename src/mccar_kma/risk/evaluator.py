"""Evaluator portofolio utang multivaluta berbasis MCCaR dan CCaR.

Menyediakan kelas PortfolioEvaluator yang menghitung seluruh metrik risiko,
biaya rata-rata, penalti kendala, dan fungsi kualitas f(w):
- Persamaan 2.13 (CCaR_alpha)
- Persamaan 2.14, 2.16 (MC), 2.17 (MCCaR), 2.18 (theta), 2.19 (theta_bar), 2.20 (J_MCCaR)
- Persamaan 2.21–2.22 (Threshold baseline tau dan eta dari w0)
- Persamaan 2.23 (Pelanggaran relatif v_J dan v_R)
- Persamaan 2.24 (Fitness penalized f(w))

Mendukung evaluasi satu portofolio w (7,) maupun batch populasi W (P, 7).
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np

from mccar_kma.risk.ccar import compute_ccar, compute_ccar_batch, compute_tail_count
from mccar_kma.risk.mccar import (
    compute_marginal_cost,
    compute_mccar,
    compute_theta,
    compute_j_mccar,
)
from mccar_kma.model.constraints import (
    compute_relative_violations,
    compute_relative_violations_batch,
    project_weights,
    project_weights_batch,
    check_weight_feasibility,
)
from mccar_kma.model.penalty import (
    compute_penalized_fitness,
    compute_penalized_fitness_batch,
)


class PortfolioEvaluator:
    """Evaluator terpadu untuk evaluasi risiko, biaya, dan penalti portofolio.

    Parameters
    ----------
    cost_matrix : np.ndarray
        Matriks biaya instrumen utang per skenario berukuran (N, n).
        Dapat berupa biaya bruto (Pers. 2.2) atau biaya bunga (Pers. 2.3).
    alpha : float
        Tingkat kepercayaan risiko (default: 0.95).
    delta : float
        Tambahan penerbitan proporsi utang (default: 0.01 = 1%).
    tau : Optional[float]
        Threshold risiko ekor acuan CCaR_alpha(w0). Jika None, dihitung via set_baseline.
    eta : Optional[float]
        Threshold dispersi risiko acuan J_MCCaR(w0). Jika None, dihitung via set_baseline.
    rho_J : float
        Koefisien penalti kuadratik untuk dispersi risiko (default: 1e6).
    rho_R : float
        Koefisien penalti kuadratik untuk risiko ekor (default: 1e6).
    eps_tol : float
        Toleransi numerik kendala (default: 1e-8).
    zero_tol_mc : float
        Toleransi pembagian nol D5 pada MC_i (default: 1e-12).
    """

    def __init__(
        self,
        cost_matrix: np.ndarray,
        alpha: float = 0.95,
        delta: float = 0.01,
        tau: Optional[float] = None,
        eta: Optional[float] = None,
        rho_J: float = 1e6,
        rho_R: float = 1e6,
        eps_tol: float = 1e-8,
        zero_tol_mc: float = 1e-12,
    ) -> None:
        self.C = np.asarray(cost_matrix, dtype=float)
        if self.C.ndim != 2:
            raise ValueError(f"cost_matrix harus 2-dimensi (N, n), didapat: {self.C.ndim}")

        self.n_scenarios, self.n_instruments = self.C.shape
        self.alpha = float(alpha)
        self.delta = float(delta)
        self.tau = float(tau) if tau is not None else None
        self.eta = float(eta) if eta is not None else None
        self.rho_J = float(rho_J)
        self.rho_R = float(rho_R)
        self.eps_tol = float(eps_tol)
        self.zero_tol_mc = float(zero_tol_mc)

        # 1. Hitung jumlah skenario ekor m (Persamaan 2.13)
        self.m = compute_tail_count(self.n_scenarios, self.alpha)

        # 2. Prekomputasi MC_i (Persamaan 2.16): konstan terhadap w!
        self.mc = compute_marginal_cost(self.C, delta=self.delta)

        # 3. Prekomputasi matriks delta * C untuk penghematan waktu eksekusi
        self.delta_C = self.delta * self.C

    @classmethod
    def from_scenario_bank(
        cls,
        bank_data_or_path: Union[str, Path, Dict[str, Any]],
        cost_def: str = "gross",
        alpha: float = 0.95,
        delta: float = 0.01,
        tau: Optional[float] = None,
        eta: Optional[float] = None,
        rho_J: float = 1e6,
        rho_R: float = 1e6,
        eps_tol: float = 1e-8,
        zero_tol_mc: float = 1e-12,
    ) -> "PortfolioEvaluator":
        """Inisialisasi evaluator langsung dari file atau data bank skenario .npz."""
        if isinstance(bank_data_or_path, (str, Path)):
            path = Path(bank_data_or_path)
            if not path.exists():
                raise FileNotFoundError(f"File bank skenario tidak ditemukan: {path}")
            data = np.load(path)
        else:
            data = bank_data_or_path

        key = "cost_gross" if cost_def == "gross" else "cost_interest"
        if key not in data:
            raise KeyError(f"Array '{key}' tidak ditemukan di bank skenario.")

        cost_mat = data[key]
        return cls(
            cost_matrix=cost_mat,
            alpha=alpha,
            delta=delta,
            tau=tau,
            eta=eta,
            rho_J=rho_J,
            rho_R=rho_R,
            eps_tol=eps_tol,
            zero_tol_mc=zero_tol_mc,
        )

    def set_baseline(self, w0: np.ndarray) -> Dict[str, float]:
        """Menghitung dan menetapkan threshold acuan tau dan eta dari w0 (Persamaan 2.22).

        Persamaan 2.22:
            tau = CCaR_alpha(w0)
            eta = J_MCCaR(w0)

        Parameters
        ----------
        w0 : np.ndarray
            Vektor bobot portofolio eksisting 2024 berukuran (n,).

        Returns
        -------
        Dict[str, float]
            Dictionary berisi {'mean_cost': ..., 'tau': ..., 'eta': ...}.
        """
        metrics = self.evaluate(w0, apply_penalty=False)
        self.tau = metrics["ccar"]
        self.eta = metrics["j_mccar"]

        return {
            "mean_cost": metrics["mean_cost"],
            "tau": self.tau,
            "eta": self.eta,
        }

    def evaluate(
        self,
        w: np.ndarray,
        apply_penalty: bool = True,
    ) -> Dict[str, Any]:
        """Mengevaluasi satu vektor bobot portofolio w.

        Parameters
        ----------
        w : np.ndarray
            Vektor bobot berukuran (n,).
        apply_penalty : bool
            Jika True, hitung v_J, v_R, dan f(w) menggunakan threshold tau dan eta.

        Returns
        -------
        Dict[str, Any]
            Dictionary lengkap hasil evaluasi:
            - 'mean_cost': float (Cost_bar(w))
            - 'ccar': float (CCaR_alpha(w))
            - 'mc': np.ndarray (MC_i)
            - 'mccar': np.ndarray (MCCaR_i)
            - 'theta': np.ndarray (theta_i)
            - 'theta_bar': float
            - 'j_mccar': float (J_MCCaR(w))
            - 'v_J': float (jika apply_penalty=True)
            - 'v_R': float (jika apply_penalty=True)
            - 'f_val': float (jika apply_penalty=True)
            - 'is_feasible': bool (jika apply_penalty=True)
        """
        w = np.asarray(w, dtype=float)

        # 1. Biaya portofolio skenario: Cost_s = C @ w (Persamaan 2.15)
        cost_s = self.C @ w
        mean_cost = float(np.mean(cost_s))

        # 2. CCaR_alpha (Persamaan 2.13) via np.partition
        tail_vals = np.partition(cost_s, self.n_scenarios - self.m)[-self.m:]
        ccar = float(np.mean(tail_vals))

        # 3. MCCaR_i (Persamaan 2.14 & 2.17)
        mccar = np.empty(self.n_instruments, dtype=float)
        for i in range(self.n_instruments):
            cost_pert = cost_s + self.delta_C[:, i]
            tail_pert = np.partition(cost_pert, self.n_scenarios - self.m)[-self.m:]
            ccar_pert = float(np.mean(tail_pert))
            mccar[i] = ccar_pert - ccar

        # 4. theta_i dan theta_bar (Persamaan 2.18 & 2.19, D5 guard)
        theta, theta_bar = compute_theta(mccar, self.mc, zero_tol=self.zero_tol_mc)

        # 5. J_MCCaR (Persamaan 2.20)
        j_mccar = float(np.std(theta, ddof=0))

        result = {
            "mean_cost": mean_cost,
            "ccar": ccar,
            "mc": self.mc,
            "mccar": mccar,
            "theta": theta,
            "theta_bar": theta_bar,
            "j_mccar": j_mccar,
        }

        if apply_penalty:
            if self.tau is None or self.eta is None:
                raise ValueError(
                    "Threshold tau dan eta belum ditentukan. Panggil set_baseline(w0) "
                    "terlebih dahulu atau berikan tau dan eta pada inisialisasi."
                )

            v_J, v_R = compute_relative_violations(
                j_mccar=j_mccar,
                ccar=ccar,
                eta=self.eta,
                tau=self.tau,
                eps_tol=self.eps_tol,
            )
            f_val = compute_penalized_fitness(
                mean_cost=mean_cost,
                v_J=v_J,
                v_R=v_R,
                rho_J=self.rho_J,
                rho_R=self.rho_R,
            )
            is_feasible = (v_J <= self.eps_tol) and (v_R <= self.eps_tol)

            result.update({
                "v_J": v_J,
                "v_R": v_R,
                "f_val": f_val,
                "is_feasible": is_feasible,
            })

        return result

    def evaluate_batch(
        self,
        W: np.ndarray,
        apply_penalty: bool = True,
    ) -> Dict[str, np.ndarray]:
        """Mengevaluasi populasi kandidat bobot W berukuran (P, n) secara batch tervektorisasi.

        Parameters
        ----------
        W : np.ndarray
            Matriks populasi bobot berukuran (P, n).
        apply_penalty : bool
            Jika True, hitung v_J, v_R, dan f_val untuk seluruh populasi.

        Returns
        -------
        Dict[str, np.ndarray]
            Dictionary berisi array berukuran (P,):
            - 'mean_cost': (P,)
            - 'ccar': (P,)
            - 'mccar': (P, n)
            - 'theta': (P, n)
            - 'theta_bar': (P,)
            - 'j_mccar': (P,)
            - 'v_J': (P,) (jika apply_penalty=True)
            - 'v_R': (P,) (jika apply_penalty=True)
            - 'f_val': (P,) (jika apply_penalty=True)
            - 'is_feasible': (P,) bool (jika apply_penalty=True)
        """
        W = np.asarray(W, dtype=float)
        p, n = W.shape
        if n != self.n_instruments:
            raise ValueError(f"W harus memiliki kolom {self.n_instruments}, didapat: {n}")

        # Cost batch: W @ C.T berukuran (P, N)
        cost_batch = W @ self.C.T
        mean_cost = np.mean(cost_batch, axis=1)

        # CCaR batch via np.partition sepanjang axis skenario (axis=1)
        tail_batch = np.partition(cost_batch, self.n_scenarios - self.m, axis=1)[:, -self.m:]
        ccar = np.mean(tail_batch, axis=1)

        # MCCaR batch untuk n_instruments
        mccar = np.empty((p, self.n_instruments), dtype=float)
        for i in range(self.n_instruments):
            cost_pert = cost_batch + self.delta_C[:, i]
            tail_pert = np.partition(cost_pert, self.n_scenarios - self.m, axis=1)[:, -self.m:]
            ccar_pert = np.mean(tail_pert, axis=1)
            mccar[:, i] = ccar_pert - ccar

        # theta batch (D5 guard)
        safe_mc = np.where(np.abs(self.mc) <= self.zero_tol_mc, np.nan, self.mc)
        theta = np.where(np.isnan(safe_mc), 0.0, mccar / safe_mc)
        theta_bar = np.mean(theta, axis=1)

        # J_MCCaR batch (pembagi n, bukan n-1)
        j_mccar = np.std(theta, axis=1, ddof=0)

        result = {
            "mean_cost": mean_cost,
            "ccar": ccar,
            "mccar": mccar,
            "theta": theta,
            "theta_bar": theta_bar,
            "j_mccar": j_mccar,
        }

        if apply_penalty:
            if self.tau is None or self.eta is None:
                raise ValueError("Threshold tau dan eta belum ditentukan.")

            v_J, v_R = compute_relative_violations_batch(
                j_mccar_arr=j_mccar,
                ccar_arr=ccar,
                eta=self.eta,
                tau=self.tau,
                eps_tol=self.eps_tol,
            )
            f_val = compute_penalized_fitness_batch(
                mean_cost_arr=mean_cost,
                v_J_arr=v_J,
                v_R_arr=v_R,
                rho_J=self.rho_J,
                rho_R=self.rho_R,
            )
            is_feasible = (v_J <= self.eps_tol) & (v_R <= self.eps_tol)

            result.update({
                "v_J": v_J,
                "v_R": v_R,
                "f_val": f_val,
                "is_feasible": is_feasible,
            })

        return result
