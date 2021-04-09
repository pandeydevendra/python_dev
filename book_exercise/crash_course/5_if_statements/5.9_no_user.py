"""
No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
usernames = ['Admin', 'John', 'rahul', 'admin', 'sachin', 'Virat_007', 'Eric']
"""
usernames = []
if usernames:
    for user in usernames:
        print("Hello {}! Would you like to see a status report?".format(user.title()))
else:
    print("List is empty. We need to find some users!")

usernames.append('Admin')
usernames.insert(0, 'John')
usernames.insert(0, 'rahul')
usernames.append('eric')
usernames.append('sachin')
print("\n", usernames)
if usernames:
    for user in usernames:
        if user.lower() == 'admin':
            print("Hello {}! Would you like to see a status report?".format(user.title()))
        else:
            print("Hello {}! Thank you for logging in again.".format(user.title()))
else:
    print("List is empty. We need to find some users!")

del usernames[0]
del usernames[-1]
usernames.pop()
usernames.pop(1)
usernames.remove('John')
print("\n", usernames)
print(usernames[:])
