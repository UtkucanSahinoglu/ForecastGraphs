import pandas as pd
import matplotlib.pyplot as plt


def calculate_seasonal_index(ts):
    """
    Computes weekly seasonal indices using daily data.
    Period = day of week (0=Mon ... 6=Sun)
    """

    # Daily frequency (NBA data is irregular)
    ts = ts.asfreq("D").fillna(0)

    df = pd.DataFrame({
        "value": ts,
        "dow": ts.index.dayofweek
    })

    # Average for each day of the week
    seasonal_index = df.groupby("dow")["value"].mean()

    # Normalize so average = 1
    seasonal_index = seasonal_index / seasonal_index.mean()

    return seasonal_index


def plot_seasonal_index(seasonal_index, player_name="Player"):
    """
    Plots weekly seasonal index.
    """

    plt.figure(figsize=(10, 4))

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    plt.bar(days, seasonal_index.values, color="skyblue")

    plt.title(f"Seasonal Index (Weekly) – {player_name}")
    plt.ylabel("Seasonal Index")
    plt.xlabel("Day of Week")

    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"figures/{player_name}_Seasonal_Index.png", dpi=300)
    plt.show()


def seasonal_index_method(ts, player_name="Player"):
    """
    Full seasonal index workflow:
    1. Compute weekly indices
    2. Plot them
    """

    print(f"Computing Seasonal Index for: {player_name}")

    seasonal_index = calculate_seasonal_index(ts)

    print("\nSeasonal Indices (Normalized):")
    print(seasonal_index)

    plot_seasonal_index(seasonal_index, player_name)

    print("\nSeasonal Index method completed.\n")
    return seasonal_index
