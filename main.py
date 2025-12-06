from src.loader import load_shot_data
from src.preprocess import prepare_player_timeseries

from src.forecast_ma import moving_average_forecast
from src.forecast_wma import wma_forecast
from src.forecast_ses import exponential_smoothing_forecast
from src.forecast_holt import holt_winters_forecast
from src.trend_projection import trend_projection_forecast
from src.least_squares import least_squares_forecast
from src.seasonal_index import seasonal_index_method
from src.associative_method import associative_method
from src.impact_of_q import impact_of_different_q
from src.compare_errors import compare_forecast_errors

import os


def count_figures():
    if not os.path.exists("figures"):
        return 0
    return len([f for f in os.listdir("figures") if f.lower().endswith(".png")])


def safe_call(name, func):
    print(f"\n--- Running {name} ---")
    before = count_figures()
    try:
        func()
    except Exception as e:
        print(f"[ERROR] {name}: {str(e)}")
        return
    after = count_figures()
    if after == before:
        print(f"[WARNING] {name}: No figure was generated!")
    else:
        print(f"[OK] {name}: Figure saved.")


if __name__ == "__main__":
    print("Loading NBA dataset...")
    df = load_shot_data()
    player = "LeBron James"

    ts = prepare_player_timeseries(df, player)
    if ts is None:
        raise SystemExit("Time series could not be prepared.")

    # FORECAST METHODS
    safe_call("MA Forecast", lambda: moving_average_forecast(ts, 14, 20, player))
    safe_call("WMA Forecast", lambda: wma_forecast(ts, 5, 20, player))
    safe_call("SES Forecast", lambda: exponential_smoothing_forecast(ts, 0.3, 20, player))
    safe_call("Holt-Winters Forecast", lambda: holt_winters_forecast(ts, 20, player))
    safe_call("Trend Projection", lambda: trend_projection_forecast(ts, 20, player))
    safe_call("Least Squares", lambda: least_squares_forecast(ts, 20, player))

    # SEASONAL INDEX (now saves PNG)
    safe_call("Seasonal Index", lambda: seasonal_index_method(ts, player))

    # ASSOCIATIVE (causal)
    safe_call("Associative Method", lambda: associative_method(df, player, 20))

    # IMPACT OF q
    safe_call("Impact of q", lambda: impact_of_different_q(ts, [7, 14, 30], player))

    # ERROR COMPARISON
    safe_call("Error Comparison", lambda: compare_forecast_errors(ts, player))

    print("\nAll methods completed.")
    print(f"Total saved figures: {count_figures()}")
