# Code

| File | Purpose | Run time |
| :--- | :--- | :--- |
| [`decomposition_ensemble_experiments.ipynb`](decomposition_ensemble_experiments.ipynb) | **Main experiment.** Decomposition, direct multi-horizon learners, ensembles, benchmarks, metrics and statistical tests (Tables 3–7, data for Figures 2–5). Stored outputs are those of the published run. | ≈ 1.5 h on a T4 GPU (full); ≈ 25 min on a 4-core CPU with `QUICK_MODE=1` |
| [`prepare_data.py`](prepare_data.py) | Builds `data/processed/` from the raw file in `data/raw/` (`--raw`) or verifies that the raw and processed files agree (`--check`). | seconds |
| [`descriptive_statistics.py`](descriptive_statistics.py) | Reproduces Table 1 and writes `results/descriptive_statistics.csv`. | seconds |
| [`extract_notebook_results.py`](extract_notebook_results.py) | Exports the result tables stored in the notebook's outputs to `results/*.csv`. | seconds |
| [`verify_tables.py`](verify_tables.py) | Checks every value of Tables 1 and 3–7 (`tables/*.docx`) against the computed results. | seconds |
| [`make_figures.py`](make_figures.py) | Redraws Figures 2–5 from the result CSVs into `outputs/figures/`. | seconds |

All scripts are run from the repository root, e.g. `python code/verify_tables.py`.

## Notebook structure

Section numbers match the notebook headings.

| § | Step |
| :-- | :--- |
| 0 | Setup (on Google Colab: install `pmdarima`, `arch`; optional Drive mount). |
| 1 | `CONFIG`: data/output paths, horizons, models, training settings, seeds, `QUICK_MODE`. |
| 2 | Load `data/processed/BTC_USD_daily_OHLCV_processed.csv`; log-transform prices and volume. |
| 3 | STL and robust STL (period 30) of the log price; development/test split (3,556 / 365 days). |
| 4 | Model builders (TCN, N-BEATS, GRU, LSTM, …) and the **direct multi-horizon** engine `deep_direct`: one window in, the full 28-step vector out; non-stationary series are modelled as h-step changes. |
| 5 | Classical benchmarks: ARIMA (order by `auto_arima`; (0, 1, 0) selected) and random walk with drift. |
| 6 | Metrics (RMSE, MAE, MAPE, sMAPE, R², Theil's U, directional accuracy) and the Diebold–Mariano test with Harvey–Leybourne–Newbold correction. |
| 7 | Multi-seed loop (seeds 42–51): direct baselines, ⟨dec⟩-⟨arch⟩, ⟨dec⟩-Auto, ⟨dec⟩-EnsAvg, ⟨dec⟩-EnsWgt and ⟨dec⟩-ARIMA-LSTM. Per-seed metrics are saved as each seed finishes. |
| 8 | Mean ± SD across seeds → `RMSE/MAPE/R2_mean_matrix.csv` (Tables 3–5). |
| 9 | Seed-averaged forecasts → Diebold–Mariano tests (Table 7) and Model Confidence Set at α = 0.10 († in Tables 3–5). |
| 10 | One-sided Wilcoxon signed-rank tests across seeds (proposed vs. benchmarks). |
| 11 | Leading model per horizon (Table 6) and a scale-free average rank. |
| 12 | Diagnostic plots and export. |
| 13 | Summary, list of output files and expected run time. |

## Configuration

Set in the `CONFIG` cell (Section 1):

| Setting | Value |
| :--- | :--- |
| `DATA_DIR`, `FILE_NAME` | `data/processed/`, `BTC_USD_daily_OHLCV_processed.csv` |
| `OUT_DIR` | `outputs/` (kept separate from the published `results/`) |
| `SEASONAL_PERIOD` | 30 days |
| `HORIZONS` | 1, 7, 14, 28 days (the models output all 28 steps) |
| `DECOMPOSITIONS` | `STL`, `RobustSTL` (`rSTL` in the article) |
| `DEEP_MODELS` | `TCN`, `NBEATS`, `GRU` |
| `LOOKBACK`, `USE_OHLCV_FEATURES` | 60 days, lagged OHLCV features on |
| `TEST_SIZE` | 365 days |
| `UNITS`, `EPOCHS`, `BATCH`, `LR`, `PATIENCE` | 64, 100, 32, 0.001 (Adam), 12 |
| `SEEDS` | 42, 43, …, 51 |
| `MCS_SIZE` | 0.10 |

`QUICK_MODE` (environment variable `QUICK_MODE=1`) shortens the run to a 120-day
test period, 15 epochs, TCN and GRU only and seeds 42–43. It is meant only to
check that the pipeline runs end to end; its numbers are not comparable with the
article.

## Model naming

| Notebook / `results/` | Article |
| :--- | :--- |
| `RobustSTL-…` | `rSTL-…` |
| `NBEATS`, `NBEATS(direct)` | `N-BEATS`, `N-BEATS (direct)` |
| `TCN(direct)`, `GRU(direct)` | `TCN (direct)`, `GRU (direct)` |
| `STL-ARIMA-LSTM` | STL-ARIMA-LSTM (ARIMA for the trend, LSTM for seasonal and remainder) |
| `resid` (component) | remainder |

## About the stored notebook outputs

The cell outputs saved in the notebook are those of the run that produced the
published results (Google Colab, Python 3.13, TensorFlow 2.20.0, NVIDIA T4 GPU;
5,066 s for the ten-seed loop). The comments, printed messages, table headers and
plot labels were afterwards translated into English and the data/output paths
were made configurable; the computations were not changed. Paths printed in the
stored outputs therefore still show the original Google Drive folders.
