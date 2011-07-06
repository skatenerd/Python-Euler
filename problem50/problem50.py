import sys
sys.path.append("..")
import prime as p

primesUnderMil=list(p.smartPrimesUnder(1000000))
#print len(primesUnderMil)
primesUnderMil.sort()
print "has finished computing primes under million.  now doing cool work"

def getMaxConsecutiveSummands(sortedPotentialSummands, x,endOfInitInterval, sumOfInitInterval,m):
    curSum=sumOfInitInterval
    curStart=0
    curEnd=endOfInitInterval
    #do something here
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
        

#    return [(curEnd-curStart)+1, initialTerminationInd,initialTerminationSum,curSum==x]
    return {"intLen":(curEnd-curStart)+1, "initTerminationInd":initialTerminationInd, "initTerminationSum":initialTerminationSum, "found":(curSum==x)}

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

    #return [indOfFirstNum,indOfLastNum,curSum]
    return {"indOfFirstNum":indOfFirstNum,"indOfLastNum":indOfLastNum,"curSum":curSum}
        
        
        
        
    



m=0
initListEndInd=0
initListSum=2
winner=0
for x in primesUnderMil:
    #print x
    rtnDict=getMaxConsecutiveSummands(primesUnderMil,x,initListEndInd,initListSum,m)
    curVal=rtnDict["intLen"]
    initListEndInd=rtnDict["initTerminationInd"]
    initListSum=rtnDict["initTerminationSum"]
    won=rtnDict["found"]
    if won and curVal > m:
        #print x
        #print curVal
        m=curVal
        #print m
        winner = x
#print m

print winner
