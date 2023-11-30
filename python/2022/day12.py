import sys
sys.setrecursionlimit(10000)

def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

blocks = []

start = (0,0)
end = (0,0)

for line in data:
    blocks.append(list(map(lambda n: ord(n), line)))

stepsPer = []
width = len(blocks[0])
height = len(blocks)

for x, block in enumerate(blocks):
    stepsPer.append([])
    for y, b in enumerate(block):
        stepsPer[x].append(-1)
        if b == 83:
            start = (x, y)
            blocks[x][y] = ord('a')
        elif(b == 69):
            end = (x, y)
            blocks[x][y] = ord('z')

ends = []

def check(newX, newY, curr, currCount):
    return (
        (newY) < width
        and (newY) >= 0
        and (newX) < height
        and (newX) >= 0
        and (
            stepsPer[newX][newY] == -1
            or stepsPer[newX][newY] > currCount + 1)
        and (
            (blocks[newX][newY] <= curr + 1)
             and (currCount < 2 or blocks[newX][newY] != ord('a'))))

def step(curr, X, Y, count):
    stepsPer[X][Y] = count

    if(check(X, Y+1, curr, count)):
        step(blocks[X][Y+1], X, Y + 1, count + 1)
    if(check(X, Y-1, curr, count)):
        step(blocks[X][Y-1], X, Y - 1, count + 1)
    if(check(X+1, Y, curr, count)):
        step(blocks[X+1][Y], X + 1, Y, count + 1)
    if(check(X-1, Y, curr, count)):
        step(blocks[X-1][Y], X -1, Y, count + 1)


print('part 1')
step(97, start[0], start[1], 0)
print(stepsPer[end[0]][end[1]])

print('part 2')
min = 5000
for i in range(height):
    stepsPer = []
    for x, block in enumerate(blocks):
        stepsPer.append([])
        for y, b in enumerate(block):
            stepsPer[x].append(-1)

    step(97, i, start[1], 0)
    current = stepsPer[end[0]][end[1]]
    if(min > current):
        min = current

print(min)
