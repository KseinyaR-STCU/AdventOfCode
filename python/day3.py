firstHalf = []
secondHalf = []

sum = 0

with open('fulldata.txt') as f:
    for line in f:
        full = line.rstrip()
        firstHalf = full[:len(full)//2:1]
        secondHalf = full[len(full)//2::1]

        intersection = ord(list(set(firstHalf).intersection(secondHalf))[0])


        if(intersection >= 97 and intersection <= 122):
            sum += (intersection - 96)
        elif(intersection < 97):
            sum += (intersection - 38)


print(sum)




firstList = []
secondList = []
thirdList = []
badges = []

count = 0

sum = 0
with open('fulldata.txt') as f:
    for line in f:
        count+= 1
        full = line.rstrip()
        if(count == 1):
            firstList = full[::1]
        elif(count == 2):
            secondList = full[::1]
        elif(count == 3):
            thirdList = full[::1]
            count = 0
            badges.append(ord(list(set(firstList).intersection(secondList).intersection(thirdList))[0]))

for badge in badges:
    if(badge >= 97 and badge <= 122):
        sum += (badge - 96)
    elif(badge < 97):
        sum += (badge - 38)


print(sum)