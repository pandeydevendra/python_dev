"""
1. Write a python function ‘convert’ to convert a python string to a python list of words: (4
marks)
example:
str = “ajit.singh@transorg.com”
list = [‘ajit’,’singh’,’transorg’,’com’]
"""


def convert_str_to_list(s):
    l = s.split("@")
    l1 = l[0].split(".")
    l2 = l[1].split(".")
    l1.extend(l2)
    print(l1)


id = "ajit.singh@transorg.com"
convert_str_to_list(id)

"""
2. Write a python program to create an intersection between two lists. (2 marks)
example:
l1 = [1,2,3,4,5,6]
l2 = [2,3,4,7,8]
new_list = [2,3,4]
"""

# two given lists:
l1 = [1, 2, 3, 4, 5, 6]
l2 = [2, 3, 4, 7, 8]

# create an empty list:
new_list = []

# find intersections between the two given lists and append it into the new_list:
for value in l1:
    if value in l2:
        new_list.append(value)
    else:
        pass

print(new_list)

"""
3. Write a python function “remove_duplicates” to remove duplicates from a list. (3 marks)
example:
l1 = [1,2,2,1,3,4]
new_list = [1,2,3,4]
"""
# given list
l1 = [1, 2, 2, 1, 3, 4]

# create an empty list:
new_list = []


def remove_duplicates(l):
    for value in l:
        if value in new_list:
            pass
        else:
            new_list.append(value)
    print(new_list)


remove_duplicates(l1)

"""
4. Write a Python program to find the second largest number in a list. (3 marks)
l1= [100,101,102,103,104,105]
"""
# given list
l1 = [100, 103, 102, 105, 101, 104]

# method_1: using sort() function directly:
l1.sort()
# second largest will be second from the last (of index value = -2)
second_largest_number = l1[-2]
print(f"The second largest number in the list is {second_largest_number}")

# method_2: through iteration process over the list:
l1 = [100, 103, 102, 105, 101, 104]


def second_largest_in_list(l):
    largest_number = 0
    second_largest_number = 0
    for num in l:
        if num >= largest_number:
            second_largest_number = largest_number
            largest_number = num
        elif num > second_largest_number:
            second_largest_number = num
    print(f"second_largest_number = {second_largest_number}")


second_largest_in_list(l1)
# print(f"largest_number = {largest_number}")


"""
5. Write a python code to generate a list of tuples from a dictionary. (2 marks)
For example:
d = {1:2,2:3,3:4}
new_list = [(1,2), (2,3), (3,4)]
"""
# let the given dictionary is
d = {1: 2, 2: 3, 3: 4}

# create an empty list:
new_list = []
for val in d.items():
    new_list.append(val)

# print(new_list)

# Part 2 (Lambda Functions):
"""
1. Write a lambda function to square the elements in a list (1.5 marks)
l1= [1,2,3,4,5,6,7,8,9]
"""
# TODO
"""
2. Write a lambda function to find the smaller value between two elements. (1.5 marks)
Example:
Input: 2,3
Output: 2
"""
# TODO

# Part 3 (Pandas DataFrames):

import pandas as pd
import numpy as np

dict1 = {'ID': [1, 2, 3, 4, 5], 'Name': ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']}
dict2 = {'ID': [2, 2, 5, 3, 1, 1, 4, 4],
         'Sport': ['Cricket', 'Football', 'Basketball', 'Basketball', 'Table tennis', 'Cricket', 'Football',
                   'Basketball']}
dict3 = {'ID': [2, 1, 3, 5, 4], 'Marks': [30, ' ', 85, 65, 97]}
df1 = pd.DataFrame(data=dict1)
df2 = pd.DataFrame(data=dict2)
df3 = pd.DataFrame(data=dict3)
df3['Marks'] = np.where(df3['ID'] == 1, np.nan, df3['Marks'])

# print(df1)
# print(df2)
# print(df3)

"""
1.Merge Table 1 and Table 2 on ID such that the resultant data frame has 3 columns in the
following order: ID, Name and Sport. The objective is to have all the sports played by a
person listed against their corresponding ID and Name. (4 marks)
"""
merged_df = pd.merge_ordered(df1, df2, on='ID')
print(merged_df)

"""
2.Find the number of ID’s having marks greater than 80. Also, find the maximum and
minimum values of the column “Marks” in table 3. (4 marks)
"""
# the number of ID’s having marks greater than 80:
df_id = df3.loc[df3['Marks'] > 80]
# print(df_id)
print(df_id['ID'])

# the maximum and minimum values of the column “Marks”:
max = df3['Marks'].max()
print(f"the maximum marks is {max}")
min = df3['Marks'].min()
print(f"the minimum marks is {min}")
