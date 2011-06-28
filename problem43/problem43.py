class Perm:
    def __init__(self, toPerm):
        #copy toPerm over to mData
        self.mData=toPerm[:]

    def passthru(self, soFar):
        if len(soFar)<len(self.mData):
            relevant=[z for z in self.mData if z not in soFar]
            for r in relevant:
                temp=soFar[:]
                temp.append(r)
                for x in self.passthru(temp):
                    yield x
        else:
            yield soFar[:]


    def __iter__(self):
        #return self.next()
        return self.passthru([])

    def next(self):
        for x in self.passthru([]):
            yield x

def consecPerms(x):
    l=range(x+1)
    pIterator=Perm(l)
    return pIterator


def lToInt(intList):
    s=0
    tensPow=len(intList)-1
    factor=math.pow(10,tensPow)
    for x in intList:
        s+=x*factor
        factor /= 10
    return int(s)

def hasProp(x):
    rtnVal=True
    inted=lToInt(x)
    stringified=str(inted)
    for i in range(1,8):
        
        substr=stringified[i:i+3]
        if int(substr) % pList[i-1] != 0:
            rtnVal=False
            return rtnVal
    return rtnVal
        

pList=[2,3,5,7,11,13,17]


balls = consecPerms(9)
s=0
for x in balls:
    if x==[1,4,0,6,3,5,7,2,8,9]:
        print x
    if hasProp(x):
        toAdd=lToInt(x)
        s+=toAdd
        print toAdd
print s
