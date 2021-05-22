def sum(n):
    if n == 1:
        return 1
    else:
        return (2*n -1)  + sum(n-1)

#num(5)


def sum_n():
    a = int(input("Enter a number: "))
    s = sum(a)
    print("Sum of first {} odd natural numbers is {}.".format(a, s))

#sum_n()

keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        sum_n()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Wrong input!!\nEnter correct choice")
