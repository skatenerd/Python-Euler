#!/usr/bin/env/python
import copy
import math
from sets import Set


def elimFactor(x,d):
    if(x % d != 0):
        return x
    else:
        return elimFactor(x/d, d)

def uniqueFactors(x, pSet):
	uf=frozenset()
	for p in pSet:
		if(p<x) and x%p == 0:
			uf.add(p)
	return uf


def yieldPrimes():
    curPrimeList=[]
    candidate=2
    while True:
        if not listHasFactor(curPrimeList, candidate):
            yield candidate
            curPrimeList.append(candidate)
        candidate+=1



def smallestDivisor(x):
    i=2
    while ((x%i) != 0):
        i = i+1
    return i


def smallestDivisor2(x,s):
    i=s
    while ((x%i) != 0):
        i = i+1
    return i
    

def listHasDivisor(tries, number):
    for x in tries:
        if number % x == 0:
            return x
    return 0

def listHasFactor(tries,number):
    root=math.sqrt(number)
    for x in tries:
        if number % x == 0:
            return x
        if x>root:
            return 0
    return 0
        
    
def nextPrime(curPrimesList):
    last = curPrimesList[-1]
    i=last + 1
    while listHasFactor(curPrimesList, i):
        i= i+1
    return i

def primesUnder(x):
    curList=[2,3,5,7,11]
    while curList[-1] < x:
        curList.append(nextPrime(curList))
    curList.pop()
    return curList

def findLargestFactor(x):
    lastDivisor=x
    while(x!=1):
        lastDivisor = smallestDivisor(x)
        x = elimFactor(x, lastDivisor)
    return lastDivisor

def numTimesDivides(x,d):
    dExp=0
    while x%d == 0:
        x=x/d
        dExp = dExp + 1
    return dExp
    
##def getFactorDict(x):
##    factorDict={}
##    curDivisor=2
##    while (x!=1):
##        curDivisor = smallestDivisor2(x,curDivisor)
##        maxPow = numTimesDivides(x,curDivisor)
##        factorDict[curDivisor]=maxPow
####        print curDivisor
####        print maxPow
##        x=x/(math.pow(curDivisor, maxPow))
##    return factorDict


def getFactorDict(x,L):
    sqrt = math.sqrt(x)
    factorDict = {}
    for d in L:
        if d > sqrt:
            if x>1:
                factorDict[int(x)]=1
            return factorDict
        else:
            if x % d == 0:
                maxPow = numTimesDivides(x, d)
                factorDict[d] = maxPow
                x = x/(math.pow(d,maxPow))
    return factorDict

#def getSetP(p,x):
    


def getPropDivisors(x, pList):
    rtnVal=0
    factorDict = getFactorDict(x,pList)
    if factorDict=={}:
        return 0
    expL=[]
    for l in factorDict:
        expL.append(range(factorDict[l]+1))
    cartProd = getCP(expL)
    sumDict={}
    keys=factorDict.keys()
    for i in range(len(cartProd)):
        toAdd = 1
        curL=cartProd[i]
        for j in range(len(factorDict)):
            sumDict[keys[j]]=curL[j]
        for k in sumDict:
            toAdd *= math.pow(k, sumDict[k])
        rtnVal += toAdd
    rtnVal -= x
    return int(rtnVal)


    

def numDivisors(x):
    prod = 1
    if(x%2!=0):
        factorDict = getFactorDict(x)
        for key in factorDict:
            prod = prod * (factorDict[key]+1)
    return prod


def getRevCP(L, curArr):
    rtnVal = []
    if L==[]:
        print "emptylist"
        return []
    if len(L)==1:
        curL=L[0]
        for x in curL:
            curArr.append(x)
            rtnVal.append(copy.copy(curArr))
            curArr.pop()
        return rtnVal
    else:
        lCpy = copy.copy(L)
        curL = lCpy.pop()
        for x in curL:
            curArr.append(x)
            toAppend = getRevCP(lCpy, curArr)
            for l in toAppend:
                rtnVal.append(l)
            curArr.pop()
        return rtnVal

def getCP(L):
    if L==[]:
        return []
    revCP = getRevCP(L, [])
    for l in revCP:
        l.reverse()
    return revCP

def isPerfect(x, L):
    return getPropDivisors(x,L)==x

def isAbundant(x, L):
    return getPropDivisors(x,L)>x

def isDeficient(x, L):
    return getPropDivisors(x,L)<x

def getAbundList(lim):
    L=primesUnder(lim)
    abundList=[]
    for x in range(lim):
        if isAbundant(x,L):
            abundList.append(x)    
    print len(abundList)
    return abundList

def getAbundDict(lim):
    L=primesUnder(lim)
    abundList={}
    for x in range(lim):
        if isAbundant(x,L):
            abundList[x]=1
        else:
            abundList[x]=0
    print len(abundList)
    return abundList



def canWriteAsSum2(x,L):
    for t in L:
        if t<x and (x-t) in L:
            print "t is " + str(t)
            print "diff is " + str(x-t)
            return 1
        if t>((x/2)+1):
            return 0





def smartPrimesUnder(x):
	#f = open('plist.txt','w')
	r=range(2,x)
	sr=set(r)
	ans=set()
	for i in r:
		#print i
		if i in sr:
			#f.write(str(i))
			#f.write("\n")
			ans.add(i)
			elimMults(sr,i,x)
	#f.close
	return ans

def smartPrimesBetween(a,b):



def elimMults(s,i,x):
	t=i
	while t <= x:
		if t in s:
			s.remove(t)
		t+=i



if __name__ == "__main__":
    pGen=p.yieldPrimes()

    for x in pGen:
        print x
        if x>20204:
            break
