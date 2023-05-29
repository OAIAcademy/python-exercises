# 1 - compute and print area of triangle taking as input base and high
# 2 - check and print if 2 integer are divisible





































# SOLUTIONS
# 1

# taking inputs
print("Base:")
b = int(input())
print("High:")
h = int(input())
area = (b * h) / 2
print(f"Area {area}")  # f string can be used to format string in place

# 2
print("Numbers")
a = int(input())
b = int(input())
is_div = a % b == 0
print(is_div)
