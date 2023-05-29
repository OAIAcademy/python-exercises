# 1 - write optimized prime number generator using list to only check divisibility to smaller prime
# 2 - write a program which classify number based on divisibility, creating a dict where the key is a number
#           and the value a list of number divisible by the key. Es {2:[2,4,6,8],3:[3,6,9]}
# 3 -  for the list [11, 42, 8, 11, 23, 42, 23, 11, 89] count occurrences in a dict
# 4 - using the same list create a list of tuple containing the values at opposite indexes
#           (es the second is going to be (42,11))























# SOLUTION
# 1
primes = []
for i in range(2, 1000):
    flag = True
    for smaller_prime in primes:
        if i % smaller_prime == 0:
            flag = False
            break
    if flag:
        primes.append(i)

for prime in primes:
    print(primes)

# 2
ris = {}
for i in range(2, 1000):
    for j in range(1, i + 1):
        if i % j == 0:
            if j not in ris:  # check if key is in dict, if not add it and init it with an empty list
                ris[j] = []
            ris[j].append(i)
print(ris)

# 3
ris = {}
for i in [11, 42, 8, 11, 23, 42, 23, 11, 89]:
    if i not in ris:
        ris[i] = 0
    ris[i] += 1
print(ris)

# 4
ris = []
l = [11, 42, 8, 11, 23, 42, 23, 11, 89]
for i in range(0, len(l)):
    ris.append((l[i], l[-i - 1]))  # index 0 goes to -1, 1 to -2 ecc...
print(ris)
