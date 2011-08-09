import sys
sys.path.append("..")
import prime as p
import math



class PrimesGod:
    def __init__(self):
        #copy toPerm over to mData
        self.curPrimes=[2]
        self.domainChecked=2

    def genCounts(self):
        cur=1
        while True:
            if cur>max(self.curPrimes):
                self.doublePList(self.curPrimes)
            yield self.countUniqueFactors(cur)
            cur += 1
            
    def doublePList(self,oldPrimeList):
        m=max(oldPrimeList)
        self.domainChecked *= 2
        setToAdd=set(range(m+1, self.domainChecked))
        self.elimComposites(setToAdd, oldPrimeList)
        listToAdd=list(setToAdd)
        #listToAdd.sort()
        oldPrimeList.extend(listToAdd)
        
    def elimComposites(self,potentialComposites,primes):
        #get rid of composites using primes
        maxPotentialComposite=max(potentialComposites)
        minPotentialComposite=min(potentialComposites)
        upperBd=math.sqrt(maxPotentialComposite)
        relevantPrimes=[z for z in primes if z<=upperBd]
        for x in relevantPrimes:
            self.elimMults(potentialComposites, x)

    def elimMults(self,s,i):
        #take a set, and eliminate all elements
        #that are multiples of i
        t=i
        bd=max(s)
        while t <= bd:
            if t in s:
                    s.remove(t)
            t+=i

    def countUniqueFactors(self,x):
        factDict=p.getFactorDict(x,self.curPrimes)
        return len(factDict)



pg=PrimesGod()
debugL=[]
ctr=1
onebefore=1
twobefore=1
threebefore=1
for x in pg.genCounts():
    if onebefore>3 and twobefore>3 and threebefore>3 and x > 3:
        print ctr - 3
        break
    else:
        threebefore=twobefore
        twobefore=onebefore
        onebefore=x
    ctr += 1

