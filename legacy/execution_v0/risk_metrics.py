"""
Modul Perhitungan Ukuran Risiko Ekor dan Biaya Portofolio:
- Expected Cost (Persamaan 3.2)
- Conditional Cost-at-Risk (CCaR, Persamaan 2.10)
- Marginal Conditional Cost-at-Risk (MCCaR, Persamaan 2.11)
- Rasio Efisiensi (Persamaan 2.12 & Tabel 2.1)
"""

import numpy as np

def calculate_expected_cost(weights, mu_vector):
    """
    Menghitung biaya ekspektasi portofolio:
    E[Cost] = mu^T * w
    """
    return float(np.dot(weights, mu_vector))

def calculate_portfolio_scenarios(weights, scenario_costs):
    """
    Menghitung total biaya portofolio pada setiap skenario s:
    Cost_s(w) = sum_{i=1}^n w_i * scenario_costs[s, i]
    scenario_costs: matriks berukuran (n_paths, n_instruments)
    weights: vektor bobot w (array 1D)
    """
    return np.dot(scenario_costs, weights)

def calculate_ccar(weights, scenario_costs, alpha=0.95):
    """
    Menghitung Conditional Cost at Risk (CCaR_alpha):
    CCaR_alpha(w) = (1 / |S_alpha|) * sum_{s in S_alpha} Cost_s(w)
    di mana S_alpha adalah (1 - alpha) fraksi skenario dengan biaya TERTINGGI (tail risk).
    """
    port_costs = calculate_portfolio_scenarios(weights, scenario_costs)
    
    # Ambil persentil (1 - alpha) terburuk (misal alpha=0.95 -> 5% biaya tertinggi)
    cutoff = np.percentile(port_costs, alpha * 100.0)
    tail_costs = port_costs[port_costs >= cutoff]
    
    if len(tail_costs) == 0:
        return float(np.max(port_costs))
    
    return float(np.mean(tail_costs))

def calculate_mccar(weights, scenario_costs, mu_vector, delta=0.01, alpha=0.95):
    """
    Menghitung Marginal Conditional Cost at Risk (MCCaR) dan Rasio Efisiensi
    untuk setiap instrumen:
    
    MCCaR_{p, i} = CCaR_{101%, i} - CCaR_{100%}
    di mana CCaR_{101%, i} adalah CCaR setelah proporsi instrumen i ditambah sebesar delta (1%).
    
    Rasio Efisiensi_i = MCCaR_{p, i} / MC_i
    dengan MC_i adalah biaya marginal (mu_i atau selisih biaya penambahan 1%).
    """
    n_instruments = len(weights)
    baseline_ccar = calculate_ccar(weights, scenario_costs, alpha=alpha)
    baseline_cost = calculate_expected_cost(weights, mu_vector)

    mccar_vector = np.zeros(n_instruments)
    marginal_cost = np.zeros(n_instruments)
    efficiency_ratios = np.zeros(n_instruments)

    for i in range(n_instruments):
        # Tambahkan delta (misal 1% = 0.01) pada instrumen i
        w_perturbed = np.copy(weights)
        w_perturbed[i] += delta
        
        # Opsi: re-normalisasi agar total bobot tetap 1, atau direct sensitivity
        # Sesuai definisi DJPPR & Yavuz (2019): CCaR_{101%, i}
        ccar_perturbed = calculate_ccar(w_perturbed, scenario_costs, alpha=alpha)
        cost_perturbed = calculate_expected_cost(w_perturbed, mu_vector)

        mccar_vector[i] = ccar_perturbed - baseline_ccar
        mc = cost_perturbed - baseline_cost
        
        # Hindari pembagian dengan nol
        marginal_cost[i] = mc if abs(mc) > 1e-9 else 1e-9
        efficiency_ratios[i] = mccar_vector[i] / marginal_cost[i]

    return {
        'baseline_ccar': baseline_ccar,
        'baseline_cost': baseline_cost,
        'mccar_vector': mccar_vector,
        'marginal_cost': marginal_cost,
        'efficiency_ratios': efficiency_ratios
    }
