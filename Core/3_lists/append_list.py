num_list = []

keep_on = True
while (keep_on is True):
    ch = input("are you sure you want to continue? y/n: ")
    if ch == 'y':
        n = input("Enter number : ")
        num_list.append(n)
    elif ch == 'n':
        keep_on = False
    else:
        print("wrong input.")

print(num_list)
