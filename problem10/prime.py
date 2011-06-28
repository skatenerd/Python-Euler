#!/usr/bin/env/python
import math

def elimFactor(x,d):
    if(x % d != 0):
        return x
    else:
        return elimFactor(x/d, d)

def smallestDivisor(x):
    i=2
    while ((x%i) != 0):
        i = i+1
    return i

def listHasDivisor(tries, number):
    for x in tries:
        if number % x == 0:
            return 1
    return 0

def listHasFactor(tries,number):
    root=math.sqrt(number)
    for x in tries:
        if number % x == 0:
            return 1
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
    expD = 1
    dExp=0
    while x%expD == 0:
        expD = expD*d
        dExp = dExp + 1
    return dExp - 1
    


if __name__ == "__main__":
    print primesUnder(10000)
