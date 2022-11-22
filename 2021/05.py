from itertools import compress
import numpy as np

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Vector:
    def __init__(self, startPoint: Point, endPoint: Point):
        self.startPoint = startPoint
        self.endPoint = endPoint

    def furthestFromZero(self) -> Point:
        furthestX = self.startPoint.x if self.startPoint.x > self.endPoint.x else self.endPoint.x
        furthestY = self.startPoint.y if self.startPoint.y > self.endPoint.y else self.endPoint.y
        return Point(furthestX, furthestY)

    def direction(self):
        return Point(self.endPoint.x - self.startPoint.x, self.endPoint.y - self.startPoint.y)

    def length(self):
        return abs(self.endPoint.x - self.startPoint.x) + abs(self.endPoint.y - self.startPoint.y)


class Board:
    def __init__(self):
        self.grid = [[0]]
        self.vectors = []

    def adjustGridSize(self, vector: Vector):
        furthestFromZero = vector.furthestFromZero()
        if furthestFromZero.x > len(self.grid[0]) - 1:
            missingColumns = furthestFromZero.x - len(self.grid[0]) + 1
            for row in self.grid:
                row += [0] * missingColumns
        if furthestFromZero.y > len(self.grid) - 1:
            missingRows = furthestFromZero.y - len(self.grid) + 1
            self.grid += [[0 for x in range(len(self.grid[0]))] for i in range(missingRows)]

    def addThermalVent(self, vector: Vector, addDiagonals: bool):
        self.adjustGridSize(vector)
        xDiff = abs(vector.direction().x)
        yDiff = abs(vector.direction().y)
        if xDiff == 0 and yDiff == 0:
            self.grid[vector.startPoint.y][vector.startPoint.x] += 1
            self.vectors.append(vector)
        elif xDiff != 0 and yDiff != 0 and addDiagonals:
            self.vectors.append(vector)
            for i in range(xDiff + 1):
                self.grid[vector.startPoint.y + (i * np.sign(vector.direction().y))][vector.startPoint.x + (i * np.sign(vector.direction().x))] += 1
        elif xDiff != 0 and yDiff != 0 and not addDiagonals:
            return
        else:
            self.vectors.append(vector)
            self.grid[vector.endPoint.y][vector.endPoint.x] += 1
            for i in range(xDiff):
                    self.grid[vector.startPoint.y][vector.startPoint.x + (i * np.sign(vector.direction().x))] += 1
            for i in range(yDiff):
                    self.grid[vector.startPoint.y + (i * np.sign(vector.direction().y))][vector.startPoint.x] += 1



def task1():
    seaFloor = Board()
    with open("05.txt") as f:
        for num, line in enumerate(f):
            start, finish = line.strip("\n").split("->")
            startPoint = Point(int(start.split(",")[0]), int(start.split(",")[1]))
            endPoint = Point(int(finish.split(",")[0]), int(finish.split(",")[1]))
            seaFloor.addThermalVent(Vector(startPoint, endPoint), False)
    sumedUp = 0
    for row in seaFloor.grid:
        sumedUp += sum(i > 1 for i in row)
    print(f" Task 1 | Sum: {sumedUp}")

def task2():
    seaFloor = Board()
    with open("05.txt") as f:
        for num, line in enumerate(f):
            start, finish = line.strip("\n").split("->")
            startPoint = Point(int(start.split(",")[0]), int(start.split(",")[1]))
            endPoint = Point(int(finish.split(",")[0]), int(finish.split(",")[1]))
            seaFloor.addThermalVent(Vector(startPoint, endPoint), True)
    sumedUp = 0
    for row in seaFloor.grid:
        sumedUp += sum(i > 1 for i in row)
    print(f" Task 2 | Sum: {sumedUp}")


task1()
task2()
