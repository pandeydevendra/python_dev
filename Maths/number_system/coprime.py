def factor_of_num(num):
    '''
    :param num: int
    :return: set(factors of num)
    '''
    set_factors = set()
    for i in range(1, num + 1):
        if num % i == 0:
            set_factors.add(i)
    return set_factors


def check_coprime():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    factors_1 = factor_of_num(num1)
    factors_2 = factor_of_num(num2)
    common_factors = factors_1.intersection(factors_2)
    print("common_factors:", common_factors)
    if len(common_factors) > 1:
        print("Numbers {} and {} are not coprime.".format(num1, num2))
    else:
        print("Numbers {} and {} are coprime.".format(num1, num2))


def start_program():
    keep_on = True
    while keep_on is True:
        ch = input("Do you want to continue? y/n: ")
        if ch == 'y':
            check_coprime()
        elif ch == 'n':
            keep_on = False
            print("End of the program.")
        else:
            print("wrong input. enter correct choice")


# program start from here

start_program()
