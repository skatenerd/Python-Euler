import math

max=354294


def sumPowDig(x):
	sum=0
	for c in str(x):
		sum+=math.pow(float(c),5)
	return sum
ctr=0
for x in range(max):
	if sumPowDig(x)==x:
		ctr += x

print ctr
