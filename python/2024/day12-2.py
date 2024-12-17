from methods import  read_data, read_grid, find_distinct_char_in_grid, get_grid_size, in_bounds, get_adjacent_points, get_point_value, get_one_step, get_one_step_up, turn_clockwise
import time
import functools
from collections import defaultdict, deque

st = time.time()


data = read_data('in.tst')
# data = read_data('in.txt')

grid = read_grid(data)


regions = []


def bfsSimple(start, char):
    visited = set()
    queueue = deque()

    queueue.append(start)

    while queueue:
        current = queueue.popleft()
        X = current[0]
        Y = current[1]

        if current in visited:
            continue

        visited.add(current)

        points = [(X, Y+1), (X, Y-1), (X+1, Y), (X-1, Y)]

        for p in points:
            if(p not in visited and in_bounds(p, grid) and get_point_value(p, grid) == char):
                queueue.append(p)
    
    return visited

p1 = 0

all_visited = set()

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        if((i,j) not in all_visited):
            reg = bfsSimple((i,j), get_point_value((i,j), grid))
            regions.append(reg)
            all_visited.update(reg)



def get_perim(region):
    all_out = set()
    all_in = []
    for r in region:
        adjs = get_adjacent_points(r)
        for a in adjs:
            if(a not in region):
                all_out.add(a)
                all_in.append(r)
    
    return (all_out, all_in)


for r in regions:
    outer, inner = get_perim(r)
    p1 += (len(r) * len(inner))
    print()

print('part 1')
print(p1)
print()

p2 = 0

def get_walls2(outer, perim, region):
    total = 0
    dist = set()
    visited_outer = set()

    if(len(outer) == 1):
        return (4, visited_outer.union(outer))

    if(len(outer) == 2):
        return (8, visited_outer.union(outer))

    dir = 'r'
    
    alls = []
    for p in perim:
        adjs = get_adjacent_points(p)
        for a in adjs:
            if(a not in perim):
                alls.append(a)

    p = list(outer)[0]
    start = p
    i = 0

    while(i < 6000):

        next = get_one_step(p, dir)

        print('p -> next', p, next)
        if((p, next) in dist):
            p = (-1, -1)
            break

        dist.add((p, next))

        poss_inset = get_one_step(p, turn_clockwise(dir))

        if(poss_inset in alls):
            next = poss_inset
            dir = turn_clockwise(dir)
            total += 1

        if(next in alls):
            visited_outer.add(p)
            visited_outer.add(next)
            print('valid next')
            p = next
            continue
        else:
            print('turning')
            dist.add((p, next))
            visited_outer.add(p)
            dir = turn_clockwise(dir)
            # ps = [x for x in get_adjacent_points(next) if x in perim]

            new_step = get_one_step(next, dir)
            if(new_step in region):
                dir = turn_clockwise(dir)
                dir = turn_clockwise(dir)
            else:
                p = get_one_step(next, dir)
                visited_outer.add(p)
            total += 1
            dist.add((p, next))
        
        i += 1
    
    print(outer)
    print(visited_outer)
    return (total, outer.difference(visited_outer))


def get_walls(outer, perim, region):
    total = 0
    dist = set()
    visited_outer = set()

    if(len(region) == 1):
        return 4

    dir = 'r'
    p = perim[0]

    alls = []
    for p in perim:
        adjs = get_adjacent_points(p)
        for a in adjs:
            if(a not in perim):
                alls.append(a)
    
    while(p in perim):
        p = get_one_step_up(p)
    
    if(p == perim[0]):
        print('uhoh')

    start = p
    i = 0

    while(i < 6000):

        next = get_one_step(p, dir)

        print('p -> next', p, next)
        if((p, next) in dist):
            p = (-1, -1)
            break

        dist.add((p, next))

        poss_inset = get_one_step(p, turn_clockwise(dir))

        if(poss_inset in alls):
            next = poss_inset
            dir = turn_clockwise(dir)
            total += 1

        if(next in alls):
            visited_outer.add(p)
            visited_outer.add(next)
            print('valid next')
            p = next
            continue
        else:
            print('turning')
            dir = turn_clockwise(dir)
            # ps = [x for x in get_adjacent_points(next) if x in perim]

            new_step = get_one_step(next, dir)
            if(new_step in region):
                dir = turn_clockwise(dir)
                dir = turn_clockwise(dir)
            else:
                p = get_one_step(next, dir)
                visited_outer.add(p)
            
            dist.add((p, next))

            total += 1
        
        i += 1

    
    while(len(visited_outer) < len(outer)):
        print()
        print('surrounded bb')
        print(outer.difference(visited_outer))
        result = get_walls2(outer.difference(visited_outer), perim, region)
        print('result', result)
        total += result[0]
        visited_outer = visited_outer.union(result[1])
        print()
        print(len(visited_outer))
        print(outer)
        print('new total', total)
    
    

    
    return total


for r in regions:
    outer, inner = get_perim(r)
    tot = get_walls(outer, inner, r)
    print(len(inner))
    print(tot)
    p2 += (len(r) * tot)
    print()

print('part 2')
print(p2)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
