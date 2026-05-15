# Lab 1:

class Restaurant:
    """A class represent a restaurant with a name and food type."""
    # Constructor method:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
    
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
       amount = int(input("How many customers served today?"))
       self.number_served += amount
    
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("How would you rate your experience today on a scale of 1-5(5 being excellent)?")
            try:
                rating = int(rating)
                if 1 <= rating <= 5:

                    self.customer_ratings.append(rating)
                    average = sum(self.customer_ratings) / len(self.customer_ratings)
                    print(f"Your rating was {rating}. The avergae rating for this restaurant is {average:.1f}.")
                    break
                else:
                    print("Invalid input. Please enter a whole number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a whole number between 1 and 5.")

# Three instances:
mcdonalds = Restaurant("McDonald's", "burgers")
applebees = Restaurant("Applebee's", "American food")
dunkin = Restaurant("Dunkin' Donuts", "coffee and donuts")

# Test new methods:
 
# Test McDonald's
print("---- McDonald's ----")
mcdonalds.print_num_served()         # Check initial value
mcdonalds.add_num_served()           # Add       
mcdonalds.add_num_served()           # Add a few times
mcdonalds.print_num_served()         # print again
mcdonalds.customer_rating()          # Add
mcdonalds.customer_rating()          # Add
mcdonalds.customer_rating()          # Add a few times 

# Test Applebee's
print("\n---- Applebee's ----")
applebees.print_num_served()        
applebees.add_num_served()            
applebees.print_num_served()         
applebees.customer_rating()         
applebees.customer_rating()          
      
# Test Dunkin' Donuts
print("\n---- Dunkin' Donuts ----")
dunkin.print_num_served()        
dunkin.add_num_served()            
dunkin.print_num_served()         
dunkin.customer_rating()         
dunkin.customer_rating()            