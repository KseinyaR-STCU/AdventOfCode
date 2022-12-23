from collections import defaultdict

def read_data(fileName):
    with open(fileName) as f:
        return [l for l in f.readlines()]

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
            x.extend([' ' for v in range(diff)])

def buildSidesFull():
    sides = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for ri, r in enumerate(map):
        for ci, c in enumerate(r):
            point = (ri,  ci)
            if(c != ' '):
                if(ri == 0):
                    if(ci > 99):
                        sides[2].append(point)
                    else:
                        sides[1].append(point)
                elif(ri == len(map) -1):
                    sides[9].append(point)
                elif(ri == 49):
                    if(ci > 99):
                        sides[4].append(point)
                elif(ri == 100):
                    if(ci < 50):
                        sides[12].append(point)
                elif(ri == 149):
                    if(ci > 49):
                        sides[7].append(point)
                 
                if(ci == 0):
                    if(ri < 150):
                        sides[11].append(point)
                    elif(ri > 149):
                        sides[10].append(point)
                elif(ci == 49):
                    if(ri > 149):
                        sides[8].append(point)
                elif(ci == 50):
                    if(ri < 50):
                        sides[14].append(point)
                    elif(ri > 49 and ri < 100):
                        sides[13].append(point)
                elif(ci == 99):
                    if(ri > 49 and ri < 100):
                        sides[5].append(point)
                    elif(ri > 99):
                        sides[6].append(point)
                elif(ci == 149):
                    sides[3].append(point)

    return sides

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

def findCurrentSide(currSpot, currDir):
    currSide = [id for id, x in enumerate(sides) if currSpot in x]
    if(len(currSide) > 1):
        # only handling the corners needed, i'm tired
        print('fack corner', currSpot, currDir)
        print()

        if(currDir == 2 and currSpot == (199, 0)):
            return 10
        if(currDir == 3 and currSpot == (0, 50)):
            return 1
        if(currDir == 1 and currSpot == (49, 149)):
            return 4
        if(currDir == 0 and currSpot == (149, 99)):
            return 6

    return currSide[0]

def findMatchingSideFull(currSide):
    match currSide:
        case 1:
            return (10, 0)
        case 2:
            return (9, 3)
        case 3:
            return (6, 2)
        case 4:
            return (5, 2)
        case 5:
            return (4, 3)
        case 6:
            return (3, 2)
        case 7:
            return (8, 2)
        case 8:
            return (7, 3)
        case 9:
            return (2, 1)
        case 10:
            return (1, 1)
        case 11:
            return (14, 0)
        case 12:
            return (13, 0)
        case 13:
            return (12, 1)
        case 14:
            return (11, 0)

def getMatchingSidePoint(currSpot, currDir):
    currSide = findCurrentSide(currSpot, currDir)
    matchingSide, newDir = findMatchingSideFull(currSide)
    
    indexOfCurr = sides[currSide].index(currSpot)
    
    matchingSpot =  (sides[matchingSide][::-1][indexOfCurr], newDir)

    if(matchingSide in [1, 10, 4,5, 12, 13, 7, 8, 2, 9]):
        matchingSpot =  (sides[matchingSide][indexOfCurr], newDir)

    return matchingSpot

def moveRight(curr, moves):
    currDir = 0
    r = curr[0]
    for x in range(moves):
        c = curr[1]
        newCurr = (r, c+1)

        if(newCurr in walls):
            return (curr, 0, currDir)
        elif(newCurr in spots):
            curr = newCurr
        else:
            newCurr, newDir = getMatchingSidePoint(curr, currDir)
            movesLeft = moves - x - 1

            if(newCurr in walls):
                return (curr, 0, currDir)
            elif(newCurr in spots):
                curr = newCurr
                return (curr, movesLeft, newDir)

    return (curr, 0, 0)

def moveLeft(curr, moves):
    currDir = 2
    r = curr[0]
    for x in range(moves):
        c = curr[1]
        newCurr = (r, c-1)

        if(newCurr in walls):
            return (curr, 0, currDir)
        elif(newCurr in spots):
            curr = newCurr
        else:
            newCurr, newDir = getMatchingSidePoint(curr, currDir)
            movesLeft = moves - x - 1

            if(newCurr in walls):
                return (curr, 0, currDir)
            elif(newCurr in spots):
                curr = newCurr
                return (curr, movesLeft, newDir)

    return (curr, 0, 2)

def moveDown(curr, moves):
    currDir = 1
    c = curr[1]
    for x in range(moves):    
        r = curr[0]
        newCurr = (r+1, c)

        if(newCurr in walls):
            return (curr, 0, currDir)
        elif(newCurr in spots):
            curr = newCurr
        else:
            newCurr, newDir = getMatchingSidePoint(curr, currDir)
            movesLeft = moves - x - 1

            if(newCurr in walls):
                return (curr, 0, currDir)
            elif(newCurr in spots):
                curr = newCurr
                return (curr, movesLeft, newDir)

    return (curr, 0, 1)

def moveUp(curr, moves):
    currDir = 3
    c = curr[1]
    for x in range(moves):    
        r = curr[0]
        newCurr = (r-1, c)

        if(newCurr in walls):
            return (curr, 0, currDir)
        elif(newCurr in spots):
            curr = newCurr
        else:
            newCurr, newDir = getMatchingSidePoint(curr, currDir)
            movesLeft = moves - x - 1

            if(newCurr in walls):
                return (curr, 0, currDir)
            elif(newCurr in spots):
                curr = newCurr
                return (curr, movesLeft, newDir)

    return (curr, 0, 3)

def move(instr, direction, current):
    moves = instr[0]
    turn = instr[1]

    newDir = direction
    movesLeft = moves

    while(movesLeft > 0):
        if(newDir == 0):
            current, movesLeft, newDir = moveRight(current, movesLeft)
        elif(newDir == 1):
            current, movesLeft, newDir = moveDown(current, movesLeft)
        elif(newDir == 2):
            current, movesLeft, newDir = moveLeft(current, movesLeft)
        else:
            current, movesLeft, newDir = moveUp(current, movesLeft)
    
    direction = newDir

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

sides = buildSidesFull()
# for i,s in enumerate(sides):
#     print(i)
#     print(s)


print('part 2')
curr = startPoint
dir = 0
for i in allInstructions:
    curr,dir = move(i, dir, curr)

row = curr[0] + 1
col = curr[1] + 1

print((1000 * row) + (4 * col) + dir)


