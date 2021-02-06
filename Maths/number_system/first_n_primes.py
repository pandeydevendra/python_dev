def check_prime(num):
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


def prime_list():
    reqd_prime_count = int(input("Enter the number: "))
    print(reqd_prime_count)
    found_prime_count = 0
    check_num = 2
    prime_numbers = []
    while found_prime_count < reqd_prime_count:
        # check_num is prime or not
        prime_flag = check_prime(check_num)
        if prime_flag is True:
            prime_numbers.append(check_num)
            found_prime_count += 1
            print("Prime numbers {}.".format(check_num))
        check_num += 1
    print("Prime numbers {}.".format(prime_numbers))


def start_program():
    keep_on = True
    while keep_on is True:
        ch = input("Do you want to continue? y/n: ")
        if ch == 'y':
            prime_list()
        elif ch == 'n':
            keep_on = False
            print("End of the program.")
        else:
            print("wrong input. enter correct choice")


start_program()
