# 10a.
f = open("about_me.txt", "r")

# 10b.
# print(f.read())

# 10c.
# f.close()

# 12.
# print(f.read(50))
# print(f.read(50))

# 13a.
# print(f.readline(10))
# print(f.readline())

# 13b.
# for i in range(1, 5):
#     print(f.readline())

# 14a.
# print(f.readline())      

# 14b. 
# print(f.readlines(1))     
                        
# 14c.
# print(f.readlines(10))     

# 14d. 
# print(f.readlines(10))

# 14e.
# print(f.readlines(100))
# print(f.readlines(-1))

# 15.
var_a = f.read(50)

var_b = []
for i in range (1, 5):
    var_b.append(f.readline())

var_c = f.readline(100)

# 16. 
print(f"First 50 characters: {var_a}")
print(f"Next four lines, as list by line: {var_b}")
print(f"Next 100 characters, as list by line, rounded up to complete lines: {var_c}")

f.close()