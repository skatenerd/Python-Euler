import sys
sys.path.append("..")
import prime as p
print "getting list"
pSet=p.smartPrimesUnder(4000000)
print "list done"

def findConsPrimes(a,b, pList):
#find how many consecutive primes starting with n=0
#produced by n^2+an+b
	i=0
	curOutput = getOutput(a,b,i)
	while curOutput in pList:
		i+=1
		curOutput = getOutput(a,b,i)
	return i

def getOutput(a,b,n):
	return (n*n)+(a*n)+b

def maxConsPrimes(pSet):
	curMax = 0
	for a in range(-999,1000):
		for b in range(-999,1000):
			temp = findConsPrimes(a,b,pSet)
			if temp > curMax:
				curMax = temp
				curArgMax = a*b
				print curArgMax
				print curMax
	return curMax

print findConsPrimes(-79,1601,pSet)
print maxConsPrimes(pSet)
