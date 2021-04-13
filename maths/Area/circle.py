from math import pi


def area_cicle(r):
    a = pi * r ** 2
    return a


def process_area():
    r = float(input("Enter radius of the circle in m: "))
    area = area_cicle(r)
    print("Area of the circle is {0}".format(area))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        process_area()
    elif ch == 'n':
        keep_on = False
        print("program end")
    else:
        print('''Wrong input!! enter valid choice: ''')
