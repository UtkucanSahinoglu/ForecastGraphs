import matplotlib.pyplot as plt


def impact_of_different_q(ts, q_values, player_name="Player"):
    """
    Shows the impact of different q (window size) on moving average smoothing.
    q_values = [7, 14, 30] for example
    """

    plt.figure(figsize=(12, 6))

    # Raw data
    plt.plot(ts.index, ts, linewidth=0.8, color="gray", alpha=0.4, label="Raw Data")

    # Different q values
    for q in q_values:
        ma = ts.rolling(q).mean()
        plt.plot(ma.index, ma, linewidth=2, label=f"MA-{q}")

    plt.title(f"Impact of Different q on Moving Averages – {player_name}")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")
    plt.grid(True, alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig(f"figures/{player_name}_Impact_of_q.png", dpi=300)
    plt.show()

    print("Impact of q plot saved.")
