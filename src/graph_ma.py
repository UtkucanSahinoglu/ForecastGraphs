import matplotlib.pyplot as plt


def graph_of_moving_averages(ts, windows, player_name="Player"):
    plt.figure(figsize=(12, 6))

    plt.plot(ts.index, ts, color="gray", alpha=0.4, linewidth=0.8)

    for w in windows:
        plt.plot(ts.rolling(w).mean(), linewidth=2, label=f"MA-{w}")

    plt.title(f"{player_name} – Moving Averages Comparison")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")

    plt.grid(True, alpha=0.3)
    plt.legend(frameon=False)

    plt.tight_layout()
    plt.savefig(f"figures/{player_name}_Graph_of_MA.png", dpi=300)
    plt.show()
