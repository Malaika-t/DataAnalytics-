# Variables
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000"

# 3) Use .lower()
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# 4) Use .title()
print(name_1.title())
print(name_2.title())
print(name_3.title())

# 5) Use .replace()
print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))

print(type(salary_1.replace("$", "")))     # <class 'str'> - It is a string, to perform math on them we need to convert it into int()

# 6) Chain .replace() and int() together
salary_1_clean = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_clean, type(salary_1_clean))