def add_numbers():
    try:
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        addition = first_number + second_number
        print(addition)
    except (ValueError, TypeError):
        print("Error! Something is missing.")
    except Exception as e:
        print(e)


keep_on = True
while keep_on is True:
    ch = input("Do you want to continue?(y/n):")
    ch = ch.lower()
    if ch == 'y':
        add_numbers()
    elif ch == 'n':
        print("Exit")
        keep_on = False
    else:
        print("Choose correct input!!")
