import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense
import os

def train_SPX():
    # Load the historical stock price data from "formatted_data.csv"
    data = pd.read_csv("csv/SPX.csv")

    # Prepare the features and target variables
    X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
    y1 = data["Open"]
    y2 = data["High"]
    y3 = data["Low"]
    y4 = data["Close"]
    y5 = data["Adj Close"]
    y6 = data["Volume"]
    y7 = data["Interest Rate"]

    # Normalize the data using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Define the input shape for the Transformer model
    input_shape = (X_scaled.shape[1],)

    def transformer_model(input_shape):
        inputs = Input(shape=input_shape)
        x = inputs

        # Implement Transformer layers here
        # Add your custom Transformer architecture here
        x = Dense(128, activation='relu')(x)
        x = Dense(64, activation='relu')(x)
        x = Dense(32, activation='relu')(x)
        return Model(inputs, x)

    # Create separate models for each target variable
    model_open = transformer_model(input_shape)
    model_high = transformer_model(input_shape)
    model_low = transformer_model(input_shape)
    model_close = transformer_model(input_shape)
    model_adj_close = transformer_model(input_shape)
    model_volume = transformer_model(input_shape)
    model_interest_rate = transformer_model(input_shape)

    # Compile each model
    def compile_model(model):
        x = Dense(1, activation='linear')(model.output)
        model = Model(model.input, x)
        model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        return model

    model_open = compile_model(model_open)
    model_high = compile_model(model_high)
    model_low = compile_model(model_low)
    model_close = compile_model(model_close)
    model_adj_close = compile_model(model_adj_close)
    model_volume = compile_model(model_volume)
    model_interest_rate = compile_model(model_interest_rate)

    # Split the data into training and testing sets for each target variable
    X_train, X_test, y1_train, y1_test = train_test_split(X_scaled, y1, test_size=0.2, random_state=42)
    _, _, y2_train, y2_test = train_test_split(X_scaled, y2, test_size=0.2, random_state=42)
    _, _, y3_train, y3_test = train_test_split(X_scaled, y3, test_size=0.2, random_state=42)
    _, _, y4_train, y4_test = train_test_split(X_scaled, y4, test_size=0.2, random_state=42)
    _, _, y5_train, y5_test = train_test_split(X_scaled, y5, test_size=0.2, random_state=42)
    _, _, y6_train, y6_test = train_test_split(X_scaled, y6, test_size=0.2, random_state=42)
    _, _, y7_train, y7_test = train_test_split(X_scaled, y7, test_size=0.2, random_state=42)

    # Train each model separately
    epochs = 2000
    batch_size = 128

    model_open.fit(X_train, y1_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_high.fit(X_train, y2_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_low.fit(X_train, y3_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_close.fit(X_train, y4_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_adj_close.fit(X_train, y5_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_volume.fit(X_train, y6_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)
    model_interest_rate.fit(X_train, y7_train, epochs=epochs, batch_size=batch_size, validation_split=0.2)

    # Evaluate each model
    _, mae_open = model_open.evaluate(X_test, y1_test)
    _, mae_high = model_high.evaluate(X_test, y2_test)
    _, mae_low = model_low.evaluate(X_test, y3_test)
    _, mae_close = model_close.evaluate(X_test, y4_test)
    _, mae_adj_close = model_adj_close.evaluate(X_test, y5_test)
    _, mae_volume = model_volume.evaluate(X_test, y6_test)
    _, mae_interest_rate = model_interest_rate.evaluate(X_test, y7_test)

    # print("MAE for 'Open' Price:", mae_open)
    # print("MAE for 'High' Price:", mae_high)
    # print("MAE for 'Low' Price:", mae_low)
    # print("MAE for 'Close' Price:", mae_close)
    # print("MAE for 'Adj Close' Price:", mae_adj_close)
    # print("MAE for 'Volume':", mae_volume)
    # print("MAE for 'Interest Rate':", mae_interest_rate)

    model_open.save("trained_models/SPX_model_open.h5")
    model_high.save("trained_models/SPX_model_high.h5")
    model_low.save("trained_models/SPX_model_low.h5")
    model_close.save("trained_models/SPX_model_close.h5")
    model_adj_close.save("trained_models/SPX_model_adj_close.h5")
    model_volume.save("trained_models/SPX_model_volume.h5")
    model_interest_rate.save("trained_models/SPX_model_interest_rate.h5")

# train_SPX()

def predict_SPX():
    data = pd.read_csv("csv/SPX.csv")

    # Prepare the features and target variables
    X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]

    # Normalize the data using StandardScaler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    #Load models
    model_open = tf.keras.models.load_model("trained_models/SPX_model_open.h5")
    model_high = tf.keras.models.load_model("trained_models/SPX_model_high.h5")
    model_low = tf.keras.models.load_model("trained_models/SPX_model_low.h5")
    model_close = tf.keras.models.load_model("trained_models/SPX_model_close.h5")
    model_adj_close = tf.keras.models.load_model("trained_models/SPX_model_adj_close.h5")
    model_volume = tf.keras.models.load_model("trained_models/SPX_model_volume.h5")
    model_interest_rate = tf.keras.models.load_model("trained_models/SPX_model_interest_rate.h5")

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

    # print(f'Open prediction: {prediction_open}')
    # print(f'High prediction: {prediction_high}')
    # print(f'Low prediction: {prediction_low}')
    # print(f'Close prediction: {prediction_close}')
    # print(f'Adj Close prediction: {prediction_adj_close}')
    # print(f'Volume prediction: {prediction_volume}')
    # print(f'Interest Rate prediction: {prediction_interest_rate}')

    # Convert the predicted values to a list
    predicted_values = [
        f"+{i} trading day",
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

    csv_file = "csv/SPX.csv"

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

# for i in range(1,91):
#     predict_SPX()