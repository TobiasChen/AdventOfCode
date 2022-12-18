class File:
    def __init__(self, name, fileSize):
        self.name = name
        self.fileSize = fileSize

    def __repr__(self):
        return f"{self.name}:{self.fileSize}"


class Directory:
    def __init__(self, parent, name):
        self.listOfSubDirs: list[Directory] = []
        self.listOfFiles: list[File] = []
        self.totalSize = 0
        self.fileSize = 0
        self.parent = parent
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def addSub(self, dire):
        self.listOfSubDirs.append(dire)

    def addFile(self, file: File):
        self.listOfFiles.append(file)
        self.fileSize += file.fileSize

    def getDirSize(self):
        totalSize = 0
        for d in self.listOfSubDirs:
            totalSize += d.getDirSize()
        totalSize += self.fileSize
        self.totalSize += totalSize
        return totalSize


def readElements(file: str):
    basicString = ""
    commandos = []
    with open(file) as f:
        for num, line in enumerate(f):
            line = line.strip()
            if line[0] == "$":
                line = line[2:]
                commandos.append([line.split(" "), []])
            else:
                argument1, argument2 = line.split(" ")
                commandos[-1][1].append((argument1, argument2))
    return commandos


def buildDirStructure(direct: Directory, commandos):
    baseDirectory = direct
    currentDirecotry = None
    for iter1, commando in enumerate(commandos):
        com = commando[0][0]
        results = commando[1]
        if com == "cd":
            argument = commando[0][1]
            basePath = "./"
            relativPath = argument
            if argument[0] == "/":
                relativPath = argument[1:]
                currentDirecotry = baseDirectory
            elif argument[0:2] == "./":
                relativPath = argument[2:]
            if relativPath:
                parts = relativPath.split("/")
                for part in parts:
                    if part == "..":
                        currentDirecotry = currentDirecotry.parent
                    else:
                        if part in map(lambda x: x.name, currentDirecotry.listOfSubDirs):
                            currentDirecotry = [x for x in currentDirecotry.listOfSubDirs if x.name == part][0]
                        else:
                            print("Moving into unkown Dir")
                            newDir = Directory(name=part, parent=currentDirecotry)
                            currentDirecotry.addSub(newDir)
                            currentDirecotry = newDir
        elif com == "ls":
            for res in results:
                if res[0] == "dir":
                    if res[1] not in map(lambda x: x.name, currentDirecotry.listOfSubDirs):
                        print("Found new Subdir")
                        newDir = Directory(name=res[1], parent=currentDirecotry)
                        currentDirecotry.addSub(newDir)
                    else:
                        print("Subdir already known")
                else:
                    currentDirecotry.addFile(File(name=res[1], fileSize=int(res[0])))
    return baseDirectory


def task1():
    commandos = readElements("07.txt")
    baseDirectory = Directory(name="/", parent=None)
    buildDirStructure(baseDirectory, commandos)
    totalSize = baseDirectory.getDirSize()

    resultDirs = []
    dirsToCheck = [baseDirectory]
    while dirsToCheck:
        dirsToAppend = []
        for currentDir in dirsToCheck:
            dirsToAppend += currentDir.listOfSubDirs
            if currentDir.totalSize < 100000:
                resultDirs.append(currentDir)
        dirsToCheck = dirsToAppend
    finalSum = 0
    for result in resultDirs:
       finalSum += result.totalSize
    print(f" Task 1 | Total filesystem size: {totalSize}, Sum of all dirs smaller than 100000: {finalSum}")


def task2():
    commandos = readElements("07.txt")
    baseDirectory = Directory(name="/", parent=None)
    buildDirStructure(baseDirectory, commandos)
    totalSize = baseDirectory.getDirSize()

    diskSpace = 70000000
    neededSpace = 30000000
    freeSpace = diskSpace - totalSize
    spaceToClear = neededSpace - freeSpace


    resultDirs = []
    dirsToCheck = [baseDirectory]
    while dirsToCheck:
        dirsToAppend = []
        for currentDir in dirsToCheck:
            dirsToAppend += currentDir.listOfSubDirs
            if currentDir.totalSize > spaceToClear:
                resultDirs.append(currentDir)
        dirsToCheck = dirsToAppend

    resultDirs.sort(key=lambda x: x.totalSize)
    finalDir = resultDirs[0]

    print(f" Task 1 | Total filesystem size: {totalSize}, Size of smallest needed Dir: {finalDir.totalSize}")


task1()
task2()
