# write a python script to sort the list given by user:::
# step:1 >> use input() function: to take values from user <<>> here, type is 'str'
user_input = input("Enter elements of a list separated by space: ")
print(user_input)
# step:2 >> use split() function: to split a 'str' into a 'list' # by assigning to a variable
user_list = user_input.split()
print(user_list)
# step:3 >> use for loop and range() function: to iterate a user 'list'
# step:4 >> use int() function: to convert each 'str' element into an 'int' element::# useful for numbers only
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print(user_list)

# step:5 >> use sort() function: to arrange number in increasing order
user_list.sort()
print("sorted list: {}".format(user_list))
