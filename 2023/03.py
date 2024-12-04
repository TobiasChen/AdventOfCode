
def readLines(file: str):
    listOfElements = []
    with open(file) as f:
        for num, line in enumerate(f):
            listOfElements.append(list(line.strip()))
    return listOfElements
    
def task1():
    lines = readLines("03a.txt")
    numbersByLine = []
    machineParts = []
    nonMachineParts = []
    for line in lines:
        line = [(i, x) for i, x in enumerate(line) if x.isnumeric()]
        numbers = []
        currentIndex = -2
        numberCount = -1
        for number in line:
            if currentIndex + 1 == number[0]:
                numbers[numberCount][0] += number[1]
                numbers[numberCount][1].append(number[0])
            else:
                numbers.append([number[1], [number[0]]])
                numberCount += 1
            currentIndex = number[0]
        numbers = [(int(i), x) for i, x in numbers]
        numbersByLine.append(numbers)
    for i, line in enumerate(numbersByLine):
        for entry in line:
            linesToScan = [j for j in range(i - 1, i+2) if 0 <= j < len(lines)]
            foundMachinePart = False
            #gridToScan = {k: v for k, v in {i - 1: [], i: [], i + 1: []}.items() if 0 <= k < len(lines)}
            for j in linesToScan:
                indexToScan = [k for k in range(entry[1][0] - 1, entry[1][-1]+2) if 0 <= k < len(lines[0])]
                for k in indexToScan:
                    if not (lines[j][k].isnumeric() or lines[j][k] == '.'):
                        foundMachinePart = True
                        break
                if foundMachinePart:
                    break
            if foundMachinePart:
                machineParts.append(entry)
            else:
                nonMachineParts.append(entry)

    results = 0
    for entry in machineParts:
        results += entry[0]

    print(f" Task 3 | Lines analysed: {len(lines)}, Total Numbers: {results}")

def task2():
    lines = readLines("03a.txt")
    numbersByLine = []
    gearParts = []
    for line in lines:
        line = [(i, x) for i, x in enumerate(line) if x.isnumeric()]
        numbers = []
        currentIndex = -2
        numberCount = -1
        for number in line:
            if currentIndex + 1 == number[0]:
                numbers[numberCount][0] += number[1]
                numbers[numberCount][1].append(number[0])
            else:
                numbers.append([number[1], [number[0]]])
                numberCount += 1
            currentIndex = number[0]
        numbers = [(int(i), tuple(x)) for i, x in numbers]
        numbersByLine.append(numbers)
    for i, line in enumerate(numbersByLine):
        gears = [(k, x) for k, x in enumerate(lines[i]) if x == '*']
        for gear in gears:
            matchingNumbers = set()
            linesToScan = [j for j in range(i - 1, i + 2) if 0 <= j < len(lines)]
            for j in linesToScan:
                indexToScan = [k for k in range(gear[0] - 1, gear[0] + 2) if 0 <= k < len(lines[0])]
                for k in indexToScan:
                    for entry in numbersByLine[j]:
                        if k in entry[1]:
                            matchingNumbers.add(entry)
            if len(matchingNumbers) == 2:
                gearParts.append((gear, matchingNumbers))

    results = 0
    for entry in gearParts:
        gearNUmbers = list(entry[1])
        gearRatio = gearNUmbers[0][0] * gearNUmbers[1][0]
        results += gearRatio

    print(f" Task 3 | Lines analysed: {len(lines)}, Total Numbers: {results}")
task1()
task2()
