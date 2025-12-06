import numpy as np
import pandas as pd
from src.plot_utils import academic_forecast_plot


def weighted_moving_average_series(ts, window=5):
    """
    Computes Weighted Moving Average (WMA) series.
    """

    weights = np.arange(1, window + 1)
    wma = ts.rolling(window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    return wma.dropna()


def wma_forecast(ts, window=5, steps=20, player_name="Player"):
    """
    Weighted Moving Average forecast.
    """

    wma_series = weighted_moving_average_series(ts, window=window)

    if wma_series.empty:
        print("Not enough data to compute Weighted Moving Average.")
        return None

    last_value = wma_series.iloc[-1]

    future_idx = pd.date_range(ts.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast = pd.Series([last_value] * steps, index=future_idx)

    explanation = (
        f"WMA-{window} assigns higher weights to recent data,\n"
        f"making the model more responsive to recent changes."
    )

    academic_forecast_plot(ts, wma_series, forecast, player_name, f"Weighted Moving Average (WMA-{window})", explanation)
    return forecast
