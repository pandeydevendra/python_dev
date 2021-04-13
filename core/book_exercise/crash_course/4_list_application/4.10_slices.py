storage_items = ['grains', 'veggies', 'fruits', 'fatties', 'pulses', 'leaves']
print("The first three items in the list are: ")
print(storage_items[0:3])
print(storage_items[:3])
for item in storage_items[:3]:
    print(item.swapcase())

print("Four items from the middle of the list are:")
print(storage_items[1:5])
print(storage_items[-5:-1])
for item in storage_items[-5:-1]:
    print(item.title())

print("The last three items in the list are:")
print(storage_items[-3:])
print(storage_items[-1], storage_items[-2], storage_items[-3])
for item in storage_items[:3]:
    print(item.swapcase())
