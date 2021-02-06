print("Hello World!")
message = "Print this message!"
print(message)
message = "Print this new message!"
print(message)

s = "This is a string."
print(s)
s1 = 'This is also a string.'
print(s1)
s1 = 'I told my friend, "Python is my favorite language!"'
print(s1)
s1 = "The language 'Python' is named after Monty Python, not the snake."
print(s1)
s1 = "One of Python's strengths is its diverse and supportive community."
print(s1)

name = "ada lovelace"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print(full_name.title())
print(full_name.upper())
print(full_name.lower())

print("Hello, " + full_name.title() + "!")
print("Hello, {}!".format(full_name.title()))

print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tC++\n\tJavaScript")
print("Languages:\nPython\nC\nC++\nJavaScript")
# message = 'One of Python's strengths is its diverse community.'
print(message)
message = "One of Python's strengths is its diverse community."
print(message)
message = 'One of Python"s strengths is its diverse community.'
print(message)
print('\tAlbert Einstein once said, “A person who never made a \n\tmistake never tried anything new.”')

famous_person = "Albert Einstein"
famous_quote = "A person who never made a mistake never tried anything new."
statement = famous_person + " " + "once said," + " " + famous_quote
print(statement)
famous_person = "\tAlbert Einstein"
famous_quote = '"A person who never made a \n\tmistake never tried anything new."'
statement = famous_person + " " + "once said," + " " + famous_quote
print(statement)

# stripping
favorite_language = '  python   '
print(favorite_language)
print(favorite_language.rstrip())
favorite_language
print(favorite_language.lstrip())
print(favorite_language.strip())
age = 23
wish = "Happy" + " " + str(age) + "rd Birthday."
print(wish)
age = "24"
wish = "Happy" + " " + age + "th Birthday."
print(wish)
print(5 + 3)
print(4 * 2)
print(10 - 2)
print(16 / 2)
print(int(16 / 2))

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[2])
print(bicycles[0].title())
print(bicycles[-2].title())
print(bicycles[0].upper())
print(bicycles[-1].lower())
message1 = "My first bicycle was a " + bicycles[0].title() + "."
message = "My first bicycle was a " + bicycles[-1].upper() + "."
print(message1)
print(message)
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles1 = []     #empty list
motorcycles1.append('honda')
motorcycles1.append('yamaha')
motorcycles1.append('suzuki')
print(motorcycles1)
#motorcycles.append('ducati')
print(motorcycles1)
#motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles1.insert(0, 'ducati')
print(motorcycles1)
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[-1]
print(motorcycles)
print('1')
motorcycles.remove('yamaha')
print(motorcycles)
motorcycles1.remove('yamaha')
print(motorcycles1)
motorcycles2 = ['honda', 'a', 'yamaha', 'suzuki']
print(motorcycles2)
popped_motorcycle = motorcycles2.pop()
print(motorcycles2)
print(popped_motorcycle)
popped_motorcycle = motorcycles2.pop(2)
print(motorcycles2)
print(popped_motorcycle)
popped_motorcycle = motorcycles2.pop(-1)
print(motorcycles2)
print(popped_motorcycle)
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
motorcycles2 = ['honda', 'a', 'yamaha', 'suzuki']
last_owned = motorcycles2.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
first_owned = motorcycles1.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
first_owned = motorcycles2.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")
print(motorcycles)
print("\nA " + "car list for me.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#cars.sort(reverse=False)
#print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)