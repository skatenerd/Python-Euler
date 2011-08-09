import sys
sys.path.append("..")
import prime as p
import math





class PrimesGod:
    def __init__(self):
        #copy toPerm over to mData
        self.curPrimes=[]

    def uniqueFactors(x, pSet):
            uf=frozenset()
            for p in pSet:
                    if(p<x) and x%p == 0:
                            uf.add(p)
            return uf
        
    def passthru(self):
        candidate=2
        while True:
            if not p.listHasFactor(self.curPrimes, candidate):
                yield candidate
                self.curPrimes.append(candidate)
            candidate+=1
    
    def __iter__(self):
        #return self.next()
        return self.passthru()


def isPrime(t,godObj):
    return t in godObj.curPrimes

def yieldNums():
    x=0
    while True:
        yield x
        x+=1



def isProblematic(z,pGen):
    #print "entering with z="
    #print z
    rtnVal=True
    if z%2==0:
        rtnVal=False
    else:
        if len(pGen.curPrimes)==0:
            rtnVal=False
        intSqrt=int(math.sqrt(z))
        for n in range(1,intSqrt+1):
            squared=n*n
            diff=z-(2*squared)
            #print diff
            if isPrime(diff,pGen):
                rtnVal=False
                break
        #print ""
    return rtnVal


def getFirstProblematic():
    pGen=PrimesGod()
    last=2
    for x in pGen:
        composites=range(last,x)
        #print"composites"
        #print composites
        for c in composites:
            if isProblematic(c,pGen):
                return c
        last=x+1


print getFirstProblematic()
