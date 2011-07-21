import itertools
import functools

class Card:
    def __init__(self,  suit,number):
        if suit not in range(3):
            raise Exception("invalid suit: "+str(suit))
        if number not in range(2,15):
            raise Exception("invalid number: "+str(number))
        self.mSuit=suit
        self.mNum=number
    def greaterThan(self,otherCard):
        if self.mNum>otherCard.mNum:
            return True
        else:
            return False
    @staticmethod
    def isPair(frst,sec):
        if frst.mNum==sec.mNum:
            return True
        else:
            return False
#foo=Card(1,13)
#bar=Card(2,55)
        
#iterate over pairs, stolenfrom stackoverflow:
def pairs(lst):
    return itertools.combinations(lst,2)

def triples(lst):
    return itertools.combinations(lst,3)


def allEqual(lst, isPair):
    isEqualToFrst=functools.partial(equalityChecker, lst[0])
    bools=map(isEqualToFrst,lst)
    return all(bools)
    

class Hand:
    def __init__(self,cardString):
        self.mCards=[]
        cardDescriptions=cardString.split(" ")
        for x in cardDescriptions:
            self.mCards.append(Card(x[0],x[1]))
    def hasPair(self):
        #for c in self.mCards:
        print "stub"


l=[1,2,3,4,5,6]
for x in pairs(l):
    print x
            
