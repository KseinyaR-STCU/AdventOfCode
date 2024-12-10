from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_valid_adjacent_points
import time
from collections import defaultdict, deque

st = time.time()


data = read_data('in.tst')
data = read_data('in.txt')

grid = read_grid(data)

trailheads = []

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        if(grid[i][j] == '0'):
            trailheads.append((i,j))



def step(start):
    ends = set()
    end_count = 0

    visited = set()
    queueue = deque()

    queueue.append(start)

    while queueue:
        current = queueue.popleft()
        X = current[0]
        Y = current[1]

        curr_value = grid[X][Y]

        if(curr_value == '9'):
            ends.add(current)
            end_count += 1

        points = get_valid_adjacent_points(current, grid)

        for p in points:
            if(p not in visited and int(grid[p[0]][p[1]]) == int(curr_value) + 1):
                queueue.append(p)
    
    return (len(ends), end_count)


p1 = 0
p2 = 0

for t in trailheads:
    sum, total = step(t)
    p1 += sum
    p2 += total


print('part 1')
print(p1)

print('part 2')
print(p2)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
