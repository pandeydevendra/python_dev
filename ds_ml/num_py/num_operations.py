import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [10, 20, 30]])  # three_dimensional array
print("3-D Array:\n {}".format(a))
print("Dimesions:", a.ndim) #?????? yes it's a 2-D array
print("Data Type:", a.dtype)

print("Max: ", a.max)
print("Principal Diagonal: ", a.diagonal())
print("Mean: ", a.mean())
print("Min", a.min())
print("Trace of det(a): ", a.trace())
print("Transpose of det(a): ", a.transpose())