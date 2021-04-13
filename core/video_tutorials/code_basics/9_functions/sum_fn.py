def sum(a, b, c):
    total = a + b + c
    return total

def proceed():
    x = int(input("enter first number:"))
    y = int(input("enter second number:"))
    z = int(input("enter third number:"))
    s = sum(x, y, z)
    print("Sum of {0}, {1}, and {2} is {3}".format(x,y,z,s))


keep_on = 1
while (keep_on==1):
    ch = input("continue??? y/n: ")
    if ch=='y':
        proceed()
    elif ch=='n':
        keep_on = 0
        print("the end")
    else:
        print("error!!!")
        print("choose y/n: ")