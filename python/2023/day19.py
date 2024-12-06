from methods import  read_data
from collections import defaultdict

data = read_data('in.tst')
data = read_data('in.txt')

class Workflow:
    def __init__(self, name, rules, default):
        self.name = name
        self.rules = rules
        self.default = default
    
    def print(self):
        print(self.name, self.default)
        for r in self.rules:
            r.print()
        print()

class Rule:
    def __init__(self, char, isGreater, amount, result):
        self.char = char
        self.isGreater = isGreater
        self.amount = amount
        self.result = result

    def print(self):
        print(self.char, self.isGreater, self.amount, self.result)

class Part:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def print(self):
        print(self.dictionary)
    
    def sum(self):
        return sum(list(self.dictionary.values()))


def parse_workflow(wline):
    sections = wline.split('{')
    name = sections[0]
    rules, default = parse_rules(sections[1])
    return Workflow(name, rules, default)

def parse_part(pline):
    sections = pline.strip('{').strip('}').split(',')
    dictionary = defaultdict(int)
    x, m, a, s = int(sections[0][2:]), int(sections[1][2:]), int(sections[2][2:]), int(sections[3][2:])
    dictionary['x'] = x
    dictionary['m'] = m
    dictionary['a'] = a
    dictionary['s'] = s
    return Part(dictionary)

def parse_rules(rline):
    sections = rline.strip('}').split(',')
    rules = []
    default = ''
    for s in sections:
        splits = s.split(':')
        if(len(splits) == 1):
            default = s
        else:
            isGreater = '>' in splits[0]
            num = 0
            if(isGreater):
                num = int(splits[0].split('>')[1])
            else:
                num = int(splits[0].split('<')[1])
            rules.append(Rule(splits[0][0], isGreater, num, splits[1]))

    return (rules, default)

workflows = defaultdict(Workflow)
parts = []

on_parts = False

for line in data:
    if(line.isspace()):
        on_parts = True
    elif(on_parts):
        parts.append(parse_part(line))
    else:
        pages = line.split('{')
        if(len(pages) == 2):
            w = parse_workflow(line)
            workflows[w.name] = w
        else:
            on_parts = True




# for p in workflows:
#     p.print()

def check_rule(part, rule):
    num = part.dictionary[rule.char]
    passes = False
    if(rule.isGreater):
        passes = num > rule.amount
    else:
        passes = num < rule.amount
    
    if(passes):
        return rule.result
    
    return ''


def run_workflow(part, name):
    flow = workflows[name]

    for r in flow.rules:
        result = check_rule(part, r)
        if(result == 'R'):
            return False
        elif(result == 'A'):
            return True
        elif(result != ''):
            return run_workflow(part, result)
    
    if(flow.default == 'R'):
        return False
    elif(flow.default == 'A'):
        return True
    else:
        return run_workflow(part, flow.default)

p1 = 0

for p in parts:
    res = run_workflow(p, 'in')
    if(res):
        p1 += p.sum()

print("part 1")
print(p1)