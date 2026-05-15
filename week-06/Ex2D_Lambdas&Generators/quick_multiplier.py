# Lab 1:

doubler = lambda n: n * 2

print("--- Doubler ---")
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))


tripler = lambda n: n * 3

print("\n--- Tripler ---")
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


def multiplier(factor):
    return lambda n: n * factor

quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7) 
octupler = multiplier(8)
nonupler = multiplier(9) 
decupler = multiplier(10)


print("\n--- Quadrupler (x4) ---")
print(quadrupler(8))

print("\n--- Quintupler (x5) ---")
print(quintupler(8))

print("\n--- Sextupler (x6) ---")
print(sextupler(8))

print("\n--- septupler (x7) ---")
print(septupler(8))

print("\n--- Octupler (x8) ---")
print(octupler(8))

print("\n--- Nonupler (x9) ---")
print(nonupler(8))

print("\n--- Decupler (x10) ---")
print(decupler(8))