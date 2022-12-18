from collections import Counter


class Map:
    def __init__(self):
        self.mappingDict = [[]]


def parseInput(inputHandle: Map):
    with open("14.txt") as f:
        for num, line in enumerate(f):
            line = line.strip()
            if not line:
                whiteSpace = True
            else:
                if not whiteSpace:
                    inputHandle.initialString = line
                else:
                    line = line.split("->")
                    inputHandle.mappingDict[line[0].strip()] = line[1].strip()


def task1(input1: Map):
    workingString = list(input1.initialString)
    mappingDict = input1.mappingDict
    mappGet = mappingDict.get
    for i in range(10):
        newString = list(workingString[0])
        append = newString.append
        for j in range(len(workingString) - 2):
            if mappGet(workingString[j] + workingString[j + 1]) is None:
                print("test")
            append(mappGet(workingString[j] + workingString[j + 1]))
            append(workingString[j+1])
        workingString = newString

    resultList = list(workingString)
    counter = Counter(resultList)
    listy = list(counter.values())
    listy.sort()
    print(f" Task 1 | Quantity: {listy[len(listy) - 1] - listy[0]}")


def task2(input1: Map):
    workingString = list(input1.initialString)
    mappingDict = input1.mappingDict
    mappGet = mappingDict.get
    for i in range(40):
        newString = list(workingString[0])
        append = newString.append
        for j in range(len(workingString) - 2):
            if mappGet(workingString[j] + workingString[j + 1]) is None:
                print("test")
            append(mappGet(workingString[j] + workingString[j + 1]))
            append(workingString[j + 1])
        workingString = newString

    resultList = list(workingString)
    counter = Counter(resultList)
    listy = list(counter.values())
    listy.sort()
    print(f" Task 2 | Quantity: {listy[len(listy) - 1] - listy[0]}")


map1 = Map()

parseInput(map1)
task1(map1)
task2(map1)
