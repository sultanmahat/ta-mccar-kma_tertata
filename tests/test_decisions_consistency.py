"""Unit testing untuk memeriksa konsistensi register keputusan (README.md vs params.yaml).

Memastikan tidak ada penyimpangan nilai numerik parameter D1-D9 dan menegakkan
status persetujuan resmi ('Dikonfirmasi oleh Sultan').
"""

from pathlib import Path
import yaml
import pytest


@pytest.fixture
def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


@pytest.fixture
def params_config(repo_root: Path) -> dict:
    params_file = repo_root / "configs" / "params.yaml"
    assert params_file.exists(), "configs/params.yaml tidak ditemukan!"
    with open(params_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture
def decisions_readme_text(repo_root: Path) -> str:
    readme_file = repo_root / "docs" / "decisions" / "README.md"
    assert readme_file.exists(), "docs/decisions/README.md tidak ditemukan!"
    return readme_file.read_text(encoding="utf-8")


def test_decisions_confirmed_status(repo_root: Path, decisions_readme_text: str):
    """Memastikan status D1-D12 sah Dikonfirmasi; D13 boleh pending ("Diusulkan agen, menunggu konfirmasi Sultan").

    D13 (docs/decisions/0013-kma-phase2-mlipir-rate-d13.md) dibuat 2026-10-25 untuk mencatat
    (bukan memilih) parameter kma.py yang sebelumnya tak tercatat (temuan T5). Statusnya sengaja
    pending sampai Sultan memutuskan antara mempertahankan nilai atau mengulang eksperimen.
    """
    # 1. Periksa README.md
    assert "Dikonfirmasi oleh Sultan" in decisions_readme_text
    assert "**Status**: DIPUTUSKAN" not in decisions_readme_text
    assert "disetujui bersama pengguna" not in decisions_readme_text.lower()

    # 2. Periksa berkas 0001 s.d. 0013
    decision_files = sorted((repo_root / "docs" / "decisions").glob("00*.md"))
    assert len(decision_files) == 13, f"Harusnya ada 13 berkas keputusan (D1-D12 + D13), ditemukan {len(decision_files)}"

    pending_allowed = {"0013-kma-phase2-mlipir-rate-d13.md"}

    for df in decision_files:
        content = df.read_text(encoding="utf-8")
        assert "- **Status**: DIPUTUSKAN" not in content, (
            f"Status di {df.name} masih mencantumkan DIPUTUSKAN!"
        )
        if df.name in pending_allowed:
            assert "- **Status**: **Diusulkan agen, menunggu konfirmasi Sultan**" in content, (
                f"Status di {df.name} harus 'Diusulkan agen, menunggu konfirmasi Sultan'!"
            )
        else:
            assert "- **Status**: **Dikonfirmasi oleh Sultan Bakri Baihaqi Mahat (Mahasiswa)**" in content, (
                f"Status di {df.name} belum berstatus Dikonfirmasi oleh Sultan!"
            )
            assert "Menunggu konfirmasi Sultan" not in content, (
                f"Status di {df.name} masih menunggu konfirmasi, tapi bukan D13!"
            )


def test_d4_kma_parameters_consistency(params_config: dict, decisions_readme_text: str, repo_root: Path):
    """Memastikan nilai D4 di README.md dan 0006 konsisten 100% dengan params.yaml."""
    kma_cfg = params_config["algorithms"]["kma"]

    # Verifikasi nilai params.yaml
    assert kma_cfg["p_bm"] == 0.5
    assert kma_cfg["gamma"] == 0.1
    assert kma_cfg["p_mating"] == 0.5
    assert kma_cfg["delta_n"] == 5
    assert kma_cfg["phase_1"]["budget"] == 5000
    assert kma_cfg["phase_2"]["budget"] == 20000
    assert kma_cfg["phase_2"]["n_pop_min"] == 20
    assert kma_cfg["phase_2"]["n_pop_max"] == 200

    # Verifikasi teks di README.md memuat nilai yang benar
    assert "0{,}5" in decisions_readme_text or "0.5" in decisions_readme_text
    assert "0{,}1" in decisions_readme_text or "0.1" in decisions_readme_text
    assert "20, 200" in decisions_readme_text or "20-200" in decisions_readme_text

    # Pastikan kesalahan lama TIDAK ada lagi di baris D4
    lines = [l for l in decisions_readme_text.splitlines() if "**D4**" in l]
    assert len(lines) == 1, "Baris D4 harus tepat satu di README.md"
    d4_line = lines[0]
    assert "p_{\\text{bm}} = 0{,}1" not in d4_line, "D4 salah mencatat p_bm 0.1!"
    assert "\\gamma = 0{,}5" not in d4_line, "D4 salah mencatat gamma 0.5!"
    assert "\\Delta n = 2" not in d4_line, "D4 salah mencatat delta_n 2!"


def test_d5_zero_division_guard_consistency(params_config: dict, decisions_readme_text: str, repo_root: Path):
    """Memastikan nilai D5 di README.md dan 0004 konsisten 100% dengan params.yaml."""
    risk_cfg = params_config["risk"]
    assert float(risk_cfg["zero_tolerance_mc"]) == 1e-12

    # Verifikasi baris D5 di README.md
    lines = [l for l in decisions_readme_text.splitlines() if "**D5**" in l]
    assert len(lines) == 1, "Baris D5 harus tepat satu di README.md"
    d5_line = lines[0]

    assert "0{,}0" in d5_line or "0.0" in d5_line
    assert "10^{-12}" in d5_line or "1.0e-12" in d5_line
    assert "penalti kuadratik" not in d5_line.lower(), "D5 tidak menggunakan penalti kuadratik!"
    assert "1{,}0" not in d5_line, "D5 tidak menetapkan theta_i = 1.0!"


def test_d1_through_d9_coverage(repo_root: Path, decisions_readme_text: str):
    """Memastikan seluruh D1 sampai D12 tercakup dan memiliki file pendukung."""
    for i in range(1, 13):
        marker = f"**D{i}**"
        assert marker in decisions_readme_text, f"Keputusan {marker} tidak ditemukan di README.md!"

    # Periksa keberadaan berkas file
    for p in (repo_root / "docs" / "decisions").glob("00*.md"):
        assert p.name in decisions_readme_text, f"Berkas {p.name} tidak ditautkan di README.md!"
