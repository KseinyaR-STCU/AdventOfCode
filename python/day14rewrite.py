import math

def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

minX = 1000
maxX, maxY = 0, 0

# this is still kinda gross
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
            minX = min(minX, point[0])
            maxX = max(maxX, point[0])
            maxY = max(maxY, point[1])

        for p, point in enumerate(points):
            lines.add(point)
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

def sandFall(point):
    y = point[1]
    x = point[0]

    pointsToCheck = [(x, y+1), (x-1, y+1), (x+1, y+1)]

    for p in pointsToCheck:
        if(p not in blocks):
            return (p, True)
    
    return (point, False)

def checkBlockBounds(y):
    return (y >= maxY)

def getBlocks():
    blocks = set()
    for l in lines:
        blocks.add(l)
    
    return blocks

def dropSand():
    sandCount = 0
    blocked = False

    while(not blocked):
        sandMoves = True
        point = (dropX, dropY)

        while(sandMoves):
            if(checkBlockBounds(point[1])):
                break

            point, sandMoves = sandFall(point)

        blocks.add(point)

        if(checkBlockBounds(point[1]) or (point[0] == dropX and point[1] == dropY)):
            blocked = True
            break

        sandCount += 1
    
    return sandCount

lines = getAllLines()
blocks = getBlocks()

dropX = 500
dropY = 0

print('part 1')
print(dropSand())

#part 2

#reset blocks
blocks = getBlocks()

# add floor
maxY += 2
for i in range(-1000, 1500, 1):
    blocks.add((i, maxY))

print('part 2')
print(dropSand() + 1)
