from methods import  read_data
import copy

data = read_data('in.tst')
data = read_data('in.txt')

guard = (0,0)

real_grid = []
for line in data:
    real_grid.append(list(map(lambda n: n, line[::1])))

for i in range(0, len(real_grid)):
    for j in range(0, len(real_grid[0])):
        if(real_grid[i][j] == '^'):
            guard = (i,j)
            real_grid[i][j] = '.'

maxI = len(real_grid)
maxJ = len(real_grid[0])

def in_bounds(point):
    if(point[0] >= 0 and point[0] < maxI and point[1] >=0 and point[1] < maxJ):
        return True
    else:
        return False


def move_right(g, grid):
    new_g = (g[0], g[1] + 1)
    if(not in_bounds(new_g)):
        return ((-1, -1), 'done')
    if(grid[new_g[0]][new_g[1]] == '#'):
        return ((g[0] + 1, g[1]), 'd')
    else:
        return (new_g, 'r')


def move_up(g, grid):
    new_g = (g[0] -1, g[1])
    if(not in_bounds(new_g)):
        return ((-1, -1), 'done')
    if(grid[new_g[0]][new_g[1]] == '#'):
        return ((g[0], g[1] + 1), 'r')
    else:
        return (new_g, 'u')


def move_left(g, grid):
    new_g = (g[0], g[1] -1)
    if(not in_bounds(new_g)):
        return ((-1, -1), 'done')
    if(grid[new_g[0]][new_g[1]] == '#'):
        return ((g[0] - 1, g[1]), 'u')
    else:
        return (new_g, 'l')


def move_down(g, grid):
    new_g = (g[0] + 1, g[1])
    if(not in_bounds(new_g)):
        return ((-1, -1), 'done')
    if(grid[new_g[0]][new_g[1]] == '#'):
        return ((g[0], g[1] -1), 'l')
    else:
        return (new_g, 'd')


p1 = 0

distinct = set()

def move(grid):
    g = guard
    alls = set()
    dir = 'u'
    for x in range(0, 10000):
        if(g == (-1, -1) or dir == 'done'):
            return False
        elif((g, dir) in alls and g != guard):
            #print(g, dir)
            #print('in loop')
            return True
        else:
            distinct.add(g)
            alls.add((g, dir))

            if(dir == 'u'):
                g, dir = move_up(g, grid)
            elif(dir == 'r'):
                g, dir = move_right(g, grid)
            elif(dir == 'l'):
                g, dir = move_left(g, grid)
            elif(dir == 'd'):
                g, dir = move_down(g, grid)
            


    return False

move(real_grid)

p1 = len(distinct)
print('part 1')
print(p1)

p2 = 0
for i in range(0, len(real_grid)):
    for j in range(0, len(real_grid[0])):
        if(real_grid[i][j] == '.' and (i,j) != guard):
            temp = copy.deepcopy(real_grid)
            temp[i][j] = '#'
            if(move(temp)):
                p2 += 1

print('part 2')
print(p2)