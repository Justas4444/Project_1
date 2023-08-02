import sqlite3
import csv
from datetime import datetime, timedelta, date

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

def is_weekend(dt):
    return dt.weekday() in [5, 6]  # Saturday is 5, Sunday is 6

def read_csv_file(csv_file):
    last_90_rows = []
    with open(csv_file, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            last_90_rows.append(row)
            if len(last_90_rows) > 90:
                last_90_rows.pop(0)

    start_date = datetime.now().date()  # Get the current date
    predicted_date = start_date
    for row in last_90_rows:
        # Increment the date by one day until we reach a weekday
        while is_weekend(predicted_date):
            predicted_date += timedelta(days=1)

        new_row_data = (
            predicted_date,
            int(row[1]),
            int(row[2]),
            int(row[3]),
            int(row[4]),
            int(row[5]),
            int(row[6]),
            int(2),
            float(row[7]),
        )
        c.execute("INSERT INTO app1_stockprediction (predicted_date, predicted_open, predicted_high, predicted_low, predicted_close, predicted_adjclose, predicted_volume, stock_symbol_id, predicted_interest_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", new_row_data)

        # Increment the date by one day for the next row
        predicted_date += timedelta(days=1)

    conn.commit()

if __name__ == "__main__":
    csv_file = r"C:\Users\Admin\Desktop\Coding\PTU13\AI\csv\NDX.csv"
    read_csv_file(csv_file)

c.close()
conn.close()