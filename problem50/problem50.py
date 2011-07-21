##The task here is to take a prime number,P, and determine
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


#calculats the maximum number consecutive summands in sortedPotentialSummands,
#which sum to x.

def getMaxConsecutiveSummands(sortedPotentialSummands,
                              x,
                              endOfInitInterval,
                              sumOfInitInterval):
    curSum=sumOfInitInterval
    curStart=0
    curEnd=endOfInitInterval
    while curSum + sortedPotentialSummands[curEnd+1] <=  x:
        curEnd+=1
        curSum+=sortedPotentialSummands[curEnd]
    initialTerminationInd=curEnd
    initialTerminationSum=curSum


    
    while curEnd>(curStart+m) and curSum!=x:
        updates=shiftOver(curStart,curEnd,curSum,x, sortedPotentialSummands)
        curStart=updates["indOfFirstNum"]
        curEnd=updates["indOfLastNum"]
        curSum=updates["curSum"]
        

    return {"intLen":(curEnd-curStart)+1,
            "initTerminationInd":initialTerminationInd,
            "initTerminationSum":initialTerminationSum,
            "found":(curSum==x)}

def shiftOver(a,b,s,x,sortedPotentialSummands):
    indOfNextPrime=b+1
    indOfFirstNum=a
    indOfLastNum=b
    curSum=s
    toAdd=sortedPotentialSummands[indOfNextPrime]

    indOfLastNum+=1
    curSum += toAdd
    

    #optimize me
    while curSum > x:
        curSum-=sortedPotentialSummands[indOfFirstNum]
        indOfFirstNum+=1
        
    return {"indOfFirstNum":indOfFirstNum,
            "indOfLastNum":indOfLastNum,
            "curSum":curSum}
        
        
        
        
    

#begin SCRIPTING
maxLen=0
initListEndInd=0
initListSum=2
winner=0
for x in primesUnderMil:
    rtnDict=getMaxConsecutiveSummands(primesUnderMil,x,initListEndInd,initListSum)
    curConsecPrimesLen=rtnDict["intLen"]
    initListEndInd=rtnDict["initTerminationInd"]
    initListSum=rtnDict["initTerminationSum"]
    won=rtnDict["found"]
    if won and curConsecPrimesLen > maxLen:
        maxLen=curConsecPrimesLen
        winner = x

print winner
