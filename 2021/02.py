def task1():
    forward = 0
    depth = 0
    with open("02.txt") as f:
        for line in f:
            command, value = line.split(" ")
            value = int(value)
            match command:
                case "down":
                    depth += value
                case "up":
                    depth -= value
                case "forward":
                    forward += value
    print(f"Task 1| Forward: {forward}, Depth: {depth}, Final: {forward * depth}")

def task2():
    forward = 0
    depth = 0
    aim = 0
    with open("02.txt") as f:
        for line in f:
            command, value = line.split(" ")
            value = int(value)
            match command:
                case "down":
                    aim += value
                case "up":
                    aim -= value
                case "forward":
                    forward += value
                    depth += aim * value
    print(f"Task 2| Forward: {forward}, Depth: {depth}, Aim: {aim}, Final: {forward * depth}")


task1()
task2()