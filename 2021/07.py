def task1():
    with open("07.txt") as f:
        inputPositions = [int(i) for i in f.readline().strip("\n").split(",")]

    print(f" Task 1 | NumberOfAnimals: {inputPositions[0]}, Fuel Spent")

def task2():
    0


task1()
task2()

