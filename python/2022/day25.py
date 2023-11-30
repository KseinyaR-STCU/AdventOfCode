from collections import defaultdict, deque
from methods import  read_data
import math

data = read_data('testdata.txt')
data = read_data('fulldata.txt')

def getMultiplier(c):
    match(c):
        case '2':
            return 2
        case '1':
            return 1
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2

total = 0

for line in data:
    length = len(line) - 1

    amount = 0

    for i, c in enumerate(line):
        pMax = getMultiplier(c) *  int( math.pow(5, length - i))
        amount += pMax
    
    total += amount
    amount = 0

## Copied off github cause I was close but oh so far
def modding(total):
    answer = '';
    while(total > 0):
        match(total % 5):
            case 0:
                answer = '0' + answer
            case 1:
                answer = '1' + answer
            case 2:
                answer = '2' + answer
            case 3:
                total += 5
                answer = '=' + answer
            case 4:
                total += 5
                answer = '-' + answer
        total = int(total / 5)
    
    return answer

print(total)
print('part 1')
print(modding(total))