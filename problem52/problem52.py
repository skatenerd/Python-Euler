##fun stuff with MAP and FOLD
def arePerms(frst,sec):
    frstDict=getDictFromNum(frst)
    secDict=getDictFromNum(sec)
    return frstDict==secDict

def arePerms(args):
    args=map(getDictFromNum, args)
    #print args
    masterDict=reduce(equalsForFold,args)
    if(masterDict):
        return True
    else:
        return False

def equalsForFold(a,b):
    if a==b:
        return a
    else:
        return False


def getDictFromNum(x):
    rtnVal={}
    #print x
    while x>0:
        curNum=x % 10
        if curNum not in rtnVal.keys():
            rtnVal[curNum]=0
        rtnVal[curNum]+=1
        x/=10
    return rtnVal


oneThroughSix=range(1,7)
found=False
i=1
while found==False:
    i+=1
    toCheck=oneThroughSix[:]
    toCheck=map(lambda x: x * i, toCheck)
    #print toCheck
    if arePerms(toCheck):
        found=True
        print i
    
