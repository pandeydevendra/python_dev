"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised men
"""
buffet_menu_list = ['rajma-rice', 'chhole-bhatture', 'paneer-paratha', 'continental', 'chinese']
buffet_menu_tuple = ('rajma-rice', 'chhole-bhatture', 'paneer-paratha', 'continental', 'chinese')
print(buffet_menu_list)
print(buffet_menu_tuple)
print("\nMenu list is: ")
for item in buffet_menu_tuple:
    print(item.title())

# modifying a list
buffet_menu_list[0] = 'idly-sambher'
print(buffet_menu_list)
# it works

# Now modifying a tuple
"""
buffet_menu_tuple(0) = 'uttapam'
print(buffet_menu_tuple) #SyntaxError: can't assign to function call

buffet_menu_tuple[0] = 'uttapam'
print(buffet_menu_tuple)
            #TypeError: 'tuple' object does not support item assignment

# TypeError:


Now:::::::::::::::::::::::::::::::
The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple
"""

buffet_menu_modified = ('idly-sambher', 'chhole-bhatture', 'paneer-paratha', 'continental', 'uttapam')
print("\nModified menu list is: ")
for item in buffet_menu_modified:
    print(item.title())

#completed
