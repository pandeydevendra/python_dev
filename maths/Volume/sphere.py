from math import pi


def cal_vol_sphere(r):
    v = (4 / 3) * pi * (r ** 3)
    return v


def process_volume():
    radius = int(input("Enter radius of the sphere: "))
    volume = cal_vol_sphere(radius)
    print("The volume of the sphere is {0}.".format(volume))


go_on = True
while go_on is True:
    user_choice = input("""Press 'p' to process the program: \n or press 'e' to end the program: """)
    if user_choice == "p":
        process_volume()
    elif user_choice == "e":
        go_on = False
        print("End of the program.")
    else:
        print("wrong input!!! Enter correct option.")
