ForecastGraphs Project – Time Series & Forecasting Methods Applied to NBA Data

ForecastGraphs is a full forecasting analysis project developed in Python. It applies multiple time series and causal forecasting techniques to NBA shot data (2004–2025) and generates academic-quality plots and tables for research, coursework, and professional reporting.

The project includes moving averages, exponential smoothing, trend models, seasonal methods, regression forecasting, and full error comparison modules. All outputs are saved as high-quality figures inside the figures/ directory.

Project Structure

data/ → ZIP files containing NBA shot data
figures/ → All generated graphs
src/ → Forecasting modules
loader.py → Loads NBA datasets
preprocess.py → Converts player data into daily time series
plot_utils.py → Academic-style plotting
metrics.py → MAD, MSE, RMSE, MAPE
forecast_ma.py → Moving Average
forecast_wma.py → Weighted Moving Average
forecast_ses.py → Simple Exponential Smoothing
forecast_holt.py → Holt–Winters Method
least_squares.py → Least Squares Trend Method
trend_projection.py → Trend Projection Method
seasonal_index.py → Seasonal Index Method
associative_method.py → Regression-based forecasting
impact_of_q.py → Effect of different q values
compare_errors.py → Forecast error comparison table
main.py → Runs all selected forecasting models

Forecasting Methods Implemented

Moving Average Methods
– Simple Moving Average (MA-q)
– Weighted Moving Average (WMA)
– Graph of multiple moving averages
– Impact of different q values

Exponential Smoothing
– Simple Exponential Smoothing (SES)
– Holt Method (trend)
– Holt–Winters Method (trend + seasonality)

Trend-Based Forecasting
– Trend Projection Method
– Least Squares Method
– Linear trend forecasting using regression

Seasonal Methods
– Seasonal Index Method (weekly seasonality)

Associative (Causal) Forecasting
– Linear regression-based forecasting
– Uses independent variables such as shot distance, quarter, and remaining time

Error Metrics & Model Evaluation
– MAD (Mean Absolute Deviation)
– MSE (Mean Squared Error)
– RMSE (Root Mean Squared Error)
– MAPE (Percentage Error)
– Full comparison table automatically generated

How to Run

Install required packages using pip and run:

python main.py

All plots will be saved into the figures/ folder.
All forecasting modules can be turned on or off inside main.py.

Notes for Academic Use

This project is suitable for forecasting courses, time series assignments, machine learning exploration, and statistical modeling. All methods follow academic definitions and produce clean, publication-level plots.

Future Enhancements (Optional)

– ARIMA / SARIMA models
– Prophet model
– Neural network forecasting
– Automated hyperparameter selection
– PDF forecasting report generation
