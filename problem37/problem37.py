import sys
sys.path.append("..")
import prime as p


def rTrunks(x):
    ans=set()
    while(x>0):
        ans.add(x)
        x=x/10
    return ans

def lTrunks(x,l):
    ans=set()
    while (x>0):
        ans.add(x)
        x=x%tensPow(l)
        l-=1
    return ans

def tensPow(x):
    ans=1
    for i in range(x):
        ans*=10
    return ans

print rTrunks(1234)
print lTrunks(1234,3)


pSet=p.smartPrimesUnder(1000000)
c=0
s=0
for x in pSet:
    r=rTrunks(x)
    l=len(r)
    if r.issubset(pSet) and  lTrunks(x,l-1).issubset(pSet):
        print x
        c+=1
        print c
        s+=x
        if c==15:
            break

print s
