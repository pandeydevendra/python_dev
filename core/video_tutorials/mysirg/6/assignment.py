# write a python script to sort the list given by user:::
# step:1 >> use input() function: to take values from user <<>> here, type is 'str'
user_input = input("Enter elements of a list separated by space: ")
print(user_input)  # 2 3 4 2 1 OR ram 4 mohan 5
print(type(user_input))  # <class 'str'>
# step:2 >> use split() function: to split a 'str' into a 'list' # by assigning to a variable
user_list = user_input.split()
print(user_list)  # ['4', '3', '5', '2', '7', '1', '8', 'ram', '4', 'mohan']
print(type(user_list))  # <class 'list'>
# step:3 >> use for loop and range() function: to iterate a user 'list'
# step:4 >> use int() function: to convert each 'str' element into an 'int' element::# useful for numbers only
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print(user_list)
print(type(user_list))