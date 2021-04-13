"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
"""
favorite_numbers = {
    "Rahul": '5',
    "Mohanty": '10',
    "Modi": '11',
    "Trump": '8',
    "Biden": '9',
    "Elizabeth": '16'
}

# more than a line;;;;

print(favorite_numbers)

for name in favorite_numbers:
    #print(name)
    print(name.title() + "'s favorite numbers is " + favorite_numbers[name] + ".")
