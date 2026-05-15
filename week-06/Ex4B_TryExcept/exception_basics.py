# ValueError
try:
    x = int("banana")
except ValueError:
    print("ValueError: Oops, that value can't be converted to the expected type.")
else:
    print(x)
finally:
    print("Let's try another one...")


# NameError
try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable.")
else:
    print(m)
finally:
    print("Let's try another one...")


# TypeError
try:
    result = "hello" + 5
except TypeError:
    print("TypeError: Oops, you tried to perform an operation on incompatible types.")
else:
    print(result)
finally:
    print("Let's try another one...")


# SyntaxError
try:
    exec("if x==")
except SyntaxError: 
    print("SyntaxError: Oops, theres a syntax mistake in the code.")
else:
    print("No syntax error found.")
finally:
    print("Let's try another one...")
