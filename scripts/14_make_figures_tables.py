"""Skrip Tahap 14 — Pembuatan Seluruh Gambar Ilmiah dan Tabel LaTeX Skripsi.

Menghasilkan seluruh gambar publikasi (PDF vektor + PNG 300 dpi, label Bahasa Indonesia,
font serif, palet konsisten, dan ramah cetak hitam-putih) serta tabel LaTeX booktabs:
1. Kurva konvergensi (median + pita IQR 30 replikasi) per konfigurasi dan panel all.
2. Boxplot nilai objektif per algoritma di 4 konfigurasi.
3. Komposisi portofolio bertumpuk: eksisting vs DJPPR vs KMA/GA/PSO.
4. Profil rasio theta_i per instrumen untuk eksisting dan solusi terbaik.
5. Perbandingan waktu komputasi per algoritma.
6. Deret waktu data pasar historis 2017–2025 (yield dan kurs).
7. Tabel LaTeX: parameter eksperimen, statistik data pasar, batas risiko, ringkasan hasil.

Keluaran disimpan ke:
- results/figures/fig_<topik>[_<config_id>].pdf / .png
- results/tables/tab_<topik>[_<config_id>].tex
"""

from pathlib import Path
import argparse
import json
import time
import numpy as np
import pandas as pd
import yaml

from mccar_kma.viz.style import (
    apply_thesis_style,
    save_figure,
    ALGO_COLORS,
    INSTRUMENT_NAMES,
)
from mccar_kma.viz.figures import (
    plot_convergence_single,
    plot_convergence_grid_all,
    plot_objective_boxplots,
    plot_portfolio_composition_single,
    plot_portfolio_composition_all,
    plot_theta_ratios_single,
    plot_theta_ratios_all,
    plot_computation_times,
    plot_market_timeseries,
)


def generate_experiment_params_table(params_path: Path, output_tex: Path) -> Path:
    """Menghasilkan tabel LaTeX parameter eksperimen (Tabel 3.1 proposal)."""
    with open(params_path, "r", encoding="utf-8") as f:
        params = yaml.safe_load(f)

    scenarios = params.get("scenarios", {})
    tex_lines = [
        r"% ==============================================================================",
        r"% Tabel Parameter Desain Eksperimen (Tabel 3.1 Proposal)",
        r"% ==============================================================================",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Parameter Desain Eksperimen Optimasi Portofolio Utang Negara}",
        r"\label{tab:experiment_params}",
        r"\begin{tabular}{llp{7.5cm}}",
        r"\toprule",
        r"\textbf{Komponen Parameter} & \textbf{Nilai Parameter} & \textbf{Keterangan / Rujukan Metodologis} \\",
        r"\midrule",
        r"Jendela Data Historis & 2017-07-03 s.d. 2025-11-24 & 2.028 hari kerja lengkap (mode \texttt{intersection}) \\",
        r"Jumlah Skenario Latih ($N_{\text{train}}$) & 5.000 skenario & Simulasi terminal GBM horizon 1 tahun ($T=252$ hari) \\",
        r"Tingkat Kepercayaan Risiko ($\alpha$) & 95\% ($\alpha = 0{,}95$) & Skenario ekor $m = \lceil 0{,}05 \times 5.000 \rceil = 250$ skenario \\",
        r"Tambahan Proporsi Utang ($\delta$) & 0,01 (1\%) & Tambahan penerbitan untuk estimasi MCCaR (Pers. 2.14) \\",
        r"Anggaran Evaluasi Fungsi & 25.000 evaluasi & Anggaran evaluasi fungsi portofolio per replikasi \\",
        r"Jumlah Replikasi Independen & 30 replikasi & Seed generator acak identik untuk KMA, GA, dan PSO \\",
        r"Koefisien Penalti Kuadratik & $\rho_J = 10^6, \rho_R = 10^6$ & Penalti pelanggaran kendala $J \le \eta$ dan $\text{CCaR} \le \tau$ \\",
        r"Toleransi Numerik Kendala & $\epsilon_{\text{tol}} = 10^{-8}$ & Batas toleransi kelayakan bobot dan risiko \\",
        r"Bank Validasi Independen & 20.000 skenario & Seed 2026, ekor $m = 1.000$ skenario untuk validasi out-of-sample \\",
        r"Konfigurasi Evaluasi & 4 konfigurasi & Kombinasi \{gross, interest\} $\times$ \{free, djppr\} \\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]
    with open(output_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(tex_lines))
    return output_tex


