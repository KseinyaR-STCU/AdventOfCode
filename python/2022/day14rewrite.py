from methods import getPoints, read_data

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

def getAllLines():
    lines = set()

    for line in data:
        sp = line.split(' -> ')
        points = []
        for i in sp:
            c = i.split(',')
            point = (int(c[0]), int(c[1]))
            points.append(point)
        
        for p, point in enumerate(points):
            lines.add(point)
            if(p == len(points) -1):
                continue

            lines = lines.union(getPoints(point, points[p+1]))
    
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

minX = min(list(map(lambda n: n[0], lines)))
maxX = max(list(map(lambda n: n[0], lines)))
maxY = max(list(map(lambda n: n[1], lines)))

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
