number = input("Enter a number, and I'll tell you if it's multiple of 10 or not: ")
number = int(number)
if number % 10 == 0:
    print("\nThe number " + str(number) + " is multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
    print("\nThe number " + str(number) + " is not a multiple of 10.")


def multiple(n):
    if n % 10 == 0:
        result = f"\n{n} is multiple of 10."
    else:
        result = f"{n} is not a multiple of 10."

    return result


print(multiple(number))
# print(result)
