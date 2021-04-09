numbers = [number for number in range(1, 21)]
print(numbers)
less_than_5 = []
between_5_10 = []
greater_than_10 = []
for number in numbers:
    if number < 5:
        less_than_5.append(number)
    elif number >= 5 and number <= 10:
        between_5_10.append(number)
    else:
        greater_than_10.append(number)
print(less_than_5)
print(between_5_10)
print(greater_than_10)

# TODO
