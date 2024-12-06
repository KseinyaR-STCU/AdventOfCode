from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_one_step, get_point_value, turn_clockwise
import copy
import argparse


parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--test', type=bool, default=False)
args = parser.parse_args()

data = read_data('in.tst')

if(not args.test):
    data = read_data('in.txt')

grid = read_grid(data)

guard = find_distinct_char_in_grid(grid, '^')

grid[guard[0]][guard[1]] = '.'

maxI, maxJ = get_grid_size(grid)

def move_or_turn(g, dir):
    new_g = get_one_step(g, dir)
    if(not in_bounds(new_g, grid)):
        return ((-1, -1), 'done')
    if(get_point_value(new_g, grid) == '#'):
        new_dir = turn_clockwise(dir)
        return (get_one_step(g, new_dir), new_dir)
    else:
        return (new_g, dir)


p1 = 0

distinct = set()

def move():
    g = guard
    alls = set()
    dir = 'u'
    for x in range(0, 10000):
        if(g == (-1, -1) or dir == 'done'):
            return False
        elif((g, dir) in alls and g != guard):
            return True
        else:
            distinct.add(g)
            alls.add((g, dir))
            g, dir = move_or_turn(g, dir)            


    return False

move()

p1 = len(distinct)
print('part 1')
print(p1)

p2 = 0
for d in distinct.copy():
    i = d[0]
    j = d[1]
    if(grid[i][j] == '.' and (i,j) != guard):
        grid[i][j] = '#'
        if(move()):
            p2 += 1
        grid[i][j] = '.'

print('part 2')
print(p2)
