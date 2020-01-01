#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
from typing import List


#
#  ZA DUŻO OBLICZEN NA TAK WIELKA LICZBE JAK 600851475143 ALE POWIINO DZIALAC
#

number = 13195

factorlist = []
primes = []
for num in range(1,number):
    if number % num == 0:
        factorlist.append(num)
        #print(num)

for num in factorlist:
    prime = True
    for x in range(2,num):
        if num % x == 0:
            prime = False
    if prime == True:
       #print(num)
        primes.append(num)

#print(factorlist)
print(max(primes))