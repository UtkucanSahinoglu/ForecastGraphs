from src.plot_utils import academic_multi_ma_plot


def impact_of_different_q(ts, q_values, player_name="Player"):
    """
    Shows the impact of different MA window sizes (q values) on smoothing.
    """

    ma_dict = {}
    for q in q_values:
        ma_series = ts.rolling(q).mean().dropna()
        ma_dict[f"MA-{q}"] = ma_series

    explanation = (
        "Smaller q reacts quickly but keeps more noise.\n"
        "Larger q produces smoother trends but responds more slowly."
    )

    academic_multi_ma_plot(ts, ma_dict, player_name, "Impact of Different q (Window Sizes)", explanation)
