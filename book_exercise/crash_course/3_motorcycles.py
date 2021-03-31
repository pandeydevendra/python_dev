#Changing, Adding, and Removing Elements:

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)                                 # ['honda', 'yamaha', 'suzuki']


#Modifying Elements in a List:

motorcycles[0] = 'ducati'
print(motorcycles)                                 #['ducati', 'yamaha', 'suzuki']
               
motorcycles[-1] = 'bmw'
print(motorcycles)                                 #['ducati', 'yamaha', 'suzuki', 'bmw']


#Adding Elements to a List; "Appending" Elements to the End of a List:
'''The simplest way to add a new element to a list is to append the item to the
list. When you append an item to a list, the new element is added to the end
of the list. Using the same list we had in the previous example, we’ll add the
new element 'ducati' to the end of the list:'''

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)									 #['honda', 'yamaha', 'suzuki'] 
#append  :add at last
motorcycles.append('ducati')
print(motorcycles)	   #The append() method adds 'ducati' to the end of the list without affecting any of the other elements in the list:
							                                 #['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles = []            #create an empty list and fill the elements by append function

motorcycles.append('honda')
motorcycles.append('yamaha')
print(motorcycles)                                                        #['honda', 'yamaha'] 
motorcycles.append('suzuki')
motorcycles.append('bmw')
print(motorcycles)									 #['honda', 'yamaha', 'suzuki', 'bmw'] 

#insert  :use index for desired location

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
motorcycles.insert(-1, 'bmw')
print(motorcycles)







