name = input("Enter your name: ")
count = 0
letter = input("Which letter you want to count in your name? ")
for e in name:
    if e == letter:
        count += 1
print("count of {} is {}.".format(letter, count))
print(len(name))

while count < +3:
    print(name)
    count += 1


def a(num):
    f = True
    for i in range(2, num):
        if num % i == 0:
            f = False
            break
    return f


def b():
    reqd_prime_count = int(input("Enter the number: "))
    print(reqd_prime_count)
    found_prime_count = 0
    check_num = 2
    prime_numbers = []
    while found_prime_count < reqd_prime_count:
        # check_num is prime or not
        prime_flag = a(check_num)
        if prime_flag is True:
            prime_numbers.append(check_num)
            found_prime_count += 1
            print("Prime numbers {}.".format(check_num))
        check_num += 1
    print("Prime numbers {}.".format(prime_numbers))


# def c():
keep_on = True
while keep_on is True:
    ch = input("Do you want to continue? y/n: ")
    if ch == 'y':
        b()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("wrong input. enter correct choice")

# c()
