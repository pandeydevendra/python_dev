#a =int(input("Enter a number to start the series:"))

f1 = 1
f2 = 1
next = f1 + f2
n =int(input("Enter a number to limit the series:"))
while f1 <= n:
    print(f1)
    f1 = f2
    f2 = next
    next = f1 + f2


