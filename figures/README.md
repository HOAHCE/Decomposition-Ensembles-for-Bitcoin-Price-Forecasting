# Figures

Publication-resolution figures for the manuscript, exactly as supplied in the
PeerJ submission package. All files are PNG with an alpha channel.

| File | Dimensions (px) | Caption |
| :--- | :--- | :--- |
| [`Figure_1.png`](Figure_1.png) | 3634 × 2134 | Overview of the forecasting pipeline: daily Bitcoin OHLCV (2014–2025) → chronological development, validation and test blocks → STL or rSTL decomposition (period = 30 days) → trend, seasonal and remainder learners (TCN / N-BEATS / GRU) → validation-guided selection and forecast combination (Auto / EnsAvg / EnsWgt) → component reconstruction and inverse log transform → horizon-specific evaluation at *h* = 1, 7, 14, 28 days with RMSE / MAPE / *R*² / DA. |
| [`Figure_2.png`](Figure_2.png) | 3034 × 1894 | Coefficient of determination (*R*²) as a function of forecast horizon for the proposed decomposition ensembles (STL-Auto, STL-EnsWgt, rSTL-EnsAvg) against the classical hybrid (STL-ARIMA-LSTM) and the non-decomposed benchmarks (ARIMA, TCN direct). |
| [`Figure_3.png`](Figure_3.png) | 3034 × 1894 | RMSE in USD by forecast horizon (*h* = 1, 7, 14, 28), grouped bar chart over the same six models. |
| [`Figure_4.png`](Figure_4.png) | 3034 × 1894 | MAPE (%) as a function of forecast horizon for the same six models. |

The captions above are descriptive summaries written from the figure content.
Replace them with the final caption text of the manuscript before submission so
that the repository and the article agree word for word.
