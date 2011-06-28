def listAdd(x,y):
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


def listMult(x,y):
    lenX = len(x)
    lenY = len(y)
    if lenX>lenY:
        top = x
        bottom = y
    else:
        top = y
        bottom = x
    top.reverse()
    bottom.reverse()
    total = [0]
    for i in range(len(bottom)):
        for j in range(len(top)):
            summand = int(bottom[i])*int(top[j])
            summand = list(str(summand))
##            print bottom[i]
##            print top[j]
##            print summand
##            print ""
            summand=appendZeros(j,summand)
            summand=appendZeros(i,summand)
            total = listAdd(total, summand)
    return total
        
        
        


def appendZeros(n, inpList):
    for x in range(n):
        inpList.append(0)
    return inpList


def prependZeros(n, inpList):
    inpList.reverse()
    for i in range(n):
        inpList.append(0)
    inpList.reverse()
    return inpList

def factorial(x):
    prod = [1]
    while x>1:
        prod = listMult(prod,list(str(x)))
        x-=1
    return prod

def sumDigStr(s):
    curSum=0
    for c in s:
        curSum += int(c)
    print curSum
    return curSum




first=834
firstL=list(str(first))
second=722
secondL = list(str(second))

fac = factorial(100)
print sumDigStr(fac)
