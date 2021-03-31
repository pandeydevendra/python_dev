"""In Python, square brackets ( [] ) indicate a list, and individual elements
in the list are separated by commas. Here’s a simple example of a list that
contains a few kinds of bicycles:"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing Elements in a List
"""Lists are ordered collections, so you can access any element in a list by
telling Python the position, or index, of the item desired. To access an ele-
ment in a list, write the name of the list followed by the index of the item
enclosed in square brackets.
For example, let’s pull out the first bicycle in the list bicycles :
bicycles = ['trek', 'cannondale', 'redline', 'specialized']"""
 
print(bicycles[0])

'''You can also use the string methods from Chapter 2 on any element in
a list. For example, you can format the element 'trek' more neatly by using
the title() method:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']'''

print(bicycles[0].title())

#Index Positions Start at 0, Not 1
#for accessing the last element in a list. By asking for the item at index -1 , Python always returns the last item in the list:

print(bicycles[-1])

'''This code returns the value 'specialized' . This syntax is quite useful,
because you’ll often want to access the last items in a list without knowing
exactly how long the list is. This convention extends to other negative index
values as well. The index - 2 returns the second item from the end of the list,
the index - 3 returns the third item from the end, and so forth.'''

#Using Individual Values from a List
message = "My first bicycle was a" + " " + bicycles[0].title() + "."
print(message)
