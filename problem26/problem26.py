import math
import fractions as f

def divide(num, den):
	quot=[]
	curSum=0.0
	curRmndr=num
	tensPower=0
	rmndrDict={}
	while curRmndr!=0:
		tens=math.pow(10,tensPower)
		tens=int(tens)
		print tens
		tensCoeff=f.Fraction(1,tens)
		curDivisor=den * tensCoeff
		#print curDivisor
		#print curRmndr
		#print curRmndr/curDivisor
		tempQuot=int(curRmndr/curDivisor)
		quot.append(tempQuot)
		curRmndr -= tempQuot * curDivisor
		expRmndr=curRmndr * tens
		#print expRmndr
		srch=processDict(rmndrDict, expRmndr, tensPower)
		#print rmndrDict
		#print quot
		tensPower += 1
		if srch != 0:
			#print "srch!!!"
			#print srch
			return srch
	return 0



def smartDivide(num,den):
	i=0
	quot=[]
    #compare RE to r*10^i
	RE=num
	rmndrDict={}
	processDict(rmndrDict, RE, i)
	while RE != 0 and i<130:
		tempQuot=int(RE/den)
		#print tempQuot
		#print RE
		RE -= tempQuot * den
		RE *= 10
		#print RE
		#print ""
		quot.append(tempQuot)
		i+=1
		srch =  processDict(rmndrDict, RE, i)
		if srch != 0:
			return srch
	return 0


def processDict(d,x,p):
	if x in d:
		return p-d[x]
	else:
		#print "x is"
		#print x
		#print "p is"
		#print p
		#print ""
		d[x]=p
		return 0



def findRep(den):
	#initialize i
	i=0
	while tensPow(i) < den:
		i+=1

	#initialize dictionary
	fracDict={}

	#begin search
	rem = -1
	while(rem != 0):
		tens=tensPow(i)
		rem=tens % den	
		srch = processDict(fracDict, rem, i)
		i+=1
		#print i
		if srch != 0:
			#print "!!"
			#print rem
			return srch
	return 0

def tensPow(x):
	r=1
	for i in range(x):
		r *= 10
	return r





#curMax=0
#curMaxDenom=0
#for x in range(1,1001):
#	temp=divide(1,x)
#	if temp>curMax:
#		curMax=temp
#		curMaxDenom=x
#print curMaxDenom


#print ""

curMax = 0
curArgMax = 0
#for x in range(2,1000):
#	#temp=smartDivide(1,x)
#	temp = findRep(x)
#	if temp>curMax:
#		curMax = temp
#		curArgMax = x
#		print temp


for x in range(1,11):
	print findRep(x)
