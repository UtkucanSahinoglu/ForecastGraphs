import numpy as np


def mad(actual, forecast):
    actual = np.array(actual)
    forecast = np.array(forecast)
    return np.mean(np.abs(actual - forecast))


def mse(actual, forecast):
    actual = np.array(actual)
    forecast = np.array(forecast)
    return np.mean((actual - forecast) ** 2)


def rmse(actual, forecast):
    return np.sqrt(mse(actual, forecast))


def mape(actual, forecast):
    actual = np.array(actual)
    forecast = np.array(forecast)
    # avoid division by zero
    actual = np.where(actual == 0, 1e-8, actual)
    return np.mean(np.abs((actual - forecast) / actual)) * 100.0