def generate_market_stats_table(gbm_params_path: Path, market_csv_path: Path, output_tex: Path) -> Path:
    """Menghasilkan tabel LaTeX statistik deskriptif data pasar historis 2017–2025."""
    df_gbm = pd.read_csv(gbm_params_path)
    df_market = pd.read_csv(market_csv_path)

    var_display_names = {
        "IR_USD_5Y": "USD Fixed 5Y (Yield)",
        "IR_USD_10Y": "USD Fixed 10Y (Yield)",
        "IR_USD_30Y": "USD Fixed 30Y (Yield)",
        "IR_EUR_7Y": "EUR Fixed 7Y (Yield)",
        "IR_EUR_10Y": "EUR Fixed 10Y (Yield)",
        "IR_JPY_5Y": "JPY Fixed 5Y (Yield)",
        "IR_JPY_10Y": "JPY Fixed 10Y (Yield)",
        "FX_USD/EUR": "Kurs FX USD/EUR (EUR/USD)",
        "FX_USD/JPY": "Kurs FX USD/JPY (JPY/USD)",
    }

    tex_lines = [
        r"% ==============================================================================",
        r"% Tabel Statistik Deskriptif dan Parameter GBM Data Pasar Historis 2017-2025",
        r"% ==============================================================================",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Statistik Deskriptif dan Parameter Geometric Brownian Motion (GBM) Data Historis 2017--2025}",
        r"\label{tab:market_stats}",
        r"\small",
        r"\begin{tabular}{lcccccc}",
        r"\toprule",
        r"\textbf{Variabel Keuangan} & \textbf{Awal ($S_0$)} & \textbf{Rerata} & \textbf{Min} & \textbf{Maks} & \textbf{Drift ($\mu$ p.a.)} & \textbf{Volatilitas ($\sigma$ p.a.)} \\",
        r"\midrule",
    ]

    for _, row in df_gbm.iterrows():
        var_name = row["variable"]
        disp_name = var_display_names.get(var_name, var_name)
        s_series = df_market[var_name]
        s0 = s_series.iloc[0]
        mean_s = s_series.mean()
        min_s = s_series.min()
        max_s = s_series.max()
        mu_ann = row["mu_annual"]
        sig_ann = row["sigma_annual"]

        fmt_s = ".3f" if "FX" in var_name or "EUR" in var_name else ".3f"
        tex_lines.append(
            f"{disp_name} & {s0:{fmt_s}} & {mean_s:{fmt_s}} & {min_s:{fmt_s}} & {max_s:{fmt_s}} & "
            f"{mu_ann:+.4f} & {sig_ann:.4f} \\\\"
        )

    tex_lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ])

    with open(output_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(tex_lines))
    return output_tex


def generate_risk_limits_table(limits_json_path: Path, output_tex: Path) -> Path:
    """Menghasilkan tabel LaTeX ambang batas risiko acuan tau dan eta."""
    with open(limits_json_path, "r", encoding="utf-8") as f:
        limits = json.load(f)

    tex_lines = [
        r"% ==============================================================================",
        r"% Tabel Ambang Batas Acuan Risiko Portofolio Eksisting w0 (Pers. 2.22)",
        r"% ==============================================================================",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Nilai Acuan Ambang Batas Risiko Portofolio Eksisting 2024 ($w_0$) pada Bank Latih $N=5.000$}",
        r"\label{tab:risk_limits}",
        r"\begin{tabular}{lcccc}",
        r"\toprule",
        r"\textbf{Definisi Biaya} & \textbf{Biaya Awal ($\text{Cost}(w_0)$)} & \textbf{Batas Ekor ($\tau = \text{CCaR}_{0{,}95}$)} & \textbf{Batas Dispersi ($\eta = J_{\text{MCCaR}}$)} & \textbf{Rerata Rasio ($\bar{\theta}$)} \\",
        r"\midrule",
        f"Biaya Bruto (\\textit{{Gross Cost}}) & {limits['gross']['mean_cost']:.6f} & {limits['gross']['tau']:.6f} & {limits['gross']['eta']:.6f} & {limits['gross']['theta_bar']:.4f} \\\\",
        f"Biaya Bunga (\\textit{{Interest Cost}}) & {limits['interest']['mean_cost']:.6f} & {limits['interest']['tau']:.6f} & {limits['interest']['eta']:.6f} & {limits['interest']['theta_bar']:.4f} \\\\",
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ]

    with open(output_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(tex_lines))
    return output_tex


