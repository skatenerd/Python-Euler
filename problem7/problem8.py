import prime

curPrimesList = primesUnder(20)

while len(curPrimesList) < 10001:
    curPrimesList.append(nextPrime(curPrimesList))

print curPrimesList
print len(curPrimesList)

print curPrimesList[0]
print curPrimesList[10000]
