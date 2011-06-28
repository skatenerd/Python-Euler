import copy
def listAdd(xOrig, yOrig):
    x=copy.copy(xOrig)
    y=copy.copy(yOrig)
    rtnVal=[]
    revRtnVal=[]
    carryInd = 0
    lenX = len(x)
    lenY = len(y)
    if lenX>lenY:
        y = prependZeros(lenX-lenY, y)
    else:
        x = prependZeros(lenY-lenX, x)
    x.reverse()
    y.reverse()
    for i in range(len(x)):
        xI=int(x[i])
        yI=int(y[i])
        s=xI+yI+carryInd
        if s>=10:
            carryInd=1
        else:
            carryInd=0
        strS = str(s)
        lastDig=int(strS[len(strS)-1])
        revRtnVal.append(lastDig)
    if carryInd:
        revRtnVal.append(1)
    revRtnVal.reverse()
    rtnVal=revRtnVal
    return rtnVal



def prependZeros(n, inpList):
    inpList.reverse()
    for i in range(n):
        inpList.append(0)
    inpList.reverse()
    return inpList

def nextFibL(pre,post):
    return listAdd(pre,post)


ctr=2


pre=[1]
post=[1]


print listAdd([1,3],[2,1])

while len(post)<1000:
	ctr+=1
	#print "setting temp to " + str(post)
	temp=post
	#print pre
	#print post
	post=listAdd(pre,post)
	#print post
	#print ""
	pre=temp
	#print "setting pre to" + str(temp)
	#print post
	#print ctr
	#print ""


print post
print ctr
