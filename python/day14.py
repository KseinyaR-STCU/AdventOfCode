import math

def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

grid = []
lines = set()

minX = 1000
maxX = 0

maxY = 0

def printBlocks():
    for y, block in enumerate(blocks):
        tempz = ''
        for x, b in enumerate(block):
            if(b):
                tempz += ('#')
            else:
                tempz += (' ')
        print(tempz)

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


for y in range(maxY+1):
    temp = []
    for x in range(minX, maxX+1):
        if((x,y) in lines):
            temp.append('#')
        else:
            temp.append('.')
    
    grid.append(temp)

blocks = []

for g in grid:
    temp = []
    for x in g:
        temp.append(x == '#')
    
    blocks.append(temp)


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

        if(y >= len(blocks) -1 or x < 0 or x >= len(blocks[0]) -1):
            blocks[y][x] = True
            sandMoves = False
            break

        if(blocks[y+1][x] == True):
            #try left
            if(blocks[y+1][x-1] == True):
                #try right
                if(blocks[y+1][x+1] == True):
                    sandMoves = False
                else:
                    point = (x+1, y+1)
            else:
                point = (x-1, y+1)
        else:
            point = (x, y+1)

        y = point[1]
        x = point[0]

    blocks[y][x] = True
    if(y >= len(blocks) or x < 0 or x >= len(blocks[0]) -1):
        abyss = True
        break
    sandCount += 1


print('part 1')
print(sandCount)

#part 2

blocks = []

# good lord I should have just made this huge to begin with
sides = (math.floor(maxX - minX) * 2) + 11

for g in grid:
    temp = []
    for i in range(sides):
        temp.append(False)
    for x in g:
        temp.append(x == '#')
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



dropX = (500 - minX) + sides
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

        if(y >= len(blocks) -1 or x <= 0 or x >= len(blocks[0]) -1):
            blocks[y][x] = True
            break

        if(blocks[y+1][x] == True):
            #try left
            if(blocks[y+1][x-1] == True):
                #try right
                if(blocks[y+1][x+1] == True):
                    sandMoves = False
                else:
                    point = (x+1, y+1)
            else:
                point = (x-1, y+1)
        else:
            point = (x, y+1)

        y = point[1]
        x = point[0]
    
    if(x == dropX and y == 0):
        print('here')
        abyss = True
        break

    blocks[y][x] = True
    # if(y >= len(blocks) or x < 0 or x >= len(blocks[0]) -1):
    #     abyss = True
        # break
    # print(str(y) + " " + str(x))
    sandCount += 1


print('part 2')
print(sandCount + 1)


