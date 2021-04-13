def volume_cuboid(l, b, h):
    v = l * b * h
    return v


def process_volume():
    length = float(input("Enter the length of the cuboid in cm."))
    width = float(input("Enter the width of the cuboid in cm."))
    height = float(input("Enter the height of the cuboid in cm."))
    vol = volume_cuboid(length, width, height)
    print("Volume of the cuboid is {0}.".format(vol))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue the calculation? y/n: ")
    if ch == "y":
        process_volume()
    elif ch == "n":
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input! Enter the correct choice.")
