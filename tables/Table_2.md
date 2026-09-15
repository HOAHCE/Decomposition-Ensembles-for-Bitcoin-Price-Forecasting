# Table 2: Common experimental configuration

| Item | Setting |
| :--- | :-: |
| Input window | 60 daily time steps |
| Forecast outputs | H = 28; evaluated at h = 1, 7, 14, and 28 days |
| Deep component library | TCN, N-BEATS, and GRU |
| Classical hybrid learner | ARIMA for trend; LSTM for seasonal and remainder components |
| TCN dilation factors | 1, 2, 4, and 8 |
| N-BEATS stack | Three doubly residual blocks |
| GRU and LSTM depth | Two recurrent layers |
| Optimizer and learning rate | Adam; 0.001 |
| Batch size and training cap | 32; 100 epochs |
| Early stopping | Patience of 12 epochs |
| Stochastic replications | Ten seeds (42-51) |

ARIMA: autoregressive integrated moving average; GRU: gated recurrent unit; LSTM: long short-term memory; N-BEATS: neural basis expansion analysis for interpretable time-series forecasting; TCN: temporal convolutional network.

---

Plain-text rendering of [`Table_2.docx`](Table_2.docx), provided for readability
and diffability. **The `.docx` is the authoritative version.**
