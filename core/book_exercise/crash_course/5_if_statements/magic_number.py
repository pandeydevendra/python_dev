# checking inequality (!=)
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
age = 19
#print(age == 19)
if age < 22:
    print("true")
elif age <= 21:
    print("ok")
# Using 'and' to Check Multiple Conditions
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("{} and {} >= 21: \t True!".format(age_0, age_1))
else:
    print("{} and {} >= 21: \t False!".format(age_0, age_1))
print("\n")
age_1 = 22
if (age_0 >= 21) and (age_1 >= 21):  # parentheses are optional here
    print("{} and {} >= 21: \t True!".format(age_0, age_1))
else:
    print("{} and {} >= 21: \t False!".format(age_0, age_1))

print("\n")
# Using 'or' to Check Multiple Conditions
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("{} or {} >= 21: \t True!".format(age_0, age_1))
else:
    print("{} or {} >= 21: \t False!".format(age_0, age_1))
print("\n")
age_1 = 22
if (age_0 >= 21) or (age_1 >= 21):  # parentheses are optional here
    print("{} or {} >= 21: \t True!".format(age_0, age_1))
else:
    print("{} or {} >= 21: \t False!".format(age_0, age_1))
