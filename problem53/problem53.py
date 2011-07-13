##observation: (n choose r) = (n choose (n-r))
##another observation: putting (n choose (r+1)) in terms of (n choose r)
##you will see that it increases until r=n/2.
##this script uses both observations.

import math as m

def choose(a,b):
    numerator=m.factorial(a)
    denominator=m.factorial(b) * m.factorial(a-b)
    return numerator/denominator



ans=0
for i in range(101):
    j=0
    curContribution=i+1
    while j<=(i/2) and choose(i,j)<=1000000:
        j+=1
        curContribution -=2
    if curContribution > 0:
        print i
        print j
        print curContribution
        print ""
        ans += curContribution

    
    
