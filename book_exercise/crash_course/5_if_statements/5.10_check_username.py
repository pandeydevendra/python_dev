"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users .
• Make another list of five usernames called new_users . Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•
Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
usernames = ['Admin', 'John', 'rahul', 'admin', 'sachin', 'Virat_007', 'Eric']
"""

current_users = ['Admin', 'John', 'Rahul', 'Mukesh', 'Sachin', 'Virat_007', 'Eric']
new_users = ['John', 'Anil', 'Rahul', 'Steve', 'Eric']
for username in new_users:
    if username in current_users:
        print("Username '{}' has already been used.".format(username))
    else:
        print("The username '{}' is available.".format(username))
