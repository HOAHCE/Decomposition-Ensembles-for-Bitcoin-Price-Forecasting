# Validation-Guided Decomposition Ensembles for Direct Multi-Horizon Bitcoin Price Forecasting

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22740176.svg)](https://doi.org/10.5281/zenodo.22740176)

Code, raw data and results supporting the article *Validation-Guided
Decomposition Ensembles for Direct Multi-Horizon Bitcoin Price Forecasting*,
submitted to **PeerJ Computer Science**.

> **Version 1.1.0 (7 October 2026) is the version for review:**
> [10.5281/zenodo.23202090](https://doi.org/10.5281/zenodo.23202090)
> (GitHub release [`v1.1.0`](https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting/releases/tag/v1.1.0)).
> All versions share the concept DOI
> [10.5281/zenodo.22740176](https://doi.org/10.5281/zenodo.22740176), which
> always resolves to the latest version. Version 1.1.0 supersedes version 1.0.0
> (10.5281/zenodo.22740177, September 2026), an early snapshot whose notebook
> comments were not yet in English and whose README was incomplete; please do
> not use version 1.0.0. The changes are listed in [`CHANGELOG.md`](CHANGELOG.md).

**Authors:** Hoa Tran Thai<sup>1</sup>, Thanh Manh Le<sup>2</sup>,
Cuong H. Nguyen-Dinh<sup>3,\*</sup>

1. University of Economics, Hue University, Hue, Viet Nam
2. University of Sciences, Hue University, Hue, Viet Nam
3. University of Finance and Marketing, Hue, Viet Nam

\* Corresponding author: Cuong H. Nguyen-Dinh (cuongndh@ufm.edu.vn)

## Contents

1. [Description](#1-description)
2. [Dataset information](#2-dataset-information)
3. [Code information](#3-code-information)
4. [Usage instructions](#4-usage-instructions)
5. [Requirements](#5-requirements)
6. [Methodology](#6-methodology)
7. [Results](#7-results)
8. [Repository structure](#8-repository-structure)
9. [Citations](#9-citations)
10. [License and contribution guidelines](#10-license-and-contribution-guidelines)

## 1. Description

This repository implements a modular machine-learning framework for forecasting
the daily Bitcoin closing price 1, 7, 14 and 28 days ahead. The framework:

1. log-transforms the price and decomposes it into **trend, seasonal and
   remainder** components with seasonal-trend decomposition based on Loess,
   using standard (**STL**) or robust (**rSTL**) fitting and a 30-day period;
2. forecasts each component with a library of deep learners — **temporal
   convolutional network (TCN), N-BEATS and gated recurrent unit (GRU)** —
   through a common **direct multi-horizon** interface that maps one 60-day input
   window to the complete 28-day forecast vector, so no prediction is fed back
   into the input;
3. combines component forecasts with three **validation-guided** rules: **Auto**
   (per component, the learner with the lowest validation loss), **EnsAvg**
   (equal-weight average of the architectures) and **EnsWgt**
   (inverse-validation-loss weights);
4. compares 19 specifications, including ARIMA, a random walk with drift,
   matched undecomposed TCN/N-BEATS/GRU models and classical STL-ARIMA-LSTM
   hybrids, over ten random seeds on a 365-day test period, with Diebold–Mariano
   tests and the Model Confidence Set.

Decomposition-based ensembles led at all four horizons. STL-Auto achieved the
lowest root mean squared error (RMSE) at one day (1,821 USD) and at 28 days
(4,219 USD, R² = 0.938), where it reduced RMSE by 61.6% relative to ARIMA.

Everything needed to reproduce the article's numbers is included: the raw and
processed data, the experiment notebook (with the outputs of the published run), the
extracted result tables, scripts that rebuild Table 1, check Tables 1 and 3–7
and redraw Figures 2–5, and the tables and figures themselves.

## 2. Dataset information

| Property | Value |
| :--- | :--- |
| Source | Yahoo Finance, ticker `BTC-USD` (daily bars) |
| Period | 17 September 2014 – 11 June 2025 |
| Observations | 3,921 consecutive days; no missing values or duplicate dates |
| Variables | Open, High, Low, Close (USD) and Volume; **Close is the forecast target** |
| Split | Development 2014-09-17 to 2024-06-11 (3,556 days; its final 10% of training windows is the validation block) · Test 2024-06-12 to 2025-06-11 (365 days) |

The repository holds the **raw data** exactly as used in the study and the
**processed data** derived from them:

| File | Contents |
| :--- | :--- |
| [`data/raw/BTC_USD_daily_2014-09-17_2025-06-11.csv`](data/raw/BTC_USD_daily_2014-09-17_2025-06-11.csv) | **Raw data.** Daily `BTC-USD` bars from Yahoo Finance (`yfinance` layout: Date, Open, High, Low, Close, Volume, Dividends, Stock Splits), unmodified from the file used in the study. |
| [`data/processed/BTC_USD_daily_OHLCV_processed.csv`](data/processed/BTC_USD_daily_OHLCV_processed.csv) | Curated daily OHLCV series with a `Sample` column (`development` / `test`). The OHLCV values are identical to the raw file; only the two all-zero columns are dropped and the dates are written as `YYYY-MM-DD`. Input file of the experiment. |
| [`data/processed/BTC_USD_daily_log_STL_components.csv`](data/processed/BTC_USD_daily_log_STL_components.csv) | Log-transformed OHLCV inputs and the trend, seasonal and remainder components of ln(Close) from STL and rSTL (period 30). |

`python code/prepare_data.py --check` confirms that the raw file reproduces the
processed files exactly.

The price level and log price are non-stationary (ADF p = 0.973 and 0.815),
whereas daily log returns are stationary with excess kurtosis 11.44 (Table 1).
The full data dictionary, processing steps and a loading example are in
[`data/README.md`](data/README.md).

## 3. Code information

All code is Python. Scripts are run from the repository root.

| File | Purpose |
| :--- | :--- |
| [`code/decomposition_ensemble_experiments.ipynb`](code/decomposition_ensemble_experiments.ipynb) | Main experiment: decomposition, direct multi-horizon learners, ensembles, benchmarks, metrics, Diebold–Mariano tests, Model Confidence Set and Wilcoxon tests (Tables 3–7; data for Figures 2–5). Saved with the outputs of the published run. |
| [`code/prepare_data.py`](code/prepare_data.py) | Builds the processed files from the raw `BTC-USD` file (`--raw`), or verifies that the raw and processed files agree (`--check`). |
| [`code/descriptive_statistics.py`](code/descriptive_statistics.py) | Reproduces Table 1. |
| [`code/extract_notebook_results.py`](code/extract_notebook_results.py) | Exports the result tables stored in the notebook outputs to `results/*.csv`. |
| [`code/verify_tables.py`](code/verify_tables.py) | Checks every value of Tables 1 and 3–7 against the computed results. |
| [`code/make_figures.py`](code/make_figures.py) | Redraws Figures 2–5 from the result CSVs. |

Main functions in the notebook: `decompose` (STL/rSTL), `build_model` (TCN,
N-BEATS, GRU, LSTM, MLP, Transformer), `deep_direct` (direct multi-horizon
training and forecasting for one series), `arima_roll` and `rw` (benchmarks),
`metrics_full` (RMSE, MAE, MAPE, sMAPE, R², Theil's U, directional accuracy) and
`dm_test` (Diebold–Mariano with Harvey–Leybourne–Newbold correction). A
section-by-section guide and the configuration options are in
[`code/README.md`](code/README.md).

## 4. Usage instructions

### 4.1 Installation

```bash
git clone https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting.git
cd Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4.2 Check the published numbers (seconds, no GPU)

```bash
python code/prepare_data.py --check     # raw -> processed data are reproduced by the cleaning/decomposition code
python code/descriptive_statistics.py   # Table 1
python code/verify_tables.py            # Tables 1 and 3-7 vs. computed results (305 checks)
python code/make_figures.py             # redraw Figures 2-5 into outputs/figures/
```

### 4.3 Quick end-to-end test of the experiment (CPU, about 25 minutes)

```bash
QUICK_MODE=1 jupyter nbconvert --to notebook --execute \
    code/decomposition_ensemble_experiments.ipynb --output-dir outputs --output quick_test.ipynb
```

`QUICK_MODE` uses a 120-day test period, 15 epochs, two architectures and two
seeds; it took about 25 minutes on a 4-core CPU. It confirms that the full
pipeline runs and writes every output file to `outputs/`; its numbers are
**not** the published ones.

### 4.4 Full replication (GPU recommended)

Open `code/decomposition_ensemble_experiments.ipynb` in Jupyter and run all
cells, or run it headless:

```bash
jupyter nbconvert --to notebook --execute code/decomposition_ensemble_experiments.ipynb \
    --output-dir outputs --output full_run.ipynb --ExecutePreprocessor.timeout=-1
python code/make_figures.py --results outputs --out outputs/figures
```

The notebook reads `data/processed/BTC_USD_daily_OHLCV_processed.csv` and writes
all result files to `outputs/`, leaving the published `results/` untouched. The
published run took about 1.5 hours on an NVIDIA T4 GPU (5,066 s for the ten-seed
loop).

**Google Colab.** Choose a GPU runtime and run in the first cell:

```python
!git clone https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting.git
%cd Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
```

then open `code/decomposition_ensemble_experiments.ipynb` (or upload it) and run
all cells; Section 0 installs `pmdarima` and `arch` automatically.

**Expected agreement.** ARIMA and the random walk are deterministic and
reproduce the published RMSE and MAPE exactly from `data/processed/`. The deep models are seeded (seeds 42–51), but GPU kernels and
library versions introduce small numerical differences, so re-run values of the
deep and ensemble models can differ slightly from the published ones while the
rankings and conclusions are expected to hold.

### 4.5 Loading the data and results

```python
import pandas as pd

ohlcv = pd.read_csv("data/processed/BTC_USD_daily_OHLCV_processed.csv",
                    parse_dates=["Date"], index_col="Date")
rmse = pd.read_csv("results/RMSE_mean_matrix.csv", index_col="Model")   # Table 3
print(rmse.loc[["STL-Auto", "ARIMA"]])
```

## 5. Requirements

| Component | Version |
| :--- | :--- |
| Python | 3.10 or later (published run: 3.13) |
| TensorFlow / Keras | 2.20.0 (TCN, N-BEATS, GRU, LSTM) |
| statsmodels | ≥ 0.14 (STL, ARIMA, ADF, KPSS) |
| pmdarima | ≥ 2.0 (ARIMA order selection) |
| arch | ≥ 6.0 (Model Confidence Set) |
| numpy, pandas, scipy, matplotlib | numpy ≥ 1.26, pandas ≥ 2.0, scipy ≥ 1.11, matplotlib ≥ 3.7 |
| jupyter, nbconvert | to run the notebook |
| python-docx, lxml | only for `verify_tables.py` and `extract_notebook_results.py` |

All packages are listed in [`requirements.txt`](requirements.txt).

**Computing infrastructure.** The published results were produced on Google
Colab (Linux, Python 3.13, TensorFlow 2.20.0, one NVIDIA T4 GPU with 16 GB).
The repository workflow (Sections 4.2–4.3) was also tested on Linux with
Python 3.11 and CPU-only TensorFlow 2.20.0. A GPU is recommended for the full
run; the quick test runs on a CPU.

## 6. Methodology

1. **Data preparation.** Daily OHLCV data are cleaned (chronological order, no
   duplicates, positive prices), the prices are log-transformed and volume is
   transformed with ln(1 + x). OHLCV variables enter the models only as lagged
   values available at the forecast origin.
2. **Chronological split.** The final 365 days form the test period. The
   preceding 3,556 days form the development sample, whose final block (the
   last 10% of training windows) is used for early stopping, component-model
   selection and ensemble weighting. Scaling parameters are estimated on the
   development data only.
3. **Decomposition.** ln(Close) = trend + seasonal + remainder, using STL or
   robust STL (rSTL) with a 30-day period; both reconstruct the log series to
   within 1.8 × 10⁻¹⁵.
4. **Direct multi-horizon component forecasting.** Each learner receives a
   60-day window of one component plus lagged OHLCV features and outputs the
   28-step vector at once. The non-stationary trend (and the undecomposed log
   price) is modelled as h-step changes and reconstructed from the value at the
   origin; seasonal and remainder components are modelled in levels. Learners:
   TCN with dilations 1, 2, 4, 8; N-BEATS with three doubly residual blocks; GRU
   with two recurrent layers (64 units, Adam, learning rate 0.001, batch 32, up
   to 100 epochs, early-stopping patience 12).
5. **Validation-guided combination.** *Auto* selects, for each component, the
   architecture with the lowest validation loss over the full output vector and
   sums the selected component forecasts. *EnsAvg* averages the reconstructed
   log-price forecasts of the three architectures with equal weights; *EnsWgt*
   weights them by inverse validation loss. The price forecast is
   exp(trend + seasonal + remainder).
6. **Benchmarks.** ARIMA (order chosen by `auto_arima` on the development data:
   (0, 1, 0)), random walk with drift, TCN/N-BEATS/GRU fitted directly to the
   undecomposed log price with the same windows, features, output interface,
   training budget and seeds, and STL-/rSTL-ARIMA-LSTM hybrids (ARIMA for the
   trend, LSTM for seasonal and remainder components).
7. **Evaluation.** RMSE (primary), MAPE, R² and directional accuracy at
   h = 1, 7, 14 and 28 days, using only forecast origins whose targets lie in the
   test period. Every stochastic model is trained with seeds 42–51; results are
   reported as seed means (± SD).
8. **Statistical inference.** Diebold–Mariano tests with the
   Harvey–Leybourne–Newbold correction compare the seed-averaged STL-Auto
   forecast with each undecomposed benchmark; the Model Confidence Set
   (α = 0.10) is computed on the seed-averaged squared errors; one-sided Wilcoxon
   signed-rank tests across seeds provide supporting evidence.

The experimental configuration is summarised in [Table 2](tables/Table_2.md).

## 7. Results

| Output | Location |
| :--- | :--- |
| Tables 1–7 (PeerJ-format `.docx` + Markdown) | [`tables/`](tables/README.md) |
| Figures 1–5 | [`figures/`](figures/README.md) |
| Result matrices and test statistics (CSV) | [`results/`](results/README.md) |

Leading model at each horizon ([Table 6](tables/Table_6.md)):

| h (days) | Leading model | RMSE (USD), mean ± SD | R² | MAPE (%) | DA (%) | In MCS |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | STL-Auto | 1,821 ± 129 | 0.9888 | 1.79 | 64.7 | Yes |
| 7 | rSTL-EnsAvg | 2,359 ± 121 | 0.9814 | 2.35 | 83.7 | No |
| 14 | STL-EnsAvg | 2,153 ± 102 | 0.9845 | 2.13 | 90.9 | No |
| 28 | STL-Auto | 4,219 ± 420 | 0.9378 | 3.85 | 88.3 | Yes |

## 8. Repository structure

```
.
├── README.md                      This file
├── code/
│   ├── decomposition_ensemble_experiments.ipynb   Main experiment (outputs of the published run)
│   ├── prepare_data.py                            data/raw/ -> data/processed/ (or --check)
│   ├── descriptive_statistics.py                  Table 1
│   ├── extract_notebook_results.py                Notebook outputs -> results/*.csv
│   ├── verify_tables.py                           Tables 1, 3-7 vs. computed results
│   ├── make_figures.py                            Figures 2-5 from results/*.csv
│   └── README.md
├── data/
│   ├── raw/
│   │   └── BTC_USD_daily_2014-09-17_2025-06-11.csv Raw Yahoo Finance data (unmodified)
│   ├── processed/
│   │   ├── BTC_USD_daily_OHLCV_processed.csv      Cleaned OHLCV + sample split
│   │   └── BTC_USD_daily_log_STL_components.csv   Log inputs + STL/rSTL components
│   └── README.md                                  Data dictionary
├── results/                       Result CSVs behind Tables 1, 3-7 and Figures 2-5
├── tables/                        Tables 1-7 (.docx and .md)
├── figures/                       Figures 1-5 (.png)
├── docs/zenodo-archiving.md       Zenodo archive (DOI) and how to add a new version
├── requirements.txt               Python dependencies
├── CHANGELOG.md                   Version history (v1.1.0 supersedes v1.0.0)
├── CITATION.cff                   Citation metadata
├── AUTHORS.md                     Authors and affiliations
├── LICENSE                        MIT (code)
└── LICENSE-DATA.md                CC BY 4.0 (data, tables, figures, results)
```

Running the notebook or `make_figures.py` creates an `outputs/` folder, which is
not tracked by Git.

## 9. Citations

If you use this code or data, please cite the article (citation details will be
updated on publication):

> Hoa Tran Thai, Thanh Manh Le, Cuong H. Nguyen-Dinh. Validation-Guided
> Decomposition Ensembles for Direct Multi-Horizon Bitcoin Price Forecasting.
> *PeerJ Computer Science* (submitted).

and the archived code and data:

> Hoa Tran Thai, Thanh Manh Le, Cuong H. Nguyen-Dinh. 2026. Validation-Guided
> Decomposition Ensembles for Direct Multi-Horizon Bitcoin Price Forecasting:
> code, raw data and results. Version 1.1.0. Zenodo.
> https://doi.org/10.5281/zenodo.23202090

**Data and code availability.** The code, raw data, processed data and results
are available on GitHub at
<https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting>
and archived on Zenodo: version 1.1.0, the version for review, at
[10.5281/zenodo.23202090](https://doi.org/10.5281/zenodo.23202090); all
versions under the concept DOI
[10.5281/zenodo.22740176](https://doi.org/10.5281/zenodo.22740176), which always
resolves to the latest version. Machine-readable metadata are in
[`CITATION.cff`](CITATION.cff).

Methods implemented in this repository:

- Ben Taieb S, Bontempi G, Atiya AF, Sorjamaa A. 2012. A review and comparison of strategies for multi-step ahead time series forecasting based on the NN5 forecasting competition. *Expert Systems with Applications* 39:7067–7083. https://doi.org/10.1016/j.eswa.2012.01.039
- Diebold FX, Mariano RS. 1995. Comparing predictive accuracy. *Journal of Business & Economic Statistics* 13:253–263. https://doi.org/10.1080/07350015.1995.10524599
- Hansen PR, Lunde A, Nason JM. 2011. The model confidence set. *Econometrica* 79:453–497. https://doi.org/10.3982/ECTA5771
- Harvey D, Leybourne S, Newbold P. 1997. Testing the equality of prediction mean squared errors. *International Journal of Forecasting* 13:281–291. https://doi.org/10.1016/S0169-2070(96)00719-4

Data source: Yahoo Finance, `BTC-USD` daily prices.

## 10. License and contribution guidelines

**License.** Source code is released under the [MIT License](LICENSE). The
raw and processed data, tables, figures and result files are released under the
[Creative Commons Attribution 4.0 International License](LICENSE-DATA.md)
(CC BY 4.0).

**Contributions.** Questions, bug reports and reproduction problems are welcome
as [GitHub issues](https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting/issues).
When reporting a reproduction difference, please include your operating system,
Python and package versions (`pip freeze`), hardware (CPU/GPU) and the affected
table or file. Pull requests that fix bugs or improve documentation are welcome;
please keep the published `results/`, `tables/` and `figures/` unchanged so
that they continue to match the article, and describe any change that affects
the numbers. For other enquiries, contact the corresponding author,
Cuong H. Nguyen-Dinh (cuongndh@ufm.edu.vn).
