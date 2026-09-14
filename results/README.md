# Results

> **Status: not yet deposited.** The submission package contained the rendered
> figures and Table 3, but not the underlying numerical results. This directory
> must be populated before submission.

## What to add here

- The per-seed, per-model, per-horizon metric values (RMSE, MAPE, *R*², DA) as
  machine-readable CSV — that is, the numbers behind
  [`../tables/Table_3.md`](../tables/Table_3.md) and Figures 2–4, before they
  were averaged over the ten seeds.
- The Model Confidence Set output (alpha = 0.10) that determines the † markers
  in Table 3.
- The test-period predictions of each model, so the error metrics can be
  recomputed without retraining.
- The remaining tables of the manuscript (Table 1, Table 2, …). Only Table 3 was
  present in the submission package.

Prefer open, text-based formats (CSV, JSON) over spreadsheets or pickles so that
the values are diffable and readable without proprietary software.
