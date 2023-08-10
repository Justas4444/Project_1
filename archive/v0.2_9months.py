# WARNING: RESTRICTED ACCESS - TOP SECRET

# This Python file contains highly sensitive and confidential information owned by Renaissance Technologies LLC. Access to this file is strictly limited to authorized personnel 
# with appropriate security clearance. Unauthorized access, distribution, or sharing of any content within this file is strictly prohibited and may lead to severe legal consequences.

# By continuing to access this file, you acknowledge that you are an authorized clearance holder for Renaissance Technologies LLC and are bound by the company's strict confidentiality 
# policies. Any breach of trust or unauthorized disclosure will be subject to immediate legal action.

# If you are not an authorized clearance holder or have received this file in error, please exit immediately and notify the appropriate authorities or the Renaissance Technologies 
# security team at security@renaissancetech.com.

# Your compliance with these security measures is vital to protect sensitive information and maintain the integrity of our organization.

# This file is property of Renaissance Technologies LLC























import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.callbacks import EarlyStopping

#NOTE: 1day, 1week, 1-9 month models------------------------------------------------------------------------------------------------------------------------


# Import historical stock price data
data = pd.read_csv("csv/SPY.csv")

# Create target variables for 1 day, 1 week, 1 month, 2 months, 3 months, 4 months, and 5 months ahead
# To predict 1 day ahead, shift the Close prices 1 business day
data["Close_1_day"] = data["Close"]
# To predict 1 week ahead, shift the Close prices 5 business days (assuming 5 business days in a week)
data["Close_1_week"] = data["Close"].shift(-5)
# To predict 1 month ahead, shift the Close prices 20 business days (assuming 20 business days in a month)
data["Close_1_month"] = data["Close"].shift(-20)
# To predict 2 months ahead, shift the Close prices 40 business days (assuming 20 business days in a month)
data["Close_2_months"] = data["Close"].shift(-40)
# To predict 3 months ahead, shift the Close prices 60 business days (assuming 20 business days in a month)
data["Close_3_months"] = data["Close"].shift(-60)
# To predict 4 months ahead, shift the Close prices 80 business days (assuming 20 business days in a month)
data["Close_4_months"] = data["Close"].shift(-80)
# To predict 5 months ahead, shift the Close prices 100 business days (assuming 20 business days in a month)
data["Close_5_months"] = data["Close"].shift(-100)
# To predict 6 months ahead, shift the Close prices 120 business days (assuming 20 business days in a month)
data["Close_6_months"] = data["Close"].shift(-120)
# To predict 7 months ahead, shift the Close prices 140 business days (assuming 20 business days in a month)
data["Close_7_months"] = data["Close"].shift(-140)
# To predict 8 months ahead, shift the Close prices 160 business days (assuming 20 business days in a month)
data["Close_8_months"] = data["Close"].shift(-160)
# To predict 9 months ahead, shift the Close prices 180 business days (assuming 20 business days in a month)
data["Close_9_months"] = data["Close"].shift(-180)

# Drop rows with NaN values in the target variables
data.dropna(subset=["Close_1_day", "Close_1_week", "Close_1_month", "Close_2_months", "Close_3_months", "Close_4_months", "Close_5_months", "Close_6_months", "Close_7_months", "Close_8_months", "Close_9_months"], inplace=True)

