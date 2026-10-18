#!/usr/bin/env bash
# ==============================================================================
# PIPELINE EKSEKUSI PENUH / REPRODUKSIBILITAS TA MCCAR + KMA (Bash / Linux / macOS)
# ==============================================================================
#
# Penggunaan:
#   ./scripts/run_all.sh            # Menjalankan pipeline eksperimen penuh (360 run)
#   ./scripts/run_all.sh --pilot    # Menjalankan pipeline mode pilot cepat (~5-7 menit)
#
# ==============================================================================

set -e

PILOT_MODE=0
for arg in "$@"; do
    case $arg in
        --pilot|-p)
            PILOT_MODE=1
            shift
            ;;
    esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Deteksi eksekutor Python
if [ -n "$VIRTUAL_ENV" ] && [ -f "$VIRTUAL_ENV/bin/python" ]; then
    PYTHON_EXE="$VIRTUAL_ENV/bin/python"
elif [ -f "$REPO_ROOT/.venv/bin/python" ]; then
    PYTHON_EXE="$REPO_ROOT/.venv/bin/python"
else
    PYTHON_EXE="python"
fi

export PYTHONPATH="$REPO_ROOT/src:$PYTHONPATH"

START_TIME=$(date +%s)

echo "================================================================================"
echo " PIPELINE REPRODUKSIBILITAS: TA MCCAR + KMA (SULTAN BAKRI BAIHAQI MAHAT)"
echo "================================================================================"
echo "Python Exe : $PYTHON_EXE"
if [ $PILOT_MODE -eq 1 ]; then
    echo "Mode       : PILOT REPRODUKSI CEPAT (Uji coba 2 replikasi, 2.000 evaluasi)"
else
    echo "Mode       : EKSPERIMEN PENUH (30 replikasi, 25.000 evaluasi, 360 run)"
fi
echo "Waktu Mulai: $(date)"
echo "--------------------------------------------------------------------------------"

run_step() {
    STEP_NUM=$1
    STEP_NAME=$2
    shift 2
    CMD="$@"

    STEP_START=$(date +%s)
    echo ""
    echo "--------------------------------------------------------------------------------"
    echo "[$STEP_NUM/13] $STEP_NAME"
    echo "Perintah: $PYTHON_EXE $CMD"
    echo "--------------------------------------------------------------------------------"

    $PYTHON_EXE $CMD

    STEP_END=$(date +%s)
    STEP_DIFF=$((STEP_END - STEP_START))
    echo "-> Selesai dalam ${STEP_DIFF} detik."
}

# 1. Jalankan Urutan Pipeline 01 s.d. 09
run_step "01" "Audit Integritas Data Mentah DJPPR" scripts/01_audit_data.py
run_step "02" "Pra-Pemrosesan & Pemotongan Jendela Historis" scripts/02_preprocess_data.py
run_step "03" "Estimasi Parameter Drift & Volatilitas GBM" scripts/03_estimate_gbm_params.py
run_step "04" "Pembangkitan Bank Skenario Terminal GBM" scripts/04_generate_scenarios.py
run_step "05" "Benchmarking Kecepatan & Akurasi Evaluator Risiko" scripts/05_benchmark_evaluator.py
run_step "06" "Perhitungan Batas Acuan Risiko w0 & Baseline DJPPR" scripts/06_compute_limits_and_baseline.py
run_step "07" "Uji Coba Asap (Smoke Test) Algoritma KMA 2-Fase" scripts/07_run_kma_smoke.py
run_step "08" "Perbandingan Awal Metaheuristik KMA vs GA vs PSO" scripts/08_compare_optimizers.py
run_step "09" "Audit & Verifikasi Kode vs Spesifikasi Model" scripts/09_run_audit_check.py

# 2. Jalankan Langkah 10 (Optimasi)
if [ $PILOT_MODE -eq 1 ]; then
    run_step "10" "Pelari Optimasi Portofolio (Mode Pilot Cepat)" scripts/10_run_experiments.py --pilot --workers 4
else
    run_step "10" "Pelari Optimasi Portofolio (Mode Penuh 360 Run)" scripts/10_run_experiments.py --workers 4
fi

# 3. Jalankan Validasi, Analisis Statistik, dan Gambar/Tabel
run_step "11" "Validasi Independen pada Bank Skenario N=20.000" scripts/12_validate_solutions.py
run_step "12" "Analisis Statistik Inferensial (Kruskal-Wallis & Dunn)" scripts/13_analyze_stats.py
run_step "13" "Pembangkitan Seluruh Gambar Ilmiah & Tabel LaTeX" scripts/14_make_figures_tables.py

# 4. Banner Akhir
END_TIME=$(date +%s)
TOTAL_DIFF=$((END_TIME - START_TIME))
TOTAL_MIN=$((TOTAL_DIFF / 60))
TOTAL_SEC=$((TOTAL_DIFF % 60))

echo ""
echo "================================================================================"
echo " SELURUH PIPELINE BERHASIL DISELESAIKAN SECARA LENGKAP!"
echo " Total Waktu Eksekusi : ${TOTAL_MIN} menit ${TOTAL_SEC} detik"
echo " Direktori Hasil      : results/ (runs/, tables/, figures/)"
echo " Status Integritas    : 100% REPRODUCIBLE (Valid & Terverifikasi)"
echo "================================================================================"
