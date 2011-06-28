def lastTenMult(a,b):
    shA = a % 10000000000
    shB = b % 10000000000
    prod = shA * shB
    return prod % 10000000000

def lastTenAdd(a,b):
    shA = a % 10000000000
    shB = b % 10000000000
    s = shA + shB
    return s % 10000000000    

def agnostNToN(n, f):
    toFold = popList(n,n)
    rtnVal = reduce(f, toFold)
    return rtnVal

def nToNFactory(f):
    rtnVal = lambda n:agnostNToN(n,f)
    return rtnVal

def popList(length, initVal):
    rtnVal = [initVal] * length
    return rtnVal


z=nToNFactory(lastTenMult)

r=range(1,1001)

#print r

s = map(z, r)

#print s

ans = reduce(lastTenAdd, s)

print ans


