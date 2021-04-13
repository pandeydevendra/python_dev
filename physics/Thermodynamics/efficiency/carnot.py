def cal_efficiency(TH, TL):
    efficiency = 1 - (TL / TH)
    eff_percentage = efficiency * 100
    return efficiency, eff_percentage


def eff():
    TH = int(input("Enter the higher temperature in K: "))
    TL = int(input("Enter the lower temperature in K: "))
    ef_carnot = cal_efficiency(TH, TL)
    print("Carnot efficiency for the given temperature limit is {}.".format(ef_carnot))


keep_on = True
while keep_on == True:
    choice = input("Do you want to continue? y/n: ")
    if choice == 'y':
        eff()
    elif choice == 'n':
        keep_on = False
        print("End of the program.")
    else:
        print("Error!!!\n Enter correct choice.")
