cars = ['audi', 'bmw', 'subaru', 'toyota']
# checking equality (==)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("\nMethod-2:-")
# checking inequality (!=) 
cars = ['audi', 'bmw', 'honda']
for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.swapcase())

print("\nMethod-3:-")
cars_up = []
for car in cars:
    if car != 'bmw':
        cars_up.append(car.title())
    else:
        cars_up.append(car)
print(cars_up)

for car in cars_up:
    if car.lower() == 'audi':
        print("{} is in list.".format(car))
    else:
        print(car)
