
# def read_data():
#     with open('fulldata.txt') as f:
#         return [l.rstrip() for l in f.readlines()]

# data = read_data()


# class Directory:
#     def __init__(self, name, parent, gp):
#         self.name = name
#         self.files = []
#         self.directories = []
#         self.parent = parent
#         self.gp = gp
#         self.fullSize = 0
#         self.fileSize = 0

# class File:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size


# directories = []

# lastDirList = ['', 'home']

# def dirExists(id, parent, gp):
#     matchingDir = [x for x in directories if x.name == id and x.parent == parent and x.gp == gp]
#     return len(matchingDir) > 0

# def getMatchingDir(id, parent, gp):
#     match = [x for x in directories if x.name == id and x.parent == parent and x.gp == gp][0]
#     return directories.index(match)

# def parse():
#     babydirectories = []
#     babyfiles = []
#     dirName = 'home'
#     for line in data:
#         if (line.startswith('$ cd ..')):
#             thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
#             thisDir.directories = babydirectories
#             thisDir.files = babyfiles

#             if(not dirExists(thisDir.name, thisDir.parent, thisDir.gp)):
#                 directories.append(thisDir)
#             dirName = lastDirList[-1]
#             lastDirList.pop()
#             babydirectories = []
#             babyfiles = []
#         elif (line.startswith('$ cd')):
#             thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
#             thisDir.directories = babydirectories
#             thisDir.files = babyfiles

#             if(not dirExists(thisDir.name, thisDir.parent, thisDir.gp)):
#                 directories.append(thisDir)

#             lastDirList.append(dirName)
#             dirName = line[5:]
#             babydirectories = []
#             babyfiles = []
#         elif(line.startswith('dir ')):
#             babydirectories.append(line[4:])
#         elif(not line.startswith('$ ls')):
#             sp = line.split(' ')
#             babyfiles.append(int(sp[0]))

#     thisDir = Directory(dirName, lastDirList[-1], lastDirList[-2])
#     thisDir.directories = babydirectories
#     thisDir.files = babyfiles
#     directories.append(thisDir)
#     lastDirList.append(dirName)


# parse()
# directories = directories[1:]

# for d in directories:
#     d.fileSize = sum(d.files)


# def addem(dir, parent, gp):
    
#     full = 0
#     dirD = getMatchingDir(dir, parent, gp)
#     if(directories[dirD].fullSize > 0):
#         return directories[dirD].fullSize

#     for b in directories[dirD].directories:
#         dirx = getMatchingDir(b, dir, parent)
#         if(directories[dirx].fullSize > 0):
#             full += directories[dirx].fullSize 
#         else:
#             size = addem(b, dir, parent)
#             full += size
    
#     full += directories[dirD].fileSize
#     directories[dirD].fullSize = full
#     return full


# allSizes = []
# allDirs = []

# for d in directories:
#     allDirs.append(d.name)
#     size = addem(d.name, d.parent, d.gp)
#     allSizes.append(size)

# totalCount = 0
# for x in allSizes:
#     if(x <= 100000):
#         totalCount += x

# print('part 1')
# print(totalCount)

# print('part 2')
# needed = 70000000 - directories[0].fullSize

# allSizes.sort()

# for x in allSizes:
#     if(x >= 30000000 - needed):
#         print(x)
#         break



#########################
######### Rewrite #######


def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

directories = dict()

pathList = []

def buildPath():
    return str.join(',',pathList)

def parse():
    totalFilesSize = 0

    for line in data:
        if (line.startswith('$ cd')):
            dirName = line[5:]
            if(dirName == '/'):
                pathList.append('/')
                directories[buildPath()] = 0
            elif(dirName == '..'):
                prevPath = buildPath()
                pathList.pop()
                directories[buildPath()] += directories[prevPath]
            else:
                dirName = line[5:]
                pathList.append(dirName)
                directories[buildPath()] = 0
        elif(not line.startswith('$ ls') and not line.startswith('dir ')):
            fileSize = int(line.split(' ')[0])
            totalFilesSize += fileSize
            directories[buildPath()] += fileSize

    directories['/'] = totalFilesSize

parse()
print('part 1')
print(sum(d for d in directories.values() if d < 100000))

minSizeNeeded = 30000000 - (70000000 - directories['/'])
print('part 2')
print(min(d for d in directories.values() if d > minSizeNeeded))