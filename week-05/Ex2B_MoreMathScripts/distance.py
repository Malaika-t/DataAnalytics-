# Distance 

import math 

x1 = eval(input("Enter x1: "))
y1 = eval(input("Enter y1: "))
x2 = eval(input("Enter x2: "))
y2 = eval(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2)

print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}): {distance:.2f}")