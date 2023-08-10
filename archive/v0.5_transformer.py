import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense
import os

# def train():
    # Load the historical stock price data from "formatted_data.csv"
    # data = pd.read_csv("csv/SPY.csv")

    # # Prepare the features and target variables
    # X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
    # y1 = data["Open"]
    # y2 = data["High"]
    # y3 = data["Low"]
    # y4 = data["Close"]
    # y5 = data["Adj Close"]
    # y6 = data["Volume"]
    # y7 = data["Interest Rate"]

    # # Normalize the data using StandardScaler
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)

    # # Split the data into training and testing sets for each target variable
    # X_train, X_test, y1_train, y1_test = train_test_split(X_scaled, y1, test_size=0.2, random_state=42)
    # X_train, X_test, y2_train, y2_test = train_test_split(X_scaled, y2, test_size=0.2, random_state=42)
    # X_train, X_test, y3_train, y3_test = train_test_split(X_scaled, y3, test_size=0.2, random_state=42)
    # X_train, X_test, y4_train, y4_test = train_test_split(X_scaled, y4, test_size=0.2, random_state=42)
    # X_train, X_test, y5_train, y5_test = train_test_split(X_scaled, y5, test_size=0.2, random_state=42)
    # X_train, X_test, y6_train, y6_test = train_test_split(X_scaled, y6, test_size=0.2, random_state=42)
    # X_train, X_test, y7_train, y7_test = train_test_split(X_scaled, y7, test_size=0.2, random_state=42)

    # def transformer_model(input_shape, output_shape):
    #     inputs = Input(shape=input_shape)
    #     x = inputs

    #     # Implement Transformer layers here
    #     # Add your custom Transformer architecture here
    #     x = Dense(128, activation='relu')(x)
    #     x = Dense(64, activation='relu')(x)
    #     x = Dense(32, activation='relu')(x)
    #     x = Dense(1, activation='linear')(x)
    #     outputs = Dense(output_shape, activation='linear')(x)

    #     model = Model(inputs, outputs)
    #     return model

    # # Define the input and output shapes for the Transformer model
    # input_shape = (X_train.shape[1],)
    # output_shape = 1

    # # Create the 1-day Transformer model for "Open" price
    # model_open = transformer_model(input_shape, output_shape)
    # model_open.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_open.fit(X_train, y1_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_open.save("trained_models/trained_model_open.h5")

    # # Create the 1-day Transformer model for "High" price
    # model_high = transformer_model(input_shape, output_shape)
    # model_high.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_high.fit(X_train, y2_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_high.save("trained_models/trained_model_high.h5")

    # # Create the 1-day Transformer model for "Low" price
    # model_low = transformer_model(input_shape, output_shape)
    # model_low.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_low.fit(X_train, y3_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_low.save("trained_models/trained_model_low.h5")

    # # Create the 1-day Transformer model for "Close" price
    # model_close = transformer_model(input_shape, output_shape)
    # model_close.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_close.fit(X_train, y4_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_close.save("trained_models/trained_model_close.h5")

    # # Create the 1-day Transformer model for "Adj Close" price
    # model_adj_close = transformer_model(input_shape, output_shape)
    # model_adj_close.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_adj_close.fit(X_train, y5_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_adj_close.save("trained_models/trained_model_adj_close.h5")

    # # Create the 1-day Transformer model for "Volume"
    # model_volume = transformer_model(input_shape, output_shape)
    # model_volume.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_volume.fit(X_train, y6_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_volume.save("trained_models/trained_model_volume.h5")

    # # Create the 1-day Transformer model for "Interest Rate"
    # model_interest_rate = transformer_model(input_shape, output_shape)
    # model_interest_rate.compile(optimizer='adam', loss='mse', metrics=['mae'])
    # model_interest_rate.fit(X_train, y7_train, epochs=2000, batch_size=128, validation_split=0.2)
    # model_interest_rate.save("trained_models/trained_model_interest_rate.h5")

# train()

#----------------------------------------------------------------------------------------

def predict():
    data = pd.read_csv("csv/SPY.csv")

    # Prepare the features and target variables
    X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
   
    # Normalize the data using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #Load models
    model_open = tf.keras.models.load_model("trained_models/trained_model_open.h5")
    model_high = tf.keras.models.load_model("trained_models/trained_model_high.h5")
    model_low = tf.keras.models.load_model("trained_models/trained_model_low.h5")
    model_close = tf.keras.models.load_model("trained_models/trained_model_close.h5")
    model_adj_close = tf.keras.models.load_model("trained_models/trained_model_adj_close.h5")
    model_volume = tf.keras.models.load_model("trained_models/trained_model_volume.h5")
    model_interest_rate = tf.keras.models.load_model("trained_models/trained_model_interest_rate.h5")

    # Extract the last row of data for tomorrow's prediction
    today_values = X_scaled[-1]

    # Reshape the data for prediction
    user_today_values_scaled = today_values.reshape(1, -1)
    # Make predictions for 1-day and using the trained models
    prediction_open = model_open.predict(user_today_values_scaled)[0][0]
    prediction_high = model_high.predict(user_today_values_scaled)[0][0]
    prediction_low = model_low.predict(user_today_values_scaled)[0][0]
    prediction_close = model_close.predict(user_today_values_scaled)[0][0]
    prediction_adj_close = model_adj_close.predict(user_today_values_scaled)[0][0]
    prediction_volume = model_volume.predict(user_today_values_scaled)[0][0]
    prediction_interest_rate = model_interest_rate.predict(user_today_values_scaled)[0][0]

    print(f'Open prediction: {prediction_open}')
    print(f'High prediction: {prediction_high}')
    print(f'Low prediction: {prediction_low}')
    print(f'Close prediction: {prediction_close}')
    print(f'Adj Close prediction: {prediction_adj_close}')
    print(f'Volume prediction: {prediction_volume}')
    print(f'Interest Rate prediction: {prediction_interest_rate}')

    # Convert the predicted values to a list
    predicted_values = [
        "+1 trading day",
        int(prediction_open),
        int(prediction_high),
        int(prediction_low),
        int(prediction_close),
        int(prediction_adj_close),
        int(prediction_volume),
        f"{prediction_interest_rate:.2f}"
    ]

    # Convert the list to a comma-separated string
    new_row = ",".join(str(value) for value in predicted_values)

    csv_file = "csv/SPY.csv"

    # Read the last line of the CSV to check if it ends with a newline
    with open(csv_file, "rb") as f:
        f.seek(-2, os.SEEK_END)  # Move to the second-to-last character
        last_chars = f.read(2)

    # Check if the last line ends with a newline character
    has_newline = last_chars.endswith(b"\r\n") or last_chars.endswith(b"\n")

    # Append the new row with or without a newline based on the last line``
    with open(csv_file, "a") as f:
        if has_newline:
            f.write(new_row + "\n")
        else:
            f.write("\n" + new_row)

for i in range(30):
    predict()

#----------------------------------------------------------------------------------------