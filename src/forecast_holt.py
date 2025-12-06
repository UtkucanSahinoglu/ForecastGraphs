from statsmodels.tsa.holtwinters import ExponentialSmoothing
from src.plot_utils import academic_forecast_plot


def holt_winters_forecast(ts, steps=20, player_name="Player"):
    """
    Holt-Winters Exponential Smoothing (trend only; no seasonality).
    """

    ts_daily = ts.asfreq("D").fillna(0)

    model = ExponentialSmoothing(
        ts_daily,
        trend="add",
        seasonal=None,
        initialization_method="estimated"
    )

    fit = model.fit()
    smoothed = fit.fittedvalues
    forecast = fit.forecast(steps)

    explanation = (
        "Holt-Winters (trend version) extends SES by modeling the\n"
        "underlying trend explicitly in addition to the level."
    )

    academic_forecast_plot(ts_daily, smoothed, forecast, player_name, "Holt-Winters (Trend Only)", explanation)
    return forecast
