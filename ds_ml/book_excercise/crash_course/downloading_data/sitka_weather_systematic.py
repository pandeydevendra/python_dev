import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    """Call the method csv.reader() to create a reader object and store it in the reader"""
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, colum_header in enumerate(header_row):
    #     print(index, colum_header)

    dates, highs, lows = [], [], []
    for row in reader:
        # Convert string to date object
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
    print(len(highs))
    # print(dates)

    # Draw graphics according to the data, alpha is the transparency setting
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='g', alpha=0.1)  # Color the chart area
    # Set graphics format
    plt.title("Daliy high and low temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    # Draw slanted date labels
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
