
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()


trees = []

for line in data:
    trees.append(list(map(lambda n: int(n), line[::1])))


width = len(trees)
height = len(trees[1])

def checkTreeHorizontal(x, irange, t):
    for i in irange:
        if(trees[x][i] >= t):
            return False
    return True

def checkTreeLeft(x, y, t):
    return checkTreeHorizontal(x, range(0, y), t)

def checkTreeRight(x, y, t):
    return checkTreeHorizontal(x, range(y + 1, width), t)

def checkTreeVertical(y, irange, t):
    for i in irange:
        if(trees[i][y] >= t):
            return False
    return True

def checkTreeDown(x, y, t):
    return checkTreeVertical(y, range(0, x), t)

def checkTreeUp(x, y, t):
    return checkTreeVertical(y, range(x + 1, height), t)

visible = 0

for x, tree in enumerate(trees):
    if(x == 0 or x == width -1):
        visible += len(tree)
    else:
        for y, t in enumerate(tree):
            if(y == 0 or y == height -1):
                visible += 1
            else:
                if(checkTreeLeft(x, y, t)
                or checkTreeRight(x, y, t)
                or checkTreeDown(x, y, t)
                or checkTreeUp(x, y, t)):
                    visible += 1


print('part 1')
print(visible)

def addTreeHorizontal(x, irange, t):
    count = 0
    for i in irange:
        count +=1
        if(trees[x][i] >= t):
            return count
    return count

def addTreeLeft(x, y, t):
    return addTreeHorizontal(x, range(y - 1, -1, -1), t)

def addTreeRight(x, y, t):
    return addTreeHorizontal(x, range(y + 1, width), t)

def addTreeVertical(y, irange, t):
    count = 0
    for i in irange:
        count +=1
        if(trees[i][y] >= t):
            return count
            
    return count

def addTreeDown(x, y, t):
    return addTreeVertical(y, range(x - 1, -1 , -1), t)

def addTreeUp(x, y, t):
    return addTreeVertical(y, range(x + 1, height), t)

highestCount = 0

for x, tree in enumerate(trees):
    if(x == 0 or x == width -1):
        score = 0
    else:
        for y, t in enumerate(tree):
            if(y == 0 or y == height -1):
                score = 0
            else:
                score = addTreeUp(x, y, t) * addTreeDown(x, y, t) * addTreeLeft(x, y, t) * addTreeRight(x, y, t)
                if(score > highestCount):
                    highestCount = score

print('part 2')
print(highestCount)