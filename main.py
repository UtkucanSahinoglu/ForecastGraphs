from src.loader import load_shot_data
from src.preprocess import prepare_player_timeseries
from src.forecast_ma import moving_average_forecast


if __name__ == "__main__":
    df = load_shot_data()

    player = "LeBron James"
    ts = prepare_player_timeseries(df, player)

    moving_average_forecast(ts, window=14, steps=20, player_name=player)
