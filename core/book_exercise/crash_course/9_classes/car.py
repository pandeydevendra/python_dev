class Car:
    """Asimple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        print("Constructor of Car is called.")
        self.make = make
        self.model = model
        self.year = year
        """Add an attribute that stores the car’s overall mileage."""
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car mileage."""
        return f"This car has {str(self.odometer_reading)} miles on it."

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
         Reject any change in odometer setting."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            return f"You can't roll back an odometer."

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


if __name__ == "__main__":
    my_new_car = Car('audi', 'a4', 2016)
    print(my_new_car.get_descriptive_name())
    print(my_new_car.read_odometer())

    """Modifying an Attribute’s Value Directly."""

    my_new_car.odometer_reading = 23
    print(my_new_car.read_odometer())

    """Modifying an Attribute’s Value Through a Method."""

    my_new_car.update_odometer(45)
    print(my_new_car.read_odometer())

    """Reject any change in odometer setting."""

    my_new_car.update_odometer(20)
    print(my_new_car.read_odometer())

    """Incrementing an Attribute’s Value Through a Method."""
    print()
    my_used_car = Car('subaru', 'outback', 2013)
    print(my_used_car.get_descriptive_name())
    my_used_car.update_odometer(23500)
    print(my_used_car.read_odometer())
    my_used_car.increment_odometer(100)
    print(my_used_car.read_odometer())
