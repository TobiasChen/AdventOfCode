from enum import Enum
def readLines(file: str, parseB):
    with open(file) as f:
        games = []
        for num, line in enumerate(f):
            line = line.strip()
            hand, bet = line.split(" ")
            games.append(Hand(hand.strip(), int(bet.strip())))
        return games


class CardStrength(Enum):
    A = 13
    K = 12
    Q = 11
    J = 10
    T = 9


class HandStrength(Enum):
    FiveKind = 7
    FourKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    Single = 1


def getStrength(hand: str) -> HandStrength:
    buckets = []
    for card in hand:
        foundFit = False
        for buck in buckets:
            if buck[0] == card:
                buck[1] += 1
                foundFit = True
        if not foundFit:
            buckets.append([card,1])
    buckets.sort(reverse=True,key=lambda x: x[1])
    match buckets[0][1]:
        case 5:
            return HandStrength.FiveKind
        case 4:
            return HandStrength.FourKind
        case 3:
            return HandStrength.FullHouse if buckets[1][1] == 2 else HandStrength.ThreeOfAKind
        case 2:
            return HandStrength.TwoPair if buckets[1][1] == 2 else HandStrength.OnePair
        case _:
            return HandStrength.Single
    pass

def getCardStrength(a: chr) -> int:
    if a.isdigit():
        return int(a) - 2
    else:
        return CardStrength[a].value

class Hand():
    def __init__(self, cards, bet) -> None:
           self.cards = cards
           self.bet = bet

    def __lt__(self,other):
        aStr = getStrength(self.cards)
        bStr = getStrength(other.cards)
        if aStr == bStr:
            for card1,card2 in zip(self.cards,other.cards):
                card1Strength = getCardStrength(card1)
                card2Strength = getCardStrength(card2)
                if card1Strength != card2Strength:
                    return card1Strength < card2Strength    
            return False
        else:
            return aStr.value < bStr.value
        
    def __str__(self) -> str:
        return f"{self.cards} {self.bet}"
    
    def __repr__(self) -> str:
        return f"Hand({self.cards},{self.bet})"
    
def task1():
    hands = readLines("07.txt", False)
    
    hands.sort()
    finalBet = 0
    for i, hand in enumerate(hands):
        finalBet += hand.bet * (i + 1)

    print(f" Task 1 | Total Winnings: {finalBet}")


def task2():
    pass


task1()
task2()