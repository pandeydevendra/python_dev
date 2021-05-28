def lcm():
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    if (a > b):  # for lcm select greater number
        x = a
    else:
        x = b

    for j in range(x, a * b + 1):
        if (j % a == 0) and (j % b == 0):
            lcm = j
            break
    print("The LCM of {0} and {1} is={2}".format(a, b, lcm))


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        lcm()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input. enter correct choice")