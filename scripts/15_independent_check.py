"""Pemeriksaan independen hasil eksperimen (TIDAK mengimpor kode di src/mccar_kma).

Tujuan: memastikan angka yang dilaporkan pipeline benar, dengan evaluator yang ditulis ulang dari rumus
proposal (Persamaan 2.1-2.3, 2.13-2.20, 2.22). Hanya membaca; tidak mengubah file apa pun.

Pakai (dari root proyek):
    python scripts/99_independent_check.py                       # semua pemeriksaan
    python scripts/99_independent_check.py --noise-banks 50
    python scripts/99_independent_check.py --runs-dir results/runs_v2   # set run lain (mis. KMA baru)
Dependensi: numpy, pandas, scipy. Kode keluar 1 bila ada ketidakcocokan numerik.
"""
import argparse
import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linprog, minimize
from scipy.stats import fisher_exact

DELTA = 0.01
W0 = np.array([0.459485835, 0.113620854, 0.147798763, 0.143927407, 0.024401992, 0.066688212, 0.044076937])
LB = np.array([0.425, 0.10, 0.13, 0.13, 0.015, 0.05, 0.03])
UB = np.array([0.49, 0.125, 0.165, 0.155, 0.03, 0.085, 0.055])
CUR = [0, 0, 0, 1, 1, 2, 2]  # indeks mata uang tiap instrumen: USD, EUR, JPY
TOL = 1e-8
PROBLEMS = []


def check(ok, msg):
    print(("  [OK]    " if ok else "  [GAGAL] ") + msg)
    if not ok:
        PROBLEMS.append(msg)


def tail_mean(x, m):
    return np.sort(x)[-m:].mean()  # rata-rata m nilai terbesar, eksak (Pers. 2.13)


def evaluate(C, w, m):
    """Cost-bar, CCaR, J_MCCaR, theta untuk satu bobot. Ekor dipilih ULANG pada biaya yang ditambah delta*C_i."""
    cost = C @ w
    ccar = tail_mean(cost, m)
    mc = DELTA * C.mean(axis=0)
    mccar = np.array([tail_mean(cost + DELTA * C[:, i], m) - ccar for i in range(C.shape[1])])
    theta = mccar / mc
    return dict(mean=cost.mean(), ccar=ccar, J=np.sqrt(np.mean((theta - theta.mean()) ** 2)), theta=theta)


