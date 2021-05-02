def find_max():
    max_num = 0
    for i in range(1, 11):
        num = int(input("Enter a number: "))
        if max_num < num:
            max_num = num

    print("max_num", max_num)


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        find_max()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input. enter correct choice")
