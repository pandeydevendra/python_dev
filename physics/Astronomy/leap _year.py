def check_leap_year():
    y = int(input("enter year: "))
    if y%400==0 or (y%4==0 and y%100!=0):
        print("{0} is a leap year".format(y))
    else:
        print("{0} is not a leap year.".format(y))

loop_flag = True
while (loop_flag is True):
    choice = input("do you want to continue, y/n:")
    if choice=='y':
        check_leap_year()
    elif choice =='n':
        loop_flag=False
        print("you have exited from the program")
    else:
        print("wrong input, please enter correct choice")