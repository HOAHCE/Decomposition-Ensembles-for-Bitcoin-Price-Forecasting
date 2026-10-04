# Table 6: Leading model at each forecast horizon

| h (days) | Leading model | RMSE (USD) | R² | MAPE (%) | DA (%) | In MCS |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| 1 | STL-Auto | 1,821 ± 129 | 0.9888 | 1.79 | 64.7 | Yes |
| 7 | rSTL-EnsAvg | 2,359 ± 121 | 0.9814 | 2.35 | 83.7 | No |
| 14 | STL-EnsAvg | 2,153 ± 102 | 0.9845 | 2.13 | 90.9 | No |
| 28 | STL-Auto | 4,219 ± 420 | 0.9378 | 3.85 | 88.3 | Yes |

The leading model minimizes seed-averaged RMSE at each horizon. MCS membership is evaluated using the seed-averaged forecast. DA: directional accuracy; MAPE: mean absolute percentage error; MCS: Model Confidence Set; RMSE: root mean squared error.

---

Plain-text rendering of [`Table_6.docx`](Table_6.docx), provided for readability
and diffability. **The `.docx` is the authoritative version.**
