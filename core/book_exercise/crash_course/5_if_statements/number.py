numbers = [number for number in range(1, 12)]
print(numbers)
multiple_of_3 = []
multiple_of_2 = []
prime_numbers = []
for number in numbers:
    if number % 3 == 0:
        multiple_of_3.append(number)
    elif number % 2 == 0:
        multiple_of_2.append(number)
    else:
        prime_numbers.append(number)
print("Multiple of 2: ", multiple_of_2)
print("\nMultiple of 3: ", multiple_of_3)
print("\nPrime number: ", prime_numbers)

# code applicable to limited range ;;;;;fails for 12, 18, 24, 25 etc.......... logical errors
