from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_one_step, get_point_value, turn_clockwise
import copy
import time
from collections import defaultdict

st = time.time()


data = read_data('in.tst')
data = read_data('in.txt')

grid = read_grid(data)

points = defaultdict()

for i in range(0, len(grid)):
    for j in range(0, len(grid[0])):
        point = grid[i][j]
        if(point != '.'):
            if(point in points):
                matching_points = points[point]
            else:
                matching_points = []

            matching_points.append((i,j))
            points[point] = matching_points
    
# maxI, maxJ = get_grid_size(grid)

p1 = 0

distinct = set()

def get_spots(a, b):
    i,j = a[0], a[1]
    x,y = b[0],b[1]

    diff_i = i - x
    diff_j = j - y

    return ((i + diff_i, j + diff_j), (x - diff_i, y - diff_j))

# print(points)

for point in points.items():
    values = point[1]
    # print(values)
    for i in range(0, len(values)):
        for j in range(i, len(values)):
            if(i != j):
                # print('comparing', values[i], values[j])
                a, b = get_spots(values[i], values[j])
                if(in_bounds(a, grid)):
                    distinct.add(a)
                if(in_bounds(b, grid)):
                    distinct.add(b)

p1 = len(distinct)
print('part 1')
print(p1)

distinctp2 = set()


def get_all_spots(a, b):
    i,j = a[0], a[1]
    x,y = b[0],b[1]

    diff_i = i - x
    diff_j = j - y

    all_points = []

    new_i = i + diff_i
    new_j = j + diff_j

    while(in_bounds((new_i, new_j), grid)):
        print('adding', new_i, new_j)
        all_points.append((new_i, new_j))
        new_i = new_i + diff_i
        new_j = new_j + diff_j


    new_x = x - diff_i
    new_y = y - diff_j

    while(in_bounds((new_x, new_y), grid)):
        all_points.append((new_x, new_y))
        new_x = new_x - diff_i
        new_y = new_y - diff_j

    return all_points

# print(points)


for point in points.items():
    values = point[1]
    poss_extra = []

    # print(values)
    for i in range(0, len(values)):

        for j in range(i, len(values)):
            if(i != j):
                # print('comparing', values[i], values[j])
                all = get_all_spots(values[i], values[j])
                poss_extra.append(values[i])
                poss_extra.append(values[j])
                for a in all:
                    distinctp2.add(a)

    for a in poss_extra:
        distinctp2.add(a)



p2 = len(distinctp2)
print('part 2')
print(distinctp2)
print(poss_extra)
print(p2)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
