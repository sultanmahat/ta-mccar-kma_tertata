# Keputusan D6: Detail Parameter dan Mekanisme GA & PSO

- **Tanggal Usulan**: 2026-10-18
- **Status**: Diusulkan agen / Menunggu konfirmasi Sultan
- **Diusulkan oleh**: Agen AI (Pair Programming)
- **Pihak yang Mengonfirmasi**: Sultan Bakri Baihaqi Mahat (Mahasiswa)

## Ringkasan Keputusan

Untuk melengkapi parameter pembanding metaheuristik Genetic Algorithm (GA) dan Particle Swarm Optimization (PSO) pada Tabel 3.1 dan Spesifikasi §7.2–7.3, ditetapkan keputusan sebagai berikut:

| Butir Keputusan | Simbol / Konsep | Nilai Terpilih | Dasar Pertimbangan / Rujukan |
|---|---|---|---|
| **D6.1: Elitisme GA** | $n_{\text{elite}}$ | $2$ individu | Mempertahankan 2 individu terbaik secara utuh; 48 keturunan dihasilkan dari 24 persilangan aritmetika. Menjamin kebugaran (*fitness*) terbaik tidak terdegradasi secara acak. |
| **D6.2: Inisialisasi Populasi Bersama** | — | Pembangkitan acak seragam $[lb, ub]$ + proyeksi `project_weights` | Identik 100% dengan mekanisme pembentukan populasi KMA. Portofolio eksisting $w_0$ **tidak** dimasukkan (Spesifikasi §11). |
| **D6.3: Kecepatan PSO Pasca-Proyeksi** | $v_i^{(t+1)}$ | $v_i^{(t+1)} \leftarrow \text{clip}(x_{i, \text{proj}}^{(t+1)} - x_i^{(t)}, -v_{\text{max}}, v_{\text{max}})$ | Menjaga konsistensi vektor arah kecepatan partikel dengan perpindahan efektif pada manifold simpleks $\sum w_i = 1$. |
| **D6.4: Jadwal Inersia PSO** | $\omega(\text{eval})$ | Penurunan linear terhadap jumlah evaluasi fungsi terpakai: $0{,}9 \to 0{,}4$ | Selaras dengan antarmuka pelacak anggaran universal `BudgetCounter` hingga tepat evaluasi ke-25.000. |

Nilai di `configs/params.yaml`:
```yaml
algorithms:
  ga:
    n_pop: 50
    tournament_size: 2
    p_crossover: 0.9
    p_mutation: 0.14285714285714285
    sigma_m_factor: 0.1
    elitism_count: 2

  pso:
    n_pop: 50
    w_start: 0.9
    w_end: 0.4
    c1: 1.49618
    c2: 1.49618
    v_max_factor: 0.2
    velocity_clamp_strategy: "effective_displacement"
    inertia_schedule: "evaluations_linear"
    shared_init_strategy: "uniform_box_projected"
```

---

## Alasan Keputusan

1. **Keadilan Komparasi**: Ketiga algoritma (KMA, GA, PSO) memiliki perlakuan yang setara:
   - Anggaran evaluasi fungsi sama persis: 25.000 per replikasi.
   - Proyeksi kendala yang sama: `project_weights` ke $\sum w_i = 1$ dan $lb \le w \le ub$.
   - Mekanisme seleksi arsip yang sama: `FeasibleArchive` berbasis biaya rata-rata terendah pada solusi layak ($v_J, v_R \le 10^{-8}$).
   - Inisialisasi awal yang sama: acak seragam dalam box proporsi yang diproyeksikan, tanpa membocorkan $w_0$.
2. **Stabilitas Numerik PSO**: Pada kendala kesetaraan ketat $\sum w_i = 1$, partikel yang bergerak secara bebas di $\mathbb{R}^D$ dapat menghasilkan kecepatan yang mengarah ke luar simpleks. Re-estimasi kecepatan efektif $x_{\text{proj}} - x_{\text{old}}$ menjamin akumulasi inersia tetap relevan dengan ruang pencarian portofolio.
3. **Elitisme GA**: Menetapkan $n_{\text{elite}} = 2$ sangat alami untuk ukuran populasi genap ($n=50$) dengan persilangan yang menghasilkan 2 anak per pasangan orang tua.
