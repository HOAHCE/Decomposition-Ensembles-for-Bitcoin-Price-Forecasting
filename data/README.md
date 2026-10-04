# Data

This folder holds the **processed** daily Bitcoin data used in every experiment of
the study. The processing is deterministic and is implemented in
[`../code/prepare_data.py`](../code/prepare_data.py); the experiment notebook
repeats the same steps internally, so both routes give identical series.

## Source

| Property | Value |
| :--- | :--- |
| Asset | Bitcoin, quoted in US dollars |
| Source | Yahoo Finance, ticker `BTC-USD`, daily bars (in the layout produced by the [`yfinance`](https://pypi.org/project/yfinance/) Python package) |
| Period | 17 September 2014 to 11 June 2025 (the full history Yahoo Finance provides for `BTC-USD` up to the cut-off) |
| Observations | 3,921 consecutive calendar days, no gaps, no duplicates, no missing values |
| Variables used | `Open`, `High`, `Low`, `Close` (USD) and `Volume` (USD) |

The underlying market prices are publicly available from Yahoo Finance; use of the
original quotes is subject to Yahoo's terms of service.

## Processing steps

1. Parse the timestamps (UTC), sort chronologically and drop duplicate dates.
2. Keep the five OHLCV columns; the `Dividends` and `Stock Splits` columns of the
   download are zero throughout and are discarded.
3. Keep rows with a positive closing price and fill any missing value by linear
   interpolation (none occur in this series).
4. Log-transform the prices (`ln`) and the volume (`ln(1 + volume)`).
5. Decompose `ln(Close)` into trend, seasonal and remainder components with
   seasonal-trend decomposition based on Loess, using a period of 30 days, in two
   configurations: standard fitting (**STL**) and iterative robust fitting
   (**rSTL**, `statsmodels` `STL(..., robust=True)`; called `RobustSTL` in the
   code). Both reconstruct `ln(Close)` to within 1.8 × 10⁻¹⁵.
6. Split chronologically into a **development** sample (first 3,556 days) and a
   **test** period (final 365 days).

| Sample | Dates | Days | Use |
| :--- | :--- | --: | :--- |
| Development | 2014-09-17 to 2024-06-11 | 3,556 | Model fitting. Input scaling is estimated here only. The final 10% of the development training windows (forecast origins 2023-06-03 to 2024-05-14) form the validation block used for early stopping, Auto selection and EnsWgt weights. |
| Test | 2024-06-12 to 2025-06-11 | 365 | Out-of-sample evaluation. Forecast origins run from 2024-06-11 onward; only targets inside the test period are scored, giving 365, 359, 352 and 338 forecasts at h = 1, 7, 14 and 28 days. |

## Files

### `processed/BTC_USD_daily_OHLCV_processed.csv`

Cleaned daily OHLCV series, one row per day. **This is the input file of the
experiment notebook.**

| Column | Type | Unit | Description |
| :--- | :--- | :--- | :--- |
| `Date` | date (`YYYY-MM-DD`) | – | Trading day (UTC) |
| `Open` | float | USD | Opening price |
| `High` | float | USD | Highest price of the day |
| `Low` | float | USD | Lowest price of the day |
| `Close` | float | USD | Closing price (forecast target) |
| `Volume` | integer | USD | Traded volume |
| `Sample` | string | – | `development` or `test` |

### `processed/BTC_USD_daily_log_STL_components.csv`

Model-ready inputs: log-transformed OHLCV variables and the decomposition of
`ln(Close)`. For each configuration, `trend + seasonal + remainder = log_close`.

| Column | Description |
| :--- | :--- |
| `Date` | Trading day (UTC) |
| `log_open`, `log_high`, `log_low`, `log_close` | Natural logarithm of the price columns |
| `log_volume` | `ln(1 + Volume)` |
| `STL_trend`, `STL_seasonal`, `STL_remainder` | STL components of `log_close` (period 30) |
| `rSTL_trend`, `rSTL_seasonal`, `rSTL_remainder` | Robust STL components of `log_close` (period 30) |
| `Sample` | `development` or `test` |

The components are computed on the full series, exactly as in the notebook
(Section 3), which recomputes them from the OHLCV file at run time.

## Summary statistics

Reproduced by [`../code/descriptive_statistics.py`](../code/descriptive_statistics.py)
(Table 1 of the article):

| Series | Mean | SD | Min | Max | Skewness | Excess kurtosis | ADF p / KPSS p |
| :--- | --: | --: | --: | --: | --: | --: | :-: |
| Close (USD) | 22,699.39 | 26,408.69 | 178.10 | 111,673.28 | 1.364 | 1.095 | 0.973 / 0.010 |
| ln(Close) | 8.928 | 1.865 | 5.182 | 11.623 | -0.551 | -0.949 | 0.815 / 0.010 |
| Log return | 0.0014 | 0.0361 | -0.465 | 0.225 | -0.715 | 11.439 | 0.000 / 0.100 |

## Loading the data

```python
import pandas as pd

ohlcv = pd.read_csv("data/processed/BTC_USD_daily_OHLCV_processed.csv",
                    parse_dates=["Date"], index_col="Date")
comps = pd.read_csv("data/processed/BTC_USD_daily_log_STL_components.csv",
                    parse_dates=["Date"], index_col="Date")

test = ohlcv[ohlcv["Sample"] == "test"]          # 365-day test period
stl = comps[["STL_trend", "STL_seasonal", "STL_remainder"]]
```

## Rebuilding and checking the processed files

```bash
# Verify the committed files (re-runs the cleaning and decomposition and compares)
python code/prepare_data.py --check

# Rebuild them from a raw yfinance-format download of BTC-USD
python code/prepare_data.py --raw path/to/BTC-USD_daily.csv
```

Yahoo Finance occasionally revises historical volumes, so a fresh download may
differ slightly from the series used in the study; the committed processed files
are the exact data behind the published results.
