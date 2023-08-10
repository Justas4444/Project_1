This is my final project. I'm using AI to predict stock market future prices, will add django web application to display the results for registered users.

Folder structure
csv folder contains python code to generate SPY.csv, used for training and validation of a transformer model. It also generated interest_rate.csv that is appended to SPY.csv later in the code so can be used as a reference.

Trained_models folder contains python file that has two functions, train() and predict(). Once the models are trained, saving them will take place and training function can be commented. Predict function will load models and will use them for predictions with a step of 1 day.

mysite1 is a folder containing django website that displays predictions to registered users. NDX.py and SPX.py populate sqlite3 database with predictions from previously mentioned csv files.

How does it work?
To run code, please install all modules from requirements.txt

Models predictions are appended to SPY.csv in csv folder and instead of date as first element in row, they will contain the number of days in the future that the model is predicting which in turn depends on what range is selected in a loop that comes after train and predict functions.

Transformer model was chosen after trialing linear dispersion, dense layer and lstm models, which all turned out to be less accurate in terms of mae(mean absolute error).

I have used 2000 epochs as a base for training, after trying multiple options, as it turned out to be more accurate that 1000 or 500. Lower epochs values were not converging yet so I quickly switched to higher values.

A possible improvement to this model could be early stopping callback to detect convergence and more importantly restore optimal weights, while reducing training time. Althought to me it proved to be less accurate, I am sure having more time to play with settings it could have worked.
