##a^2+b^2=c^2
##a+b+c=n
##c=n-(a+b)
##a^2+b^2=(n-(a+b))^2
##a^2+b^2=n^2+(a+b)^2-2n(a+b)
##a^2+b^2=n^2+a^2+b^2+2ab-2n(a+b)
##0=n^2 +2ab - 2n(a+b)
##0=n^2 + 2ab -2na -2nb

#b(2a-2n)=(-n^2)+2na

#b=(2na-n^2)/(2a-2n)

##0=n^2 + 2(ab - na - nb)
##QUADRATIC IN N
##0=n^2 - (2a+2b) n + 2ab
##
##SOLUTIONS BY QUADRATIC FORMULA:
##
##TOP: 2a+2b \pm \sqrt{4(a+b)(a+b)-8ab}
##BOTTOM: 2
##
##or
##
##n=a+b \pm \sqrt{(a+b)^2 - 2ab}
##n=a+b \pm \sqrt(a^2 + b^2)
##n=a+b-c NOT AN OPTION
##n=a+b+c
##n=a+b+sqrt(a^2+b^2)




#heuristic:  a>0 and a < ???
#so start with a=1 and run through to n/2 solving for b
import math as m


def solveB(a,n):
    top=2*n*a-n*n
    bot=2*a-2*n
    if top % bot ==0:
        return top/bot
    else:
        return -1

def maxPTs(n):
    count=0
    for x in range(1,n/2):
        a=solveB(x,n)
        if a > 0:
            #print  ((x,a,n))
            count +=1
    return count

argMax=0
maxSols=0
for n in range(1000):
    a=maxPTs(n)
    if a>maxSols:
        maxSols=a
        argMax=n

print rtnVal
print argMax
