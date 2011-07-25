##PROBLEM 53:
##How many (non distinct) values of (N,R) are there for N<=100?


##observation: (n choose r) = (n choose (n-r))
##another observation: putting (n choose (r+1)) in terms of (n choose r)
##you will see that it increases until r=n/2.
##this script uses both observations.

import math as m



def choose(a,b):
    #implement choose function
    numerator=m.factorial(a)
    denominator=m.factorial(b) * m.factorial(a-b)
    return numerator/denominator



ans=0

#iterate over i and then j, evaluating (i,j).
#curContribution at value i represents the number of non-distinct values
#(i,j) where (i,j) >=1000000.

for i in range(101):
    j=0
    #curContribution starts out as all of the values in [0,i]
    cur_contribution=i+1
    while j<=(i/2) and choose(i,j)<=1000000:
        #each time we find that (i,j)<=1000000,
        #we eliminate (j) and (n-j)
        j+=1
        cur_contribution -=2
    if cur_contribution > 0:
        ans += cur_contribution

    
print "answer is: " + str(ans)
