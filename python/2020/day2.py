from methods import read_data, read_udf_data, splitNumsOnSeparator

data = read_data('in.tst')
data = read_udf_data('in.txt')

p1 = 0
p2 = 0

for line in data:
    rules, passes = list(line.split(': '))

    minC = int(rules.split('-')[0])
    maxC = int(rules.split('-')[1].split()[0])
    character = rules.split()[1]

    passChar = passes.count(character)
    if( passChar >= minC and passChar <= maxC):
        p1 += 1

    if(passes[minC -1] == character and passes[maxC-1] != character) or (passes[minC-1] != character and passes[maxC-1] == character):
        p2 += 1
    

print("part 1")
print(p1)

print("part 2")
print(p2)