import prime

#initialize
curSum = 3
lastSummand = 2
curNumDivisors = 2

#functions
def nextNum(curSum, lastSummand):
    return curSum + (lastSummand + 1)


while (curNumDivisors < 500):
    curSum = nextNum(curSum, lastSummand)
    lastSummand += 1
    #print curSum
    #print str(curSum) + " " + str(lastSummand)
    curNumDivisors = prime.numDivisors(curSum)
    #print curNumDivisors
    #print ""

print curSum
print prime.numDivisors(curSum)
print prime.getFactorDict(curSum)