def generate_results_summary_table(val_summary_csv: Path, output_tex: Path) -> Path:
    """Menghasilkan tabel LaTeX ringkasan performa optimasi dan penghematan biaya."""
    df_val = pd.read_csv(val_summary_csv)
    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    tex_lines = [
        r"% ==============================================================================",
        r"% Tabel Ringkasan Komparasi Solusi Optimal dan Penghematan Relatif",
        r"% ==============================================================================",
        r"\begin{table}[htbp]",
        r"\centering",
        r"\caption{Ringkasan Perbandingan Performa Solusi Portofolio Optimal pada Bank Validasi ($N=20.000$)}",
        r"\label{tab:results_summary}",
        r"\small",
        r"\begin{tabular}{llcccccc}",
        r"\toprule",
        r"\textbf{Konfigurasi} & \textbf{Metode / Solusi} & \textbf{Biaya ($Cost$)} & \textbf{CCaR (0,95)} & \textbf{J (MCCaR)} & \textbf{Layak (\%)} & \textbf{$\Delta$ vs $w_0$ (\%)} & \textbf{$\Delta$ vs Base (\%)} \\",
        r"\midrule",
    ]

    for cid in config_ids:
        sub = df_val[df_val["config_id"] == cid]
        is_djppr = cid.endswith("djppr")

        # Rujukan Eksisting & Baseline
        if cid.startswith("gross"):
            w0_c = 1.042186
            base_c = 1.042709 if is_djppr else None
        else:
            w0_c = 0.044369
            base_c = 0.044148 if is_djppr else None

        tex_lines.append(f"\\multirow{{4}}{{*}}{{\\texttt{{{cid}}}}} & Eksisting 2024 ($w_0$) & {w0_c:.6f} & -- & -- & 100{{,}}0\\% & +0{{,}}000\\% & -- \\\\")

        for algo in ["kma", "ga", "pso"]:
            asub = sub[sub["algo"] == algo]
            feas_sub = asub[asub["val_is_feasible"] == True]
            ref_sub = feas_sub if len(feas_sub) > 0 else asub
            best_row = ref_sub.loc[ref_sub["val_cost"].idxmin()]

            c = best_row["val_cost"]
            cc = best_row["val_ccar"]
            j = best_row["val_j_mccar"]
            feas_pct = (len(feas_sub) / len(asub)) * 100.0
            h_w0 = ((w0_c - c) / w0_c) * 100.0
            h_base = f"{((base_c - c) / base_c) * 100.0:+.3f}\\%" if base_c is not None else "--"

            tex_lines.append(
                f" & {algo.upper()} (Best) & {c:.6f} & {cc:.6f} & {j:.6f} & {feas_pct:.1f}\\% & "
                f"{h_w0:+.3f}\\% & {h_base} \\\\"
            )
        tex_lines.append(r"\midrule")

    # Ganti midrule terakhir dengan bottomrule
    tex_lines[-1] = r"\bottomrule"
    tex_lines.extend([
        r"\end{tabular}",
        r"\end{table}",
    ])

    with open(output_tex, "w", encoding="utf-8") as f:
        f.write("\n".join(tex_lines))
    return output_tex


