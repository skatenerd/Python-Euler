file = open('number.txt', 'r')
length = 1001
counter=0
intList=[]
while 1:
    char = file.read(1)          # read by character
    counter = counter+1
    if not char: break
    if counter < length:
        intList.append(int(char))

file.close()

length = len(intList)
curMaxSum=0
curDummySum=0
i=0
while i<length-4:
    curDummySum=intList[i]*intList[i+1]*intList[i+2]*intList[i+3]*intList[i+4]
    if(curDummySum>curMaxSum):
        curMaxSum=curDummySum
        print "??"
    i=i+1

print curMaxSum
