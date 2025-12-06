import pandas as pd
import matplotlib.pyplot as plt
from src.plot_utils import academic_plot


def moving_average_forecast(ts, window=14, steps=20, player_name="Player"):
    ma = ts.rolling(window=window).mean()
    last_value = ma.dropna().iloc[-1]

    future_idx = pd.date_range(ts.index[-1] + pd.Timedelta(days=1),
                               periods=steps)
    forecast = pd.Series([last_value] * steps, index=future_idx)

    academic_plot(ts, ma, forecast, player_name, method=f"MA-{window}")
