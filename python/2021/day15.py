from collections import defaultdict, deque
from methods import read_data, splitNumsWholeGrid, bfs

data = read_data('testdata.txt')
# data = read_data('fulldata.txt')

risks = splitNumsWholeGrid(data)

def check(newX, newY):
    return (
        (newY) < width
        and (newY) >= 0
        and (newX) < height
        and (newX) >= 0)

width = len(risks[0])
height = len(risks)

start = (0,0)
end = (width -1, height -1)

print('part 1')
print(bfs(start, end, check, risks))


#### part 2

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

width = len(risks2[0])
height = len(risks2)

start = (0,0)
end = (width -1, height -1)

## this is still wrong and idk whyyyyyy
print('part 2')
print(bfs(start, end, check, risks2))