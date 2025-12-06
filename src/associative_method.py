import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def associative_method(df, player_name="Player", steps=10):
    """
    Associative (Causal) Forecasting Method.
    Predicts MADE SHOTS based on related independent variables (X variables).
    """

    print(f"Associative Forecast (Regression-Based) for: {player_name}")

    # Filter player
    player_df = df[df["PLAYER_NAME"] == player_name].copy()

    # Binary target variable (1 = made shot)
    player_df["MADE"] = player_df["EVENT_TYPE"].map({"Made Shot": 1, "Missed Shot": 0})

    # Choose independent variables (X)
    X = player_df[[
        "SHOT_DISTANCE",
        "QUARTER",
        "MINS_LEFT",
        "SECS_LEFT"
    ]]

    # Replace missing values
    X = X.fillna(0)

    # Target variable
    y = player_df["MADE"]

    # Create regression model
    model = LinearRegression()
    model.fit(X, y)

    print("\nRegression Coefficients:")
    for name, coef in zip(X.columns, model.coef_):
        print(f"{name}: {coef:.4f}")

    print(f"Intercept: {model.intercept_:.4f}")

    # Predict using fitted model (in-sample)
    fitted = model.predict(X)

    # For forecasting, simulate next 'steps' shots
    future_X = pd.DataFrame({
        "SHOT_DISTANCE": np.linspace(X["SHOT_DISTANCE"].mean(), X["SHOT_DISTANCE"].mean(), steps),
        "QUARTER": np.full(steps, 1),
        "MINS_LEFT": np.full(steps, 6),
        "SECS_LEFT": np.linspace(0, 24, steps)
    })

    future_pred = model.predict(future_X)

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(fitted[:200], label="Fitted Values (Sample)", color="blue")
    plt.plot(range(len(fitted), len(fitted) + steps), future_pred,
             "--", color="red", label="Forecast")

    plt.title(f"Associative (Causal) Forecast – {player_name}")
    plt.ylabel("Probability of Made Shot")
    plt.xlabel("Shot Sequence")
    plt.grid(True, alpha=0.3)
    plt.legend(frameon=False)

    plt.tight_layout()
    plt.savefig(f"figures/{player_name}_Associative_Method.png", dpi=300)
    plt.show()

    print("\nAssociative forecasting completed.\n")
    return future_pred
