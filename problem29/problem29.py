import sys
sys.path.append("..")
import prime as p

pList=p.primesUnder(100)


def getPFDict(x):
	rtnVal={}
	for i in range(1,x):
		rtnVal[i]=p.getFactorDict(i,pList)
	return rtnVal

PFD=getPFDict(103)

def makePowDict():
	powDict={}
	for b in range(2,101):
		print b
		for p in range(2,101):
			insertIntoPowDict(powDict, (b,p))
	return powDict

def insertIntoPowDict(powDict, pair):
	found=False
	for k in powDict.keys():
		if pairsSame(k,pair):
			#print "found"
			#print k
			#print pair
			#print ""
			powDict[k].append(pair)
			found=True
	if not found:
		#print "notFound"
		powDict[pair]=[]
		powDict[pair].append(pair)
	

def pairsSame(a,b):
	baseA=a[0]
	expA=a[1]
	baseB=b[0]
	expB=b[1]
	aDict=PFD[baseA]
	bDict=PFD[baseB]
	if (aDict.keys() == bDict.keys()):
		newA={}
		newB={}
		for x in aDict:
			newA[x]=aDict[x] * expA
		for x in bDict:
			newB[x]=bDict[x] * expB
		return newA==newB
	else:
		return False
powDict=makePowDict()
print len(powDict.keys())
#print getPFDict(100)
