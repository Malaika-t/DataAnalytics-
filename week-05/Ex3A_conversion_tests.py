# Description: This script tests various numeric conversion techniques
# Author: Malaika Tariq Newprogrammer

# variables:
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Transformation of a:

# a_int = int(a)                    # ValueError: invalid literal for int() with base 10 - fails, because it has decimal point
a_float = float(a)                  # works because a is a numeric string with spaces - it gives 101.1
a_int_from_float = int(float(a))    # works, first float and then int
a_sliced = int(float(a.strip()))     # strip spaces around it, cast to float then int 

print(a, type(a))                                      
print(a_float, type(a_float))                           
print(a_int_from_float, type(a_int_from_float))         
print(a.strip(), type(a.strip())) 


# Transformation of b:

b_int = int(b)                     # works as b is a valid integer string
b_float = float(b)                 # works, b can be a float too 

print(b, type(b))
print(b_int, type(b_int))
print(b_float, type(b_float))


# Transformation of c:

# c_int = int(c)                   # ValueError: invalid literal for int() with base 10 - invalid, because it has text "Stevens"
# c_float = float(c)               # ValueError: could not convert string to float: '402 Stevens' - invalid, because it has text "Stevens"
c_sliced = int(c[:3])              # Slices just the first 3 charaters "402" (index 0-2) and then cast to int 

print(c, type(c))
print(c_sliced, type(c_sliced))


# Transformation of d:
# d_int = int(d)                   # ValueError: invalid literal for int() with base 10 - invalid, because it has text "Number"
# d_float = float(d)               # ValueError: could not convert string to float - inavlid, because it has text "Number"
d_sliced = int(d[7:8])             # Slices just '5' out and then cast to int

print(d, type(d))
print(d_sliced, type(d_sliced))
print(d.strip(), type(d.strip()))

                                                         


