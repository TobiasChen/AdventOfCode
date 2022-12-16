import re


class CleaningSection:
    def __init__(self, start, end):
        self.start = start
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
                listOfStackLines.reverse()
                for stackLine in listOfStackLines:
                    for num1, stack in enumerate(listOfStacks):
                        if not str.isspace(stackLine[num1 * 4 + 1]):
                            stack.append(stackLine[num1 * 4 + 1])
                continue
            if not readingInstructions:
                listOfStackLines.append(line)
            else:
                listOfInstructions.append(list(map(lambda x: int(x), re.findall(r'\d+', line2))))

    return listOfStacks, listOfInstructions


def task1():
    stacks, instructions = readElements("05.txt")
    for instruction in instructions:
        target = instruction[2] - 1
        source = instruction[1] - 1
        num = instruction[0]
        for i in range(num):
            stacks[target] += stacks[source].pop()

    strin = ""
    for stack in stacks:
        strin += stack[-1]

    print(f" Task 1 | Instructions done: {len(instructions)}, Final String: {strin}")


def task2():
    stacks, instructions = readElements("05.txt")
    for instruction in instructions:
        target = instruction[2] - 1
        source = instruction[1] - 1
        num = instruction[0]

        stacks[target] += stacks[source][-num:]
        del stacks[source][-num:]

    strin = ""
    for stack in stacks:
        strin += stack[-1]

    print(f" Task 2 | Instructions done: {len(instructions)}, Final String: {strin}")


task1()
task2()
