"""Perhitungan faktor konversi kurs q dan matriks biaya portofolio skenario.

Menyediakan fungsi untuk:
1. Menghitung faktor konversi kurs q_{c,s} (Persamaan 2.1):
   - q_USD = 1.0
   - q_EUR = X_{USD/EUR, 0} / X_{USD/EUR, s}
   - q_JPY = X_{USD/JPY, 0} / X_{USD/JPY, s}
2. Menghitung matriks biaya instrumen utang C_{i,s} (N x 7):
   - Biaya bruto (Pers. 2.2 — Definisi UTAMA): C_{i,s} = q_{c(i),s} * (1 + y_{i,s}/100)
   - Biaya bunga (Pers. 2.3 — Definisi SENSITIVITAS): C^I_{i,s} = q_{c(i),s} * (y_{i,s}/100)
3. Mengemas paket bank skenario lengkap untuk penyimpanan dan evaluasi optimasi.
"""

from typing import Any, Dict, List, Optional
import numpy as np

from mccar_kma.data.cleaning import ALL_MARKET_COLS
from mccar_kma.scenarios.estimation import INSTRUMENTS, INSTRUMENT_NAMES


CURRENCY_ORDER = ["USD", "EUR", "JPY"]


def compute_q_factors(
    market_scenarios: np.ndarray,
    market_cols: List[str],
    x0_dict: Dict[str, float],
) -> np.ndarray:
    """Menghitung faktor konversi kurs q_{c,s} untuk setiap skenario s (Persamaan 2.1).

    Persamaan:
        q_{USD,s} = 1.0
        q_{EUR,s} = X_{USD/EUR,0} / X_{USD/EUR,s}
        q_{JPY,s} = X_{USD/JPY,0} / X_{USD/JPY,s}

    Parameters
    ----------
    market_scenarios : np.ndarray
        Array skenario pasar (N, K).
    market_cols : List[str]
        Daftar nama kolom variabel pasar pada market_scenarios.
    x0_dict : Dict[str, float]
        Nilai kurs awal t=0 (observasi terakhir jendela).

    Returns
    -------
    np.ndarray
        Array berukuran (N, 3) dengan kolom [q_USD, q_EUR, q_JPY].
    """
    n_scen = len(market_scenarios)
    idx_eur = market_cols.index("FX_USD/EUR")
    idx_jpy = market_cols.index("FX_USD/JPY")

    x0_eur = float(x0_dict["FX_USD/EUR"])
    x0_jpy = float(x0_dict["FX_USD/JPY"])

    fx_eur_scen = market_scenarios[:, idx_eur]
    fx_jpy_scen = market_scenarios[:, idx_jpy]

    if np.any(fx_eur_scen <= 0) or np.any(fx_jpy_scen <= 0):
        raise ValueError("Kurs skenario harus bernilai positif (> 0).")

    q_usd = np.ones(n_scen, dtype=float)
    q_eur = x0_eur / fx_eur_scen
    q_jpy = x0_jpy / fx_jpy_scen

    q_mat = np.column_stack([q_usd, q_eur, q_jpy])
    return q_mat


