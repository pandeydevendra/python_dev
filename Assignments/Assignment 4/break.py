x = int(input("Enetr an even number: "))
i = 1
while i <= 3:
    if x % 2 == 0:
        print("Correct")
        i += 1
        break

    else:
        print("Wrong")
