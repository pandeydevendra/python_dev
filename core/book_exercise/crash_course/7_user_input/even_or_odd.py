number = input("Enter a number, and I'll tell you if it's multiple of 10 or not: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print(f"{number} is odd.")
    print("\nThe number " + str(number) + " is odd.")