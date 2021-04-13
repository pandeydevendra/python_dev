"""Hello Admin: Make a list of five or more usernames, including the name
'admin' . Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin' , print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.
"""
usernames = ['Admin', 'John', 'rahul', 'admin', 'sachin', 'Virat_007', 'Eric']
for user in usernames:
    if user.lower() == 'admin':
        print("Hello {}! Would you like to see a status report?".format(user.title()))
    else:
        print("Hello {}! Thank you for logging in again.".format(user.title()))