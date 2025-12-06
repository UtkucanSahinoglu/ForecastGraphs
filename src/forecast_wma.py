import numpy as np
import pandas as pd
from src.plot_utils import academic_plot


def weighted_moving_average(ts, window=5):
    weights = np.arange(1, window + 1)
    return ts.rolling(window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)


def wma_forecast(ts, window=5, steps=20, player_name="Player"):
    wma_series = weighted_moving_average(ts, window)
    last_value = wma_series.dropna().iloc[-1]

    future_idx = pd.date_range(ts.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast = pd.Series([last_value] * steps, index=future_idx)

    academic_plot(ts, wma_series, forecast, player_name, method=f"WMA-{window}")
