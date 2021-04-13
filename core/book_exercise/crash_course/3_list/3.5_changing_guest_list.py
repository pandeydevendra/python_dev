# program to modify list
guests = ["ram", 'shyam', "gopal"]
print(guests)
print(guests[0].title(), guests[1].title(), guests[-1].title())
message = "Today is my birthday. I invite you to join me at dinner."
for name in guests:
    print("Hello my dear friend Mr. " + name.title() + "! " + message)

# guest who can't make it.
popped_guest = guests.pop()
print("\nMr. " + popped_guest.title() + " is out-station tonight, so he can,t make it to dinner.")
print("The new person I am inviting is Mr. Mohan insetad of Mr. Gopal.")

# new list
print(guests)
guests.append('mohan')
print(guests)
message = "It's my birthday party tonight. Please join me at dinner."
for name in guests:
    print("Hello my dear friend Mr. " + name.title() + "! " + message)
