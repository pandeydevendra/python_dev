# Tuple = An immutable list.
"""
Sometimes you’ll want to create a list of items that cannot change.
Tuples allow you to do just that.
Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
"""

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)

# dimensions[0] = 250 # assigining new value similar to list
"""Traceback (most recent call last):
File "dimensions.py", line 3, in <module>
dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment"""

# Looping Through All Values in a Tuple:

for dimension in dimensions:
    print(dimension)
# looping is similar to list

# Writing over a Tuple:
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
# Python doesn’t raise any errors this time, because overwriting a variable is valid

#done