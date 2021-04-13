def enter_choice():
    CHOICE = int(input("which laws you want to compute? 1/2/3: "))
    if CHOICE==1:
        import motion_rule1
    elif CHOICE==2:
        import motion_rule2
    elif CHOICE==3:
        import motion_rule3

run_motion = True
while (run_motion is True):
    ch = input("do you want to continue? y/n: ")
    if ch=='y':
       print("you have entered y, please enter choice also")
       enter_choice()
    elif ch=='n':
        print("you have exited")
        run_motion = False
    else:
        print("you have entered wrong input")