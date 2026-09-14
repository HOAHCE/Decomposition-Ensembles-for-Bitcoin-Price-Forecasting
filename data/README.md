# Data

## `raw/BTC_USD_daily_2014-09-17_2025-06-11.csv`

The daily Bitcoin series used for every experiment, committed byte for byte as
supplied by the authors (original working filename: `BTC_all (6).csv`).

| Property | Value |
| :--- | :--- |
| Observations | 3,921 daily records |
| Period | 2014-09-17 to 2025-06-11 |
| Columns | `Date`, `Open`, `High`, `Low`, `Close`, `Volume`, `Dividends`, `Stock Splits` |
| Date format | ISO 8601 with UTC offset, e.g. `2014-09-17 00:00:00+00:00` |
| Currency | USD |
| Missing values | None |
| Duplicate dates | None |
| `Close` range | 178.10 – 111,673.28 USD |

`Dividends` and `Stock Splits` are zero throughout; they are artefacts of the
download format and are not used. The column layout is the one produced by
[`yfinance`](https://pypi.org/project/yfinance/)'s `Ticker.history()` for the
`BTC-USD` ticker.

### Use in the analysis

`Close` is the forecast target. `Open`, `High`, `Low`, `Close` and `Volume` are
used as input features (`USE_OHLCV_FEATURES=True`). The series is log-transformed,
then decomposed by STL and robust STL at a period of 30 days, and split
chronologically into 3,556 training and 365 test observations — the last 365 days
form the test period reported in the manuscript.

### To be completed by the authors before submission

- [ ] **Exact provenance.** State the download source and the retrieval date. If
      the file came from `yfinance` / Yahoo Finance, say so explicitly and give
      the ticker and the date it was pulled, so the series can be reconstructed.
- [ ] **Terms of use.** Confirm that the source permits redistribution of the
      series in this repository, and name the applicable terms.

## `processed/`

Empty. The decompositions and the train/validation/test splits are derived
deterministically from the raw file by the notebook, so they are not stored
separately. Running the notebook writes its intermediate and final outputs to
[`../results/`](../results).
