#SUMMARY:
##it seems like these problems are getting us to think about
##equivalence relations.  in this case, the equivalence class is defined by
##a collection of indices which are variable and a set of integers occupying
##numbers at the non-variable indices.
##or maybe that is wrong.  who knows.

##OBSERVATION:
##i don't have to do anything fancy.
##you might worry that i'm doing extra work,
##checking if a number is the winner when i already know that it isn't.
##This is wrong. Suppose you're worried that checking [1,4,*,*,2,1] is unnecessary,
##that would mean that i had checked some other class of the form,
##[A,B,*,*,C,D].  but whare are A,B,C,D other than 1,4,2,1?


import sys
sys.path.append("..")
import math as m
import prime as p
import itertools as i
#assume answer < 1000000
primes=p.smartPrimesUnder(1000000)
print "primes calculated.  starting cool stuff"

#(equivalence)CLASS definition
class numChangeEquivalenceClass:
    def __init__(self,seed,varIndices):
        self.mSeed=seed
        self.mVarIndices=varIndices
        self.mDigitList=self.getDigitList(seed,varIndices)
        self.mElements=self.getElements()
    def getElements(self):
        rtnVal=[]
        for x in range(10):
            toAdd=self.mDigitList[:]
            for i in self.mVarIndices:
                toAdd[i]=x
            rtnVal.append(self.listToNum(toAdd))
        return rtnVal
    #turn a list of integers to the number
    #[1,2,3]->123
    def listToNum(self,l):
        rtnVal=0
        i=0
        while i < len(l):
            rtnVal *= 10
            rtnVal += l[i]
            i+=1
        return rtnVal
    def getDigitList(self,seed,varIndices):
        rtnVal=self.getListFromNum(seed)
        for x in self.mVarIndices:
            rtnVal[x]=-1
        return rtnVal

    def getListFromNum(self,x):
        rtnVal=[]
        while x>0:
            curNum=x%10
            rtnVal.insert(0,curNum)
            x/=10
        return rtnVal
    def isInEightPrimeFam(self):
        count=0
        for x in self.mElements:
            if x in primes and x >= self.mSeed:
                count +=1
        if (count<8):
            return False
        else:
            return True
    def isInSevenPrimeFam(self):
        count=0
        for x in self.mElements:
            if x in primes:
                count +=1
        if (count<7):
            return False
        else:
            return True        


#begin SCRIPTING

#make a dictionary where key N maps to
#proper subsets of [1,2,...N]
indicesList=[0,1,2,3,4,5,6]
properSubsetsDict={}

def getSubsets(l):
    length=len(l)
    rtnVal=[]
    for x in range(1,length+1):
        curIter=i.combinations(l,x)
        for y in curIter:
            rtnVal.append(y)
    return rtnVal

#get the proper subsets of a list
def getProperSubsets(l):
    length=len(l)
    rtnVal=[]
    for x in range(1,length):
        curIter=i.combinations(l,x)
        for y in curIter:
            rtnVal.append(y)
    return rtnVal


#subsetsDict maps a length "l" to all subsets of the list "range(l)"
for x in range(1,7):
    properSubsetsDict[x]=getProperSubsets(range(x))


#use pre existing stufff to SOLVE PROBLEM
for curPrime in primes:
    found=False
    l=m.floor(m.log(curPrime,10))+1
    subs=properSubsetsDict[l]
    #print curPrime
    for indicesToChange in subs:
        curEQClass=numChangeEquivalenceClass(curPrime,indicesToChange)
        if curEQClass.isInEightPrimeFam():
            found=True
            print curPrime
            print indicesToChange
            for x in curEQClass.mElements:
                if x in primes:
                    print x
            break
    if found:
        break


###sanity checks:
##foo=numChangeEquivalenceClass(56003,[2,3])
##print foo.mElements
##print foo.isInSevenPrimeFam()
##bar=numChangeEquivalenceClass(123456,[1,4])
##print bar.isInSevenPrimeFam()
##fizz=numChangeEquivalenceClass(100109,[2,4])
##print fizz.isInEightPrimeFam()
