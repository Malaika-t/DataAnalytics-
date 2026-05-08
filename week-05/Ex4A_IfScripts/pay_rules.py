pay_rate = eval(input("Enter pay rate:"))
hours_worked = eval(input("Enter hours worked:"))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = pay_rate * hours_worked

print("Gross Pay:", gross_pay)