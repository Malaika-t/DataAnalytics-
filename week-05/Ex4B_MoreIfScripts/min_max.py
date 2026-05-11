# Lab 4:

a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"Smallest: {smallest}")
print(f"Largest: {largest}")
