test = False


def createMap(pageOrder):
    ruleMap = {}
    for order in pageOrder:
        ruleMap[order[1]] = ruleMap.get(order[1], []) + [order[0]]

    return ruleMap


def prepInput(path):
    rules = True
    pageOrder = []
    tasks = []
    lines = open(path, 'r').readlines()
    for line in lines:
        line = line.strip()
        if line:
            if rules:
                pageOrder.append([int(x) for x in line.strip().split("|")])
            else:
                tasks.append([int(x) for x in line.strip().split(",")])
        else:
            rules = False
    return pageOrder, tasks


def isValid(task, numbersWithBefore):
    for i, num in enumerate(task):
        afterList = task[i + 1:]
        for val in numbersWithBefore.get(num, []):
            if val in afterList:
                return False
    return True


def fixPages(task, numbersWithBefore, isRecursive=False):
    for i, num in enumerate(task):
        afterList = task[i + 1:]
        for val in numbersWithBefore.get(num, []):
            if val in afterList:
                truncatedAfterList = task[i:].copy()
                truncatedAfterList.remove(val)
                reorderdAfterList = [val] + truncatedAfterList
                newTaskOrder = task[:i] + fixPages(reorderdAfterList, numbersWithBefore, isRecursive=True)
                if isRecursive:
                    return newTaskOrder
                else:
                    return newTaskOrder[len(newTaskOrder) // 2]

    if (isRecursive):
        return task
    else:
        return 0


def one(path: str):
    pageOrder, tasks = prepInput(path)
    numbersWithBefores = createMap(pageOrder)

    summedPageNumbers = 0
    for task in tasks:
        if isValid(task, numbersWithBefores):
            summedPageNumbers += task[(len(task) // 2)]

    print(f"Final Task One: {summedPageNumbers}")


def two(path: str):
    pageOrder, tasks = prepInput(path)
    numbersWithBefores = createMap(pageOrder)

    summedPageNumbers = 0
    for task in tasks:
        summedPageNumbers += fixPages(task, numbersWithBefores)

    print(f"Final Task Two: {summedPageNumbers}")


def main():
    current = __file__.strip('.py')
    if test:
        one(current + "a.txt")
        two(current + "a.txt")
    else:
        print("Calling Toby")
        one(current + "b.txt")
        two(current + "b.txt")
        print("Calling Freya")
        one(current + "c.txt")
        two(current + "c.txt")


main()
