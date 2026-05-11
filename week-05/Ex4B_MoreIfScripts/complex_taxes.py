# Lab 3: Federal Tax Calculation:

hours_worked = eval(input("Enter hours worked: "))
pay_rate = eval(input("Enter hourly pay rate: "))
filing_status = input("Enter filing status('single' or 'joint')? : ").strip().lower()

# Gross Pay Calculation (from pay_rules.py)
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    weekly_gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    weekly_gross_pay = pay_rate * hours_worked

# Annual Gross Pay Calculation
weeks_per_year = 52
annual_gross_pay = weekly_gross_pay * weeks_per_year

# Tax Rate 
if filing_status == 'single':
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif 12000 <= annual_gross_pay <= 24999.99:
        tax_rate = 0.10
    elif 25000 <= annual_gross_pay <= 74999.99:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

elif filing_status == 'joint':
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif 12000 <= annual_gross_pay <= 24999.99:
        tax_rate = 0.06
    elif 25000 <= annual_gross_pay <= 74999.99:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
        
else:
    print("Invalid filing status. Please enter 'single' or 'joint'.")
    exit()

# Weekly Tax
weekly_tax = weekly_gross_pay * tax_rate 

# Net Pay 
net_pay = weekly_gross_pay - weekly_tax

# Output 
print(f"\nYou worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}")
print(f"Your net pay is ${net_pay:.2f}")


