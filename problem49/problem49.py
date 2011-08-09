import sys
sys.path.append("..")
import prime as p


#this is a lazy doubling prime checker
class primeChecker:

    def __init__(self,val):
        self.max=2
        self.primeSet=set([2])
        self.updtCurPrimes(val)

    #initialize primeSet variable.
    #this will be the information the checker uses to check primality
    def updtCurPrimes(self,maxVal):
        #print "doubling with" + str(self.max) + "and " +str(maxVal)
        self.primeSet=self.primeSet.union(p.smartPrimesBetween(self.max,maxVal,self.primeSet))
        self.max=max(self.primeSet)
        
    #check if the argument is prime!
    def isPrime(self,val):
        while val>self.max:
            self.doublePCollection()

        rtnVal=val in self.primeSet
        return rtnVal

    #increase collection of known primes
    def doublePCollection(self):
        self.updtCurPrimes(self.max * 2)
    

class PermutationEquivClass:
    def __init__(self, val,checker):
        if type(val) is dict:
            self.dict=val
        elif self.isNumeric(val):
            self.dict=self.getDictFromNum(val)
        self.populatePerms()
        self.populatePrimePermSet(checker)

    #turn a number into a dictionary representing
    #number of appearances of each digit.
    #for fun, we will remove keys from dictionar
    #when the value would be zero
    def getDictFromNum(self, x):
        rtnVal={}
        while x>0:
            curNum=x % 10
            if curNum not in rtnVal.keys():
                rtnVal[curNum]=0
            rtnVal[curNum]+=1
            x/=10
        return rtnVal
    
    #this should be in a library somewhere.
    #I stole it from the internet
    def isNumeric(self, val):
        try:
            dummy=val + 1
            return True
        except TypeError:
            return False

    #this object defines an equivalence class!
    #google it, fool
    def equals(self,other):
        if self.dict==other.dict:
            return True
        else:
            return False

    #figure out all the members of this equivalence class
    def populatePerms(self):
        #do a DFS style population of list
        self.permsAsLists = self.doPopulatePerms([])
        self.permsAsInts = map(self.listToNum,self.permsAsLists)

    #figure out which ones are prime    
    def populatePrimePermSet(self,checker):
        curPermSet=set()
        for x in self.permsAsInts:
            if checker.isPrime(x):
                curPermSet.add(x)
        self.primePermSet=frozenset(curPermSet)

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

    #do work to figure out permutations
    def doPopulatePerms(self,partialOutput):
        ans=[]
        for k in self.dict.keys():
            self.smartDecrementDict(k)
            partialOutput.append(k)
            if len(self.dict.keys())==0:
                toAdd=[partialOutput[:]]
            else:
                toAdd=self.doPopulatePerms(partialOutput)
            ans.extend(toAdd)
            partialOutput.pop()
            self.smartIncrementDict(k)
        
        return ans

    def smartDecrementDict(self,k):
        self.dict[k] -= 1
        if self.dict[k]==0:
            del self.dict[k]
    def smartIncrementDict(self,k):
        if k in self.dict.keys():
            self.dict[k] +=1
        else:
            self.dict[k]=1

    #check to see if this equivalence class is the winner!
    #basically look for the good arithmetic sequences
    def permsHasSolution(self):
        diffSet=set()
        try:
            #populate a set containing potential
            #imcrements in arithmetic sequence!
            for x in self.primePermSet:
                for y in self.primePermSet:
                    if x-y != 0:
                        diffSet.add(abs(x-y))
            #use this set of potential increments:
            #for each one, build an arithemtic progression
            #and see if it's teh winnar
            for x in self.primePermSet:
                for y in diffSet:
                    dummySet=set()
                    curVal=x
                    for i in range(3):
                        dummySet.add(curVal)
                        curVal += y

                    if dummySet.issubset(self.primePermSet):
                        return True
        except AttributeError:
                print "Some field (probably prime perm set) not yet defined"
                raise
        except:
                print "unexpected exception"
                raise
        return False
                

#begin SCRIPTING

def numberContainsZeroDigit(x):
    rtnVal=False
    for d in str(x):
        if int(d)==0:
            rtnVal= True
    return rtnVal



checker=primeChecker(2)
knownAnswer=PermutationEquivClass(1487,checker)
winnersSoFar=set()
answer=-1
for x in range(9871):
    foo=PermutationEquivClass(x,checker)
    if foo.permsHasSolution():
        if x not in knownAnswer.permsAsInts and not numberContainsZeroDigit(x):
            answer=foo
            break
print [z for z in answer.permsAsInts if checker.isPrime(z)]
