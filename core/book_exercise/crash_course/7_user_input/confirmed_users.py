# start with users list and an empty confirmed users list::

unconfirmed_users = ['mohan', 'sohan', 'alice', 'harry']
print("unconfirmed_users", unconfirmed_users)
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print(f"\nConfirmed Users: {confirmed_users}")
print("\nThe following users have been confirmed: ")

for confirmed_user in confirmed_users:
    print(confirmed_user)
