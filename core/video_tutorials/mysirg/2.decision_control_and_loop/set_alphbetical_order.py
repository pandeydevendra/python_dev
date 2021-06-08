# Arranging words in alphabetical order is very easy if words are in a list:

x = [eval(x) for x in input("Enter some words: ").split(' ')]
print("Words are: ", x)
x.sort()
print(x)

# TODO >> Arrange set of words in alphabetical order:
"""
x = set([eval(x) for x in input("Enter some words: ").split(' ')])
print("Words are: ", x)
x_alphabetial = x.sort([x])
print(x_alphabetial)

output::

x_alphabetial = x.sort([x])
AttributeError: 'set' object has no attribute 'sort'

"""