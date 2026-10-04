"""Build the processed Bitcoin dataset used in the study.

The experiment uses daily BTC-USD prices from Yahoo Finance (17 September 2014 -
11 June 2025, 3,921 observations). This script turns a raw daily file in the
layout produced by `yfinance` (`Date, Open, High, Low, Close, Volume, Dividends,
Stock Splits`) into the two processed files stored in `data/processed/`:

1. `BTC_USD_daily_OHLCV_processed.csv`
   Cleaned daily OHLCV levels, one row per day, plus the chronological sample
   label (`development` for the first 3,556 days, `test` for the final 365).
   This is the file the experiment notebook reads.

2. `BTC_USD_daily_log_STL_components.csv`
   Log-transformed OHLCV inputs and the trend / seasonal / remainder components
   of ln(Close) obtained with STL and robust STL (rSTL) at a period of 30 days.

The cleaning and decomposition steps are identical to Sections 2-3 of
`code/decomposition_ensemble_experiments.ipynb`, so the notebook reproduces the
same series when it reads file 1.

Usage:
    python code/prepare_data.py --raw path/to/BTC-USD_daily.csv
    python code/prepare_data.py --check   # verify the committed processed files
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "data" / "processed"
OHLCV_FILE = OUT_DIR / "BTC_USD_daily_OHLCV_processed.csv"
COMPONENTS_FILE = OUT_DIR / "BTC_USD_daily_log_STL_components.csv"

OHLCV_COLS = ["Open", "High", "Low", "Close", "Volume"]
TARGET = "Close"
SEASONAL_PERIOD = 30   # days
TEST_SIZE = 365        # final 365 observations form the test period


def clean_ohlcv(raw: pd.DataFrame) -> pd.DataFrame:
    """Parse dates, sort, de-duplicate and keep positive, gap-free OHLCV rows."""
    raw = raw.copy()
    raw["Date"] = pd.to_datetime(raw["Date"], utc=True, errors="coerce")
    raw = (raw.dropna(subset=["Date"]).sort_values("Date")
              .drop_duplicates("Date").set_index("Date"))
    df = raw[[c for c in OHLCV_COLS if c in raw.columns]].apply(pd.to_numeric, errors="coerce")
    df = df[df[TARGET] > 0].interpolate(limit_direction="both")
    return df


def log_features(df: pd.DataFrame) -> pd.DataFrame:
    """Log-transformed model inputs (log1p for volume)."""
    feat = pd.DataFrame(index=df.index)
    for c in ["Open", "High", "Low", "Close"]:
        feat["log_" + c.lower()] = np.log(df[c].clip(lower=1e-8))
    feat["log_volume"] = np.log1p(df["Volume"].clip(lower=0))
    return feat


def decompose(y_log: pd.Series, robust: bool) -> pd.DataFrame:
    """STL (robust=False) or robust STL (robust=True) of the log price."""
    res = STL(y_log, period=SEASONAL_PERIOD, robust=robust).fit()
    return pd.DataFrame({"trend": res.trend, "seasonal": res.seasonal,
                         "remainder": res.resid}, index=y_log.index)


def sample_labels(n: int) -> list[str]:
    n_dev = n - TEST_SIZE
    return ["development"] * n_dev + ["test"] * TEST_SIZE


def build(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Return the two processed tables, both indexed by calendar date."""
    dates = df.index.strftime("%Y-%m-%d")
    sample = sample_labels(len(df))

    ohlcv = df.copy()
    ohlcv.index = dates
    ohlcv.index.name = "Date"
    ohlcv["Volume"] = ohlcv["Volume"].round().astype("int64")
    ohlcv["Sample"] = sample

    feat = log_features(df)
    y_log = feat["log_close"]
    comps = feat.copy()
    for label, robust in (("STL", False), ("rSTL", True)):
        dec = decompose(y_log, robust)
        for col in dec.columns:
            comps[f"{label}_{col}"] = dec[col].values
    comps.index = dates
    comps.index.name = "Date"
    comps["Sample"] = sample
    return ohlcv, comps


def summary(ohlcv: pd.DataFrame, comps: pd.DataFrame) -> None:
    n_dev = int((ohlcv["Sample"] == "development").sum())
    n_test = int((ohlcv["Sample"] == "test").sum())
    print(f"Observations: {len(ohlcv):,} ({ohlcv.index[0]} to {ohlcv.index[-1]})")
    print(f"Development: {n_dev:,}  Test: {n_test:,}")
    for label in ("STL", "rSTL"):
        recon = comps[[f"{label}_trend", f"{label}_seasonal", f"{label}_remainder"]].sum(axis=1)
        err = np.max(np.abs(recon.values - comps["log_close"].values))
        print(f"{label:<4} max reconstruction error: {err:.1e}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--raw", type=Path, help="raw daily CSV in yfinance layout")
    group.add_argument("--check", action="store_true",
                       help="rebuild from the committed OHLCV file and compare")
    args = parser.parse_args()

    if args.raw:
        df = clean_ohlcv(pd.read_csv(args.raw))
        ohlcv, comps = build(df)
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        ohlcv.to_csv(OHLCV_FILE)
        comps.to_csv(COMPONENTS_FILE)
        print(f"Wrote {OHLCV_FILE.relative_to(REPO)}")
        print(f"Wrote {COMPONENTS_FILE.relative_to(REPO)}")
        summary(ohlcv, comps)
        return

    # --check: the processed OHLCV file must survive the same cleaning step
    # unchanged, and the stored components must match a fresh decomposition.
    stored_ohlcv = pd.read_csv(OHLCV_FILE)
    stored_comps = pd.read_csv(COMPONENTS_FILE, index_col="Date")
    df = clean_ohlcv(stored_ohlcv)
    ohlcv, comps = build(df)
    pd.testing.assert_frame_equal(ohlcv, stored_ohlcv.set_index("Date"), check_exact=True)
    num = [c for c in comps.columns if c != "Sample"]
    diff = np.max(np.abs(comps[num].values - stored_comps[num].values))
    print(f"OHLCV file: consistent. Max difference in log/STL columns: {diff:.1e}")
    summary(ohlcv, comps)


if __name__ == "__main__":
    main()