def main() -> None:
    parser = argparse.ArgumentParser(description="Pembangkit seluruh gambar ilmiah dan tabel LaTeX tugas akhir (Tahap 14).")
    parser.add_argument("--runs-summary", type=str, default="results/tables/runs_summary.csv")
    parser.add_argument("--validation-all", type=str, default="results/tables/validation_all_runs.csv")
    parser.add_argument("--runs-dir", type=str, default="results/runs")
    parser.add_argument("--params", type=str, default="configs/params.yaml")
    parser.add_argument("--limits", type=str, default="data/processed/risk_limits_bank_train_seed42_N5000.json")
    parser.add_argument("--market-csv", type=str, default="data/processed/market_2017-07-03_2025-11-24_intersection.csv")
    parser.add_argument("--gbm-params", type=str, default="data/processed/gbm_params_intersection.csv")
    parser.add_argument("--figures-dir", type=str, default="results/figures")
    parser.add_argument("--tables-dir", type=str, default="results/tables")
    args = parser.parse_args()

    fig_dir = Path(args.figures_dir)
    fig_dir.mkdir(parents=True, exist_ok=True)
    tab_dir = Path(args.tables_dir)
    tab_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 78)
    print("TAHAP 14 — PEMBUATAN GAMBAR ILMIAH DAN TABEL LATEX SKRIPSI")
    print("=" * 78)
    print(f"Direktori Gambar: {fig_dir}")
    print(f"Direktori Tabel : {tab_dir}")
    print("-" * 78)

    t0 = time.perf_counter()

    # Memuat berkas pendukung
    df_runs = pd.read_csv(args.runs_summary)
    df_val = pd.read_csv(args.validation_all)
    with open(args.limits, "r", encoding="utf-8") as f:
        limits = json.load(f)

    config_ids = ["gross_free", "gross_djppr", "interest_free", "interest_djppr"]

    # ==========================================================================
    # 1. Pembangkitan Kurva Konvergensi (Topik 1)
    # ==========================================================================
    print("\n[1/6] Menggambar Kurva Konvergensi...")
    w0_costs = {
        "gross_free": float(limits["gross"]["mean_cost"]),
        "gross_djppr": float(limits["gross"]["mean_cost"]),
        "interest_free": float(limits["interest"]["mean_cost"]),
        "interest_djppr": float(limits["interest"]["mean_cost"]),
    }
    base_costs = {
        "gross_free": None,
        "gross_djppr": 1.042709,
        "interest_free": None,
        "interest_djppr": 0.044148,
    }

    for cid in config_ids:
        out_f = fig_dir / f"fig_convergence_{cid}"
        p_pdf, p_png = plot_convergence_single(
            runs_dir=args.runs_dir,
            config_id=cid,
            output_path=out_f,
            w0_cost=w0_costs[cid],
            baseline_cost=base_costs[cid],
        )
        print(f"      -> Tersimpan: {p_pdf.name} & {p_png.name}")

    out_all_conv = fig_dir / "fig_convergence_all"
    p_pdf, p_png = plot_convergence_grid_all(args.runs_dir, args.limits, out_all_conv)
    print(f"      -> Panel Gabungan: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 2. Pembangkitan Boxplot Nilai Objektif (Topik 2)
    # ==========================================================================
    print("\n[2/6] Menggambar Boxplot Nilai Objektif...")
    out_bp = fig_dir / "fig_boxplot_cost"
    p_pdf, p_png = plot_objective_boxplots(df_runs, out_bp)
    print(f"      -> Panel Boxplot: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 3. Pembangkitan Komposisi Portofolio (Topik 3)
    # ==========================================================================
    print("\n[3/6] Menggambar Komposisi Portofolio (Batang Bertumpuk 7 Instrumen)...")
    w0_weights_gross = np.array(limits["gross"]["w0"], dtype=float)
    w0_weights_interest = np.array(limits["interest"]["w0"], dtype=float)

    all_compositions = {}
    for cid in config_ids:
        sub = df_val[df_val["config_id"] == cid]
        is_djppr = cid.endswith("djppr")
        cost_def = "gross" if cid.startswith("gross") else "interest"
        w0_w = w0_weights_gross if cost_def == "gross" else w0_weights_interest

        comp_dict = {"Eksisting 2024": w0_w}

        # Baseline DJPPR (jika ada)
        if is_djppr:
            base_csv = Path("results/tables") / f"baseline_djppr_{cost_def}.csv"
            if base_csv.exists():
                df_base = pd.read_csv(base_csv)
                feas_base = df_base[df_base["is_feasible"] == True]
                if len(feas_base) > 0:
                    best_base_idx = feas_base["mean_cost"].idxmin()
                    w_cols_base = [c for c in df_base.columns if c.startswith("w_")]
                    comp_dict["Baseline DJPPR"] = feas_base.loc[best_base_idx, w_cols_base].values.astype(float)

        for algo in ["kma", "ga", "pso"]:
            asub = sub[sub["algo"] == algo]
            feas_sub = asub[asub["val_is_feasible"] == True]
            ref_sub = feas_sub if len(feas_sub) > 0 else asub
            best_row = ref_sub.loc[ref_sub["val_cost"].idxmin()]
            w_cols = [f"w_{i}" for i in range(1, 8)]
            comp_dict[f"{algo.upper()} Best"] = best_row[w_cols].values.astype(float)

        all_compositions[cid] = comp_dict

        out_comp = fig_dir / f"fig_composition_{cid}"
        p_pdf, p_png = plot_portfolio_composition_single(comp_dict, cid, out_comp)
        print(f"      -> Tersimpan: {p_pdf.name} & {p_png.name}")

    out_all_comp = fig_dir / "fig_composition_all"
    p_pdf, p_png = plot_portfolio_composition_all(all_compositions, out_all_comp)
    print(f"      -> Panel Gabungan Komposisi: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 4. Pembangkitan Profil Rasio theta_i (Topik 4)
    # ==========================================================================
    print("\n[4/6] Menggambar Profil Rasio theta_i...")
    all_thetas = {}
    all_theta_bars = {}

    runs_path = Path(args.runs_dir)

    for cid in config_ids:
        sub = df_val[df_val["config_id"] == cid]
        is_djppr = cid.endswith("djppr")
        cost_def = "gross" if cid.startswith("gross") else "interest"

        th_dict = {"Eksisting 2024": np.array(limits[cost_def]["theta"], dtype=float)}
        th_bar_dict = {"Eksisting 2024": float(limits[cost_def]["theta_bar"])}

        # Baseline DJPPR (jika ada)
        if is_djppr:
            base_csv = Path("results/tables") / f"baseline_djppr_{cost_def}.csv"
            if base_csv.exists():
                df_base = pd.read_csv(base_csv)
                feas_base = df_base[df_base["is_feasible"] == True]
                if len(feas_base) > 0:
                    best_base_idx = feas_base["mean_cost"].idxmin()
                    th_cols = [c for c in df_base.columns if c.startswith("theta_") and c != "theta_bar"]
                    th_dict["Baseline DJPPR"] = feas_base.loc[best_base_idx, th_cols].values.astype(float)
                    th_bar_dict["Baseline DJPPR"] = float(feas_base.loc[best_base_idx, "theta_bar"])

        for algo in ["kma", "ga", "pso"]:
            asub = sub[sub["algo"] == algo]
            feas_sub = asub[asub["val_is_feasible"] == True]
            ref_sub = feas_sub if len(feas_sub) > 0 else asub
            best_row = ref_sub.loc[ref_sub["val_cost"].idxmin()]
            rep = int(best_row["rep"])
            seed = int(best_row["seed"])

            json_file = runs_path / cid / algo / f"rep_{rep:02d}_seed{seed}.json"
            if json_file.exists():
                with open(json_file, "r", encoding="utf-8") as jf:
                    jdata = json.load(jf)
                th_dict[f"{algo.upper()} Best"] = np.array(jdata["theta_i"], dtype=float)
                th_bar_dict[f"{algo.upper()} Best"] = float(np.mean(jdata["theta_i"]))

        all_thetas[cid] = th_dict
        all_theta_bars[cid] = th_bar_dict

        out_th = fig_dir / f"fig_theta_ratio_{cid}"
        p_pdf, p_png = plot_theta_ratios_single(th_dict, th_bar_dict, cid, out_th)
        print(f"      -> Tersimpan: {p_pdf.name} & {p_png.name}")

    out_all_th = fig_dir / "fig_theta_ratio_all"
    p_pdf, p_png = plot_theta_ratios_all(all_thetas, all_theta_bars, out_all_th)
    print(f"      -> Panel Gabungan Rasio theta: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 5. Pembangkitan Waktu Komputasi (Topik 5)
    # ==========================================================================
    print("\n[5/6] Menggambar Waktu Komputasi...")
    out_time = fig_dir / "fig_computation_time"
    p_pdf, p_png = plot_computation_times(df_runs, out_time)
    print(f"      -> Waktu Komputasi: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 6. Pembangkitan Deret Waktu Pasar (Topik 6)
    # ==========================================================================
    print("\n[6/6] Menggambar Deret Waktu Pasar 2017–2025...")
    out_mkt = fig_dir / "fig_timeseries_market"
    p_pdf, p_png = plot_market_timeseries(args.market_csv, out_mkt)
    print(f"      -> Deret Waktu Pasar: {p_pdf.name} & {p_png.name}")

    # ==========================================================================
    # 7. Pembangkitan Tabel-Tabel LaTeX (booktabs)
    # ==========================================================================
    print("\n[+] Menyusun Tabel-tabel LaTeX (booktabs)...")
    p1 = generate_experiment_params_table(Path(args.params), tab_dir / "tab_experiment_params.tex")
    print(f"    -> Tabel Parameter Eksperimen : {p1.name}")

    p2 = generate_market_stats_table(Path(args.gbm_params), Path(args.market_csv), tab_dir / "tab_market_stats.tex")
    print(f"    -> Tabel Statistik Pasar & GBM: {p2.name}")

    p3 = generate_risk_limits_table(Path(args.limits), tab_dir / "tab_risk_limits.tex")
    print(f"    -> Tabel Ambang Batas Risiko  : {p3.name}")

    p4 = generate_results_summary_table(Path(args.validation_all), tab_dir / "tab_results_summary.tex")
    print(f"    -> Tabel Ringkasan Hasil      : {p4.name}")

    elapsed = time.perf_counter() - t0
    print("-" * 78)
    print(f"SELURUH GAMBAR DAN TABEL BERHASIL DIBUAT dalam {elapsed:.2f} detik.")
    print("=" * 78)


if __name__ == "__main__":
    main()
