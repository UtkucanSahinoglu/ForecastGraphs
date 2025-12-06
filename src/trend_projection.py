import numpy as np
import pandas as pd
from src.plot_utils import academic_forecast_plot


def trend_projection_forecast(ts, steps=20, player_name="Player"):
    """
    Trend Projection Method using simple linear regression:
    Ŷ = a + b * t
    """

    ts_daily = ts.asfreq("D").fillna(0)
    n = len(ts_daily)
    t = np.arange(1, n + 1)

    # polyfit: slope b, intercept a
    b, a = np.polyfit(t, ts_daily.values, deg=1)

    fitted = a + b * t

    t_future = np.arange(n + 1, n + steps + 1)
    forecast_values = a + b * t_future

    future_dates = pd.date_range(ts_daily.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast = pd.Series(forecast_values, index=future_dates)

    fitted_series = pd.Series(fitted, index=ts_daily.index)

    explanation = (
        "Trend Projection fits a straight line Ŷ = a + bt\n"
        "and extrapolates it into future periods."
    )

    academic_forecast_plot(ts_daily, fitted_series, forecast, player_name, "Trend Projection (Linear)", explanation)
    return forecast
