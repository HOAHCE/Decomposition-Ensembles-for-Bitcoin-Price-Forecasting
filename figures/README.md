# Figures

Figures 1–5 of the article. All files are PNG.

| File | Size (px) | Caption |
| :--- | :--- | :--- |
| [`Figure_1.png`](Figure_1.png) | 3634 × 2134 | **Validation-guided decomposition and ensemble forecasting workflow.** Daily Bitcoin observations are partitioned chronologically, decomposed into trend, seasonal, and remainder components, and modeled with direct multi-output learners. Validation results determine component selection or ensemble weights before price reconstruction and horizon-specific evaluation. |
| [`Figure_2.png`](Figure_2.png) | 3034 × 1894 | **Coefficient of determination across forecast horizons.** Colored lines represent decomposition-based models; gray lines represent undecomposed benchmarks. Markers and line styles retain the distinction when reproduced in grayscale. |
| [`Figure_3.png`](Figure_3.png) | 3034 × 1894 | **Root mean squared error across forecast horizons.** Bars compare the proposed ensembles with representative classical and undecomposed deep-learning benchmarks. Hatching preserves model distinctions in grayscale. |
| [`Figure_4.png`](Figure_4.png) | 3034 × 1894 | **Mean absolute percentage error across forecast horizons.** The figure highlights the divergence between the model that minimizes proportional error and the models that minimize absolute-scale error at longer horizons. |
| [`Figure_5.png`](Figure_5.png) | 1875 × 1170 | **Root mean squared error reduction relative to autoregressive integrated moving average.** Positive values indicate the percentage reduction achieved by each decomposition ensemble at the corresponding forecast horizon. |

## Data behind the figures

| Figure | Data | Models shown |
| :--- | :--- | :--- |
| 2 | `results/R2_mean_matrix.csv` | STL-Auto, STL-EnsWgt, rSTL-EnsAvg, STL-ARIMA-LSTM, ARIMA, TCN (direct) |
| 3 | `results/RMSE_mean_matrix.csv` | same six models |
| 4 | `results/MAPE_mean_matrix.csv` | same six models |
| 5 | `results/RMSE_mean_matrix.csv`, as 100 × (1 − RMSE / RMSE<sub>ARIMA</sub>) | STL-Auto, STL-EnsWgt, rSTL-EnsAvg |

Figure 1 is a schematic of the workflow and has no underlying data.

## Redrawing Figures 2–5

```bash
python code/make_figures.py                      # from the published results/
python code/make_figures.py --results outputs    # from a fresh notebook run
```

The script writes `Figure_2.png` … `Figure_5.png` to `outputs/figures/` at
300 dpi, in the same layout as the published figures, and never overwrites the
files in this folder.
