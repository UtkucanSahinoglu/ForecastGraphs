import numpy as np


def mad(actual, forecast):
    return np.mean(np.abs(actual - forecast))


def mse(actual, forecast):
    return np.mean((actual - forecast) ** 2)


def rmse(actual, forecast):
    return np.sqrt(mse(actual, forecast))


def mape(actual, forecast):
    actual = np.where(actual == 0, 1e-8, actual)
    return np.mean(np.abs((actual - forecast) / actual)) * 100
