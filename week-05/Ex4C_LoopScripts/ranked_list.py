# Lab 3:

favorites = ["tacos", "ramen", "jerk chicken", "injera", "pierogi"]

for index, item in enumerate (favorites, start=1):
    line = f"{index}. {item}"
    if index == 1:
        line += "<- top pick!"
    print(line)
print()