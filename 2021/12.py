from enum import StrEnum


class Node:
    def __init__(self, id):
        self.id = id
        self.connections = []
        self.BigCave = id.isupper()
    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        strStart = f"{self.id}"
        #strStart += "+->" + ",".join([x.id for x in self.connections])
        return str(strStart)

    def __eq__(self, other):
        if not isinstance(other, Node):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.id == other.id

    def isEnd(self):
        return self.id == "end"


class Map:
    def __init__(self):
        self.listOfNodes = []
        self.start = None
        self.end = None

    def setUp(self):
        self.start = [x for x in self.listOfNodes if x.id == "start"][0]
        self.end = [x for x in self.listOfNodes if x.id == "end"][0]

    def buildPath(self, visitedNodes: Node, currentNode: Node) -> list:
        if len(visitedNodes) > 0 and currentNode == self.start:
            return None
        if currentNode in visitedNodes and not currentNode.BigCave:
            return None
        if currentNode == self.end:
            return [currentNode]
        visitedNodes = visitedNodes.copy()
        visitedNodes.append(currentNode)
        listOfPaths = []

        for node in currentNode.connections:
            results = self.buildPath(visitedNodes, node)
            if results:
                for result in results:
                    if isinstance(result,list):
                        newList = [currentNode]
                        newList.extend(result)
                        listOfPaths.append(newList)
                    else:
                        listOfPaths.append([currentNode, result])
        return listOfPaths

    def buildPath2(self, visitedNodes: Node, currentNode: Node, jokerUsed: bool) -> list:

        #localJokerUser = jokerUsed.copy()
        if len(visitedNodes) > 0 and currentNode == self.start:
            return None
        if currentNode in visitedNodes and not currentNode.BigCave and jokerUsed:
            return None
        if currentNode == self.end:
            return [currentNode]

        tempBool = not jokerUsed and currentNode in visitedNodes and not currentNode.BigCave

        visitedNodes = visitedNodes.copy()
        visitedNodes.append(currentNode)
        listOfPaths = []
        for node in currentNode.connections:
            if tempBool:
                results = self.buildPath2(visitedNodes, node, True)
            else:

                results = self.buildPath2(visitedNodes, node, jokerUsed)
            if results:
                for result in results:
                    if isinstance(result,list):
                        newList = [currentNode]
                        newList.extend(result)
                        listOfPaths.append(newList)
                    else:
                        listOfPaths.append([currentNode, result])
        return listOfPaths

    def printPaths(self, test):
        print("\n".join([",".join([y.id for y in x]) for x in test]) + "\n")
def task1():
    board = Map()
    with open("12.txt") as f:
        for num, line in enumerate(f):
            nodes = line.strip().split("-")
            for numb, node in enumerate(nodes):
                nodeObject = Node(node)
                if nodeObject not in board.listOfNodes:
                    nodes[numb] = nodeObject
                    board.listOfNodes.append(nodeObject)
                else:
                    nodes[numb] = [n for n in board.listOfNodes if n == nodeObject][0]
            for node in nodes:
                otherNode = [n for n in nodes if n != node][0]
                node.connections.append(otherNode)
                node.connections = list(dict.fromkeys(node.connections))

    board.setUp()
    test = board.buildPath([], board.start)

    print(f" Task 1 | Paths: {len(test)}")


def task2():
    board = Map()
    with open("12.txt") as f:
        for num, line in enumerate(f):
            nodes = line.strip().split("-")
            for numb, node in enumerate(nodes):
                nodeObject = Node(node)
                if nodeObject not in board.listOfNodes:
                    nodes[numb] = nodeObject
                    board.listOfNodes.append(nodeObject)
                else:
                    nodes[numb] = [n for n in board.listOfNodes if n == nodeObject][0]
            for node in nodes:
                otherNode = [n for n in nodes if n != node][0]
                node.connections.append(otherNode)
                node.connections = list(dict.fromkeys(node.connections))

    board.setUp()
    test = board.buildPath2([], board.start, False)

    print(f" Task 2 | Paths: {len(test)}")



task1()
task2()
