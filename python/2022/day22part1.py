from collections import defaultdict, deque
from functools import cmp_to_key

def read_data(fileName):
    with open(fileName) as f:
        return [l for l in f.readlines()]

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

map = []
onMap = True
instructions = []

for line in data:
    if(line == "\n"):
        onMap = False
        continue

    if(onMap):
        sp = list(line)
        map.append(sp[:-1])
    else:
        instructions = line

def getSpotsAndWalls():
    spots = defaultdict()
    walls = defaultdict()

    for ri, r in enumerate(map):
        for ci, c in enumerate(r):
            if(c == '.'):
                spots[(ri, ci)] = None
            elif(c == '#'):
                walls[(ri, ci)] = None

    return (spots, walls)

def getNext(I):
    if(I >= len(instructions)):
        return ('S',I + 1)
    instr = instructions[I]
    if(instr == 'R' or instr == 'L'):
        return (instr, I+1)
    else:
        nexter = getNext(I + 1)
        return (instr + nexter[0], nexter[1])

def getInstructions():
    steps = []
    I = 0
    while(I <= len(instructions)):
        instr, I = getNext(I)
        if(instr[0] != 'S'):
            steps.append((int(instr[:-1]), instr[-1]))

    return steps

def padMap():
    # padding cause i don't wanna deal with it
    maxWidth = len(map[0])

    for x in map:
        diff = maxWidth - len(x)
        if(diff > 0):
            x.extend(['' for v in range(diff)])

def findFirstInRow(r):
    row = map[r]
    firstSpot = row.index('.')
    if('#' in row):
        firstWall = row.index('#')
        return min(firstSpot, firstWall)
    else:
        return firstSpot

def findFirstInColumn(c):
    col = ''.join([row[c] for row in map])
    firstSpot = col.index('.')
    if('#' in col):
        firstWall = col.index('#')
        return min(firstSpot, firstWall)
    else:
        return firstSpot

def findLastInRow(r):
    row = ''.join(map[r])
    lastSpot = row.rindex('.')
    if('#' in row):
        lastWall = row.rindex('#')
        return max(lastSpot, lastWall)
    else:
        return lastSpot

def findLastInColumn(c):
    col = ''.join([row[c] for row in map])
    lastSpot = col.rindex('.')
    if('#' in col):
        lastWall = col.rindex('#')
        return max(lastSpot, lastWall)
    else:
        return lastSpot

def moveRight(curr, moves):
    r = curr[0]
    for x in range(moves):
        c = curr[1]
        newCurr = (r, c+1)

        if(newCurr in walls):
            return curr
        elif(newCurr in spots):
            curr = newCurr
        else:
            #wrap
            newC = findFirstInRow(r)
            newCurr = (r, newC)

            if(newCurr in walls):
                return curr
            elif(newCurr in spots):
                curr = newCurr

    return curr

def moveLeft(curr, moves):
    r = curr[0]
    for x in range(moves):
        c = curr[1]
        newCurr = (r, c-1)

        if(newCurr in walls):
            return curr
        elif(newCurr in spots):
            curr = newCurr
        else:
            #wrap
            newC = findLastInRow(r)
            newCurr = (r, newC)

            if(newCurr in walls):
                return curr
            elif(newCurr in spots):
                curr = newCurr

    return curr

def moveDown(curr, moves):
    c = curr[1]
    for x in range(moves):    
        r = curr[0]
        newCurr = (r+1, c)

        if(newCurr in walls):
            return curr
        elif(newCurr in spots):
            curr = newCurr
        else:
            #wrap
            newR = findFirstInColumn(c)
            newCurr = (newR, c)
            if(newCurr in walls):
                return curr
            elif(newCurr in spots):
                curr = newCurr

    return curr

def moveUp(curr, moves):
    c = curr[1]
    for x in range(moves):    
        r = curr[0]
        newCurr = (r-1, c)

        if(newCurr in walls):
            return curr
        elif(newCurr in spots):
            curr = newCurr
        else:
            #wrap
            newR = findLastInColumn(c)
            newCurr = (newR, c)
            # print(newCurr)
            if(newCurr in walls):
                # print('is wall')
                return curr
            elif(newCurr in spots):
                # print('is spot')
                curr = newCurr

    return curr

def move(instr, direction, current):
    moves = instr[0]
    turn = instr[1]

    if(direction == 0):
        current = moveRight(current, moves)
    elif(direction == 1):
        current = moveDown(current, moves)
    elif(direction == 2):
        current = moveLeft(current, moves)
    else:
        current = moveUp(current, moves)
    
    if(turn == 'R'):
        direction += 1
    elif(turn == 'L'):
        direction -= 1

    if(direction == 4):
        direction = 0
    elif(direction < 0):
        direction = 3

    # print(current)
    # print(direction)
    # print()

    return (current, direction)

spots, walls = getSpotsAndWalls()
allInstructions = getInstructions()
padMap()
startPoint = (0,map[0].index('.'))

print('part 1')
curr = startPoint
dir = 0
for i in allInstructions:
    curr,dir = move(i, dir, curr)

row = curr[0] + 1
col = curr[1] + 1

print((1000 * row) + (4 * col) + dir)
