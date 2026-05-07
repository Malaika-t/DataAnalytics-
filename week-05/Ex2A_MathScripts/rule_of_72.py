# Rule of 72

# Formula: Yeard to double = 72 / interest rate 
 
savings = 5000
interest_rate = 0.08  #8%

years_to_double = 72 / (interest_rate * 100)
doubled_amount = savings * 2

print("Your current savings is $" + format(savings, '.2f') + ".")
print("At a " + format(interest_rate, '.0%') +  " interest rate, your savings account will be worth $" + format(doubled_amount, '.2f') + " in " + format(years_to_double, '.1f') +  " years")