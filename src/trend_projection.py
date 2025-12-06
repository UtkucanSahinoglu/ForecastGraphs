import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def trend_projection_forecast(ts, steps=20, player_name="Player"):
    """
    Trend Projection Method (Linear Trend Forecasting).
    Fits Y = a + b*t and forecasts future values.
    """

    print(f"Trend Projection Forecast for: {player_name}")

    # Ensure regular frequency
    ts = ts.asfreq('D').fillna(0)

    # Create t index: 1, 2, 3, ...
    t = np.arange(1, len(ts) + 1)

    # Fit Linear Regression
    coeffs = np.polyfit(t, ts.values, deg=1)
    a, b = coeffs[1], coeffs[0]  # a = intercept, b = slope

    print(f"Trend equation: Y = {a:.4f} + {b:.4f} * t")

    # Fitted values
    fitted = a + b * t

    # Future forecast
    t_future = np.arange(len(ts) + 1, len(ts) + steps + 1)
    forecast = a + b * t_future

    future_dates = pd.date_range(ts.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast_series = pd.Series(forecast, index=future_dates)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(ts.index, ts.values, color="gray", alpha=0.4, label="Raw Data")
    plt.plot(ts.index, fitted, color="blue", linewidth=2, label="Trend Line")
    plt.plot(forecast_series.index, forecast_series.values,
             "--", color="red", linewidth=2, label="Forecast")

    plt.title(f"Trend Projection Method – {player_name}")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")
    plt.grid(True, alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.savefig(f"figures/{player_name}_Trend_Projection.png", dpi=300)
    plt.show()

    print("Trend Projection forecast completed.\n")
    return forecast_series
