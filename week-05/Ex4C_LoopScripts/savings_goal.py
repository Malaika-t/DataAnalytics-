# Lab 2:

bank_balance = eval(input("Enter your starting bank balance: $"))
savings_goal = eval(input("Enter your savings goal: $"))
weekly_savings = eval(input("Enter your weekly savings amount: $"))

while bank_balance < savings_goal:
    bank_balance += weekly_savings 

    if bank_balance >= savings_goal * 0.75:       #75%
        treat = bank_balance * 0.02               #spent 2% on a treat
        bank_balance -= treat 
        print(f" So close! After treating myself, my balance is up to ${bank_balance:.2f}.")

    elif bank_balance >= savings_goal * 0.50:     #halfway 50%
        print(f"Almost there! This week my balnce is up to ${bank_balance:.2f}.")
    else: 
        print(f"This week my balance increased to ${bank_balance:.2f}.")

print(f"Goal met! My current balance is {bank_balance:.2f}.")

