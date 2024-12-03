from methods import  read_data, read_udf_data, splitNumsOnWhitespace
import re

data = read_data('in.tst')
data = read_udf_data('in.txt')

def get_nums(section):
    nums = section.split(',')
    first_num = int(nums[0][4:])
    second_num = int(nums[1][:-1])
    return first_num * second_num

p1 = 0

pattern = r"mul\(\d+,\d+\)"

for line in data:
    matches = re.findall(pattern, line)

    print(matches)
    for m in matches:
        p1 += get_nums(m)

print('part 1')
print(p1)

p2 = 0

pattern = r"mul\(\d+,\d+\)"
dont = r"don\'t\(\)"
do = r"do\(\)"

enable = True

for line in data:
    matches_indices = list(map(lambda n: n.start(), re.finditer(pattern, line)))
    matches_text = re.findall(pattern, line)

    donts = list(map(lambda n: n.start(), re.finditer(dont, line)))
    dos = list(map(lambda n: n.start(), re.finditer(do, line)))

    for i in range(0, len(line)):
        if(i in donts):
            enable = False
        elif(i in dos):
            enable = True
        elif(enable and i in matches_indices):
            p2 += get_nums(matches_text[matches_indices.index(i)])

print('part 2')
print(p2)