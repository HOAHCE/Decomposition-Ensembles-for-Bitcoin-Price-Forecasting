# Table 3: Root mean squared error across forecast horizons

| Model | h = 1 day (USD) | h = 7 days (USD) | h = 14 days (USD) | h = 28 days (USD) |
| :-: | :-: | :-: | :-: | :-: |
| **Benchmarks without decomposition** |  |  |  |  |
| ARIMA | 2,105 | 5,122 | 7,418 | 10,986 |
| RW-drift | 2,103 | 5,082 | 7,301 | 10,558 |
| GRU (direct) | 2,115 | 5,226 | 7,634 | 11,080 |
| TCN (direct) | 2,112 | 5,135 | 7,413 | 10,737 |
| N-BEATS (direct) | 2,287 | 5,582 | 8,010 | 11,773 |
| **STL with one architecture** |  |  |  |  |
| STL-TCN | 1,902 | 2,496† | 2,528 | 4,809† |
| STL-N-BEATS | 2,203 | 2,616† | 2,637† | 6,098 |
| STL-GRU | 1,972 | 2,696 | 2,536 | 4,240† |
| **STL with deep ensemble (proposed)** |  |  |  |  |
| STL-Auto | 1,821† | 2,569† | 2,381 | 4,219† |
| STL-EnsWgt | 1,833 | 2,380† | 2,153 | 4,238† |
| STL-EnsAvg | 1,836 | 2,380† | 2,153 | 4,253† |
| **STL with classical hybrid** |  |  |  |  |
| STL-ARIMA-LSTM | 2,530 | 3,099 | 3,250† | 5,269† |
| **rSTL with one architecture** |  |  |  |  |
| rSTL-TCN | 2,308 | 2,451 | 2,557 | 4,905 |
| rSTL-N-BEATS | 2,653 | 2,609† | 2,850 | 6,017 |
| rSTL-GRU | 2,191 | 2,917 | 2,894 | 4,930† |
| **rSTL with deep ensemble (proposed)** |  |  |  |  |
| rSTL-Auto | 1,983† | 2,547 | 2,246 | 4,536† |
| rSTL-EnsWgt | 2,001 | 2,361 | 2,397 | 4,645 |
| rSTL-EnsAvg | 2,008 | 2,359 | 2,396 | 4,651 |
| **rSTL with classical hybrid** |  |  |  |  |
| rSTL-ARIMA-LSTM | 2,640 | 2,928 | 3,508† | 5,452† |

Values are means over ten random seeds during the 365-day test period. Bold
indicates the lowest value in a column; † indicates membership in the Model
Confidence Set (alpha = 0.10).

---

This Markdown file is a plain-text rendering of [`Table_3.docx`](Table_3.docx),
provided for readability and diffability. **`Table_3.docx` is the authoritative
version**: the bold highlighting of the best value per column is preserved there
but is not reproduced in the row values above (only the group headings are bold
here).
