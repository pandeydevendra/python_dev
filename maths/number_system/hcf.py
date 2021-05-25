def hcf():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    if (a > b):  # for hcf select lower number
        x = b
    else:
        x = a
    for i in range(1, x + 1):
        if (a % i == 0) and (b % i == 0):
            hcf = i
    print("The HCF of {0} and {1} is={2}".format(a, b, hcf))

keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        hcf()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input. enter correct choice")

