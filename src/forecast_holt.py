import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from src.plot_utils import academic_plot


def holt_winters_forecast(ts, steps=20, player_name="Player"):
    ts = ts.asfreq('D').fillna(0)

    model = ExponentialSmoothing(
        ts,
        trend="add",
        seasonal=None,
        initialization_method="estimated"
    )

    fit = model.fit()
    smoothed = fit.fittedvalues
    forecast = fit.forecast(steps)

    academic_plot(ts, smoothed, forecast, player_name, method="Holt-Winters")
