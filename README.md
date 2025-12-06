# 🎯 FORECASTGRAPHS PROJECT  
### Time Series & Forecasting Methods Applied to NBA Data (2004–2025)

ForecastGraphs is a complete Python forecasting project that applies multiple time series and causal forecasting methods to NBA shot data.  
It produces clean, academic-quality plots and model evaluation tables for research and coursework.

---

## 📁 Project Structure

ForecastGraphs/
│
├── data/ # NBA shot ZIP files
├── figures/ # Exported plots
│
├── src/
│ ├── loader.py # Dataset loader
│ ├── preprocess.py # Build player time series
│ ├── plot_utils.py # Academic plotting
│ ├── metrics.py # MAD, MSE, RMSE, MAPE
│ ├── forecast_ma.py # Moving Average
│ ├── forecast_wma.py # Weighted MA
│ ├── forecast_ses.py # Simple Exp. Smoothing
│ ├── forecast_holt.py # Holt–Winters
│ ├── trend_projection.py # Trend Projection
│ ├── least_squares.py # Least Squares Regression
│ ├── seasonal_index.py # Seasonal Index Method
│ ├── associative_method.py # Regression (Causal) Forecasting
│ ├── impact_of_q.py # Effect of different MA-q values
│ └── compare_errors.py # Error comparison table
│
└── main.py # Runs all forecast models


---

## 📈 Forecasting Methods Implemented

### **Moving Average Methods**
- Simple Moving Average (MA-q)  
- Weighted Moving Average (WMA)  
- Multiple MA comparison  
- Impact of different window lengths (q)

### **Exponential Smoothing**
- Simple Exponential Smoothing (SES)  
- Holt Trend Method  
- Holt–Winters Method (trend + seasonality)

### **Trend-Based Models**
- Trend Projection Method  
- Least Squares Trend (Linear Regression)

### **Seasonal Methods**
- Seasonal Index Method (Weekly Seasonality)

### **Associative (Causal) Forecasting**
- Linear Regression Model  
- Uses explanatory variables:
  - Shot Distance  
  - Quarter  
  - Time Left  

### **Error Metrics & Model Evaluation**
- MAD – Mean Absolute Deviation  
- MSE – Mean Squared Error  
- RMSE – Root Mean Squared Error  
- MAPE – Mean Absolute Percentage Error  
- Comparison table generated automatically  

---

## 🚀 How to Run the Project

### 1️⃣ Install required Python packages:
```bash
pip install -r requirements.txt

Execute main forecast script:
python main.py

All outputs are saved in:
figures/

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
