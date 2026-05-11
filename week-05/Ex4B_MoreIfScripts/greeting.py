# Lab 2:

hour = eval(input("Enter the current hour (0-23): "))
if hour < 10:
    print("Good Morning!")
elif hour >= 10 and hour < 17:
    print("Good day!")
elif hour >=23 or hour < 4:
    print("What are you doing up so late?")
else:
    print("Good evening!")