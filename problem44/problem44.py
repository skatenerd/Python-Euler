import math as m

def getTriNums():
    curNum=0
    curDiff=1
    while True:
        curNum += curDiff
        curDiff += 3
        yield curNum

def isTri(x):
    #2x=3n^2-n
    rtnVal=False
    x=24*x + 1
    if isSqr(x):
        x=int(m.sqrt(x))
        x+=1
        if x%6==0:
            rtnVal=True
    return rtnVal

def isSqr(x):
    t=m.sqrt(x)
    t=int(t)
    return t*t==x



getter=getTriNums()
curTris=[]
smallestDiff=-1
hasFound=False
l=0
d=0
while hasFound==False or d<smallestDiff:
    justAdded=getter.next()
    curTris.append(justAdded)
    l+=1
    if l>2:
        d=curTris[l-1]-curTris[l-2]
    #print d
    toIter= curTris[:-1]
    toIter.sort(reverse=True)
    for t in toIter:
        curD=justAdded-t
        curS=justAdded+t
        if isTri(curD) and isTri(curS):
            if hasFound==False:
                smallestDiff=curD
                hasFound=True
                print (justAdded, t)
                print curD
                break
            elif curD<smallestDiff:
                hasFound=True
                smallestDiff=curD
                print (justAdded, t)
                break
            else:
                print fail
                print curD
