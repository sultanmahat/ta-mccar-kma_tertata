"""Implementasi Natural Cubic Spline mandiri sesuai Persamaan 2.4–2.6.

Persamaan 2.4–2.6 (proposal revisi pasca-sempro):
  g_i(x) = a_i + b_i(x − x_i) + c_i(x − x_i)² + d_i(x − x_i)³

Syarat batas natural: c_1 = c_M = 0.
Sistem tridiagonal untuk c_i:
  h_{i-1}·c_{i-1} + 2(h_{i-1} + h_i)·c_i + h_i·c_{i+1}
      = 3 · ((z_{i+1} − z_i)/h_i − (z_i − z_{i-1})/h_{i-1})

Koefisien turunan:
  b_i = (z_{i+1} − z_i)/h_i − (h_i/3)·(2·c_i + c_{i+1})
  d_i = (c_{i+1} − c_i) / (3·h_i)
"""

from typing import Optional, Union

import numpy as np
import pandas as pd


class NaturalCubicSpline:
    """Natural cubic spline interpolator mandiri.

    Menyelesaikan sistem tridiagonal sesuai Persamaan 2.4–2.6 proposal.
    Syarat batas natural: turunan kedua di titik ujung = 0.

    Parameters
    ----------
    x : array-like
        Titik simpul (knot), harus unik dan terurut monoton naik.
    y : array-like
        Nilai fungsi pada titik simpul.
    """

    def __init__(self) -> None:
        self._x: Optional[np.ndarray] = None
        self._a: Optional[np.ndarray] = None  # koefisien orde 0 (a_i = z_i)
        self._b: Optional[np.ndarray] = None  # koefisien orde 1
        self._c_full: Optional[np.ndarray] = None  # panjang n (termasuk c_n)
        self._d: Optional[np.ndarray] = None  # koefisien orde 3

    def fit(self, x: np.ndarray, y: np.ndarray) -> "NaturalCubicSpline":
        """Hitung koefisien natural cubic spline dari titik simpul.

        Persamaan 2.4–2.6: Menyelesaikan sistem linear tridiagonal n×n
        untuk mendapatkan c_1,...,c_n dengan syarat c_1 = c_n = 0.

        Parameters
        ----------
        x : np.ndarray
            Titik simpul, urutan monotonik naik, tanpa duplikat.
        y : np.ndarray
            Nilai fungsi di titik simpul.

        Returns
        -------
        self
        """
        x = np.asarray(x, dtype=float)
        y = np.asarray(y, dtype=float)

        if len(x) < 2:
            raise ValueError("Dibutuhkan minimal 2 titik simpul.")
        if len(x) != len(y):
            raise ValueError("x dan y harus memiliki panjang yang sama.")
        if not np.all(np.diff(x) > 0):
            raise ValueError("Titik simpul x harus terurut monotonik naik dan unik.")

        n = len(x)
        h = np.diff(x)  # h_i = x_{i+1} - x_i, panjang n-1

        # --- Membangun sistem tridiagonal (Persamaan 2.5) ---
        # Baris 0: c_0 = 0 (syarat batas natural)
        # Baris i (1 <= i <= n-2): persamaan tridiagonal
        # Baris n-1: c_{n-1} = 0 (syarat batas natural)
        A = np.zeros((n, n))
        rhs = np.zeros(n)

        # Syarat batas natural: c_0 = 0 dan c_{n-1} = 0
        A[0, 0] = 1.0
        A[n - 1, n - 1] = 1.0

        for i in range(1, n - 1):
            A[i, i - 1] = h[i - 1]
            A[i, i] = 2.0 * (h[i - 1] + h[i])
            A[i, i + 1] = h[i]
            rhs[i] = 3.0 * (
                (y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1]
            )

        # Selesaikan sistem tridiagonal
        c_full = np.linalg.solve(A, rhs)

        # --- Hitung koefisien b_i dan d_i (Persamaan 2.6) ---
        n_intervals = n - 1
        a = y[:-1]  # a_i = z_i
        b = np.empty(n_intervals)
        d = np.empty(n_intervals)

        for i in range(n_intervals):
            b[i] = (y[i + 1] - y[i]) / h[i] - (h[i] / 3.0) * (
                2.0 * c_full[i] + c_full[i + 1]
            )
            d[i] = (c_full[i + 1] - c_full[i]) / (3.0 * h[i])

        self._x = x
        self._a = a
        self._b = b
        self._c_full = c_full
        self._d = d

        return self

    def predict(self, x_new: Union[float, np.ndarray]) -> np.ndarray:
        """Evaluasi spline pada titik baru.

        Parameters
        ----------
        x_new : float or np.ndarray
            Titik evaluasi. Harus berada dalam rentang [x_min, x_max].

        Returns
        -------
        np.ndarray
            Nilai spline di titik x_new.
        """
        if self._x is None:
            raise RuntimeError("Spline belum di-fit. Panggil fit() terlebih dahulu.")

        x_new = np.atleast_1d(np.asarray(x_new, dtype=float))

        # Temukan interval i: x_i <= x_new < x_{i+1}
        idx = np.searchsorted(self._x, x_new, side="right") - 1
        idx = np.clip(idx, 0, len(self._a) - 1)

        dx = x_new - self._x[idx]
        result = (
            self._a[idx]
            + self._b[idx] * dx
            + self._c_full[idx] * dx**2
            + self._d[idx] * dx**3
        )
        return result

    @property
    def c_boundary(self) -> tuple:
        """Nilai c di batas kiri dan kanan (harus = 0 untuk natural spline)."""
        if self._c_full is None:
            return (None, None)
        return (float(self._c_full[0]), float(self._c_full[-1]))


def interpolate_series_spline(series: pd.Series) -> pd.Series:
    """Mengisi nilai NaN pada pandas Series menggunakan NaturalCubicSpline.

    Titik simpul adalah seluruh posisi indeks numerik dengan nilai non-NaN.
    Titik evaluasi adalah posisi indeks NaN.

    Parameters
    ----------
    series : pd.Series
        Deret numerik dengan kemungkinan nilai NaN yang akan diisi.

    Returns
    -------
    pd.Series
        Series yang nilai NaN-nya telah diisi dengan spline.
    """
    result = series.copy()
    valid_mask = series.notna()

    if valid_mask.all():
        return result  # Tidak ada NaN, tidak perlu interpolasi

    if not valid_mask.any():
        raise ValueError("Seluruh nilai adalah NaN; tidak dapat membangun spline.")

    x_knots = np.where(valid_mask)[0].astype(float)
    y_knots = series.loc[valid_mask].to_numpy(dtype=float)

    spline = NaturalCubicSpline()
    spline.fit(x_knots, y_knots)

    missing_positions = np.where(~valid_mask)[0].astype(float)
    interpolated = spline.predict(missing_positions)

    result.iloc[np.where(~valid_mask)[0]] = interpolated
    return result
