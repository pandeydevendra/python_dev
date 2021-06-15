fact = lambda n: 1 if n == 0 else n * fact(n - 1)  # (int(input("Enter the value of n: ")))
n = int(input("Enter the value of n: "))
print(f"Factorial of {n} is {fact(n)}.")
