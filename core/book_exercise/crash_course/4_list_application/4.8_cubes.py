# cubes = "list(range())"  will not work here
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

cubes = []
for num in range(1, 11):
    cube = num ** 3
    cubes.append(cube)
    print(cubes)
print(cubes)
