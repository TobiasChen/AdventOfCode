# This is a sample Python script.
import collections
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def task1():
    with open("06.txt") as f:
        inputLifeExpectancy = [int(i) for i in f.readline().strip("\n").split(",")]

    for i in range(80):
        appendList = []
        for j, elemt in enumerate(inputLifeExpectancy):
            inputLifeExpectancy[j] = elemt - 1
            if inputLifeExpectancy[j] < 0:
                inputLifeExpectancy[j] = 6
                appendList.append(8)
        inputLifeExpectancy.extend(appendList)
    print(f" Task 1, Day: {80}, NumberOfAnimals: {len(inputLifeExpectancy)}")

def task2():
    with open("06.txt") as f:
        inputLifeExpectancy = [int(i) for i in f.readline().strip("\n").split(",")]

    counter = collections.Counter(inputLifeExpectancy)
    newList = [0] * 9
    for k,v in counter.items():
        newList[int(k)] = v

    for i in range(256):
        new6 = 0
        new8 = 0
        for num, val in enumerate(newList):
            if num == 0:
                new6 = val
                new8 = val
            if num == 8:
                newList[num] = new8
            else:
                newList[num] = newList[num+1]
        newList[6] += new6
    print(f" Task 1, Day: {256}, NumberOfAnimals: {sum(newList)}")


#Task 2
task1()
task2()

