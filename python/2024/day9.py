from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_one_step, get_point_value, turn_clockwise
import copy
import time
import re
from collections import defaultdict

st = time.time()


data = read_data('in.tst')
#data = read_data('in.txt')

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


files = []

section_count = 0
character = chars[0]
ii = 0

for c in chars:
    if(character != c):
        files.append((ii, character, section_count))
        character = c
        section_count = 1
        ii += 1
    else:
        section_count += 1
    
        
files.append((ii, character, section_count))

print('files',files)

reordered = []
i = len(files) - 1
ci = 0

moved = set()

last_index = -1
count_inserts = 0

while i >= 0:
    index, last, len_last = files[i]

    if(last != '.'):
        fitting = [n for n in files if n[1] == '.' and n[2] >= len_last and n[0] > last_index]
        if(len(fitting) > 0):
            fits = fitting[0]
            files_id = fits[0]
            last_index = files_id - 1
            if(fits[2] == len_last):
                del files[i]
                files[files_id] = (fits[0] + count_inserts, last, fits[2])
                print('replaced perfect fit')
                print('id', files_id)
                print(files)
                # replace
            else:
                del files[i]
                files[files_id] = (fits[0] + count_inserts, fits[1], fits[2] - len_last)
                files.insert(files[files_id][0] + count_inserts, (last_index, last, len_last))
                count_inserts += 1
                print('big enough fit')
                print('id', files_id)
                print('files', files)
                print('fits', fits)
                print('last', last)
                #splits

    i -= 1
    print()

p2 = 0

print(files)
for r in range(0, len(char_string)):
    if(char_string[r] != '.'):
        p2 += (r * int(char_string[r]))

print('part 2')
print(p2)

print(char_string)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
