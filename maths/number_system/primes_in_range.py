def check_prime(num):
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break
    return prime_flag


def prime_list():
    num1 = int(input("Enter the start number: "))
    num2 = int(input("Enter the end number: "))
    prime_numbers = []
    for num in range(num1, num2 + 1):
        prime_flag = check_prime(num)
        if prime_flag is True:
            prime_numbers.append(num)

    print("Prime numbers {}.".format(prime_numbers))  # it gives a complete list
    print(len(prime_numbers))


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
