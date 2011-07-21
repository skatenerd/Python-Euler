##fun stuff with MAP and FOLD


#takes two integers.
#returns TRUE if the digits
#in frst are a permutation of the digits in sec
def arePerms(frst,sec):
    frstDict=getDictFromNum(frst)
    secDict=getDictFromNum(sec)
    return frstDict==secDict

#takes a list of integers.
#returns TRUE if all of the integers'
#digits are permutations of each other
def arePerms(numbers):
    digitsDictList=map(getDictFromNum, numbers)
    #print args
    masterDict=reduce(equalsForFold,digitsDictList)
    if(masterDict):
        return True
    else:
        return False

def equalsForFold(a,b):
    if a==b:
        return a
    else:
        return False


#takes an integer.
#returns a dictionary mapping
#a digit to the number of times that digit appears
#note: I could use something like,
#for d in str(x): ...,
#but i figured this is probably faster?
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
    toCheck=oneThroughSix
    toCheck=map(lambda x: x * i, toCheck)
    #print toCheck
    if arePerms(toCheck):
        found=True
        print i
    
