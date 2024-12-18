from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, turn_clockwise, turn_counter_clockwise,  get_one_step, get_one_step_down, get_one_step_right, get_one_step_up
import time
import functools
from collections import defaultdict, deque

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')


grid = read_grid(data)

start = find_distinct_char_in_grid(grid, 'S')
end = find_distinct_char_in_grid(grid, 'E')

grid[start[0]][start[1]] = '.'
grid[end[0]][end[1]] = '.'

def isValid(p, grid):
    return in_bounds(p, grid) and get_point_value(p, grid) != '#'

def bfsWithCounts(start, end):
    negative_start = (-1, -1)
    cellcount = defaultdict(lambda: 1e9)
    cellcount[(negative_start, start)] = 0
    visited = set()
    queueue = deque()

    ends = set()

    start_dir = 'r'

    queueue.append((negative_start, start, start_dir, 0))

    while queueue:
        last, current, dir, totalCount = queueue.pop()

        if current == end:
            ends.add(totalCount)
            continue

        if ((last, current) in visited or (current, last) in visited) and (cellcount[(current, last)] < totalCount or cellcount[(last, current)] < totalCount):
            continue

        visited.add((last, current))
        visited.add((current, last))

        points = []
        points.append((current, get_one_step(current, dir), dir, totalCount + 1))

        counter_clockwise = turn_counter_clockwise(dir)
        points.append((current, get_one_step(current, counter_clockwise), counter_clockwise, totalCount +  1001))

        clockwise = turn_clockwise(dir)
        points.append((current, get_one_step(current, clockwise), clockwise, totalCount + 1001))

        for p in points:
            if(isValid(p[1], grid)):
                cellcount[(p[0], p[1])] = min(p[3], cellcount[(p[0], p[1])])
                cellcount[(p[1], p[0])] = min(p[3], cellcount[(p[1], p[0])])
                queueue.append(p)
    
    return min(ends)


p1 = bfsWithCounts(start, end)

print('part 1')
print(p1)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
