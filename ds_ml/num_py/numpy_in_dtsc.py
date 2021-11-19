import numpy as np

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
# a, b ; 1-D arrays
print(np.dot(a, b))

# transpose of a matrix
print(np.transpose(a))

x = [1, 2]  # 1-D array ; a matrix., 1*2 == R*C
y = [[2, 4, 6], [3, 5, 7]]  # 2-D array ; a matrix., 2*3
print(np.dot(x, y))  # output > [1*2]*[2*3] = [1*3]

z = [[8], [9], [10]]  # 3-D array ; a matrix., 3*1 == R*C
print(np.dot(y, z))  # output > [2*3]*[3*1] = [2*1]


gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

point = [[[4, 2, 1]]]
medals = [[gold], [silver], [bronze]]
print(f"{point} \n{medals}")
print(f"{type(point)} \n{type(medals)}")

print(np.transpose(b))
print(f"z = {z}")
t_z = np.transpose(z)
print(f"Tanspose of z = {t_z}")
print((f"{type(t_z)}"))

print(np.dot(z, t_z))

point = [4, 2, 1]
t_point = np.transpose(point)
print(f"{point} {type(point)} \n{t_point} {type(t_point)}")

points = [[4, 2, 1]]
t_points = np.transpose(points)
print(f"{points} {type(points)} \n{t_points} {type(t_points)}")


medals = [np.array(gold), np.array(silver), np.array(bronze)]
medals = [[gold], [silver], [bronze]]
medals1 = [gold, silver, bronze]
print(medals, type(np.array(medals)))
print(medals1, type(np.array(medals1)))

total_point = np.dot(t_points, medals)
print(f"{total_point}")

total_point = np.dot(point, medals1)
print(f"{total_point}")