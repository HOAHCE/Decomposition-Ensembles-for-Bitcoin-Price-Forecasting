# Table 4: Coefficient of determination across forecast horizons

| Model | h = 1 day | h = 7 days | h = 14 days | h = 28 days |
| :--- | :-: | :-: | :-: | :-: |
| **Benchmarks without decomposition** | | | | |
| ARIMA | 0.9852 | 0.9125 | 0.8159 | 0.5821 |
| RW-drift | 0.9852 | 0.9138 | 0.8216 | 0.6140 |
| GRU (direct) | 0.9850 | 0.9085 | 0.8038 | 0.5705 |
| TCN (direct) | 0.9851 | 0.9120 | 0.8161 | 0.6007 |
| N-BEATS (direct) | 0.9825 | 0.8959 | 0.7852 | 0.5199 |
| **STL with one architecture** | | | | |
| STL-TCN | 0.9878 | 0.9792† | 0.9786 | 0.9198† |
| STL-N-BEATS | 0.9826 | 0.9761† | 0.9762† | 0.8710 |
| STL-GRU | 0.9870 | 0.9757 | 0.9784 | 0.9373† |
| **STL with deep ensemble (proposed)** | | | | |
| STL-Auto | **0.9888†** | 0.9777† | 0.9810 | **0.9378†** |
| STL-EnsWgt | 0.9887 | 0.9810† | **0.9845** | 0.9378† |
| STL-EnsAvg | 0.9886 | 0.9810† | 0.9845 | 0.9373† |
| **STL with classical hybrid** | | | | |
| STL-ARIMA-LSTM | 0.9785 | 0.9677 | 0.9646† | 0.9039† |
| **rSTL with one architecture** | | | | |
| rSTL-TCN | 0.9812 | 0.9798 | 0.9780 | 0.9167 |
| rSTL-N-BEATS | 0.9750 | 0.9768† | 0.9724 | 0.8742 |
| rSTL-GRU | 0.9839 | 0.9712 | 0.9704 | 0.9151† |
| **rSTL with deep ensemble (proposed)** | | | | |
| rSTL-Auto | 0.9867† | 0.9781 | 0.9830 | 0.9286† |
| rSTL-EnsWgt | 0.9864 | **0.9814** | 0.9805 | 0.9252 |
| rSTL-EnsAvg | 0.9863 | 0.9814 | 0.9805 | 0.9250 |
| **rSTL with classical hybrid** | | | | |
| rSTL-ARIMA-LSTM | 0.9765 | 0.9710 | 0.9587† | 0.8970† |

Values are means over ten random seeds during the 365-day test period. Bold indicates the highest value in a column; † indicates membership in the Model Confidence Set (alpha = 0.10).

---

Plain-text rendering of [`Table_4.docx`](Table_4.docx), provided for readability
and diffability. **The `.docx` is the authoritative version.**
