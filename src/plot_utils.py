import matplotlib.pyplot as plt


def academic_plot(ts, smooth, forecast, player_name, method="Model"):
    """
    Draws a clean academic-style forecast plot.
    """

    plt.figure(figsize=(10, 5))

    plt.plot(ts.index, ts, color="gray", alpha=0.4, linewidth=0.8, label="Raw Data")
    plt.plot(smooth.index, smooth, linewidth=2, label="Smoothed")
    plt.plot(forecast.index, forecast, "--", linewidth=2, color="red", label="Forecast")

    plt.axvline(ts.index[-1], linestyle=":", color="black", alpha=0.7)

    plt.title(f"{player_name} – {method} Forecast")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")

    plt.grid(True, linewidth=0.5, alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig(f"figures/{player_name}_{method}.png", dpi=300)
    plt.show()
