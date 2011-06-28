import copy

def minGreaterThan(L,x):
    #print "x is " + str(x)
    #print "L is " + str(L)
    curMin=max(L)
    for i in L:
        if i<curMin and i>x:
            curMin = i
    if curMin > x:
        return curMin
    else:
        print "all smaller than x"
        return (-1)

def listSwap(L, ind1, ind2):
    temp=L[ind1]
    L[ind1]=L[ind2]
    L[ind2]=temp

def indexOfFirstDecrease(L):
    for x in range(1,len(L)):
        tempL=L[0:x]
        if L[x]<max(tempL):
            return x
    return (-1)

def sortDownFirstSeg(L,i):
    toSort=L[:i]
    #print "L is " + str(L)
    #print "i is" + str(i)
    #print "tosort is " + str(toSort)
    toSort.reverse()
    toSort.sort()
    toSort.reverse()
    #print "after sorting " + str(toSort)
    L[:i]=toSort
    return L

#takes the reverse of a permutation,
#finds the next permutation in lex order
#and reverses it
def nextPerm(L):
    cpy=copy.copy(L)
    bdryInd = indexOfFirstDecrease(cpy)
    leftSwap = cpy.index(minGreaterThan(cpy[:bdryInd], cpy[bdryInd]))
    listSwap(cpy,bdryInd,leftSwap)
    cpy=sortDownFirstSeg(cpy,bdryInd)
    return cpy
    

seed = [0,1,2,3,4,5,6,7,8,9]
print seed
seed.reverse()
for x in range(999999):
    seed=nextPerm(seed)
##    seed.reverse()
##    print seed
##    seed.reverse()


seed.reverse()
print seed
