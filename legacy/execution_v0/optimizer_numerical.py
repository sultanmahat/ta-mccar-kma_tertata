"""
Metode Pembanding 2: Optimasi Numerik Deterministik (SLSQP / Padanan fmincon)
Sesuai Subbab 3.6.2 Proposal TA Sultan Bakri.

Menyelesaikan model optimasi nonlinear berkendala:
min_w  mu^T * w
s.t.   CCaR_alpha(w) <= tau
       sum(w_i) = 1
       lb_i <= w_i <= ub_i
"""

import numpy as np
from scipy.optimize import minimize
from .risk_metrics import calculate_expected_cost, calculate_ccar

def run_numerical_optimization(scenario_costs, mu_vector, lower_bounds, upper_bounds,
                               tau=None, initial_weights=None, alpha=0.95):
    """
    Menjalankan optimasi numerik deterministik menggunakan algoritma SLSQP (Sequential Least Squares Programming).
    """
    n_instruments = len(mu_vector)

    # Inisialisasi bobot awal jika tidak diberikan (gunakan titik tengah)
    if initial_weights is None:
        initial_weights = (lower_bounds + upper_bounds) / 2.0
        initial_weights /= np.sum(initial_weights)

    if tau is None:
        tau = calculate_ccar(initial_weights, scenario_costs, alpha=alpha) * 1.05

    # Fungsi objektif: meminimumkan biaya ekspektasi mu^T * w
    def objective(w):
        return calculate_expected_cost(w, mu_vector)

    # Kendala persamaan: sum(w_i) = 1  =>  sum(w_i) - 1 = 0
    constraint_budget = {
        'type': 'eq',
        'fun': lambda w: np.sum(w) - 1.0
    }

    # Kendala pertidaksamaan: CCaR(w) <= tau  =>  tau - CCaR(w) >= 0
    constraint_risk = {
        'type': 'ineq',
        'fun': lambda w: tau - calculate_ccar(w, scenario_costs, alpha=alpha)
    }

    constraints = [constraint_budget, constraint_risk]

    # Batas box [lb, ub]
    bounds = [(lower_bounds[i], upper_bounds[i]) for i in range(n_instruments)]

    # Eksekusi SLSQP
    res = minimize(
        objective,
        x0=initial_weights,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints,
        options={'maxiter': 500, 'ftol': 1e-6, 'disp': False}
    )

    opt_weights = res.x
    opt_weights = np.clip(opt_weights, lower_bounds, upper_bounds)
    opt_weights /= np.sum(opt_weights)

    opt_cost = calculate_expected_cost(opt_weights, mu_vector)
    opt_ccar = calculate_ccar(opt_weights, scenario_costs, alpha=alpha)

    return {
        'method': 'Optimasi Numerik (SLSQP / fmincon equivalent)',
        'success': res.success,
        'message': res.message,
        'nit': res.nit,
        'best_solution': {
            'weights': opt_weights,
            'cost': opt_cost,
            'ccar': opt_ccar
        },
        'tau': tau
    }
