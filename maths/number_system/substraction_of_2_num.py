def cal_substraction(a, b):
    if a > b:
        substraction = int(a) - int(b)
    else:
        substraction = int(b) - int(a)
    return substraction


def process_substraction():
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    print(a, b)
    print(type(a), type(b))
    substraction_result = cal_substraction(a, b)
    print(substraction_result)
    print("Substraction of {0} and {1} is {2}.".format(a, b, substraction_result))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue??y/n: ")
    if ch == "y":
        process_substraction()
    elif ch == "n":
        keep_on = False
        print("end of the program.")
    else:
        print("wrong input, enter correct input")
