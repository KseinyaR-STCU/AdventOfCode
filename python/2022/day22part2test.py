from collections import defaultdict

def read_data(fileName):
    with open(fileName) as f:
        return [l for l in f.readlines()]

data = read_data('testdata.txt')

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

def buildSidesSample():
    sides = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    for ri, r in enumerate(map):
        for ci, c in enumerate(r):
            point = (ri,  ci)
            if(c != ' '):
                if(ri == 0):
                    sides[1].append(point)
                elif(ri == len(map) -1):
                    if(ci > 11):
                        sides[6].append(point)
                    else:
                        sides[7].append(point)
                elif(ri == 7):
                    if(ci > 3 and ci < 8):
                        sides[9].append(point)
                    elif(ci < 4):
                        sides[10].append(point)
                elif(ri == 8):
                    if(ci > 11):
                        sides[4].append(point)
                elif(ri == 4):
                    if(ci > 3 and ci < 8):
                        sides[13].append(point)
                    elif(ci < 4):
                        sides[12].append(point)
                 
                if(ci == 0):
                    sides[11].append(point)
                elif(ci == 8):
                    if(ri < 4):
                        sides[14].append(point)
                    elif(ri > 7):
                        sides[8].append(point)
                elif(ci == 11):
                    if(ri < 4):
                        sides[2].append(point)
                    elif(4 <= ri < 8):
                        sides[3].append(point)
                elif(ci == 15):
                    sides[5].append(point)

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

def findCurrentSide(currSpot):
    currSide = [id for id, x in enumerate(sides) if currSpot in x]
    if(len(currSide) > 1):
        print('fack corner')
        # yay no corners in test data

    return currSide[0]

def findMatchingSideSample(currSide):
    match currSide:
        case 1:
            return (12, 1)
        case 2:
            return (5, 2)
        case 3:
            return (4, 1)
        case 4:
            return (3, 2)
        case 5:
            return (2, 2)
        case 6:
            return (11, 0)
        case 7:
            return (10, 3)
        case 8:
            return (9, 3)
        case 9:
            return (8, 0)
        case 10:
            return (7, 3)
        case 11:
            return (6, 3)
        case 12:
            return (1, 1)
        case 13:
            return (14, 0)
        case 14:
            return (13, 1)

def getMatchingSidePoint(currSpot):
    currSide = findCurrentSide(currSpot)
    matchingSide, newDir = findMatchingSideSample(currSide)
    
    indexOfCurr = sides[currSide].index(currSpot)
    
    matchingSpot =  (sides[matchingSide][::-1][indexOfCurr], newDir)

    if(matchingSide == 13 or matchingSide == 14):
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
            newCurr, newDir = getMatchingSidePoint(curr)
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
            newCurr, newDir = getMatchingSidePoint(curr)
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
            newCurr, newDir = getMatchingSidePoint(curr)
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
            newCurr, newDir = getMatchingSidePoint(curr)
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

sides = buildSidesSample()
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


