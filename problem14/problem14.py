def nextInSeq(x):
    if x%2==0:
        return x/2
    else:
        return (3*x + 1)

def afterNTurns(n, seed):
    rtnVal = []
    rtnVal.append(seed)
    for x in range(n-1):
        seed=nextInSeq(seed)
        rtnVal.append(seed)
        if seed==1:
            return rtnVal
    return rtnVal

##def firstShared(first, second):
##    for x in first:
##        if x in second:
##            return x
##    return 0
##
##
##
##seeds=range(2,1000)
##def kill(x,seeds):
##    for y in seeds:
##        if x<y:
##            xStr = afterNTurns(5, x)
##            yStr = afterNTurns(5, y)
##            intersection = firstShared(xStr,yStr)
##            if intersection != 0:
##                if xStr.index(intersection) < yStr.index(intersection):
##                    seeds.remove(x)
##                    return seeds
##                else:
##                    seeds.remove(y)
##    return seeds



def getLen(x, lenDict):
    xCtr=1
    c=x
    while c!=1:
        if c in lenDict:
            lenDict[x]=xCtr + lenDict[c] - 1
            return lenDict
        c=nextInSeq(c)
        xCtr += 1
    lenDict[x]=xCtr
    return lenDict

seeds = range(500000, 1000000)
curDict = {}
curMax=0
for x in seeds:
    #print x
    curDict = getLen(x, curDict)
    if curDict[x]>curMax:
        curMax = curDict[x]
        if curMax == 525:
            print x
print curMax
