import collections
from itertools import groupby

def testLineForCorruption(stri):
    opening = ['{', '(', '[', '<']
    closing = ['}', ')', ']', '>']

    stack = []
    for num,char in enumerate(stri):
        if char in opening:
            stack.append(char)
        elif char in closing:
            element = stack.pop()
            if closing[opening.index(element)] != char:
                return num, char
        else:
            print("Warning")
    return None

def testLineForCorruptionAndRepair(stri):
    opening = ['{', '(', '[', '<']
    closing = ['}', ')', ']', '>']

    stack = []
    for num,char in enumerate(stri):
        if char in opening:
            stack.append(char)
        elif char in closing:
            element = stack.pop()
            if closing[opening.index(element)] != char:
                return None
        else:
            print("Warning")
    result = ""
    while stack:
        el = stack.pop()
        result += closing[opening.index(el)]
    return result

def task1():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    corruptedLines = []
    with open("10.txt") as f:
        for num, line in enumerate(f):
            listy = list(line.strip())
            lineResult = testLineForCorruption(listy)
            if lineResult:
                corruptedLines.append((num, lineResult[0], lineResult[1]))

    sumPoints = 0
    for line in corruptedLines:
        sumPoints += points.get(line[2])

    print(f" Task 1 | Number of lines: {len(points)}, Score: {sumPoints}")



def task2():
    points = {')': 1, ']': 2, '}': 3, '>': 4}
    fixedStrings = []
    with open("10.txt") as f:
        for num, line in enumerate(f):
            listy = list(line.strip())
            lineResult = testLineForCorruptionAndRepair(listy)
            if lineResult:
                fixedStrings.append(lineResult)

    scores = []
    for num, line in enumerate(fixedStrings):
        scores.append(0)
        for char in line:
            scores[num] *= 5
            scores[num] += points.get(char)
    scores.sort()
    print(f" Task 2 | NumberOfScores: {len(scores)} FinalScore: {scores[(len(scores) - 1) // 2]}")

task1()
task2()
