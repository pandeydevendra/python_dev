#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
# Create an Empty Series
s = pd.Series() # A basic series, which can be created is an Empty Series.
print(s)

"""
# Create a Series from ndarray
If data is an ndarray, then index passed must be of the same length.
If no index is passed, then by default index will be range(n)
where n is array length, i.e., [0,1,2,3…. range(len(array))-1].
"""
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

# We did not pass any index, so by default, it assigned the indexes ranging from 0 to len(data)-1,i.e., 0 to 3.
data = np.array(['aam','ball','catch','done'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

fruits = np.array(['mango', 'grapes', 'orange', 'banana'])
s_index = pd.Series(fruits, index=[10, 12, 15, 18])
print(s_index)

# Create a Series from dict
'''# A dict can be passed as input and if no index is specified, 
then the dictionary keys are taken in a sorted order to construct index.
If index is passed, the values in data corresponding to the labels in the index will be pulled out.
'''
dict_data = {'a' : 0, 'b' : 1, 'c' : 2, 'd': 3}
series = pd.Series(dict_data)
print(series)

# Observe − Dictionary keys are used to construct index.
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
# Observe − Index order is persisted and the missing element is filled with NaN (Not a Number).

'''
#Create a Series from Scalar
If data is a scalar value, an index must be provided. The value will be repeated to match the length of index
'''
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
