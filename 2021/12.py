class Octopus:
    def __init__(self, energyLevel):
        self.hasFlashed = False
        self.energyLevel = energyLevel

    def __repr__(self):
        return str(self.energyLevel)


class Board:
    def __init__(self):
        self.grid = []
        self.flashCounter = []

    def checkAllFlashed(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if not self.grid[y][x].hasFlashed:
                    return False
        return True

    def runSimulation(self, steps):
        #self.printBoard(0)
        for i in range(steps):
            flashList = self.increaseEnergy()
            self.simulateFlashes(i, flashList)
            self.resetEnergy()
            #self.printBoard(i + 1)

    def runSimulationContinously(self):
        count = 0
        while True:
            flashList = self.increaseEnergy()
            self.simulateFlashes(count, flashList)
            if self.checkAllFlashed():
                return count
            self.resetEnergy()
            count += 1
    def printBoard(self, step):
        print(f"After Step {step}:")
        if(step > 0):
            print(f"Flash counter {self.flashCounter[step - 1]}")
        for y in range(len(self.grid)):
            print(" ".join(str(x.energyLevel) for x in self.grid[y]))

    def increaseEnergy(self):
        flashList = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                self.grid[y][x].energyLevel += 1
                if self.grid[y][x].energyLevel > 9:
                    self.grid[y][x].hasFlashed = True
                    flashList.append((x, y))
        return flashList

    def simulateFlashes(self, step, flashList):
        self.flashCounter.append(0)
        while flashList:
            newFlashList = []
            for flash in flashList:
                self.flashCounter[step] += 1
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        newX = flash[0] + dx
                        newY = flash[1] + dy
                        if dx == 0 and dy == 0:
                            continue
                        if 0 <= newX < len(self.grid[0]) and 0 <= newY < len(self.grid):
                            self.grid[newY][newX].energyLevel += 1
                            if self.grid[newY][newX].energyLevel > 9 and not self.grid[newY][newX].hasFlashed:
                                self.grid[newY][newX].hasFlashed = True
                                newFlashList.append((newX, newY))
            flashList = newFlashList

    def resetEnergy(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x].hasFlashed:
                    self.grid[y][x].energyLevel = 0
                    self.grid[y][x].hasFlashed = False


def task1():
    board = Board()
    steps = 100
    with open("11.txt") as f:
        for num, line in enumerate(f):
            board.grid.append([])
            line = line.strip()
            for char in line:
                board.grid[num].append(Octopus(int(char)))

    board.runSimulation(steps)
    sumFlashes = 0
    for flash in board.flashCounter:
        sumFlashes += flash

    print(f" Task 1 | Steps: {steps}, Number of Flashes: {sumFlashes}")


def task2():
    board = Board()
    with open("11.txt") as f:
        for num, line in enumerate(f):
            board.grid.append([])
            line = line.strip()
            for char in line:
                board.grid[num].append(Octopus(int(char)))

    allFlashedTurn = board.runSimulationContinously()
    sumFlashes = 0
    for flash in board.flashCounter:
        sumFlashes += flash

    print(f" Task 1 | Steps: {allFlashedTurn + 1}, Number of Flashes: {sumFlashes}")


task1()
task2()
