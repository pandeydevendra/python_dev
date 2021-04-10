# Checking Whether a Value Is Not in a List:
banned_users = ['andrew', 'carolina', 'david', 'john']
print("Banned users: {}".format(banned_users))
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", you are banned, you can't post a response.")
if 'john' not in banned_users:
    print("John, you can post a response if you wish.")
else:
    print("John, you are banned, you can't post a response.")
