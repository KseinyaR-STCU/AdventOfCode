from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, get_one_step, get_one_step_up, turn_clockwise
import time
import functools
from collections import defaultdict, deque

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')

class Equation:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        print(prize)
        self.prize = prize
        self.i = a[0]
        self.j = b[0]
        self.k = prize[0]
        self.x = a[1]
        self.y = b[1]
        self.z = prize[1]
    
    def print(self):
        print(self.i, self.j, self.k)


def parse_button(line):
    parts = line.split('+')
    x = parts[1].split(',')[0]
    y = parts[2]
    return (int(x), int(y))

def parse_prize(line):
    print(line)
    parts = line.split('=')
    x = parts[1].split(',')[0]
    y = parts[2]
    print(x,y)
    return (int(x), int(y))

buttonA = (0,0)
buttonB = (0,0)
prize = (0,0)
onA = True

equations = []

for line in data:
    if 'Button' in line:
        temp = parse_button(line)
        if(onA):
            buttonA = temp
            onA = False
        else:
            buttonB = temp
            onA = True
    
    elif 'Prize' in line:
        temp = parse_prize(line)
        equations.append(Equation(buttonA, buttonB, temp))


def solve(equation):
    opts = []
    equation.print()
    for a in range(0, 101):
        for b in range(0, 101):
            tot = (a * equation.i) + (b * equation.j)
            tot2 = (a * equation.x) + (b * equation.y)
            if(tot == equation.k and tot2 == equation.z):
                opts.append((a, b))
    
    return opts

def min_tokens(all_opts):
    if(len(all_opts) == 0):
        return 0

    first_opt = all_opts[0]
    min = (3 * first_opt[0]) + first_opt[1]

    if(len(all_opts) == 1):
        return min

    for opt in all_opts[1:]:
        tot = (3 * opt[0]) + opt[1]
        if(tot < min):
            min = tot

    return min

p1 = 0

for e in equations:
    all_opts = solve(e)
    print(all_opts)
    min =  min_tokens(all_opts)
    print(min)
    print()
    p1 += min

print('part 1')
print(p1)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
