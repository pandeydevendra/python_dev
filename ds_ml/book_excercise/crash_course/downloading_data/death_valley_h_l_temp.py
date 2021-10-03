import csv
from datetime import datetime
import matplotlib.pyplot as plt  # come to this step after getting that 'highs'

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # to get high temperatures from file:
    # try - except - else block to handle missing data
    dates, highs, lows = [], [], []
    for row in reader:
        # print(row)
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # print(highs)
    # print(len(highs))

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='r')
plt.plot(dates, lows, c='b')

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.title("death_valley_2014 : high_low_temperatures", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
