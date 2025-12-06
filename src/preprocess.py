def prepare_player_timeseries(df, player_name):
    """
    Extracts a player's daily made-shot time series.
    EVENT_TYPE is converted to numeric (1 = Made Shot, 0 = Missed Shot).
    """

    player_df = df[df["PLAYER_NAME"] == player_name].copy()

    if player_df.empty:
        print(f"No data found for player: {player_name}")
        return None

    player_df["MADE"] = player_df["EVENT_TYPE"].map({
        "Made Shot": 1,
        "Missed Shot": 0
    })

    ts = player_df.groupby("GAME_DATE")["MADE"].sum().sort_index()
    return ts
