import pandas as pd
from src.plot_utils import academic_forecast_plot


def moving_average_forecast(ts, window=14, steps=20, player_name="Player"):
    """
    Simple Moving Average (MA) forecast.
    """

    ma = ts.rolling(window=window).mean().dropna()

    if ma.empty:
        print("Not enough data to compute Moving Average.")
        return None

    last_value = ma.iloc[-1]

    future_idx = pd.date_range(ts.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast = pd.Series([last_value] * steps, index=future_idx)

    explanation = (
        f"MA-{window} smooths out short-term fluctuations\n"
        f"by averaging the last {window} observations, highlighting the trend."
    )

    academic_forecast_plot(ts, ma, forecast, player_name, f"Moving Average (MA-{window})", explanation)
    return forecast
