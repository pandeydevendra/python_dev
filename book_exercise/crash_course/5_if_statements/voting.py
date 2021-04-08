# Simple if Statements : use for only one check.......
age = 19
if age >= 18:
    print("you are {} years old!".format(age))
    print("You are old enough to vote!")
age = 20
if age >= 18:
    print("\nyou are {} years old!".format(age))
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# if-else Statements : more than one conditions..................
age = 17
if age >= 18:
    print("\nyou are {} years old!".format(age))
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("\nyou are {} years old!".format(age))
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
