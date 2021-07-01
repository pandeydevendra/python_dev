class Restaurant():
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name_p, cuisine_type_p):
        self.restaurant_name = restaurant_name_p
        self.cuisine_type = cuisine_type_p

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} has cuisine type {self.cuisine_type.title()}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name.title()} is open now.")


kansar = Restaurant("Kansar", "Maharaja Thali")
ub_dhaba = Restaurant('Urban Dhaba', 'Pyaz Paratha')
kansar.describe_restaurant()
ub_dhaba.describe_restaurant()
kansar.open_restaurant()
ub_dhaba.open_restaurant()
