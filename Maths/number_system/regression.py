def cal_reg(n):
    x = 1
    i = n
    while i >=3:
        x = x * i
        i = i + 1
    return reg


def process_reg():
    n = int(input("Enter a number:"))
    x = cal_reg(n)
    print("Factorial of {0} is {1}".format(n, reg))

loop_fact = 0
while (loop_fact==0):
    choice = input("do you want to continue, y/n: ")
    if choice=='y':
        process_reg()
    elif choice=='n':
        loop_fact = 1
        print("end of the program")
    else:
        print("worng input choose correct option")