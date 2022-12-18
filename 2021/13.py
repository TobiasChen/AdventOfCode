from enum import StrEnum


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Map:
    def __init__(self):
        self.grid = [[0]]
        self.operatorList = []

    def adjustGridSize(self, point: Point):
        if point.x > len(self.grid[0]) - 1:
            missingColumns = point.x - len(self.grid[0]) + 1
            for row in self.grid:
                row += [0] * missingColumns
        if point.y > len(self.grid) - 1:
            missingRows = point.y - len(self.grid) + 1
            self.grid += [[0 for x in range(len(self.grid[0]))] for i in range(missingRows)]

    def addPoint(self, point: Point):
        self.adjustGridSize(point)
        self.grid[point.y][point.x] = 1

    def foldAlongHorizontalAxis(self, lineNumberY):
        for y, row in enumerate(self.grid):
            if y < lineNumberY:
                continue
            else:
                for x, col in enumerate(self.grid[y]):
                    if self.grid[y][x]:
                        newY = (len(self.grid) - 1) - y
                        self.grid[newY][x] = 1

        del self.grid[lineNumberY:]

    def foldAlongVerticalAxis(self, lineNumberX):
        for y, row in enumerate(self.grid):
            for x, col in enumerate(self.grid[y]):
                if x < lineNumberX:
                    continue
                else:
                    if self.grid[y][x]:
                        newX = (len(self.grid[y]) - 1) - x
                        self.grid[y][newX] = 1
            del self.grid[y][lineNumberX:]

    def countDots(self):
        sum1 = 0
        for row in self.grid:
            for col in row:
                if col:
                    sum1 += 1
        return sum1


def parseInput(map: Map):
    with open("13.txt") as f:
        whiteSpace = False
        for num, line in enumerate(f):
            line = line.strip()
            if not line:
                whiteSpace = True
            else:
                if not whiteSpace:
                    x, y = line.split(",")
                    map.addPoint(Point(int(x), int(y)))
                else:
                    line = line.split(" ")[2].split("=")
                    line[1] = int(line[1])
                    map.operatorList.append(line)


def task1():
    board = Map()
    parseInput(board)
    operator = board.operatorList[0]
    if operator[0] == "x":
        board.foldAlongVerticalAxis(operator[1])
    elif operator[0] == "y":
        board.foldAlongHorizontalAxis(operator[1])

    print(f" Task 1 | Dots: {board.countDots()}")


def task2():
    board = Map()
    parseInput(board)
    for operator in board.operatorList:
        if operator[0] == "x":
            board.foldAlongVerticalAxis(operator[1])
        elif operator[0] == "y":
            board.foldAlongHorizontalAxis(operator[1])
    newGrid = []
    for i in range(8):
        newGrid.append([])
        for row in board.grid:
            newGrid[i].append(row[i*5:i*5 + 5])
    print(f" Task 2 | Dots: {board.countDots()}")




task1()
task2()
