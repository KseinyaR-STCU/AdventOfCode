
def read_data():
    fileName = 'testdata.txt'
    # fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

class Monkey:
    def __init__(self, op, opNum, items, test, testTrue, testFalse):
        self.op = op
        self.opNum = opNum
        self.items = items
        self.test = test
        self.testTrue = testTrue
        self.testFalse = testFalse
        self.count = 0


monkeys = []

for line in data:
    if(line.startswith('Monkey')):
        items = []
        op = ''
        opNum = ''
        test = 0
        ifTrue = 0
        ifFalse = 0
    elif(line.startswith('  Starting')):
        sp = line.split(': ')[1]
        items = list(map(lambda n: int(n), sp.split(', ')))
    elif(line.startswith('  Operation')):
        sp = line.split('old ')[1]
        op = sp[0]
        opNum = sp[2:]
    elif(line.startswith('  Test')):
        test = int(line.split('by ')[1])
    elif('If true' in line):
        ifTrue = int(line.split('monkey ')[1])
    elif('If false' in line):
        ifFalse = int(line.split('monkey ')[1])
    else:
        monkeys.append(Monkey(op, opNum, items, test, ifTrue, ifFalse))

monkeys.append(Monkey(op, opNum, items, test, ifTrue, ifFalse))


def worry(monkey, item):
    num = 0
    if(monkey.opNum == 'old'):
        num = item
    else:
        num = int(monkey.opNum)
    
    if(monkey.op == '*'):
        return item * num
    elif(monkey.op == '+'):
        return item + num
    elif(monkey.op == '-'):
        return item - num
    else:
        return item / num

def relief(item):
    return int((item - (item % 3)) / 3)

def inspect(monkey, item):
    monkey.count += 1
    return (worry(monkey, item))

def throw(monkey, item):
    if(item % monkey.test == 0):
        monkeys[monkey.testTrue].items.append(item)
    else:
        monkeys[monkey.testFalse].items.append(item)

for i in range(20):
    for monkey in monkeys:
        allItems = monkey.items[:]
        for item in allItems:
            if(len(monkey.items) > 1):
                monkey.items = monkey.items[1:]
            else:
                monkey.items = []
            newitem = inspect(monkey, item)
            throw(monkey, newitem)


counts = list(map(lambda n: n.count, monkeys))
print(counts)
counts.sort()
print(counts[-1] * counts[-2])
