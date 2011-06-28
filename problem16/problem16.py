def strAdd(x,y):
    rtnVal=""
    revRtnVal=""
    carryInd = 0
    lenX = len(x)
    lenY = len(y)
    if lenX>lenY:
        y = prependZeros(lenX-lenY, y)
    else:
        x = prependZeros(lenY-lenX, x)
    x=x[::-1]
    y=y[::-1]
    for i in range(len(x)):
        xI=int(x[i])
        yI=int(y[i])
        s=xI+yI+carryInd
        if s>=10:
            carryInd=1
        else:
            carryInd=0
        strS = str(s)
        lastChar=strS[len(strS)-1]
        revRtnVal += lastChar
    if carryInd:
        revRtnVal += "1"
    rtnVal = revRtnVal[::-1]
    return rtnVal

def prependZeros(n, inpStr):
    for i in range(n):
        inpStr="0"+inpStr
    return inpStr

def exp2(n):
    s="1"
    for i in range(n):
       s=strAdd(s,s)
    return s

def sumDigStr(s):
    curSum=0
    for c in s:
        curSum += int(c)
    print curSum
    return curSum

twoToThousand = exp2(1000)
sumDigStr(twoToThousand)
