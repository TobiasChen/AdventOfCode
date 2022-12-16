from functools import total_ordering


@total_ordering
class Element:
    listOfElements = [["A", "X"], ["B", "Y"], ["C", "Z"]]
    points = [1, 2, 3]

    def __repr__(self):
        return str(self.id)

    def __init__(self, inp):
        self.id = None
        for count, lis in enumerate(self.listOfElements):
            if inp in lis:
                self.id = count
                break
        if self.id is None:
            raise Exception("Unkown Input")
        self.point = self.points[self.id]

    def giveMatchingElement(self, inputId):
        newElements = []
        for listy in self.listOfElements:
            newElements.append(Element(listy[0]))
        newElements.sort(key=lambda el: ((el > self) - (el < self)))
        return newElements[inputId]

    def __eq__(self, other):
        return other.id == self.id

    def __lt__(self, other):
        if self.id == (len(self.listOfElements) - 1) and other.id == 0:
            return True
        if self.id == 0 and other.id == len(self.listOfElements) - 1:
            return False
        else:
            return self.id < other.id


def readElements(file: str):
    listOfElements = []
    with open(file) as f:
        for num, line in enumerate(f):
            line = line.split(" ")
            listOfElements.append([])
            for strin in line:
                strin = strin.strip()
                listOfElements[num].append(Element(strin))
    return listOfElements


def task1():
    elements = readElements("02.txt")
    points = 0
    for listy in elements:
        points += listy[1].point
        if listy[0] == listy[1]:
            points += 3
        elif listy[0] < listy[1]:
            points += 6


def task2():
    elements = readElements("02.txt")
    for listy in elements:
        listy[1] = listy[0].giveMatchingElement(listy[1].id)

    points = 0
    for listy in elements:
        points += listy[1].point
        if listy[0] == listy[1]:
            points += 3
        elif listy[0] < listy[1]:
            points += 6
    print(f" Task 2 | Games played: {len(elements)}, Total Points: {points}")


task1()
task2()
