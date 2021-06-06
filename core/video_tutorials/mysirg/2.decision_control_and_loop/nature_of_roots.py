import math

from math import sqrt


def roots():
    coeff = input("Enter the value of a, b and c: ")
    print(coeff)
    coeff_list = coeff.split(',')
    print(coeff_list)
    coeff_list_int = [int(i) for i in coeff_list]
    print(coeff_list_int)
    a, b, c = coeff_list_int
    print(a, type(a))
    print(b)
    print(c)
    d = math.sqrt((b ** 2) - (4 * a * c))
    print(d)

    if d == 0:
        root_1 = (-b + d) / 2
        root_2 = (-b - d) / 2
        print("Roots are: ", root_1, root_2)
        print("Roots are equal and opposite in nature.")
    elif d > 0:
        root_1 = (-b + d) / 2
        root_2 = (-b - d) / 2
        print("Roots are: ", root_1, root_2)
        print("Roots are unequal and real in nature.")
    else:
        print("Roots are imaginary in nature.")
    #
    # root_1 = (-b + d)/2
    # root_2 = (-b - d)/2
    # print("Roots are: ", root_1, root_2)


def roots_nature():
    coeff = input("Enter the value of a, b and c: ")
    print(coeff)
    coeff_list = coeff.split(',')
    print(coeff_list)
    coeff_list_int = [int(i) for i in coeff_list]
    print(coeff_list_int)
    a, b, c = coeff_list_int
    print(a, type(a))
    print(b)
    print(c)
    if b ** 2 == 4 * a * c:
        print("Roots are equal and opposite in nature.")
    elif b ** 2 > 4 * a * c:
        print("Roots are unequal and real in nature.")
    else:
        print("Roots are imaginary in nature.")


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        find = input("What to want to know? RootsNature 1/All 2: ")
        if find == '1':
            roots_nature()
        elif find == '2':
            roots()
    elif ch == 'n':
        keep_on = False
        print("End of Program.")
    else:
        print("Wrong input")