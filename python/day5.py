#part1

stacks = [[],[],[],[],[],[],[],[],[]]
moves = []
section = 0

with open('fulldata.txt') as f:
    for line in f:
        temp = line[1::4]

        if(len(temp) > 0):
            if(temp[0] == '1'):
                section += 1
            elif(temp[0] == 'o'):
                section = 2

        if(section == 0):    
            for id, itme in enumerate(temp):
                if(itme != ' '):
                    stacks[id].append(itme)
        elif(section == 2):
            steps = line.rstrip().split(' ')[1::2]
            moves.append(steps)

for stack in stacks:
    stack.reverse()

print(stacks)
print(moves)

for move in moves:
    count = int(move[0])
    froms = int(move[1]) -1
    to = int(move[2]) -1

    for num in range(count):
        stacks[to].append(stacks[froms].pop())

print(stacks)

answer = ''

for stack in stacks:
    answer += stack.pop()

print(answer)



#part2

stacks = [[],[],[],[],[],[],[],[],[]]
moves = []
section = 0

with open('fulldata.txt') as f:
    for line in f:
        temp = line[1::4]

        if(len(temp) > 0):
            if(temp[0] == '1'):
                section += 1
            elif(temp[0] == 'o'):
                section = 2

        if(section == 0):    
            for id, itme in enumerate(temp):
                if(itme != ' '):
                    stacks[id].append(itme)
        elif(section == 2):
            steps = line.rstrip().split(' ')[1::2]
            moves.append(steps)

for stack in stacks:
    stack.reverse()


for move in moves:
    count = int(move[0])
    froms = int(move[1]) -1
    to = int(move[2]) -1

    print(stacks)
    print(move)

    temps = []
    for num in range(count):
        temps.append(stacks[froms].pop())
    
    temps.reverse()
    for thing in temps:
        stacks[to].append(thing)

print(stacks)

answer = ''

for stack in stacks:
    answer += stack.pop()

print(answer)