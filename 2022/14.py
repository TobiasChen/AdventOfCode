from functools import reduce
def readElements(file: str):
    with open(file) as f:
        edges = []
        for num, line in enumerate(f):
            line = line.strip()
            line = line.split(" -> ")
            points = [[int(j) for j in i.split(",")] for i in line]
            print(points)
            points = list(map(lambda x: Point(x[0],x[1]), points))
            firstPoint = points[0]
            for point in points[1:]:
                edges.append(Edge(firstPoint, point))
                firstPoint = point
    return edges

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return f"({self.x}x{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Edge:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2
        self.vertical = self.testVertical()
        self.reorderPoints()

    def testVertical(self):
        if self.point1.x - self.point2.x == 0:
            return True
        elif self.point1.y - self.point2.y == 0:
            return False
        else:
            print("Queer Edge detected: {self}")
    
    def reorderPoints(self):
        if self.vertical:
            if self.point1.y > self.point2.y:
                p = self.point1
                self.point1 = self.point2
                self.point2 = p
        else:
            if self.point1.x > self.point2.x:
                p = self.point1
                self.point1 = self.point2
                self.point2 = p
    
    def __repr__(self):
        return f"{self.point1}-{self.point2}"


class Map:
    def __init__(self):
        self.grid = [[0]]
        self.operatorList = []

    def adjustGridSize(self, point: Point):
        if point.x > len(self.grid[0]) - 1:
            missingColumns = point.x - len(self.grid[0]) + 3
            for row in self.grid:
                row += [0] * missingColumns
        if point.y > len(self.grid) - 1:
            missingRows = point.y - len(self.grid) + 1
            self.grid += [[0 for x in range(len(self.grid[0]))] for i in range(missingRows)]

    def addEdge(self, edge: Edge):
        self.adjustGridSize(edge.point1)
        self.adjustGridSize(edge.point2)
        if edge.vertical:
            for row in self.grid[edge.point1.y:edge.point2.y+1]:
                row[edge.point1.x] = 1
        else:
            self.grid[edge.point1.y][edge.point1.x:edge.point2.x+1] = [1] * (edge.point2.x + 1 - edge.point1.x)
    
def runSandCalculations(rockMap: Map, startPoint: Point):
    sandCounter = 0
    stepCounterList = []
    
    while(True):
        #Produce New Sand:
        trueStart = Point(startPoint.x, startPoint.y)
        sandCounter += 1
        finished, stepCounter, lastSandPos = dropSand(rockMap, trueStart)
        stepCounterList.append(stepCounter)
        iterations = 2000000
        if sandCounter > iterations:
            print(f"Canceling after {iterations}")
            return (sandCounter, stepCounterList, lastSandPos)
        if finished:
            print(f"Sandgrain {sandCounter} started falling after {stepCounter} steps from {lastSandPos}")
            return (sandCounter, stepCounterList, lastSandPos)
        else:
            if(iterations % 1000 == 0):
                print(f"Sandgrain {sandCounter} came to Rest after {stepCounter} steps at {lastSandPos}")


def dropSand(rockMap: Map, startPoint: Point):
    #print("Dropping Sand at", startPoint)
    stepCounter = 0
    currentSandPos = Point(startPoint.x, startPoint.y)
    while(True):
        #print(f"Sand: {sandCounter}, Step: {stepCounterList[-1]}")
        if(currentSandPos.y == len(rockMap.grid) - 1):
            return (True, stepCounter, currentSandPos)
        elif(rockMap.grid[startPoint.y][startPoint.x]):
            return (True, stepCounter, currentSandPos)
        stepCounter += 1
        if rockMap.grid[currentSandPos.y + 1][currentSandPos.x] == 0:
            currentSandPos.y += 1
        elif rockMap.grid[currentSandPos.y + 1][currentSandPos.x - 1] == 0:
            currentSandPos.y += 1
            currentSandPos.x -= 1
        elif rockMap.grid[currentSandPos.y + 1][currentSandPos.x + 1] == 0:
            currentSandPos.y += 1
            currentSandPos.x += 1    
        else:
            rockMap.grid[currentSandPos.y][currentSandPos.x] = 2
            return (False, stepCounter, currentSandPos)


def task1():
    edges = readElements("14.txt")
    rockMap = Map()
    for edge in edges:
        rockMap.addEdge(edge)
    
    StartPoint = Point(500,0)
    sandCounter, stepCounterList, lastSandPos = runSandCalculations(rockMap, StartPoint)
    totalSteps = reduce(lambda x, last: x+last, stepCounterList[:-1])
    header = [i for i in range(0,20)]
    for i,row in enumerate(rockMap.grid):
        print(f"{i} {row[490:510]}")
    print(f"Task 1 | Grid Size: {len(rockMap.grid)}x{len(rockMap.grid[0])}, TotalSteps: {totalSteps}, Number of settled Grains: {sandCounter - 1}")


def task2():
    edges = readElements("14.txt")
    rockMap = Map()
    for edge in edges:
        rockMap.addEdge(edge)
    
    missingColumns = len(rockMap.grid) * 2
    print("")
    for row in rockMap.grid:
        row += [0] * missingColumns
    rockMap.grid += [[0 for x in range(len(rockMap.grid[0]))] for i in range(1)]
    rockMap.grid += [[1 for x in range(len(rockMap.grid[0]))] for i in range(1)]

    for i,row in enumerate(rockMap.grid):
        print(f"{i} {row[490:510]}")

    StartPoint = Point(500,0)
    sandCounter, stepCounterList, lastSandPos = runSandCalculations(rockMap, StartPoint)
    totalSteps = reduce(lambda x, last: x+last, stepCounterList[:-1])
    header = [i for i in range(0,20)]
   # for i,row in enumerate(rockMap.grid):
   #     print(f"{i} {row[490:510]}")
    print(f"Task 2 | Grid Size: {len(rockMap.grid)}x{len(rockMap.grid[0])}, TotalSteps: {totalSteps}, Number of settled Grains: {sandCounter - 1}")




task1()
task2()
