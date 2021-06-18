# M1:
print("M1: \n")
y = 10  # Global variable
print("Global y= ", y)


def f1():
    x = 5  # Local variable
    print("Local x= ", x)
    print("Inside y= ", y)


f1()
# print("Outside x= ", x) # NameError: name 'x' is not defined

print("Outside y= ", y)

# M2:

print("\nM2: \n")
y = 10  # Global variable
print("Global y= ", y)


def f1():
    y = 5
    x = 5  # Local variable
    print("Local x= ", x)
    print("Inside y= ", y)


f1()
# print("Outside x= ", x) # NameError: name 'x' is not defined

print("Outside y= ", y)

# M3:

print("\nM3: \n")
y = 10  # Global variable
print("Global y= ", y)


def f1():
    global y
    y = 5
    print("Inside y= ", y)


f1()
print("Outside y= ", y)

# M4:

print("\nM4: \n")
y = 10  # Global variable
print("Global y= ", y)


def f1():
    y = 5
    # global y  ::: SyntaxError: name 'y' is assigned to before global declaration
    print("Inside y= ", y)


f1()
print("Outside y= ", y)

# M5:

print("\nM5: \n")


def f1():
    global y
    y = 5
    print("Inside y= ", y)


f1()
print("Outside y= ", y)

# M6:

print("\nM6: \n")

y = 10
print("Global y= ", y)


def f1():
    y = 5
    print("Inside y= ", y)
    print("Global y= ", globals()['y'])


f1()
print("Outside y= ", y)
