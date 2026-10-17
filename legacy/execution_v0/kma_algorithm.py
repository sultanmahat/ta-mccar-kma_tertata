"""
Modul Implementasi Utama: Komodo Mlipir Algorithm (KMA)
Berdasarkan Suyanto et al. (2022) & Proposal Tugas Akhir Sultan Bakri Baihaqi Mahat (Subbab 2.8 & 3.6.3).

Komponen KMA:
1. Pembagian Populasi: q Big Males, 1 Female, s Small Males.
2. Pergerakan Big Males (Persamaan 2.11 - 2.12) -> Eksploitasi tinggi.
3. Reproduksi Female (Persamaan 2.13 - 2.15):
   - Mating dengan winner big male.
   - Parthenogenesis dengan radius mutasi alpha = 0.1.
4. Pergerakan Small Males (Persamaan 2.16 - 2.17) -> Gerakan Mlipir dengan rate d.
5. Adaptasi Ukuran Populasi (Persamaan 2.18 - 2.19).
6. Kriteria Penghentian Gabungan: ||x^(k) - x^(k-1)|| <= epsilon atau k >= k_max.
"""

import numpy as np
from .risk_metrics import calculate_expected_cost, calculate_ccar, calculate_mccar

def project_to_feasible_weights(weights, lower_bounds, upper_bounds):
    """
    Memproyeksikan vektor bobot sembarang agar:
    1. Memenuhi batas box: lb_i <= w_i <= ub_i
    2. Memenuhi kendala anggaran: sum(w_i) = 1
    Menggunakan algoritma projection-bisection sederhana.
    """
    w = np.clip(weights, lower_bounds, upper_bounds)
    sum_w = np.sum(w)
    if abs(sum_w - 1.0) < 1e-7:
        return w

    # Bisection search untuk mencari offset c sehingga sum(clip(w + c, lb, ub)) = 1
    c_low = np.min(lower_bounds - weights)
    c_high = np.max(upper_bounds - weights)

    for _ in range(50):
        c_mid = (c_low + c_high) / 2.0
        w_trial = np.clip(weights + c_mid, lower_bounds, upper_bounds)
        s = np.sum(w_trial)
        if abs(s - 1.0) < 1e-6:
            return w_trial
        elif s < 1.0:
            c_low = c_mid
        else:
            c_high = c_mid

    w_final = np.clip(weights + (c_low + c_high) / 2.0, lower_bounds, upper_bounds)
    return w_final / np.sum(w_final)

