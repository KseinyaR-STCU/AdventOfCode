from collections import defaultdict, deque
import math

def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

risks = []

for line in data:
    risks.append(list(map(lambda n: int(n), line[::1])))

width = len(risks[0])
height = len(risks)

start = (0,0)
end = (width -1, height -1)

def check(newX, newY):
    return (
        (newY) < width
        and (newY) >= 0
        and (newX) < height
        and (newX) >= 0)

def step(start):

    cellrisks = defaultdict(lambda: 1e9)
    cellrisks[start] = 0
    visited = set()
    queueue = deque()

    queueue.append(start)

    while queueue:
        current = queueue.popleft()
        X = current[0]
        Y = current[1]

        if (X,Y) in visited:
            continue

        visited.add((X,Y))
        
        if(current == end):
            print(cellrisks[end])

        newCount = cellrisks[current] + risks[X][Y]

        points = [(X, Y+1), (X, Y-1), (X+1, Y), (X-1, Y)]

        for p in points:
            if(p not in visited and check(p[0], p[1])):
                cellrisks[p] = min(newCount, cellrisks[p])
                queueue.append(p)


print('part 1')
step(start)

def getNum(n, i):
    if(n + i > 9):
        return (n + i) - 9
    else:
        return n + i

def multiplyList(riskList, i):
    if i == 0:
        return riskList
    else:
        return list(map(lambda n: getNum(n, i), riskList))

tempList = []

for risk in risks:
    tempRisk = []
    for i in range(5):
        tempRisk.extend(multiplyList(risk[:], i))
    tempList.append(tempRisk)

risks2 = []
for i in range(5):
    for x in tempList:
        risks2.append(multiplyList(x, i))

risks = risks2
width = len(risks[0])
height = len(risks)

start = (0,0)
end = (width -1, height -1)

print('part 2')
step(start)
print('plus ' + str(risks[end[0]][end[1]]))
print('minus ' + str(risks[start[0]][start[1]]))