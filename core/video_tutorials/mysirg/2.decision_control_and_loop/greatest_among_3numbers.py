def greatest_number(a, b, c):
    if c < a > b:
        g = a
    elif a < b > c:
        g = b
    else:
        g = c
    return g


a, b, c = (int(x) for x in input("Enter three numbers separated by comma: ").split(','))
print("Three numbers are: {}, {} and {}".format(a, b, c))
grtst_num = greatest_number(a, b, c)
print("The greatest number is {}.".format(grtst_num))
