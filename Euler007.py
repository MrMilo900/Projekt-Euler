# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

primes = [2]
for x in range(3,105000,2):
    prime = True
    for y in range(2,x):
        if x % y == 0:
            prime = False
            break
    if prime == True:
        primes.append(x)

print(len(primes))
print('10001st Prime nubmer ',primes[10000])
