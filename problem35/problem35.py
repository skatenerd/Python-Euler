import sys
sys.path.append("..")
import prime as p

pSet=p.smartPrimesUnder(1000000)

def lenNum(x):
    l=0
    while x>0:
        l+=1
        x=x/10
    return l


def rotations(x):
    lenX=lenNum(x)
    ans=set()
    for i in range(lenX):
        ans.add(x)
        last=x % 10
        x/=10
        x+=last*tenPow(lenX-1)
    return ans

def tenPow(x):
    ans=1
    for i in range(x):
        ans*=10
    return ans

def isRotPrime(x, pSet):
    return rotations(x).issubset(pSet)


def findRotPrimes(pSet):
    ans=set()
    for x in pSet:
        r=rotations(x)
        if r.issubset(pSet):
            ans.add(frozenset(r))
    return ans


for x in range(5):
    print tenPow(x)
print rotations(12345)

print findRotPrimes(pSet)
foo=findRotPrimes(pSet)
s=0
for x in foo:
    s+=len(x)
print s
