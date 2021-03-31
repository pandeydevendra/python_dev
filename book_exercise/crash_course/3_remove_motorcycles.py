#Removing Elements from a List
#Removing an Item Using the del Statement
'''If you know the position of the item you want to remove from a list, you can use the del statement.'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)							#['honda', 'yamaha', 'suzuki']


del motorcycles[0]          						#element of position 0 get removed
print(motorcycles)							#	  ['yamaha', 'suzuki']

'''You can remove an item from any position in a list using the del statement if you know its index. For example, here’s how to remove the second item, 'yamaha' , in the list:'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)							#['honda', 'yamaha', 'suzuki']

del motorcycles[1]							#The second motorcycle is deleted from the list:
print(motorcycles)							#['honda','suzuki']

'''In both examples, you can no longer access the value that was removed from the list after the del statement is used.'''

#Removing an Item Using the pop() Method;          >>pop is reciprocal to append (both works for end element by default):

'''Sometimes you’ll want to use the value of an item after you remove.The pop() method removes the last item in a list, but it lets you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the stack. In this analogy, the top of a stack corresponds to the end of a list. Let’s pop a motorcycle from the list of motorcycles:'''

motorcycles = ['honda', 'yamaha', 'suzuki']				
print(motorcycles)							#['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)							#['honda', 'yamaha']
print(popped_motorcycle)						# suzuki


'''How might this pop() method be useful? Imagine that the motorcyclesin the list are stored in chronological order according to when we owned them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought:'''

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")                       #The last motorcycle I owned was a Suzuki.


'''You can actually use pop() to remove an item in a list at any position by including the index of the item you want to remove in parentheses.'''
#Popping Items from any Position in a List:
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing an Item by Value:
'''won’t know the position of the value only know the value of the item you want to remove, you can use the remove() method. For example, let’s say we want to remove the value 'ducati' from the list of motorcycles.'''

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)							#['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')
print(motorcycles)							#['honda', 'yamaha', 'suzuki']



'''You can also use the remove() method to work with a value that’s being removed from a list. Let’s remove the value 'ducati' and print a reason for removing it from the list:'''
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")				#A Ducati is too expensive for me.


'''Note:
The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed. You’ll learn how to do this in Chapter 7.'''
