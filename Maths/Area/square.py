def square_process():
    a = int(input("Enter the side of number: "))
    area = a ** 2
    print("Area of the given square is {0}.".format(area))


run = True
while run is True:
    ch = input("Do yo want to continue the program? y/n: ")
    if ch == "y":
        square_process()
    elif ch == "n":
        run = False
        print("End of the program")
    else:
        print("Incorrect input! Enter correct choice.")
