# 1 - write optimized prime number generator using list to only check divisibility to smaller prime



















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

