
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()


class Directory:
    def __init__(self, name, parent, gp):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent
        self.gp = gp
        self.fullSize = 0
        self.fileSize = 0

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


directories = []

lastDirList = ['', 'home']

def dirExists(id, parent, gp):
    matchingDir = [x for x in directories if x.name == id and x.parent == parent and x.gp == gp]
    return len(matchingDir) > 0

def getMatchingDir(id, parent, gp):
    match = [x for x in directories if x.name == id and x.parent == parent and x.gp == gp][0]
    return directories.index(match)

def parse():
    babydirectories = []
    babyfiles = []
    dirName = 'home'
    for line in data:
        if (line.startswith('$ cd ..')):
            thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
            thisDir.directories = babydirectories
            thisDir.files = babyfiles

            if(not dirExists(thisDir.name, thisDir.parent, thisDir.gp)):
                directories.append(thisDir)
            dirName = lastDirList[-1]
            lastDirList.pop()
            babydirectories = []
            babyfiles = []
        elif (line.startswith('$ cd')):
            thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
            thisDir.directories = babydirectories
            thisDir.files = babyfiles

            if(not dirExists(thisDir.name, thisDir.parent, thisDir.gp)):
                directories.append(thisDir)

            lastDirList.append(dirName)
            dirName = line[5:]
            babydirectories = []
            babyfiles = []
        elif(line.startswith('dir ')):
            babydirectories.append(line[4:])
        elif(not line.startswith('$ ls')):
            sp = line.split(' ')
            babyfiles.append(int(sp[0]))

    thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
    thisDir.directories = babydirectories
    thisDir.files = babyfiles
    directories.append(thisDir)
    lastDirList.append(dirName)


parse()
directories = directories[1:]

for d in directories:
    d.fileSize = sum(d.files)


def addem(dir, parent, gp):
    
    full = 0
    dirD = getMatchingDir(dir, parent, gp)
    if(directories[dirD].fullSize > 0):
        return directories[dirD].fullSize

    for b in directories[dirD].directories:
        dirx = getMatchingDir(b, dir, parent)
        if(directories[dirx].fullSize > 0):
            full += directories[dirx].fullSize 
        else:
            size = addem(b, dir, parent)
            full += size
    
    full += directories[dirD].fileSize
    directories[dirD].fullSize = full
    return full


allSizes = []
allDirs = []

for d in directories:
    allDirs.append(d.name)
    size = addem(d.name, d.parent, d.gp)
    allSizes.append(size)

totalCount = 0
for x in allSizes:
    if(x <= 100000):
        totalCount += x

print('part 1')
print(totalCount)

print('part 2')
needed = 70000000 - directories[0].fullSize

allSizes.sort()

for x in allSizes:
    if(x >= 30000000 - needed):
        print(x)
        break