import collections
from itertools import groupby

class Matcher:
    def __init__(self):
        self.currentMatches = {key: [] for key in range(7)}
        self.pattern = {key: None for key in range(10)}
        self.relevantNumbers = {
            1: {2, 5},
            7: {0, 2, 5},
            4: {1, 2, 3, 5},
            2: {0, 2, 3, 4, 6}, 3: {0, 2, 3, 5, 6}, 5: {0, 1, 3, 5, 6},
            0: {0, 1, 2, 4, 5, 6}, 6: {0, 1, 3, 4, 5, 6},9: {0, 1, 2, 3, 5, 6},
            8: {0, 1, 2, 3, 4, 5, 6}}
    def identify0(self, pattern1,pattern7):
        pattern = list(set(pattern7).difference(pattern1))[0]
        self.pattern[1] = set(pattern1)
        self.pattern[7] = set(pattern7)
        self.currentMatches[0] = pattern

    def identify1And4(self,listOf5erPatterns, pattern4):
        totalList = []
        for pattern in listOf5erPatterns:
            totalList.extend(pattern)
        counter = collections.Counter(totalList)
        self.pattern[4] = set(pattern4)
        onesAndFours = [d for d in totalList if counter[d] == 1]
        if onesAndFours[0] in pattern4:
            self.currentMatches[1] = onesAndFours[0]
            self.currentMatches[4] = onesAndFours[1]
        elif onesAndFours[1] in pattern4:
            self.currentMatches[1] = onesAndFours[1]
            self.currentMatches[4] = onesAndFours[0]
        else:
            return 10/0

    def identify3(self):
        oneAndThree = [sym for sym in self.pattern[4] if sym not in self.pattern[1]]
        oneAndThree.remove(self.currentMatches[1])
        self.currentMatches[3] = oneAndThree[0]

    def identify2And5(self, listOf6erPatterns):
        totalList = []
        for pattern in listOf6erPatterns:
            totalList.extend(pattern)
        counter = collections.Counter(totalList)
        twoAndThreeAndFour = {d for d in totalList if counter[d] == 2}
        twoAndThreeAndFour.remove(self.currentMatches[3])
        twoAndThreeAndFour.remove(self.currentMatches[4])
        finalTwo = list(twoAndThreeAndFour)[0]
        self.currentMatches[2] = finalTwo
        finalFive = list(self.pattern[1])
        finalFive.remove(finalTwo)
        self.currentMatches[5] = finalFive[0]

    def identify6(self, pattern8):
        setPattern = set(pattern8)
        self.pattern[8] = setPattern.copy()
        for key,val in self.currentMatches.items():
            if val:
                setPattern.remove(val)
        self.currentMatches[6] = list(setPattern)[0]

    def buildMissingPatterns(self):
        for k, v in self.pattern.items():
            if not v:
                testSet = {self.currentMatches[number] for number in self.relevantNumbers.get(k) }
                self.pattern[k] = testSet
            else:
                if v != {self.currentMatches[number] for number in self.relevantNumbers.get(k)}:
                    print("Warning")

    def identifyNumber(self, inputSet):
        for k,v in self.pattern.items():
            if v == inputSet:
                return k
        else:
            return None

def task1():
    with open("08.txt") as f:
        listOfInputs = []
        for line in f:
            pattern, display = line.strip().split("|")
            display = display.strip().split(" ")
            pattern = pattern.strip().split(" ")
            listOfInputs.append({"pattern": pattern, "display": display})

        sumIng = 0
        for dicty in listOfInputs:
            for dis in dicty.get("display"):
                if len(dis) in [7, 4, 2, 3]:
                    sumIng += 1

    print(f" Task 1 | Count Digits {sumIng}")


def task2():
    with open("08.txt") as f:
        listOfInputs = []
        for line in f:
            pattern, display = line.strip().split("|")
            display = display.strip().split(" ")
            pattern = pattern.strip().split(" ")
            listOfInputs.append({"pattern": pattern, "display": display})

        sumIng = 0
        for num, dicty in enumerate(listOfInputs):
            matcher = Matcher()
            patternDict = {}
            for item in dicty.get("pattern"):
                if not len(item) in patternDict.keys():
                    patternDict[len(item)] = []
                patternDict[len(item)].append(item)
            matcher.identify0(patternDict[2][0], patternDict[3][0])
            matcher.identify1And4(patternDict[5], patternDict[4][0])
            matcher.identify3()
            matcher.identify2And5(patternDict[6])
            matcher.identify6(patternDict[7][0])
            matcher.buildMissingPatterns()

            outputNumber = ""
            for number in dicty.get("display"):
                numberSet = set(number)
                if(matcher.identifyNumber(numberSet) == None):
                    print("warning")
                outputNumber += str(matcher.identifyNumber(numberSet))
            sumIng += int(outputNumber)
        print(f" Task 2 | Counted Digits {sumIng}")


task1()
task2()
