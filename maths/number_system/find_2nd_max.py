def find_2nd_max():
    max_num = 0
    max_2nd_num = 0
    for i in range(1, 6):
        num = int(input("Enter a number: "))
        if num > max_num:
            max_2nd_num = max_num
            max_num = num

        elif num > max_2nd_num:
            max_2nd_num = num

    print("maxnum", max_num)
    print("max_2nd_num", max_2nd_num)


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        find_2nd_max()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input. enter correct choice")
