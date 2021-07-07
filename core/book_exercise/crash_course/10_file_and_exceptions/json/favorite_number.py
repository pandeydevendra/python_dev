import json

f_number = int(input("What is your favorite_number? "))
filename = 'favorite_number.json'
with open(filename, 'w') as f_obj:
    json.dump(f_number, f_obj)
