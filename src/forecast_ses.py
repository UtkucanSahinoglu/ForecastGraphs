import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from src.plot_utils import academic_plot


def exponential_smoothing_forecast(ts, alpha=0.3, steps=20, player_name="Player"):
    ts = ts.asfreq('D').fillna(0)

    model = SimpleExpSmoothing(ts, initialization_method="estimated")
    fit = model.fit(smoothing_level=alpha, optimized=False)

    smoothed = fit.fittedvalues
    forecast = fit.forecast(steps)

    academic_plot(ts, smoothed, forecast, player_name, method=f"SES-alpha{alpha}")
