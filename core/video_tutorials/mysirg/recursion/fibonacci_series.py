def fibonacci_series(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        nth_value = fibonacci_series(n - 1) + fibonacci_series(n - 2)
        return nth_value


def fibonacci():
    a = int(input("Enter a number: "))
    fib_series = []
    for i in range(1, a + 1):
        f = fibonacci_series(i)
        fib_series.append(f)
    print("First {} terms of fibonacci series are {}.".format(a, fib_series))


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