# Prepare the features and target variables
X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
y_1_day = data["Close_1_day"]
y_1_week = data["Close_1_week"]
y_1_month = data["Close_1_month"]
y_2_months = data["Close_2_months"]
y_3_months = data["Close_3_months"]
y_4_months = data["Close_4_months"]
y_5_months = data["Close_5_months"]
y_6_months = data["Close_6_months"]
y_7_months = data["Close_7_months"]
y_8_months = data["Close_8_months"]
y_9_months = data["Close_9_months"]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# For 1-day data
X_train_1_day, X_test_1_day, y_1_day_train, y_1_day_test = train_test_split(X_scaled, y_1_day, test_size=0.2, random_state=42)
# For 1-week data
X_train_1_week, X_test_1_week, y_1_week_train, y_1_week_test = train_test_split(X_scaled, y_1_week, test_size=0.2, random_state=42)
# For 1-month data
X_train_1_month, X_test_1_month, y_1_month_train, y_1_month_test = train_test_split(X_scaled, y_1_month, test_size=0.2, random_state=42)
# For 2-month data
X_train_2_months, X_test_2_months, y_2_months_train, y_2_months_test = train_test_split(X_scaled, y_2_months, test_size=0.2, random_state=42)
# For 3-month data
X_train_3_months, X_test_3_months, y_3_months_train, y_3_months_test = train_test_split(X_scaled, y_3_months, test_size=0.2, random_state=42)
# For 4-month data
X_train_4_months, X_test_4_months, y_4_months_train, y_4_months_test = train_test_split(X_scaled, y_4_months, test_size=0.2, random_state=42)
# For 5-month data
X_train_5_months, X_test_5_months, y_5_months_train, y_5_months_test = train_test_split(X_scaled, y_5_months, test_size=0.2, random_state=42)
# For 6-month data
X_train_6_months, X_test_6_months, y_6_months_train, y_6_months_test = train_test_split(X_scaled, y_6_months, test_size=0.2, random_state=42)
# For 7-month data
X_train_7_months, X_test_7_months, y_7_months_train, y_7_months_test = train_test_split(X_scaled, y_7_months, test_size=0.2, random_state=42)
# For 8-month data
X_train_8_months, X_test_8_months, y_8_months_train, y_8_months_test = train_test_split(X_scaled, y_8_months, test_size=0.2, random_state=42)
# For 9-month data
X_train_9_months, X_test_9_months, y_9_months_train, y_9_months_test = train_test_split(X_scaled, y_9_months, test_size=0.2, random_state=42)

# Define the neural network architectures for each prediction
model_1_day = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_1_day.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_1_week = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_1_week.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_1_month = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_1_month.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_2_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_2_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_3_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_3_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_4_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_4_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_5_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_5_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_6_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_6_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_7_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_7_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_8_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_8_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])

model_9_months = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train_9_months.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')  # Output layer with linear activation for regression
])




