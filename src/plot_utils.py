import matplotlib.pyplot as plt
import os


# ======================================================
#  MASTER SAVE FUNCTION (TÜM GRAFİKLER BUNU KULLANIR)
# ======================================================
def save_figure(filename):
    os.makedirs("figures", exist_ok=True)
    filename = f"figures/{filename}.png"
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    print(f"[SAVED] {filename}")


# ======================================================
#  1) FORECAST / FITTED / RAW DATA GRAFİĞİ
# ======================================================
def academic_forecast_plot(ts, smoothed, forecast, player_name, method_name, explanation=None):
    """
    Unified academic plot for MA, WMA, SES, Holt, Holt-Winters, Trend, LS.
    Saves figure automatically.
    Explanation is placed bottom-right.
    """

    plt.figure(figsize=(12, 6))

    # RAW DATA
    if ts is not None:
        plt.plot(ts.index, ts.values,
                 linewidth=1.2, color="#9A9A9A",
                 label="Raw Data")

    # SMOOTHED SERIES
    if smoothed is not None:
        plt.plot(smoothed.index, smoothed.values,
                 linewidth=2.2, color="#005BBB",
                 label="Smoothed / Fitted")

    # FORECAST
    if forecast is not None and len(forecast) > 0:
        plt.plot(forecast.index, forecast.values,
                 "--", linewidth=2.2, color="#D11B1B",
                 label="Forecast")

        # Forecast region shading
        if ts is not None:
            plt.axvspan(ts.index[-1], forecast.index[-1],
                        color="#FFD500", alpha=0.18)

    # TITLE + AXES
    plt.title(f"{player_name} – {method_name}", fontsize=15, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")
    plt.grid(alpha=0.25, linewidth=0.6)
    plt.legend(frameon=False, fontsize=10, loc="upper left")
    plt.xticks(rotation=25)

    # EXPLANATION BOX (BOTTOM-RIGHT)
    if explanation:
        plt.annotate(
            explanation,
            xy=(0.98, 0.02),
            xycoords="axes fraction",
            fontsize=9,
            color="black",
            ha="right", va="bottom",
            bbox=dict(boxstyle="round,pad=0.45",
                      fc="white", ec="gray", alpha=0.90)
        )

    plt.tight_layout()

    # === SAVE ===
    filename = f"{player_name}_{method_name.replace(' ', '_')}"
    save_figure(filename)

    plt.show()


# ======================================================
#  2) MULTI-MA: Birden Fazla Moving Average Grafiği
# ======================================================
def academic_multi_ma_plot(ts, ma_dict, player_name, title, explanation=None):
    """
    Plots multiple moving averages on top of raw data.
    Saves figure automatically.
    """

    plt.figure(figsize=(12, 6))

    # RAW DATA
    plt.plot(ts.index, ts.values,
             linewidth=1.2, color="#9A9A9A", alpha=0.6,
             label="Raw Data")

    # MULTIPLE MA LINES
    for label, series in ma_dict.items():
        plt.plot(series.index, series.values,
                 linewidth=2.0, label=label)

    plt.title(f"{player_name} – {title}", fontsize=15, fontweight="bold")
    plt.xlabel("Date")
    plt.ylabel("Shots Made")

    plt.grid(alpha=0.25, linewidth=0.6)
    plt.legend(frameon=False, fontsize=10, loc="upper left")
    plt.xticks(rotation=25)

    # EXPLANATION RIGHT-BOTTOM
    if explanation:
        plt.annotate(
            explanation,
            xy=(0.98, 0.02),
            xycoords="axes fraction",
            fontsize=9,
            color="black",
            ha="right", va="bottom",
            bbox=dict(boxstyle="round,pad=0.45",
                      fc="white", ec="gray", alpha=0.90)
        )

    plt.tight_layout()

    filename = f"{player_name}_{title.replace(' ', '_')}"
    save_figure(filename)

    plt.show()


# ======================================================
#  3) ERROR COMPARISON BAR CHART
# ======================================================
def error_bar_plot(df_errors, player_name="Player"):
    """
    Bar chart of MAD values for all forecasting models.
    Saves automatically.
    """

    plt.figure(figsize=(10, 5))

    models = df_errors["Model"].values
    mad_values = df_errors["MAD"].values

    plt.bar(models, mad_values, color="#005BBB", alpha=0.8)

    plt.title(f"{player_name} – Forecast Error Comparison (MAD)", fontsize=14, fontweight="bold")
    plt.ylabel("MAD")
    plt.xlabel("Model")
    plt.grid(axis="y", alpha=0.3)

    plt.xticks(rotation=20)
    plt.tight_layout()

    filename = f"{player_name}_Error_Comparison"
    save_figure(filename)

    plt.show()


# ======================================================
#  4) SEASONAL INDEX BAR PLOT (Opsiyonel)
# ======================================================
def seasonal_bar_plot(seasonal_index, player_name="Player"):
    """
    Saves seasonal index bar chart.
    """

    plt.figure(figsize=(8, 4))

    seasonal_index.plot(kind="bar", color="#005BBB", alpha=0.85)

    plt.title(f"{player_name} – Seasonal Index (Weekly)", fontsize=14, fontweight="bold")
    plt.grid(axis="y", alpha=0.3)

    plt.tight_layout()

    filename = f"{player_name}_Seasonal_Index"
    save_figure(filename)

    plt.show()
