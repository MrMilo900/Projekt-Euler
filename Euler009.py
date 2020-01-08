# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def checkifpyth(a,b,c):
    return (a ** 2 + b ** 2 == c ** 2)

def checkforabc(a,b,c):
    if a < b < c:
        return checkifpyth(a,b,c)
    elif a < b > c:
        return checkforabc(a,c,b)
    elif a > b < c:
        return checkforabc(b,a,c)
    elif a > b > c:
        return checkforabc(c,b,a)
    else:
        pass

for x in range(3,1000):
    for y in range(x,1000):
        c = (x ** 2 + y ** 2) ** 0.5
        d = c.__round__()
        if c-d == 0:
            #print(x, y, d, 'not yes 1000')
            check = checkforabc(x,y,d)
            if check == True:
                if x+y+c == 1000:
                    print(f'{x} + {y} + {d} = 1000')
                    print(f'Product is {x*y*d}')
        else:
            pass
