def simple_interest(p, r, t):
    s_i = p * r * t / 100
    return s_i


def proceed_simple_interest():
    principal = int(input("Enter the principal amount: "))
    rate = float(input("Enter the rate applied on the principal amount: "))
    time = int(input("Enter the time period in year: "))
    si_in = simple_interest(principal, rate, time)
    print("The simple interest is {0}.".format(si_in))


keep_on = True
while keep_on is True:
    ch = input("Do you want to run further? y/n: ")
    if ch == "y":
        proceed_simple_interest()
    elif ch == "n":
        keep_on = False
        print("End of the  program")
    else:
        print("something is wrong with input! Enter correct choice.")
