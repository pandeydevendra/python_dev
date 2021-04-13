def cal_add(a, b):
    add = int(a) + int(b)
    return add


def process_add():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(a, b)
    print(type(a), type(b))
    sum_result = cal_add(a, b)
    print(sum_result)
    print("Addition of {0} and {1} is {2}.".format(a, b, sum_result))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue??y/n: ")
    if ch == "y":
        process_add()
    elif ch == "n":
        keep_on = False
        print("end of the program")
    else:
        print("wrong input, enter correct input")
