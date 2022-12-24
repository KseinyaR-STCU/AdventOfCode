from collections import defaultdict, deque
from methods import  read_data
import math

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

# grid = []

blizzards = []

blizzLoc = defaultdict()

for r, line in enumerate(data):
    for c, l in enumerate(line):
        point = (r -1,c -1)
        if(l in ['<', '>', '^', 'v']):
            blizzards.append((point, l))

        # grid[r][c] = l

#walls are (0, 0-maxCol), (r, 0 -maxCol), (o-maxRow, 0), (0 -maxRow, c)

minRow = 0
maxRow = r -1
minCol = 0
maxCol = c - 1

lcm = math.lcm(maxRow, maxCol)

start = (-1, minCol)
end = (maxRow, maxCol - 1)

#this can be independent of my own steps
def blizzardMove(minute):
    blizzLocations = []

    if(minute in blizzLoc):
        return blizzLoc[minute]

    for b in [blizz for blizz in blizzards]:
        l = b[1]
        newBr = b[0][0]
        newBc = b[0][1]
        if(l == '<'):
            newBc = ((newBc - minute) % maxCol) 
        elif(l == '>'):
            newBc = ((newBc + minute) % maxCol) 
        elif(l == '^'):
            newBr = ((newBr - minute) % maxRow) 
        elif(l == 'v'):
            newBr = ((newBr + minute) % maxRow) 

        blizzLocations.append((newBr, newBc))
    
    blizzLoc[minute] = blizzLocations
    return blizzLocations


def getValidPoints(curr, blizzLocations):
    news = [curr, (curr[0], curr[1] + 1), (curr[0], curr[1] - 1), (curr[0] + 1, curr[1]), (curr[0] - 1, curr[1])]

    if(curr == start):
        news = [start, (0,0)]

    # print('news', news)
    valids = [v for v in news if v not in blizzLocations and v[0] not in [-1, maxRow] and v[0] <= maxRow and v[1] <= maxCol and v[1] not in [-1, maxCol]]
    # print('valids', valids)

    if(end in news):
        valids.append(end)
    
    if(start in news):
        valids.append(start)

    return valids

# print(maxRow)
print(start)
print(end)
# print(blizzards)
# # print(blizzardMove(blizzards, 1))
# # print(blizzardMove(blizzards, 2))
# # print(blizzardMove(blizzards, 3))
# # print(blizzardMove(blizzards, 4))
# print(blizzardMove(blizzards, 5))
# # print(blizzardMove(blizzards, 6))
# print(getValidPoints((0,0), blizzardMove(blizzards, 5)))

def bfs(start, end, m):
    minCounts = defaultdict(lambda: 1e9)
    # minCounts[start] = m
    visited = set()
    queueue = deque()

    queueue.append((start, m))

    while queueue:
        current, m = queueue.popleft()
        minCounts[current] = m
        newCount = minCounts[current] + 1

        if(current == end):
             break

        if (current, m % lcm) in visited:
            continue

        visited.add((current, m % lcm))

        points = getValidPoints(current, blizzardMove(m))
        # print(points, 'for', current, 'at', m)
        for p in points:
            if((p, newCount) not in visited):
                minCounts[p] = min(newCount, minCounts[p])
                queueue.append((p, m + 1))
    
    return minCounts[end]

# start = (0,0)
round1 = bfs(start, end, 1)
print('part 1')
print(round1 - 1)
round2 = bfs(end, start, round1 - 1)
print(round2)
round3 = bfs(start, end, round2 - 1)
print(round3)

print('part 2')
print(round3 -1)
