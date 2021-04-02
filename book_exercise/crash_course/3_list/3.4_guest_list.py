#program to inviting three persons
guests = ["ram", 'shyam', "gopal"]
print(guests)
print(guests[0].title(), guests[1].title(), guests[-1].title())
message = "Today is my birthday. I invite you to join me at dinner."
print("Hello my dear friend Mr. " + guests[0].title() + "! " + message)
for name in guests:
    print("Hello my dear friend Mr. " + name.title() + "! " + message)
