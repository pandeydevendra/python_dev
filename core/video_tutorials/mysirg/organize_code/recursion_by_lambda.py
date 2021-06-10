# wrtie a code to get factorial of n:>>

# 1. by simple recursion:
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


number = int(input("Enter the value of n: "))
result = fact(number)
print(f"Line 13: Factorial of {number} is {result}.".format(number, result))
# # @ Note f

# 2. by lambda recursion:
"""
name a factorial function as fact
"""

s = lambda n: 1 if n == 0 else n * s(n - 1)
n = int(input("Enter the value of n: "))
r = s(n)
print("Line 24: Factorial of {} is {} ".format(n, r))

# precise:
# fact = (lambda n: 1 if n == 0 else n * fact(n - 1))(int(input("Enter the value of n: ")))
# result = fact()
# print("Factorial is {}.".format(result))
# TypeError: 'int' object is not callable

# more precise:
fact = (lambda n: 1 if n == 0 else n * fact(n - 1))(int(input("Enter the value of n: ")))
print("line 34: Factorial is {}.".format(fact))

# NameError: name 'fact' is not defined
"""
Enter the value of n: 3
Line 13: Factorial of 3 is 6.
Enter the value of n: 4
Line 24: Factorial of 4 is 24 
Enter the value of n: 5
line 34: Factorial is 120.

Process finished with exit code 0
"""

# TODO check last program(L33,L34)