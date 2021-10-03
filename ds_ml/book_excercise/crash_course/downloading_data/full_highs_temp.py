import matplotlib.pyplot as plt  # come to this step after getting that 'highs'

import csv
from datetime import datetime

f_name = 'sitka_weather_2014.csv'  # file has been changed to get a full year data....

with open(f_name) as f:
    f_read = csv.reader(f)
    head_row = next(f_read)
    print(head_row)

    h_temps = []
    l_temps = []
    dates = []
    for row in f_read:
        c_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(c_date)

        # h_temp = int(row[1])
        # h_temps.append(h_temp)
        h_temps.append(int(row[1]))
        l_temps.append(int(row[3]))

    # print(h_temps)
    # print(dates)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, h_temps, c='red')
plt.plot(dates, l_temps, c='b')
fig.autofmt_xdate()

# Shading an Area in the Chart:::
plt.fill_between(dates, h_temps, l_temps, facecolor='blue', alpha=0.1)
# plt.show()

# Format plot.

plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
