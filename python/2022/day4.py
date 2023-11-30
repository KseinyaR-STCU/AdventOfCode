startOne = 0
endOne = 0

startTwo = 0
endTwo = 0

sum = 0

with open('fulldata.txt') as f:
    for line in f:
        full = line.rstrip().split(',')
        for idx, part in enumerate(full):
            splits = part.split('-')
            if(idx == 0):
                startOne = int(splits[0])
                endOne = int(splits[1])
            else:
                startTwo = int(splits[0])
                endTwo = int(splits[1])

        if((startTwo >= startOne or endTwo <= endOne) and (startOne >= startTwo or endOne <= endTwo)):
            sum += 1

print(sum)


startOne = 0
endOne = 0

startTwo = 0
endTwo = 0

sum = 0

with open('fulldata.txt') as f:
    for line in f:
        full = line.rstrip().split(',')
        for idx, part in enumerate(full):
            splits = part.split('-')
            if(idx == 0):
                startOne = int(splits[0])
                endOne = int(splits[1])
            else:
                startTwo = int(splits[0])
                endTwo = int(splits[1])

        if(startTwo >= startOne and startTwo <= endOne) or (endTwo >= startOne and endTwo <= endOne) or (startOne >= startTwo and startOne <= endTwo) or (endOne >= startTwo and endOne <= endTwo):
            sum += 1

print(sum)