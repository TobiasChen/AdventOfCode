class CleaningSection:
    def __init__(self, start, end):
        self.start =start
        self.end = end

    def __repr__(self):
        return f"{str(self.start)}-{str(self.end)}"

    def contains(self, other):
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other):
        return self.start <= other.start <= self.end or self.start <= other.end <= self.end or self.contains(other)

def readElements(file: str):
    listOfStacks = []
    listOfInstructions = []
    readingInstructions = False
    with open(file) as f:
        listOfStackLines = []
        for num, line in enumerate(f):
            line2 = line.strip()
            if not line2:
                readingInstructions = True

                stackNumberLine = listOfStackLines.pop()
                stackNumberLine = list(set(stackNumberLine.strip()))
                stackNumberLine.remove(" ")
                for el in stackNumberLine:
                    listOfStacks.append([])
                numberOfStacks = len(listOfStacks)
                listOfStackLines.reverse()
                for stackLine in listOfStackLines:
                    for num1, stack in enumerate(listOfStacks):
                        if not str.isspace(stackLine[num1*4 + 1]):
                            stack.append(stackLine[num1 * 4 + 1])
                continue
            if not readingInstructions:
                listOfStackLines.append(line)
            else:
                listOfInstructions.append(line2)

    return listOfStacks,listOfInstructions


def task1():
    stacks, instructions = readElements("05.txt")
    faultyAssignments = 0
    for sections in elvenPairs:
        if sections[0].contains(sections[1]) or sections[1].contains(sections[0]):
            faultyAssignments += 1

    print(f" Task 1 | Assignments analyzed: {len(elvenPairs)}, Faulty Assignments: {faultyAssignments}")


def task2():
    elvenPairs = readElements("04.txt")
    faultyAssignments = 0
    for sections in elvenPairs:
        if sections[0].overlaps(sections[1]) or sections[1].overlaps(sections[0]):
            faultyAssignments += 1

    print(f" Task 2 | Assignments analyzed: {len(elvenPairs)}, Faulty Assignments: {faultyAssignments}")


task1()