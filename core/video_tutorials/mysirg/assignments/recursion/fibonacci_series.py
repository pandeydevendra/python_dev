def fibonacci_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        fibonacci_series(n - 1)
        print(n - 1)


def fibonacci():
    a = int(input("Enter a number: "))
    f = fibonacci_series(a)
    print("First {} terms of the fibonacci series are {}.".format(a, f))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        fibonacci()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Wrong input!!\nEnter correct choice")

#TODO