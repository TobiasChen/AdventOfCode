import collections
from itertools import groupby
class Board:
    def __init__(self, ):
        self.grid = []
        self.basin = None
        self.basinDictionary = {}
        self.vectors = []

    def generateSurroundingBasin(self, x ,y):
        nodeList = [(x, y)]
        basinID = len(self.basinDictionary)
        self.basin[y][x] = basinID
        self.basinDictionary[basinID] = 1

        while nodeList:
            newNodeList = []
            for node in nodeList:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        newx = node[0] + dx
                        newy = node[1] + dy
                        if dx == 0 and dy == 0:
                            continue
                        if abs(dx) == abs(dy):
                            continue
                        if 0 <= newx < len(self.basin[0]) and 0 <= newy < len(self.basin):
                            if self.basin[newy][newx] == basinID or self.basin[newy][newx] == "X":
                                continue
                            elif self.basin[newy][newx] is None:
                                if self.grid[newy][newx] == 9:
                                    self.basin[newy][newx] = "X"
                                else:
                                    self.basin[newy][newx] = basinID
                                    self.basinDictionary[basinID] += 1
                                    newNodeList.append((newx, newy))
                            else:
                                print("Warning 2")
            nodeList = newNodeList

    def generateBasinMap(self):
        self.basin = [[None] * len(self.grid[0]) for i in range(len(self.grid))]
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == 9:
                    self.basin[y][x] = "X"
                    continue
                else:
                    if self.basin[y][x] is None:
                        self.generateSurroundingBasin(x, y)




    def checkMostDangerous(self, x, y):
        results = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                newx = x + dx
                newy = y + dy
                if (dx == 0 and dy == 0):
                    continue
                if (abs(dx) == abs(dy)):
                    continue
                if (newx >= 0 and newx < len(self.grid[0]) and newy >= 0 and newy < len(self.grid)):
                    results.append((newx, newy))
        smallest = self.grid[y][x]
        for nx,ny in results:
            if self.grid[ny][nx] <= smallest:
                return -5
        return self.grid[y][x]


def task1():
    board = Board()
    with open("09.txt") as f:
        for line in f:
            listy = list(line.strip())
            board.grid.append([int(x) for x in listy])

    totalSum = 0
    for y in range(len(board.grid)):
        for x in range(len(board.grid[y])):
            result = board.checkMostDangerous(x,y)
            if result > -4:
                result += 1
                totalSum += result
                print(f" Task 1 | Low Point: {(y,x)}, RiskLevel: {result}, Total Sum: {totalSum}")



def task2():
    board = Board()
    with open("09.txt") as f:
        for line in f:
            listy = list(line.strip())
            board.grid.append([int(x) for x in listy])

    board.generateBasinMap()
    for y in range(len(board.grid)):
        print("".join(str(x) for x in board.basin[y]))
    top3 = sorted(board.basinDictionary, key=board.basinDictionary.get, reverse=True)[:3]
    largest = 1
    for key in top3:
        largest *= board.basinDictionary.get(key)
    print(f" Task 1 | biggestBasin: {top3}, finalValue: {largest}")


task1()
task2()
