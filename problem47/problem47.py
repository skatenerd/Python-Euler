import sys
sys.path.append("..")
import prime as p
import math



class PrimesGod:
    def __init__(self):
        #copy toPerm over to mData
        self.curPrimes=[2]
        self.domainChecked=2

    def next(self):
        ind=0
        while True:
            if ind >= len(self.curPrimes) - 1:
                self.doublePList(self.curPrimes)
            yield self.curPrimes[ind]
            ind += 1

    def genCounts(self):
        cur=1
        while True:
            if cur>max(self.curPrimes):
                self.doublePList(self.curPrimes)
            yield self.countUniqueFactors(cur)
            cur += 1
            
    def doublePList(self,oldL):
        m=max(oldL)
        self.domainChecked *= 2
        toAddS=set(range(m+1, self.domainChecked))
        #print m
        #print toAddS
        self.smartKill(toAddS, oldL)
        #print toAddS
        toAddL=list(toAddS)
        toAddL.sort()
        #print toAddL
        oldL.extend(toAddL)
        
    def smartKill(self,fodder,killers):
        maxFodder=max(fodder)
        minFodder=min(fodder)
        upperBd=maxFodder/2
        cutKillers=[z for z in killers if z<=upperBd]
        for x in cutKillers:
            self.elimMults(fodder, x)

    def elimMults(self,s,i):
        t=i
        bd=max(s)
        while t <= bd:
            if t in s:
                    s.remove(t)
            t+=i

    def countUniqueFactors(self,x):
        factDict=p.getFactorDict(x,self.curPrimes)
        return len(factDict.keys())

    
    def __iter__(self):
        #return self.next()
        return self.next()


pg=PrimesGod()
debugL=[]
ctr=1
onebefore=1
twobefore=1
threebefore=1
for x in pg.genCounts():
    #print x
    #print onebefore
    #print twobefore
    #print ""
    if onebefore>3 and twobefore>3 and threebefore>3 and x > 3:
        print ctr
        print x
        #print onebefore
        #print twobefore
        #print x
        break
    else:
        threebefore=twobefore
        twobefore=onebefore
        onebefore=x
    ctr += 1

