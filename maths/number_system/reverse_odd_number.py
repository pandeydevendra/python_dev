"""
input num,
print num
generate 'N' odd numbers

"""
def generate_odd_nums():
    n = int(input("Enter the number count: "))
    print(n)
    odd_numbers = []
    odd_found = 0
    number = 0
    while odd_found < n:
        number = number + 1
        if number%2 == 0:
            continue
        else:
            odd_numbers.append(number)
            odd_found = odd_found + 1
    print(odd_numbers)
    print(odd_numbers.reverse())

generate_odd_nums()
'''def start_program():
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


start_program()'''
