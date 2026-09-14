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
├── code/           Analysis code                    (to be deposited — see below)
├── data/
│   ├── raw/        Daily Bitcoin OHLCV, 2014–2025   (to be deposited — see below)
│   └── processed/  Decompositions and splits        (to be deposited — see below)
├── figures/        Figures 1–4, publication resolution
├── results/        Per-seed metrics and predictions (to be deposited — see below)
├── tables/         Table 3 (.docx and Markdown)
├── docs/           PeerJ submission checklist
├── AUTHORS.md      Authors, affiliations, contributions
├── CITATION.cff    Machine-readable citation metadata
├── LICENSE         MIT — applies to source code
├── LICENSE-DATA.md CC BY 4.0 — applies to data, figures, tables, results
└── requirements.txt
```

## Current contents and what is still missing

This repository was populated from the
`PeerJ_Computer_Science_Submission_Package` Google Drive folder. That folder
contained **only** `Figures/` (four PNGs), `Tables/` (`Table_3.docx`) and an
empty `Supplemental/` folder. Everything it held is here, unmodified:

| Present | |
| :--- | :--- |
| `figures/Figure_1.png` … `Figure_4.png` | Verbatim copies, with captions in [`figures/README.md`](figures/README.md) |
| `tables/Table_3.docx` | Verbatim copy, plus a Markdown rendering |

**Not yet present**, and required by PeerJ before the article can be published:

| Missing | Where it goes |
| :--- | :--- |
| Analysis code | [`code/`](code/README.md) |
| Raw and processed data | [`data/`](data/README.md) |
| Per-seed numerical results, MCS output, predictions | [`results/`](results/README.md) |
| Tables 1, 2 and any further tables | `tables/` |
| Supplemental files | `docs/` or a `supplemental/` folder |

Each of those directories contains a README describing exactly what to place
there. See [`docs/peerj-submission-checklist.md`](docs/peerj-submission-checklist.md)
for the full list of journal requirements.

## Reproducing the results

Once the code is deposited:

```bash
git clone https://github.com/HOAHCE/Decomposition-Ensembles-for-Bitcoin-Price-Forecasting.git
cd Decomposition-Ensembles-for-Bitcoin-Price-Forecasting
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python code/run_all.py
```

The versions in [`requirements.txt`](requirements.txt) are currently minimum
bounds inferred from the reported methods; they must be pinned to the exact
versions used before submission.

## Licence

- **Source code** — [MIT](LICENSE).
- **Data, figures, tables and results** — [CC BY 4.0](LICENSE-DATA.md), the
  licence PeerJ applies to published content.

## How to cite

Citation metadata is in [`CITATION.cff`](CITATION.cff). Update it with the DOI,
volume and page numbers once the article is published.

> Tran Thai H, Manh Le T, Nguyen-Dinh CH. Decomposition Ensembles for Bitcoin
> Price Forecasting. Submitted to *PeerJ Computer Science*.
