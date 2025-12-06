
# 🎯 ForecastGraphs

This repository provides a complete, modular, and academically structured implementation of **time series forecasting methods** using NBA shot data (2004–2025).
The project includes classical forecasting approaches, causal regression models, and evaluation metrics — all packaged with clean plots and a scalable architecture suitable for data science and analytics workflows.

---

## ⭐ Features

* Full implementation of classical **time series forecasting models**
* Clean academic-style graphs for all forecast methods
* **Moving Average**, **WMA**, **SES**, **Holt**, **Holt–Winters**, **Trend Projection**, **Least Squares**
* **Seasonal Index Method** for weekly seasonality detection
* **Associative (Causal) Forecasting** using regression
* Automatic **error comparison table** (MAD, MSE, RMSE, MAPE)
* Modular Python architecture (src folder)
* Ready-to-run main controller
* Extendable structure for ARIMA, Prophet, ML models

---

## 📁 Project Structure

* **ForecastGraphs/**

  * **data/**

    * NBA shot datasets (.zip)
  * **figures/**

    * Exported forecasts, trend plots, seasonal charts, error tables
  * **src/**

    * `loader.py` — dataset loader
    * `preprocess.py` — player time series builder
    * `plot_utils.py` — academic plotting system
    * `metrics.py` — MAD, MSE, RMSE, MAPE
    * `forecast_ma.py` — Moving Average
    * `forecast_wma.py` — Weighted MA
    * `forecast_ses.py` — Simple Exponential Smoothing
    * `forecast_holt.py` — Holt & Holt–Winters Forecast
    * `trend_projection.py` — Trend Projection Model
    * `least_squares.py` — Least Squares Regression Trend
    * `seasonal_index.py` — Seasonal Index Method
    * `associative_method.py` — Regression (Causal Forecasting)
    * `impact_of_q.py` — Analysis of different MA window lengths
    * `compare_errors.py` — Full error comparison table
  * **main.py**

    * Executes selected forecasting models

---

## 🛠 Technologies Used

* **Python 3.10+**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **scikit-learn** (for regression forecasting)
* **statsmodels** (smoothing and exponential models)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/ForecastGraphs.git
cd ForecastGraphs
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

### 3. Run Forecast Analysis

```bash
python main.py
```

All generated plots and tables appear inside:

```
figures/
```

---

## 🧩 Architecture Overview

### 🔹 Time Series Pipeline

Data → Preprocessing → Modeling → Forecast → Visualization → Error Evaluation

### 🔹 Supported Models

* Moving Average (MA-q)
* Weighted Moving Average (WMA)
* Simple Exponential Smoothing
* Holt Trend Method
* Holt–Winters Method
* Trend Projection
* Least Squares Regression Trend
* Seasonal Index Calculation
* Associative (Causal) Regression Forecast

### 🔹 High-Level Flow

Dataset → Player Time Series → Forecast Model → Plot → Error Table

---

## 🧪 Error Evaluation

ForecastGraphs includes automatic error metric calculations:

* **MAD** (Mean Absolute Deviation)
* **MSE** (Mean Squared Error)
* **RMSE** (Root Mean Squared Error)
* **MAPE** (Percentage Error)

Comparison table is saved as:

```
figures/{PlayerName}_forecast_error_comparison.csv
```

---

## 📘 Example Use Cases

This project demonstrates:

* Building time-series-based forecasting pipelines
* Detecting trend and seasonality patterns
* Comparing multiple forecast models
* Using regression for causal forecasting
* Evaluating predictive performance using statistical metrics
* Generating academic-quality visualizations for reports

---

## 🔧 Optional Extensions

You may extend the project with:

* ARIMA / SARIMA
* Prophet model
* LSTM / RNN neural networks
* Automated hyperparameter tuning
* PDF forecasting reports

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `feature/my-change`
3. Commit your changes
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License.
See the LICENSE file for more information.
