"""
x = int(input("Enter x: "))
y = input("Enter y: ")
print("Sum is ", x + y)

"""
# TypeError: unsupported operand type(s) for +: 'int' and 'str':;
print("Normal Calculation:>>")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Division is ", x / y)

"""
Enter x: 4
Enter y: 0
Traceback (most recent call last):
  File "/home/vins/Workspace/Py/python/core/video_tutorials/mysirg/organize_code/exception_handling.py", line 11, in <module>
    print("Division is ", x/y)
ZeroDivisionError: division by zero
"""

print("Exceptional Calculation:>>")
x = int(input("Enter x: "))
y = int(input("Enter y: "))
try:
    z = x / y
    print("Division is ", z)
except TypeError:
    print("Type Error Found!")
except ValueError:
    print("Value Error Found!")
except ZeroDivisionError:
    print("Can't be divide by zero.")
else:
    print("No exceptional error.")
finally:
    print("This completes the program.")
print("This is the last line.")
