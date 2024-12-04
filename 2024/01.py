
def prepInput(path):
    aList, bList = [],[]

    for line in open(path):
        a, b = line.split("   ")
        aList.append(int(a))
        bList.append(int(b))

    return aList, bList
def one():
    aList, bList = prepInput("01c.txt")

    aList.sort()
    bList.sort()

    finalList = []
    for a,b in zip(aList,bList):
        finalList.append(abs(a-b))

    resutl = sum(finalList)
    print(finalList,resutl)
def two():
    aList, bList = prepInput("01c.txt")
    finalScore = 0
    for val in aList:
        score = bList.count(val)
        finalScore += val * score

    print(finalScore)

#one()
two()