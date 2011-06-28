import copy
def getMatrix(fname):
    f=open(fname, 'r')
    rtnVal = []
    for line in f:
        s=line
        row=s.split(' ')
        for i in range(len(row)):
            row[i]=int(row[i])
        rtnVal.append(row)
    return rtnVal

def getNextNum(nums, i):
    return i+1

def maxProdInList(nums):
    if len(nums)<4:
        return 0
    curMaxProd = 0
    maxIndex = len(nums) - 4
    i=0
    while i<=maxIndex:
        dummyProd = nums[i]*nums[i+1]*nums[i+2]*nums[i+3]
        if dummyProd > curMaxProd:
            curMaxProd=dummyProd
        if dummyProd==1788696:
            print 'good...'
        i=getNextNum(nums, i)
    return curMaxProd

def maxProdInLists(listOfLists):
    maxProd=0
    for curList in listOfLists:
        dummyProd = maxProdInList(curList)
        if dummyProd>maxProd:
            maxProd=dummyProd
    return maxProd

def getCol(index, matrix):
    rtnVal=[]
    for i in range(len(matrix)):
        rtnVal.append(matrix[i][index])
    return rtnVal

#def bottomLeftDiagonals(matrix):
#    rtnVal=[]
#    for i in range(20):
#       rtnVal.append(bottomLeftDiagonal(i,matrix))
#    return rtnVal

def bottomLeftDiagonal(i,matrix):
    rtnVal = []
    horizCnt = 0
    while i<20:
        rtnVal.append(matrix[i][horizCnt])
        i+=1
        horizCnt+=1
    return rtnVal

def printMatrix(matrix):
    for row in matrix:
        print row

def transpose(matrix):
    rtnVal=[]
    for i in range(20):
        rtnVal.append(getCol(i, matrix))
    return rtnVal


#get various matrices
matrix=[]
matrix=getMatrix('data.txt')
transMatrix=transpose(matrix)
##printMatrix(transMatrix)
##print ""
##printMatrix(matrix)
revMatrix = copy.copy(matrix)
revMatrix.reverse()
transRevMatrix = transpose(revMatrix)


##get various lists of lists (diagonal lists of lists)
negSlope=[]
for i in range(0,16):
    negSlope.append(bottomLeftDiagonal(i, matrix))
    
for i in range(0,16):
    negSlope.append(bottomLeftDiagonal(i, transMatrix))


posSlope=[]
for i in range(0,16):
    posSlope.append(bottomLeftDiagonal(i, revMatrix))
for i in range(0,16):
    posSlope.append(bottomLeftDiagonal(i, transRevMatrix))




printMatrix(negSlope)
print ""
printMatrix(posSlope)
print ""
printMatrix(matrix)
print ""
printMatrix(transMatrix)


maxHoriz = maxProdInLists(matrix)
maxVert = maxProdInLists(transMatrix)
maxNegSlope=maxProdInLists(negSlope)
maxPosSlope=maxProdInLists(posSlope)
print max(maxHoriz, maxVert, maxNegSlope, maxPosSlope)
