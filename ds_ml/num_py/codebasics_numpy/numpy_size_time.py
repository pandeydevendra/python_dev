import numpy as np
import time
import sys

# size_concept:

l = range(1000)
print(l)
print(sys.getsizeof(1))  # size of one object = 28 bytes
print(sys.getsizeof(1) * len(l))  # size of the complete list = 28000 bytes

array = np.arange(1000)
# print(array)
print(array.itemsize)  # size of one object = 8 bytes
print(array.size * array.itemsize)  # size of complete array = 8000 bytes

"""
output 
range(0, 1000)
28
28000
8
8000
"""

# time_concept:
size = 1000000
l1 = range(size)
l2 = range(size)
result_l12 = zip(l1, l2)
# print(result_l12)
a1 = np.arange(size)
a2 = np.arange(size)
result_a12 = a1 + a2
# print(len(result_a12))

start = time.time()

print(f"python list took: {(time.time() - start) * 1000000}")

start = time.time()

print(f"numpy took: {(time.time() - start) * 1000000}")

# time++
l_start = time.time()
comprehension_list_12 = [(x + y) for x, y in zip(l1, l2)]
print(f"python list took: {(time.time() - l_start) * 1000}")
# time by default is in seconds ; *ly by 1000 to make it milliseconds

np_start = time.time()
np_result_12 = a1 + a2
print(f"numpy took: {(time.time() - np_start) * 1000}")
