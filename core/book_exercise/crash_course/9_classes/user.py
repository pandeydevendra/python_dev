class User():

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name
        """Add an attribute login attempt."""
        self.login_attempt = 0

    def describe_user(self):
        print(f"User's name is {self.first_name.title()} {self.last_name.title()}.")

    def greet_user(self):
        print(f"Welcome Mr. {self.first_name.title()}.")

    def count_user_login(self):
        print(f"{self.first_name.title()} has attempted to login {str(self.login_attempt)} times.")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


dev = User('Devendra', 'Pandey')
vin = User('Vinay', 'Pandey')
dev.describe_user()
dev.greet_user()
vin.describe_user()
vin.greet_user()

dev.count_user_login()
dev.increment_login_attempts()
dev.count_user_login()
dev.increment_login_attempts()
dev.increment_login_attempts()
dev.increment_login_attempts()
dev.count_user_login()

dev.reset_login_attempts()
dev.count_user_login()

vin.count_user_login()
vin.reset_login_attempts()
vin.count_user_login()
vin.increment_login_attempts()
vin.increment_login_attempts()
vin.count_user_login()