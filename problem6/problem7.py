sumOfSquares = 0
squareOfSums = 0
rawSum = 0

for i in range(0,101):
    sumOfSquares += (i*i)
    rawSum += i

squareOfSums = rawSum*rawSum

print rawSum

print squareOfSums - sumOfSquares
