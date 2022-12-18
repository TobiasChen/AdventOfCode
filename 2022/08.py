def readElements(file: str):
    with open(file) as f:
        grid = []
        for num, line in enumerate(f):
            line = line.strip()
            grid.append([int(x) for x in line])
    return grid


def checkDirection(x, y, dx, dy, grid):
    if dx != 0:
        length = len(grid[y])
    else:
        length = len(grid)
    for i in range(1, length):
        newX = x + dx * i
        newY = y + dy * i
        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            return True
        if grid[newY][newX] >= grid[y][x]:
            return False


def checkDirections(x, y, grid, visible):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if abs(dx) == abs(dy):
                continue
            if checkDirection(x, y, dx, dy, grid):
                test = [[None, "Rigt", "Left"], ["Down"], ["Up"]]
                visible[y][x] = test[dy][dx]
                return


def getDirectionScore(x, y, dx, dy, grid):
    visionScore = 0
    if dx != 0:
        length = len(grid[y])
    else:
        length = len(grid)
    for i in range(1, length):
        newX = x + dx * i
        newY = y + dy * i
        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            return visionScore
        else:
            visionScore += 1
            if grid[newY][newX] >= grid[y][x]:
                return visionScore
    return visionScore


def getScore(x, y, grid):
    totalScore = 1
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if abs(dx) == abs(dy):
                continue
            visionScore = getDirectionScore(x, y, dx, dy, grid)
            if visionScore == 0:
                return 0
            else:
                totalScore *= visionScore
    return totalScore


def task1():
    grid = readElements("08.txt")
    visible = [[None] * len(grid[0]) for i in range(len(grid))]
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if x == 0 or x == len(row) - 1 or y == 0 or y == len(grid) - 1:
                visible[y][x] = "Edge"
            else:
                checkDirections(x, y, grid, visible)

    visibleTres = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if visible[y][x]:
                visibleTres += 1

    print(f" Task 1 | Total trees: {len(grid) * len(grid[0])}, Number of Trees: {visibleTres}")


def task2():
    grid = readElements("08.txt")
    scenicScore = [[0] * len(grid[0]) for i in range(len(grid))]
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            scenicScore[y][x] = getScore(x, y, grid)

    maxScore = max(max(x) for x in scenicScore)
    print(f" Task 2 | TotalTrees : {len(grid) * len(grid[0])}, Optimal Scenic Score: {maxScore}")


task1()
task2()
