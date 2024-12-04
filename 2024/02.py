def prepInput(path):
    listOfLists = []

    for line in open(path):
        inputList = line.strip().split(" ")
        listOfLists.append([int(x) for x in inputList])

    return listOfLists

def isIncreasing(lis: list, stripped = False, excersiseOne=True) -> bool:
    for i, val in enumerate(lis[0:-1]):
        if val >= lis[i+1] or (lis[i+1] - val) > 3:
            if excersiseOne or stripped:
                return False
            else:
                return isIncreasing(lis[0:i] + lis[i+1:], stripped=True, excersiseOne=excersiseOne) or isIncreasing(lis[0:i+1] + lis[i+2:], stripped=True, excersiseOne=excersiseOne)
    return True

def isDeacreasing(lis: list, stripped = False, excersiseOne=True):
    for i, val in enumerate(lis[0:-1]):
        if val <= lis[i+1] or (val - lis[i+1]) > 3:
            if excersiseOne or stripped:
                return False
            else:
                return isDeacreasing(lis[0:i] + lis[i+1:], stripped=True, excersiseOne=excersiseOne) or isDeacreasing(lis[0:i+1] + lis[i+2:], stripped=True, excersiseOne=excersiseOne)
    return True

def one():
    listOfLists = prepInput("02c.txt")

    counter = 0
    for line in listOfLists:
        if isIncreasing(line) or isDeacreasing(line):
            counter += 1
    print(f" Task 1 | Counter: {counter}")


def two():
    listOfLists = prepInput("02c.txt")

    counter = 0
    for line in listOfLists:
        safe = isIncreasing(line, excersiseOne=False) or isDeacreasing(line, excersiseOne=False)
        #print(line, safe, isIncreasing(line, excersiseOne=False), isDeacreasing(line, excersiseOne=False))
        if safe:
            counter += 1
    print(f" Task 2 | Counter: {counter}")

one()
two()