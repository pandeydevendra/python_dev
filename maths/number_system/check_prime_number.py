def cal_prime():
    num = int(input("Enter a number: "))
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            print("{0} is divided by {1}".format(num, i))
            prime_flag = False
            break
    if prime_flag is True:
        print("{0} is a prime number.".format(num))
    else:
        print("{0} is not a prime number.".format(num))

def start_program():
    keep_on = True
    while keep_on is True:
        ch = input("Do you want to continue? y/n: ")
        if ch == 'y':
            cal_prime()
        elif ch == 'n':
            keep_on = False
            print("End of the program.")
        else:
            print("wrong input. enter correct choice")

#program start from here

start_program()