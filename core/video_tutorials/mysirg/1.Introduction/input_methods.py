name = input("Enter your name: ")
print(f"Hello {name.title()}")


fname, lname = input("Enter your full name: ").split()
print(f"Hello {fname.title()} {lname.title()}.")


a, b = input("Enter two comma-separated values: ").split(",")
print(f"The values were {a} and {b}")

a, b, c = input("Enter three comma-separated values: ").split(",")
print(f"The values were {a}, {b}, and {c}")


a, b, c, d, e = input("Enter five comma-separated values: ").split(",")
print(f"The values were {a}, {b}, {c}, {d}, and {e}")