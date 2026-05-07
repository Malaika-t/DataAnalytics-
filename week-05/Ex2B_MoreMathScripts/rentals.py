# Rentals 

import math

people = eval(input("Enter the number of people going on the tour: "))

van_seats = 15
van_cost = 250

vans_needed = math.ceil(people / van_seats)
total_cost = vans_needed * van_cost
cost_per_person = total_cost / people

print(f"\nNumber of people: {people}")
print(f"Vans needed: {vans_needed}")
print(f"Total cost to rent vans: ${total_cost:.2f}")
print (f"Cost per person: ${cost_per_person:.2f}")

# Calculations with 38 tourists:
# a) How much money did your script say you had to charge per person? $19.74
# b) If you multiply that out, how much did you collect? $19.74 x 38 = $749.12
# c) How much were the vans? 3 vans x $250 = $750
# d) Why do you have leftover money? The leftover happens because you are charging each person a rounded up whole amount that doesn't divide evenly by 38 people.Each person was cahrged $20 so you collect $760 but the vans cost $750, meaning you have $10 leftover. 