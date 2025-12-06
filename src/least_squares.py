import numpy as np
import pandas as pd
from src.plot_utils import academic_forecast_plot


def least_squares_forecast(ts, steps=20, player_name="Player"):
    """
    Least Squares Method for linear trend:
    Minimizes sum of squared errors for Ŷ = a + bt.
    """

    ts_daily = ts.asfreq("D").fillna(0)
    n = len(ts_daily)
    t = np.arange(1, n + 1)

    # slope b, intercept a
    b, a = np.polyfit(t, ts_daily.values, deg=1)

    fitted = a + b * t

    t_future = np.arange(n + 1, n + steps + 1)
    forecast_vals = a + b * t_future

    future_dates = pd.date_range(ts_daily.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast = pd.Series(forecast_vals, index=future_dates)

    fitted_series = pd.Series(fitted, index=ts_daily.index)

    explanation = (
        "Least Squares estimates a and b by minimizing\n"
        "the sum of squared deviations between Y and Ŷ."
    )

    academic_forecast_plot(ts_daily, fitted_series, forecast, player_name, "Least Squares Trend", explanation)
    return forecast
