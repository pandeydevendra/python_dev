import csv
import matplotlib.pyplot as plt  # come to this step after getting that 'highs'

filename = 'sitka_weather_07_2014.csv'
with open(filename) as f:
    read_1 = csv.reader(f)
    header_row = next(read_1)
    print(header_row)

    # print(header_row) # it gives a list of all header_row.

    for index, column_header in enumerate(header_row):
        print(index, column_header)

        # to get high temperatures from file:

    highs = []
    for row in read_1:
        # highs.append((row[1])) # ['64', '71', '64', '59',...............]
        highs.append(int(row[1]))

    print(highs)

# plot data..

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')
# plt.show()

# Format plot.
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
