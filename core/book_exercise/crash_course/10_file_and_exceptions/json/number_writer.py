# JSON :: JavaScript Object Notation
import json

numbers = [2, 3, 5, 7, 11, 13]
"""
function> json.dump() > takes two arguments: a piece of data to
store and a file object it can use to store the data.
"""
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)