def compute_scenario_costs(
    market_scenarios: np.ndarray,
    market_cols: List[str],
    x0_dict: Dict[str, float],
    instruments: Optional[List[Dict[str, Any]]] = None,
    cost_def: str = "gross",
) -> np.ndarray:
    """Menghitung matriks biaya instrumen utang C_{i,s} berukuran (N, 7).

    Persamaan:
        Biaya bruto (Pers. 2.2):    C_{i,s} = q_{c(i),s} * (1 + y_{i,s}/100)
        Biaya bunga (Pers. 2.3):    C^I_{i,s} = q_{c(i),s} * (y_{i,s}/100)

    Parameters
    ----------
    market_scenarios : np.ndarray
        Array skenario pasar (N, K).
    market_cols : List[str]
        Daftar nama kolom variabel pasar pada market_scenarios.
    x0_dict : Dict[str, float]
        Nilai kurs awal t=0.
    instruments : Optional[List[Dict[str, Any]]]
        Daftar metadata 7 instrumen. Default: INSTRUMENTS.
    cost_def : str
        'gross' (utama) atau 'interest' (sensitivitas).

    Returns
    -------
    np.ndarray
        Array berukuran (N, 7) berisi biaya tiap instrumen per skenario.
    """
    if cost_def not in ("gross", "interest"):
        raise ValueError(f"cost_def tidak valid: '{cost_def}'. Pilih 'gross' atau 'interest'.")

    if instruments is None:
        instruments = INSTRUMENTS

    n_scen = len(market_scenarios)
    q_mat = compute_q_factors(market_scenarios, market_cols, x0_dict)
    q_map = {"USD": q_mat[:, 0], "EUR": q_mat[:, 1], "JPY": q_mat[:, 2]}

    costs = np.zeros((n_scen, len(instruments)), dtype=float)

    for i, inst in enumerate(instruments):
        curr = inst["currency"]
        y_col = inst["yield_col"]
        idx_y = market_cols.index(y_col)

        y_vals = market_scenarios[:, idx_y]  # dalam persen, misal 4.231%
        q_vals = q_map[curr]

        if cost_def == "gross":
            # Persamaan 2.2: q * (1 + y/100)
            costs[:, i] = q_vals * (1.0 + y_vals / 100.0)
        else:
            # Persamaan 2.3: q * (y/100)
            costs[:, i] = q_vals * (y_vals / 100.0)

    return costs


def build_scenario_bank(
    market_scenarios: np.ndarray,
    log_returns: np.ndarray,
    market_cols: List[str],
    s0_dict: Dict[str, float],
    instruments: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, np.ndarray]:
    """Mengemas seluruh array skenario ke dictionary terstruktur untuk disimpan.

    Parameters
    ----------
    market_scenarios : np.ndarray
        Array nilai pasar terminal S_T (N, 9).
    log_returns : np.ndarray
        Array log-return tahunan ln(S_T / S_0) (N, 9).
    market_cols : List[str]
        Daftar nama kolom pasar (9).
    s0_dict : Dict[str, float]
        Dictionary nilai awal S_0 pada t=0.
    instruments : Optional[List[Dict[str, Any]]]
        Metadata 7 instrumen utang.

    Returns
    -------
    Dict[str, np.ndarray]
        Dictionary berisi:
        - 'scenarios_market': (N, 9)
        - 'scenarios_log_returns': (N, 9)
        - 'cost_gross': (N, 7)
        - 'cost_interest': (N, 7)
        - 'q_factors': (N, 3)
        - 's0': (9,)
        - 'variable_names': array of str (9,)
        - 'instrument_names': array of str (7,)
        - 'currency_names': array of str (3,)
    """
    if instruments is None:
        instruments = INSTRUMENTS

    inst_names = [inst["name"] for inst in instruments]
    s0_arr = np.array([float(s0_dict[c]) for c in market_cols], dtype=float)

    # 1. Faktor q
    q_mat = compute_q_factors(market_scenarios, market_cols, s0_dict)

    # 2. Biaya bruto (Pers. 2.2)
    c_gross = compute_scenario_costs(
        market_scenarios=market_scenarios,
        market_cols=market_cols,
        x0_dict=s0_dict,
        instruments=instruments,
        cost_def="gross",
    )

    # 3. Biaya bunga (Pers. 2.3)
    c_interest = compute_scenario_costs(
        market_scenarios=market_scenarios,
        market_cols=market_cols,
        x0_dict=s0_dict,
        instruments=instruments,
        cost_def="interest",
    )

    return {
        "scenarios_market": market_scenarios,
        "scenarios_log_returns": log_returns,
        "cost_gross": c_gross,
        "cost_interest": c_interest,
        "q_factors": q_mat,
        "s0": s0_arr,
        "variable_names": np.array(market_cols, dtype=object),
        "instrument_names": np.array(inst_names, dtype=object),
        "currency_names": np.array(CURRENCY_ORDER, dtype=object),
    }
