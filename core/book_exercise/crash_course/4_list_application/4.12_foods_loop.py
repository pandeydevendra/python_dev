my_favorite_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_favorite_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'dry cream']

print("\nFirst four pizza of both the lists are same: ")
print(my_favorite_foods[:4])
print(friend_favorite_foods[:4])

print("\nFirst four pizza of my_favorite_foods lists are: ")
for pizza in my_favorite_foods[:4]:
    print(pizza.title())

print("\nLast three pizzas of my friend's favorite are: ")
for pizza in friend_favorite_foods[-3:]:
    print(pizza.title())

"""
print("All food items are: ")
for food_1 in my_favorite_foods:
    for food_2 in friend_favorite_foods:
        print(food_1, food_2)

"""
