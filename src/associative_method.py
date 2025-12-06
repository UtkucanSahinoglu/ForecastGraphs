import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def associative_method(df, player_name="Player", steps=20):
    """
    Associative (Causal) Forecasting using Linear Regression.
    Predicts probability of a made shot based on explanatory variables.
    """

    player_df = df[df["PLAYER_NAME"] == player_name].copy()
    if player_df.empty:
        print(f"No data found for player: {player_name}")
        return None

    player_df["MADE"] = player_df["EVENT_TYPE"].map({"Made Shot": 1, "Missed Shot": 0})

    X = player_df[["SHOT_DISTANCE", "QUARTER", "MINS_LEFT", "SECS_LEFT"]].fillna(0)
    y = player_df["MADE"]

    model = LinearRegression()
    model.fit(X, y)

    print(f"\nAssociative Method – Regression Coefficients for {player_name}:")
    for col, coef in zip(X.columns, model.coef_):
        print(f"{col}: {coef:.4f}")
    print(f"Intercept: {model.intercept_:.4f}")

    fitted = model.predict(X)

    # Construct some "typical" future scenarios (simple example)
    future_X = pd.DataFrame({
        "SHOT_DISTANCE": np.full(steps, X["SHOT_DISTANCE"].mean()),
        "QUARTER": np.full(steps, 1),
        "MINS_LEFT": np.full(steps, 6),
        "SECS_LEFT": np.linspace(24, 0, steps),
    })

    future_pred = model.predict(future_X)

    plt.figure(figsize=(10, 5))
    plt.plot(fitted[:200], label="Fitted (First 200 Shots)", color="#005BBB", linewidth=1.5)
    plt.plot(range(len(fitted), len(fitted) + steps), future_pred,
             "--", color="#D11B1B", linewidth=2.0, label="Forecast (Associative)")

    plt.title(f"{player_name} – Associative (Causal) Forecast")
    plt.xlabel("Shot Index")
    plt.ylabel("Predicted Probability of Made Shot")
    plt.grid(alpha=0.3)
    plt.legend(frameon=False)
    plt.tight_layout()
    plt.show()

    return future_pred
