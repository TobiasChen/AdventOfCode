import os

here = os.path.dirname(os.path.abspath(__file__))


def readLines(file: str):
    listOfLines = []
    with open(file) as f:
        for num, line in enumerate(f):
            numbers, winnings = line.split("|")
            id,numbers = numbers.split(":")
            id = id.split(" ")[1]
            numbers = [int(x) for x in numbers.strip().split(" ") if x or x == 0]
            winnings =  [int(x) for x in winnings.strip().split(" ") if x or x == 0]
            listOfLines.append([id,numbers, winnings,1])
    return listOfLines


def task1():
    lines = readLines("04a.txt")
    points = 0
    for line in lines:
        value = 0
        for num in line[1]:
            if num in line[2]:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        points += value
    print(f" Task 2 | Games played: {len(lines)}, Total Points: {points}")

def task2():
    lines = readLines("04a.txt")
    points = 0
    for i, line in enumerate(lines):
        value = 0
        for num in line[1]:
            if num in line[2]:
                value +=1
        maxIndex = min(i + value, len(lines) -1)
        for i in range(i + 1, maxIndex + 1):
            lines[i][3] += 1 * line[3]
    points = sum([x[3] for x in lines])
    print(f" Task 2 | Games played: {len(lines)}, Total Points: {points}")

task1()
task2()