def side(r):
	return 1+2*r

def fourth(r):
	return side(r)-1

def circ(r):
	if(r==0):
		return 0
	else:	
		return 4*fourth(r)

def lowerRight(r):
	if r==0:
		return 1
	else:
		prev = lowerRight(r-1)
		c=circ(r-1)
		prev += c+2
		return prev

def upperRight(r):
	if r==0:
		return 1
	else:
		prev=upperRight(r-1)
		prev += circ(r)
		return prev

def upperLeft(r):
	if r==0:
		return 1
	else:
		prev=upperLeft(r-1)
		prev += fourth(r-1)
		prev += 3*fourth(r)
		return prev

def lowerLeft(r):
	if r==0:
		return 1
	else:
		prev=lowerLeft(r-1)
		prev += 2*fourth(r-1)
		prev += 2*fourth(r)
		return prev


if __name__ =="__main__":
	sum=1
	for x in range(1,501):
		sum+= lowerRight(x)
		sum+= upperRight(x)
		sum+= upperLeft(x)
		sum+= lowerLeft(x)
	print sum
	


