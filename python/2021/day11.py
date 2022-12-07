
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

flashCount = [0]
octoList = []
justFlashed = []

for line in data:
    octoList.append(list(map(lambda n: int(n), line[::1])))


def up():
    for x, octopi in enumerate(octoList):
        for y, octo in enumerate(octopi):
            octoList[x][y] += 1

def exists(x, y):
    return (x >= 0 and len(octoList) > x and y >= 0 and len(octoList[x]) > y)

def doTheFlash(x, y):
    flashId = str(x) + str(y)
    if(justFlashed.count(flashId) == 0):
        octoList[x][y] = 0
        flashCount[0] += 1
        justFlashed.append(flashId)
        flash(x, y)

def flash(x, y):
    for xi in [x-1, x, x+1]:
        for yi in [y-1, y, y+1]:
            flashId = str(xi) + str(yi)
            if(exists(xi, yi) and justFlashed.count(flashId) == 0):
                octoList[xi][yi] += 1
                if(octoList[xi][yi] > 9):
                    doTheFlash(xi, yi)

def checkFlash():
    for x, octopi in enumerate(octoList):
        for y, octo in enumerate(octopi):
            if(octo > 9):
                doTheFlash(x, y)

def step():
    up()
    checkFlash()

count = 0
lastLen = 0
while  lastLen < 100:
    count += 1
    step()
    lastLen = len(justFlashed)
    justFlashed.clear()
    print(count)