
def readLines(file: str):
    listOfElements = []
    with open(file) as f:
        for num, line in enumerate(f):
            listOfElements.append(list(line.strip()))
    return listOfElements
    
def task1():
    lines = readLines("01a.txt")
    results = 0
    for line in lines:
        line = [x for x in line if x.isnumeric()]
        number = int(line[0]+line[-1])
        results += number
    print(f" Task 1 | Lines analysed: {len(lines)}, Total Numbers: {results}")

class PossibleString():
    def __init__(self,char):
        self.currentPossibleNumberIndex = [x for x in range(0,9)]
        self.currentLetterIndex = 1
        self.currentLetterString = char 


def checkLine(line):
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    line2 = []
    possibleStrings = []
    for char in line:
        resetVars = False
        if char.isnumeric():
            line2.append(char)
            resetVars = True
        newPossibleStrings = []
        for possibleString in possibleStrings:
            if char in [numbers[x][possibleString.currentLetterIndex] for x in possibleString.currentPossibleNumberIndex if possibleString.currentLetterIndex < len(numbers[x])]:
                possibleString.currentPossibleNumberIndex = [x for x in possibleString.currentPossibleNumberIndex if numbers[x][possibleString.currentLetterIndex] == char]
                possibleString.currentLetterString += char 
                possibleString.currentLetterIndex += 1
                newPossibleStrings.append(possibleString)
                if possibleString.currentLetterString in numbers:
                    line2.append(str(numbers.index(possibleString.currentLetterString) + 1))
                    resetVars = True

        possibleStrings = newPossibleStrings
        if char in [x[0] for x in numbers]:
            possibleStrings.append(PossibleString(char))

        if resetVars:
            possibleStrings = []
    return line2

def task2():
    lines = readLines("01a.txt")
    results = 0
    
    for line in lines:
        newLine = checkLine(line)
        number = int(newLine[0]+newLine[-1])
        print(line,newLine,number)
        results += number
    print(f" Task 2 | Lines analysed: {len(lines)}, Total Numbers: {results}")
task1()
task2()
