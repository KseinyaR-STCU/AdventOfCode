def read_data(fileName):
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

import codecs
def read_udf_data(fileName):
    with codecs.open(fileName, encoding = 'utf-16') as f:
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

    # read the given line into a list of numbers split by whitespace
def splitNumsOnWhitespace(line):
    return list(map(lambda n: int(n), line.split()))

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


# Get all points between two points (not diagonally)
def getPoints(p1, p2):
    xs = list(range(p1[0], p2[0], 1))
    xs.extend(range(p2[0], p1[0],  1))
    ys = list(range(p1[1], p2[1], 1))
    ys.extend(range(p2[1], p1[1],  1))

    all = set()

    for x in xs:
        all.add((x, p1[1]))

    for y in ys:
        all.add((p1[0], y))
    
    return all

# dijkstra? bfs? idk exactly lol
from collections import defaultdict, deque

def bfsWithCounts(start, end, isValid, risks):
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

def bfsSimple(start, end, isValid):
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

        newCount = cellrisks[current] + 1

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



# grid stuff

# read grid into lists of chars
def read_grid(data):
    grid = []
    for line in data:
        grid.append(list(map(lambda n: n, line[::1])))
    
    return grid

# find a distinct character in the grid (e.g. starting point)
def find_distinct_char_in_grid(grid, char):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if(grid[i][j] == char):
                return (i,j)
    
    return (-1, -1)

# get grid size
def get_grid_size(grid):
    maxI = len(grid)
    maxJ = len(grid[0])
    return (maxI, maxJ)

# check if point is in grid
def in_bounds(point, grid):
    maxI, maxJ = get_grid_size(grid)
    if(point[0] >= 0 and point[0] < maxI and point[1] >=0 and point[1] < maxJ):
        return True
    else:
        return False

# get value from grid
def get_point_value(point, grid):
    return grid[point[0]][point[1]]


# get one step in the given direction
def get_one_step(point, dir):
    match dir:
        case 'r':
            return get_one_step_right(point)
        case 'l':
            return get_one_step_left(point)
        case 'u':
            return get_one_step_up(point)
        case 'd':
            return get_one_step_down(point)
    
    return (-1, -1)


# turn clockwise
def turn_clockwise(dir):
    match dir:
        case 'r':
            return 'd'
        case 'l':
            return 'u'
        case 'u':
            return 'r'
        case 'd':
            return 'l'
    
    return ''

# turn counter clockwise
def turn_counter_clockwise(dir):
    match dir:
        case 'r':
            return 'u'
        case 'l':
            return 'd'
        case 'u':
            return 'l'
        case 'd':
            return 'r'
    
    return ''

# get point to the right
def get_one_step_right(point):
    return (point[0], point[1] + 1)

# get valid point to the right
def get_one_valid_step_right(point, grid):
    new_point = get_one_step_right(point)
    if(not in_bounds(new_point, grid)):
        return (-1, -1)
    return new_point

# get point to the left
def get_one_step_left(point):
    return (point[0], point[1] - 1)

# get valid point to the left
def get_one_valid_step_left(point, grid):
    new_point = get_one_step_left(point)
    if(not in_bounds(new_point, grid)):
        return (-1, -1)
    return new_point

# get point to the up
def get_one_step_up(point):
    return (point[0] - 1, point[1])

# get valid point to the up
def get_one_valid_step_up(point, grid):
    new_point = get_one_step_up(point)
    if(not in_bounds(new_point, grid)):
        return (-1, -1)
    return new_point

# get point to the down
def get_one_step_down(point):
    return (point[0] + 1, point[1])

# get valid point to the down
def get_one_valid_step_down(point, grid):
    new_point = get_one_step_down(point)
    if(not in_bounds(new_point, grid)):
        return (-1, -1)
    return new_point


# get straight points around a point
def get_adjacent_points(point):
    points = []
    points.append(get_one_step_down(point))
    points.append(get_one_step_left(point))
    points.append(get_one_step_up(point))
    points.append(get_one_step_right(point))
    return points

# get valid straight points around a point
def get_valid_adjacent_points(point, grid):
    all_points = get_adjacent_points(point)
    return [p for p in all_points if in_bounds(p, grid)]

# get diagonal points around a point
def get_diagonal_points(point):
    points = []
    points.append((point[0] +1, point[1] + 1))
    points.append((point[0] -1, point[1] + 1))
    points.append((point[0] +1, point[1] - 1))
    points.append((point[0] -1, point[1] - 1))
    return points

# get valid diagonal points around a point
def get_valid_diagonal_points(point, grid):
    all_points = get_diagonal_points(point)
    return [p for p in all_points if in_bounds(p, grid)]

# get ALL points around a point
def get_all_points(point, grid):
    all_points = get_diagonal_points(point)
    all_points.extend(get_adjacent_points(point))
    return all_points

# get ALL valid points around a point
def get_all_valid_points(point, grid):
    all_points = get_diagonal_points(point)
    all_points.extend(get_adjacent_points(point))
    return [p for p in all_points if in_bounds(p, grid)]


# scanning for a certain character (returns bool if found and the index)

def checkTreeHorizontal(grid, x, irange, char):
    for i in irange:
        if(grid[x][i] == char):
            return (True, (x, i))
    return (False, (-1, -1))

def checkTreeLeft(grid, x, y, char):
    return checkTreeHorizontal(grid, x, range(0, y), char)

def checkTreeRight(grid, x, y, char):
    maxI, maxJ = get_grid_size(grid)
    return checkTreeHorizontal(grid, x, range(y + 1, maxI), char)

def checkTreeVertical(grid, y, irange, char):
    for i in irange:
        if(grid[i][y] == char):
            return (True, (i, y))
    return (False, (-1, -1))

def checkTreeDown(grid, x, y, char):
    return checkTreeVertical(grid, y, range(0, x), char)

def checkTreeUp(grid, x, y, char):
    maxI, maxJ = get_grid_size(grid)
    return checkTreeVertical(grid, y, range(x + 1, maxJ), char)