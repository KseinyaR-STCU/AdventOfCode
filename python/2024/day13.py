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
        self.prize = prize
        self.i = a[0]
        self.j = b[0]
        self.k = prize[0]
        self.x = a[1]
        self.y = b[1]
        self.z = prize[1]
    
    def print(self):
        print(self.i, self.j, self.k)
        print(self.x, self.y, self.z)


def parse_button(line):
    parts = line.split('+')
    x = parts[1].split(',')[0]
    y = parts[2]
    return (int(x), int(y))

def parse_prize(line):
    parts = line.split('=')
    x = parts[1].split(',')[0]
    y = parts[2]
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

def solve(equation, add = 0):
    # equation.print()
    bigk = equation.k + add
    bigz = equation.z + add

    b = ((bigz * equation.i) - (equation.x * bigk))/((equation.i * equation.y)-(equation.x * equation.j))

    a = ((bigz * equation.j) - (equation.y * bigk))/((equation.j * equation.x)-(equation.i * equation.y))
    
    if (a < 0 or b < 0 or int(a) != a or int(b) != b):
        return 0
    
    return (3 * a) + b

p1 = 0

for e in equations:
    min = solve(e)
    p1 += min

print('part 1')
print(p1)

p2 = 0

for e in equations:
    min = solve(e, 10000000000000)
    p2 += min

print('part 2')
print(p2)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
