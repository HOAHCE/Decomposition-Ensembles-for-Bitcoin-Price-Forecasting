# Results

Result tables from the run that produced Table 3 and Figures 2–4 of the
manuscript. They were extracted from the stored cell outputs of
[`../code/decomposition_ensemble_experiments.ipynb`](../code/decomposition_ensemble_experiments.ipynb)
by [`../code/extract_notebook_results.py`](../code/extract_notebook_results.py),
and carry the same file names the notebook itself writes when it runs.

All values are computed over the 365-day test period and averaged over ten
random seeds (42–51). Model names follow the notebook's convention:
`RobustSTL-…` is the manuscript's `rSTL-…`, and `NBEATS` is `N-BEATS`.

| File | Contents |
| :--- | :--- |
| `RMSE_mean_matrix.csv` | Mean RMSE (USD), 19 models × 4 horizons. **This is the source of Table 3.** |
| `MAPE_mean_matrix.csv` | Mean MAPE (%), 19 models × 4 horizons. Source of Figure 4. |
| `R2_mean_matrix.csv` | Mean *R*², 19 models × 4 horizons. Source of Figure 2. |
| `MCS_h1.csv`, `MCS_h7.csv`, `MCS_h14.csv`, `MCS_h28.csv` | Model Confidence Set *p*-values per horizon (alpha = 0.10). Models with *p* ≥ 0.10 are in the confidence set and carry the † marker in Table 3. |
| `DM_seedavg.csv` | Diebold–Mariano tests of the best proposed model against each baseline, on seed-averaged forecasts. |
| `wilcoxon_seed.csv` | Across-seed Wilcoxon / *t*-tests, proposed models against baselines (30 comparisons; 85% significant at *p* < 0.05). |
| `best_per_horizon.csv` | Winning model at each horizon, with RMSE (mean ± std), *R*², MAPE, DA, MCS membership and the Wilcoxon *p*-value against the strongest baseline. |
| `overall_rank.csv` | Scale-free average rank by RMSE across horizons, top 8 models. |

## Consistency with Table 3

Tables 3, 4 and 5 were checked cell by cell against `RMSE_mean_matrix.csv`,
`R2_mean_matrix.csv` and `MAPE_mean_matrix.csv`: **all 228 values agree exactly**
after rounding, and **all 228 † markers** match the confidence sets in
`MCS_h*.csv`.

One correction was applied to the table files: STL-ARIMA-LSTM at *h* = 14
computes to 3,249.4973, which rounds to **3,249**, but earlier drafts printed
**3,250**. The manuscript text needs the same correction.

## Not included

Two tables the notebook produces were truncated by pandas' display limit before
the notebook was saved, so they cannot be recovered from it:

- `aggregate_mean_std.csv` — per-model, per-horizon metrics **with standard
  deviations** (76 rows).
- `seed_averaged_metrics.csv` — metrics of the seed-averaged forecasts (76 rows).

Also absent are the per-seed metric files (`metrics_seed42.csv` … `metrics_seed51.csv`)
and the test-period predictions, which the notebook writes to its output folder
during the run. If those files still exist in the authors' Drive folder
(`3-results_v4/`), adding them here would make the deposit complete; otherwise
re-running the notebook regenerates all of them.
