# Code

| File | Purpose |
| :--- | :--- |
| [`decomposition_ensemble_experiments.ipynb`](decomposition_ensemble_experiments.ipynb) | The full experiment: decomposition, model training, evaluation and statistical testing. Committed with its cell outputs intact, so every reported number is readable without re-running. |
| [`extract_notebook_results.py`](extract_notebook_results.py) | Reads the result tables out of the notebook's stored outputs and writes them to [`../results/`](../results) as CSV. |

The notebook was developed in Google Colab (Python 3, T4 GPU, TensorFlow 2.20.0)
and is the version that produced Table 3 and Figures 2–4 of the manuscript. Its
original working filename was `paper14_v4_directmultihorizon_multiseed_3.ipynb`.

## What the notebook does

Section numbers below match the notebook headings.

| § | Step |
| :-- | :--- |
| 0–1 | Install `pmdarima` and `arch`; set `CONFIG`. |
| 2 | Load the daily OHLCV series and apply a log transform. |
| 3 | STL and robust STL decomposition into trend / seasonal / remainder (reconstruction error ≈ 1.8e-15). |
| 4 | Build the **direct multi-horizon** architectures — each model emits the whole H-step vector at once instead of being applied recursively, which is what removes the error accumulation at *h* = 28. Non-stationary series are differenced: the target is `base[t+h] − base[t]`, and levels are reconstructed afterwards. |
| 5 | Classical baselines: ARIMA (order selected by `auto_arima`, chosen as (0,1,0)) and random walk with drift. Deterministic, so run once. |
| 6 | Metrics: RMSE, MAE, MAPE, sMAPE, *R*², directional accuracy, Theil's U. |
| 7 | Multi-seed run over 10 seeds (42–51), saving per-seed metrics as it goes. |
| 8 | Aggregate to mean ± standard deviation across seeds. |
| 9 | Diebold–Mariano tests and the Model Confidence Set (alpha = 0.10) on the seed-averaged forecasts. |
| 10 | Wilcoxon / *t*-tests across seeds, proposed models against baselines. |
| 11 | Best model per horizon, plus a scale-free average rank. |
| 12 | Figures and export. |

## Key configuration

Set in the `CONFIG` cell:

| Setting | Value |
| :--- | :--- |
| Seasonal period | 30 days |
| Horizons | 1, 7, 14, 28 days |
| Decompositions | STL, RobustSTL (`rSTL` in the manuscript) |
| Deep models | TCN, N-BEATS, GRU |
| Lookback window | 60 days, OHLCV features enabled |
| Test size | 365 days (train 3,556 / test 365 of 3,921 observations) |
| Training | 100 epochs max, batch 32, lr 1e-3, early-stopping patience 12, 64 units |
| Seeds | 42, 43, …, 51 (ten) |
| MCS size | 0.10 |

## Re-running

The notebook was written for Colab and reads from Google Drive. To run it
against this repository instead, change two entries in the `CONFIG` cell:

```python
DATA_DIR = 'data/raw/'      # was '/content/drive/MyDrive/NCS/Hoa/paper14/1-data/'
OUT_DIR  = 'results/'       # was '/content/drive/MyDrive/NCS/Hoa/paper14/3-results_v4/'
```

and skip the `drive.mount` cell. The data-loading helper picks the first CSV in
`DATA_DIR` whose name contains `btc`, which
[`../data/raw/BTC_USD_daily_2014-09-17_2025-06-11.csv`](../data/README.md) does.

These paths have deliberately **not** been edited in the committed notebook, so
that what is in the repository is exactly the notebook that produced the
published results.

Expect a long run: ten seeds × three architectures × three components × two
decompositions, at roughly 485 s per seed on a T4 for the first seed.

## Model naming

The notebook writes `RobustSTL-…`; the manuscript writes `rSTL-…`. The notebook's
`NBEATS` is the manuscript's `N-BEATS`, and `TCN(direct)` is `TCN (direct)`.
