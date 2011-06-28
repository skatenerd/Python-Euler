def spell(x):
    if x==1000:
        return "one thousand"
    else:
        first=x/100
        lastTwo=x%100
        if spellDig(first)!="zero":
            firstSeg=spellDig(first)+"hundred"
            if lastTwo!=0:
                firstSeg+="and"
        else:
            firstSeg=""
        return firstSeg+spellPair(lastTwo)

def spellDig(x):
    if x==0:
        return "zero"
    elif x==1:
        return "one"
    elif x==2:
        return "two"
    elif x==3:
        return "three"
    elif x==4:
        return "four"
    elif x==5:
        return "five"
    elif x==6:
        return "six"
    elif x==7:
        return "seven"
    elif x==8:
        return "eight"
    elif x==9:
        return "nine"

def spellPair(x):
    if x==0:
        return ""
    elif x<10:
        return spellDig(x)
    elif x==10:
        return "ten"
    elif x==11:
        return "eleven"
    elif x==12:
        return "twelve"
    elif x==13:
        return "thirteen"
    elif x==14:
        return "fourteen"
    elif x==15:
        return "fifteen"
    elif x==16:
        return "sixteen"
    elif x==17:
        return "seventeen"
    elif x==18:
        return "eighteen"
    elif x==19:
        return "nineteen"
    else:
        if x%10 != 0:
            return spellTens(x/10)+""+spellDig(x%10)
        else:
            return spellTens(x/10)

def spellTens(x):
    if x==1:
        print "ERROR"
    elif x==2:
        return "twenty"
    elif x==3:
        return "thirty"
    elif x==4:
        return "forty"
    elif x==5:
        return "fifty"
    elif x==6:
        return "sixty"
    elif x==7:
        return "seventy"
    elif x==8:
        return "eighty"
    elif x==9:
        return "ninety"
s=0
for x in range(1,1001):
    print spell(x)
    s += len(spell(x))
print s
    
