class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age, color):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        """Simulate a dog sitting in response to command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to command."""
        print(f"{self.name.title()} rolled over.")


my_dog = Dog('willi', 6, 'black')
print(my_dog)
print(my_dog.__dict__)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {str(my_dog.age)} years old.")
print(f"It is {my_dog.color}.")

my_dog.sit()
my_dog.roll_over()
