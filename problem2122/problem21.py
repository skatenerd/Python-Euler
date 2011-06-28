import prime

def findAmicablePairsBelow(x):
    pList = primesUnder(10000)
    rtnVal = 0
    for c in range(x):
        sumD = getPropDivisors(c, pList)
        if c==getPropDivisors(sumD, pList):
            if sumD != c:
                print c
                rtnVal += c
    print ""
    return rtnVal

print findAmicablePairsBelow(10000)
