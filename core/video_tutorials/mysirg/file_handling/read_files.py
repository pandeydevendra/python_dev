f = open('string.txt', 'r')
# s = f.read() # read() reads all string
# print(s) # File handling analysis
# or
# print(f.read())

s1 = f.read(5)
s2 = f.read(9)
s3 = f.read(8)
print(s1)  # File >> 4 letters + 1 space = 5
print(s2)  # handling
print(s3)  # analysis
# print()


f.close()

"""
Read Function: to read all file; use -->> read()
To read word by word; use -->> read(n), read(n1)... n represent number of letters one need to read
"""