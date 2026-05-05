print('Hello world!')

message = "Hello world!"
print(message)

# "Hello world" prints twice because there are two print statemnets 
# One prints the string directly, and one prints it through the variable.

# Displaying dollars and cents
dollars = 3
cents = .50
print(dollars + cents)

# Adding dollars (3) and cents(.50) gives 3.5, not 3.50
# Python adds them as numbers, not as a formatted currency amount. 

cents = cents + .25
print(dollars + cents)

d_str = '3 dollars'
c_str = '50 cents'
print(d_str + ' ' + c_str)