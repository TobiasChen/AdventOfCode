import itertools
from enum import Enum
from itertools import cycle


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}|{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))


class Directions(Enum):
    North = Coordinate(0, -1)
    East = Coordinate(1, 0)
    South = Coordinate(0, 1)
    West = Coordinate(-1, 0)


def outOfBoundes(coordinates, height, width):
    if 0 <= coordinates.x <= width - 1:
        if 0 <= coordinates.y <= height - 1:
            return False
    return True


def prepInput(path):
    puzzle = []
    lines = open(path, 'r').readlines()
    for line in lines:
        line = line.strip()
        puzzle.append([x for x in line])
    return puzzle


def one(path: str):
    lines = prepInput(path)
    height = len(lines)
    width = len(lines[0])
    directionsCycle = cycle(Directions)

    for y, line in enumerate(lines):
        if "^" in line:
            x = line.index("^")
            currentPos = Coordinate(x, y)
            break
    lines[y][x] = "."
    currentDirection = next(directionsCycle)

    guardPatrolling = True
    counter = 0

    while guardPatrolling:
        nextPos = currentPos + currentDirection.value
        if outOfBoundes(nextPos, height, width):
            guardPatrolling = False
            lines[currentPos.y][currentPos.x] = "X"
            counter += 1
        else:
            if lines[nextPos.y][nextPos.x] == "#":
                currentDirection = next(directionsCycle)
            else:
                if lines[currentPos.y][currentPos.x] == '.':
                    lines[currentPos.y][currentPos.x] = "X"
                    counter += 1
                currentPos = nextPos

    print(f"Final Task One: {counter}")


def findFirstSharpInLine(puzzle: list[list[str]], pos, direction):
    currentPos = pos
    height = len(puzzle)
    width = len(puzzle[0])
    while True:
        currentPos += direction.value
        if outOfBoundes(currentPos, height, width):
            return False
        if puzzle[currentPos.y][currentPos.x] == "#":
            return currentPos


def clearLineBetweenPoints(puzzle: list[list[str]], pointA: Coordinate, pointB: Coordinate):
    height = len(puzzle)
    width = len(puzzle[0])
    diff = pointB - pointA
    if diff.x != 0 and diff.y != 0:
        print(f"Points not in same Row or Column: {pointA}, {pointB}")
        return False
    else:
        absolute = abs(diff.x + diff.y)
        direction = Coordinate(diff.x // absolute, diff.y // absolute)
        curentPos = pointA
        while curentPos != pointB:
            if puzzle[curentPos.y][curentPos.x] == "#":
                return False
            else:
                curentPos += direction
        return True


def two(path: str):
    lines = prepInput(path)
    height = len(lines)
    width = len(lines[0])
    directionsCycle = cycle(Directions)

    for y, line in enumerate(lines):
        if "^" in line:
            x = line.index("^")
            currentPos = Coordinate(x, y)
            break
    lines[y][x] = "^"
    startPos = Coordinate(x, y)
    currentDirection = next(directionsCycle)

    guardPatrolling = True
    counter = 0

    while guardPatrolling:
        nextPos = currentPos + currentDirection.value
        if outOfBoundes(nextPos, height, width):
            guardPatrolling = False
            lines[currentPos.y][currentPos.x] = "X"
        else:
            if lines[nextPos.y][nextPos.x] == "#":  # Next Step is an obstacle
                # turnQueue.append((currentPos,abs(currentDirection.x))) #For NorthToEast Turn abs(currentDirection.x) = 0, East=1,South=0,West=1
                currentDirection = next(directionsCycle)
            else:  # Next step is not an obstacle
                if lines[currentPos.y][currentPos.x] == '.':  # Current was not visited previously:
                    lines[currentPos.y][currentPos.x] = "X"

                # Check for potential turn
                if lines[nextPos.y][nextPos.x] == ".":
                    listOfPoints = [(nextPos, currentDirection)]
                    directionsCycle, potentialNextDirectionCycle = itertools.tee(directionsCycle)
                    potentialNextDirection = next(potentialNextDirectionCycle)
                    lines[nextPos.y][nextPos.x] = "#"
                    nextSharp = findFirstSharpInLine(puzzle=lines, pos=currentPos, direction=potentialNextDirection)
                    while True:
                        if nextSharp:
                            if (nextSharp, potentialNextDirection) in listOfPoints:
                                # print(f"--------------Counter {counter}----------------")
                                # print(len(listOfPoints))
                                # print(listOfPoints)
                                # lines2 = [line.copy() for line in lines]
                                # for a in listOfPoints:
                                #     lines2[a[0].y][a[0].x] = "V"
                                # lines2[nextPos.y][nextPos.x] = "T"
                                # lines2[startPos.y][startPos.x] = "^"
                                # for line123 in lines2:
                                #     print("".join(line123))
                                # print("------------------------------")
                                counter += 1
                                break
                            else:
                                listOfPoints.append((nextSharp, potentialNextDirection))
                                anchor = nextSharp - potentialNextDirection.value
                                potentialNextDirection = next(potentialNextDirectionCycle)
                                nextSharp = findFirstSharpInLine(puzzle=lines, pos=anchor,
                                                                 direction=potentialNextDirection)
                        else:
                            break
                    lines[nextPos.y][nextPos.x] = "."
                    # directionsCycle, potentialNextDirectionCycle = itertools.tee(directionsCycle)
                    # potentialNextDirection = next(potentialNextDirectionCycle)
                    # a1 = findFirstSharpInLine(puzzle=lines, pos=currentPos, direction=potentialNextDirection)
                    # if a1:
                    #     anchor1 = a1 - potentialNextDirection.value
                    #     potentialNextDirection = next(potentialNextDirectionCycle)
                    #     a2 = findFirstSharpInLine(puzzle=lines, pos=anchor1, direction=potentialNextDirection)
                    #     if a2:
                    #         anchor2 = a2 - potentialNextDirection.value
                    #         potentialNextDirection = next(potentialNextDirectionCycle)
                    #         a3 = findFirstSharpInLine(puzzle=lines, pos=anchor2, direction=potentialNextDirection)
                    #         if a3 and clearLineBetweenPoints(puzzle=lines, pointA=a3-potentialNextDirection.value, pointB=currentPos):

                currentPos = nextPos

    print(f"Final Task Two: {counter}")


test = False


def main():
    current = __file__.strip('.py')
    if test:
        one(current + "a.txt")
        two(current + "a.txt")
    else:
        print("Calling Toby")
        one(current + "b.txt")
        two(current + "b.txt")
        print("Calling Freya")
        one(current + "c.txt")
        two(current + "c.txt")


main()
