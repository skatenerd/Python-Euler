curMonth=1
curYear=1901
dayInMonth=6

monthDict={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
    }

def updDay(oldDay, oldMonth, oldYr):
    rtnVal = oldDay
    rtnVal += 7
    oldMoDays=getOldMoDays(oldMonth, oldYr)
    if rtnVal > oldMoDays:
        rtnVal -= oldMoDays
    return rtnVal

def updMonth(oldDay, oldMonth, oldYr):
    rtnVal=oldMonth
    oldMoDays=getOldMoDays(oldMonth, oldYr)    
    if oldDay + 7 > oldMoDays:
        rtnVal += 1
    if rtnVal==13:
        rtnVal=1
    return rtnVal

def updYr(oldDay, oldMonth, oldYr):
    rtnVal = oldYr
    if oldMonth==12:
        if oldDay + 7 > monthDict[12]:
            rtnVal += 1
    return rtnVal

def isLeapYear(x):
    return (((x % 4==0) and (x%100 !=0)) or (x%400 == 0))


def getOldMoDays(oldMonth, oldYr):
        rtnVal=monthDict[oldMonth]
        if isLeapYear(oldYr) and oldMonth == 4:
            rtnVal += 1
        return rtnVal

sList=[]
while curYear<2001:
    if dayInMonth == 1:
        sList.append((curMonth, dayInMonth, curYear))
        print (curMonth, dayInMonth, curYear)
    m=curMonth
    d=dayInMonth
    y=curYear
    curMonth=updMonth(d,m,y)
    curYear=updYr(d,m,y)
    dayInMonth=updDay(d,m,y)
