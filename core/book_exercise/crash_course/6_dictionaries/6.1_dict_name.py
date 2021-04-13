"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name , last_name , age , and city . Print each
piece of information stored in your dictionary.
"""
person = {'first_name': 'rahul', 'last_name': 'dravid', 'age': '45', 'city': 'banglore'}
print(person)
First_name = person['first_name'].title()
print(First_name, "\n")
print(person['first_name'].title())
print(person['last_name'].title())
print(person['age'])
print(person['city'].title(), "\n")
print(person['first_name'].title() + " " + person['last_name'].title() + " is " + str(person['age']) +
      " years old. He lives in " + person['city'] + ".")
