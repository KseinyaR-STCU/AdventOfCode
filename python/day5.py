# #part1

# stacks = [[],[],[],[],[],[],[],[],[]]
# moves = []
# section = 0

# with open('fulldata.txt') as f:
#     for line in f:
#         temp = line[1::4]

#         if(len(temp) > 0):
#             if(temp[0] == '1'):
#                 section += 1
#             elif(temp[0] == 'o'):
#                 section = 2

#         if(section == 0):    
#             for id, itme in enumerate(temp):
#                 if(itme != ' '):
#                     stacks[id].append(itme)
#         elif(section == 2):
#             steps = line.rstrip().split(' ')[1::2]
#             moves.append(steps)

# for stack in stacks:
#     stack.reverse()

# print(stacks)
# print(moves)

# for move in moves:
#     count = int(move[0])
#     froms = int(move[1]) -1
#     to = int(move[2]) -1

#     for num in range(count):
#         stacks[to].append(stacks[froms].pop())

# print(stacks)

# answer = ''

# for stack in stacks:
#     answer += stack.pop()

# print(answer)

# part 1 better

stacks = [[],[],[],[],[],[],[],[],[]]
moves = []
section = 0

def get_stack(temp):
    for id, item in enumerate(temp):
        if(item != ' '):
            stacks[id].append(item)

def get_move(line):
    steps = line.rstrip().split(' ')[1::2]
    moves.append(steps)

with open('fulldata.txt') as f:
    for line in f:

        temp = line[1::4]

        if(len(temp) > 0):
            if(temp[0] == '1'):
                section += 1
            elif(temp[0] == 'o'):
                section = 2
        
        if(section == 0):
            get_stack(temp)
        elif(section == 2):
            get_move(line)


for stack in stacks:
    stack.reverse()


for move in moves:
    count = int(move[0])
    froms = int(move[1]) -1
    to = int(move[2]) -1

    for num in range(count):
        stacks[to].append(stacks[froms].pop())


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



    temps = []
    for num in range(count):
        temps.append(stacks[froms].pop())
    
    temps.reverse()
    for thing in temps:
        stacks[to].append(thing)


answer = ''

for stack in stacks:
    answer += stack.pop()

print(answer)