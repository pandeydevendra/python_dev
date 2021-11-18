# making a dataframe:
"""
a dataframe is basically a table comprising rows and columns:
a dataframe is created with the help of 'pandas' library's module named 'DataFrame' and
using the concept of list in dictionary;
"""
# eg..,

d1 = {'name': ['ram', 'rahul', 'dev'], 'age': [26, 28, 27]}
print(d1) # it prints as it is

# now import DataFrame module from pandas library

from pandas import DataFrame
# operate DataFrame module over dict
df1 = DataFrame(d1)
print(df1)

# Similarly:
# Extending dataframe with another module called 'Series' ;
import pandas as pd
from pandas import Series

series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
print(series)


d2 = {
    'name' : Series(['Braund', 'Cummings', 'Heikkinen', 'Allen'], index=['a', 'b', 'c', 'd']),
    'age' : Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
    'fare' : Series([7.25, 71.83, 8.05], index=['a', 'b', 'd']),
    'survived?' : Series([False, True, True, False], index=['a', 'b', 'c', 'd'])
}

df2 = DataFrame(d2)
print(df2)