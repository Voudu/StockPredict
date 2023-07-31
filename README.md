# StockPredict
Stock Price Prediction Model

## Disclaimer
This is NOT meant to be used as a tool to make financial investment decisions. This software is solely for educational purposes and for use in the pursuit of learning machine learning technologies and libraries.

## Objective

Build a machine learning model that predicts future stock prices based on histroical price data

## Methodology

1. Data Collection: Obtain historical stock price data for the stock of your choice. Using financial API, Yahoo Finance.

2. Data Preprocessing: Clean the data and handle missing values. Perform any necessary transformations like calculating returns or log-returns from the raw price data.

3. Exploratory Data Analysis (EDA): Explore the data to gain insights into the stock's behavior, trends, and relationships with other financial indicators. Using visualization libraries like Matplotlib to create plots that help you understand the data.

4. Feature Engineering: Create relevant features that can improve the predictive power of your model. These features could include technical indicators (e.g., Moving Averages, Relative Strength Index), macroeconomic factors, or sentiment analysis scores.

5. Time Series Forecasting Model: Select a suitable time series forecasting model for your stock price prediction. Using popular models like Autoregressive Integrated Moving Average (ARIMA), Seasonal Autoregressive Integrated Moving-Average (SARIMA), or more advanced models like Long Short-Term Memory (LSTM) networks.

6. Data Splitting: Split the data into training and testing sets. Ensure that the testing data represents a future timeframe than the training data to simulate real-world forecasting scenarios.

7. Model Training: Train your chosen time series forecasting model on the training data. Tune hyperparameters if applicable to improve the model's performance.

8. Model Evaluation: Evaluate the model's performance on the testing data using appropriate metrics such as Mean Squared Error (MSE), Mean Absolute Error (MAE), or Root Mean Squared Error (RMSE).

9. Model Visualization: Visualize the predicted stock prices against the actual prices using plots to see how well your model performs.

10. Future Price Prediction: Use your trained model to predict future stock prices for a specific time horizon. Compare these predictions with actual prices if available.

11. Project Summary and Documentation: Summarize your findings, including the performance of the model and any insights you gained during the analysis. Document the entire project to showcase your approach and thought process.

## Build

1. Create a python venv
2. Install dependencies from required.txt