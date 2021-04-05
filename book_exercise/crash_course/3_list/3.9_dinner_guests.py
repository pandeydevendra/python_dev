"""
#TODO
find the length of all lists used in examples 3.4 to 3.7
"""
guests = ["ram", 'shyam', "gopal"]
print("Number of guests are = ", len(guests))
guests = ["ram", 'shyam', "gopal"]
print(guests[0].title(), guests[1].title(), guests[-1].title())
message = "Today is my birthday. I invite you to join me at dinner."
for name in guests:
    print("Hello my dear friend Mr. " + name.title() + "! " + message)

# guest who can't make it.
popped_guest = guests.pop()
print("\nMr. " + popped_guest.title() + " is out-station tonight, so he can,t make it to dinner.")
print("The new person I am inviting is Mr. Mohan insetad of Mr. Gopal.")
print("Number of guests are = ", len(guests))

guests.append('mohan')
message = "It's my birthday party tonight. Please join me at dinner."
print("Hello my dear friend Mr. " + guests[-1].title() + "! " + message)
print("Number of guests are = ", len(guests))

# 3.6 starts from here
print("\nHello folks! Good news is that I have found a bigger dinner table")
guests.insert(0, 'bahubali')
print("Number of guests are = ", len(guests))

guests.insert(2, 'batman')
print("Number of guests are = ", len(guests))

print(guests)
print("Number of guests are = ", len(guests))

guests.append('avtar')
print("Number of guests are = ", len(guests))

print(guests)
print("Number of guests are = ", len(guests))

inviation = "It's my birthday party tonight. Let us celebrate. Join me at dinner."
for person in guests:
    print("Hello Mr. " + person.title() + "! " + inviation)
print("\nNumber of guests are = ", len(guests))
