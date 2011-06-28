def lenInt(x):
    rtnVal=1
    x/=10
    while x != 0:
        x/=10
        rtnVal+=1
    return rtnVal
#keys are numbers (indexes in the string)
#values are what is starting at the key
numPlaceDict={}
curVal=1
curKey=1
while curKey <  1000001:
    numPlaceDict[curKey]=curVal
    curKey += lenInt(curVal)
    curVal += 1
    if curKey % 10000 == 0:
        print curKey

def getPrevNumStartInd(ind):
    while ind not in numPlaceDict:
        ind -= 1
    return ind
def getDigAt(ind):
    sInd=getPrevNumStartInd(ind)
    curNum=numPlaceDict[sInd]
    curNum=str(curNum)
    diff=ind-sInd
    return curNum[diff]

s=""
for x in range(1,400):
    print getDigAt(x)

curInd=1
while curInd < 10000000:
    print curInd
    print getDigAt(curInd)
    print ""
    curInd *=10
