import sys
sys.setrecursionlimit(20000)
from collections import deque
from methods import  read_data

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

class Cube:
    def __init__(self, coords):
        self.x = int(coords[0])
        self.y = int(coords[1])
        self.z = int(coords[2])
        self.adjacents = 0

def checkAdjacency(c, c2):
    return ((c.x == c2.x and c.y == c2.y and abs(c.z - c2.z) <= 1)
        or (c.x == c2.x and c.z == c2.z and abs(c.y - c2.y) <= 1)
        or (c.z == c2.z and c.y == c2.y and abs(c.x - c2.x) <= 1))

def checkIfExists(x,y,z):
    return len([c for c in cubes if c.x == x and c.y ==y and c.z ==z]) >0


cubes = []
minX = 100
maxX = 0
minY = 100
maxY = 0
minZ = 100
maxZ = 0

for line in data:
    cubes.append(Cube(line.split(',')))

for i, c in enumerate(cubes):
    minX = min(minX, c.x)
    maxX = max(maxX, c.x)
    minY = min(minY, c.y)
    maxY = max(maxY, c.y)
    minZ = min(minZ, c.z)
    maxZ = max(maxZ, c.z)
    for j, c2 in enumerate(cubes):
        if(i != j):
            if(checkAdjacency(c, c2)):
                c.adjacents += 1

area = 6*len(cubes) - sum([v.adjacents for v in cubes])
print('part 1')
print(area)

def getCoordString(x, y, z):
    return str(x) + '-' + str(y) + '-' + str(z)

# for c in cubes:
#     print(getCoordString(c.x, c.y, c.z))
#     print(c.adjacents)
#     print(6 - c.adjacents)

def isValid(c):
    return (minX -1 <= c[0] and c[0] <= maxX + 1
        and minY -1 <= c[1] and c[1] <= maxY + 1
        and minZ -1 <= c[2] and c[2] <= maxZ + 1)

def getCoordString(x, y, z):
    return str(x) + '-' + str(y) + '-' + str(z)

def fillQueue():
    queueue = deque()
    visited = set()
    cubeTouches = set()
    cubesPoints = set([(c.x, c.y, c.z) for c in cubes])
    # visited.update(cubesPoints)
    queueue.append((minX, minY, minZ))

    while queueue:
        x,y,z = queueue.popleft()
        if((x,y,z) in visited):
            continue

        # print(getCoordString(x,y,z))

        visited.add((x,y,z))

        coords = [
            [x-1, y, z],
            [x+1, y, z],
            [x, y+1, z],
            [x, y-1, z],
            [x, y, z+1],
            [x, y, z-1]
            ]
        for c in coords:
            newPoint = (c[0], c[1], c[2])
            if(newPoint in cubesPoints):
                cubeTouches.add(newPoint)
            if(isValid(c) and newPoint not in visited and newPoint not in cubesPoints): #and not checkIfExists(c[0], c[1], c[2])):
                queueue.append(newPoint)

    return visited, cubeTouches


allFilled, cubesTouched = fillQueue()

print(len(cubesTouched))
totalArea = 6 * len(cubesTouched)

totalAdjs = 0

for i in range(minX, maxX +1):
    for j in range(minY, maxY +1):
        for k in range(minZ, maxZ + 1):
            if((i,j,k) not in allFilled and not checkIfExists(i,j,k)):
                cubes.append(Cube([i,j,k]))

for c in cubesTouched:
    cube = Cube([c[0],c[1],c[2]])
    for j, c2 in enumerate(cubes):
        if(getCoordString(cube.x, cube.y, cube.z) != getCoordString(c2.x, c2.y, c2.z) and checkAdjacency(cube, c2)):
            totalAdjs += 1

print(totalArea)
print(totalAdjs)
print()
print(totalArea - totalAdjs)

# works on sample
# touchCount = 0
# for i, c in enumerate(allFilled):
#     # print()
#     # print(c)
#     for j, c2 in enumerate(cubes):
#         # print(getCoordString(c2.x, c2.y, c2.z))
#         if(c[0] == c2.x and c[1] == c2.y and abs(c[2] - c2.z) <= 1):
#             # print('touchz')
#             touchCount += 1
#         if(c[0] == c2.x and c[2] == c2.z and abs(c[1] - c2.y) <= 1):
#             # print('touchy')
#             touchCount += 1
#         if(c[2] == c2.z and c[1] == c2.y and abs(c[0] - c2.x) <= 1):
#             # print('touchx')
#             touchCount += 1

# print(touchCount)

# touchCount +=  len([c for c in cubes if c.x == minX or c.x == maxX])
# touchCount +=  len([c for c in cubes if c.y == minY or c.y == maxY])
# touchCount +=  len([c for c in cubes if c.z == minZ or c.z == maxZ])


# print(touchCount)


#works on sample
# for i in range(minX, maxX +1):
#     for j in range(minY, maxY +1):
#         for k in range(minZ, maxZ + 1):
#             if((i,j,k) not in allFilled):
#                 pockets.append(Cube([i,j,k]))

# for i, c in enumerate(cubes):
#     c.adjacents = 0

# cubes.extend(pockets)
# for i, c in enumerate(cubes):
#     for j, c2 in enumerate(cubes):
#         if(i != j):
#             if(checkAdjacency(c, c2)):
#                 c.adjacents += 1



# print(originalCubeCount)
# adjSum = len([v.adjacents for v in cubes if v.adjacents == 6])
# area = 6*len(cubes) - sum([v.adjacents for v in cubes])

# print('part 2')
# print(adjSum)
# print(area)