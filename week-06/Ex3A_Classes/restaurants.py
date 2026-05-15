# Lab 1:

class Restaurant:
    """A class represent a restaurant with a name and food type."""
    # Constructor method:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")
    
# Three instances:
mcdonalds = Restaurant("McDonald's", "burgers")
applebees = Restaurant("Applebee's", "American food")
dunkin = Restaurant("Dunkin' Donuts", "coffee and donuts")

# Call methods for each instance:
mcdonalds.describe_rest()
mcdonalds.rest_open()

applebees.describe_rest()
applebees.rest_open()

dunkin.describe_rest()
dunkin.rest_open()