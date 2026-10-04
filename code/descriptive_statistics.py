"""Reproduce Table 1: descriptive statistics and stationarity diagnostics.

Computes, for the closing price, its natural logarithm and the daily log return,
the mean, standard deviation, minimum, maximum, skewness, excess kurtosis and the
p-values of the augmented Dickey-Fuller (ADF, null: unit root) and
Kwiatkowski-Phillips-Schmidt-Shin (KPSS, null: stationarity) tests.

Conventions (matching Table 1): population standard deviation (ddof = 0);
moment-based skewness and excess kurtosis (scipy defaults); ADF with a constant
and lag length chosen by AIC; KPSS with a constant and automatic lag selection.
statsmodels reports KPSS p-values only within [0.01, 0.10], so 0.010 means
"0.01 or smaller" and 0.100 means "0.10 or larger".

Usage:
    python code/descriptive_statistics.py
Writes results/descriptive_statistics.csv and prints the table.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.tools.sm_exceptions import InterpolationWarning
from statsmodels.tsa.stattools import adfuller, kpss

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data" / "processed" / "BTC_USD_daily_OHLCV_processed.csv"
OUT = REPO / "results" / "descriptive_statistics.csv"


def describe(name: str, x: np.ndarray) -> dict:
    with warnings.catch_warnings():
        # InterpolationWarning: KPSS p-value outside the lookup table (reported at the bound);
        # FutureWarning: newer statsmodels announces a change of return type.
        warnings.simplefilter("ignore", InterpolationWarning)
        warnings.simplefilter("ignore", FutureWarning)
        kpss_p = kpss(x, regression="c", nlags="auto")[1]
        adf_p = adfuller(x, regression="c", autolag="AIC")[1]
    return {
        "Series": name,
        "Mean": x.mean(),
        "SD": x.std(ddof=0),
        "Minimum": x.min(),
        "Maximum": x.max(),
        "Skewness": stats.skew(x),
        "Excess kurtosis": stats.kurtosis(x),
        "ADF p": adf_p,
        "KPSS p": kpss_p,
    }


def table1() -> pd.DataFrame:
    close = pd.read_csv(DATA)["Close"].to_numpy(float)
    log_close = np.log(close)
    log_return = np.diff(log_close)
    rows = [describe("Close (USD)", close),
            describe("ln(Close)", log_close),
            describe("Log return", log_return)]
    return pd.DataFrame(rows).set_index("Series")


def main() -> None:
    df = table1()
    df.to_csv(OUT)
    with pd.option_context("display.float_format", "{:,.4f}".format,
                           "display.width", 200, "display.max_columns", None):
        print(df)
    print(f"\nN = {len(pd.read_csv(DATA)):,} daily observations. Wrote {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
