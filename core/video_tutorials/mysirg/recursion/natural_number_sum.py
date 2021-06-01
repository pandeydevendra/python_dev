def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


def sum_n():
    num = int(input("Enter a number: "))
    s = sum(num)
    print("Sum of first {} natural numbers is {}.".format(num, s))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        sum_n()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Wrong input!!\n Enter correct choice")
