def readLines(file: str, parseB):
    with open(file) as f:
        ret = {}
        for num, line in enumerate(f):
            line = line.strip()
            key, values = line.split(":")
            key = key.strip()
            values = values.strip().split(" ")
            values = [int(x) for x in values if x != ""]
            ret[key] = values
        return list(zip(ret["Time"], ret["Distance"]))

def task1():
    tuples = readLines("06b.txt", False)
    races = []

    for time,dist in tuples:
        fasterDist = []
        for i in range(time + 1):
            distance = i * (time-i)
            if distance > dist:
                fasterDist.append((i, distance))
        races.append(fasterDist)
    bigger = [len(x) for x in races]
    final = 1
    for big in bigger:
        final *= big
    print(f" Task 1 | Ways to be faster: {final}")


def task2():
    tuples = readLines("06b.txt", False)
    races = []
    finalTime = ""
    finalDist = ""
    for time,dist in tuples:
        finalTime += str(time)
        finalDist += str(dist)
    finalTime = int(finalTime)
    finalDist = int(finalDist)
    fasterDist = []
    for i in range(finalTime + 1):
        distance = i * (finalTime-i)
        if distance > finalDist:
            fasterDist.append((i, distance))
    races.append(fasterDist)
    bigger = [len(x) for x in races]
    final = 1
    for big in bigger:
        final *= big
    print(f" Task 2 | Ways to be faster: {final}")


task1()
task2()