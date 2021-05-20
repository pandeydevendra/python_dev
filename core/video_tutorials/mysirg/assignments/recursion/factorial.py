def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
def fact():
    num = int(input("Enter a number: "))
    f = factorial(num)
    print("Factorial of {} is {}.".format(num, f))

keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        fact()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Wrong input!!\n Enter correct choice")
