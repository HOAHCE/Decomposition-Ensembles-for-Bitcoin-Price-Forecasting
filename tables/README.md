# Tables

Tables 1–7 of the article as editable Word files in PeerJ format (`.docx`, the
authoritative versions) with plain-text Markdown renderings (`.md`) for reading
on GitHub.

| Table | Caption | Source of the values |
| :--- | :--- | :--- |
| [Table 1](Table_1.md) ([docx](Table_1.docx)) | Descriptive statistics and stationarity diagnostics for the Bitcoin series | `code/descriptive_statistics.py` → `results/descriptive_statistics.csv` |
| [Table 2](Table_2.md) ([docx](Table_2.docx)) | Common experimental configuration | `CONFIG` cell and model builders of the notebook |
| [Table 3](Table_3.md) ([docx](Table_3.docx)) | Root mean squared error across forecast horizons | `results/RMSE_mean_matrix.csv`; † from `results/MCS_h*.csv` |
| [Table 4](Table_4.md) ([docx](Table_4.docx)) | Coefficient of determination across forecast horizons | `results/R2_mean_matrix.csv`; † from `results/MCS_h*.csv` |
| [Table 5](Table_5.md) ([docx](Table_5.docx)) | Mean absolute percentage error across forecast horizons | `results/MAPE_mean_matrix.csv`; † from `results/MCS_h*.csv` |
| [Table 6](Table_6.md) ([docx](Table_6.docx)) | Leading model at each forecast horizon | `results/best_per_horizon.csv` |
| [Table 7](Table_7.md) ([docx](Table_7.docx)) | Diebold-Mariano tests of STL-Auto against undecomposed benchmarks | `results/DM_seedavg.csv` |

In Tables 3–5, values are means over ten random seeds during the 365-day test
period, bold marks the best value in each column, and † marks membership in the
Model Confidence Set (α = 0.10). In Table 7, \*\*\* p < 0.01 and \*\* p < 0.05.

## Verification

```bash
python code/verify_tables.py
```

checks every number, † marker, bold value, leading model and significance star of
Tables 1 and 3–7 against the computed results (305 checks; all pass). The script
needs `python-docx` (listed in `requirements.txt`).

Note on rounding: STL-ARIMA-LSTM at h = 14 in Table 3 computes to 3,249.4973 USD
and is printed as **3,249**.
