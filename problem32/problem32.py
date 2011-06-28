allSet=set([1,2,3,4,5,6,7,8,9])
panPairSet=set()

def numSet(x):
    s=set()
    while x > 0:
        s.add(x % 10)
        x=x/10
    return s

def isPanPair(a,b):
    prod=a*b
    aSet=numSet(a)
    bSet=numSet(b)
    pSet=numSet(prod)
    totalLen=lenNum(a)+lenNum(b)+lenNum(prod)
    uSet=(aSet.union(bSet,pSet))
    return totalLen==9 and uSet==allSet

def lenNum(x):
    l=0
    while x>0:
        l+=1
        x=x/10
    return l


print isPanPair(39,186)
print isPanPair(39,188)
print isPanPair(40,186)


for x in range(9876):
    for y in range(9876):
        p=x*y
        if p>98765:
            break
        if(isPanPair(x,y)):
            panPairSet.add(x*y)
            print (x*y)
print panPairSet
print len(panPairSet)
asdf=0
for x in panPairSet:
    asdf+=x
print asdf
