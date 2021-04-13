# Copying a List:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # All;  just [:], no index;;; actually a copy of original list;though separated
print(my_foods, "\n", friend_foods)

print("\nMy favorite foods are:", my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:", my_foods)
print("\nMy friend's favorite foods are: {}".format(friend_foods))
for food in my_foods:
    print(food.title())

# Now try to make a copy by assigning (=) trick;;;;;
# This doesn't work:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:", my_foods)
print("\nMy friend's favorite foods are: {}".format(friend_foods))
for food in my_foods:
    print(food.title())

"""
This syntax actually tells Python to connect the new variable friend_foods to the list that is already contained in
my_foods , so now both variables point to the same list. As a result, when we add 'cannoli' to my_foods , it will 
also appear in friend_foods . Likewise 'ice cream' will appear in both lists, even though it appears to be added 
only to friend_foods.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nSpecial list: ")
print(players[:])  # All;  just [:], no index;;; actually a copy of original list
