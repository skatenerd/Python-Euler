def scoreName(n):
	s=0
	n=n.lower()
	for c in n:
		s+=scoreChar(c)
	return s

def scoreChar(c):
	num=ord(c)-96
	if num>0 and num<27:
		return num
	else:
		return 0

f = open('names.txt', 'r')
inputList=[]
for x in f:
    inputList.append(x)
nameStr=inputList[0]
nameList=nameStr.split(',')
nameList.sort()
print nameList
f.close()
print scoreName("colin")
print nameList[937]
print scoreName(nameList[937])
s=0
ind=1
for x in nameList:
	pre=scoreName(x)
	post=ind * pre
	s+=post
	ind+=1
print s
