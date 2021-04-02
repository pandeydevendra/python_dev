# Changing, Adding, and Removing Elements:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying Elements in a List:
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[-1] = 'bmw'
print(motorcycles)

# Adding Elements to a List; "Appending" Elements to the End of a List:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')  # append  :add at last
print(motorcycles)

motorcycles = []  # create an empty list and fill the elements by append function
motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)
motorcycles.append('suzuki')
motorcycles.append('bmw')
print(motorcycles)

# insert  :use index for desired location
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(-1, 'bmw')
print(motorcycles)
