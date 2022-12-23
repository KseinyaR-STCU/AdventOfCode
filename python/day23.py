from collections import defaultdict, deque
from methods import  read_data

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

class Elf():
    def __init__(self, point):
        self.point = point
        self.options = []
        self.proposed = None

    def move(self):
        self.point = self.proposed


elves = []

for r, line in enumerate(data):
    for c, char in enumerate(line):
        if(char == '#'):
            elves.append(Elf((r,c)))


directions = [0,1,2,3]

def vertical(curr, currentElves, newRow):
    for c in range(-1, 2):
        check = (newRow, curr[1] + c)
        if(check in currentElves):
            return None

    return (newRow, curr[1])

def north(curr, currentElves):
    newRow = curr[0] - 1
    return vertical(curr, currentElves, newRow)

def south(curr, currentElves):
    newRow = curr[0] + 1
    return vertical(curr, currentElves, newRow)

def horizontal(curr, currentElves, newCol):
    for r in range(-1, 2):
        check = (curr[0] + r, newCol)
        if(check in currentElves):
            return None

    return (curr[0], newCol)

def west(curr, currentElves):
    newCol = curr[1] - 1
    return horizontal(curr, currentElves, newCol)

def east(curr, currentElves):
    newCol = curr[1] + 1
    return horizontal(curr, currentElves, newCol)

def look(curr, currentElves):
    proposeds = []
    for dir in directions:
        if(dir == 0):
            proposal = north(curr, currentElves)
            if(proposal is not None):
                proposeds.append(proposal)
        elif(dir == 1):
            proposal = south(curr, currentElves)
            if(proposal is not None):
                proposeds.append(proposal)
        elif(dir == 2):
            proposal = west(curr, currentElves)
            if(proposal is not None):
                proposeds.append(proposal)
        else:
            proposal = east(curr, currentElves)
            if(proposal is not None):
                proposeds.append(proposal)

    return proposeds

def printPart1():
    rows = [e.point[0] for e in elves]
    cols = [e.point[1] for e in elves]

    minRow = min(rows)
    maxRow = max(rows)

    minCol = min(cols)
    maxCol = max(cols)

    rowSize = maxRow - minRow +1
    colSize = maxCol - minCol +1

    print('part 1')
    print((rowSize * colSize) - len(elves))

for i in range(10000):
    currentElves = [e.point for e in elves]
    proposedMoves = defaultdict(int)

    #propose
    for e in elves:
        proposals = look(e.point, currentElves)
        if(len(proposals) == 4):
            e.proposed = None
        elif(len(proposals) > 0):
            e.proposed = proposals[0]
            proposedMoves[e.proposed] +=1
        else:
            e.proposed = None

        # print(e.point, proposed)

    movers = [e for e in elves if e.proposed is not None]

    if(len(movers) == 0):
        break

    #move
    for e in movers:
        if(proposedMoves[e.proposed] == 1):
            e.move()

    directions.append(directions.pop(0))

    if(i == 9):
        printPart1()
    
print()
print('part 2')
print(i + 1)
