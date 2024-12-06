from methods import  read_data, read_udf_data, splitNumsOnWhitespace
import math

data = read_data('in.tst')
data = read_data('in.txt')

rules = []
updates  = []

on_pages = False

for line in data:
    if(line.isspace()):
        on_pages = True
    elif(on_pages):
        updates.append(line.split(','))
    else:
        pages = line.split('|')
        if(len(pages) == 2):
            rules.append((pages[0], pages[1]))
        else:
            on_pages = True


def check_before(current, rest):
    afters = [x[1] for x in rules if x[0] == current]
    for r in rest:
        if(r in afters):
            return False
    
    return True

def check_after(current, rest):
    befores = [x[0] for x in rules if x[1] == current]

    for r in rest:
        if(r in befores):
            return False
    
    return True

def check_all(update):
    for i in range(0, len(update)):
        if(not check_before(update[i], update[:i])):
            return False
        
        if(i < len(update) and not check_after(update[i], update[i + 1: ])):
            return False

    return True

p1 = 0

good = []
bad = []

for u in updates:
    if(check_all(u)):
        good.append(u)
    else:
        bad.append(u)

print(good)

for b in good:
    mid = math.floor(len(b) / 2)
    p1 += int(b[mid])

print('part 1')
print(p1)

p2 = 0

def sort_em(bad):
    sorted = bad.copy()

    for x in range(0, 30):
        for i in range(1,len(bad)):
            a = sorted[i - 1]
            b = sorted[i]
            if((b,a) in rules):
                sorted[i -1] = b
                sorted[i] = a
    
    return sorted



for b in bad:
    sorted = sort_em(b)
    print('result', sorted)

    mid = math.floor(len(b) / 2)
    print(b[mid])
    p2 += int(sorted[mid])

print('part 2')
print(p2)