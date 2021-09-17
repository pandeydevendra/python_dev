import numpy as np

a = []
print(a)
print(type(a))
bit_length = a.__len__()
print(bit_length)
print()
n = np.array([])
print(n)
print(type(n))
bit_length = n.__len__()
print(bit_length)
print()
a = np.array([1, 2, 3])
print(a)
print(type(a))
bit_length = a.__len__()
print(bit_length)
print()
x = a + 5
print(x)
print(type(x))
bit_length = x.__len__()
print(bit_length)

"""
l = [1,2,3]
print(l)  # [1, 2, 3]
print(type(l))  # <class 'list'>

s = l + 5
# TypeError: can only concatenate list (not "int") to list
print(s)
# TypeError: can only concatenate list (not "int") to list

"""
print()

b = np.array([[1, 2, 3], [5, 6, 7]])
print(b)
print(type(b))
bit_length = b.__len__()
print(bit_length)

print()

y = b + 6
print(y)
print(type(y))
bit_length = y.__len__()
print(bit_length)
