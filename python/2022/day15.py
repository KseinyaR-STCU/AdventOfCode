from collections import defaultdict
from methods import getPoints, read_data
import math

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

sensors = []
beacons = []
distances = []

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


for line in data:
    sp = line.split(':')

    sen = sp[0].split(',')
    bea = sp[1].split(',')

    sensor = (int(sen[0].split('=')[1]), int(sen[1].split('=')[1]))
    beacon = (int(bea[0].split('=')[1]), int(bea[1].split('=')[1]))

    sensors.append(sensor)
    beacons.append(beacon)
    distances.append(distance(sensor, beacon))


def getMinX(p1, y, distance):
    return p1[0] - distance + abs(p1[1] - y)

possibs = set()
y = 2000000 

for i, sensor in enumerate(sensors):
    minDistance = distances[i]

    minimum = getMinX(sensor, y, minDistance)
    maximum = ((sensor[0] - minimum) * 2) +  minimum


    for x in range(minimum, maximum):
        possibs.add(x)

print('part 1')
print(len(possibs))

maxSize = 4000000

spotsToCheck = defaultdict(int)

def getBorder(yMin, yMax, x, xMin, xMax):
    checks = set()
    for i in range(xMax - x):
        checks.add((x+i, yMin +i))
        checks.add((x+i, yMax -i))
 
    for i in range(x - xMin):
        checks.add((xMin+i, yMin +i))
        checks.add((xMin+i, yMax -i))

    return checks

for i, sensor in enumerate(sensors):
    minDistance = distances[i] + 1

    yMin = max(sensor[1] - minDistance, 0)
    yMax = min(sensor[1] + minDistance, maxSize)
    xMin = max(sensor[0] - minDistance, 0)
    xMax = min(sensor[0] + minDistance, maxSize)

    spots = getBorder(yMin, yMax, sensor[0], xMin, xMax)
    for s in spots:
        spotsToCheck[(s)] = spotsToCheck[(s)] + 1


duped = [k for k, v in spotsToCheck.items() if v >= 2]

checkers = duped.copy()

for spot in checkers:
    if(spot in duped):
        for i, sensor in enumerate(sensors):
            if(distance(spot, sensor) <= distances[i]):
                duped.remove(spot)
                break

print('part 2')

only = duped.pop()
print(only[0] * maxSize + only[1])





#### failed attempt to filter by range

# searching = True
# currY = 0
# while(searching):
#     xRange = set()

#     for i, sensor in enumerate(sensors):
#         minDistance = distances[i]

#         minimum = getMinX(sensor, currY, minDistance)
#         maximum = ((sensor[0] - minimum) * 2) +  minimum

#         subList = set(list(range(minimum, maximum + 1)))

#         xRange = xRange.union(subList)

#     if(len(xRange) < maxSize - 1):
#         print('in this row ' + str(currY))
#         searching = False
#         break
#     else:
#         currY += 1

