"""
In summary, if you want only one block of code to run, use an if - elif -
else chain. If more than one block of code needs to run, use a series of
independent if statements.
"""
# Testing Multiple Condition::::

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# not finished desired order ::
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
"""
The test for 'mushrooms' is the first test to pass, so mushrooms are added
to the pizza. However, the values 'extra cheese' and 'pepperoni' are never
checked, because Python doesn’t run any tests beyond the first test that
passes in an if-elif-else chain. The customer’s first topping will be added,
but all of their other toppings will be missed:
"""

# checking an empty list:
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\nAdding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
