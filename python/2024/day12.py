from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, get_one_step, get_one_step_up, turn_clockwise
import time
import functools
from collections import defaultdict, deque

st = time.time()


data = read_data('in.tst')
# data = read_data('in.txt')

grid = read_grid(data)


regions = []


def bfsSimple(start, char):
    visited = set()
    queueue = deque()

    queueue.append(start)

    while queueue:
        current = queueue.popleft()
        X = current[0]
        Y = current[1]

        if current in visited:
            continue

        visited.add(current)

        points = [(X, Y+1), (X, Y-1), (X+1, Y), (X-1, Y)]

        for p in points:
            if(p not in visited and in_bounds(p, grid) and get_point_value(p, grid) == char):
                queueue.append(p)
    
    return visited

p1 = 0

all_visited = set()

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if((i,j) not in all_visited):
            reg = bfsSimple((i,j), get_point_value((i,j), grid))
            regions.append(reg)
            all_visited.update(reg)



def get_perim(region):
    all_out = set()
    all_in = []
    for r in region:
        adjs = get_adjacent_points(r)
        for a in adjs:
            if(a not in region):
                all_out.add(a)
                all_in.append(r)
    
    return (all_out, all_in)


for r in regions:
    _, inner = get_perim(r)
    p1 += (len(r) * len(inner))

print('part 1')
print(p1)


def add_sides(listz):

    if(len(listz) == 1):
        return 1

    listz.sort()
    print(listz)

    side = 1

    for l in range(0, len(listz) -1):
        if (listz[l + 1] - listz[l] > 1):
            side += 1
    
    print()
    return int(side / 2)



def get_sides(outer_perim):
    distinct_x = set([x[1] for x in outer_perim])
    distinct_y = set([x[0] for x in outer_perim])

    print('xs', distinct_x)
    print('ys', distinct_y)

    total = 0

    for d in distinct_x:
        print('for x', d)
        total += add_sides([x[0] for x in outer_perim if x[1] == d])
    
    for d in distinct_y:
        print('for y', d)
        total += add_sides([x[1] for x in outer_perim if x[0] == d])

    return total

p2 = 0

for r in regions[0:1]:
    outer, inner = get_perim(r)
    print('outer',outer)
    sides = get_sides(outer)
    print('sides', sides)
    print()
    p2 += (len(r) * sides)

print('part 1')
print(p2)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
