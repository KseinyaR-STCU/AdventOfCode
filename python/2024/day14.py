from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, get_one_step, get_one_step_up, turn_clockwise
import time
import functools
from collections import defaultdict, deque

st = time.time()

data = read_data('in.tst')
data = read_data('in.txt')

class Robot:
    def __init__(self, a, b, va, vb):
        self.a = int(a)
        self.b = int(b)
        self.va = int(va)
        self.vb = int(vb)
    
    def print(self):
        print(self.a, self.b, self.va, self.vb)


maxA = 11
maxB = 7

maxA = 101
maxB = 103

def parse_robot(line):
    parts = line.split('=')
    start = parts[1].split(',')
    speed = parts[2].split(',')
    return Robot(start[0], start[1].split()[0], speed[0], speed[1])


robots = []

for line in data:
    temp = parse_robot(line)
    robots.append(temp)

def step(robot):
    if(robot.a + robot.va < 0):
        robot.a = maxA + (robot.a + robot.va)
    else:
        robot.a = (robot.a + robot.va) % maxA

    if(robot.b + robot.vb < 0):
        robot.b = maxB + (robot.b + robot.vb)
    else:
        robot.b = (robot.b + robot.vb) % maxB

    return robot


for i in range(0, 100):
    for r in robots:
        r = step(r)


def count_quadrants():
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for r in robots:
        if(r.a < ((maxA -1) /2)):
            if(r.b < ((maxB - 1) /2)):
                q1 += 1
            elif(r.b > ((maxB - 1) /2)):
                q2 += 1
        elif(r.a > ((maxA -1) /2)):
            if(r.b < ((maxB - 1) /2)):
                q3 += 1
            elif(r.b > ((maxB - 1) /2)):
                q4 += 1

    return q1, q2, q3, q4

q1, q2, q3, q4 = count_quadrants()

p1 = q1 * q2 * q3 * q4

print('part 1')
print(p1)


print('part 2')

for i in range(1, 10000):
    for r in robots:
        r = step(r)

    q1, q2, q3, q4 = count_quadrants()
    if(q1 < 100):
        for a in range(0, maxA):
            make_line = ''
            for b in range(0, maxB):
                if(len([RR for RR in robots if RR.a == b and RR.b == a]) > 0):
                    make_line += '#'
                else:
                    make_line += ' '
            
            print(make_line)

        print(i)
        print()
        time.sleep(0.5)


et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
