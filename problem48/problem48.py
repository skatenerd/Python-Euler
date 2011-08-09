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

#makes functions which map n->n^n.
#according to some notion of multiplication
def nToNFactory(multiplier):
    rtnVal=lambda n:reduce(multiplier,[n]*n)
    return rtnVal

#z is a function that maps n->n^n where
#we use lastTenMult instead of traditional multiplication
z=nToNFactory(lastTenMult)

r=range(1,1001)

#s is a list where s[i]=i^i according to last-ten-digit multiplication
s = map(z, r)

ans = reduce(lastTenAdd, s)

print ans


