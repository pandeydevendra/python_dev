n = int(input("Enetr a number: "))
for i in range(2, n):
    run = True
    if n % i == 0:
       # run = False
        i = i + 1
        print("{} is a prime number.".format(n))
    else:
        #run = False
        print("{} is not a prime number.".format(n))
