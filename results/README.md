# Results

Machine-readable results behind Tables 1 and 3–7 and Figures 2–5. All forecast
metrics are computed over the 365-day test period (2024-06-12 to 2025-06-11).
Seed statistics use ten random seeds (42–51).

The files except `descriptive_statistics.csv` were exported from the stored
outputs of the published notebook run by
[`../code/extract_notebook_results.py`](../code/extract_notebook_results.py).
Because they come from the notebook's displayed tables, values carry the four
decimal places shown there. A fresh run of the notebook writes the same files, at
full precision, to `outputs/`.

Model names follow the code: `RobustSTL-…` is the article's `rSTL-…`, `NBEATS`
is `N-BEATS`, and `TCN(direct)` is `TCN (direct)`.

| File | Contents | Used for |
| :--- | :--- | :--- |
| `descriptive_statistics.csv` | Mean, SD, min, max, skewness, excess kurtosis, ADF and KPSS p-values of Close, ln(Close) and the log return (written by `code/descriptive_statistics.py`). | Table 1 |
| `RMSE_mean_matrix.csv` | Mean RMSE (USD) across seeds; 19 models × 4 horizons. | Table 3, Figures 3 and 5 |
| `R2_mean_matrix.csv` | Mean R² across seeds; 19 models × 4 horizons. | Table 4, Figure 2 |
| `MAPE_mean_matrix.csv` | Mean MAPE (%) across seeds; 19 models × 4 horizons. | Table 5, Figure 4 |
| `MCS_h1.csv`, `MCS_h7.csv`, `MCS_h14.csv`, `MCS_h28.csv` | Model Confidence Set p-values per horizon, from the squared errors of the seed-averaged forecasts. Models with p ≥ 0.10 belong to the confidence set. | † markers in Tables 3–5; Table 6 |
| `best_per_horizon.csv` | Leading model per horizon (lowest mean RMSE) with RMSE mean ± SD, R², MAPE, DA, MCS membership and the Wilcoxon test against the strongest benchmark. | Table 6 |
| `DM_seedavg.csv` | Diebold–Mariano tests (Harvey–Leybourne–Newbold correction) of STL-Auto against each undecomposed benchmark, on seed-averaged forecasts. | Table 7 |
| `wilcoxon_seed_excerpt.csv` | One-sided Wilcoxon signed-rank tests across seeds, proposed vs. benchmark: the 30 rows displayed in the notebook (STL-TCN, STL-NBEATS and STL-GRU at h = 1 and 28). Across all 280 comparisons, 85% are significant at p < 0.05. | Supporting evidence |
| `overall_rank.csv` | Average rank by RMSE across the four horizons (scale-free), top eight models. | Supporting evidence |

## Column dictionary

| Column | Meaning |
| :--- | :--- |
| `Model` / `Model name` | Model specification (code naming, see above) |
| `1`, `7`, `14`, `28` | Forecast horizon h in days |
| `Pvalue` | MCS p-value |
| `h` | Forecast horizon (days) |
| `Leader` | Model with the lowest mean RMSE at that horizon |
| `RMSE` | Mean ± standard deviation of RMSE across seeds (USD) |
| `R2`, `MAPE`, `DA` | Mean R², MAPE (%) and directional accuracy (%) of the leader |
| `in_MCS` | Whether the leader belongs to the 90% Model Confidence Set |
| `vs_baseline` | Strongest undecomposed benchmark at that horizon |
| `Wilcoxon_p`, `beats_baseline` | Wilcoxon p-value of the leader vs. that benchmark, and whether p < 0.05 |
| `Top3` | Three best models with their mean RMSE (truncated in the notebook display) |
| `Proposed`, `Baseline` | Compared models |
| `DM`, `p` | Diebold–Mariano statistic (negative = proposed model more accurate) and two-sided p-value |
| `Conclusion` | `proposed better`, `baseline better` or `no difference` at the 5% level |
| `test_type` | `one-sample` (deterministic benchmark: ARIMA, RW-drift) or `paired` (stochastic benchmark) |
| `RMSE_mean`, `RMSE_std`, `base_RMSE` | Proposed model's mean and SD of RMSE across seeds; benchmark RMSE |
| `wilcoxon_p`, `significant` | Wilcoxon p-value and whether p < 0.05 |
| `avg_rank`, `avg_RMSE` | Mean rank and mean RMSE across the four horizons |

## Files produced only by a full re-run

Two tables were longer than the notebook's display limit and are therefore not
included here: `aggregate_mean_std.csv` (all metrics with standard deviations,
76 rows) and `seed_averaged_metrics.csv` (metrics of the seed-averaged forecasts,
76 rows). The per-seed files `metrics_seed42.csv` … `metrics_seed51.csv`, the full
`wilcoxon_seed.csv` (280 rows) and the diagnostic plots are also written to
`outputs/` when the notebook runs.

## Checking the tables

```bash
python code/verify_tables.py
```

compares every value, † marker, bold best value and significance star in
Tables 1 and 3–7 with the files above (305 checks).
