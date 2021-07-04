import json

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'


def get_stored_username():
    """Get stored username if available."""
    try:
        # filename = 'username.json'
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"""Welcome back {username}!""")
    else:
        username = input("What is your name? ")
        # filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print(f"""We'll remember you when you come back, {username}!""")


greet_user()
