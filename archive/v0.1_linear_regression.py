import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Import historical stock price data
data = pd.read_csv("csv/SPY.csv")

# Train a linear regression model on the data
model = LinearRegression()
model.fit(data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]], data["Close"])

# Predict the stock price for tomorrow
prediction = model.predict(data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]].iloc[[-1]].values.reshape(1, -1))

# Print the prediction
print(prediction)