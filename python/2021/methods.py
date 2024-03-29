def read_data(fileName):
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

# get the unique values of a list
def unique_list(list):
    return list(set(list))

# read the whole blob of data into a grid of numbers split by character
def splitNumsWholeGrid(data):
    grid = []
    for line in data:
        grid.append(list(map(lambda n: int(n), line[::1])))
    return grid

# read the whole blob of data into a grid of numbers split by the given separator
def splitNumsOnSeparatorWholeGrid(data, sep):
    grid = []
    for line in data:
        grid.append(list(map(lambda n: int(n), line.split(sep))))
    return grid

# read the given line into a list of numbers split by character
def splitNums(line):
    return list(map(lambda n: int(n), line[::1]))

# read the given line into a list of numbers split by given separator
def splitNumsOnSeparator(line, sep):
    return list(map(lambda n: int(n), line.split(sep)))

# check the given row for the given range for the given value (greater than or equal)
def checkGridHorizontal(grid, r, irange, t):
    for i in irange:
        if(grid[r][i] >= t):
            return False
    return True

# check the given col for the given range for the given value (greater than or equal)
def checkGridVertical(grid, c, irange, t):
    for i in irange:
        if(grid[i][c] >= t):
            return False
    return True

# get the count of the values in the given row for the given range that meet the condition (greater than or equal)
def addGridHorizontal(grid, r, irange, t):
    count = 0
    for i in irange:
        count +=1
        if(grid[r][i] >= t):
            return count
    return count

# get the count of the values in the given col for the given range that meet the condition (greater than or equal)
def addGridVertical(grid, c, irange, t):
    count = 0
    for i in irange:
        count +=1
        if(grid[i][c] >= t):
            return count
            
    return count


# dijkstra? bfs? idk exactly lol
from collections import defaultdict, deque

def bfs(start, end, isValid, risks):
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

        newCount = cellrisks[current] + risks[X][Y]

        points = [(X, Y+1), (X, Y-1), (X+1, Y), (X-1, Y)]

        for p in points:
            if(p not in visited and isValid(p[0], p[1])):
                cellrisks[p] = min(newCount, cellrisks[p])
                queueue.append(p)
    
    return cellrisks[end]


# hex to binary
def hex2b(hex):
    return bin(hex2d(hex))

# hex to decimal
def hex2d(hex):
    return int(hex, 16)

# decimal to binary
def d2b(dec):
    return bin(int(dec))

def b2d(bin):
    return int(bin, 2)

# hex to binary
def b2hex(b):
    return hex(int(b, 2))[2:]
