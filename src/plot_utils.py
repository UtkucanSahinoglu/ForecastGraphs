import matplotlib.pyplot as plt


def academic_plot(ts, smooth, forecast, player_name, method="MA"):
    plt.figure(figsize=(10,5))

    plt.plot(ts.index, ts, color="gray", alpha=0.4, linewidth=0.8,
             label="Gerçek İsabetler")

    plt.plot(smooth.index, smooth, linewidth=2,
             label="Hareketli Ortalama")

    plt.plot(forecast.index, forecast, "--", color="red", linewidth=2,
             label="Forecast")

    plt.axvline(ts.index[-1], linestyle=":", color="black", alpha=0.7)

    plt.title(f"{player_name} – {method} Tahmini")
    plt.xlabel("Tarih")
    plt.ylabel("İsabet Sayısı")

    plt.grid(True, linewidth=0.5, alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig(f"figures/{player_name}_{method}.png", dpi=300)
    plt.show()
