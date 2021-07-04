with open('learning_python.txt') as pylearn:
    lines = pylearn.readlines()
    print(lines)

py_string = ''
for line in lines:
    py_string += line

print(py_string)
print(len(py_string))