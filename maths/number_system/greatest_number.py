def find_max(numbers):
    max_num = 0
    print("current max is {0}.".format(max_num))
    for n in numbers:
        n = int(n)
        print("current number is", n)
        if n > max_num:
            max_num = n
            print("current max is {0}.".format(max_num))
    return max_num


print("welcome at max")
num = (input("enter all numbers separated by comma:"))
# print("entered numbers are:", num,type(num))
num_list = num.split(',')
# print(num_list, type(num_list), max(num_list))

max_value = find_max(num_list)
print("max value is {0}.".format(max_value))
