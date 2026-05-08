# 2. Two tuples
candy_types = ("sour patch", "gummy bears", "lollipop")
fruity_flavors = ("strawberry", "watermelon", "orange") 

# 3. Candy Combinations 
candy_combinations = {
    candy_types[0] + " - " + fruity_flavors[2],
    candy_types[1] + " - " + fruity_flavors[0],
    candy_types[2] + " - " + fruity_flavors[1],
    candy_types[0] + " - " + fruity_flavors[1],
    candy_types[1] + " - " + fruity_flavors[2],
    candy_types[2] + " - " + fruity_flavors[0] 
}



# 4. Ouput message
print("Today's candy options include:")
print(candy_combinations)

# 5. Output multiple times
print("Today's candy options include:")
print(candy_combinations)

print("Today's candy options include:")
print(candy_combinations)

# What do you notice about the order? 
# Sets are unordered in Python, so each time it print, the items may appear in a different order. 
# This is the key difference between sets and lists/tuples, which always maintain their order in which they were added.


