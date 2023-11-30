from collections import defaultdict
from methods import  read_data

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

numbers = []
originals = []


class Number:
    def __init__(self, num, index):
        self.num = num
        self.index = index
        self.original = index
    
    def print(self):
        print(self.index, self.num)

for i, line in enumerate(data):
    thang = Number(int(line) * 811589153, i)
    originals.append(thang)
    numbers.append(thang)

maxLength = len(numbers)

def getNewIndex(i, n):
    newI = (i + n) % (maxLength - 1)

    return newI

for x in range(10):
    for i, n in enumerate(numbers):
        initialIndex = originals.index(n)
        newIndex = getNewIndex(initialIndex, n.num)
        originals.remove(n)
        originals.insert(newIndex, n)



# print()
# for o in originals:
#     o.print()

zero = originals.index([num for num in originals if num.num == 0][0])

first = (1000 + zero) % (maxLength  )
second = (2000 + zero) % (maxLength )
third = (3000 + zero) % (maxLength)

print(third)

fValue = originals[first].num
sValue = originals[second].num
tValue = originals[third].num

print(fValue, sValue, tValue)
print(fValue +  sValue + tValue)
