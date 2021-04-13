def cal_tri_area(b, h):
    a = (1 / 2) * (b * h)
    return a


def process_area():
    b = int(input("base of the triangle:"))
    h = int(input("height of the triangle:"))
    area = cal_tri_area(b, h)
    print("area of the triangle with base {0} and height {1} is {2}".format(b, h, area))


continue_process = 1
while (continue_process == 1):
    ch = input("do you want to continue, y/n: ")
    if ch == 'y':
        process_area()
    elif ch == 'n':
        continue_process = 0
        print("end of the program")
    else:
        print("wrong input, enter correct input")
