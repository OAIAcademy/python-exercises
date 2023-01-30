# Hello World!


print("Hello World!")

# Variables declaration

a = 10
b = "pippo"
c = a
d = a + 1
print(a, b, c, d)

# Build-in types
#   numeric
base_10_integer = 173
binary = 0b0101
octal = 0o255
hexadecimal = 0xFF
floating_point = 3.14
floating_point_sci = 1.14E-12
complex_number = 14 - 56.2j

#   numeric operations
import math  # import of library

res = 1 + 1 - 1 * 1 / 1 + abs(1) + pow(1, 1) + math.sqrt(1) + math.log(1) + math.cos(1)
integer_division = 3 // 2
module = 3 % 2

#   boolean
a = (True or False) and True
equals = 1 == 1
comparisons = 1 < 2 and 1 <= 1 and 1 == 1

#   string
string = "pippo"
concat = string + "2"
uppercase = string.upper()
to_int = int(132)
to_float = float(172.3)

#   Null
a = None
print(a is None)

# reading input from user
input_string = input()
