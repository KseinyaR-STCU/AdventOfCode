
def read_data():
    fileName = 'testdata.txt'
    fileName = 'fulldata.txt'
    with open(fileName) as f:
        return [l.rstrip() for l in f.readlines()]

data = read_data()

class Op:
    def __init__(self, op, opNum, test, testTrue, testFalse):
        self.op = op
        self.opNum = opNum
        self.test = test
        self.testTrue = testTrue
        self.testFalse = testFalse


ops = []
worries = []
counts = []

mods = []

monkeyOp = -1
for line in data:
    if(line.startswith('Monkey')):
        monkeyOp += 1
        op = ''
        opNum = ''
        test = 0
        ifTrue = 0
        ifFalse = 0
    elif(line.startswith('  Starting')):
        sp = line.split(': ')[1]
        worries = worries + (list(map(lambda n: [int(n), monkeyOp], sp.split(', '))))
    elif(line.startswith('  Operation')):
        sp = line.split('old ')[1]
        op = sp[0]
        opNum = sp[2:]
    elif(line.startswith('  Test')):
        test = int(line.split('by ')[1])
        mods.append(test)
    elif('If true' in line):
        ifTrue = int(line.split('monkey ')[1])
    elif('If false' in line):
        ifFalse = int(line.split('monkey ')[1])
    else:
        ops.append(Op(op, opNum, test, ifTrue, ifFalse))
        counts.append(0)

ops.append(Op(op, opNum, test, ifTrue, ifFalse))
counts.append(0)


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

thingy = multiplyList(mods)

def inspect(monkey, item):
    num = 0
    if(monkey.opNum == 'old'):
        return (item * item) % thingy
    else:
        num = int(monkey.opNum)
    
    if(monkey.op == '*'):
        return (item * num)  % thingy
    elif(monkey.op == '+'):
        return (item + num) % thingy

def throw(monkey, item):
    if(item % monkey.test == 0):
        return monkey.testTrue
    else:
        return monkey.testFalse

def monkeyBiz(worry):
    originalItem = worry[0]
    originalOp = worry[1]
    counts[originalOp] += 1
    worry[0] = inspect(ops[originalOp], originalItem)
    worry[1] = throw(ops[originalOp], worry[0])

    if(worry[1] > originalOp):
        monkeyBiz(worry)



for worry in worries:
    for i in range(10000):
        monkeyBiz(worry)

    # counts[worry[1]] += 1

            

print(counts)
counts.sort()
print(counts)
print(counts[-1] * counts[-2])
