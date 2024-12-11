from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_one_step, get_point_value, turn_clockwise
import copy
import time
import re
from collections import defaultdict

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')

is_file = True

chars = []
file_index = 0

for line in data:
    for c in line:
        numb = int(c)

        if(is_file):
            chars.extend([str(file_index)] * numb)
            is_file = False
        else:
            is_file = True
            file_index += 1
            chars.extend(['.'] * numb)


reordered = []

for_index = 0

only_nums = [x  for x in chars if x != '.']
total = len(only_nums)
rev_index = len(only_nums) - 1

for i in range(0, len(chars)):
    c = chars[i]
    if(c == '.'):
        last = only_nums[rev_index]
        rev_index -= 1
        reordered.append(last)
    else:
        reordered.append(c)
        for_index += 1

    if(for_index >= rev_index + 1 or for_index >= total):
        break

p1 = 0

for r in range(0, len(reordered)):
    p1 += (r * int(reordered[r]))

print('part 1')
print(p1)


def get_leftmost_spot(chars, size_needed):
    size_got = 0

    for i in range(0, len(chars)):
        if(chars[i] == '.'):
            size_got += 1
        else:
            size_got = 0
        
        if(size_got == size_needed):
            return (i-size_got +1, i)
    
    return (-1, -1)



curr_char = [x for x in chars if x != '.'][-1]
curr_char_size = 0

already_moved = set()
print(curr_char)
for i in range(len(chars) -1, 0, -1):
    # print('loop')
    if(chars[i] == curr_char):
        curr_char_size += 1
    else:
        # time to move the last thing now that i know the size
        if(curr_char != '.' and curr_char_size > 0 and curr_char not in already_moved):
            # print('current to move', curr_char, curr_char_size)
            #find indexes of leftmost fitting spot
            start, end = get_leftmost_spot(chars, curr_char_size)
            # print('leftmost', start, end)
            if(start > -1 and end > -1 and start < i):
                for j in range(start, end + 1):
                    chars[j] = curr_char
                
                # print('removing', i +1, curr_char_size)
                for j in range(i +1, i +1 + curr_char_size):
                    chars[j] = '.'
            
            already_moved.add(curr_char)
        
        # reset to new char
        curr_char = chars[i]
        curr_char_size = 1
    
    # print(chars)


p2 = 0

for r in range(0, len(chars)):
    if(chars[r] != '.'):
        p2 += (r * int(chars[r]))

print('part 2')
print(p2)

# print(chars)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
