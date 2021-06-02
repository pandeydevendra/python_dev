file = open('file_city_name.txt', 'w')
line = ["Bhopal\n", "Delhi\n", "Mumbai\n", "Chennai"]
file.writelines(line)
file.close()