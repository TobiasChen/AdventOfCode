import math


def py2round(x):
    if x >= 0.0:
        return math.floor(x + 0.5)
    else:
        return math.ceil(x - 0.5)


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def tailFollowHead(tailPosition: Point, headPosition: Point):
    xDiff = headPosition.x - tailPosition.x
    yDiff = headPosition.y - tailPosition.y
    if abs(xDiff) < 2 and abs(yDiff) < 2:
        return tailPosition
    else:
        newX = tailPosition.x + py2round(xDiff / 2)
        newY = tailPosition.y + py2round(yDiff / 2)
        return Point(newX, newY)


def readElements(file: str):
    with open(file) as f:
        instructions = []
        for num, line in enumerate(f):
            line = line.strip()
            instructions.append(line.split(" "))
        return instructions

def task1():
    instructions = readElements("09.txt")
    visitedPoints = []
    tailPosition = Point(0, 0)
    headPosition = Point(0, 0)
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
            tailPosition = tailFollowHead(tailPosition, headPosition)
            visitedPoints.append(tailPosition)

    visitedPoints = list(set(visitedPoints))
    visitedPoints.sort(key=lambda x: x.y)
    print(f" Task 1 | Total instructions: {len(instructions)}, Visited points: {visitedPoints} and {len(visitedPoints)}")


def task2():
    instructions = readElements("09.txt")
    visitedPoints = []
    headPosition = Point(0, 0)
    tailPositions = []
    for i in range(9):
        tailPositions.append(Point(0,0))
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
            for i in range(1,9):
                tailPositions[i] = tailFollowHead(tailPositions[i], tailPositions[i - 1])
            visitedPoints.append(tailPositions[8])

    visitedPoints = list(set(visitedPoints))
    visitedPoints.sort(key=lambda x: x.y)
    print(f" Task 2 | Total instructions: {len(instructions)}, Visited points: {visitedPoints} and {len(visitedPoints)}")


task1()
task2()
