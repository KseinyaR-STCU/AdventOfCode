
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

dots = []
instructions = []

section = 0

for line in data:
    if(line == ''):
        section = 1
    if(section == 0):
        splitz = line.split(',')
        dots.append(splitz[1] + ',' + splitz[0])
    elif(section == 1):
        section += 1
    else:
        splitz = line.split('=')
        instructions.append([splitz[0][-1], splitz[1]])

def foldY(count):
    for i, dot in enumerate(dots):
        splitz = dot.split(',')
        dotint = int(splitz[0])
        amount = (dotint - count) * 2 
        if(dotint > count):
            dots[i] = str(dotint - amount) + ',' + splitz[1]

def foldX(count):
    for i, dot in enumerate(dots):
        splitz = dot.split(',')
        dotint = int(splitz[1])
        amount = (dotint - count) * 2

        if(dotint > count):
            dots[i] = splitz[0]+ ',' + str(dotint - amount)

def fold(direction, count):
    if(direction == 'x'):
        foldX(int(count))
    else:
        foldY(int(count))

for intsr in instructions:
    fold(intsr[0], intsr[1])

dots.sort()
print(len(list(set(dots))))

for x in range(6):
    currPrint = ''
    for y in range(40):
        id =str(x) + ',' + str(y) 
        if(id in dots):
            currPrint += ('#')
        else:
            currPrint += ('.')
    print(currPrint)
