#SUMMARY:
##it seems like these problems are getting us to think about
##equivalence relations.  in this case, the equivalence class is defined by
##a collection of indices which are variable and a set of integers occupying
##numbers at the non-variable indices.  For example, [1,2,4,6],[2,4]
##defines the class [1,2,*,4,*,6].
##or maybe that is wrong.  who knows.

##OPTIMIZATION EMPLOYED:
##Suppose that I come across the number [1,2,3,4,5,6], where indices [2,4]
##are variable.  Then, i will look at the numbers of the form [1,2,*,4,*,6].
##If I later examine the number [1,2,9,4,9,6] where indices [2,4] are varaible,
##I would also be examining the class [1,2,*,4,*,6].  SO, if i were smart,
##I would recognize that the pair ([1,2,4,6],[2,4]) was already used,
##and not bother computing with it.


import sys
sys.path.append("..")
import math as m
import prime as p
import itertools as i
import time


#assume answer < 1000000
primes=p.smartPrimesUnder(1000000)
print "primes calculated.  starting cool stuff"

#(equivalence)CLASS definition:
#EXAMPLE:
#for the class [1,2,*,4,*,6], we will have
#mVarIndices=[2,4]
#and mDigitList=[1,2,-1,4,-1,6].
#mElements is everything in {1,2,*,4,*,6]
class numChangeEquivalenceClass:
    def __init__(self,seed,varIndices):
        #seed, in conjunction with varIndices, defines the class
        self.mSeed=seed
        self.mVarIndices=varIndices
        self.mDigitList=self.getDigitList(seed,varIndices)
        self.mElements=self.getElements()

    #figure out the members of [1,2,*,4,*,6]
    def getElements(self):
        rtnVal=[]
        for x in range(10):
            toAdd=self.mDigitList[:]
            for i in self.mVarIndices:
                toAdd[i]=x
            rtnVal.append(self.listToNum(toAdd))
        return rtnVal
    
    #turn a list of integers to the corresponding number
    #[1,2,3]->123
    def listToNum(self,l):
        rtnVal=0
        i=0
        while i < len(l):
            rtnVal *= 10
            rtnVal += l[i]
            i+=1
        return rtnVal

    #get a list of the static digits from the seed
    #and varIndices constructor args
    def getDigitList(self,seed,varIndices):
        rtnVal=self.getListFromNum(seed)
        for x in self.mVarIndices:
            rtnVal[x]=-1
        return rtnVal

    #turn an integer to a list of digits
    #123->[1,2,3]
    def getListFromNum(self,x):
        rtnVal=[]
        while x>0:
            curNum=x%10
            rtnVal.insert(0,curNum)
            x/=10
        return rtnVal

    #check if the current equivalence class is the winner.
    #iterate through mElements,
    #counging how many primes exist.
    def isInEightPrimeFam(self):
        count=0
        misses=0
        greaterThanSeedElts=filter(lambda(x):x>=self.mSeed,self.mElements)
        #begin counting primes
        for x in greaterThanSeedElts:
            if x in primes:
                count +=1
            else:
                misses+=1
            if misses > 2:
                #short circuit!
                break
        #check if count was adequate
        if (count<8):
            return False
        else:
            return True

    #analogous to isInEightPrimeFam, non-optimized.
    def isInSevenPrimeFam(self):
        count=0
        for x in self.mElements:
            if x in primes:
                count +=1
        if (count<7):
            return False
        else:
            return True

    #return a tuple containing the static digits and a list of
    #variable indices.  this uniquely defines the class
    def signature(self):
        staticDigits=[]
        for x in self.mDigitList:
            if x >=0:
                staticDigits.append(x)
        numRepresentingStaticDigits=self.listToNum(staticDigits)
        return (numRepresentingStaticDigits,self.mVarIndices[:])


#begin SCRIPTING

#make a dictionary where key N maps to
#proper subsets of [1,2,...N]
indicesList=[0,1,2,3,4,5,6]
properSubsetsDict={}



#get the proper subsets of a list
def getProperSubsets(l):
    length=len(l)
    rtnVal=[]
    for x in range(1,length):
        curIterator=i.combinations(l,x)
        for y in curIterator:
            rtnVal.append(y)
    return rtnVal


#properSubsetsDict maps a length "l" to all subsets of the list "range(l)"
for x in range(1,7):
    properSubsetsDict[x]=getProperSubsets(range(x))

startTime=time.clock()
#use pre existing stufff to SOLVE PROBLEM
found=False
for curPrime in primes:
    #for each prime in the prime list,
    #look for all of the potential eight-prime families
    #by swapping out subsets of its digits.
    l=m.floor(m.log(curPrime,10))+1
    subs=properSubsetsDict[l]
    for indicesToChange in subs:
        #take curPrime and indicesToChage, and generate
        #an object to represent the equivalence class
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

endTime=time.clock()
print endTime-startTime
