def readElements(file: str):
    with open(file) as f:
        instructions = []
        for num, line in enumerate(f):
            line = line.strip()
            instructions.append(line.split(" "))
        return instructions


class CPU:
    def __init__(self):
        self.register = 1
        self.crtOutput = [[]]
        self.clock = 0
        self.signalStrength = []
        self.relevantCycles = [40 + 40 * x for x in range(6)]

    def advanceClock(self):
        self.clock += 1
        if self.clock - 1 in self.relevantCycles:
            self.crtOutput.append([])
            self.signalStrength.append((self.clock, self.register, self.clock * self.register))
        if -1 <= self.clock % 40 -1 - self.register <= 1:
            self.crtOutput[-1].append("#")
        else:
            self.crtOutput[-1].append(".")

def task1():
    instructions = readElements("10.txt")
    cpu = CPU()
    for instruction in instructions:
        if instruction[0] == "noop":
            cpu.advanceClock()
        elif instruction[0] == "addx":
            cpu.advanceClock()
            cpu.advanceClock()
            cpu.register += int(instruction[1])

    totalSignalStrength = sum([x[2] for x in cpu.signalStrength])
    print(f" Task 1 | Total instructions: {len(instructions)}, TotalSignalStrength: {totalSignalStrength}")


def task2():
    instructions = readElements("10.txt")
    cpu = CPU()
    for instruction in instructions:
        if instruction[0] == "noop":
            cpu.advanceClock()
        elif instruction[0] == "addx":
            cpu.advanceClock()
            cpu.advanceClock()
            cpu.register += int(instruction[1])


    print(f" Task 2 | Total instructions: {len(instructions)}, Final image")
    for line in cpu.crtOutput:
        print("".join(line))



task1()
task2()
