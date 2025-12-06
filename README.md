🎯 FORECASTGRAPHS PROJECT
Time Series & Forecasting Methods Applied to NBA Data (2004–2025)

ForecastGraphs is a complete Python forecasting project that applies multiple time series and causal forecasting methods to NBA shot data.
It produces clean, academic-quality plots and model evaluation tables for research and coursework.

📁 Project Structure
ForecastGraphs/
│
├── data/                      # NBA shot ZIP files
├── figures/                   # Exported plots
│
├── src/
│   ├── loader.py              # Dataset loader
│   ├── preprocess.py          # Build player time series
│   ├── plot_utils.py          # Academic plotting
│   ├── metrics.py             # MAD, MSE, RMSE, MAPE
│   ├── forecast_ma.py         # Moving Average
│   ├── forecast_wma.py        # Weighted MA
│   ├── forecast_ses.py        # Simple Exp. Smoothing
│   ├── forecast_holt.py       # Holt–Winters
│   ├── trend_projection.py    # Trend Projection
│   ├── least_squares.py       # Least Squares Regression
│   ├── seasonal_index.py      # Seasonal Index Method
│   ├── associative_method.py  # Regression (Causal) Forecasting
│   ├── impact_of_q.py         # Effect of different MA-q values
│   └── compare_errors.py      # Error comparison table
│
└── main.py                    # Runs all forecast models

📈 Forecasting Methods Implemented
1. Moving Average Methods

Simple Moving Average (MA-q)

Weighted Moving Average (WMA)

Multiple MA comparison

Impact of different window lengths (q)

2. Exponential Smoothing

Simple Exponential Smoothing (SES)

Holt Trend Method

Holt–Winters Method (trend + seasonality)

3. Trend-Based Models

Trend Projection Method

Least Squares Trend (Linear Regression)

4. Seasonal Methods

Seasonal Index Method (Weekly Seasonality)

5. Associative (Causal) Forecasting

Linear Regression Model

Uses explanatory variables:

Shot Distance

Quarter

Time Left

6. Error Metrics & Model Evaluation

MAD – Mean Absolute Deviation

MSE – Mean Squared Error

RMSE – Root Mean Squared Error

MAPE – Mean Absolute Percentage Error

Comparison table generated automatically

🚀 How to Run the Project
1️⃣ Install required Python packages:
pip install -r requirements.txt

2️⃣ Execute main forecast script:
python main.py

3️⃣ View results in:
figures/


All plots and comparison tables are automatically saved here.

🧠 What This Project Produces

Clean academic-style forecast graphs

Trend and seasonality visualizations

Regression-based explanatory forecasting

Performance comparison of all models

Forecast tables & prediction series

📚 Academic Purpose

This project is ideal for:

MBA forecasting assignments

Time series analysis coursework

Statistical modeling studies

Regression and decomposition research

End-of-term forecasting projects

All methods follow academically accepted formulas and produce publication-level charts.

🔧 Future Improvements (Optional)

ARIMA / SARIMA models

Prophet forecasting

Neural network forecasting (LSTM, RNN)

Full automatic PDF report generation

Hyperparameter optimization
