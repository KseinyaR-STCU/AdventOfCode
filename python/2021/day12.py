
def read_data():
    with open('testdata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

class Cave:
    def __init__(self, id):
        self.id = id
        self.big = id.isupper()
        self.exits = []

paths = []
caves = []

def saveCave(currCave, end):
    if (any(cave.id == currCave.id for cave in caves)):
        matchingCave = [x for x in caves if x.id == currCave.id][0]
        thecave = caves.index(matchingCave)
        caves[thecave].exits.append(end)
    else:
        caves.append(currCave)
        caves[-1].exits.append(end)

def buildCaves():
    for line in data:
        splitz = line.split('-')
        a = splitz[0]
        b= splitz[1]
        saveCave(Cave(a), b)
        saveCave(Cave(b), a)

def findCaveIndexById(id):
    matchCave = [x for x in caves if x.id == id][0]
    return caves.index(matchCave)

def isCaveBig(id):
    return caves[findCaveIndexById(id)].big

def goDownPath(currCave, currPath, hasDupeSmallCave):
    startCaveIndex = findCaveIndexById(currCave)
    currPath += currCave + ','
    for exit in caves[startCaveIndex].exits:
        if(exit == 'end'):
            paths.append(currPath + 'end')
        elif(isCaveBig(exit)):
            goDownPath(exit, currPath, hasDupeSmallCave)
        elif(exit not in currPath):
            goDownPath(exit, currPath, hasDupeSmallCave)
        elif(exit != 'start' and not hasDupeSmallCave):
            goDownPath(exit, currPath, True)
        

def buildPaths():
    goDownPath('start', '', False)

def printCave(cave):
    print(cave.id + ' ' + str.join(',',cave.exits))

def printPath(path):
    print(path)

buildCaves()
buildPaths()
print(len(paths))