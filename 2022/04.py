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
    listOfSections = []
    with open(file) as f:
        for num, line in enumerate(f):
            line = line.strip()
            elves = line.split(",")
            listOfSections.append([])
            for elf in elves:
                elements = elf.split("-")
                listOfSections[num].append(CleaningSection(int(elements[0]),int(elements[1])))

    return listOfSections


def task1():
    elvenPairs = readElements("04.txt")
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
task2()