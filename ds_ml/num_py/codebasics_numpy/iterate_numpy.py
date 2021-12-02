import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)
for row in a:
    print(row)

for x in a:
    print(x.reshape(4, 1))

for row in a:
    for cell in row:
        print(cell)
print("")

for cell in a.flatten():
    print(cell)

print(" ")
print(f"In 'C' it's Row_wise:-")
for x in np.nditer(a, order='C'):  # 'C' for "C-Language"
    print(f"{x}")

print(" ")

print(f"In 'Fortran' it's Column_wise:-")
for x in np.nditer(a, order='F'):  # 'F' for "Fortran-Language"
    print(f"{x}")

print(" ")
for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)

print(" ")
for x in np.nditer(a, order='C', flags=['external_loop']):
    print(x)

print(" ")
for x in np.nditer(a, op_flags=['readwrite']):
    print(x)
print(a)

print(" ")
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
print(a)

# simultaneous iteration:
b = np.array([[3,5,12]]) .reshape(3,1)
print(b)

for x,y in np.nditer([a,b]):
    print(x,y)