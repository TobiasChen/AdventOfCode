def readElements(file: str):
    basicString = ""
    with open(file) as f:
        for num, line in enumerate(f):
            line = line.strip()
            basicString += line
    return basicString


def task1():
    basicString = readElements("06.txt")
    stackOfLastFour = []
    correctSlot = 0
    for iter1, char in enumerate(basicString):
        stackOfLastFour.append(char)
        if len(set(stackOfLastFour)) == 4:
            correctSlot = iter1 + 1
            break
        if len(stackOfLastFour) > 3:
            del stackOfLastFour[0]

    print(f" Task 1 | Length of String: {len(basicString)}, Final Slot: {correctSlot}")


def task2():
    basicString = readElements("06.txt")
    stackOfLastFour = []
    correctSlot = 0
    for iter1, char in enumerate(basicString):
        stackOfLastFour.append(char)
        if len(set(stackOfLastFour)) == 14:
            correctSlot = iter1 + 1
            break
        if len(stackOfLastFour) > 13:
            del stackOfLastFour[0]

    print(f" Task 1 | Length of String: {len(basicString)}, Final Slot: {correctSlot}")



task1()
task2()
