def enter_process():
    PROCESSES = ['add', 'substract']
    choice = input("Enter the process you want to perform;addition/substraction): ")
    if choice in PROCESSES:
        if choice == 'add':
            import add_2_num
            # print("addition")
        elif choice == 'substract':
            import substraction_of_2_num
            # print("substraction")
    else:
        print("Wrong choice!! Enter correct option.")


run_flag = True
while (run_flag is True):
    ch = input("do you want to continue? y/n: ")
    if ch.lower() == 'y':
        enter_process()
    elif ch.lower() == 'n':
        run_flag = False
        print("you have exited")
    else:
        print("you have entered wrong choice, try again")
