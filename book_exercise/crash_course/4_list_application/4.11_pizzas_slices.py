my_pizzas = ['veg mushroom pizza', 'vegan pepperoni pizza', 'domino special pizza']
friend_pizzas = my_pizzas[:]
print(my_pizzas, "\n", friend_pizzas)

my_pizzas.append('grilled paneer pizza')
friend_pizzas.append('capsicum tikka pizza')
print("my favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza.title())
print("\nmy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())


#slices
print(my_pizzas[:3])

print(my_pizzas[1:])
print(friend_pizzas[-3:])
print(friend_pizzas[:])

print("\n", my_pizzas[:3], friend_pizzas[-3:])