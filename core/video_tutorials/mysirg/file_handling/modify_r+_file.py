'''
modify city name Bhopal to a new format as BHOPAL
'''
# f is for file

f = open('file_city_name.txt', 'r+')  # open the folder in which one has to perform operation
x = "Bhopal\n"  # Bhopal is older data ;; x = city
s = f.readline()  # s = string
l = 0
while True:
    if s == '':
        break
    l = l + len(s)
    if s == x:
        f.seek(l - len(s), 0)
        f.write("BHOPAl\n")  # write the modified content
        break
    s = f.readline()
f.close()

f = open('file_city_name.txt', 'r+')
x = "Mumbai\n"
s = f.readline()
l = 0
while True:
    if s == '':
        break
    l = l + len(s)
    if s == x:
        f.seek(l - len(s), 0)
        f.write("MUMBAI\n")
        break
    s = f.readline()
f.close()
