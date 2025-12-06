def prepare_player_timeseries(df, player_name):
    player_df = df[df["PLAYER_NAME"] == player_name].copy()

    if player_df.empty:
        return None

    # EVENT_TYPE → numeric
    player_df["MADE"] = player_df["EVENT_TYPE"].map({
        "Made Shot": 1,
        "Missed Shot": 0
    })

    ts = player_df.groupby("GAME_DATE")["MADE"].sum()

    return ts
