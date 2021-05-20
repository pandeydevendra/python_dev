def cube_sum(n):
    if n == 1:
        return 1
    else:
        return n**3 + cube_sum(n-1)



def sum_n():
    a = int(input("Enter a number: "))
    s = cube_sum(a)
    print("Sum of the cube of first {} natural numbers is {}.".format(a, s))

#sum_n()

keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?y/n: ")
    if ch == 'y':
        sum_n()
    elif ch == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Wrong input!!\nEnter correct choice")
