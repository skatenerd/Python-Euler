def getStrings(fname):
    f=open(fname, 'r')
    rtnVal = []
    for line in f:
        s=line
        rtnVal.append(s)
    return rtnVal



def getFirstFourteen(longStr):
    shortened=longStr[0:14]
    shortened=int(shortened)
#    print shortened
    return shortened



strList = getStrings("numList.txt")


print strList
print ""

for i in range(len(strList)):
    strList[i]=getFirstFourteen(strList[i])
print strList


total= sum(strList)
total=str(total)
print total
total=total[0:14]
print total
