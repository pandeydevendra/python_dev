print("Exceptional Calculation:>>")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
try:
    z = x / y
    print("Division is ", z)
except (TypeError, ValueError, ZeroDivisionError):
    print("Invalid attempt f division.")
except:
    print("Default Exception!!")
else:
    print("No exceptional error.")
finally:
    print("This completes the program.")
print("This is the last line.")

print("\nExceptional Calculation2:>>")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if y == 0:
    raise ZeroDivisionError("Denominator cannot be zero.")
    # ZeroDivisionError: Denominator cannot be zero. exception raised not handled
z = x / y
print("Division is ", z)

print("\nExceptional Calculation3:>>")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
try:
    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
        # ZeroDivisionError: Denominator cannot be zero. exception raised and handled
    z = x / y
    print("Division is ", z)
except ZeroDivisionError:
    print("Can't be divide by zero.")
