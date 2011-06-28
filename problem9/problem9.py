def isPythagTrip(a,b,c):
    return a*a + b*b == c*c

def checkForPythagTrip(a, total):
    s=total-a    
    b=s-1
    c=s-b
    while b>=1:
#        print "a="+str(a)
#        print "b="+str(b)
#        print "c="+str(c)
        if (isPythagTrip(a,b,c)):
            print a
            print b
            print c
            return 1
        b=b-1
        c=s-b
    return 0


a=998

while a>0:
    if(checkForPythagTrip(a,1000)):
        break
    a=a-1
