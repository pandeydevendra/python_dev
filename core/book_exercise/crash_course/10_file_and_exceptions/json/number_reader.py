import json

filename = 'numbers.json'
"""
function > json.load() >> load the
information stored in abc.json(eg.; filenumbers.json)
"""
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
