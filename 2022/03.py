def getPriority(character: str):
    if str.isupper(character):
        return ord(character) - ord("A") + 27
    else:
        return ord(character) - ord("a") + 1

def readElements(file: str):
    listOfBackpacks = []
    with open(file) as f:
        for num, line in enumerate(f):
            listOfBackpacks.append(line.strip())

    return listOfBackpacks


def task1():
    backpacks = readElements("03.txt")
    sumOfPoints = 0
    for listy in backpacks:
        listy = [listy[:len(listy) // 2], listy[len(listy) // 2:]]
        matchingChars = list(set(listy[0])&set(listy[1]))
        if len(matchingChars) > 1:
            print(matchingChars)
        else:
            sumOfPoints += getPriority(matchingChars[0])

    print(f" Task 1 | Games played: {len(backpacks)}, Total Points: {sumOfPoints}")


def task2():
    elements = readElements("03.txt")
    totalBadgeType = 0
    currentList = []
    for ident, backpack in enumerate(elements):
        currentList.append(backpack)
        if (ident + 1) % 3 == 0:
            badgeSet = set(currentList[0])
            for listy in currentList:
                badgeSet = badgeSet & set(listy)
            if len(badgeSet) > 1:
                print("Shouldnt happen")
            charac = list(badgeSet)[0]
            totalBadgeType += getPriority(charac)
            currentList = []
    if currentList:
        print("Shouldnt happeneither")
    print(f" Task 2 | Backpacks counted: {len(elements)}, Total Points: {totalBadgeType}")


task1()
task2()