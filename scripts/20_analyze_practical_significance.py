"""Tahap 20: Analisis signifikansi praktis (melengkapi, bukan mengganti, Tahap 13).

Menjawab 4 tugas:
1. Selisih median (%, satuan biaya), estimator Hodges-Lehmann + CI bootstrap,
   dan uji ekivalensi (TOST non-parametrik + CI-vs-margin) untuk tiap pasangan
   algoritma per konfigurasi, memakai results/tables/runs_summary.csv (sumber
   yang sama dengan Tahap 13) -- tidak menjalankan ulang optimasi.
2. Status kendala aktif (J, CCaR) dan vertex kotak-simpleks ("optimum LP
   layak") per run, dibaca ulang dari results/runs/**/*.json, diringkas per
   config_id.
3. Waktu komputasi 1 proses (results/tables/timing_single_worker_360.csv,
   Tahap 19) dibandingkan dengan waktu 6-worker (results/tables/stats_<cid>.csv,
   Tahap 13).
4. Uji eksak Fisher dan Barnard untuk tabel kelayakan validasi 2x2
   (results/tables/validation_<config_id>.csv, Tahap 12), koreksi Holm per
   config_id.

Keluaran: results/tables/stats_praktis.csv, results/tables/fisher_feasibility.csv,
docs/reviews/signifikansi_praktis.md. Tidak menulis ke results/tables/runs_summary.csv
maupun results/runs/.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

from mccar_kma.analysis import practical_significance as ps
from mccar_kma.analysis.stats_tests import holm_bonferroni_correction
from mccar_kma.experiments.runner import get_bounds_for_constraint

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_IDS = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]
ALGOS = ["kma", "ga", "pso"]
PAIRS = list(itertools.combinations(ALGOS, 2))


def task1_task2(cfg: dict) -> pd.DataFrame:
    """Selisih praktis (Tugas 1) + kendala aktif & LP-vertex (Tugas 2), 1 baris per config_id+pasangan."""
    pcfg = cfg["practical_significance"]
    margin_pct = float(pcfg["equivalence_margin_pct"])
    resamples = int(pcfg["bootstrap_resamples"])
    bseed = int(pcfg["bootstrap_seed"])
    level = float(pcfg["confidence_level"])
    rel_tol = float(pcfg["j_r_active_rel_tol"])
    bound_tol = float(pcfg["bound_active_abs_tol"])

    df_runs = pd.read_csv(BASE_DIR / "results" / "tables" / "runs_summary.csv")
    runs_dir = BASE_DIR / "results" / "runs"

    rows = []
    for cid in CONFIG_IDS:
        sub = df_runs[df_runs["config_id"] == cid]
        margin_abs = margin_pct / 100.0 * float(sub["best_cost"].median())

        # --- Tugas 2 dihitung dulu (agregat seluruh run config ini), lalu dilekatkan ke tiap pasangan ---
        constraint_type = cid.split("_", 1)[1]
        lb, ub = get_bounds_for_constraint(constraint_type)
        flags = []
        for p in sorted((runs_dir / cid).rglob("rep_*.json")):
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
            flags.append(ps.lp_vertex_feasible(
                w=d["best_w"], lb=lb, ub=ub, bound_tol=bound_tol,
                j_mccar=d["j_mccar"], eta=d["eta_limit"],
                ccar=d["ccar"], tau=d["tau_limit"], rel_tol=rel_tol,
            ))
        n = len(flags)
        j_frac = sum(f["j_active"] for f in flags) / n
        r_frac = sum(f["r_active"] for f in flags) / n
        vtx_frac = sum(f["is_lp_vertex"] for f in flags) / n
        lp_frac = sum(f["lp_feasible"] for f in flags) / n
        mean_bound_active = float(np.mean([f["n_bound_active"] for f in flags]))

        if lp_frac >= 0.8:
            catatan = (
                f"{cid}: optimum didominasi vertex kotak-simpleks (rata-rata {mean_bound_active:.1f}/7 "
                f"bobot di batas), kendala risiko tidak aktif pada {lp_frac*100:.0f}% run -- ketiga "
                "algoritma konvergen ke titik yang hampir identik secara geometris, bukan karena satu "
                "algoritma lebih unggul."
            )
        elif j_frac >= 0.5 or r_frac >= 0.5:
            catatan = (
                f"{cid}: kendala risiko aktif pada sebagian besar run (J aktif {j_frac*100:.0f}%, "
                f"CCaR aktif {r_frac*100:.0f}%) -- solusi ditahan oleh batas J/CCaR, bukan oleh batas kotak."
            )
        else:
            catatan = (
                f"{cid}: tidak dominan vertex kotak ({vtx_frac*100:.0f}% run) maupun kendala risiko aktif "
                f"(J {j_frac*100:.0f}%, CCaR {r_frac*100:.0f}%) -- ruang gerak lebih bebas, selisih antar "
                "algoritma lebih mungkin mencerminkan perbedaan eksplorasi nyata."
            )

        task2_fields = {
            "j_aktif_frac": j_frac, "r_aktif_frac": r_frac,
            "lp_vertex_frac": vtx_frac, "lp_feasible_frac": lp_frac,
            "mean_bound_active": mean_bound_active, "catatan": catatan,
        }

        # --- Tugas 1: selisih praktis per pasangan ---
        for a, b in PAIRS:
            x = sub[sub["algo"] == a]["best_cost"].to_numpy(dtype=float)
            y = sub[sub["algo"] == b]["best_cost"].to_numpy(dtype=float)
            diff = ps.median_diff_pct(x, y)
            hl = ps.hodges_lehmann_estimator(x, y)
            ci = ps.bootstrap_hl_ci(x, y, resamples=resamples, seed=bseed, level=level)
            tost = ps.equivalence_test_tost(x, y, margin=margin_abs, alpha=0.05)
            eq_ci = ps.equivalence_via_ci(hl, ci, margin=margin_abs)
            rows.append({
                "config_id": cid, "pair": f"{a}_vs_{b}",
                "median_a": diff["median_x"], "median_b": diff["median_y"],
                "diff_abs": diff["diff_abs"], "diff_pct": diff["diff_pct"],
                "hodges_lehmann": hl, "hl_ci_lo": ci[0], "hl_ci_hi": ci[1],
                "equivalence_margin_abs": margin_abs,
                "tost_p": tost["p_tost"], "tost_equivalent": tost["is_equivalent"],
                "ci_equivalent": eq_ci,
                **task2_fields,
            })

    return pd.DataFrame(rows)


def task3_timing(cfg: dict) -> pd.DataFrame:
    """Waktu 1-proses (Tahap 19) vs waktu 6-worker (Tahap 13), ringkasan per config/algo."""
    sw_path = BASE_DIR / cfg["single_worker_timing"]["output_path"]
    df_sw = pd.read_csv(sw_path)
    rows = []
    for cid in CONFIG_IDS:
        stats_path = BASE_DIR / "results" / "tables" / f"stats_{cid}.csv"
        df_stats = pd.read_csv(stats_path)
        for algo in ALGOS:
            sw_sub = df_sw[(df_sw["config_id"] == cid) & (df_sw["algo"] == algo)]
            st_row = df_stats[df_stats["algo"].str.lower() == algo].iloc[0]
            rows.append({
                "config_id": cid, "algo": algo,
                "time_1proc_median_s": float(sw_sub["time_seconds"].median()),
                "time_1proc_n": int(len(sw_sub)),
                "time_6worker_mean_s": float(st_row["mean_time_sec"]),
                "machine_cpu": sw_sub["machine_cpu"].iloc[0],
                "machine_cores_logical": int(sw_sub["machine_cores_logical"].iloc[0]),
                "os_version": sw_sub["os_version"].iloc[0],
            })
    df = pd.DataFrame(rows)
    df["ratio_1proc_over_6worker"] = df["time_1proc_median_s"] / df["time_6worker_mean_s"]
    return df


def task4_fisher(cfg: dict) -> pd.DataFrame:
    """Fisher/Barnard untuk kelayakan validasi 2x2, koreksi Holm per config_id (Tugas 4)."""
    rows = []
    for cid in CONFIG_IDS:
        df_val = pd.read_csv(BASE_DIR / "results" / "tables" / f"validation_{cid}.csv")
        feas = {a: df_val[df_val["algo"] == a]["val_is_feasible"] for a in ALGOS}
        p_fisher_list, p_barnard_list, pair_rows = [], [], []
        for a, b in PAIRS:
            ka, na = int(feas[a].sum()), int(len(feas[a]))
            kb, nb = int(feas[b].sum()), int(len(feas[b]))
            table = [[ka, na - ka], [kb, nb - kb]]
            res = ps.contingency_exact_test(table)
            pair_rows.append({
                "config_id": cid, "pair": f"{a}_vs_{b}",
                "k_a": ka, "n_a": na, "k_b": kb, "n_b": nb,
                "p_fisher": res["p_fisher"], "p_barnard": res["p_barnard"],
            })
            p_fisher_list.append(res["p_fisher"])
            p_barnard_list.append(res["p_barnard"])
        p_fisher_holm = holm_bonferroni_correction(p_fisher_list)
        p_barnard_holm = holm_bonferroni_correction(p_barnard_list)
        for i, row in enumerate(pair_rows):
            row["p_fisher_holm"] = float(p_fisher_holm[i])
            row["p_barnard_holm"] = float(p_barnard_holm[i])
            rows.append(row)
    return pd.DataFrame(rows)


def write_report(df_main: pd.DataFrame, df_timing: pd.DataFrame, df_fisher: pd.DataFrame, cfg: dict) -> None:
    pcfg = cfg["practical_significance"]
    lines = [
        "# Signifikansi Praktis 360 Run — Selisih Biaya, Kendala Aktif, Waktu, Kelayakan",
        "",
        "**Tahap**: 19-20 (`scripts/19_measure_single_worker_timing.py`, "
        "`scripts/20_analyze_practical_significance.py`)",
        "",
        "Laporan ini **melengkapi** Tahap 13 (`results/tables/stats_summary.md`), tidak "
        "menggantikannya. Kruskal-Wallis/Dunn Tahap 13 valid secara statistik "
        "($p\\ll0{,}001$, $\\epsilon^2$ besar) — pertanyaannya di sini adalah seberapa "
        "**bermakna secara praktis** selisih itu, bukan apakah selisihnya nyata secara "
        "statistik (selisih yang sangat kecil pun bisa signifikan dengan presisi numerik "
        "tinggi dan $n=30$).",
        "",
        f"Margin ekivalensi (D12): **{pcfg['equivalence_margin_pct']}%** relatif terhadap "
        "median biaya grup pembanding (Opsi A, lihat `docs/decisions/0012-*.md`).",
        "",
        "> **Tidak ada klaim algoritma 'terbaik' di laporan ini.** Tabel di bawah melaporkan "
        "selisih, interval, dan status ekivalensi/kelayakan apa adanya.",
        "",
        "---",
        "",
        "## 1. Selisih praktis, Hodges-Lehmann, dan ekivalensi (TOST)",
        "",
    ]

    for cid in CONFIG_IDS:
        sub = df_main[df_main["config_id"] == cid]
        lines += [f"### `{cid}`", "", sub.iloc[0]["catatan"], ""]
        lines += [
            "| Pasangan | Median A | Median B | Selisih (satuan) | Selisih (%) | Hodges-Lehmann | CI 95% HL | TOST ekivalen? | CI-margin ekivalen? |",
            "|---|---:|---:|---:|---:|---:|---|:---:|:---:|",
        ]
        for _, r in sub.iterrows():
            lines.append(
                f"| {r['pair']} | `{r['median_a']:.6f}` | `{r['median_b']:.6f}` | `{r['diff_abs']:.2e}` | "
                f"`{r['diff_pct']:.4f}%` | `{r['hodges_lehmann']:.2e}` | "
                f"[`{r['hl_ci_lo']:.2e}`, `{r['hl_ci_hi']:.2e}`] | "
                f"{'Ya' if r['tost_equivalent'] else 'Tidak'} | {'Ya' if r['ci_equivalent'] else 'Tidak'} |"
            )
        lines.append("")

    lines += [
        "---",
        "",
        "## 2. Kendala aktif dan vertex kotak-simpleks (\"optimum LP\")",
        "",
        "| Konfigurasi | J aktif | CCaR aktif | Vertex kotak-simpleks | Vertex & kendala risiko tidak aktif | Rata-rata bobot di batas |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    seen = set()
    for _, r in df_main.iterrows():
        if r["config_id"] in seen:
            continue
        seen.add(r["config_id"])
        lines.append(
            f"| `{r['config_id']}` | {r['j_aktif_frac']*100:.0f}% | {r['r_aktif_frac']*100:.0f}% | "
            f"{r['lp_vertex_frac']*100:.0f}% | {r['lp_feasible_frac']*100:.0f}% | {r['mean_bound_active']:.1f}/7 |"
        )
    lines.append("")

    lines += [
        "---",
        "",
        "## 3. Waktu komputasi: 1 proses vs 6-worker",
        "",
        f"Mesin: `{df_timing.iloc[0]['machine_cpu']}`, {df_timing.iloc[0]['machine_cores_logical']} core logis, "
        f"`{df_timing.iloc[0]['os_version']}`. 1-proses = median {int(df_timing.iloc[0]['time_1proc_n'])} "
        "replikasi baru (seed terpisah, tidak menimpa 360 run utama); 6-worker = rata-rata 30 replikasi "
        "eksperimen utama Tahap 10/13.",
        "",
        "| Konfigurasi | Algo | Waktu 1-proses (median, s) | Waktu 6-worker (mean, s) | Rasio |",
        "|---|---|---:|---:|---:|",
    ]
    for _, r in df_timing.iterrows():
        lines.append(
            f"| `{r['config_id']}` | {r['algo'].upper()} | {r['time_1proc_median_s']:.2f} | "
            f"{r['time_6worker_mean_s']:.2f} | {r['ratio_1proc_over_6worker']:.2f}x |"
        )
    lines.append("")

    lines += [
        "---",
        "",
        "## 4. Kelayakan validasi OOS: Fisher dan Barnard (koreksi Holm per konfigurasi)",
        "",
        "| Konfigurasi | Pasangan | k/n A | k/n B | p Fisher | p Fisher Holm | p Barnard | p Barnard Holm |",
        "|---|---|---|---|---:|---:|---:|---:|",
    ]
    for _, r in df_fisher.iterrows():
        lines.append(
            f"| `{r['config_id']}` | {r['pair']} | {r['k_a']}/{r['n_a']} | {r['k_b']}/{r['n_b']} | "
            f"`{r['p_fisher']:.4f}` | `{r['p_fisher_holm']:.4f}` | `{r['p_barnard']:.4f}` | `{r['p_barnard_holm']:.4f}` |"
        )
    lines.append("")

    lines += [
        "---",
        "",
        "## Keterbatasan",
        "",
        "- Margin ekivalensi 0,01% seragam (D12 Opsi A) relatif longgar secara absolut untuk "
        "`interest_free`/`interest_djppr` (biaya absolut kecil, ~0,03-0,17) dibanding `gross_*` (~1,04) — "
        "lihat `docs/decisions/0012-practical-equivalence-margin-d12.md`.",
        "- \"Optimum LP layak\" bukan hasil solve LP sungguhan (`scipy.optimize.linprog`), melainkan "
        "diagnosis dari status kendala aktif dan jumlah bobot di batas kotak per run — pendekatan, "
        "bukan pembuktian formal bahwa kendala risiko benar-benar tidak berperan di titik optimum global.",
        "- Waktu 1-proses diukur dengan seed baru (bukan seed eksperimen utama) — perbandingan ke waktu "
        "6-worker bersifat indikatif (kontensi CPU berbeda), bukan replikasi run yang sama persis.",
        "",
    ]

    out_path = BASE_DIR / "docs" / "reviews" / "signifikansi_praktis.md"
    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Tersimpan: {out_path}")


def main() -> int:
    cfg = yaml.safe_load((BASE_DIR / "configs" / "params.yaml").read_text(encoding="utf-8"))

    df_main = task1_task2(cfg)
    df_timing = task3_timing(cfg)
    df_fisher = task4_fisher(cfg)

    out_dir = BASE_DIR / cfg["practical_significance"]["output_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    df_main.to_csv(out_dir / "stats_praktis.csv", index=False)
    df_fisher.to_csv(out_dir / "fisher_feasibility.csv", index=False)
    print(f"Tersimpan: {out_dir / 'stats_praktis.csv'} ({len(df_main)} baris)")
    print(f"Tersimpan: {out_dir / 'fisher_feasibility.csv'} ({len(df_fisher)} baris)")

    write_report(df_main, df_timing, df_fisher, cfg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
