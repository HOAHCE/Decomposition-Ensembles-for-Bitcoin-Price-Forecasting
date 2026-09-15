# Table 5: Mean absolute percentage error across forecast horizons

| Model | h = 1 day (%) | h = 7 days (%) | h = 14 days (%) | h = 28 days (%) |
| :--- | :-: | :-: | :-: | :-: |
| **Benchmarks without decomposition** | | | | |
| ARIMA | 1.86 | 4.89 | 7.20 | 9.70 |
| RW-drift | 1.87 | 4.91 | 7.26 | 9.69 |
| GRU (direct) | 1.89 | 5.05 | 7.56 | 10.27 |
| TCN (direct) | 1.88 | 4.99 | 7.35 | 9.87 |
| N-BEATS (direct) | 2.08 | 5.42 | 7.86 | 10.76 |
| **STL with one architecture** | | | | |
| STL-TCN | 1.88 | 2.52† | 2.50 | 4.50† |
| STL-N-BEATS | 2.24 | 2.66† | 2.56† | 5.75 |
| STL-GRU | 1.88 | 2.71 | 2.47 | 3.84† |
| **STL with deep ensemble (proposed)** | | | | |
| STL-Auto | **1.79†** | 2.60† | 2.28 | 3.85† |
| STL-EnsWgt | 1.81 | 2.43† | 2.13 | 3.91† |
| STL-EnsAvg | 1.81 | 2.43† | **2.13** | 3.93† |
| **STL with classical hybrid** | | | | |
| STL-ARIMA-LSTM | 2.52 | 3.14 | 2.64† | **3.33†** |
| **rSTL with one architecture** | | | | |
| rSTL-TCN | 2.30 | 2.43 | 2.49 | 4.65 |
| rSTL-N-BEATS | 2.65 | 2.56† | 2.79 | 5.58 |
| rSTL-GRU | 2.13 | 2.94 | 2.87 | 4.65† |
| **rSTL with deep ensemble (proposed)** | | | | |
| rSTL-Auto | 1.93† | 2.54 | 2.17 | 4.27† |
| rSTL-EnsWgt | 1.96 | 2.35 | 2.37 | 4.34 |
| rSTL-EnsAvg | 1.97 | **2.35** | 2.37 | 4.34 |
| **rSTL with classical hybrid** | | | | |
| rSTL-ARIMA-LSTM | 2.62 | 2.89 | 2.77† | 4.55† |

Values are means over ten random seeds during the 365-day test period. Bold indicates the lowest value in a column; † indicates membership in the Model Confidence Set (alpha = 0.10).

---

Plain-text rendering of [`Table_5.docx`](Table_5.docx), provided for readability
and diffability. **The `.docx` is the authoritative version.**
