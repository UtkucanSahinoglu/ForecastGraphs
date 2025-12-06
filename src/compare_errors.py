import pandas as pd
from src.metrics import mad, mse, rmse, mape
from src.forecast_ma import moving_average_forecast
from src.forecast_wma import wma_forecast
from src.forecast_ses import exponential_smoothing_forecast
from src.forecast_holt import holt_winters_forecast


def compute_smoothed_ma(ts, window):
    return ts.rolling(window).mean().dropna()


def compute_smoothed_wma(ts, window):
    import numpy as np
    weights = np.arange(1, window + 1)
    wma = ts.rolling(window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True)
    return wma.dropna()


def compute_smoothed_ses(ts, alpha):
    from statsmodels.tsa.holtwinters import SimpleExpSmoothing
    ts2 = ts.asfreq('D').fillna(0)
    model = SimpleExpSmoothing(ts2, initialization_method="estimated")
    fit = model.fit(smoothing_level=alpha, optimized=False)
    return fit.fittedvalues


def compute_smoothed_holt(ts):
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    ts2 = ts.asfreq('D').fillna(0)
    model = ExponentialSmoothing(
        ts2, trend="add", seasonal=None, initialization_method="estimated"
    )
    fit = model.fit()
    return fit.fittedvalues


def compare_forecast_errors(ts, player_name="Player"):
    results = []

    # ---- MA ----
    ma = compute_smoothed_ma(ts, 14)
    common = ts[-len(ma):]
    results.append({
        "Model": "MA-14",
        "MAD": mad(common, ma),
        "MSE": mse(common, ma),
        "RMSE": rmse(common, ma),
        "MAPE": mape(common, ma)
    })

    # ---- WMA ----
    wma = compute_smoothed_wma(ts, 5)
    common = ts[-len(wma):]
    results.append({
        "Model": "WMA-5",
        "MAD": mad(common, wma),
        "MSE": mse(common, wma),
        "RMSE": rmse(common, wma),
        "MAPE": mape(common, wma)
    })

    # ---- SES ----
    ses = compute_smoothed_ses(ts, alpha=0.3)
    common = ts.asfreq('D').fillna(0)
    results.append({
        "Model": "SES-0.3",
        "MAD": mad(common, ses),
        "MSE": mse(common, ses),
        "RMSE": rmse(common, ses),
        "MAPE": mape(common, ses)
    })

    # ---- Holt-Winters ----
    holt = compute_smoothed_holt(ts)
    common = ts.asfreq('D').fillna(0)
    results.append({
        "Model": "Holt-Winters",
        "MAD": mad(common, holt),
        "MSE": mse(common, holt),
        "RMSE": rmse(common, holt),
        "MAPE": mape(common, holt)
    })

    # Convert to DataFrame for readability
    df = pd.DataFrame(results)
    print("\nForecast Error Comparison")
    print(df.to_string(index=False), "\n")

    # Save result as CSV (optional)
    df.to_csv(f"figures/{player_name}_forecast_error_comparison.csv", index=False)

    return df
