"""
Creating an empty list initially;
then appending obtained values in steps under loop

"""
squares = []
for number in range(1, 11):  # never miss a colon (:) for loop syntax
    square = number ** 2
    squares.append(square)
    print(squares)  # values get printed at every steps; as it is inside the loop
print(squares)  # final list of values get printed at last; as it is outside the loop
# Observe the difference between the above two 'print' commands.

# comprehending above program:

print("\n")
squares = []
for number in range(1, 11):  # never miss a colon (:) for loop syntax
    # square = number**2
    squares.append(number ** 2)  # without creating a variable square, directly operate on its assigned value
print(squares)
print("\n")

# further comprehension of the above program:
# squares = [number**2, number in range(1, 16)]  # comma (,) doesn't work
squares = [number ** 2 for number in range(1, 16)]  # replace comma (,) with 'for'
print(squares)
# number; a variable can be any suitable name
squares = [value ** 2 for value in range(1, 31)]
print(squares)

# cube
cubes = [number ** 3 for number in range(1, 21)]
print(cubes)
