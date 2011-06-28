import math as m

def isSumFacDig(x):
    s=0
    for d in str(x):
        s+=m.factorial(int(d))
    return s==x
def numList(x):
    s=[]
    while x > 0:
        s.append(x % 10)
        x=x/10
    return s


for x in range(2540161):
    if isSumFacDig(x):
        print x
