
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()


trees = []

for line in data:
    trees.append(list(map(lambda n: int(n), line[::1])))


width = len(trees)
height = len(trees[1])

visible = 0

def checkTreeLeft(x, y, t):
    for i in range(0, y):
        if(trees[x][i] >= t):
            return 0
    return 1

def checkTreeRight(x, y, t):
    for i in range(y + 1, width):
        if(trees[x][i] >= t):
            return 0
    return 1

def checkTreeDown(x, y, t):
    for i in range(0, x):
        if(trees[i][y] >= t):
            return 0
    return 1

def checkTreeUp(x, y, t):
    for i in range(x + 1, height):
        if(trees[i][y] >= t):
            return 0
    return 1

for x, tree in enumerate(trees):
    if(x == 0 or x == width -1):
        visible += len(tree)
    else:
        for y, t in enumerate(tree):
            if(y == 0 or y == height -1):
                visible += 1
            else:
                isVisible = 0
                isVisible = checkTreeLeft(x, y, t)
                if(isVisible == 0):
                    isVisible = checkTreeRight(x, y, t)
                if(isVisible == 0):
                    isVisible = checkTreeDown(x, y, t)
                if(isVisible == 0):
                    isVisible = checkTreeUp(x, y, t)
                visible += isVisible


print('part 1')
print(visible)


def addTreeLeft(x, y, t):
    count = 0
    for i in range(y - 1, -1, -1):
        if(trees[x][i] >= t):
            count +=1
            return count
        else:
            count +=1
    return count

def addTreeRight(x, y, t):
    count = 0
    for i in range(y + 1, width):
        if(trees[x][i] >= t):
            count +=1
            return count
        else:
            count +=1
    return count

def addTreeDown(x, y, t):
    count = 0
    for i in range(x - 1, -1 , -1):
        if(trees[i][y] >= t):
            count +=1
            return count
        else:
            count +=1
    return count

def addTreeUp(x, y, t):
    count = 0
    for i in range(x + 1, height):
        if(trees[i][y] >= t):
            count +=1
            return count
        else:
            count +=1
    return count

highestCount = 0

for x, tree in enumerate(trees):
    if(x == 0 or x == width -1):
        score = 0
    else:
        for y, t in enumerate(tree):
            if(y == 0 or y == height -1):
                score = 0
            else:
                left = addTreeLeft(x, y, t)
                right = addTreeRight(x, y, t)
                up = addTreeUp(x, y, t)
                down = addTreeDown(x, y, t)

                score = up * down * left * right
                if(score > highestCount):
                    highestCount = score

print('part 2')
print(highestCount)