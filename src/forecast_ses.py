import pandas as pd
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from src.plot_utils import academic_forecast_plot


def exponential_smoothing_forecast(ts, alpha=0.3, steps=20, player_name="Player"):
    """
    Simple Exponential Smoothing (SES) forecast.
    Only level component is modeled (no trend, no seasonality).
    """

    ts_daily = ts.asfreq("D").fillna(0)

    model = SimpleExpSmoothing(ts_daily, initialization_method="estimated")
    fit = model.fit(smoothing_level=alpha, optimized=False)

    smoothed = fit.fittedvalues
    forecast = fit.forecast(steps)

    explanation = (
        f"SES uses a smoothing factor α={alpha}, assigning exponentially\n"
        f"decreasing weights to older observations."
    )

    academic_forecast_plot(ts_daily, smoothed, forecast, player_name, f"Simple Exponential Smoothing (α={alpha})", explanation)
    return forecast
