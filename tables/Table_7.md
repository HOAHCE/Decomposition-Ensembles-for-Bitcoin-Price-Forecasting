# Table 7: Diebold-Mariano tests of STL-Auto against undecomposed benchmarks

| Benchmark | h = 1 day | h = 7 days | h = 14 days | h = 28 days |
| :--- | :-: | :-: | :-: | :-: |
| ARIMA | -4.83<sup>\*\*\*</sup> | -3.97<sup>\*\*\*</sup> | -3.17<sup>\*\*\*</sup> | -2.06<sup>\*\*</sup> |
| RW-drift | -4.89<sup>\*\*\*</sup> | -4.19<sup>\*\*\*</sup> | -3.63<sup>\*\*\*</sup> | -2.50<sup>\*\*</sup> |
| GRU (direct) | -4.97<sup>\*\*\*</sup> | -4.28<sup>\*\*\*</sup> | -4.04<sup>\*\*\*</sup> | -2.79<sup>\*\*\*</sup> |
| TCN (direct) | -4.96<sup>\*\*\*</sup> | -4.33<sup>\*\*\*</sup> | -3.80<sup>\*\*\*</sup> | -2.61<sup>\*\*\*</sup> |
| N-BEATS (direct) | -5.03<sup>\*\*\*</sup> | -4.21<sup>\*\*\*</sup> | -3.72<sup>\*\*\*</sup> | -2.54<sup>\*\*</sup> |

A negative statistic indicates that STL-Auto is more accurate than the benchmark. \*\*\* p < 0.01; \*\* p < 0.05 (two-sided Harvey-Leybourne-Newbold correction). Tests use squared-error loss differentials from the seed-averaged forecasts.

---

Plain-text rendering of [`Table_7.docx`](Table_7.docx), provided for readability
and diffability. **The `.docx` is the authoritative version.**
