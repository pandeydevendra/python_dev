def enter_choice():
    CHOICES=['ke','pe']
    choice=input("enter type of energy, ke/pe:")
    if choice in CHOICES:
        if choice=='ke':
            import kinetic
            print("ke")
        elif choice=='pe':
            import potential
            print("pe")

    else:
        print("you have entered wrong choice")

run_flag = True
while(run_flag is True):
    ch = input("do you want to continue? y/n: ")
    if ch.lower()=='y':
        enter_choice()
    elif ch.lower()=='n':
        run_flag=False
        print("you have exited")
    else:
        print("you have entered wrong choice, try again")