#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


for x in range(200000000,300000000,20):
    for y in range(2,21):
        check = False
        if x % y != 0:
            count = 1
            break
        check = True
    if check:
        print(x)

