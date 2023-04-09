def readElements(file: str):
    with open(file) as f:
        grid = []
        for num, line in enumerate(f):
            line = line.strip()
            grid.append([])
            for pos, char in enumerate(line):
                grid[num].append(Node(pos,num,char))
    return grid

class Node:
    def __init__(self, x: int, y: int, ident: str):
        self.x = x
        self.y = y
        self.height = self.setId(ident)
        self.visited = False
        self.start = ident == "S"
        self.start2 = ident == "S" or ident == "a"
        self.end = ident == "E"
        self.distance = 0

    def setId(self, ident: str):
        if ident == "S": 
            return 0
        elif ident == "E":
            return 25
        else:
            return ord(ident) - 97


    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return f"({self.x}x{self.y}x{self.height} - {self.distance} |V:{self.visited},S:{self.start},S2:{self.start2},E:{self.end}) "

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def getNeighbour(currentX: int, currentY: int,  grid):
    currentPoint = grid[currentY][currentX]
    validNeighbours = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if abs(dx) == abs(dy):
                continue
            newx = currentX + dx
            newy = currentY + dy
            if 0 <= newx < len(grid[0]) and 0 <= newy < len(grid):
                newNode = grid[newy][newx]
                if not newNode.visited:
                    if newNode.height - currentPoint.height <= 1:
                        validNeighbours.append(newNode)
    return validNeighbours


def findShortesPath(grid, source):
    #BFS:   
    queue = []
    print(f"Source: {source}")
    queue.append(grid[source.y][source.x])
    source.visited = True
    while (queue):
        node = queue.pop(0)
        if (node.end):
            return node
        for neighbour in getNeighbour(node.x, node.y, grid):
            neighbour.distance = node.distance + 1
            neighbour.visited = True
            queue.append(neighbour)


def task1():
    grid = readElements("12.txt")
    source = False
    for row in grid:
        for node in row:
            if node.start:
                source = node
                break

    target = findShortesPath(grid, source)

    print(f"Task 1 | Grid Size: {len(grid)}x{len(grid[0])}, Node: {target}")


def task2():
    grid = readElements("12.txt")
    listOfSource = []
    for row in grid:
        for node in row:
            if node.start2:
                listOfSource.append(node)

    print(f"Task 2 | Number of Sources: {len(listOfSource)}")
    listOfTargets = []
    for source in listOfSource:
        node = findShortesPath(grid, source)
        if node:
            listOfTargets.append(node.distance)
        for row in grid:
            for node in row:
                node.visited = False
                node.distance = 0
    print(listOfTargets)
    listOfTargets.sort()

    print(f"Task 2 | Grid Size: {len(grid)}x{len(grid[0])}, Node: {listOfTargets[0]}")



task1()
task2()
