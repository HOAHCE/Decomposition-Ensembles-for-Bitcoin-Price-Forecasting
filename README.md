# Decomposition Ensembles for Bitcoin Price Forecasting

Data, code and results supporting the manuscript **"Decomposition Ensembles for
Bitcoin Price Forecasting"**, submitted to *PeerJ Computer Science*.

## Authors

Hoa Tran Thai <sup>1,2</sup>, Thanh Manh Le <sup>2</sup>, Cuong H. Nguyen-Dinh <sup>3,\*</sup>

1. University of Economics, Hue University, Hue, Viet Nam
2. University of Sciences, Hue University, Hue, Viet Nam
3. University of Finance and Marketing, Hue, Viet Nam

\* Corresponding author: Cuong H. Nguyen-Dinh — ndhcuong@ufm.edu.vn

| Author | Email |
| :--- | :--- |
| Hoa Tran Thai | tranthaihoa@hueuni.edu.vn |
| Thanh Manh Le | lmthanh@hueuni.edu.vn |
| Cuong H. Nguyen-Dinh | ndhcuong@ufm.edu.vn |

See [`AUTHORS.md`](AUTHORS.md) for full affiliations and the author
contributions statement.

## Overview

The study forecasts the daily Bitcoin price by decomposing the series before
learning, rather than fitting a single model to the raw series. Daily OHLCV data
covering 2014–2025 is split into chronological development, validation and test
blocks, then decomposed with **STL** or **robust STL (rSTL)** at a period of 30
days. Separate deep learners — **TCN**, **N-BEATS** and **GRU** — are fitted to
the trend, seasonal and remainder components. Their forecasts are combined by a
validation-guided rule (`Auto` selection, `EnsAvg` simple averaging, `EnsWgt`
weighted averaging), the components are reconstructed, the log transform is
inverted, and the result is evaluated at horizons of **1, 7, 14 and 28 days**
using RMSE, MAPE, *R*² and directional accuracy.

The pipeline is summarised in [`figures/Figure_1.png`](figures/Figure_1.png).

### Headline result

Decomposition is what separates the two groups of models. At *h* = 28 days the
non-decomposed benchmarks reach an RMSE of roughly 10,500–11,800 USD, while
every STL- and rSTL-based model stays between about 4,200 and 6,100 USD; the
proposed ensembles are the strongest of these (STL-Auto: 4,219 USD). Metrics are
means over ten random seeds on a 365-day test period, with Model Confidence Set
membership reported at alpha = 0.10. Full numbers:
[`tables/Table_3.md`](tables/Table_3.md).

## Repository structure

```
.
├── code/
│   ├── decomposition_ensemble_experiments.ipynb   Full experiment, outputs intact
│   └── extract_notebook_results.py                Notebook outputs -> results/*.csv
├── data/
│   ├── raw/BTC_USD_daily_2014-09-17_2025-06-11.csv   3,921 daily records
│   └── processed/                                 Derived deterministically; not stored
├── figures/        Figures 1-4, publication resolution
├── results/        RMSE / MAPE / R2 matrices, MCS, Diebold-Mariano, Wilcoxon
├── tables/         Table 3 (.docx and Markdown)
├── docs/           PeerJ submission checklist
├── AUTHORS.md      Authors, affiliations, contributions
├── CITATION.cff    Machine-readable citation metadata
├── LICENSE         MIT - applies to source code
├── LICENSE-DATA.md CC BY 4.0 - applies to data, figures, tables, results
└── requirements.txt
```

Every directory carries its own README describing its contents in detail.

| | |
| :--- | :--- |
| **Data** | [`data/raw/`](data/README.md) — daily Bitcoin OHLCV, 2014-09-17 to 2025-06-11, 3,921 records, no missing values or duplicate dates. |
| **Code** | [`code/`](code/README.md) — the notebook that produced the published results (Google Colab, TensorFlow 2.20.0, T4 GPU), committed with its cell outputs intact. |
| **Results** | [`results/`](results/README.md) — the result tables behind Table 3 and Figures 2–4, as CSV. |
| **Figures** | [`figures/`](figures/README.md) — Figures 1–4 exactly as supplied in the submission package. |
| **Tables** | [`tables/`](tables/) — `Table_3.docx` plus a Markdown rendering. |

### Verification

`results/RMSE_mean_matrix.csv` was checked against
[`tables/Table_3.md`](tables/Table_3.md) value by value: **75 of the 76 values
agree exactly**. The single exception is a rounding slip in the manuscript —
STL-ARIMA-LSTM at *h* = 14 computes to 3,249.4973, which rounds to 3,249, but
Table 3 prints 3,250. The Model Confidence Sets in `results/MCS_h*.csv` reproduce
the † markers of Table 3 exactly at all four horizons.

### Still to add before submission

| Item | Notes |
| :--- | :--- |
| Tables 1, 2 and any others | Only Table 3 was present in the submission package. |
| Per-seed metrics and test-period predictions | Written by the notebook to its Drive output folder during the run; see [`results/README.md`](results/README.md). |
| Data provenance statement | Source and retrieval date of the raw series; see [`data/README.md`](data/README.md). |
| Zenodo DOI | GitHub is not a permanent archive; see [`docs/peerj-submission-checklist.md`](docs/peerj-submission-checklist.md). |

## Reproducing the results

```bash
git clone https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting.git
cd Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook code/decomposition_ensemble_experiments.ipynb
```

The notebook was written for Google Colab and reads from Google Drive. To run it
against this repository, point `CONFIG['DATA_DIR']` at `data/raw/` and
`CONFIG['OUT_DIR']` at `results/`, and skip the `drive.mount` cell.
[`code/README.md`](code/README.md) documents the configuration in full.

A complete run covers ten seeds × three architectures × three components × two
decompositions and takes hours of GPU time. To read the published numbers without
re-running anything, open the committed notebook — its outputs are intact — or
the CSVs in [`results/`](results/README.md).

## Licence

- **Source code** — [MIT](LICENSE).
- **Data, figures, tables and results** — [CC BY 4.0](LICENSE-DATA.md), the
  licence PeerJ applies to published content.

## How to cite

Citation metadata is in [`CITATION.cff`](CITATION.cff). Update it with the DOI,
volume and page numbers once the article is published.

> Tran Thai H, Manh Le T, Nguyen-Dinh CH. Decomposition Ensembles for Bitcoin
> Price Forecasting. Submitted to *PeerJ Computer Science*.
