# Sieve_of_Eratosthenes

import math

n = 2000000
primes = []
for x in range(2, n+1):
    primes.append(x)

i = 2

while (i<=int(math.sqrt(n))):
    # print(i)
    if i in primes:
        for j in range(i*2, n+1, i):
            if j in primes:
                print(j)
                primes.remove(j)
    i = i + 1

print(sum(primes))
