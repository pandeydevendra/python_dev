"""
Organising a list by
1. sorting a list >> sort() : changes list permanently, >>sorted ; tmeporarily
 2.
"""

cars = ["bmw", "audi", "toyata", "subaru"]
print(cars)
print("Number of cars are = ", len(cars))
cars.sort()  # sort() function arrange list in alphabetical order
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyata", "subaru"]
cars.sort(reverse=True)
print(cars)

cars = ["bmw", "audi", "toyata", "subaru"]
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))  # sorted() function
print("\nHere is the original list again:")
print(cars)
# print(sorted(cars(reversed()t))) >> how sorted() function accept a reverse=True argument, example????
# cars.sorted(reversed(True))

print(sorted(cars, reverse=True))  # orted() function accept a reverse=True argument, found.

# cars = ["bmw", "audi", "toyata", "subaru"] #reverse with with sorted doesn't affect origin list for futher uses.
# here again writing list cars is redundant...
cars.reverse()  # reverse() function does not sort alphabetically
print(cars)
print("Number of cars are = ", len(cars))
"""
# Length of a list; very simple >> len(list_name)
>>>len(cars) #@# it will run on terminal with python, or on idle not on pycharm...
"""
