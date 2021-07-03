class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name_p, cuisine_type_p):
        self.restaurant_name = restaurant_name_p
        self.cuisine_type = cuisine_type_p
        """Add an attribute that stores the car’s overall mileage."""
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} has cuisine type {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open now.")

    def count_person(self):
        """Print a statement showing the number of persons served."""
        print(f"The restaurant has served {str(self.number_served)} persons.")

    def set_number_served(self, number_of_served):
        self.number_served = number_of_served

    def increment_number_served(self):
        self.number_served += 1

if __name__ == "__main__":
    kansar = Restaurant("Kansar", "Maharaja Thali")
    ub_dhaba = Restaurant('Urban Dhaba', 'Pyaz Paratha')
    kansar.describe_restaurant()
    ub_dhaba.describe_restaurant()
    kansar.open_restaurant()
    ub_dhaba.open_restaurant()

    kansar.count_person()
    ub_dhaba.count_person()

    kansar.set_number_served(5)
    kansar.count_person()
    kansar.increment_number_served()
