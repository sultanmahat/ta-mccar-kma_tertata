"""Tes tabel turunan naskah (Tahap 22): perubahan bobot vs w0 dan contoh skenario (Pers. 2.1-2.3)."""

import numpy as np
import pandas as pd
import pytest

from mccar_kma.analysis.thesis_tables import (
    WEIGHT_COLUMNS,
    representative_runs,
    scenario_example,
    weight_change_vs_w0,
)

NAMES = [f"I{i}" for i in range(1, 8)]
W0 = np.full(7, 1.0 / 7.0)


def _runs(costs):
    rows = []
    for rep, c in enumerate(costs, start=1):
        w = np.zeros(7)
        w[rep % 7] = 1.0
        rows.append({"config_id": "gross_free", "algo": "kma", "rep": rep, "best_cost": c,
                     **dict(zip(WEIGHT_COLUMNS, w))})
    return pd.DataFrame(rows)


def test_representative_runs_pick_best_and_lower_median():
    g = _runs([3.0, 1.0, 2.0, 4.0])
    reps = representative_runs(g)
    assert int(reps["best"]["rep"]) == 2
    assert float(reps["median"]["best_cost"]) == 2.0  # median bawah dari {1,2,3,4}


def test_weight_change_sums_to_zero_and_matches_definition():
    df = weight_change_vs_w0(_runs([3.0, 1.0, 2.0]), W0, NAMES, ["gross_free"], ["kma"])
    assert set(df["kind"]) == {"best", "median", "mean30"}
    for _, g in df.groupby("kind"):
        assert len(g) == 7
        # sum(w) = sum(w0) = 1 -> jumlah selisih bobot nol
        assert g["delta"].sum() == pytest.approx(0.0, abs=1e-12)
        assert np.allclose(g["delta"], g["w"] - g["w0"])
    best = df[df["kind"] == "best"]
    assert int(best["rep"].iloc[0]) == 2 and best["cost_train"].iloc[0] == 1.0


def test_missing_group_raises():
    with pytest.raises(ValueError):
        weight_change_vs_w0(_runs([1.0]), W0, NAMES, ["gross_free"], ["ga"])


def _toy_bank():
    var = np.array(["IR_USD_5Y", "IR_USD_10Y", "IR_USD_30Y", "IR_EUR_7Y", "IR_EUR_10Y",
                    "IR_JPY_5Y", "IR_JPY_10Y", "FX_USD/EUR", "FX_USD/JPY"])
    s0 = np.array([4.0, 4.5, 5.0, 3.0, 3.5, 1.0, 1.5, 0.9, 150.0])
    market = np.array([[5.0, 4.0, 5.0, 3.0, 3.0, 2.0, 1.0, 0.9, 150.0],
                       [4.0, 4.0, 4.0, 2.0, 2.0, 1.0, 1.0, 1.8, 75.0]])
    q = np.column_stack([np.ones(2), 0.9 / market[:, 7], 150.0 / market[:, 8]])
    curr = [0, 0, 0, 1, 1, 2, 2]
    y = market[:, :7]
    gross = q[:, curr] * (1.0 + y / 100.0)
    interest = q[:, curr] * (y / 100.0)
    return {"variable_names": var, "s0": s0, "scenarios_market": market, "q_factors": q,
            "cost_gross": gross, "cost_interest": interest,
            "instrument_names": np.array(["USD_Fixed_5Y", "USD_Fixed_10Y", "USD_Fixed_30Y",
                                          "EUR_Fixed_7Y", "EUR_Fixed_10Y", "JPY_Fixed_5Y",
                                          "JPY_Fixed_10Y"]),
            "currency_names": np.array(["USD", "EUR", "JPY"])}


def test_scenario_example_reproduces_equations_2_1_to_2_3():
    df = scenario_example(_toy_bank(), 2)
    s2 = df[df["scenario"] == 2].set_index(["kind", "name"])["value"]
    # Kurs USD/EUR naik 2x -> q_EUR = 0,5; kurs USD/JPY turun separuh -> q_JPY = 2 (Pers. 2.1)
    assert s2[("q", "EUR")] == pytest.approx(0.5)
    assert s2[("q", "JPY")] == pytest.approx(2.0)
    assert s2[("cost_gross", "EUR_Fixed_7Y")] == pytest.approx(0.5 * 1.02)     # Pers. 2.2
    assert s2[("cost_interest", "JPY_Fixed_5Y")] == pytest.approx(2.0 * 0.01)  # Pers. 2.3


def test_scenario_example_detects_inconsistent_bank():
    bank = _toy_bank()
    bank["cost_gross"] = bank["cost_gross"] + 1e-6
    with pytest.raises(ValueError):
        scenario_example(bank, 2)
