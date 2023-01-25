# 1 - write optimized prime number generator using list to only check divisibility to smaller prime
# 1 - write a program which classify number based on divisibility, creating a dict where the key is a number
#           and the value a list of number divisible by the key. Es {2:[2,4,6,8],3:[3,6,9]}


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
    print(prime)

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

