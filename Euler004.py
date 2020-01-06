#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

mylistx = []

for x in range(100,1000):
    mylistx.append(x)

mylistx = mylistx[::-1]
palilist = []
def check():
    for index1 in range(0,len(mylistx)):
        for index2 in range(0,len(mylistx)):
            pali = str(mylistx[index1] * mylistx[index2])
            if pali == pali[::-1]:
                palilist.append(int(pali))
    return palilist

result = check()

print(max(result))