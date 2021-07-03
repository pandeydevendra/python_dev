# Importing a Single Class;
from car import Car
from electric_car import Car
from electric_car import Car, ElectricCar
import electric_car

my_new_car = Car('audi', 'a001', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())

print()

# from electric_car import Car

my_new_car = Car('audi', 'a007', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 45
my_new_car.read_odometer()

print()

# Importing Multiple Classes from a Module::

# from electric_car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

print()

# Importing an Entire Module:;

# import electric_car

my_beetle = electric_car.Car('volkswagen01', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = electric_car.ElectricCar('tesla01', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
