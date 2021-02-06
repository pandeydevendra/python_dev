#'in' operator is used to find out whether a item is in list or not.
heroes = ['spiderman', 'thor', 'irnman', 'hulk', 'captain america']
len(heroes)

food=["rice", "pulse","maize","chana"]
veg=["tomato", "potato", "pumpkin"]     
list=food+veg  #food+"ghee" ; invalid syntax
print("old list:",list)

food.append("peanut")
print("food:",food)
veg.insert(2,"beans")
print("veg:", veg)
print(food[0])
print(veg[-1])

list=food+veg
print("new list:",list)

#rice in list