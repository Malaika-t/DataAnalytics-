# Sample Problem:

# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
# print("The total due is " + str(total_due))

# str() converts a number (float/int) to a string so it can be joined with other strings using +.
# str()is used here because total_due is a float(97.79). The + operator can't combine a string and a float directly, it would cause a TypeError.
# str() converts the numberto a string first, making the concatenation possible.

print("Food cost is " + str(food_cost) + " and tax is " + str(tax)) 
# print("Tip is " + str(tip)) 
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))