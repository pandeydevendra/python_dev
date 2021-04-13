"""The else block is a catchall statement.
It matches any condition that wasn’t matched by a specific if or elif test,
,and that can sometimes include invalid or even malicious data.
If you have a specific final condition you are testing for,
consider using a final elif block and omit the else block. As a
result, you’ll gain extra confidence that your code will run only under the
correct conditions."""

# The if-elif-else Chain::::::::::
age = 12
if age < 4:
    print("you are {} years old!".format(age))
    print("Your admission cost is $0.")
elif age < 18:
    print("you are {} years old!".format(age))
    print("Your admission cost is $5.")
else:
    print("you are {} years old!".format(age))
    print("Your admission cost is $10.")

    print("you are {} years old!".format(age))
print("\n")
# concise codes:
age = 20
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("you are {} years old!".format(age), "Your admission cost is $" + str(price) + ".")

print("\n")

# Using Multiple elif Blocks

age = 60
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("you are {} years old!".format(age), "Your admission cost is $" + str(price) + ".")

# Omitting the else Block

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("you are {} years old!".format(age), "Your admission cost is $" + str(price) + ".")
