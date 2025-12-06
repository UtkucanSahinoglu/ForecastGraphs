import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def least_squares_forecast(ts, steps=20, player_name="Player"):
    """
    Least Squares Method (Simple Linear Regression Trend Forecast)
    Fits Y = a + bt and forecasts future periods.
    """

    print(f"Least Squares Method Forecast for: {player_name}")

    # Ensure regular time frequency
    ts = ts.asfreq("D").fillna(0)

    # Create time index t = 1, 2, ..., n
    n = len(ts)
    t = np.arange(1, n + 1)

    # Apply Least Squares Regression
    # polyfit returns slope b and intercept a
    b, a = np.polyfit(t, ts.values, deg=1)

    print(f"\nEstimated Trend Equation:")
    print(f"Ŷ = {a:.4f} + {b:.4f} * t")

    # Fitted trend line
    fitted = a + b * t

    # Forecast future t
    t_future = np.arange(n + 1, n + steps + 1)
    forecast_values = a + b * t_future

    # Create forecast index
    future_dates = pd.date_range(ts.index[-1] + pd.Timedelta(days=1), periods=steps)
    forecast_series = pd.Series(forecast_values, index=future_dates)

    # ----- Plot -----
    plt.figure(figsize=(10, 5))

    plt.plot(ts.index, ts.values, color="gray", alpha=0.5, linewidth=0.8, label="Raw Data")
    plt.plot(ts.index, fitted, color="blue", linewidth=2, label="Least Squares Trend")
    plt.plot(forecast_series.index, forecast_series.values,
             "--", color="red", linewidth=2, label="Forecast")

    plt.title(f"Least Squares Method – {player_name}")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")
    plt.grid(True, alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig(f"figures/{player_name}_Least_Squares.png", dpi=300)
    plt.show()

    print("\nLeast Squares Method completed.\n")
    return forecast_series
