responses = {}

# set a flag to indicate that polling is active::

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb? ")
    # store the response in the dictionary:
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# polling is complete ..show the results..
print("\n--Poll Results -- ")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
