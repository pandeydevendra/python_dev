# write a python script to sort the list given by user
"""
l1 = [2,4,6,1,3,5]
l1.sort()
print(l1) # >>> [1, 2, 3, 4, 5, 6]
print(type(l1)) # <class 'list'>
ls = ['summer', 'winter', 'rainy', 'season']
ls.sort()
print(ls) # >>> ['rainy', 'season', 'summer', 'winter']
print(type(ls)) # <class 'list'>
lsn = [2, 1, 3, 'sum', 'add', 'divide']
print(lsn) # [2, 1, 3, 'sum', 'add', 'divide']
print(type(ls)) # <class 'list'>
lsn.sort()
print(lsn) # >>> TypeError: '<' not supported between instances of 'str' and 'int'
"""
user_list = (input("Enter the list: "))
# numbers =
# for num in numbers:
#    user_list.append(num)
print(user_list)
user_list.sort()
print(user_list)
