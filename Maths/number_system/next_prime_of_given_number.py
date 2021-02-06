def check_prime(num):
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


def cal_next_prime():
    n = int(input("Enter a number: "))
    next_num = n
    p_flag = False
    while p_flag is False:
        p_flag = check_prime(next_num)
        if p_flag is False:
            next_num += 1

    print("Prime number next to {} is {}.".format(n, next_num))


def start_program():
    keep_on = True
    while keep_on is True:
        ch = input("Do you want to continue? y/n: ")
        if ch == 'y':
            cal_next_prime()
        elif ch == 'n':
            keep_on = False
            print("End of the program.")
        else:
            print("wrong input. enter correct choice")


# program start from here

start_program()
