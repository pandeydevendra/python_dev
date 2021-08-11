"""
input_data = {"Dravid": "Cricket", "Messi": "Football", "Sachin": "Cricket", "Ronaldo": "Football"}

write a python program to the below result

output_data = {"Cricket": ["Dravid", "Sachin"], "Football": ["Messi", "Ronaldo"]}
"""

input_data = {"Dravid": "Cricket", "Messi": "Football", "Sachin": "Cricket", "Ronaldo": "Football"}
output_data= {}
for k,v in input_data.items():
    if v in output_data:
        output_data[v].append(k)
    else:
        output_data.update({v:[k]})

print(output_data)

elements = {'a': 'fire', 'b': 'ice', 'c': 'fire', 'd': 'water', 'f': 'fire', 'i': 'ice'}

# inverted_dict = {'fire': ['a', 'c'], 'ice': ['b'], 'water': ['d']}

# Use this code to invert dictionaries that have non-unique values

element_set = {}
for key, value in elements.items():
    element_set.setdefault(value, list()).append(key)

print(element_set)