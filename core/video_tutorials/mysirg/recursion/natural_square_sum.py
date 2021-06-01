def square_sum(n):
    if n == 1:
        return 1
    else:
        return n**2 + square_sum(n-1)

#square_sum(5)


def sum_n():
    a = int(input("Enter a number: "))
    s = square_sum(a)
    print("Sum of the square of first {} natural numbers is {}.".format(a, s))

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
