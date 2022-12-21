from collections import defaultdict, deque
from methods import  read_data

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

maths = []
nums = defaultdict()

for line in data:
    sp = line.split(': ')
    name = sp[0]
    op = sp[1]

    if(name == 'humn'):
        tester  = 'humn'
        continue

    if(' ' in op):
        ops = op.split(' ')

        maths.append((name, ops[1], [ops[0], ops[2]]))
    else:
        nums[name] = int(op)

def runOp(op, f, s):
    if(op == '/'):
        return f / s
    elif(op == '+'):
        return f + s
    elif(op == '-'):
        return f - s
    elif(op == '*'):
        return f * s

# foundRoot = False
# print('part 1')
# # should this be a queue and not a list?
# while(not foundRoot):
    # x = maths.pop(0)
    # name = x[0]

    # if(name in nums or name == 'humn'):
    #     continue

    # operation = x[1]
    # first = x[2][0]
    # second = x[2][1]
    # if(first in nums and second in nums):
    #     print('found ' + name)
    #     nums[name] = runOp(operation, nums[first], nums[second])
    #     if(name == 'root'):
    #         print(nums[x[0]])
    #         foundRoot = True
    #         break

    # maths.append(x)


# gets all it can first
for i in range(6000):
    x = maths.pop(0)
    name = x[0]

    if(name in nums or name == tester):
        continue

    operation = x[1]
    first = x[2][0]
    second = x[2][1]
    if(first in nums and second in nums):
        nums[name] = runOp(operation, nums[first], nums[second])
        if(name == 'root'):
            # print(nums[x[0]])
            foundRoot = True
            break

    maths.append(x)



def solveForY(op, f, s):
    # print(op, f, s)
    if(op == '/'):
        return f * s
    elif(op == '+'):
        return f - s
    elif(op == '-'):
        return f + s
    elif(op == '*'):
        return f /s

def solveForX(op, f, s):
    # print(op, f, s)
    if(op == '/'):
        return f / s
    elif(op == '+'):
        return s - f
    elif(op == '-'):
        return f - s 
    elif(op == '*'):
        return s / f

def goDown(op, f, s, VV):
    if(f == tester or s == tester):
        if(f in nums):
            return solveForX(op, nums[f], VV)
        else:
            return solveForY(op, VV, nums[s])

    if(f in nums and s not in nums):
        next = [v for v in maths if v[0] == s][0]
        z = solveForX(op, nums[f], VV)
        v = goDown(next[1], next[2][0], next[2][1], z)
        

    elif(s in nums and f not in nums):
        next = [v for v in maths if v[0] == f][0]
        z = solveForY(op, VV, nums[s])
        v = goDown(next[1], next[2][0], next[2][1], z)
    
    return v

rootDude = [v for v in maths if v[0] == 'root'][0]

print('part 2')
print(goDown('-', rootDude[2][0], rootDude[2][1], 0))