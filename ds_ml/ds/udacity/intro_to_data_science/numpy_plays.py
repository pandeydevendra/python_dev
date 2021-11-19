import numpy

a = [1, 2, 3, 4]
b = [3, 4, 2, 1]

print(f"a = {a}")
print(f"b = {b}")
# add
s = numpy.add(a, b)
print(f"Addition of a and b: {s}")

# join
s = a + b
print(f"Joining of a and b: {s}")

# more: standard ways;

ar_1 = numpy.array([1, 2, 3, 4])
ar_2 = numpy.array([3, 4, 2, 1])
ar_1_2 = ar_1 + ar_2
print(f"Addition of arrays a and b: {ar_1_2}")

c = [5, 6, 3, 2]

"""
#limitation of simple addition is that it can't work beyond two arrays
# sum = numpy.add(a,b,c)
# print(sum)
Traceback (most recent call last):
  File "/home/vins/Workspace/Py/python/ds_ml/ds/udacity/intro_to_data_science/numpy_plays.py", line 24, in <module>
    sum = numpy.add(a,b,c)
TypeError: return arrays must be of ArrayType
"""

# by standard method;

ar_3 = numpy.array(c)
print(f"c = {ar_3}")

ar_1_2_3 = ar_1 + ar_2 + ar_3
print(f"Addition of arrays a, b and c: {ar_1_2_3}")  # it works
