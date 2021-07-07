import json

filename = 'favorite_number.json'
with open(filename, 'r') as f_num_file:
    f_num = json.load(f_num_file)
    print(f"""I know your favorite number! It’s {str(f_num)}.""")
