def get_celsius(f):
    c = (5 / 9) * (f - 32)
    return c


def get_fohrenheit(c):
    f = 1.8 * c + 32
    return f


def process_temp():
    CHOICE = input("enter your temperature type, f or c:")
    if CHOICE == 'f':
        print("you have selected fohrenheit")
        f_value = float(input("enter value of temperature = "))
        # print("f_value")
        c_value = get_celsius(f_value)
        print("Fohrenheit is {0} and Celsius is {1}".format(f_value, c_value))
    elif CHOICE == 'c':
        print("you have selected celsius")
        c_value = float(input("enter value of temperature = "))
        # print("c_value")
        f_value = get_fohrenheit(c_value)
        print(" Celsius is {0} and Fohrenheit is {1}".format(c_value, f_value))
    else:
        print("you have entered wrong choice")


print("welcome to celsius and fohrenheit conversion")
choice_flag = True
while (choice_flag is True):
    ch = input("do you want to continue, y/n: ")
    if ch == 'y':
        process_temp()
    elif ch == 'n':
        print("program exit.")
        choice_flag = False
