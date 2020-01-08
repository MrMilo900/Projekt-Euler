# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

primes = [2]

for x in range(3,2000001,2):
    prime = True
    for y in range(2,x):
        if x % y == 0:
            prime = False
            break
    if prime == True:
        primes.append(x)

print(sum(primes))