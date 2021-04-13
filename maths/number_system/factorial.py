def cal_fact(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    return fact


def process_fact():
    n = int(input("Enter a number:"))
    fact = cal_fact(n)
    print("Factorial of {0} is {1}".format(n, fact))


loop_fact = 0
while (loop_fact == 0):
    choice = input("do you want to continue, y/n: ")
    if choice == 'y':
        process_fact()
    elif choice == 'n':
        loop_fact = 1
        print("end of the program")
    else:
        print("wrong input choose correct option")
