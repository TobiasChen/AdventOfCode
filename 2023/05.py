def readLines(file: str, parseB):
    listOfLines = []
    keys = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    maps = {x: [] for x in keys}
    seeds = []
    idx = "seeds"

    with open(file) as f:
        for num, line in enumerate(f):
            line = line.strip()
            match line:
                case "seed-to-soil map:":
                    idx = "soil"
                case "soil-to-fertilizer map:":
                    idx = "fertilizer"
                case "fertilizer-to-water map:":
                    idx = "water"
                case "water-to-light map:":
                    idx = "light"
                case "light-to-temperature map:":
                    idx = 'temperature'
                case "temperature-to-humidity map:":
                    idx = "humidity"
                case "humidity-to-location map:":
                    idx = "location"
                case _:
                    if not line:
                        continue
                    else:
                        line = line.split(" ")
                        if idx == "seeds":
                            currentSeed = -1
                            for item in line:
                                if item.strip() == "seeds:" or (not item and item != 0):
                                        continue
                                if parseB:
                                    if currentSeed == -1:
                                        currentSeed = int(item)
                                    else:
                                        seeds.append((currentSeed, int(item)))
                                        currentSeed = -1
                                else:
                                    seeds.append(int(item))
                        else:
                            line = [int(x) for x in line]
                            if parseB:                
                                maps[idx].append((line[0], line[1], line[2]))
                            else:
                                maps[idx].append((line[1], line[1] + line[2] -1, line[0]))
    for key in keys:
        maps[key].sort(key=lambda x: x[0])
        additions = []
        if parseB:
            prevHigh = None
            for item in maps[key]:
                if prevHigh == None and item[0] != 0:
                    additions.append((0,0,item[0]))
                    prevHigh = item[0] - 1
                if prevHigh:
                    diff = item[0] - prevHigh
                    if diff > 1:
                        additions.append((prevHigh, prevHigh, diff))
                    elif diff == 1:
                        print(f"Clean border between {prevHigh} and {item}")
                    else:
                        print(f"Overlap detected between {prevHigh} and {item}")
                prevHigh = item[0] + item[2] - 1
        maps[key].extend(additions)
        maps[key].sort(key=lambda x: x[0])
    return (keys,maps,seeds)

def findMapping(key,maps,seed):
        value = seed
        for low,high, target in maps[key]:
            if value < low:
                return value
            elif low <= value <= high:
                diff = value - low
                return target + diff
        return value

def task1():
    keys,maps,seeds = readLines("05b.txt", False)
    finals = []
    for i,seed in enumerate(seeds):
        finals.append([seed])
        for key in keys:
            currentVal = findMapping(key, maps,finals[i][-1])
            finals[i].append(currentVal)

    lowest = min(finals, key=lambda x: x[-1])
    lowestLocation = lowest[-1]
    print(f" Task 1 | Lowest Lcation: {lowestLocation}")
#def weirdSort(a,b):
def findTargets(beginning, length, nexKeyMap):
    targets=[]
    for target, src, rangeY in nexKeyMap:
        if target <= beginning + length - 1:
            if target + rangeY -1 < beginning:
                continue

            elif beginning <= target + rangeY -1:
                smallestEnd = min(target + rangeY -1 , beginning + length -1)
                biggestStart = max(target, beginning)
                startDIff = beginning - target
                endDIff = smallestEnd - biggestStart + 1
                if startDIff > 0:
                    targets.append((biggestStart, src + startDIff, endDIff))
                else:
                    targets.append((biggestStart, src, endDIff))
            else:
                print(f"MAYDAY {(beginning,length)} and {(target,src,rangeY)}") 
        else: 
            break
    if not targets:
            print(f"Didnt find a match, creating new entry for {beginning}/{nexKeyMap[-1][0] + nexKeyMap[-1][2]}")
            target = nexKeyMap[-1][0] + nexKeyMap[-1][2]
            src = target
            rangeY = beginning - target + length
            targets.append((target,),(beginning, src, rangeY))
    return targets


def task2():
    keys,maps,seeds = readLines("05a.txt", True)
    finals = []
    keys.reverse()
    for i,key in enumerate(keys):
        newMap =[]
        if key == "soil":
            continue
        for item in maps[key]:
            newMap.extend(findTargets(item[1],item[2], maps[keys[i+1]]))
        thirdMap = []
        for j,item in enumerate(newMap):
            if j == 0: 
                thirdMap.append([item])
                continue
            prevItem = newMap[j-1]
            if item[0] == prevItem[0] + prevItem[2] and item[1] == prevItem[1] + prevItem[2]:
                thirdMap[-1].append(item)
            else:
                thirdMap.append([item])
        fourthMap = []
        for lis in thirdMap:
            len = None
            for item in lis:
                if len == None:
                     len = item[2]
                else:
                    len += item[2]
            fourthMap.append((lis[0][0], lis[0][1], len))
        #fourthMap.sort(key=lambda x: x[0])
        maps[keys[i+1]] = fourthMap
    print("test")

    print(f" Task 2 | Lowest Lcation: {lowestLocation}")
"""     for i,seed in enumerate(seeds):
        print(f"({i + 1}/{len(seeds)})Testing Seed {seed[0]} with range {seed[1]}")
        for actualSeed in range(seed[0], seed[0] + seed[1] + 1):
            finals.append([actualSeed])
            for key in keys:
                currentVal = findMapping(key, maps,finals[-1][-1])
                finals[-1].append(currentVal)

    lowest = min(finals, key=lambda x: x[-1])
    lowestLocation = lowest[-1] """


task1()
task2()