def load_bank(root, name):
    z = np.load(root / "data" / "processed" / name, allow_pickle=True)
    return {k: z[k] for k in z.files}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--noise-banks", type=int, default=30)
    ap.add_argument("--runs-dir", default="results/runs")
    a = ap.parse_args()
    root = Path(a.root).resolve()
    pd.set_option("display.width", 220)
    pd.set_option("display.max_columns", 30)

    tr = load_bank(root, "bank_train_seed42_N5000.npz")
    va = load_bank(root, "bank_valid_seed2026_N20000.npz")
    lim = json.load(open(root / "data/processed/risk_limits_bank_train_seed42_N5000.json"))
    m_tr, m_va = int(np.ceil(round(0.05 * len(tr["cost_gross"]), 9))), int(np.ceil(round(0.05 * len(va["cost_gross"]), 9)))

    print("\n[1] Biaya bank = rumus 2.1-2.3 dari skenario pasar")
    for nm, bk in (("latih", tr), ("validasi", va)):
        M, s0 = bk["scenarios_market"], bk["s0"]
        q = np.column_stack([np.ones(len(M)), s0[7] / M[:, 7], s0[8] / M[:, 8]])
        Cg = np.column_stack([q[:, CUR[i]] * (1 + M[:, i] / 100) for i in range(7)])
        Ci = np.column_stack([q[:, CUR[i]] * (M[:, i] / 100) for i in range(7)])
        check(abs(Cg - bk["cost_gross"]).max() < 1e-12 and abs(Ci - bk["cost_interest"]).max() < 1e-12, f"bank {nm}: cost_gross/cost_interest cocok rumus")

    print(f"\n[2] Batas η dan τ dari portofolio eksisting (m latih = {m_tr}, m validasi = {m_va})")
    check(m_tr == 250 and m_va == 1000, "m = 250 (N=5.000) dan 1.000 (N=20.000)")
    for cd in ("gross", "interest"):
        e = evaluate(tr[f"cost_{cd}"], W0, m_tr)
        check(abs(e["ccar"] - lim[cd]["tau"]) < 1e-10 and abs(e["J"] - lim[cd]["eta"]) < 1e-10,
              f"{cd}: τ={e['ccar']:.8f} η={e['J']:.8f} cocok file batas")

    print("\n[3] Hitung ulang semua solusi run")
    rows = []
    for f in sorted(glob.glob(str(root / a.runs_dir / "*/*/rep_*.json"))):
        r = json.load(open(f))
        cd, w = r["cost_definition"], np.array(r["best_w"])
        lo, hi = (np.zeros(7), np.ones(7)) if r["constraint_type"] == "free" else (LB, UB)
        e, v = evaluate(tr[f"cost_{cd}"], w, m_tr), evaluate(va[f"cost_{cd}"], w, m_va)
        tau, eta = lim[cd]["tau"], lim[cd]["eta"]
        rows.append(dict(cfg=r["config_id"], algo=r["algo"], rep=r["rep"], evals=r["evaluations"], flag=r["is_feasible"],
                         d_cost=abs(e["mean"] - r["best_cost"]), d_ccar=abs(e["ccar"] - r["ccar"]), d_J=abs(e["J"] - r["j_mccar"]),
                         sum_err=abs(w.sum() - 1), bnd=max((lo - w).max(), (w - hi).max(), 0),
                         cost=e["mean"], slack_R=(tau - e["ccar"]) / tau, slack_J=(eta - e["J"]) / eta,
                         val_slack_R=(tau - v["ccar"]) / tau, val_slack_J=(eta - v["J"]) / eta))
    d = pd.DataFrame(rows)
    check(len(d) == 360 and (d.groupby(["cfg", "algo"]).size() == 30).all(), f"{len(d)} run; 30 replikasi per konfigurasi×algoritma")
    check(max(d.d_cost.max(), d.d_ccar.max(), d.d_J.max()) < 1e-9, "cost, CCaR, J tersimpan = hitung ulang (selisih maks %.1e)" % max(d.d_cost.max(), d.d_ccar.max(), d.d_J.max()))
    d["ok"] = (d.slack_R > -TOL) & (d.slack_J > -TOL) & (d.sum_err < TOL) & (d.bnd < TOL)
    check(d.ok.all() and d.flag.all(), f"semua run layak menurut hitungan independen ({int(d.ok.sum())}/{len(d)})")
    check((d.evals == 25000).all(), "anggaran evaluasi tepat 25.000 di semua run")

    print("\n[4] Posisi terhadap batas kendala (slack 0 = kendala aktif) dan kelayakan di bank validasi")
    d["val_ok"] = (d.val_slack_R > -TOL) & (d.val_slack_J > -TOL)
    t = d.groupby(["cfg", "algo"]).agg(slack_CCaR=("slack_R", "mean"), slack_J=("slack_J", "mean"), val_layak=("val_ok", "sum"), val_slackJ_min=("val_slack_J", "min"))
    print(t.round(5).to_string())
    print(f"  korelasi slack_J latih vs validasi: {d[['slack_J', 'val_slack_J']].corr().iloc[0, 1]:.3f}  (tinggi = kelayakan validasi ditentukan seberapa dekat solusi ke batas)")
    x = d[(d.cfg == "interest_free")]
    if (x.algo == "pso").any() and (x.algo == "kma").any():
        p = x[x.algo == "pso"].val_ok.sum(); k = x[x.algo == "kma"].val_ok.sum()
        print(f"  Fisher PSO vs KMA di interest_free: {p}/30 vs {k}/30 layak, p = {fisher_exact([[p, 30 - p], [k, 30 - k]])[1]:.3f}")

    print("\n[5] Batas bawah LP (tanpa kendala risiko) dan solusi referensi SLSQP; selisih median tiap algoritma")
    for cd in ("gross", "interest"):
        C = tr[f"cost_{cd}"]; tau, eta = lim[cd]["tau"], lim[cd]["eta"]
        for bnd in ("free", "djppr"):
            lo, hi = (np.zeros(7), np.ones(7)) if bnd == "free" else (LB, UB)
            lp = linprog(C.mean(0), A_eq=np.ones((1, 7)), b_eq=[1], bounds=list(zip(lo, hi)))
            e = evaluate(C, lp.x, m_tr)
            lp_ok = e["ccar"] <= tau + 1e-9 and e["J"] <= eta + 1e-9
            cons = [{"type": "eq", "fun": lambda w: w.sum() - 1},
                    {"type": "ineq", "fun": lambda w: tau - evaluate(C, w, m_tr)["ccar"]},
                    {"type": "ineq", "fun": lambda w: eta - evaluate(C, w, m_tr)["J"]}]
            rng, best = np.random.default_rng(0), None
            for x0 in [lp.x, W0] + [np.clip(rng.uniform(lo, hi), lo, hi) for _ in range(8)]:
                x0 = x0 / x0.sum()
                try:
                    s = minimize(lambda w: C.mean(0) @ w, x0, method="SLSQP", bounds=list(zip(lo, hi)), constraints=cons, options=dict(maxiter=300, ftol=1e-12))
                except Exception:
                    continue
                w = np.clip(s.x, lo, hi); w /= w.sum(); ev = evaluate(C, w, m_tr)
                if ev["ccar"] <= tau * (1 + 1e-8) and ev["J"] <= eta * (1 + 1e-8) and (best is None or ev["mean"] < best):
                    best = ev["mean"]
            g = d[d.cfg == f"{cd}_{bnd}"].groupby("algo").cost.median()
            ref = min(best if best else np.inf, d[d.cfg == f"{cd}_{bnd}"].cost.min())
            print(f"  {cd}_{bnd:5s} LP-bawah={lp.fun:.6f} (LP layak: {lp_ok}) | referensi terbaik={ref:.6f} | selisih median (%): " +
                  ", ".join(f"{k}={100 * (v - ref) / ref:.4f}" for k, v in g.items()))
            if lp_ok:
                print("      -> optimum LP sudah memenuhi J dan CCaR: kendala risiko TIDAK aktif pada konfigurasi ini")

    print(f"\n[6] Kebisingan batas η, τ antar {a.noise_banks} bank independen (N=5.000, portofolio eksisting)")
    p = pd.read_csv(root / "data/processed/gbm_params_intersection.csv").set_index("variable")
    corr = pd.read_csv(root / "data/processed/corr_intersection.csv", index_col=0).values
    L, mu, sg, s0 = np.linalg.cholesky(corr), p["mu_annual"].values, p["sigma_annual"].values, tr["s0"]
    out = []
    for seed in range(100, 100 + a.noise_banks):
        Z = np.random.default_rng(seed).standard_normal((5000, 9)) @ L.T
        S = s0 * np.exp(mu - 0.5 * sg ** 2 + sg * Z)
        q = np.column_stack([np.ones(5000), s0[7] / S[:, 7], s0[8] / S[:, 8]])
        for cd, fn in (("gross", lambda y: 1 + y / 100), ("interest", lambda y: y / 100)):
            C = np.column_stack([q[:, CUR[i]] * fn(S[:, i]) for i in range(7)])
            e = evaluate(C, W0, 250); out.append(dict(cd=cd, tau=e["ccar"], eta=e["J"]))
    o = pd.DataFrame(out)
    for cd, g in o.groupby("cd"):
        z = (lim[cd]["eta"] - g.eta.mean()) / g.eta.std()
        print(f"  {cd:8s} τ: rata-rata={g.tau.mean():.5f} CV={100 * g.tau.std() / g.tau.mean():.2f}% | η: rata-rata={g.eta.mean():.5f} CV={100 * g.eta.std() / g.eta.mean():.2f}% "
              f"[{g.eta.min():.4f}, {g.eta.max():.4f}] | η bank latih = {lim[cd]['eta']:.5f} (z = {z:+.2f})")

    print("\nRINGKASAN:", "SEMUA PEMERIKSAAN NUMERIK LOLOS" if not PROBLEMS else f"{len(PROBLEMS)} MASALAH: " + "; ".join(PROBLEMS))
    return 1 if PROBLEMS else 0


if __name__ == "__main__":
    sys.exit(main())
