
# more precise:
fact = (lambda n: 1 if n == 0 else n * fact(n - 1))(int(input("Enter the value of n: ")))
print("line 34: Factorial is {}.".format(fact))

# NameError: name 'fact' is not defined