'''
We'll see why numpy is very popular and talk about its
main feature "n dimensional array". It is memory efficient,
fast and convenient compared to python native list.
h

'''
import numpy as np
import time
import sys

l = range(1000)  # create a list with thousand/1000 element in it

print(sys.getsizeof(5) * len(l))  # here 5 is any number between 0-999 // consume 24000 byte
'''
size of one python object list is 24 byte (64 byte Architecture)
'''

numPyarray = np.arange(1000)  # arange is funtion to create array element 0-999 // consume 8000 byte

print(numPyarray.size * numPyarray.itemsize);
'''
size of one  numbpy python object list is 8 byte (64 byte Architecture)
'''
a = np.array([1, 2, 3])  # one_dimensional array
print("1-D Array:\n {}".format(a))
print("Dimesions:", a.ndim)
print("Data Type:", a.dtype)

b = np.array([[1, 2, 3], [10, 20, 30]])  # two_dimensional array
print("2-D Array:\n {}".format(b))
print("Dimesions:", b.ndim)
print("Data Type:", b.dtype)

c = np.array([[1, 2, 3], [10, 20, 30], [4, 5, 6]])  # three_dimensional array
print("3-D Array:\n {}".format(c))
print("Dimesions:", c.ndim) #??????
print("Data Type:", c.dtype)

d = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [10, 20, 30]])  # three_dimensional array
print("3-D Array:\n {}".format(d))
print("Dimesions:", d.ndim) #??????
print("Data Type:", d.dtype)

# Changing datatype:
print("\nData Type of a:", a.dtype)
a = a.astype('float32')
print("New Data Type of a:", a.dtype)
print("\nData Type of b:", b.dtype)
b = b.astype('float64')
print("New Data Type of b:", b.dtype)
