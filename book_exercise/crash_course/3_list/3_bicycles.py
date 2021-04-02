"""In Python, square brackets ( [] ) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles:"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])

print(bicycles[0].title())
print(bicycles[-1])

message = "My first bicycle was a" + " " + bicycles[0].title() + "."
print(message)
message = "My first bicycle was a " + bicycles[-2].upper() + "."
print(message)
