##1: (1,1,1,1,1,1,1,1,1), (1,1,1,1,1,1,1,2),(1,1,1,1,1,2,2),(1,1,1,2,2,2),(1,2,2,2,2)
##X:   1                     NONE               NONE           3             5,6,7,8,9
##
##
##
##2: (2,2,2,3)
##     25-99          
##
##3: (3,3,3)
##     100-333
##
##4: (4,5)
##     5000-9999
##


allSet=set([1,2,3,4,5,6,7,8,9])
def numSet(x):
    s=set()
    while x > 0:
        s.add(x % 10)
        x=x/10
    return s

def isPandigital(x):
    s=numSet(x)
    return len(s)==9 and s ==allSet

def concProd(x,n):
    s=0
    for i in range(1,n+1):
        #print s
        s=concat(s,x*i)
    return s

def concat(s,r):
    s*=tensPow(lenInt(r))
    s+=r
    return s

def lenInt(x):
    rtnVal=1
    x/=10
    while x != 0:
        x/=10
        rtnVal+=1
    return rtnVal

def tensPow(x):
    ans=1
    for i in range(x):
        ans*=10
    return ans

def finalLenConcProd(x,n):
    s=0
    for i in range(1,n+1):
        s+=lenProd(x,i)
    return s

def lenProd(a,b):
    return lenInt(a*b)


a = concProd(192,3)
print a
print concProd(9,5)
print finalLenConcProd(192,3)
print isPandigital(a)


max = 0
mp=(1,2)
if isPandigital(concProd(3,6)):
    max=concProd(3,6)

for x in range(5,10):
    a=concProd(x,5)
    if isPandigital(a) and a > max:
        mp=(x,5)
        max = a

for x in range(25,100):
    a=concProd(x,4)
    if isPandigital(a) and a > max:
        mp=(x,4)
        max=a
        
for x in range(100,334):
    a=concProd(x,3)
    if isPandigital(a) and a > max:
        mp=(x,3)
        max=a

for x in range(5000,10000):
    a=concProd(x,2)
    if isPandigital(a) and a > max:
        mp=(x,2)
        max=a
print max
print mp
