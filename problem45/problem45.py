import math as m

def getHexNums():
    curNum=0
    curDiff=1
    while True:
        curNum += curDiff
        curDiff += 4
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

def isPent(x):
    #x=2n^2-n
    rtnVal = False
    x = 24*x + 1
    if isSqr(x):
        x=int(m.sqrt(x))
        x+=1
        if x % 6 == 0:
            rtnVal= True
    return rtnVal

def isSqr(x):
    t=m.sqrt(x)
    t=int(t)
    return t*t==x



for x in getHexNums():
    if isPent(x):
        if isTri(x):
            print x
            if x>40755:
                break
