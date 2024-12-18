from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, turn_clockwise, turn_counter_clockwise,  get_one_step, get_one_step_down, get_one_step_right, get_one_step_up
import time
import functools
from collections import defaultdict, deque

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')

boots = []

for line in data:
    sp =line.split(',')
    boots.append((int(sp[0]), int(sp[1])))

maxI = 70
maxJ = 70

baby_boots = boots[0:1024]

def isValid(X, Y):
    if(X >= 0 and X <= maxI and Y >=0 and Y <= maxJ):
        return (X, Y) not in baby_boots
    else:
        return False


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


p1 = bfsSimple((0,0), (maxI, maxJ), isValid)

print('part 1')
print(p1)


for i in range(1024, len(boots)):
    baby_boots = boots[0:i]
    steps = bfsSimple((0,0), (maxI, maxJ), isValid)
    if steps == 1e9:
        break

p2 = i

print('part 2')
print(baby_boots[-1])

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
