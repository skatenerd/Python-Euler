import prime

f = open('2million.txt','w')

primesList = prime.primesUnder(2000000)
for x in primesList:
    f.write(str(x))
    f.write('\n')
print 'doneWithPrimes'
ans = sum(primesList)
print ans

f.close()
