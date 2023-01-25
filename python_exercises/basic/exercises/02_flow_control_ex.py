# 1 - print number 1 to 10
# 2 - print odd number to 1000
# 3 - print multiplication matrix 10*10 (search docs to see how to use print)
# 4 - check if input number is prime
# 5 - print prime numbers < 1000






































# Solutions
# 1
import math

print("EX 1")
for i in range(0, 10):
    print(i)
# 2
print("EX 2")
for i in range(0, 1000):
    if i % 2 != 0:
        print(i)
# 3
print("EX 3")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j} ", end='')
    print("\n")
# 4
print("EX 4")
print("Number:")
x = int(input())
flag_primo = True
for i in range(2, int(math.sqrt(x))):  # it is sufficient to check till sqrt(x)
    if x % i == 0:  # check divisibility
        flag_primo = False
        break  # if divisibility found exit immediately
if flag_primo and x >= 2:
    print(f"{x} is prime")
else:
    print(f"{x} is not prime")
# 5
print("EX 5")
for x in range(2, 1000):
    flag_primo = True
    for i in range(2, int(math.sqrt(x))):  # it is sufficient to check till sqrt(x)
        if x % i == 0:  # check divisibility
            flag_primo = False
            break  # if divisibility found exit immediately
    if flag_primo:
        print(x)
