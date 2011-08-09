5##The task here is to take a prime number,P, and determine
##the maximum number of consecutive primes which sum to P.
##41=[2+3+5+7+11+13].

##The relevant observation is that the FIRST string of consecutive primes
##summing to P will be the winner, since any later string will be composed
##of larger numbers!

##The heuristic for finding this first string is as follows:
##take the longest list of consecutive primes summing to less than P.
##L=[2,3,5,7...73].
##Now, until L has length 0, we will do the following process:
##1:  append the next prime to L,
##2:  remove a bunch of primes from the beginning of L until sum(L)<=P
##3:  if sum(L)=P: win,
##     else: repeat


import sys
sys.path.append("..")
import prime as p

primesUnderMil=list(p.smartPrimesUnder(1000000))
primesUnderMil.sort()
print "has finished computing primes under million.  now doing cool work"



def getMaxConsecutiveSummands(sortedSummands,
                              x,
                              sumOfFirstNSummands,
                              curMaxConsecPrimes):
    #This function calculats the maximum number consecutive summands
    #in sortedSummands, which sum to x.
    #Arg sumOfFirstNSummands is a tuple representing the sum of some consecutive
    #summands summing to less than "x"
    #Arg curMaxConsecPrimes represents the current "best" answer to the problem.

    
    curStartIdx=0
    
    #tack on as many possible primes to the end
    #so that we have the most primes whose sum is less than "x".
    sumOfFirstNSummands=updtsumOfFirstNSummands(x,
                                            sumOfFirstNSummands,
                                            sortedSummands)
    curEndIdx=sumOfFirstNSummands[0]
    curSum=sumOfFirstNSummands[1]
    

    #continually "push over" our trial interview,
    #tacking primes on the end and taking them off the front
    while (curEndIdx-curStartIdx) > curMaxConsecPrimes and curSum!=x:
        updates=shiftOver(curStartIdx,curEndIdx,curSum,x, sortedSummands)
        curStartIdx=updates["indOfFirstNum"]
        curEndIdx=updates["indOfLastNum"]
        curSum=updates["curSum"]
        

    return {"intLen":(curEndIdx-curStartIdx)+1,
            "sumOfFirstNSummands":sumOfFirstNSummands,
            "found":(curSum==x)}



def updtsumOfFirstNSummands(x,sumOfFirstNSummands, sortedSummands):
    #return a tuple representing the most (consecutive) primes
    #whose sum is less than x
    
    curEnd=sumOfFirstNSummands[0]
    curSum=sumOfFirstNSummands[1]
    
    while curSum + sortedSummands[curEnd+1] <=  x:
        curEnd+=1
        curSum+=sortedSummands[curEnd]
        #print (x,curSum)
    return(curEnd,curSum)




def shiftOver(a,b,s,x,sortedSummands):
    #"push over" our trial interval, by tacking a prime on the end
    #and removing primes from the front (looking for an interval that
    #sums to x)
    
    indOfNextPrime=b+1
    indOfFirstNum=a
    indOfLastNum=b
    curSum=s
    toAdd=sortedSummands[indOfNextPrime]

    indOfLastNum+=1
    curSum += toAdd
    

    #optimize me
    while curSum > x:
        curSum-=sortedSummands[indOfFirstNum]
        indOfFirstNum+=1
        
    return {"indOfFirstNum":indOfFirstNum,
            "indOfLastNum":indOfLastNum,
            "curSum":curSum}
        
        
        
        
    

#begin SCRIPTING
curMaxConsecPrimes=0
sumOfFrstConsecPrimes=(0,2)
winner=0
for x in primesUnderMil:
    rtnDict=getMaxConsecutiveSummands(primesUnderMil,x,sumOfFrstConsecPrimes, curMaxConsecPrimes)
    curConsecPrimesLen=rtnDict["intLen"]
    sumOfFrstConsecPrimes=rtnDict["sumOfFirstNSummands"]
    won=rtnDict["found"]
    if won and curConsecPrimesLen > curMaxConsecPrimes:
        curMaxConsecPrimes=curConsecPrimesLen
        winner = x

print winner
