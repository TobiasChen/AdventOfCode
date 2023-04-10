from functools import cmp_to_key

def readElements(file: str):
    with open(file) as f:
        signals = []
        signals.append([])
        currentIndex = 0
        currentNumber = ""
        for num, line in enumerate(f):
            line = line.strip()
            if not line:
                currentIndex += 1
                signals.append([])
            else:
                stackOfLineIndeces = []
                for pos, char in enumerate(line):
                    if pos == 0:
                        if not char == "[":
                            print("ALARM!!!!!!", line)
                            currentStr = None
                        else:
                            currentStr = []
                            stackOfLineIndeces.   append(0)
                    else:
                        if char == "[":
                            if currentNumber: 
                                deep_set(currentStr, int(currentNumber), *stackOfLineIndeces)
                                stackOfLineIndeces[-1] += 1
                                currentNumber = ""
                            deep_set(currentStr, [], *stackOfLineIndeces)
                            stackOfLineIndeces.append(0)
                        elif char == "]":
                            if currentNumber: 
                                deep_set(currentStr, int(currentNumber), *stackOfLineIndeces)
                                stackOfLineIndeces[-1] += 1
                                currentNumber = ""
                            stackOfLineIndeces.pop()
                            if stackOfLineIndeces:
                               stackOfLineIndeces[-1] +=1
                        elif char == ",":
                            if currentNumber:
                                deep_set(currentStr, int(currentNumber), *stackOfLineIndeces)
                                stackOfLineIndeces[-1] += 1
                                currentNumber = ""
                        else:
                            currentNumber += char
                signals[currentIndex].append(currentStr)
    return signals

def deep_set(lst, value, *indices):
    for i in indices[:-1]:
        lst = lst[i]
    if indices[-1] == len(lst):
        lst.append(value)
    lst[indices[-1]] = value

def compareSignals(sig1, sig2):
    if isinstance(sig1, int) and isinstance(sig2, int):
        #print(f" 1 Comparing {sig1} and {sig2}, returning: {(sig1 < sig2) - (sig1 > sig2)}")
        return (sig1 < sig2) - (sig1 > sig2)
    elif isinstance(sig1, int) and not isinstance(sig2, int):
        return compareSignals([sig1], sig2)
    elif not isinstance(sig1, int) and isinstance(sig2, int):
        return compareSignals(sig1,[sig2])
    else:
        for i in range(min(len(sig1),len(sig2))):
            result = compareSignals(sig1[i],sig2[i])
            if result != 0:
                #print(f" 2 Comparing {sig1} and {sig2}, returning: {result}")
                return result
        #print(f" 3 Comparing {sig1} and {sig2}, returning: {(len(sig1) < len(sig2)) - (len(sig1) > len(sig2))}")
        return (len(sig1) < len(sig2)) - (len(sig1) > len(sig2))

def task1():
    signals = readElements("13.txt")
    resultList = []
    for signal in signals:
        result = compareSignals(signal[0], signal[1])
        if result != 0 and not None:
            #print("Signal: ", signal, result)
            resultList.append(result)
        else:
            print("Uncomparable Signal detected:", signal )
    resultSum = 0
    for i, val in enumerate(resultList):
        #print(i,val)
        if val > 0:
            resultSum += i + 1
    print(f"Task 1 | Result Size: {len(resultList)}, CorrectValues: {resultSum}")

def task2():
    signals = readElements("13.txt")
    newSignals = []
    resultList = []
    div1 = [[2]]
    div2 = [[6]]
    newSignals.append(div1)
    newSignals.append(div2)
    for signal in signals:
        newSignals.append(signal[0])
        newSignals.append(signal[1])
    print("-------")
    newSignals.sort(key=cmp_to_key(compareSignals), reverse = True)
    resultSum = 0
    #for sig in newSignals:
        #print(sig)
    res = (newSignals.index(div1) + 1) * (newSignals.index(div2) + 1)

    print(f"Task 2 | Result: {res}")

task1()
task2()
