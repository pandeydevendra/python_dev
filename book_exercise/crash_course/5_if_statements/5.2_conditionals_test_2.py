car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
# checking in list
banned_users = ['andrew', 'carolina', 'david', 'john']
print("banned_users are : {}".format(banned_users))
banned_users = 'subaru'
print("Is andrew banned? I predict True.")
print(banned_users[0] in banned_users)

print("2nd last banned user is david. yes! True")
print(banned_users[-2] == 'david')
print("\njohn is banned. yes! True. ")
print('john' in banned_users)
print("\ncarolina is not banned. no! Its not True. ")
print('carolina' not in banned_users)

# checking in list with lower() function:

biggest_cities = ['newyork', 'beijing', 'mumbai', 'tokyo', 'london']
fat_cities = []
for city in biggest_cities:
    fat_cities.append(city.title())
print(fat_cities)
for city in fat_cities:
    if city.lower() == 'beijing':
        print("{} is the capital city of China.".format(city))

# checking for equality and inequality ; numbers list
numbers = [number for number in range(1, 31, 2)]
print("\n", numbers)
print(numbers[0])
print(numbers)
print("first number in the list is {}.".format(numbers[0]), "yes!True")
print(numbers[0] == 1)
print("{} is in the middle of the list.".format(numbers[7]), "yes!True")
print(numbers[7] == 15)

# equality:
numbers[-1] == 30
print(numbers[-1 == 30])
print("last number is 30.\n", numbers[-1 == 30])  # It seems something different :gives value in boolean
print(numbers[-1] == 28)
# inequality:
print("<, >, <= and >=")
print(numbers[-1] <= 30)
print(numbers[-1 <= 30])  # It seems something different :gives value in boolean
print("{} is less than 10. ".format(numbers[3]), numbers[3] <= 10)

# and & or: with if statement
print("\n", numbers)
# and
if numbers[2] > 1 and numbers[3] <= 10:
    print("\nBoth conditions {} > 1 and {} <= 10 are satisfied. Predict True".format(numbers[2], numbers[3]))
    print(numbers[2] > 1 and numbers[3] <= 10)
else:
    print("\nBoth conditions {} > 1 and {} <= 10 or any of two are unsatisfied. Predict False".format(numbers[2],
                                                                                                      numbers[3]))
    print(numbers[2] > 1 and numbers[3] <= 10)

if numbers[2] >= 5 and numbers[3] >= 10:
    print("\nBoth conditions {} >= 5 and {} >= 10 are satisfied. Predict True".format(numbers[2], numbers[3]))
    print(numbers[2] >= 5 and numbers[3] >= 10)
else:
    print("\nBoth conditions {} >= 5 and {} >= 10 or any of two are unsatisfied. Predict False".format(numbers[2],
                                                                                                       numbers[3]))
    print(numbers[2] >= 5 and numbers[3] >= 10)

# or

if numbers[2] > 1 or numbers[3] <= 10:
    print("\nBoth or any conditions {} > 1 or {} <= 10 are satisfied. Predict True".format(numbers[2], numbers[3]))
    print(numbers[2] > 1 or numbers[3] <= 10)
else:
    print("\nBoth conditions {} > 1 or {} <= 10 are unsatisfied. Predict False".format(numbers[2], numbers[3]))
    print(numbers[2] > 1 or numbers[3] <= 10)

if numbers[2] >= 5 or numbers[3] >= 10:
    print("\nBoth or any conditions {} >= 5 or {} >= 10 are satisfied. Predict True".format(numbers[2], numbers[3]))
    print(numbers[2] >= 5 or numbers[3] >= 10)
else:
    print("\nBoth conditions {} >= 5 or {} >= 10 are unsatisfied. Predict False".format(numbers[2], numbers[3]))
    print(numbers[2] >= 5 or numbers[3] >= 10)
if numbers[5] <= 5 or numbers[10] <= 10:
    print("\nBoth or any conditions {} <= 5 or {} <= 10 are satisfied. Predict True".format(numbers[5], numbers[10]))
    print(numbers[5] <= 5 or numbers[10] <= 10)
else:
    print("\nBoth conditions {} <= 5 or {} <= 10 are unsatisfied. Predict False".format(numbers[5], numbers[10]))
    print(numbers[5] <= 5 or numbers[10] <= 10)
