import pandas as pd
import matplotlib.pyplot as plt


def calculate_seasonal_index(ts):
    """
    Computes normalized weekly seasonal indices (0=Mon ... 6=Sun).
    """

    ts_daily = ts.asfreq("D").fillna(0)

    df = pd.DataFrame({"value": ts_daily})
    df["dow"] = df.index.dayofweek

    seasonal_index = df.groupby("dow")["value"].mean()
    seasonal_index = seasonal_index / seasonal_index.mean()

    return seasonal_index


def seasonal_index_method(ts, player_name="Player"):
    """
    Full seasonal index workflow:
    1. Compute weekly indices
    2. Plot them
    """

    print(f"Computing Seasonal Index for: {player_name}")
    si = calculate_seasonal_index(ts)

    print("\nSeasonal Indices (normalized):")
    print(si)

    plt.figure(figsize=(8, 4))
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    plt.bar(days, si.values)

    plt.title(f"{player_name} – Weekly Seasonal Index")
    plt.ylabel("Seasonal Index")
    plt.xlabel("Day of Week")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()

    return si
