def readElements(file: str):
    monkeyList = []
    with open(file) as f:
        for num, line in enumerate(f):
            line = line.strip()
            if line.startswith("Monkey"):
                monkeyList.append(Monkey(len(monkeyList), [], 0, 0, 0))
            elif line.startswith("Starting"):
                items = line.split(":")[1]
                items = list(map(lambda x: int(x.strip()), items.split(",")))
                monkeyList[-1].items = items
            elif line.startswith("Operation"):
                operators = line.split("=")[1].strip()
                operators = operators.split(" ")
                monkeyList[-1].operator = operators[1]
                if operators[2] == "old":
                    monkeyList[-1].operatorValue = operators[2]
                else:
                    monkeyList[-1].operatorValue = int(operators[2])
            elif line.startswith("Test"):
                monkeyList[-1].testValue = int(line.strip("Test: divisible by "))
            elif line.startswith("If true"):
                monkeyList[-1].trueMonkey = int(line.strip("If true: throw to monkey "))
            elif line.startswith("If false"):
                monkeyList[-1].falseMonkey = int(line.strip("If false: throw to monkey "))

        for monkey in monkeyList:
            monkey.trueMonkey = monkeyList[monkey.trueMonkey]
            monkey.falseMonkey = monkeyList[monkey.falseMonkey]
        return monkeyList


class Monkey:
    def __init__(self, id, items,testValue, trueMonkey, falseMonkey):
        self.id = id
        self.items = items
        self.operator = "+"
        self.operatorValue = 0
        self.testValue = testValue
        self.trueMonkey = trueMonkey
        self.falseMonkey = falseMonkey
        self.inspectionCounter = 0

    def __repr__(self):
        return str(self.id)

    def doRound(self):
        for item in self.items:
            self.inspectionCounter += 1
            if self.operator == "+":
                newItem = item + self.operatorValue
            else:
                if self.operatorValue == "old":
                    newItem = item * item
                else:
                    newItem = item * self.operatorValue
           # newItem //= 3
            if newItem % self.testValue == 0:
                self.trueMonkey.items.append(newItem)
            else:
                self.falseMonkey.items.append(newItem)
        self.items = []


def task1():
    monkeys = readElements("11.txt")
    for round in range(1000):
        print(f"Round {round} started")
        for monkey in monkeys:
            monkey.doRound()

    monkeys.sort(key=lambda x: x.inspectionCounter)

    totalSignalStrength = monkeys[-1].inspectionCounter * monkeys[-2].inspectionCounter
    print(f" Task 1 | Monkey Ordering: {monkeys}, Monkey Buisness: {totalSignalStrength}")


def task2():
    instructions = readElements("10.txt")


task1()
task2()
