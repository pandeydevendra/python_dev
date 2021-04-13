# 3.6 starts from here
guests = ["ram", 'shyam', "mohan"]
print("\nHello folks! Good news is that I have found a bigger dinner table")
guests.insert(0, 'bahubali')
guests.insert(2, 'batman')
print(guests)
guests.append('avtar')
print(guests)
inviation = "It's my birthday party tonight. Let us celebrate. Join me at dinner."
for person in guests:
    print("Hello Mr. " + person.title() + "! " + inviation)

# 3.7 starts from here onward:
print(
    "\nI'm very sad that the bigger dining table is not going to reach on time. So, unfortunately I have to invite to only two of my guests.")
cancellation = "I'm sorry I can't invite you to dinner."
guests_popped_1 = guests.pop()
print("\tHello Mr. " + guests_popped_1.title() + "! " + cancellation)
guests_popped_2 = guests.pop()
print("\tHello Mr. " + guests_popped_2.title() + "! " + cancellation)
guests_popped_3 = guests.pop()
print("\tHello Mr. " + guests_popped_3.title() + "! " + cancellation)
guests_popped_4 = guests.pop()
print("\tHello Mr. " + guests_popped_4.title() + "! " + cancellation)
print(guests)
message = "You are still in the list. Let us celebrate. Join me at dinner."
for guest in guests:
    print("\n\tHello Mr. " + guest.title() + "! " "Luckily " + message)

# delete to empty list:
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)  # empty list.
