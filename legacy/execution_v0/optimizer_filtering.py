"""
Metode Pembanding 1: Penyaringan Kombinasi Acak (Random Filtering Baseline DJPPR)
Sesuai Subbab 3.6.1 dan Kajian DJPPR Kemenkeu (2025).

Prosedur:
1. Membangkitkan n_samples (misal 1.000) kombinasi bobot acak di dalam rentang batas [lb, ub].
2. Menormalisasi bobot sehingga sum(w_i) = 1.
3. Mengevaluasi biaya ekspektasi, CCaR, MCCaR, dan rasio efisiensi.
4. Memilih kandidat solusi dengan biaya terendah yang memenuhi kendala risiko (CCaR <= tau)
   atau yang memiliki rasio efisiensi paling seimbang mendekati 1.
"""

import numpy as np
from .risk_metrics import calculate_expected_cost, calculate_ccar, calculate_mccar

def run_random_filtering(scenario_costs, mu_vector, lower_bounds, upper_bounds, 
                         tau=None, n_samples=1000, alpha=0.95, seed=42):
    """
    Menjalankan prosedur Random Filtering DJPPR.
    """
    if seed is not None:
        np.random.seed(seed)

    n_instruments = len(mu_vector)
    valid_weights = []
    costs = []
    ccars = []
    efficiency_diffs = []

    # Jika tau belum ditentukan, gunakan CCaR dari bobot tengah (mid-point)
    if tau is None:
        mid_weights = (lower_bounds + upper_bounds) / 2.0
        mid_weights /= np.sum(mid_weights)
        tau = calculate_ccar(mid_weights, scenario_costs, alpha=alpha) * 1.05

    count = 0
    max_attempts = n_samples * 100

    for _ in range(max_attempts):
        # Bangkitkan kandidat acak seragam dalam batas
        raw_w = np.random.uniform(lower_bounds, upper_bounds)
        norm_w = raw_w / np.sum(raw_w)

        # Periksa apakah setelah normalisasi masih berada dalam rentang toleransi
        if np.all(norm_w >= lower_bounds - 1e-4) and np.all(norm_w <= upper_bounds + 1e-4):
            # Proyeksikan tepat ke batas
            norm_w = np.clip(norm_w, lower_bounds, upper_bounds)
            norm_w /= np.sum(norm_w)

            c = calculate_expected_cost(norm_w, mu_vector)
            ccar_val = calculate_ccar(norm_w, scenario_costs, alpha=alpha)

            valid_weights.append(norm_w)
            costs.append(c)
            ccars.append(ccar_val)

            # Hitung selisih rasio efisiensi terhadap 1
            mccar_res = calculate_mccar(norm_w, scenario_costs, mu_vector, alpha=alpha)
            # Deviasi rata-rata rasio efisiensi dari 1 (keseimbangan ideal)
            eff_dev = np.mean(np.abs(mccar_res['efficiency_ratios'] - 1.0))
            efficiency_diffs.append(eff_dev)

            count += 1
            if count >= n_samples:
                break

    valid_weights = np.array(valid_weights)
    costs = np.array(costs)
    ccars = np.array(ccars)
    efficiency_diffs = np.array(efficiency_diffs)

    # Filter yang memenuhi kendala CCaR <= tau
    feasible_idx = np.where(ccars <= tau)[0]

    if len(feasible_idx) > 0:
        # Pilih yang meminimumkan biaya di antara yang feasible
        best_cost_idx = feasible_idx[np.argmin(costs[feasible_idx])]
        # Pilih yang memiliki rasio efisiensi paling seimbang
        best_eff_idx = feasible_idx[np.argmin(efficiency_diffs[feasible_idx])]
    else:
        best_cost_idx = np.argmin(costs)
        best_eff_idx = np.argmin(efficiency_diffs)

    return {
        'method': 'Random Filtering (DJPPR)',
        'best_cost_solution': {
            'weights': valid_weights[best_cost_idx],
            'cost': costs[best_cost_idx],
            'ccar': ccars[best_cost_idx]
        },
        'best_efficiency_solution': {
            'weights': valid_weights[best_eff_idx],
            'cost': costs[best_eff_idx],
            'ccar': ccars[best_eff_idx]
        },
        'all_weights': valid_weights,
        'all_costs': costs,
        'all_ccars': ccars,
        'tau': tau
    }
