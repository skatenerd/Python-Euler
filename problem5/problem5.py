import prime

primesUnder20 = prime.primesUnder(20)
print primesUnder20

primeMap = {}

for curPrime in primesUnder20:
    primeMap[curPrime]=0


for x in range(1,20):
    for p in primesUnder20:
        if numTimesDivides(x,p)>primeMap[p]:
            primeMap[p]= numTimesDivides(x,p)
#        print primeMap

print primeMap
product = 1
for x in primeMap:
    product = product * math.pow(x,primeMap[x])
    print 'x is ' + str(x)
    print 'pmat at x is ' + str(primeMap[x])
    print 'pow is ' + str(math.pow(x,primeMap[x]))

print product
