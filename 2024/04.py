from enum import Enum

test = False

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(self.x,self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __hash__(self):
        return hash((self.x, self.y))

class OrthogonalDirections(Enum):
    NorthEast = Coordinate(1, -1)
    SouthEast = Coordinate(1, 1)
    SouthWest = Coordinate(-1, 1)
    NorthWest = Coordinate(-1, -1)

class Directions(Enum):
    North = Coordinate(0, -1)
    East = Coordinate(1, 0)
    South = Coordinate(0, 1)
    West = Coordinate(-1, 0)
    NorthEast = Coordinate(1, -1)
    SouthEast = Coordinate(1, 1)
    SouthWest = Coordinate(-1, 1)
    NorthWest = Coordinate(-1, -1)

def prepInput(path):
    lines = open(path, 'r').readlines()
    return [x.strip('\n') for x in lines]


def outOfBoundes(coordinates, puzzle):
    if 0 <= coordinates.x <= len(puzzle[0]) - 1:
        if 0 <= coordinates.y <= len(puzzle) - 1:
            return False
    return True

def wordFound(letters: list[str], coordinates: Coordinate, direction, puzzle):
    if not letters:
        return True

    if outOfBoundes(coordinates, puzzle):
        return False

    if puzzle[coordinates.y][coordinates.x] == letters[0]:
        return wordFound(letters[1:], coordinates+direction.value, direction, puzzle)
    else:
        return False

def one(path: str):
    count = 0
    puzzle = prepInput(path)
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == 'X':
                for direction in Directions:
                    if wordFound(["M","A","S"], Coordinate(x, y) + direction.value, direction, puzzle):
                        count += 1
    print(f"Final Task One: {count}")

def two(path: str):
    puzzle = prepInput(path)
    coordinateDictionary = {}
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char == 'M':
                for direction in OrthogonalDirections:
                    if wordFound(["A","S"], Coordinate(x, y) + direction.value, direction, puzzle):
                        coordinateDictionary[Coordinate(x, y) + direction.value] = coordinateDictionary.get(Coordinate(x, y) + direction.value,0) + 1
    count = 0
    for x in coordinateDictionary.values():
        if x == 2:
            count += 1
    print(f"Final Task Two: {count}")

def main():
    current = __file__.strip('.py')
    if test:
        one(current+"a.txt")
    else:
        print("Calling Toby")
        one(current+"b.txt")
        two(current+"b.txt")
        print("Calling Freya")
        one(current+"c.txt")
        two(current+"c.txt")
main()