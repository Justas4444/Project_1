import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Model
from keras.layers import Input, Dense

# Load the historical stock price data from "formatted_data.csv"
data = pd.read_csv("csv/SPY.csv")

# Prepare the features and target variables
X = data[["Open", "High", "Low", "Close", "Adj Close", "Volume", "Interest Rate"]]
y = data["Close"]

# Normalize the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

def transformer_model(input_shape, output_shape):
    inputs = Input(shape=input_shape)
    x = inputs

    # Implement Transformer layers here
    # Add your custom Transformer architecture here
    x = Dense(128, activation='relu')(x)
    x = Dense(64, activation='relu')(x)
    x = Dense(32, activation='relu')(x)
    x = Dense(1, activation='linear')(x)
    outputs = Dense(output_shape, activation='linear')(x)

    model = Model(inputs, outputs)
    return model


# Define the input and output shapes for the Transformer model
input_shape = (X_train.shape[1],)
output_shape = 1

# Create the 1-day Transformer model
model_1_day = transformer_model(input_shape, output_shape)

model_1_day.compile(optimizer='adam', loss='mse', metrics=['mae'])
model_1_day.fit(X_train, y_train, epochs=20, batch_size=128, validation_split=0.2)

loss, mean_absolute_error = model_1_day.evaluate(X_test, y_test)
print(f"1-day Test mean absolute error: {mean_absolute_error}")

model_1_day.save("trained_models/trained_model_1_day.h5")

#----------------------------------------------------------------------------------------
# Load the trained models for 1-day and 1-12 month forecasts
model_1_day = tf.keras.models.load_model("trained_models/trained_model_1_day.h5")

# Extract the last row of data for tomorrow's prediction
today_values = X_scaled[-1]

# Reshape the data for prediction
user_today_values_scaled = today_values.reshape(1, -1)

# Make predictions for 1-day and using the trained models
prediction_1_day = model_1_day.predict(user_today_values_scaled)[0][0]

print(f'Transformers\nPrediction for tomorrow: {prediction_1_day}')




#Day 1.
# True=4521, Predict=4526
 
#Day 2.
# True=4542, Predict=4522

#Day 3.
# True=, Predict=4538

#Day 4.
# True=, Predict=

#Day 5.
# True=, Predict=








#--------------------------------------------------

#Day 1. 3747

#Winner!
#epochs-1000: 3847
#epochs-500: 3852
#epochs-250: 3869
#epochs-125: 3876
#epochs-50: 3931

#Day 2. 3675
#Winner!
#epochs-1000: 3666
#epochs-500: 3657
#epochs-250: 3655
#epochs-125: 3628
#epochs-50: 3634

#Day 3. 4372
#Winner!
#epochs-1000: 4404
#epochs-500: 4408
#epochs-250: 4392
#epochs-125: 4369
#epochs-50: 4372

#Day 4. 4053
#Winner!
#epochs-1000: 4066
#epochs-500: 4065
#epochs-250: 4055
#epochs-125: 4060
#epochs-50: 4084

#Day 5. 2817
# #Winner!
#epochs-1000: 2925
#epochs-500: 2925
#epochs-250: 2926
#epochs-125: 2926
#epochs-50: 2938

#Day 5. 2693
# #Winner!
#epochs-1000: 2699
#epochs-500: 2703
#epochs-250: 2702
#epochs-125: 2694
#epochs-50: 2682