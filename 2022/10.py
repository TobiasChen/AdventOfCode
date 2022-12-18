def readElements(file: str):
    with open(file) as f:
        instructions = []
        for num, line in enumerate(f):
            line = line.strip()
            instructions.append(line.split(" "))
        return instructions


class CPU:
    def __init__(self):
        self.register = 1
        self.crtOutput = [["#"]]
        self.clock = 0
        self.signalStrength = []
        self.relevantCycles = [40 + 40 * x for x in range(6)]

    def advanceClock(self):
        self.clock += 1
        if self.clock in self.relevantCycles:
            self.crtOutput.append([])
            self.signalStrength.append((self.clock, self.register, self.clock * self.register))
        if self.clock % 40 - reg


def task1():
    instructions = readElements("10.txt")
    cpu = CPU()
    for instruction in instructions:
        if instruction[0] == "noop":
            cpu.advanceClock()
        elif instruction[0] == "addx":
            cpu.advanceClock()
            cpu.advanceClock()
            cpu.register += int(instruction[1])

    totalSignalStrength = sum([x[2] for x in cpu.signalStrength])
    print(f" Task 1 | Total instructions: {len(instructions)}, TotalSignalStrength: {totalSignalStrength}")


def task2():
    instructions = readElements("09.txt")
    visitedPoints = []
    headPosition = Point(0, 0)
    tailPositions = []
    for i in range(9):
        tailPositions.append(Point(0, 0))
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1])
        for step in range(steps):
            if direction == "R":
                headPosition.x += 1
            elif direction == "L":
                headPosition.x -= 1
            elif direction == "U":
                headPosition.y += 1
            elif direction == "D":
                headPosition.y -= 1
            tailPositions[0] = tailFollowHead(tailPositions[0], headPosition)
            for i in range(1, 9):
                tailPositions[i] = tailFollowHead(tailPositions[i], tailPositions[i - 1])
            visitedPoints.append(tailPositions[8])

    visitedPoints = list(set(visitedPoints))
    visitedPoints.sort(key=lambda x: x.y)
    print(
        f" Task 2 | Total instructions: {len(instructions)}, Visited points: {visitedPoints} and {len(visitedPoints)}")


task1()
task2()
