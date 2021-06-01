# write a python script to create a list of 1st N natural number, where N is given by user
N = int(input("Enter the value of N: "))
natural_list = [num for num in range(1, N + 1)]
print(natural_list)

# write a python script to create a list of 1st N natural number using for loop, where N is given by user

square_natural_list = []
for value in natural_list:
    sq_value = value ** 2
    square_natural_list.append(sq_value)
print(square_natural_list)

# write a python script to create a list of 1st N natural number, where N is given by user
N = int(input("Enter the value of N: "))
square_natural_list = [num ** 2 for num in range(1, N + 1)]
print(square_natural_list)
