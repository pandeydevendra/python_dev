# method 1
odd_numbers = list(range(1, 20, 2))
print(odd_numbers, "\n")

# method 2
odd_numbers = []
for number in range(1, 20, 2):
    odd_numbers.append(number)
print(odd_numbers, "\n")

# method 3
odd_numbers = [value for value in range(1, 20, 2)]
print(odd_numbers)
