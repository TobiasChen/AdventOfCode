# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def task1():
    counter = 0
    otherCounter = 0
    with open("01.txt") as f:
        currentMeasure = int(f.readline())
        for line in f:
            line = int(line)
            if currentMeasure < line:
                counter += 1
            else:
                otherCounter += 1
            currentMeasure = line
    print("Task 1:", counter, otherCounter, counter + otherCounter)

def task2():
    slidingWindowOld = [None] * 3
    slidingWindowNew = [None] * 3
    counter = 0
    otherCounter = 0
    with open("01.txt") as f:
        for line in f:
            slidingWindowNew[0] = slidingWindowOld[1]
            slidingWindowNew[1] = slidingWindowOld[2]
            slidingWindowNew[2] = int(line)
            if None not in slidingWindowOld:
                if sum(slidingWindowOld) < sum(slidingWindowNew):
                    counter += 1
                else:
                    otherCounter += 1
            slidingWindowOld = slidingWindowNew.copy()
    print("Task 2:", counter, otherCounter, counter + otherCounter)


task1()
task2()
        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
