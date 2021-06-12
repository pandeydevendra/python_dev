# way 1:
sum = lambda a, b: a + b
result = sum(20, 30)
print(result, type(result))

# way 2:
sum = (lambda a, b: a + b)(20, 30)
print(sum, type(sum))


# @ Note the difference in 1 & 2 >>>> parenthesis >> ()

# way 3:
sum = (lambda a, b: a + b)(int(input("Enter a: ")), int(input("Enter b: ")))
print(sum, type(sum))

# write a lambda expression to find bigger number:
bigger_number = (lambda a, b: a if a > b else b)(int(input("Enter a: ")), int(input("Enter b: ")))
print("Bigger number is {}.".format(bigger_number))