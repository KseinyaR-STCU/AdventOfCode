from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_valid_adjacent_points
import time
from collections import defaultdict, deque

st = time.time()


data = read_data('in.tst')
data = read_data('in.txt')

stones  = []

for line in data:
    stones.extend(list(map(lambda n: n, line.split())))

stones_map = defaultdict(int)

for s in stones:
    stones_map[s] += 1


def trim_zero(stone):
    new_st = stone.lstrip('0')
    if(len(new_st) == 0):
        return '0'
    else:
        return new_st


def map_it(stonesmap):
    new_stones = defaultdict(int)

    for (s, count) in stonesmap.items():
        if(s == '0'):
            new_stones['1'] += count
        elif(len(s) % 2 ==0):
            half = int(len(s) / 2)
            new_stones[s[:half]] += count
            new_stones[trim_zero(s[half:])] += count
        else:
            new_stones[str(int(s) * 2024)] += count
    
    return new_stones


for i in range(0, 25):
    stones_map = map_it(stones_map)


p1 = sum([x[1] for x in stones_map.items()])
print('part 1')
print(p1)

for i in range(0, 50):
    stones_map = map_it(stones_map)

p2 = sum([x[1] for x in stones_map.items()])
print('part 2')
print(p2)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
