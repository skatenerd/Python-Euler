def charInt(c):
    return ord(c)-96

def wrdScore(w):
    s=0
    w=w.lower()

    w=w.replace('"','')

    for c in w:
        s+=charInt(c)
    return s

def triangleNums():
    n=0
    while True:
        n+=1
        yield (n*(n+1))/2

def isTriangleNum(n):
    for x in triangleNums():
        if x==n:
            return True
        elif x>n:
            return False
print isTriangleNum(55)
print isTriangleNum(56)
c=0
f=open("words.txt", 'r')
for x in f:
    s=x

s=s.split(",")
for x in s:
    
    if isTriangleNum(wrdScore(x)):
        c+=1
        print x



f.close()
