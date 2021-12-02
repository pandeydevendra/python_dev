# file baseball.csv not available

"""
from pandas import *
import numpy

if __name__ == '__main__':
    # Pandas dataframes have a method called 'fillna(value)', such that you can
    # pass in a single value to replace any NAs in a dataframe or series. You
    # can call it like this:
    #     dataframe['column'] = dataframe['column'].fillna(value)
    #
    # Using the numpy.mean function, which calculates the mean of a numpy
    # array, impute any missing values in our Lahman baseball
    # data sets 'weight' column by setting them equal to the average weight.
    #
    # You can access the 'weight' colum in the baseball data frame by
    # calling baseball['weight']

    baseball = pandas.read_csv('../data/Master.csv')

    baseball['weight'] = baseball['weight'].fillna(numpy.mean(baseball['weight']))

    # YOUR CODE GOES HERE

    print(numpy.sum(baseball['weight']), numpy.mean(baseball['weight']))
"""

# FileNotFoundError: [Errno 2] File ../data/Master.csv does not exist: '../data/Master.csv'
'''
Traceback (most recent call last):
  File "vm_main.py", line 33, in <module>
    import main
  File "/tmp/vmuser_eiwsdzfwfl/main.py", line 2, in <module>
    import studentMain
  File "/tmp/vmuser_eiwsdzfwfl/studentMain.py", line 4, in <module>
    from imputation import imputation
ImportError: cannot import name imputation
'''