import pandas as pd
import numpy as np
from statsmodels.tsa.holtwinters import SimpleExpSmoothing, ExponentialSmoothing

from src.metrics import mad, mse, rmse, mape
from src.plot_utils import error_bar_plot


def _compute_ma(ts, window):
    ma = ts.rolling(window).mean().dropna()
    aligned = ts[-len(ma):]
    return aligned, ma


def _compute_wma(ts, window):
    weights = np.arange(1, window + 1)
    wma = ts.rolling(window).apply(lambda x: np.dot(x, weights) / weights.sum(), raw=True).dropna()
    aligned = ts[-len(wma):]
    return aligned, wma


def _compute_ses(ts, alpha):
    ts2 = ts.asfreq("D").fillna(0)
    model = SimpleExpSmoothing(ts2, initialization_method="estimated")
    fit = model.fit(smoothing_level=alpha, optimized=False)
    fitted = fit.fittedvalues
    aligned = ts2[-len(fitted):]
    return aligned, fitted


def _compute_holt(ts):
    ts2 = ts.asfreq("D").fillna(0)
    model = ExponentialSmoothing(ts2, trend="add", seasonal=None, initialization_method="estimated")
    fit = model.fit()
    fitted = fit.fittedvalues
    aligned = ts2[-len(fitted):]
    return aligned, fitted


def compare_forecast_errors(ts, player_name="Player"):
    """
    Compares MA, WMA, SES, Holt-Winters in terms of MAD, MSE, RMSE, MAPE.
    Returns a DataFrame and saves CSV + shows MAD bar chart.
    """

    results = []

    # MA-14
    aligned, ma = _compute_ma(ts, 14)
    results.append({
        "Model": "MA-14",
        "MAD": mad(aligned, ma),
        "MSE": mse(aligned, ma),
        "RMSE": rmse(aligned, ma),
        "MAPE": mape(aligned, ma)
    })

    # WMA-5
    aligned, wma = _compute_wma(ts, 5)
    results.append({
        "Model": "WMA-5",
        "MAD": mad(aligned, wma),
        "MSE": mse(aligned, wma),
        "RMSE": rmse(aligned, wma),
        "MAPE": mape(aligned, wma)
    })

    # SES-0.3
    aligned, ses = _compute_ses(ts, alpha=0.3)
    results.append({
        "Model": "SES-0.3",
        "MAD": mad(aligned, ses),
        "MSE": mse(aligned, ses),
        "RMSE": rmse(aligned, ses),
        "MAPE": mape(aligned, ses)
    })

    # Holt-Winters
    aligned, holt = _compute_holt(ts)
    results.append({
        "Model": "Holt-Winters",
        "MAD": mad(aligned, holt),
        "MSE": mse(aligned, holt),
        "RMSE": rmse(aligned, holt),
        "MAPE": mape(aligned, holt)
    })

    df = pd.DataFrame(results)
    df = df.sort_values("MAD").reset_index(drop=True)

    print("\n============ Forecast Error Comparison ============\n")
    print(df.to_string(index=False))
    print("\n===================================================\n")

    # Save CSV
    df.to_csv(f"figures/{player_name}_error_comparison.csv", index=False)

    # Plot MAD comparison
    error_bar_plot(df, player_name=player_name)

    return df
