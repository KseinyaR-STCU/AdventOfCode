score = 0

with open('fulldata.txt') as f:
    for line in f:
        opp = line[0]
        you = line.rstrip()[-1]

        if(you == 'X'):
            score += 1
            if(opp == 'A'):
                score += 3
            elif(opp == 'C'):
                score += 6
        elif(you == 'Y'):
            score += 2
            if(opp == 'B'):
                score += 3
            elif(opp == 'A'):
                score += 6
        elif(you == 'Z'):
            score += 3
            if(opp == 'C'):
                score += 3
            elif(opp == 'B'):
                score += 6

print(score)


score = 0

with open('fulldata.txt') as f:
    for line in f:
        opp = line[0]
        you = line.rstrip()[-1]

        if(you == 'X'):
            score += 0
            if(opp == 'A'):
                score += 3
            elif(opp == 'B'):
                score += 1
            elif(opp == 'C'):
                score += 2
        elif(you == 'Y'):
            score += 3
            if(opp == 'A'):
                score += 1
            elif(opp == 'B'):
                score += 2
            elif(opp == 'C'):
                score += 3
        elif(you == 'Z'):
            score += 6
            if(opp == 'A'):
                score += 2
            elif(opp == 'B'):
                score += 3
            elif(opp == 'C'):
                score += 1

print(score)
