"""
ask user to enter a number in int
x*x = y
loop count <= y/2 + 1;
"""


def check_perfect_sqr():
    n = int(input("Enter a number: "))
    start = 1
    end = n // 2 + 1
    perfect_num_flag = False
    while start <= end:
        if start ** 2 == n:
            perfect_num_flag = True
            break
        start = start + 1

    if perfect_num_flag is True:
        print("{} is a perfect square of {}.".format(n, start))
    else:
        print("{} is a not perfect square.".format(n))


def start_program():
    keep_on = True
    while keep_on is True:
        ch = input("Do you want to continue? y/n: ")
        if ch == 'y':
            check_perfect_sqr()
        elif ch == 'n':
            keep_on = False
            print("End of the program.")
        else:
            print("wrong input. enter correct choice")


start_program()
