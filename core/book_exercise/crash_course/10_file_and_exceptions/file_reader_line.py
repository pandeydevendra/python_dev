filename = 'pi_digits.txt'

with open(filename) as file_object:
    print(file_object, type(file_object))
    for line in file_object:
        print(line)
        print(line.rstrip())

with open(filename) as file_obj:
    lines = file_obj.readlines()
    print(lines, type(lines))

for line in lines:
    print(line.rstrip())