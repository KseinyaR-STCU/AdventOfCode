
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

#part 1
tail = [0,0]
head = [0,0]

def move(dir):
    if(dir == 'U'):
        head[0] += 1
    elif(dir == 'D'):
        head[0] -= 1
    elif(dir == 'R'):
        head[1] += 1
    else:
        head[1] -= 1

def tailNeedsMove(h, t):
    return (abs(h[0] - t[0]) > 1
        or abs(h[1] - t[1]) > 1)

def chase(h, t):
    if(h[0] == t[0]):
        if(h[1] > t[1]):
            t[1] += 1
        else:
            t[1] -= 1
    elif(h[1] == t[1]):
        if(h[0] > t[0]):
            t[0] += 1
        else:
            t[0] -= 1
    else:
        # diagonal
        if(h[0] > t[0]):
            t[0] += 1
        else:
            t[0] -= 1
        if(h[1] > t[1]):
            t[1] += 1
        else:
            t[1] -= 1

def doIt(h, t):
    if(tailNeedsMove(h, t)):
        chase(h, t)

visits = [[0,0]]

for line in data:
    sp = line.split(' ')
    dir = sp[0]
    count = int(sp[1])
    for i in range(count):
        move(dir)
        if(tailNeedsMove(head, tail)):
            chase(head, tail)
            if(len([v for v in visits if(v[0] == tail[0] and v[1] == tail[1])]) == 0):
                visits.append(tail[:])

print('part 1')
print(len(visits))


#part 2
visits = [[0,0]]

tail = [0,0]
head = [0,0]

rope = [head]
for i in range(9):
    rope.append(tail[:])

for line in data:
    sp = line.split(' ')
    dir = sp[0]
    count = int(sp[1])
    for i in range(count):
        move(dir)
        for z, knot in enumerate(rope):
            if(z != len(rope) -1):
                doIt(knot, rope[z+1])

            if(z == len(rope) - 1):
                if(len([v for v in visits if(v[0] == knot[0] and v[1] == knot[1])]) == 0):
                    visits.append(knot[:])

print('part 2')
print(len(visits))