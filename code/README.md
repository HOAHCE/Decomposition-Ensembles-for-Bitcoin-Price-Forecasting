# Code

> **Status: not yet deposited.** The
> `PeerJ_Computer_Science_Submission_Package` folder this repository was built
> from contained only `Figures/`, `Tables/` and an empty `Supplemental/` folder.
> No analysis code was present, so nothing could be copied here. PeerJ requires
> that code be made available, so this directory must be populated before the
> manuscript is submitted.

## What to add here

Everything needed for a third party to regenerate the figures, tables and
results from the raw data, organised to match the pipeline in
[`../figures/Figure_1.png`](../figures/Figure_1.png):

| Suggested module | Responsibility |
| :--- | :--- |
| `data_prep.py` | Load daily Bitcoin OHLCV (2014–2025), log-transform, build the chronological development / validation / test blocks. |
| `decomposition.py` | STL and robust STL decomposition with period = 30 days. |
| `models.py` | Component learners: TCN, N-BEATS, GRU; plus the ARIMA, RW-drift and ARIMA-LSTM baselines. |
| `ensemble.py` | Validation-guided selection (`Auto`) and forecast combination (`EnsAvg`, `EnsWgt`). |
| `evaluate.py` | Component reconstruction, inverse log transform, and the RMSE / MAPE / *R*² / DA metrics at *h* = 1, 7, 14, 28. |
| `mcs.py` | Model Confidence Set procedure (alpha = 0.10) reported in Table 3. |
| `make_figures.py` | Regenerate `figures/Figure_1.png` … `Figure_4.png`. |
| `run_all.py` | Single entry point that reproduces every reported number end to end. |

## Reproducibility requirements

- Fix and document the ten random seeds used for the seed-averaged results.
- Pin exact package versions in [`../requirements.txt`](../requirements.txt).
- Record hardware, CPU/GPU and total runtime in the top-level `README.md`.
- Make `run_all.py` write its outputs into `../results/`, not into this folder.
