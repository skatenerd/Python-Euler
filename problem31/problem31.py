import copy as c

##class BritishSum:
##        def __init__(self, curTuple):
##                self.curTuple=curTuple
##        def add(x)



def sumAdd(x, curTuple):
        ind=getInd(x)
        l=list(curTuple)
        l[ind]=curTuple[ind]+1
        return tuple(l)

def getInd(x):
        if x==1:
                return 0
        elif x==2:
                return 1
        elif x==5:
                return 2
        elif x==10:
                return 3
        elif x==20:
                return 4
        elif x==50:
                return 5
        elif x==100:
                return 6
        elif x==200:
                return 7
        else:
                print "error"
                return -1



def numWays(x):
        wayDict={}
        wayDict[0]=set()
        wayDict[0].add((0,0,0,0,0,0,0,0))
        for i in range(1,x+1):
                print i
                updDict(i,wayDict)
        return wayDict  

def updDict(x,D):
        newSet=set()
        updSet(x-1,1,D,newSet)
        updSet(x-2,2,D,newSet)
        updSet(x-5,5,D,newSet)
        updSet(x-10,10,D,newSet)
        updSet(x-20,20,D,newSet)
        updSet(x-50,50,D,newSet)
        updSet(x-100,100,D,newSet)
        updSet(x-200,200,D,newSet)
        D[x]=newSet
        return D

def updSet(ind,toIncr,D,newSet):
        if ind in D:
                curSums=D[ind]
                for t in curSums:
                        #t is a tuple
                        newTuple=sumAdd(toIncr, t)
                        newSet.add(newTuple)

##d={0: 0, 1: 5, 2: 10, 3: 15, 4: 20}
##print d
##print dictToTuple(d)
##print dict(dictToTuple(d))
##for x in range(8):
##        print len(numWays(x)[x])
##        print numWays(x)[x]
print len(numWays(200)[200])
