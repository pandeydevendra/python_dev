"""
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits .
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
"""
favorite_fruits = ['bananas', 'apple', 'kiwi']
print("favorite_fruits: {}".format(favorite_fruits))
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
else:
    print("Don't you like bananas?")

if 'apple' in favorite_fruits:
    print("You really like apple!")
else:
    print("Don't you like apple?")
if 'kiwi' in favorite_fruits:
    print("You really like kiwi!")
else:
    print("Don't you like kiwi?")
if 'orange' in favorite_fruits:
    print("You really like orange!")
else:
    print("Don't you like orange?")
if 'mango' in favorite_fruits:
    print("You really like mango!")
else:
    print("Don't you like mango?")
if 'guava' in favorite_fruits:
    print("You really like guava!")
else:
    print("Don't you like guava?")
