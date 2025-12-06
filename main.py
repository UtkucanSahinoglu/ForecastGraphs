from src.loader import load_shot_data
from src.preprocess import prepare_player_timeseries

from src.forecast_ma import moving_average_forecast
from src.forecast_wma import wma_forecast
from src.forecast_ses import exponential_smoothing_forecast
from src.forecast_holt import holt_winters_forecast
from src.graph_ma import graph_of_moving_averages
from src.compare_errors import compare_forecast_errors
from src.impact_of_q import impact_of_different_q
from src.seasonal_index import seasonal_index_method
from src.trend_projection import trend_projection_forecast
from src.least_squares import least_squares_forecast
from src.associative_method import associative_method


if __name__ == "__main__":
    df = load_shot_data()

    player = "LeBron James"
    ts = prepare_player_timeseries(df, player)

    moving_average_forecast(ts, window=14, steps=20, player_name=player)
    wma_forecast(ts, window=5, steps=20, player_name=player)
    exponential_smoothing_forecast(ts, alpha=0.3, steps=20, player_name=player)
    holt_winters_forecast(ts, steps=20, player_name=player)
    graph_of_moving_averages(ts, windows=[7, 14, 30], player_name=player)
    error_table = compare_forecast_errors(ts, player_name=player)
    impact_of_different_q(ts, q_values=[7, 14, 30], player_name=player)
    seasonal_index_method(ts, player_name=player)
    trend_projection_forecast(ts, steps=20, player_name=player)
    least_squares_forecast(ts, steps=20, player_name=player)
    associative_method(df, player_name=player, steps=20)
