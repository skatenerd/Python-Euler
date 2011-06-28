import sys
sys.path.append("..")
import prime as p
import math
#digSet=set([1,2,3,4,5,6,7,8,9])
#digList=[1,2,3,4,5,6,7,8,9]

relevantPrimes=p.smartPrimesUnder(31427)
relevantPrimes=list(relevantPrimes)
relevantPrimes.sort()

##def getNextNPand(curPands):
##    rtnVal=[]
##    curLen=
##    for n in curPands:
##        news=buildOn(n)
##        rtnVal.extend(news)
##    return rtnVal
##
##def buildOn(n,x):
##    toAdd=len(
##    n*=10
##    rtnVal=[]
##    nums=numSet(n)
##    toAdd=digSet - nums
##    for x in toAdd:
##        cur = n+x
##        rtnVal.append(cur)
##    return rtnVal
##
##def numSet(x):
##    s=set()
##    while x > 0:
##        s.add(x % 10)
##        x=x/10
##    return s
##
##def newPandList(oldPandList, x):
##    for oldP in oldPandList:
##        
##
##curPands = digList
##tmp=curPands
##for x in range(8):
##    tmp=getNextNPand(tmp)
##    curPands.extend(tmp)
##
##curPands.sort(reverse=True)

##class Perm:
##    def __init__(self, toPerm):
##        #copy toPerm over to mData
##        self.mData=toPerm[:]
##        #state to represent current truncated permutation
##        self.mSoFar=[]
##    def __iter__(self):
##        return self.next()
##    def next(self):
##        if len(self.mSoFar)<len(self.mData):
##            relevant=[z for z in self.mData if z not in self.mSoFar]
##            for r in relevant:
##                self.mSoFar.append(r)
##                for x in self.next():
##                    yield x
##                self.mSoFar.pop()
##        else:
##            yield self.mSoFar
        
class Perm:
    def __init__(self, toPerm):
        #copy toPerm over to mData
        self.mData=toPerm[:]

    def passthru(self, soFar):
        if len(soFar)<len(self.mData):
            relevant=[z for z in self.mData if z not in soFar]
            for r in relevant:
                temp=soFar[:]
                temp.append(r)
                for x in self.passthru(temp):
                    yield x
        else:
            yield soFar[:]


    def __iter__(self):
        #return self.next()
        return self.passthru([])

    def next(self):
        for x in self.passthru([]):
            yield x


def addPerms(soFar, toPerm, rtnVals):
    if len(soFar)<len(toPerm):
        relevant=[z for z in toPerm if z not in soFar]
        for r in relevant:
            temp=soFar[:]
            temp.append(r)
            addPerms(temp, toPerm, rtnVals)
    else:
        rtnVals.append(soFar)

def addPermsY(soFar, toPerm):
    if len(soFar)<len(toPerm):
        relevant=[z for z in toPerm if z not in soFar]
        for r in relevant:
            temp=soFar[:]
            temp.append(r)
            for x in addPermsY(temp, toPerm):
                yield x
    else:
        yield soFar[:]

def consecPerms(x):
    l=range(1,x+1)
    pIterator=Perm(l)
    return pIterator

def lToInt(intList):
    s=0
    tensPow=len(intList)-1
    factor=math.pow(10,tensPow)
    for x in intList:
        s+=x*factor
        factor /= 10
    return int(s)



r=range(1,10)
r.sort(reverse=1)
for x in r:
    print x
    curL=consecPerms(x)
    for y in curL:
        intified=lToInt(y)
        if not p.listHasFactor(relevantPrimes, intified):
            print y
##        else:
##            print p.listHasFactor(relevantPrimes, x)
##            print x
##            print ""
