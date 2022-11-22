def task1():
    with open("03.txt") as f:
        firstLine = f.readline().strip("\n")
    results = [[] for i in range(len(firstLine))]
    epsilonRateString = ""
    gammaRateString = ""
    with open("03.txt") as f:
        for line in f:
            for num, character in enumerate(line.strip("\n")):
                results[num].append(int(character))
    for listLike in results:
        if moreOnes(listLike):
            gammaRateString += "1"
            epsilonRateString += "0"
        else:
            gammaRateString += "0"
            epsilonRateString += "1"

    epsilonRate = int(epsilonRateString, 2)
    gammaRate = int(gammaRateString, 2)

    print(f"Task 1| Epsilon: {epsilonRate}, Gamma: {gammaRate}, Final: {epsilonRate * gammaRate}")


def moreOnes(listLike: list) -> bool:
    ones = listLike.count(1)
    zeros = listLike.count(0)
    return ones >= zeros


def removeNumber(number, sourceList, targetList):
    targetList = targetList.copy()
    sourceList = sourceList.copy()
    if len(sourceList) != len(targetList):
        exit(2)
    for num, element in enumerate(sourceList):
        if element == number:
            targetList[num] = None
    return list(filter(lambda item: item is not None, targetList))


def buildFinalByte(index, columnWiseBits):
    finalString = ""
    for colum in columnWiseBits:
        finalString += str(colum[index])

    return int(finalString, 2)


def task2():
    with open("03.txt") as f:
        firstLine = f.readline().strip("\n")
    sortedBits = [[] for i in range(len(firstLine))]

    with open("03.txt") as f:
        for line in f:
            for num, character in enumerate(line.strip("\n")):
                sortedBits[num].append(int(character))

    indicesCO2Scrubber = [i for i in range(len(sortedBits[0]))]
    for num, listOfBits in enumerate(sortedBits):
        if len(indicesCO2Scrubber) == 1:
            break
        consideredListCO2 = [listOfBits[x] for x in indicesCO2Scrubber]
        indicesCO2Scrubber = removeNumber(1, consideredListCO2, indicesCO2Scrubber) \
            if moreOnes(consideredListCO2) else removeNumber(0, consideredListCO2, indicesCO2Scrubber)

    indicesOxygenGenerator = [i for i in range(len(sortedBits[0]))]
    for num, listOfBits in enumerate(sortedBits):
        if len(indicesOxygenGenerator) == 1:
            break
        consideredListOxygen = [listOfBits[x] for x in indicesOxygenGenerator]
        indicesOxygenGenerator = removeNumber(0, consideredListOxygen, indicesOxygenGenerator) \
            if moreOnes(consideredListOxygen) else removeNumber(1, consideredListOxygen, indicesOxygenGenerator)

    finalCO2Rating = buildFinalByte(indicesCO2Scrubber[0], sortedBits)
    finalOxygenRating = buildFinalByte(indicesOxygenGenerator[0], sortedBits)

    print(f"Task 2| CO2: {finalCO2Rating}, Oxygen: {finalOxygenRating}, Final: {finalCO2Rating * finalOxygenRating}")


task1()
task2()
