import math
from methods import read_data

data = read_data('testdata.txt')
# data = read_data('fulldata.txt')


minX = 1000
maxX, maxY = 0, 0


def printBlocks():
    for block in enumerate(blocks):
        tempz = ''
        for b in enumerate(block):
            if(b):
                tempz += ('#')
            else:
                tempz += (' ')
        print(tempz)

def getAllLines():
    global minX, maxX, maxY
    lines = set()

    for line in data:
        sp = line.split(' -> ')
        points = []
        for i in sp:
            c = i.split(',')
            point = (int(c[0]), int(c[1]))
            points.append(point)
            lines.add(point)
            minX = min(minX, point[0])
            maxX = max(maxX, point[0])
            maxY = max(maxY, point[1])

        for p, point in enumerate(points):
            if(p == len(points) -1):
                continue
            xs = list(range(point[0], points[p+1][0], 1))
            xs.extend(range(points[p+1][0], point[0],  1))
            ys = list(range(point[1], points[p+1][1], 1))
            ys.extend(range(points[p+1][1], point[1],  1))

            for x in xs:
                lines.add((x, point[1]))

            for y in ys:
                lines.add((point[0], y))
    
    return lines

def sandFall(x, y):
    if(blocks[y+1][x]):
        #try left
        if(blocks[y+1][x-1]):
            #try right
            if(blocks[y+1][x+1]):
                return ((x, y), False)
            else:
                point = (x+1, y+1)
        else:
            point = (x-1, y+1)
    else:
        point = (x, y+1)
    
    return (point, True)

def checkBlockBounds(x, y):
    return (y >= len(blocks) -1 or x < 0 or x >= len(blocks[0]) -1)

def getBlocks():
    blocks = []
    for y in range(maxY+1):
        temp = []
        for x in range(minX, maxX+1):
            if((x,y) in lines):
                temp.append(True)
            else:
                temp.append(False)
        
        blocks.append(temp)
    
    return blocks

lines = getAllLines()
blocks = getBlocks()

dropX = (500 - minX)
dropY = 0

sandCount = 0
abyss = False

while(not abyss):
    sandMoves = True

    point = (dropX, dropY)
    y = point[1]
    x = point[0]

    while(sandMoves):
        y = point[1]
        x = point[0]

        if(checkBlockBounds(x, y)):
            sandMoves = False
            break

        point, sandMoves = sandFall(x, y)

        y = point[1]
        x = point[0]

    blocks[y][x] = True

    if(checkBlockBounds(x, y)):
        abyss = True
        break

    sandCount += 1


print('part 1')
print(sandCount)

#part 2

# good lord I should have just made this huge to begin with
sides = (math.floor(maxX - minX) * 2) + 11

def getBlocks2():
    
    blocks = []
    for y in range(maxY+1):
        temp = []
        for i in range(sides):
            temp.append(False)
        for x in range(minX, maxX+1):
            if((x,y) in lines):
                temp.append(True)
            else:
                temp.append(False)
        for i in range(sides):
            temp.append(False)
        
        blocks.append(temp)
    
    temp = []
    for i in range(len(blocks[0])):
        temp.append(False)

    blocks.append(temp)

    temp = []
    for i in range(len(blocks[0])):
        temp.append(True)

    blocks.append(temp)
    
    return blocks

blocks = getBlocks2()

dropX = (500 - minX) + sides
dropY = 0

sandCount = 0
blocked = False


while(not blocked):
    sandMoves = True

    point = (dropX, dropY)
    y = point[1]
    x = point[0]

    while(sandMoves):
        y = point[1]
        x = point[0]

        if(checkBlockBounds(x, y)):
            break

        point, sandMoves = sandFall(x, y)

        y = point[1]
        x = point[0]


    blocks[y][x] = True
    if(checkBlockBounds(x, y) or (x == dropX and y == 0)):
        blocked = True
        break

    sandCount += 1


print('part 2')
print(sandCount + 1)