# Compile the models
model_1_day.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_1_week.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_1_month.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_2_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_3_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_4_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_5_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_6_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_7_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_8_months.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_9_months.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train the models
model_1_day.fit(X_train_1_day, y_1_day_train, epochs=350, batch_size=128, validation_split=0.2)
model_1_week.fit(X_train_1_week, y_1_week_train, epochs=10, batch_size=128, validation_split=0.2)
model_1_month.fit(X_train_1_month, y_1_month_train, epochs=10, batch_size=128, validation_split=0.2)
model_2_months.fit(X_train_2_months, y_2_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_3_months.fit(X_train_3_months, y_3_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_4_months.fit(X_train_4_months, y_4_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_5_months.fit(X_train_5_months, y_5_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_6_months.fit(X_train_6_months, y_6_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_7_months.fit(X_train_7_months, y_7_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_8_months.fit(X_train_8_months, y_8_months_train, epochs=10, batch_size=128, validation_split=0.2)
model_9_months.fit(X_train_9_months, y_9_months_train, epochs=10, batch_size=128, validation_split=0.2)

# Evaluate the models on the test data
loss_1_day, mean_absolute_error_1_day = model_1_day.evaluate(X_test_1_day, y_1_day_test)
loss_1_week, mean_absolute_error_1_week = model_1_week.evaluate(X_test_1_week, y_1_week_test)
loss_1_month, mean_absolute_error_1_month = model_1_month.evaluate(X_test_1_month, y_1_month_test)
loss_2_months, mean_absolute_error_2_months = model_2_months.evaluate(X_test_2_months, y_2_months_test)
loss_3_months, mean_absolute_error_3_months = model_3_months.evaluate(X_test_3_months, y_3_months_test)
loss_4_months, mean_absolute_error_4_months = model_4_months.evaluate(X_test_4_months, y_4_months_test)
loss_5_months, mean_absolute_error_5_months = model_5_months.evaluate(X_test_5_months, y_5_months_test)
loss_6_months, mean_absolute_error_6_months = model_6_months.evaluate(X_test_6_months, y_6_months_test)
loss_7_months, mean_absolute_error_7_months = model_7_months.evaluate(X_test_7_months, y_7_months_test)
loss_8_months, mean_absolute_error_8_months = model_8_months.evaluate(X_test_8_months, y_8_months_test)
loss_9_months, mean_absolute_error_9_months = model_9_months.evaluate(X_test_9_months, y_9_months_test)

print(f"Test mean absolute error (1 day ahead): {mean_absolute_error_1_day}")
print(f"Test mean absolute error (1 week ahead): {mean_absolute_error_1_week}")
print(f"Test mean absolute error (1 month ahead): {mean_absolute_error_1_month}")
print(f"Test mean absolute error (2 months ahead): {mean_absolute_error_2_months}")
print(f"Test mean absolute error (3 months ahead): {mean_absolute_error_3_months}")
print(f"Test mean absolute error (4 months ahead): {mean_absolute_error_4_months}")
print(f"Test mean absolute error (5 months ahead): {mean_absolute_error_5_months}")
print(f"Test mean absolute error (6 months ahead): {mean_absolute_error_6_months}")
print(f"Test mean absolute error (7 months ahead): {mean_absolute_error_7_months}")
print(f"Test mean absolute error (8 months ahead): {mean_absolute_error_8_months}")
print(f"Test mean absolute error (9 months ahead): {mean_absolute_error_9_months}")

# Save the models
model_1_day.save("trained_models/trained_model_1_day.h5")
model_1_week.save("trained_models/trained_model_1_week.h5")
model_1_month.save("trained_models/trained_model_1_month.h5")
model_2_months.save("trained_models/trained_model_2_months.h5")
model_3_months.save("trained_models/trained_model_3_months.h5")
model_4_months.save("trained_models/trained_model_4_months.h5")
model_5_months.save("trained_models/trained_model_5_months.h5")
model_6_months.save("trained_models/trained_model_6_months.h5")
model_7_months.save("trained_models/trained_model_7_months.h5")
model_8_months.save("trained_models/trained_model_8_months.h5")
model_9_months.save("trained_models/trained_model_9_months.h5")

#NOTE: test 1day, 1week, 1-9 months-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Load the historical stock price data from "updated_SPY.csv"
data = pd.read_csv("csv/SPY.csv")

# Prepare the features and target variables
X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
y = data["Close"]

# Normalize the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Load the trained models
model_1_day = tf.keras.models.load_model("trained_models/trained_model_1_day.h5")
model_1_week = tf.keras.models.load_model("trained_models/trained_model_1_week.h5")
model_1_month = tf.keras.models.load_model("trained_models/trained_model_1_month.h5")
model_2_months = tf.keras.models.load_model("trained_models/trained_model_2_months.h5")
model_3_months = tf.keras.models.load_model("trained_models/trained_model_3_months.h5")
model_4_months = tf.keras.models.load_model("trained_models/trained_model_4_months.h5")
model_5_months = tf.keras.models.load_model("trained_models/trained_model_5_months.h5")
model_6_months = tf.keras.models.load_model("trained_models/trained_model_6_months.h5")
model_7_months = tf.keras.models.load_model("trained_models/trained_model_7_months.h5")
model_8_months = tf.keras.models.load_model("trained_models/trained_model_8_months.h5")
model_9_months = tf.keras.models.load_model("trained_models/trained_model_9_months.h5")

# Extract the last row of data for predictions
today_values = X_scaled[-1]

# Reshape the data for prediction
user_today_values_scaled = today_values.reshape(1, -1)

# Make predictions for all time horizons using the loaded models
prediction_1_day = model_1_day.predict(user_today_values_scaled)[0][0]
prediction_1_week = model_1_week.predict(user_today_values_scaled)[0][0]
prediction_1_month = model_1_month.predict(user_today_values_scaled)[0][0]
prediction_2_months = model_2_months.predict(user_today_values_scaled)[0][0]
prediction_3_months = model_3_months.predict(user_today_values_scaled)[0][0]
prediction_4_months = model_4_months.predict(user_today_values_scaled)[0][0]
prediction_5_months = model_5_months.predict(user_today_values_scaled)[0][0]
prediction_6_months = model_6_months.predict(user_today_values_scaled)[0][0]
prediction_7_months = model_7_months.predict(user_today_values_scaled)[0][0]
prediction_8_months = model_8_months.predict(user_today_values_scaled)[0][0]
prediction_9_months = model_9_months.predict(user_today_values_scaled)[0][0]

# Print the predictions for all time horizons
print("Predicted Close for 1 day ahead:", prediction_1_day)
print("Predicted Close for 1 week ahead:", prediction_1_week)
print("Predicted Close for 1 month ahead:", prediction_1_month)
print("Predicted Close for 2 months ahead:", prediction_2_months)
print("Predicted Close for 3 months ahead:", prediction_3_months)
print("Predicted Close for 4 months ahead:", prediction_4_months)
print("Predicted Close for 5 months ahead:", prediction_5_months)
print("Predicted Close for 6 months ahead:", prediction_6_months)
print("Predicted Close for 7 months ahead:", prediction_7_months)
print("Predicted Close for 8 months ahead:", prediction_8_months)
print("Predicted Close for 9 months ahead:", prediction_9_months)

#NOTE: RESULTS:

#==================================================OK!


#====================================================!