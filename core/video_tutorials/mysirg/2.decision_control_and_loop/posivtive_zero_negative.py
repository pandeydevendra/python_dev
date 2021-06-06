def num_nature():
    n = int(input("Enter a number: "))
    if n == 0:
        print("Entered number is zero.".format(n))
    elif n > 0:
        print("Entered number is positive.".format(n))
    else:
        print("Entered number is negative.".format(n))

k = True
while k == True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        num_nature()
    elif ch == 'n':
        k = False
        print("End of the program.")
    else:
        print("Wrong input!!\nEnter correct choice.")
