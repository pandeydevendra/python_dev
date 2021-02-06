def cal_area_rect(length=10, breadth=4):
    area = length * breadth
    return area


def area_rect():
    l = int(input("enter the length of the rectangle : "))
    b = int(input("enter the breadth of the rectangle: "))
    default_area = cal_area_rect()
    print("default area is {0}".format(default_area))
    area = cal_area_rect(l, b)
    print("area of rectangle with length {L} and breadth {B} is {A}".format(L=l, B=b, A=area))


continue_process = 1
while (continue_process == 1):
    ch = input("do you want to continue, y/n: ")
    if ch == 'y':
        area_rect()
    elif ch == 'n':
        continue_process = 0
        print("end of the program")
    else:
        print("wrong input, enter correct input")
