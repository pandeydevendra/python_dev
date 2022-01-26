def add(a, b):
    """

    @param a: int
    @param b: int
    @return: sum
    """
    sum = a + b
    return sum


a = int(input("Enter a: "))
b = int(input("Enter b: "))

s = add(a, b)
print(f"a = {a}, b = {b}")
print(f"Sum of {a} and {b} is {s}")

# docstring concept:
print(add(a, b).__doc__)


def add_more(a, b):
    """
    a and b are integers
    and hence sum is also an integer.
    """
    sum = a + b
    return sum


a = int(input("Enter a: "))
b = int(input("Enter b: "))

s = add(a, b)
print(f"a = {a}, b = {b}")
print(f"Sum of {a} and {b} is {s}")

print(add_more(a, b).__doc__)