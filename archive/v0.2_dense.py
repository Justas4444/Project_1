import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# NOTE: 1day model------------------------------------------------------------------------------------------

# Import historical stock price data
# data = pd.read_csv("csv/SPY.csv")

# # Prepare the features and target variables
# X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
# y = data["Close"]

# # Normalize the data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# # Split the data into training and testing sets (80% training, 20% testing)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# # Define the neural network architecture
# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
#     tf.keras.layers.Dense(32, activation='relu'),
#     tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
# ])

# # Compile the model
# model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# # Train the model
# model.fit(X_train, y_train, epochs=1000, batch_size=128, validation_split=0.2)

# # Evaluate the model on the test data
# loss, mean_absolute_error = model.evaluate(X_test, y_test)
# print(f"Test mean absolute error: {mean_absolute_error}")

# # Make predictions on the test data
# y_pred = model.predict(X_test)

# # Print the first few predicted and true target values
# print("Predicted\tTrue")
# for i in range(min(100, len(y_pred))):  # Print the first 100 predictions, or all if less than 100
#     print(f"{y_pred[i][0]}\t\t{y_test.iloc[i]}")

# model.save("trained_models/trained_model.h5")

#NOTE:---------------------------------------------------------

# Test with interest rate: 
# epochs=2000, batch_size=32, mae:  0.004320909734815359

#---------------------------------------------------------

# NOTE: test 1 day model ------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

# Load the historical stock price data from "formatted_data.csv"
data = pd.read_csv("csv/SPY.csv")

# Prepare the features and target variables
X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
y = data["Close"]

# Normalize the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Load the trained model from "trained_model.h5"
model = tf.keras.models.load_model("trained_models/trained_model.h5")

# Extract the last row of data for tomorrow's prediction
today_values = X_scaled[-1]

# Reshape the data for prediction
user_today_values_scaled = today_values.reshape(1, -1)

# Make a prediction for tomorrow's close using the trained model
prediction = model.predict(user_today_values_scaled)
predicted_close = prediction[0][0]

# Print the last row values (before normalization)
last_row_values = data.iloc[-1]

print("Last row values:\n",last_row_values)

print("Neural_Nets\nTomorrow's predicted close:",predicted_close)




#Day 1.
# True=4521, Predict=4519
 
#Day 2.
# True=4542, Predict=4518

#Day 3.
# True=, Predict=4536

#Day 4.
# True=, Predict=

#Day 5.