class KomodoMlipirOptimizer:
    def __init__(self, scenario_costs, mu_vector, lower_bounds, upper_bounds,
                 tau=None, n_pop=50, p_big=0.3, mlipir_rate=0.5, alpha_mutation=0.1,
                 penalty_factor=100.0, max_iter=200, epsilon=1e-5,
                 adaptive_pop=True, a_pop=2, min_pop=20, max_pop=100,
                 risk_alpha=0.95, seed=42):
        """
        Inisialisasi Parameter KMA.
        """
        self.scenario_costs = scenario_costs
        self.mu_vector = mu_vector
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds
        self.dim = len(mu_vector)

        # Jika tau belum diisi, gunakan toleransi dari titik tengah bounds
        if tau is None:
            mid_w = (lower_bounds + upper_bounds) / 2.0
            mid_w /= np.sum(mid_w)
            self.tau = calculate_ccar(mid_w, scenario_costs, alpha=risk_alpha) * 1.05
        else:
            self.tau = tau

        self.n_pop = n_pop
        self.p_big = p_big
        self.mlipir_rate = mlipir_rate
        self.alpha_mutation = alpha_mutation
        self.penalty_factor = penalty_factor
        self.max_iter = max_iter
        self.epsilon = epsilon
        self.adaptive_pop = adaptive_pop
        self.a_pop = a_pop
        self.min_pop = min_pop
        self.max_pop = max_pop
        self.risk_alpha = risk_alpha
        self.seed = seed

        if seed is not None:
            np.random.seed(seed)

    def evaluate_fitness(self, w_raw):
        """
        Menghitung nilai fitness (fungsi objektif terpenalti):
        f(w) = Cost(w) + penalty * max(0, CCaR(w) - tau)
        """
        w = project_to_feasible_weights(w_raw, self.lower_bounds, self.upper_bounds)
        cost = calculate_expected_cost(w, self.mu_vector)
        ccar = calculate_ccar(w, self.scenario_costs, alpha=self.risk_alpha)
        
        # Penalti jika melanggar batas risiko ekor
        risk_violation = max(0.0, ccar - self.tau)
        fitness = cost + self.penalty_factor * (risk_violation ** 2)

        return fitness, cost, ccar, w

    def optimize(self):
        """
        Menjalankan loop utama Algoritma Komodo Mlipir (KMA).
        """
        # Inisialisasi populasi
        population = []
        for _ in range(self.n_pop):
            raw_w = np.random.uniform(self.lower_bounds, self.upper_bounds)
            population.append(project_to_feasible_weights(raw_w, self.lower_bounds, self.upper_bounds))
        population = np.array(population)

        best_history = []
        best_solution_pos = None
        best_fitness = float('inf')
        best_cost = None
        best_ccar = None

        # Riwayat fitness terbaik untuk adaptasi populasi
        f_history = []

        iteration_converged = self.max_iter

        for it in range(1, self.max_iter + 1):
            # Evaluasi fitness untuk setiap individu
            fitness_list = []
            costs_list = []
            ccars_list = []
            feasible_pop = []

            for ind in population:
                fit, c, ccar_val, w_feas = self.evaluate_fitness(ind)
                fitness_list.append(fit)
                costs_list.append(c)
                ccars_list.append(ccar_val)
                feasible_pop.append(w_feas)

            fitness = np.array(fitness_list)
            population = np.array(feasible_pop)

            # Urutkan berdasarkan fitness (minimasi: fitness terkecil terbaik)
            sort_idx = np.argsort(fitness)
            population = population[sort_idx]
            fitness = fitness[sort_idx]
            costs_list = np.array(costs_list)[sort_idx]
            ccars_list = np.array(ccars_list)[sort_idx]

            # Cek pembaruan best solution
            prev_best_pos = np.copy(best_solution_pos) if best_solution_pos is not None else None

            if fitness[0] < best_fitness:
                best_fitness = fitness[0]
                best_solution_pos = np.copy(population[0])
                best_cost = costs_list[0]
                best_ccar = ccars_list[0]

            best_history.append({
                'iteration': it,
                'fitness': best_fitness,
                'cost': best_cost,
                'ccar': best_ccar,
                'population_size': len(population)
            })

            # Cek stopping criteria (norm difference)
            if prev_best_pos is not None:
                norm_diff = np.linalg.norm(best_solution_pos - prev_best_pos)
                if norm_diff <= self.epsilon and it > 20:
                    iteration_converged = it
                    break

            # Pembagian populasi: q Big Males, 1 Female, s Small Males
            n_current = len(population)
            q = max(1, int(np.round(self.p_big * n_current)))
            
            # Big Males: 0 sampai q-1
            # Female: indeks q
            # Small Males: indeks q+1 sampai n_current-1
            if q >= n_current - 1:
                q = max(1, n_current - 2)

            new_population = []

            # 1. Pergerakan Big Males (Persamaan 2.11 - 2.12)
            for i in range(q):
                k_i = population[i]
                w_ij_sum = np.zeros(self.dim)
                for j in range(q):
                    if j != i:
                        k_j = population[j]
                        r1 = np.random.rand()
                        r2 = np.random.rand()
                        if fitness[j] < fitness[i] or r2 < 0.5:
                            w_ij = r1 * (k_j - k_i)
                        else:
                            w_ij = r1 * (k_i - k_j)
                        w_ij_sum += w_ij
                k_i_new = k_i + w_ij_sum
                new_population.append(project_to_feasible_weights(k_i_new, self.lower_bounds, self.upper_bounds))

            # 2. Reproduksi Female (Persamaan 2.13 - 2.15)
            female_idx = q
            if female_idx < n_current:
                k_female = population[female_idx]
                k_winner_male = population[0] # Winner big male
                mating_prob = np.random.rand()

                if mating_prob < 0.5:
                    # Mating
                    r_l = np.random.rand(self.dim)
                    k_female_new1 = r_l * k_female + (1.0 - r_l) * k_winner_male
                    new_population.append(project_to_feasible_weights(k_female_new1, self.lower_bounds, self.upper_bounds))
                else:
                    # Parthenogenesis
                    r = np.random.rand(self.dim)
                    bound_range = np.abs(self.upper_bounds - self.lower_bounds)
                    k_female_new2 = k_female + (2.0 * r - 1.0) * self.alpha_mutation * bound_range
                    new_population.append(project_to_feasible_weights(k_female_new2, self.lower_bounds, self.upper_bounds))

            # 3. Pergerakan Small Males (Persamaan 2.16 - 2.17)
            for i in range(q + 1, n_current):
                k_i = population[i]
                k_i_new = np.copy(k_i)
                for l in range(self.dim):
                    r2 = np.random.rand()
                    if r2 < self.mlipir_rate:
                        r1 = np.random.rand()
                        # Gerakan mlipir mengikuti big males pada dimensi l
                        diff_sum = np.sum([r1 * (population[j][l] - k_i[l]) for j in range(q)])
                        k_i_new[l] += diff_sum
                new_population.append(project_to_feasible_weights(k_i_new, self.lower_bounds, self.upper_bounds))

            # 4. Adaptasi Ukuran Populasi (Persamaan 2.18 - 2.19)
            f_history.append(best_fitness)
            if self.adaptive_pop and len(f_history) >= 3:
                f_n = f_history[-1]
                f_n1 = f_history[-2]
                f_n2 = f_history[-3]

                delta_f1 = (f_n1 - f_n) / abs(f_n1) if abs(f_n1) > 1e-9 else 0.0
                delta_f2 = (f_n2 - f_n1) / abs(f_n2) if abs(f_n2) > 1e-9 else 0.0

                if delta_f1 > 0 and delta_f2 > 0:
                    # Kualitas meningkat 2 generasi beruntun -> kurangi populasi
                    target_n = max(self.min_pop, len(new_population) - self.a_pop)
                    new_population = new_population[:target_n]
                elif abs(delta_f1) < 1e-7 and abs(delta_f2) < 1e-7:
                    # Stagnasi -> tambahkan populasi untuk eksplorasi
                    target_n = min(self.max_pop, len(new_population) + self.a_pop)
                    while len(new_population) < target_n:
                        rand_w = np.random.uniform(self.lower_bounds, self.upper_bounds)
                        new_population.append(project_to_feasible_weights(rand_w, self.lower_bounds, self.upper_bounds))

            population = np.array(new_population)

        # Evaluasi akhir solusi terbaik
        final_mccar = calculate_mccar(best_solution_pos, self.scenario_costs, self.mu_vector, alpha=self.risk_alpha)

        return {
            'method': 'Komodo Mlipir Algorithm (KMA)',
            'best_solution': {
                'weights': best_solution_pos,
                'cost': best_cost,
                'ccar': best_ccar,
                'fitness': best_fitness,
                'mccar_details': final_mccar
            },
            'convergence_history': best_history,
            'converged_iteration': iteration_converged,
            'tau': self.tau
        }
