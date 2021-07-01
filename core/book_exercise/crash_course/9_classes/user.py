class User():

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"User's name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        print(f"Welcome Mr. {self.first_name.title()}.")


dev = User('Devendra', 'Pandey')
vin = User('Vinay', 'Pandey')
dev.describe_user()
dev.greet_user()
vin.describe_user()
vin.greet_user()