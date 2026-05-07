# Tiles

import math 

length, width = input("Enter the length and width of the room (feet), separated by a space: ").split()
length = float(length)
width = float(width)

area = length * width

tiles_needed = area * 1.10  # 10% more tiles
boxes_needed = math.ceil(tiles_needed / 12)  # 12 tiles per box and must buy full boxes

print(f"\nRoom area: {area:.0f} square feet")
print(f"Tiles needed (with 10% extra): {math.ceil(tiles_needed)}")
print(f"Boxes to buy: {boxes_needed}")
