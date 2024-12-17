from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, turn_clockwise, get_one_step_left, get_one_step_down, get_one_step_right, get_one_step_up
import time
import functools
from collections import defaultdict, deque

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')


grid = []
moves = ''
onMoves = False

for line in data:
    if(line == ''):
        onMoves = True
    elif(not onMoves):
        grid.append(list(map(lambda n: n, line[::1])))
    else:
        moves += line


robot = find_distinct_char_in_grid(grid, '@')

grid[robot[0]][robot[1]] = '.'

def get_one_step(point, dir):
    match dir:
        case '>':
            return get_one_step_right(point)
        case '<':
            return get_one_step_left(point)
        case '^':
            return get_one_step_up(point)
        case 'v':
            return get_one_step_down(point)
    
    return (-1, -1)


def print_grid():
    for i in range(0, len(grid)):
        line = ''
        for j in range(0, len(grid[0])):
            if(robot == (i,j)):
                line += '@'
            else:
                line += get_point_value((i,j), grid)
        print(line)


def get_nexts(point, move):
    next_step = get_one_step(point, move)
    next_block = get_point_value(next_step, grid)
    if(next_block == '.'):
        return (True, next_step)
    elif(next_block == '#'):
        return (False, point)
    elif(next_block == 'O'):
        return get_nexts(next_step, move)
    
    return (False, point)


def do_step(point, move):
    next_step = get_one_step(point, move)
    next_block = get_point_value(next_step, grid)
    if(next_block == '.'):
        return next_step
    elif(next_block == '#'):
        return point
    elif(next_block == 'O'):
        can_move, next_possible = get_nexts(next_step, move)
        if(not can_move):
            return point
        else:
            grid[next_possible[0]][next_possible[1]] ='O'
            grid[next_step[0]][next_step[1]] = '.'

            return next_step
    
    return point


for move in moves:
    robot = do_step(robot, move)

p1 = 0

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if( get_point_value((i, j), grid) == 'O'):
            p1 += (100 * i) + j


print('part 1')
print(p1)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
