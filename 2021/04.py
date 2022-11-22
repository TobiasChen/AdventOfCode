from itertools import compress
class Board:
    def __init__(self):
        self.boardsize = 5
        self.grid = []
        self.marked = [[False] * 5 for i in range(self.boardsize)]

    def markValue(self, value):
        newlyMarked = []
        for y, row in enumerate(self.grid):
            for x, column in enumerate(row):
                if column == value:
                    newlyMarked.append((y, x))

        for tuples in newlyMarked:
            self.marked[tuples[0]][tuples[1]] = True

        for tuples in newlyMarked:
            columnList = [row[tuples[1]] for row in self.marked]
            #Rows
            if all(self.marked[tuples[0]]):
                return True
            #Columns
            elif all(columnList):
                return True
            else:
                return False

def calculateScore(board, lastCalledValue):
    score = 0
    for i in range(board.boardsize):
        score += sum([i for (i, v) in zip(board.grid[i], board.marked[i]) if not v])
    return score * lastCalledValue

def runGame(randomValues, listOfBoards):
    for x in randomValues:
        for i, board in enumerate(listOfBoards):
            if board.markValue(x):
                score = calculateScore(board, x)
                print(f"Task 1 | Value: {x}, Board: {i}, Score: {score}")
                return
def task1():
    listOfBoards = []

    with open("04.txt") as f:
        randomValues = [int(i) for i in f.readline().strip("\n").split(",")]
        currentBoard = None
        for num, line in enumerate(f):
            if num % 6 == 0:
                currentBoard = Board()
                listOfBoards.append(currentBoard)
            else:
                currentBoard.grid.append([int(i) for i in line.strip("\n").split()])

    runGame(randomValues,listOfBoards)


def runGame2(randomValues, listOfBoards):
    for x in randomValues:
        listOfBoardsToRemove = []
        for i, board in enumerate(listOfBoards):
            if board.markValue(x):
                if len(listOfBoards) == 1:
                    score = calculateScore(board, x)
                    print(f"Task 1 | Value: {x}, Board: {i}, Score: {score}")
                    return
                else:
                    listOfBoardsToRemove.append(i)
        listOfBoards = [v for i, v in enumerate(listOfBoards) if i not in listOfBoardsToRemove]



def task2():
    listOfBoards = []

    with open("04.txt") as f:
        randomValues = [int(i) for i in f.readline().strip("\n").split(",")]
        currentBoard = None
        for num, line in enumerate(f):
            if num % 6 == 0:
                currentBoard = Board()
                listOfBoards.append(currentBoard)
            else:
                currentBoard.grid.append([int(i) for i in line.strip("\n").split()])

    runGame2(randomValues, listOfBoards)


task1()
task2()
