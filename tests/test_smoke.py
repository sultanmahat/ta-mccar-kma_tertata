"""Smoke test untuk memastikan kerangka paket mccar_kma dapat diimpor."""

import importlib
import pytest


def test_import_package():
    """Uji impor modul utama mccar_kma."""
    import mccar_kma
    assert mccar_kma is not None
    assert hasattr(mccar_kma, "__version__")


@pytest.mark.parametrize(
    "submodule",
    [
        "mccar_kma.data",
        "mccar_kma.scenarios",
        "mccar_kma.risk",
        "mccar_kma.model",
        "mccar_kma.optimizers",
        "mccar_kma.experiments",
        "mccar_kma.analysis",
        "mccar_kma.viz",
        "mccar_kma.utils",
    ],
)
def test_import_submodules(submodule):
    """Uji impor seluruh subpaket kerangka."""
    mod = importlib.import_module(submodule)
    assert mod is not None
