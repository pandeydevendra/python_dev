def greet_user():
    print("Hello!")


greet_user()


# passing an input
def greet_user(username):
    print(f"Hello {username.title()}!")


greet_user('jesse')
greet_user('sarah')
