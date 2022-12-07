
def read_data():
    with open('fulldata.txt') as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

start = data[0]
rules = []
ruleAdd = []

for line in data[2:]:
    splitz = line.split(" -> ")
    rules.append(splitz[0])
    ruleAdd.append(splitz[1])

# part 1

def step(start):
    temp = ''
    pair = ''
    for id in range(len(start) -1):
        pair = start[id:id+2]        
        temp += pair[0]
        if rules.count(pair) > 0:
            index = rules.index(pair)
            temp += ruleAdd[index]
    temp += pair[1]
    return temp

thingy = start
for i in range(10):
    thingy = step(thingy)

listz = list(set(thingy))

sums = []

for x in listz:
    sums.append(thingy.count(x))

print(sums)
print(max(sums) - min(sums))



# part 2 lol oh no

# letterPossibilities = ['N','C','B','H']
letterPossibilities = ['S','C','V','H','K','P','N','B','F','O']
letters = []
letterCounts = []
letterstemp = []

# pairPossibilites = ['CH','HH','CB','NH','HB','HC','HN','NN','BH','NC','BN','BB','BC','CC','CN']
pairs = []
pairCounts = []
pairstemp = []

def initialCount():
    for l in letterPossibilities:
        letters.append(l)
        letterCounts.append(start.count(l))

    for p in rules:
        pairs.append(p)
        pairCounts.append(start.count(p))

initialCount()

for x in range(40):
    letterstemp = letterCounts[:]
    pairstemp = pairCounts[:]

    for pi, p in enumerate(pairs):
        if rules.count(p) > 0:
            pCount = pairCounts[pi]
            index = rules.index(p)
            newletter = ruleAdd[index]
            newletterIndex = letters.index(newletter)
            letterstemp[newletterIndex] = letterstemp[newletterIndex] + pCount
            pairstemp[index] = pairstemp[index] - pCount
            newpairone = p[0] + newletter
            newpairtwo = newletter + p[1]
            pairstemp[pairs.index(newpairone)] = pairstemp[pairs.index(newpairone)] + pCount
            pairstemp[pairs.index(newpairtwo)] = pairstemp[pairs.index(newpairtwo)] + pCount
    
    letterCounts  = letterstemp[:]
    pairCounts = pairstemp[:]
    

print(max(letterCounts) - min(letterCounts))