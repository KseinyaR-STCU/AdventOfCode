#part 1
# score = 0

# with open('fulldata.txt') as f:
#     for line in f:
#         opp = line[0]
#         you = line.rstrip()[-1]

#         if(you == 'X'):
#             score += 1
#             if(opp == 'A'):
#                 score += 3
#             elif(opp == 'C'):
#                 score += 6
#         elif(you == 'Y'):
#             score += 2
#             if(opp == 'B'):
#                 score += 3
#             elif(opp == 'A'):
#                 score += 6
#         elif(you == 'Z'):
#             score += 3
#             if(opp == 'C'):
#                 score += 3
#             elif(opp == 'B'):
#                 score += 6

# print(score)

#part 2
# score = 0

# with open('fulldata.txt') as f:
#     for line in f:
#         opp = line[0]
#         you = line.rstrip()[-1]

#         if(you == 'X'):
#             score += 0
#             if(opp == 'A'):
#                 score += 3
#             elif(opp == 'B'):
#                 score += 1
#             elif(opp == 'C'):
#                 score += 2
#         elif(you == 'Y'):
#             score += 3
#             if(opp == 'A'):
#                 score += 1
#             elif(opp == 'B'):
#                 score += 2
#             elif(opp == 'C'):
#                 score += 3
#         elif(you == 'Z'):
#             score += 6
#             if(opp == 'A'):
#                 score += 2
#             elif(opp == 'B'):
#                 score += 3
#             elif(opp == 'C'):
#                 score += 1

# print(score)



### Attempt 2 cleanup

opts = ['A','B','C']
outcomes = ['X','Y','Z']

#part 1

score = 0

with open('fulldata.txt') as f:
    for line in f:
        opp = line[0]
        you = line.rstrip()[-1]

        oppIndex = opts.index(opp)
        youIndex = outcomes.index(you)

        if(oppIndex == youIndex):
            score += 3
        elif(oppIndex == youIndex - 1 or (youIndex == 0 and oppIndex == 2)):
            score += 6

        score += 1 + youIndex


print(score)

#part 2

score = 0

with open('fulldata.txt') as f:
    for line in f:
        opp = line[0]
        outcome = line.rstrip()[-1]

        oppIndex = opts.index(opp)

        score += (outcomes.index(outcome) * 3)

        if(outcome == 'X'):
            if(oppIndex == 0):
                score += 3
            else:
                score += oppIndex
        elif(outcome == 'Y'):
            score += oppIndex + 1
        elif(outcome == 'Z'):
            if(oppIndex == 2):
                score += 1
            else:
                score += oppIndex + 2


print(score)
