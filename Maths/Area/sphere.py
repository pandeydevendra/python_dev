from math import pi


def sphere_area(r):
    s = 4 * pi * (r ** 2)
    return s


def proceed_area():
    r = int(input("enter radius in m: "))
    surface_area = sphere_area(r)
    print("surface area of the sphere of radius {0} m is {1} sq.m.".format(r, surface_area))


keep_on = 1
while keep_on == 1:
    ch = input("continue? y/n: ")
    if ch == 'y':
        proceed_area()
    elif ch == 'n':
        keep_on = 0
        print("the end")
    else:
        print('''error!!!enter valid choice: ''')
