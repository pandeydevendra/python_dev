def greater_num():
    a = int(input("enter a number1:"))
    b = int(input("enter a number2:"))
    c = int(input("enter a number3:"))
    max_num = 0
    if a > b and a > c:
        max_num = a
    elif a > b and a < c:
        max_num = c
    elif b > a and b > c:
        max_num = b
    else:
        max_num = c
    print("greatest number is {0}".format(max_num))


keep_on = 1
while (keep_on == 1):
    ch = input("do you want to continue? y/n: ")
    if ch == 'y':
        greater_num()
    elif ch == 'n':
        keep_on = 0
        print("the end.")
    else:
        print("wrong input. enter correct choice")
