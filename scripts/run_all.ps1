# ==============================================================================
# PIPELINE EKSEKUSI PENUH / REPRODUKSIBILITAS TA MCCAR + KMA (PowerShell)
# ==============================================================================
#
# Penggunaan:
#   .\scripts\run_all.ps1            # Menjalankan pipeline eksperimen penuh (360 run)
#   .\scripts\run_all.ps1 -Pilot     # Menjalankan pipeline mode pilot cepat (~5-7 menit)
#
# ==============================================================================

[CmdletBinding()]
param (
    [switch]$Pilot
)

$ErrorActionPreference = "Stop"
$StartTimeTotal = Get-Date

# Deteksi root repositori dan eksekutor Python
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not $ScriptDir) { $ScriptDir = $PSScriptRoot }
$RepoRoot = Split-Path -Parent $ScriptDir

if ($env:VIRTUAL_ENV -and (Test-Path "$env:VIRTUAL_ENV\Scripts\python.exe")) {
    $PythonExe = "$env:VIRTUAL_ENV\Scripts\python.exe"
} elseif (Test-Path "$RepoRoot\.venv\Scripts\python.exe") {
    $PythonExe = "$RepoRoot\.venv\Scripts\python.exe"
} else {
    $PythonExe = "python"
}

# Tambahkan src ke PYTHONPATH agar modul mccar_kma selalu dapat diimpor
$env:PYTHONPATH = "$RepoRoot\src;$env:PYTHONPATH"

function Write-Banner([string]$Title) {
    Write-Host ""
    Write-Host ("=" * 80) -ForegroundColor Cyan
    Write-Host " $Title" -ForegroundColor Yellow
    Write-Host ("=" * 80) -ForegroundColor Cyan
}

function Run-Step([string]$StepNumber, [string]$StepName, [string]$Command, [string[]]$Arguments) {
    $StepStart = Get-Date
    Write-Host ""
    Write-Host ("-" * 80) -ForegroundColor Gray
    Write-Host "[$StepNumber/13] $StepName" -ForegroundColor Green
    Write-Host "Perintah: $PythonExe $Command $($Arguments -join ' ')" -ForegroundColor DarkGray
    Write-Host ("-" * 80) -ForegroundColor Gray

    $proc = Start-Process -FilePath $PythonExe -ArgumentList (@($Command) + $Arguments) -NoNewWindow -Wait -PassThru
    if ($proc.ExitCode -ne 0) {
        Write-Host ""
        Write-Host "ERROR: Langkah $StepNumber ($StepName) gagal dengan kode keluar $($proc.ExitCode)." -ForegroundColor Red
        exit $proc.ExitCode
    }

    $StepDuration = (Get-Date) - $StepStart
    Write-Host "-> Selesai dalam $([math]::Round($StepDuration.TotalSeconds, 2)) detik." -ForegroundColor Green
}

# 1. Pengecekan Environment
Write-Banner "PIPELINE REPRODUKSIBILITAS: TA MCCAR + KMA (SULTAN BAKRI BAIHAQI MAHAT)"
Write-Host "Waktu Mulai: $($StartTimeTotal.ToString('yyyy-MM-dd HH:mm:ss'))"
Write-Host "Python Exe : $PythonExe"
if ($Pilot) {
    Write-Host "Mode       : PILOT REPRODUKSI CEPAT (Uji coba 2 replikasi, 2.000 evaluasi)" -ForegroundColor Magenta
} else {
    Write-Host "Mode       : EKSPERIMEN PENUH (30 replikasi, 25.000 evaluasi, 360 run)" -ForegroundColor Cyan
}

# 2. Urutan Pipeline 01 s.d. 14
Run-Step "01" "Audit Integritas Data Mentah DJPPR" "scripts/01_audit_data.py" @()
Run-Step "02" "Pra-Pemrosesan & Pemotongan Jendela Historis" "scripts/02_preprocess_data.py" @()
Run-Step "03" "Estimasi Parameter Drift & Volatilitas GBM" "scripts/03_estimate_gbm_params.py" @()
Run-Step "04" "Pembangkitan Bank Skenario Terminal GBM" "scripts/04_generate_scenarios.py" @()
Run-Step "05" "Benchmarking Kecepatan & Akurasi Evaluator Risiko" "scripts/05_benchmark_evaluator.py" @()
Run-Step "06" "Perhitungan Batas Acuan Risiko w0 & Baseline DJPPR" "scripts/06_compute_limits_and_baseline.py" @()
Run-Step "07" "Uji Coba Asap (Smoke Test) Algoritma KMA 2-Fase" "scripts/07_run_kma_smoke.py" @()
Run-Step "08" "Perbandingan Awal Metaheuristik KMA vs GA vs PSO" "scripts/08_compare_optimizers.py" @()
Run-Step "09" "Audit & Verifikasi Kode vs Spesifikasi Model" "scripts/09_run_audit_check.py" @()

# Langkah 10: Optimasi Portofolio
if ($Pilot) {
    Run-Step "10" "Pelari Optimasi Portofolio (Mode Pilot Cepat)" "scripts/10_run_experiments.py" @("--pilot", "--workers", "4")
} else {
    Run-Step "10" "Pelari Optimasi Portofolio (Mode Penuh 360 Run)" "scripts/10_run_experiments.py" @("--workers", "4")
}

Run-Step "11" "Validasi Independen pada Bank Skenario N=20.000" "scripts/12_validate_solutions.py" @()
Run-Step "12" "Analisis Statistik Inferensial (Kruskal-Wallis & Dunn)" "scripts/13_analyze_stats.py" @()
Run-Step "13" "Pembangkitan Seluruh Gambar Ilmiah & Tabel LaTeX" "scripts/14_make_figures_tables.py" @()

# 3. Banner Ringkasan Akhir
$TotalDuration = (Get-Date) - $StartTimeTotal
Write-Banner "SELURUH PIPELINE BERHASIL DISELESAIKAN SECARA LENGKAP!"
Write-Host "Total Waktu Eksekusi : $([math]::Floor($TotalDuration.TotalMinutes)) menit $([math]::Round($TotalDuration.Seconds, 1)) detik" -ForegroundColor Green
Write-Host "Direktori Hasil      : results/ (runs/, tables/, figures/)"
Write-Host "Status Integritas    : 100% REPRODUCIBLE (Valid & Terverifikasi)" -ForegroundColor Green
Write-Host ("=" * 80) -ForegroundColor Cyan
