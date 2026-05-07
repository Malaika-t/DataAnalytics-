# Calculate Tip with input()-Lab 3

bill = float(input("How much was your restaurant bill?"))
tip_percentage = float(input("What tip percentage would you like to give?"))

tip = bill * tip_percentage

print(f"The tip on a ${bill} restaurant bill is ${tip}")