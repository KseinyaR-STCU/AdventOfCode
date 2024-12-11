from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_valid_adjacent_points
import time
import functools
from collections import defaultdict, deque

st = time.time()


data = read_data('in.tst')
data = read_data('in.txt')

stones  = []

for line in data:
    stones.extend(list(map(lambda n: n, line.split())))

p1 = 0
p2 = 0

def trim_zero(stone):
    new_st = stone.lstrip('0')
    if(len(new_st) == 0):
        return '0'
    else:
        return new_st

new_s = []

@functools.cache
def map_it(s, c):
    total = 0
    if(c == 0):
        return 1

    if(s == '0'):
        total += map_it('1', c-1)
    elif(len(s) % 2 ==0):
        half = int(len(s) / 2)
        total += map_it(s[:half], c-1)
        total += map_it(trim_zero(s[half:]), c-1)
    else:
        total += map_it(str(int(s) * 2024), c-1)
    
    return total

for s in stones:
    p1 += map_it(s, 25)

print('part 1')
print(p1)

for s in stones:
    p2 += map_it(s, 75)

print('part 2')
print(p2)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
