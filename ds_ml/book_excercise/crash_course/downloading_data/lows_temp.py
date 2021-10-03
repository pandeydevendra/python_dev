import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07_2014.csv'
with open(filename) as f:
    read_2 = csv.reader(f)
    header_row = next(read_2)
    # print(header_row)
    # to get the index of desired row..
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    # date = []
    # low_temp = []

    """
    for row in read_2:
        # print(row[3])
        # low_temp.append(row[2]) # ['56', '62', '58', '56'.....]
        # print(type(row[2])) # str type >> 'numbers'
        # to convert temp in int type
        low_temp.append(int(row[2]))
    """
    dates, low_temp = [], []
    for row in read_2:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        low_temp.append(int(row[3]))

print(low_temp)
# print(type(low_temp)) # list type

# plot data..

fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(low_temp, c='b')
# plt.show()

plt.plot(dates, low_temp, c = 'b')

fig.autofmt_xdate() # to inclined date on x axis >> look better in less space
# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()

# datetime on x axis::
